# 📝 AI CONSULTANT

> **"Thinks like a McKinsey consultant, writes for the C-suite."**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-purple.svg)](https://github.com/langchain-ai/langgraph)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-emerald.svg)](https://github.com/langchain-ai/langchain)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-teal.svg)](https://fastapi.tiangolo.com)
[![Hugging Face](https://img.shields.io/badge/Open%20Source-Hugging%20Face-yellow.svg)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A consultant-grade AI system engineered to transform messy operational reports, financial statements, meeting transcripts, and strategic documents into concise, quantified, action-oriented executive summaries tailored for C-suite decision-makers and boards of directors.

---

## 📌 Table of Contents

- [What is Executive Summary Generator?](#-what-is-executive-summary-generator)
- [Why It Matters: The Problem It Solves](#-why-it-matters-the-problem-it-solves)
- [How It Is Helpful: Value Proposition & Impact](#-how-it-is-helpful-value-proposition--impact)
- [Consulting Frameworks & Methodology](#-consulting-frameworks--methodology)
- [The 5 Strict Output Sections](#-the-5-strict-output-sections)
- [C-Suite Compliance & QA Audit (Step 4)](#-c-suite-compliance--qa-audit-step-4)
- [System Architecture (LangGraph StateGraph)](#-system-architecture-langgraph-stategraph)
- [Multi-Model & Open Source Support](#-multi-model--open-source-support)
- [4 Interactive C-Suite Views](#-4-interactive-c-suite-views)
- [Quickstart & Installation](#-quickstart--installation)
- [API Reference](#-api-reference)
- [Enterprise Case Studies Preloaded](#-enterprise-case-studies-preloaded)

---

## 🔍 What is Executive Summary Generator?

**Executive Summary Generator** is a senior strategy consulting specialist encoded into a stateful AI agent graph. It combines the rigorous analytical methodologies of the world's leading management consultancies:

- **McKinsey & Company**: SCQA narrative framework (Situation – Complication – Question – Answer)
- **Boston Consulting Group (BCG)**: Pyramid Principle and top-down insight ordering
- **Bain & Company**: Action-oriented recommendation matrix with strict ownership and accountability

Rather than generating generic summaries or bulleted overviews, this system extracts every quantitative metric, calculates exposure, bolds strategic implications, and structures prioritized initiatives that enable executives to grasp the situation and make confident capital allocation decisions in **under 3.5 minutes**.

---

## ⚡ Why It Matters: The Problem It Solves

Modern corporate leadership is inundated with data:
- **50+ page operational reviews**, complex audit reports, and multi-tab financial spreadsheets.
- **Narrative ambiguity**: Team updates frequently describe activities rather than business impact.
- **Missing quantification**: Claims lack comparative benchmarks or financial stakes.
- **Unclear ownership**: Recommendations often lack explicit deadlines, designated owners, and measurable outcomes.
- **Executive scanning friction**: CEOs and board members read at ~200 words per minute and typically have less than 5 minutes between committee meetings.

**Executive Summary Generator** eliminates this friction by enforcing Fortune 500 consultant standards on every document processed.

---

## 💡 How It Is Helpful: Value Proposition & Impact

| Capability | What It Does | Tangible Benefit to Leadership |
| :--- | :--- | :--- |
| **Brevity & Word Budget** | Calibrates output strictly to **500–600 words** (≤ 650 max ceiling). | Ensures complete read time is **< 3.5 minutes**, respecting executive time. |
| **100% Metric Density** | Mandates ≥ 1 quantified or comparative data point per finding (`$`, `%`, ratios). | Eliminates vague qualitative fluff; every finding is backed by data. |
| **Bold Strategic Implications** | Formats strategic impacts as `**Strategic implication: [Impact]**`. | Allows C-suite scanning in under 60 seconds during high-stakes reviews. |
| **Bain Action Accountability** | Assigns `[Critical / High / Medium]` priority, explicit **Owner**, **Timeline**, and **Expected Result**. | Guarantees clear accountability and eliminates ambiguity on who delivers what. |
| **Immediate Next Steps** | Identifies 2–3 actions (≤ 30-day horizon) plus an explicit **Decision Point** with deadline. | Accelerates execution velocity and provides immediate committee voting clarity. |
| **Multi-Format Deliverables** | Produces a formal Confidential Memo, 16:9 Board Slide, Action Matrix, and Audit Scorecard. | Ready for boardroom presentations, executive committee packets, or Slack/email briefs. |

---

## 📐 Consulting Frameworks & Methodology

### 1. McKinsey SCQA Framework
- **Situation**: Contextualizes what is currently happening and establishes the operational baseline.
- **Complication**: Identifies the operational drag, cost inflation, or market bottleneck causing performance to diverge.
- **Question**: Pinpoints the strategic question confronting senior leadership.
- **Answer**: Outlines the decisive strategic resolution.

### 2. BCG Pyramid Principle
- **Governing Thought / Answer First**: Leads with the primary high-impact conclusion before supporting details.
- **Hierarchical Grouping**: Organizes insights logically by descending order of business impact.
- **Mutually Exclusive, Collectively Exhaustive (MECE)**: Ensures findings cover key strategic pillars without redundant overlap.

### 3. Bain Action-Oriented Model
- **Prioritization**: Categorized as `[Critical]`, `[High]`, or `[Medium]` based on risk and value creation potential.
- **Owner Accountability**: Assigned to specific C-suite roles (COO, CFO, CTO, VP).
- **Time-Bound**: Concrete delivery windows (30-day sprint, 45-day governance, 60-day consolidation).
- **Measurable Result**: Quantified targets (e.g., *"Reduce cycle times by 40% and halt mid-market churn"*).

---

## 📋 The 5 Strict Output Sections

Every generated summary adheres to this calibrated structure:

```markdown
# Executive Summary: [Initiative Title]

## 1. SITUATION OVERVIEW [75–100 words]
[Current state context, operational baseline, and the critical gap between authorized budget and actual execution.]

## 2. KEY FINDINGS [200–250 words]
**Finding 1**: [Quantified operational throughput]. **Strategic implication: [Impact on valuation & revenue].**
**Finding 2**: [Comparative unit economics metric]. **Strategic implication: [Impact on capital runway].**
**Finding 3**: [Process drag or infrastructure figure]. **Strategic implication: [Impact on market share].**
**Finding 4**: [Resilient cohort benchmark]. **Strategic implication: [Impact on margin recovery].**

## 3. BUSINESS IMPACT [80–110 words]
**Financial Impact**: [Quantified exposure with $ and % figures]
**Risk/Opportunity**: [Probability of covenant breach or upside realization]
**Time Horizon**: [Specific realization timeline (90-day stabilization, 6-12 month synergy)]

## 4. RECOMMENDATIONS [110–140 words]
**[Critical]**: [Action] — Owner: [Role] | Timeline: [Specific dates] | Expected Result: [Quantified target]
**[High]**: [Action] — Owner: [Role] | Timeline: [Specific dates] | Expected Result: [Quantified target]
**[Medium]**: [Action] — Owner: [Role] | Timeline: [Specific dates] | Expected Result: [Quantified target]

## 5. NEXT STEPS [40–60 words]
1. **[Immediate action 1]** — Deadline: [Within 14 business days]
2. **[Immediate action 2]** — Deadline: [Within 30 business days]
**Decision Point**: [Explicit board approval required] by [Specific deadline]
```

---

## 🔍 C-Suite Compliance & QA Audit (Step 4)

The platform features an automated **C-Suite QA Inspector & Scorecard** that evaluates every generated summary across 6 rigor dimensions:

1. **Word Budget Calibration**: Checks against the **500–600 word optimal window** (with a ≤ 650 word ceiling).
2. **Quantified Data Point Density**: Requires 100% of key findings to include numeric data points.
3. **Bold Strategic Implications**: Verifies presence of bolded strategic implications.
4. **Recommendation Completeness**: Ensures all recommendations possess Priority, Owner, Timeline, and Measurable Deliverable.
5. **Next Steps & Decision Deadline**: Validates immediate 30-day horizon steps and explicit Decision Point.
6. **Executive Reading Speed**: Measures reading time against the < 3.5 minute target.

---

## 🏗️ System Architecture (LangGraph StateGraph)

The backend is built as a stateful **LangGraph StateGraph** pipeline running on Python 3.12 and FastAPI:

```
[Raw Business Input / Memo]
           │
           ▼
[Node 1: extract_metrics] ─────► Extracts numbers, percentages, currencies, timelines
           │
           ▼
[Node 2: structure_pyramid] ───► McKinsey SCQA Situation Overview (75–100w)
           │                     + BCG Pyramid Key Findings (200–250w) with bold implications
           ▼
[Node 3: synthesize_actions] ──► Business Impact (80–110w)
           │                     + Bain Action Recommendations (110–140w)
           │                     + Next Steps & Decision Point (40–60w)
           ▼
[Node 4: assemble_and_qa] ─────► Assembles brief, audits word budget & metric density
           │
   ┌───────┴───────┐
[Out of Range]   [Compliant]
   │               │
   ▼               ▼
[Node 5: refine] [C-Suite Deliverable (JSON + Markdown)]
```

### Directory Layout
```
├── backend/
│   ├── __init__.py
│   ├── graph.py          # LangGraph StateGraph, nodes, and conditional edges
│   ├── models.py         # Pydantic schemas (ConsultantState, Request/Response, Scorecard)
│   ├── prompts.py        # System prompt & framework templates
│   ├── server.py         # FastAPI REST server (:8000)
│   └── requirements.txt  # FastAPI, LangChain, LangGraph, Hugging Face Hub
├── index.html            # Consultant-grade web app structure
├── style.css             # Royal purple & obsidian design system
├── app.js                # Frontend state, client engine, and Step 4 QA auditor
├── system_prompt.md      # Full agent personality specification
├── .env.example          # Environment variable template
└── README.md             # Project documentation
```

---

## 🤖 Multi-Model & Open Source Support

The system can run in three flexible modes:

1. **Hugging Face Open Source LLMs (Serverless Inference)**:
   - Connect your free or pro Hugging Face API Token (`hf_...`)
   - Supported models:
     - `meta-llama/Llama-3.3-70B-Instruct` (Recommended for complex strategy analysis)
     - `meta-llama/Meta-Llama-3-8B-Instruct` (Fast inference)
     - `mistralai/Mistral-7B-Instruct-v0.3`
     - `Qwen/Qwen2.5-72B-Instruct`
     - `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
2. **Google Gemini API**:
   - Connect your Gemini API Key for Gemini 1.5 Flash / 2.0.
3. **Built-in Enterprise Heuristic Engine**:
   - Fully offline, deterministic, zero-latency execution directly via LangGraph without requiring any API keys.

---

## 📊 4 Interactive C-Suite Views

The frontend provides 4 specialized perspective tabs:

- 📄 **Executive Memo**: Confidential board briefing document formatted with classic Newsreader serif typography.
- 📊 **Board Slide Preview**: 16:9 widescreen presentation slide complete with KPI badges and key takeaways.
- 📋 **Bain Action Matrix**: Sortable table of Priorities, Strategic Actions, Executive Owners, Timelines, and Expected Outcomes.
- 🔍 **C-Suite QA Scorecard**: Visual compliance dashboard displaying audit scores and pass/fail badges.

---

## 🚀 Quickstart & Installation

### Prerequisites
- Python 3.12+
- `uv` (recommended) or standard `python3-venv`

### 1. Clone the Repository
```bash
git clone https://github.com/Aryan22163/executive-summary-generator.git
cd executive-summary-generator
```

### 2. Setup Python Virtual Environment & Install Dependencies
```bash
# Using uv (blazing fast):
uv venv
source .venv/bin/activate
uv pip install -r backend/requirements.txt

# Or using standard pip:
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 3. (Optional) Configure API Keys
Copy the example environment file:
```bash
cp .env.example .env
```
Add your Hugging Face or Gemini API keys if you wish to use frontier LLMs:
```env
HUGGINGFACE_API_KEY=hf_your_token_here
HUGGINGFACE_MODEL=meta-llama/Llama-3.3-70B-Instruct
```

### 4. Start the Application

**Terminal 1 — Start Python LangGraph Backend (Port 8000)**:
```bash
source .venv/bin/activate
uvicorn backend.server:app --host 0.0.0.0 --port 8000 --reload
```
*API documentation is available at `http://localhost:8000/docs`.*

**Terminal 2 — Start Frontend Server (Port 3030)**:
```bash
python3 -m http.server 3030
```
Open **`http://localhost:3030`** in your browser.

---

## 📡 API Reference

### Health Check
```http
GET /api/health
```
**Response**:
```json
{
  "status": "operational",
  "engine": "LangGraph + LangChain",
  "version": "1.0.0",
  "frameworks": ["McKinsey SCQA", "BCG Pyramid Principle", "Bain Action Model"],
  "word_budget": "500-600 words (<= 650 max)",
  "reading_time": "< 3.5 minutes"
}
```

### Generate Executive Summary
```http
POST /api/generate
Content-Type: application/json
```
**Request Body**:
```json
{
  "topic": "B2B SaaS Net Retention Turnaround",
  "framework": "hybrid",
  "content": "Raw operational memos, quarterly figures, customer churn data...",
  "hf_api_key": "optional_hf_token",
  "hf_model": "meta-llama/Llama-3.3-70B-Instruct"
}
```
**Response**:
```json
{
  "topic": "B2B SaaS Net Retention Turnaround",
  "framework": "hybrid",
  "situation_overview": "...",
  "findings": [...],
  "business_impact": {...},
  "recommendations": [...],
  "next_steps": [...],
  "decision_point": {...},
  "final_markdown": "# Executive Summary...",
  "qa_scorecard": {
    "word_count": 595,
    "word_count_status": "optimal",
    "reading_time_minutes": 3.1,
    "data_density_pct": 100,
    "overall_compliance_score": 100,
    "certification_status": "C-Suite Certified"
  }
}
```

---

## 📂 Enterprise Case Studies Preloaded

The application includes 4 preloaded enterprise scenarios to test immediately:

1. **B2B SaaS Churn Crisis**: Addressing NRR drops from 114% to 89% and CAC payback extending to 28.5 months across mid-market tiers.
2. **Cloud Infrastructure Cost Overrun**: Taming a 43% overrun ($18.4M spend) through automated compute rightsizing and reserved instance optimization.
3. **Supply Chain Shock**: Mitigating 29-week semiconductor lead times and releasing $22M in stranded inventory via North American dual-sourcing.
4. **HealthTech M&A Commercial Integration**: Capturing stalled post-merger EBITDA synergies ($48M target) across enterprise hospital networks.

---

## ☁️ Deploying to Render (render.com)

The project is architected to run on Render as a **single unified Web Service** (serving both the FastAPI LangGraph backend and the frontend UI) with **zero CORS configuration** needed, fitting seamlessly within Render's Free tier.

### Method 1: Deploy via Render Blueprint (Recommended — 1 Click)

1. Log into your [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** in the top right corner and select **Blueprint**.
3. Connect your GitHub repository:
   ```
   https://github.com/Aryan22163/executive-summary-generator
   ```
4. Render will automatically detect the [`render.yaml`](render.yaml) specification:
   - **Service Type**: Web Service
   - **Runtime**: Python 3.12
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.server:app --host 0.0.0.0 --port $PORT`
5. *(Optional)* Add your `HUGGINGFACE_API_KEY` or `GEMINI_API_KEY` under Environment Variables.
6. Click **Apply**. Your app will build and deploy with a live public URL (e.g., `https://executive-summary-generator.onrender.com`).

---

### Method 2: Manual Web Service Setup on Render

If configuring manually without Blueprints:

1. Click **New +** -> **Web Service** in your Render dashboard.
2. Select your repository: `Aryan22163/executive-summary-generator`.
3. Configure the following settings:
   | Setting | Value |
   |---|---|
   | **Name** | `executive-summary-generator` |
   | **Region** | `Oregon (US West)` or nearest |
   | **Branch** | `main` |
   | **Runtime** | `Python` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `uvicorn backend.server:app --host 0.0.0.0 --port $PORT` |
   | **Instance Type** | `Free` |

4. Under **Environment Variables**, add:
   - `PYTHON_VERSION` = `3.12.0`
   - *(Optional)* `HUGGINGFACE_API_KEY` = your HF token
   - *(Optional)* `HUGGINGFACE_MODEL` = `meta-llama/Llama-3.3-70B-Instruct`
   - *(Optional)* `GEMINI_API_KEY` = your Google Gemini key

5. Click **Create Web Service**.

> [!TIP]
> **Zero Key Requirement**: The app includes a built-in deterministic fallback consultant engine that operates 100% offline without needing API keys. Adding API keys unlocks frontier open-source LLMs (Llama 3.3 70B, Mistral, Qwen, DeepSeek). Users can also enter API keys directly into the UI modal at runtime!

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
