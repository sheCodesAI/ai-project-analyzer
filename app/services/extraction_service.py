import json

from app.services.openai_service import call_openai
from app.services.prompt_builder import build_extraction_prompt


def extract_project_information(project_text: str) -> dict:
    """
    Extract structured project information using OpenAI.
    """

    prompt = build_extraction_prompt(project_text)

    ai_response = call_openai(prompt)

    # Remove markdown if present
    ai_response = ai_response.strip()

    if ai_response.startswith("```json"):
        ai_response = ai_response.replace("```json", "", 1)

    if ai_response.startswith("```"):
        ai_response = ai_response.replace("```", "", 1)

    if ai_response.endswith("```"):
        ai_response = ai_response[:-3]

    ai_response = ai_response.strip()

    try:
        return json.loads(ai_response)

    except json.JSONDecodeError:
        raise ValueError(
            "OpenAI returned invalid JSON. Please check the prompt or model response."
        )