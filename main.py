# main.py
import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from scenarios import BUSINESS_SCENARIOS
from engine import evaluate_prompt

load_dotenv()  # Load environment variables from .env file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("prompt_simulator")

app = FastAPI(title="PromptCraft Enterprise API", version="1.0")

# Rate limiting: keyed by client IP. Protects the server's own GROQ_API_KEY
# (used whenever a caller doesn't supply their own) from being drained by
# unauthenticated, repeated hits to /api/evaluate.
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Mount static folder for frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")


# Request schema supports an optional user-provided API key and an optional
# user-authored challenge. Length caps keep one request from burning an outsized
# number of tokens on the server's shared GROQ_API_KEY.
class EvaluationRequest(BaseModel):
    scenario_id: str = Field(max_length=100)
    player_prompt: str = Field(max_length=6000)
    api_key: str | None = Field(default=None, max_length=256)  # Optional client key
    # Task text for a custom challenge created in the browser. When present it
    # is used instead of looking up scenario_id in BUSINESS_SCENARIOS.
    custom_task: str | None = Field(default=None, max_length=1500)


@app.get("/")
async def serve_index():
    """Serves the main web UI."""
    return FileResponse("static/index.html")


@app.get("/api/scenarios")
async def get_scenarios():
    """Returns all available scenarios."""
    return BUSINESS_SCENARIOS


@app.post("/api/evaluate")
@limiter.limit("10/minute")
async def process_evaluation(req: EvaluationRequest, request: Request):
    """
    Evaluates a prompt against the CREATE framework.
    Uses the user's provided key if present; falls back to server .env key.
    """
    # 1. Resolve the challenge task: a custom challenge supplies its own task
    #    text; otherwise fetch the matching built-in scenario.
    if req.custom_task and req.custom_task.strip():
        scenario_task = req.custom_task.strip()
    else:
        scenario = next(
            (s for s in BUSINESS_SCENARIOS if s["id"] == req.scenario_id), None
        )
        if not scenario:
            raise HTTPException(status_code=404, detail="Scenario not found")
        scenario_task = scenario["task"]

    # 2. Resolve Key: User-provided key takes precedence over server .env
    effective_key = (
        req.api_key.strip()
        if (req.api_key and req.api_key.strip())
        else os.getenv("GROQ_API_KEY")
    )

    if not effective_key:
        raise HTTPException(
            status_code=400,
            detail="No API Key available. Provide your own Groq key or configure GROQ_API_KEY on the server.",
        )

    # 3. Process prompt with Groq
    try:
        result = evaluate_prompt(scenario_task, req.player_prompt, effective_key)
        return result
    except Exception:
        # Log the full error server-side; never forward internal exception
        # details (which may include API error text) to the client.
        logger.exception(
            "Evaluation failed for scenario_id=%s", req.scenario_id
        )
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while evaluating your prompt. Please try again.",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
