from typing import Optional, List
from pydantic import BaseModel


class AnalyzeProjectRequest(BaseModel):
    project_id: str
    text: str


from typing import Optional, Union

class Dimensions(BaseModel):
    length: Optional[Union[str, int, float]] = None
    width: Optional[Union[str, int, float]] = None


class ExtractedFields(BaseModel):
    project_type: Optional[str] = None
    location: Optional[str] = None
    dimensions: Optional[Dimensions] = None
    glass_type: Optional[str] = None
    finish: Optional[str] = None
    drawings_available: Optional[bool] = None
    load_requirements: Optional[str] = None
    special_conditions: Optional[str] = None


class AnalyzeProjectResponse(BaseModel):
    project_id: str
    extracted_fields: ExtractedFields
    missing_information: List[str]
    risk_level: str
    confidence_score: int
    follow_up_questions: List[str]
