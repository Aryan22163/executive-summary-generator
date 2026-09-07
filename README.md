# 📝 Executive Summary Generator

> **"Thinks like a McKinsey consultant, writes for the C-suite."**

Consultant-grade AI system powered by **Python, LangChain, and LangGraph**. Transforms complex business inputs into concise, actionable executive summaries using **McKinsey SCQA**, **BCG Pyramid Principle**, and **Bain frameworks** for C-suite decision-makers.

---

## 🧠 System Specifications

- **Name**: Executive Summary Generator
- **Theme Color**: Royal Purple (`#8B5CF6` / Obsidian `#090714`)
- **Emoji**: 📝
- **Word Target**: 500–600 words (≤ 650 max)
- **Reading Time**: < 3.5 minutes
- **Methodology**: 
  - **McKinsey SCQA**: Situation – Complication – Question – Answer
  - **BCG Pyramid Principle**: Top-down insight ordering & quantified findings
  - **Bain Action-Oriented Model**: Prioritized recommendations labeled [Critical / High / Medium] with Owner + Timeline + Expected Result

---

## 🏗️ Python LangChain & LangGraph Architecture

The backend is built as a stateful **LangGraph StateGraph** pipeline:

```
[Raw Business Input / Memo]
           │
           ▼
[Node 1: extract_metrics] ──► Extracts numeric metrics, percentages, dollar values
           │
           ▼
[Node 2: structure_pyramid] ──► McKinsey SCQA Situation Overview + BCG Pyramid Findings
           │
           ▼
[Node 3: synthesize_actions] ──► Bain Action Model (Priorities, Owners, Timelines, Results)
           │
           ▼
[Node 4: assemble_and_qa] ──► Word budget audit (325-475 words), metric density, reading speed
           │
   ┌───────┴───────┐
[Needs Refine]   [Compliant]
   │               │
   ▼               ▼
[Node 5: refine]  [C-Suite Deliverable JSON + Markdown]
```

### Backend Directory Structure
```
backend/
├── __init__.py
├── graph.py          # LangGraph StateGraph, nodes, and conditional edges
├── models.py         # Pydantic schemas (ConsultantState, Request/Response, Scorecard)
├── prompts.py        # System prompt & framework instructions
├── server.py         # FastAPI REST API (:8000)
└── requirements.txt  # FastAPI, Uvicorn, LangChain, LangGraph, Pydantic
```

---

## 🚀 Running the Full Stack Application

### 1. Start the Python LangGraph Backend (Port 8000)
```bash
# In project root:
source .venv/bin/activate
uvicorn backend.server:app --host 0.0.0.0 --port 8000
```
API Documentation will be accessible at: `http://localhost:8000/docs`

### 2. Start the Frontend Web UI (Port 3030)
```bash
python3 -m http.server 3030
```
Open `http://localhost:3030` in your web browser.

---

## 📊 Endpoints

- `GET /api/health`: Health status and engine metadata
- `GET /api/spec`: Agent personality, system prompt, and framework rules
- `POST /api/generate`: LangGraph execution endpoint:
  ```json
  {
    "topic": "B2B SaaS Net Retention Turnaround",
    "framework": "hybrid",
    "content": "Raw operational memos, transcripts, and financial figures...",
    "api_key": "optional-gemini-key"
  }
  ```
