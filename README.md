# MCM-Killer: Autonomous Multi-Agent System for MCM/ICM Competitions

> **Project Goal**: A fully autonomous AI system that solves mathematical modeling competitions from problem PDF to final paper

---

> [!WARNING]
> **⚠️ IMPORTANT: READ BEFORE USING**
>
> - This is a **RESEARCH PROTOTYPE** - results are unreliable
> - AI-generated content **MUST be thoroughly verified** by humans
> - You **MUST disclose AI use** per competition rules
> - You are **SOLELY RESPONSIBLE** for submitted content
> - Developers provide **NO WARRANTY**
>
> See sections below for details.

---

## What is MCM-Killer?

**MCM-Killer is a fully autonomous AI system** - not a tool or framework you need to manually operate.

### The Simple Workflow

```
You provide:
  ↓
Problem PDF + Data Files
  ↓
[AI System Works Automatically]
  - 13 AI agents collaborate
  - Design models, write code, create figures, write paper
  - 10-phase workflow with 7 strict validation gates
  ↓
You receive:
  ↓
Complete LaTeX paper + Summary Sheet
  ↓
You verify and submit
```

### What You Need to Do

**Step 1**: Prepare your problem PDF and data files
**Step 2**: Run the system
**Step 3**: Wait for completion
**Step 4**: Review the generated paper (human verification required)
**Step 5**: Submit to competition (with AI use disclosure)

**That's it.** The AI handles everything else.

---

## How It Works: The 13-Agent AI System

MCM-Killer uses **13 specialized AI agents** that work together autonomously in a strict pipeline:

| Agent | Role | What It Does |
|-------|------|--------------|
| **Reader** | Problem Analyst | Extracts requirements from PDF (using Docling) |
| **Researcher** | Strategy Advisor | Brainstorms mathematical methods & innovation |
| **Modeler** | Mathematical Architect | Designs formal models with equations |
| **Feasibility Checker** | Implementation Gatekeeper | Evaluates technical/time feasibility |
| **Data Engineer** | Data Pipeline Specialist | Creates features from raw data |
| **Code Translator** | Math-to-Code Translator | Converts mathematical models to Python |
| **Model Trainer** | Model Training Specialist | Trains models and generates results |
| **Validator** | Quality Gatekeeper | Independent multi-perspective verification |
| **Visualizer** | Graphics Designer | Creates publication-quality figures |
| **Writer** | Paper Author | Writes LaTeX paper |
| **Summarizer** | Summary Expert | Creates 1-page summary sheet |
| **Editor** | Language Polisher | Fixes grammar and style |
| **Advisor** | Faculty Reviewer | Final O-Prize level quality control |

### The AI Workflow (Automatic - 10-Phase Pipeline)

The AI agents follow a strict pipeline workflow with 7 mandatory quality gates:

```
PHASE 0: Problem Understanding
  Reader → extracts requirements
  Researcher → proposes methods

PHASE 1: Model Design (Gate 1)
  Modeler → designs mathematical models
  └─ Validation Gate MODEL: Checked by Reader, Feasibility, Advisor, Researcher

PHASE 2: Feasibility Check
  Feasibility Checker → confirms technical viability

PHASE 3: Data Processing (Gate 2)
  Data Engineer → creates features
  └─ Validation Gate DATA: Checked by Modeler, Validator, Reader

PHASE 4: Code Translation (Gate 3)
  Code Translator → translates math to Python
  └─ Validation Gate CODE: Checked by Modeler, Code Translator, Feasibility

PHASE 5: Model Training (Gate 4)
  Model Trainer → generates results
  └─ Validation Gate TRAINING: Checked by Modeler, Code Translator, Validator, Reader

PHASE 6: Visualization
  Visualizer → creates figures

PHASE 7: Paper Writing (Gate 5)
  Writer → writes LaTeX paper
  └─ Validation Gate PAPER: Checked by Reader, Validator, Advisor, Writer

PHASE 8: Summary (Gate 6)
  Summarizer → creates summary sheet
  └─ Validation Gate SUMMARY: Checked by Validator, Reader

PHASE 9: Polish (Gate 7)
  Editor → polishes language
  └─ Validation Gate FINAL: Checked by Validator, Advisor, Reader

PHASE 10: Final Review
  Advisor → final O-Prize assessment
```

### Key Quality Mechanisms (v2.4.0)

**1. Multi-Participant Validation**
Each validation gate involves **multiple agents** checking from different perspectives (e.g., Reader checks compliance, Validator checks data integrity, Advisor checks innovation). No "rubber stamping" allowed.

**2. Strict Rework Mechanism**
- **"Rework does not exempt verification"**: Reworked outputs must pass the same high standards.
- **Maximum 3 reworks** per gate before escalation.
- **Backtracking**: Serious issues trigger fallback to earlier phases (e.g., failed training -> redesign model).

**3. Data Authority Hierarchy**
1. **Level 1 (Highest)**: Code Execution Outputs (CSV/PKL)
2. **Level 2**: Agent Reports
3. **Level 3**: Paper/Summary (Drafts)
*Paper must always match CSV. If they differ, the Paper is wrong.*

**4. Global Version Control**
- All files use explicit versioning: `{name}_{i}.{ext}`
- `VERSION_MANIFEST.json` tracks everything
- No "final", "backup", or "old" filenames allowed

---

## System Architecture

### Directory Structure

```
output/
├── VERSION_MANIFEST.json    # Single Source of Truth for versions
├── problem/                 # Problem files & requirements
├── docs/                    # Collaboration documents
│   ├── consultation/        # Agent-to-Agent inquiries
│   ├── validation/          # Multi-agent validation reports
│   └── report/              # Agent execution reports
├── model/                   # Mathematical model designs
├── implementation/          # Code & Data
│   ├── .venv/               # Isolated Python environment
│   ├── data/                # CSVs, PKLs
│   └── code/                # Python scripts
└── paper/                   # Final deliverables
    ├── figures/             # Figures
    └── summary/             # Summary sheet
```

### Collaboration Contracts

- **Consultation**: Blocking, file-based inquiries. Agents ask before guessing.
- **Validation**: Independent, parallel assessment. No consultation allowed during validation.
- **Report**: Mandatory reporting to Director after every task.

---

## Quick Start

### Prerequisites

- **Python 3.10+**
- **Claude Code CLI** (Latest)
- **Docling MCP Server** (for accurate PDF reading)
- **LaTeX** (optional, for PDF compilation)

### Installation (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/hlife0/MCM-Killer.git
cd MCM-Killer

# 2. Navigate to the workspace
cd workspace/2025_C

# 3. Prepare your files
# Place your problem.pdf and data.zip in this directory

# 4. Run Claude Code
claude
```

### Running the System

Inside Claude Code, simply tell it:

```
Read CLAUDE.md and run the multi-agent workflow to solve this MCM problem.
```

---

## What's New in v2.4.0

**Complete Architecture Redesign - Self-Consistent Specification Layer**

v2.4.0 is a major architectural overhaul focused on creating a "single source of truth" for system design.

### Key Changes
- **Authoritative Architecture**: `architectures/v2-4-0/architecture.md` defines all rules.
- **Multi-Participant Validation**: Gates now involve 2-4 independent validators.
- **Structured Collaboration**: Formal contracts for Consultation, Validation, and Reporting.
- **10-Phase Workflow**: Expanded pipeline with explicit feasibility checks and polishing steps.
- **Global Versioning**: Unified version counter `{i}` for all artifact types.
- **New Directory Structure**: `output/docs/` centralizes collaboration history.

---

## Disclaimer & Liability

### Research-Only Status

**This project is a research prototype.**
- ❌ NOT production-ready
- ❌ NOT guaranteed to produce correct results
- ✅ For research and educational purposes only

### Your Responsibility

By using this system, you agree that **you are solely responsible** for verifying all AI-generated content and submitting it under your own name (with proper AI disclosure).

---

**Version**: v2.4.0
**Last Updated**: 2026-01-04
