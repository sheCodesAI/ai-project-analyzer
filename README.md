# AI Project Analyzer

An AI-powered FastAPI service that converts unstructured customer project notes into structured project information for proposal preparation.

The system uses an LLM for structured information extraction and combines it with rule-based validation to produce reliable and consistent results.

---

## Problem Statement

Estimators often receive project details through emails or customer notes that are incomplete and unstructured.

This service analyzes those project descriptions and extracts the key information required for preparing quotations and technical proposals.

---

## Features

- Extracts structured project information from unstructured text
- Identifies missing project details
- Generates follow-up questions for missing information
- Calculates project risk using rule-based logic
- Calculates confidence score using rule-based validation
- Returns structured JSON through a FastAPI endpoint

---

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn
- python-dotenv

---

## Project Structure

```text
ai-project-analyzer/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── services/
│   │   ├── extraction_service.py
│   │   ├── openai_service.py
│   │   ├── prompt_builder.py
│   │   ├── risk_service.py
│   │   ├── confidence_service.py
│   │   └── followup_service.py
│   └── utils/
│
├── tests/
├── README.md
├── requirements.txt
├── .env
└── .gitignore
```

---

## AI Pipeline

```text
Customer Project Notes
          │
          ▼
Prompt Builder
          │
          ▼
OpenAI API
          │
          ▼
Structured Information Extraction
          │
          ├──────────────► Missing Information Detection
          │
          ├──────────────► Follow-up Question Generation
          │
          ▼
Rule-Based Risk Assessment
          │
          ▼
Rule-Based Confidence Scoring
          │
          ▼
Structured JSON Response
```

---

## API Endpoint

### POST `/analyze-project`

### Request

```json
{
  "project_id": "P1001",
  "text": "Customer project description..."
}
```

### Response

Returns:

- Extracted project fields
- Missing information
- Risk level
- Confidence score
- Follow-up questions

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd ai-project-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Design Decisions

- Used an LLM only for structured information extraction.
- Implemented rule-based logic for risk assessment and confidence scoring to ensure consistent outputs.
- Kept prompt generation, OpenAI communication, extraction, and business logic in separate services for better maintainability.
- Returned missing information explicitly instead of allowing the model to guess unavailable values.

---

## Future Improvements

- Support PDF and scanned document processing using OCR.
- Add batch processing for multiple project documents.
- Store user feedback to continuously improve extraction quality.
- Add evaluation metrics to measure extraction accuracy.
- Containerize the application using Docker for easier deployment.
