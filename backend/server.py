"""
FastAPI Backend Server for Executive Summary Generator.
Exposes LangGraph workflow via REST API.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from backend.models import (
    GenerateRequest,
    GenerateResponse,
    ConsultantState,
)
from backend.graph import consultant_graph
from backend.prompts import EXECUTIVE_CONSULTANT_SYSTEM_PROMPT

from fastapi.responses import FileResponse

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="Executive Summary Generator API",
    description="Consultant-grade C-Suite AI powered by LangChain and LangGraph",
    version="1.0.0",
)

# Enable CORS for cross-origin or local clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Serve Frontend Web Application for Render Deployment ---
@app.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
async def serve_index():
    index_file = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Executive Summary Generator API is running."}


@app.api_route("/style.css", methods=["GET", "HEAD"], include_in_schema=False)
async def serve_css():
    css_file = os.path.join(BASE_DIR, "style.css")
    if os.path.exists(css_file):
        return FileResponse(css_file, media_type="text/css")
    raise HTTPException(status_code=404, detail="style.css not found")


@app.api_route("/app.js", methods=["GET", "HEAD"], include_in_schema=False)
async def serve_js():
    js_file = os.path.join(BASE_DIR, "app.js")
    if os.path.exists(js_file):
        return FileResponse(js_file, media_type="application/javascript")
    raise HTTPException(status_code=404, detail="app.js not found")


@app.api_route("/api/health", methods=["GET", "HEAD"])
def health_check():
    """Returns backend status and LangGraph engine details."""
    return {
        "status": "operational",
        "engine": "LangGraph + LangChain",
        "version": "1.0.0",
        "frameworks": ["McKinsey SCQA", "BCG Pyramid Principle", "Bain Action Model"],
        "word_budget": "500-600 words (<= 650 max)",
        "reading_time": "< 3.5 minutes",
    }


@app.get("/api/spec")
def get_agent_spec():
    """Returns full agent personality and system prompt."""
    return {
        "name": "Executive Summary Generator",
        "role": "Senior Strategy Consultant & Executive Communication Specialist",
        "color": "#8B5CF6",
        "emoji": "📝",
        "vibe": "Thinks like a McKinsey consultant, writes for the C-suite.",
        "system_prompt": EXECUTIVE_CONSULTANT_SYSTEM_PROMPT,
    }


@app.post("/api/generate", response_model=GenerateResponse)
def generate_summary(req: GenerateRequest):
    """Executes the 4-step LangGraph pipeline to synthesize an executive summary."""
    if not req.content or not req.content.strip():
        raise HTTPException(status_code=400, detail="Business content cannot be empty.")

    api_key = req.api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    hf_api_key = req.hf_api_key or os.getenv("HUGGINGFACE_API_KEY") or os.getenv("HF_TOKEN")
    hf_model = req.hf_model or os.getenv("HUGGINGFACE_MODEL") or "meta-llama/Llama-3.3-70B-Instruct"

    # Initial state
    initial_state = ConsultantState(
        topic=req.topic or "Enterprise Strategic Initiative",
        framework=req.framework or "hybrid",
        raw_content=req.content,
        api_key=api_key,
        model_name=req.model_name or "gemini-1.5-flash",
        hf_api_key=hf_api_key,
        hf_model=hf_model,
    )

    try:
        # Run through LangGraph
        result_dict = consultant_graph.invoke(initial_state)

        # Build response
        response = GenerateResponse(
            topic=result_dict.get("topic", req.topic),
            framework=result_dict.get("framework", req.framework),
            situation_overview=result_dict.get("situation_overview", ""),
            findings=result_dict.get("findings", []),
            business_impact=result_dict.get("business_impact"),
            recommendations=result_dict.get("recommendations", []),
            next_steps=result_dict.get("next_steps", []),
            decision_point=result_dict.get("decision_point"),
            final_markdown=result_dict.get("final_markdown", ""),
            qa_scorecard=result_dict.get("qa_scorecard"),
            pipeline_steps_completed=result_dict.get("pipeline_steps_completed", []),
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LangGraph execution error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.server:app", host="0.0.0.0", port=port, reload=False)
