# main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from scenarios import BUSINESS_SCENARIOS
from engine import evaluate_prompt

app = FastAPI(title="PromptCraft Enterprise API", version="1.0")

# Mount static folder for frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")

load_dotenv()  # Load environment variables from .env file

# Request schema supports an optional user-provided API key
class EvaluationRequest(BaseModel):
    scenario_id: str
    player_prompt: str
    api_key: str | None = None  # Optional client key


@app.get("/")
async def serve_index():
    """Serves the main web UI."""
    return FileResponse("static/index.html")


@app.get("/api/scenarios")
async def get_scenarios():
    """Returns all available scenarios."""
    return BUSINESS_SCENARIOS


@app.post("/api/evaluate")
async def process_evaluation(req: EvaluationRequest):
    """
    Evaluates a prompt against the CREATE framework.
    Uses the user's provided key if present; falls back to server .env key.
    """
    # 1. Fetch matching scenario
    scenario = next((s for s in BUSINESS_SCENARIOS if s["id"] == req.scenario_id), None)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

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
        result = evaluate_prompt(scenario["task"], req.player_prompt, effective_key)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
