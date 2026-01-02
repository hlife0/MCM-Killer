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
  - 10 AI agents collaborate
  - Design models, write code, create figures, write paper
  - Iteration and quality checks happen automatically
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
| **Reader** | Problem Analyst | Extracts all requirements from PDF |
| **Researcher** | Strategy Advisor | Brainstorms mathematical methods |
| **Modeler** | Mathematical Architect | Designs formal models with equations |
| **Feasibility Checker** | Implementation Gatekeeper | Evaluates technical feasibility of models |
| **Data Engineer** | Data Pipeline Specialist | Creates features from raw data |
| **Code Translator** | Math-to-Code Translator | Converts mathematical models to Python |
| **Model Trainer** | Model Training Specialist | Trains models and generates predictions |
| **Validator** | Quality Gatekeeper | Verifies outputs at every stage (6 gates) |
| **Visualizer** | Graphics Designer | Creates publication-quality figures |
| **Writer** | Paper Author | Writes 25-page LaTeX paper |
| **Summarizer** | Summary Expert | Creates 1-page summary sheet |
| **Editor** | Language Polisher | Fixes grammar and style |
| **Advisor** | Faculty Reviewer | Final quality control |

### The AI Workflow (Automatic - 8-Phase Pipeline)

The AI agents follow a strict pipeline workflow with 6 mandatory quality gates:

```
PHASE 0: Problem Understanding
  Reader → extracts requirements from PDF
  Researcher → proposes methods

PHASE 1: Model Design
  Modeler → designs mathematical models
  Feasibility Checker → evaluates implementation feasibility
  └─ Validator Gate: APPROVED → proceed / NEEDS REVISION → back to Modeler

PHASE 2: Data Preparation (Gate 1)
  Data Engineer → creates features from data
  └─ Validator Gate: APPROVED → proceed / NEEDS REVISION → back to Data Engineer

PHASE 3: Code Translation (Gate 2)
  Code Translator → converts math to Python
  └─ Validator Gate: APPROVED → proceed / NEEDS REVISION → back to Code Translator

PHASE 4: Model Training (Gate 3)
  Model Trainer → trains models on full data
  └─ Validator Gate: APPROVED → proceed / NEEDS REVISION → back to Model Trainer

PHASE 5: Output Generation (Parallel)
  → Visualizer → creates figures (awaiting Validator approval)
  → Writer → writes paper (awaiting Validator approval)

PHASE 6: Paper & Summary (Gates 4 & 5)
  Writer completes → Validator Gate 4: APPROVED → proceed / NEEDS REVISION
  Summarizer writes summary → Validator Gate 5: APPROVED → proceed / NEEDS REVISION

PHASE 7: Final Polish (Gate 6)
  Editor polishes paper and summary
  └─ Validator Gate 6: APPROVED → proceed / NEEDS REVISION → back to Editor

PHASE 8: Final Review
  Advisor → performs final quality check
  └─ APPROVED → READY FOR SUBMISSION / REJECTED → fix issues
```

**Key Pipeline Features:**
- **Sequential Execution**: Each stage must complete before the next begins
- **Mandatory Verification**: Validator checks every output before proceeding
- **Auto-Reverification**: Failed stages must be re-checked after fixes
- **No Shortcuts**: All gates must be passed, no exceptions

### Key Quality Mechanisms (Built-in)

**Six Mandatory Quality Gates**
The Validator agent enforces strict quality control at 6 critical points:
- **Gate 1**: Data quality check (all features created, no NaN values)
- **Gate 2**: Code translation accuracy (model type matches design, feature count exact)
- **Gate 3**: Training results sanity (models converged, predictions logical)
- **Gate 4**: Paper verification (all requirements met, numbers match data)
- **Gate 5**: Summary verification (matches paper exactly, fits 1 page)
- **Gate 6**: Final edit check (data consistency preserved, no technical changes)

**Data Authority Hierarchy**
When conflicts occur, the system follows this strict priority:
1. **CSV outputs** (e.g., `la2028_projections.csv`) - Source of Truth
2. **Training reports** - Human-verified summaries
3. **Draft summaries** - May be outdated
4. **Draft papers** - Must match Level 1

*Example: If CSV shows USA=118 but paper says USA=188, the CSV wins and the paper must be corrected.*

**Automatic Revision Loops**
- If Validator rejects → Agent automatically fixes and resubmits for re-verification
- If Advisor rejects → Affected agents fix issues and re-enter the pipeline
- Continues until all gates are passed

**Mandatory Rejection Criteria**
Validator MUST reject (no exceptions) for:
- Model type mismatches (e.g., OLS used instead of designed Hurdle-NB)
- Feature count reduction (e.g., 3 features used when 9 designed)
- Data version conflicts (e.g., CSV and summary have different timestamps)
- Sanity check failures (e.g., host country prediction decreases)
- Internal contradictions (e.g., abstract shows China=51, table shows China=69)

**Tool Usage Enforcement**
- Every agent must use actual tools (Read, Write, Bash, etc.)
- "0 tool uses" = automatic rejection and retry (prevents hallucination)

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

**The AI will:**
- Extract requirements automatically
- Design and implement models
- Generate figures and results
- Write the complete paper
- Perform quality checks and revisions

**You will:**
- Monitor progress
- Answer occasional clarification questions
- Review the final output
- Submit to competition

---

## Academic Integrity & AI Use Policy

### You MUST Disclose AI Use

**MCM/ICM competitions permit AI use but require disclosure:**

- You **MUST** submit an AI Use Report with your paper
- The report does **NOT** count toward the 25-page limit
- See [COMAP AI Use Policy](https://www.comap.com/undergraduate/contests/mcm/instructions.html#AI)

### Example AI Use Report

```markdown
# AI Use Report

## Tools Used
- MCM-Killer autonomous multi-agent system (v2.1)
- Claude Code CLI (Model: Claude Opus 4.5 / Sonnet 4.5)
- 13 specialized AI agents within the system
- Docling MCP Server for PDF processing
- **NEW in v2.1**: Problem-type-aware pipeline (adapts to 6 MCM problem types)

## AI-Assisted Tasks
The following tasks were performed autonomously by AI agents:
1. Problem requirement extraction from PDF (Reader)
2. Mathematical method research and brainstorming (Researcher)
3. Model design and mathematical formulation (Modeler)
4. Implementation feasibility evaluation (Feasibility Checker)
5. Feature engineering from raw data (Data Engineer)
6. Mathematical model to Python code translation (Code Translator)
7. Model training and prediction generation (Model Trainer)
8. Quality verification at 6 critical stages (Validator)
9. Publication-quality figure creation (Visualizer)
10. LaTeX paper writing (Writer)
11. One-page summary sheet creation (Summarizer)
12. Language editing and polishing (Editor)
13. Final quality control review (Advisor)

## Human Verification
We reviewed all AI-generated content for:
- Mathematical correctness
- Code accuracy and functionality
- Logical consistency
- Appropriate citations
- Compliance with competition requirements

## Responsibility Statement
We take full responsibility for this submission.
The AI system served as an autonomous assistant.
We verified and approved all final outputs.
```

### Consequences of Non-Disclosure

- **Academic misconduct** charges
- **Competition disqualification**
- **Reputation damage**
- **Institutional penalties**

---

## Disclaimer & Liability

### Research-Only Status

**This project is a research prototype.**

- ❌ NOT production-ready
- ❌ NOT guaranteed to produce correct results
- ❌ NOT a substitute for human expertise
- ✅ For research and educational purposes only

### Reliability Warnings

**AI-generated content has significant risks:**

| Risk | Description |
|------|-------------|
| **Hallucinations** | AI may generate false information, incorrect math, or fabricated data |
| **Logical Errors** | Reasoning may be flawed or unsound |
| **Code Bugs** | Generated code may contain errors or security issues |
| **Inconsistent Results** | Multiple runs may produce different outputs |

### No Warranty

**THIS PROJECT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.**

Developers:
- ❌ Do NOT guarantee correctness of any content
- ❌ Do NOT guarantee suitability for any purpose
- ❌ Do NOT guarantee competition success
- ❌ Will NOT be liable for any damages

### Your Responsibility

By using this system, you agree that:

1. **You are solely responsible** for verifying all AI-generated content
2. **You must conduct thorough human review** before submission
3. **You take full liability** for all consequences
4. **You will not hold developers liable** for any damages including:
   - Academic penalties
   - Competition disqualification
   - Financial losses
   - Reputation damage

### Recommended Usage

**✅ DO:**
- Use as a productivity tool
- Verify all mathematical derivations
- Test all code thoroughly
- Review all text for accuracy
- Disclose AI use honestly
- Conduct multiple quality checks

**❌ DON'T:**
- Blindly trust AI outputs
- Submit without human review
- Hide AI assistance
- Skip verification steps

---

## System Architecture (For Technical Users)

### The AI Director

The system is orchestrated by an AI "Director" (using Claude Code CLI) that:

- Calls specialized agents in strict pipeline sequence
- Manages all verification gates and re-verification loops
- Enforces data authority hierarchy
- Ensures no stages are skipped
- Handles automatic retries on failures

**Critical Rule**: Director NEVER does the work themselves - always delegates to specialized agents.

### Agent Interaction Patterns

**1. Strict Sequential Pipeline**
```
Reader → Researcher → Modeler → Feasibility_Checker
  ↓ (Validator Gate)
Data_Engineer → Code_Translator → Model_Trainer
  ↓ (Validator Gates 2-3)
Visualizer + Writer (parallel)
  ↓ (Validator Gates 4-5)
Summarizer → Editor
  ↓ (Validator Gate 6)
Advisor → Final Approval
```

**2. Verification Gates**
- Every output must be verified by Validator before next stage can use it
- Rejected outputs trigger automatic revision + re-verification cycle
- No exceptions - even "close enough" outputs are rejected

**3. Data Consistency**
- CSV outputs are single source of truth (Level 1 Authority)
- All papers and summaries must match CSV exactly
- Version timestamps are checked to detect outdated documents

**4. Specialization Over Generalization**
- Original "Coder" agent split into 4 specialists:
  - Feasibility Checker (evaluates if model is implementable)
  - Data Engineer (prepares features from raw data)
  - Code Translator (converts math equations to Python)
  - Model Trainer (fits models and generates predictions)
- Each specialist has deep expertise in their domain

### Technology Stack

**Orchestration Layer:**
- Claude Code CLI (multi-agent coordination and workflow management)

**AI Models:**
- Backend: User-configurable (Claude Opus/Sonnet, GPT-4, etc.)
- All 13 agents use the same LLM backend
- Agent behavior controlled by prompt configuration files

**Specialized Tools:**
- **Docling MCP Server**: Accurate PDF parsing (mandatory for problem extraction)
- **Python + Scientific Stack**: pandas, numpy, scikit-learn, statsmodels
- **LaTeX**: Paper generation (uses MCM/ICM template)
- **Matplotlib/Seaborn**: Publication-quality visualizations

**Project Structure:**
```
workspace/2025_C/
├── .claude/agents/         # 13 agent configuration files
├── reference_papers/       # 33 O-Prize winning papers for reference
├── latex_template/         # MCM/ICM LaTeX template
├── 2025_MCM_Problem_C.pdf # Current problem statement
├── 2025_Problem_C_Data.zip # Data files
└── output/                 # All generated outputs (papers, code, figures)
```

---

## What's New in v2.1

**Problem-Type-Aware Multi-Agent System**

If you're familiar with v2.0, v2.1 adds critical generalization capabilities:

### From Prediction-Specific to Problem-Type-Aware

**Why**: v2.0 was hardcoded for time-series prediction problems (e.g., Olympics medal forecasting). It couldn't handle optimization, network design, evaluation, or other MCM problem types.

**What Changed**:
- ❌ **Old (v2.0)**: Assumed all problems were time-series prediction with "Year", "Country", "Medals" columns
- ✅ **New (v2.1)**: System now identifies problem type and adapts strategies accordingly

### New Problem Type Classification System

**@reader** now classifies problems into 6 primary types:

| Type | Description | Example |
|------|-------------|---------|
| **PREDICTION** | Forecast future values from historical data | Medal forecasting, stock prediction |
| **OPTIMIZATION** | Find optimal solution under constraints | Resource allocation, facility location |
| **NETWORK_DESIGN** | Design/analyze network topology | Communication networks, transportation |
| **EVALUATION** | Assess/rank alternatives | Project selection, policy comparison |
| **CLASSIFICATION** | Categorize items into groups | Image recognition, spam detection |
| **SIMULATION** | Model dynamic systems | Population dynamics, disease spread |

### Type-Aware Feature Engineering

**@data_engineer** now creates features appropriate to problem type:

| Problem Type | Example Features |
|--------------|-----------------|
| PREDICTION | Lag variables, moving averages, trends |
| OPTIMIZATION | Decision variables, constraint slack, feasibility indicators |
| NETWORK | Node degrees, edge capacities, betweenness centrality |
| EVALUATION | Weighted scores, criteria comparisons, rankings |
| CLASSIFICATION | Scaled features, polynomial terms, class weights |
| SIMULATION | State changes, cumulative states, volatility measures |

### Type-Aware Visualizations

**@visualizer** now creates problem-type-appropriate figures:

| Problem Type | Example Visualizations |
|--------------|---------------------|
| PREDICTION | Time series plots, prediction intervals, actual vs predicted scatter |
| OPTIMIZATION | Feasible regions, objective contours, decision variable bar charts |
| NETWORK | Network topology graphs, flow visualizations, centrality heatmaps |
| EVALUATION | Ranking bar charts, criteria comparisons, radar charts |
| CLASSIFICATION | Confusion matrices, ROC curves, decision boundaries |
| SIMULATION | State evolution plots, phase portraits, trajectory diagrams |

### Type-Aware Validation

**@validator** now enforces type-specific sanity checks:

| Problem Type | Sanity Checks |
|--------------|--------------|
| PREDICTION | Trends are reasonable, no impossible values, confidence intervals valid |
| OPTIMIZATION | All constraints satisfied, optimal solution at boundary (if binding) |
| NETWORK | Network connected (if required), flow conservation respected |
| EVALUATION | Rankings are transitive (no cycles), weights sum to 1 |
| CLASSIFICATION | Class distribution reasonable, confusion matrix diagonal-dominant |
| SIMULATION | State evolution smooth, timestep consistency maintained |

### Type-Specific Output Filenames

**@model_trainer** now saves results to type-appropriate filenames:

- PREDICTION → `predictions.csv`
- OPTIMIZATION → `solution.csv`
- NETWORK_DESIGN → `network_solution.csv`
- EVALUATION → `rankings.csv`
- CLASSIFICATION → `classifications.csv`
- SIMULATION → `simulation_results.csv`

### Impact on Problem Coverage

**v2.0**: Could handle 1 problem type (time-series prediction)
- ✅ Olympics medal forecasting
- ❌ Network design problems
- ❌ Optimization problems
- ❌ Evaluation problems

**v2.1**: Can handle 6 major MCM problem types
- ✅ Time-series prediction
- ✅ Mathematical optimization
- ✅ Network design and analysis
- ✅ Multi-criteria evaluation
- ✅ Classification problems
- ✅ Simulation modeling

### Technical Changes Summary

- **14 agents updated** (all agents + Director)
- **~4,000 lines of agent prompts modified** to add problem-type awareness
- **6 problem-type strategies implemented** across data engineering, visualization, and validation
- **Dynamic column detection** enhanced for all problem types
- **Type-specific sanity checks** added throughout pipeline

### Known Limitations of v2.1

**Not a complete rewrite** - v2.1 is an incremental improvement on v2.0:
- Core pipeline architecture unchanged (still 13 agents, 8 phases)
- Prediction problems still best-supported (most mature feature set)
- Some problem types may need additional refinement (e.g., simulation, complex optimization)
- Requires testing on real MCM problems to validate effectiveness

**Future roadmap**: v3.0 would require complete architectural redesign for full generalization.

---

## What's New in v2.0

If you're familiar with v1.0, here are the major changes:

### From 10 Agents to 13 Agents

**Why**: The original "Coder" agent was trying to do too much, leading to quality issues.

**What Changed**:
- ❌ **Old**: Coder (handled everything from feasibility to training)
- ✅ **New**: 4 specialized agents split the work:
  - **Feasibility Checker**: Evaluates if model can be implemented before coding starts
  - **Data Engineer**: Prepares features and data pipeline
  - **Code Translator**: Converts math equations directly to Python code
  - **Model Trainer**: Focuses solely on training and generating predictions

### From Flexible Collaboration to Strict Pipeline

**Why**: Free-form agent interaction led to coordination failures and inconsistent results.

**What Changed**:
- ❌ **Old**: Agents could work in any order, parallel execution encouraged
- ✅ **New**: Strict 8-phase sequential pipeline with 6 verification gates
  - Each stage must complete before next begins
  - Validator checks every output
  - Rejected stages must be re-verified after fixes

### From Loose Coordination to Data Authority Hierarchy

**Why**: Version conflicts caused major inconsistencies (e.g., paper showed USA=188, CSV showed USA=118).

**What Changed**:
- ❌ **Old**: Multiple data versions could exist simultaneously
- ✅ **New**: 4-level data authority hierarchy
  - Level 1: CSV outputs (single source of truth)
  - Level 2-4: Reports, summaries, papers (must match Level 1)
  - Automatic timestamp checking to detect outdated documents

### From "Good Enough" to Mandatory Rejection Criteria

**Why**: Accepting "close enough" outputs led to quality drift.

**What Changed**:
- ❌ **Old**: Validator could approve with "trade-offs documented"
- ✅ **New**: Validator MUST reject for:
  - Model type mismatches (no exceptions)
  - Feature count reduction (no exceptions)
  - Data version conflicts (no exceptions)
  - Sanity check failures (no exceptions)

### Impact on Results

**v1.0 Experience** (from `trail-Istanbul/` execution reports):
- ✅ Generated 97 workflow files, 10 Python scripts, 27 figures
- ❌ Suffered from coordination failures
- ❌ Inconsistent results between code and paper

**v2.0 Goals**:
- Maintain productivity while improving quality
- Eliminate data inconsistencies
- Ensure all outputs are verified and synchronized
- Reduce human correction burden through stricter gates

---

## Project Status

**Current Phase**: Active Research & Development (v2.1 - Problem Type Generalization)

**Recent Updates:**
- **v2.1 (Current)**: Problem-type-aware generalization
  - Added problem type classification system (@reader)
  - All 14 agents now problem-type-aware
  - Implemented 6 problem-type strategies (PREDICTION, OPTIMIZATION, NETWORK, EVALUATION, CLASSIFICATION, SIMULATION)
  - Type-specific feature engineering, visualizations, and validation
  - Dynamic output filenames based on problem type
- **v2.0**: Complete pipeline reconstruction
  - Split "Coder" into 4 specialized agents (Feasibility Checker, Data Engineer, Code Translator, Model Trainer)
  - Implemented 6 mandatory verification gates
  - Added data authority hierarchy and version synchronization
  - Strengthened quality control with mandatory rejection criteria
- **v1.0**: Initial 10-agent system

**Known Issues:**
- v2.1 is an incremental improvement - not a complete rewrite
- Prediction problems still best-supported (most mature feature set)
- Some problem types need additional refinement (simulation, complex optimization)
- System generates large amounts of intermediate files (requires cleanup)
- Still experimental - human verification is absolutely required

**Roadmap:**
- [x] Phase 1: Data collection & agent system design
- [x] Phase 2: Implementation of 10-agent architecture (v1.0)
- [x] Phase 3: Pipeline reconstruction with 13 agents (v2.0)
- [ ] Phase 4: Testing on real MCM/ICM problems
- [ ] Phase 5: Quality validation and optimization
- [ ] Phase 6: Production-readiness assessment

---

## License

**For research and educational purposes only.**

By using this project, you agree to:
1. Use only for research or education
2. Follow all competition rules and AI disclosure requirements
3. Take full responsibility for generated content
4. Accept no liability from developers

Commercial use prohibited without explicit permission.

---

## Contact & Support

For questions about:
- **Appropriate use**: Consult your academic advisor or competition officials
- **Technical issues**: Check the documentation or contact developers
- **Licensing**: See license section above

**Remember**: This is an AI research prototype. Always verify outputs before use.
