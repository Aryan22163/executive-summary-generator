"""
Data models and state schemas for the Executive Summary Generator.
Uses Pydantic V2.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Finding(BaseModel):
    num: int
    insight: str
    implication: str


class BusinessImpact(BaseModel):
    financial: str
    risk: str
    horizon: str


class Recommendation(BaseModel):
    priority: str = Field(description="Critical, High, or Medium")
    action: str
    owner: str
    timeline: str
    result: str


class NextStep(BaseModel):
    action: str
    deadline: str


class DecisionPoint(BaseModel):
    decision: str
    deadline: str


class QAScorecard(BaseModel):
    word_count: int
    word_count_status: str  # optimal, acceptable, out_of_range
    reading_time_minutes: float
    data_density_pct: int
    bold_implications_count: int
    recommendations_complete_count: int
    overall_compliance_score: int  # 0 - 100
    certification_status: str  # C-Suite Certified, High Quality, Needs Tuning
    audit_notes: List[str] = Field(default_factory=list)


# --- Request and Response Schemas for FastAPI ---
class GenerateRequest(BaseModel):
    topic: str = Field(default="Enterprise Strategic Initiative", description="Initiative Title")
    framework: str = Field(default="hybrid", description="hybrid, scqa, pyramid, or bain")
    content: str = Field(description="Raw business data, memos, or transcripts")
    api_key: Optional[str] = Field(default=None, description="Optional Google Gemini API Key")
    model_name: Optional[str] = Field(default="gemini-1.5-flash", description="Gemini model name")
    hf_api_key: Optional[str] = Field(default=None, description="Hugging Face Open Source API Token")
    hf_model: Optional[str] = Field(default="meta-llama/Llama-3.3-70B-Instruct", description="Hugging Face model ID")


class GenerateResponse(BaseModel):
    topic: str
    framework: str
    situation_overview: str
    findings: List[Finding]
    business_impact: BusinessImpact
    recommendations: List[Recommendation]
    next_steps: List[NextStep]
    decision_point: DecisionPoint
    final_markdown: str
    qa_scorecard: QAScorecard
    pipeline_steps_completed: List[str] = Field(default_factory=list)


# --- LangGraph State Schema ---
class ConsultantState(BaseModel):
    topic: str
    framework: str
    raw_content: str
    api_key: Optional[str] = None
    model_name: Optional[str] = "gemini-1.5-flash"
    hf_api_key: Optional[str] = None
    hf_model: Optional[str] = "meta-llama/Llama-3.3-70B-Instruct"

    # Extracted data
    extracted_metrics: List[str] = Field(default_factory=list)

    # Generated components
    situation_overview: str = ""
    findings: List[Finding] = Field(default_factory=list)
    business_impact: Optional[BusinessImpact] = None
    recommendations: List[Recommendation] = Field(default_factory=list)
    next_steps: List[NextStep] = Field(default_factory=list)
    decision_point: Optional[DecisionPoint] = None

    # Assembly & QA
    final_markdown: str = ""
    qa_scorecard: Optional[QAScorecard] = None
    iteration_count: int = 0
    needs_refinement: bool = False
    pipeline_steps_completed: List[str] = Field(default_factory=list)
