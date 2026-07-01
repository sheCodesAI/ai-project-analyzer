from fastapi import FastAPI

from app.models import (
    AnalyzeProjectRequest,
    AnalyzeProjectResponse,
    ExtractedFields,
)
from app.services.extraction_service import extract_project_information
from app.services.risk_service import calculate_risk
from app.services.confidence_service import calculate_confidence

app = FastAPI(
    title="AI Project Analyzer API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Project Analyzer API is running!"
    }


@app.post("/analyze-project", response_model=AnalyzeProjectResponse)
def analyze_project(request: AnalyzeProjectRequest):

    result = extract_project_information(request.text)

    missing_information = result.get("missing_information", [])

    # Calculate using our own logic
    risk_level = calculate_risk(missing_information)
    confidence_score = calculate_confidence(
        request.text,
        missing_information
    )

    return AnalyzeProjectResponse(
        project_id=request.project_id,
        extracted_fields=ExtractedFields(**result["extracted_fields"]),
        missing_information=missing_information,
        risk_level=risk_level,
        confidence_score=confidence_score,
        follow_up_questions=result.get("follow_up_questions", []),
    )