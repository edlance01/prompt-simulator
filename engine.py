# engine.py
import json
import os
from groq import Groq

EVALUATOR_SYSTEM_PROMPT = """
You are an AI Prompt Engineering Coach evaluating a prompt against Microsoft's CREATE framework:
- C: Character (Assigned role/persona)
- R: Request (Clear main task)
- E: Examples (Sample inputs or output structures)
- A: Adjustments (Tone, style, or reading level)
- T: Type of Output (Format like bullets, table, email)
- E: Extras / Constraints (Negative constraints, word limits, audience)

Your Task:
1. Grade the prompt (0-100).
2. Identify missing CREATE elements.
3. Provide constructive feedback.
4. Generate a 'Simulated Response' demonstrating what the user's prompt actually outputs.

Respond strictly in valid JSON using this format:
{
  "score": 85,
  "detected_elements": ["Character", "Request", "Type"],
  "missing_elements": ["Examples", "Adjustments", "Extras"],
  "feedback": "Clear task and format! Add a target tone (Adjustments) and length limit (Extras).",
  "simulated_output": "The actual text produced by the player's prompt..."
}
"""


def evaluate_prompt(scenario_task: str, player_prompt: str, api_key: str) -> dict:
    client = Groq(api_key=api_key)

    user_payload = f"""
    [SCENARIO TASK]: {scenario_task}
    [PLAYER PROMPT]: {player_prompt}
    """

    # When paid use llama-3.1-8b-instant (Fast, stable, and universal across all Groq accounts)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": EVALUATOR_SYSTEM_PROMPT},
            {"role": "user", "content": user_payload},
        ],
        response_format={"type": "json_object"},
    )

    return json.loads(response.choices[0].message.content)
