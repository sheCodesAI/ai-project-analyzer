def build_extraction_prompt(project_text: str) -> str:
    return f"""
You are an AI assistant that extracts structured information from customer project notes.

Analyze the project description and return ONLY valid JSON.

Rules:
- Do not guess missing information.
- Use null if information is unavailable.
- Return only valid JSON.
- Do not add explanations, markdown, or extra text.
- Do not make engineering decisions.
- Do NOT calculate risk level.
- Do NOT calculate confidence score.
- Only extract factual information present in the input.

Return the JSON in exactly this structure:

{{
  "extracted_fields": {{
    "project_type": null,
    "location": null,
    "dimensions": {{
      "length": null,
      "width": null
    }},
    "glass_type": null,
    "finish": null,
    "drawings_available": null,
    "load_requirements": null,
    "special_conditions": null
  }},
  "missing_information": [],
  "follow_up_questions": []
}}

Project Description:

{project_text}
"""