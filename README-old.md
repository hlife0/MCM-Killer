# MCM-Killer: Multi-Agent Framework for Mathematical Modeling Competitions

> **Project Goal**: A framework that creates 10 specialized AI agents to solve MCM/ICM problems through iterative collaboration

> [!WARNING]
> **⚠️ CRITICAL: READ BEFORE USING**
>
> - This is a **RESEARCH PROTOTYPE**, not a production tool
> - AI-generated content is **unreliable** and requires **thorough human verification**
> - You **MUST** disclose AI use per competition rules (e.g., MCM AI Use Report)
> - You are **SOLELY RESPONSIBLE** for all content you submit
> - Developers provide **NO WARRANTY** and accept **NO LIABILITY**
>
> See [Academic Integrity](#-academic-integrity--ai-use-policy) and [Disclaimer](#-disclaimer--liability) below.

---

## 🎯 What is MCM-Killer?

**MCM-Killer is a multi-agent ORCHESTRATION FRAMEWORK** - not an automated paper generator.

### The Core Distinction

| ❌ Common Misconception | ✅ What MCM-Killer Actually Is |
|------------------------|-------------------------------|
| An AI that writes your MCM paper | A framework that **coordinates 10 specialized AI agents** |
| Push-button solution | Requires active **human orchestration** |
| Single AI model | **Multi-agent system** with consultation and revision loops |
| Black box | **Transparent workflow** with verification gates |

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  FRAMEWERK SETUP (One-time, per problem)                    │
│  Input: Problem PDF + Data + Reference Papers               │
│  Process: MCM-Killer configures 10 agents with prompts      │
│  Output: workspace/ with agent system ready                │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  COMPETITION EXECUTION (You orchestrate the agents)         │
│  Process:                                                  │
│    1. You (Director) call agents sequentially              │
│    2. Agents use LLM backend (you choose which model)      │
│    3. Agents consult with each other                       │
│    4. Agents iterate based on feedback                     │
│    5. You verify all outputs before submission            │
│  Output: Requirements, models, code, figures, paper        │
│  Owner: YOU (the competition participant)                  │
└─────────────────────────────────────────────────────────────┘
```

### Key Principle

**MCM-Killer orchestrates agents, YOU orchestrate the workflow.**

- The framework provides: Agent prompts, workflow structure, quality gates
- **You provide**: Strategic decisions, iteration direction, human verification
- **The agents provide**: Domain expertise using their LLM backend
- **You own**: The generated paper and take full responsibility

---

## 👥 The 10-Agent System

| Agent | Role | Model | Key Responsibility |
|-------|------|-------|-------------------|
| **@reader** | Problem Analyst | Opus | Extracts ALL requirements from PDF using docling MCP |
| **@researcher** | Strategy Advisor | Opus | Brainstorms mathematical methods based on domain knowledge |
| **@modeler** | Mathematical Architect | Opus | Designs formal models with LaTeX-ready formulations |
| **@coder** | Implementation Engineer | Opus | Writes and executes Python code, generates results |
| **@validator** | Quality Checker | Opus | Verifies code correctness and result accuracy |
| **@visualizer** | Graphics Designer | Opus | Creates publication-quality visualizations |
| **@writer** | Paper Author | Opus | Writes 25-page LaTeX paper using mcmthesis template |
| **@summarizer** | Summary Expert | Opus | Creates critical 1-page Summary Sheet |
| **@editor** | Language Polisher | Opus | Polishes grammar, style, consistency |
| **@advisor** | Faculty Reviewer | Opus | Final quality gate against O-Prize standards |

---

## 🔄 Critical Workflow Mechanisms

### 1. Revision-Verification Loop ⭐ (Most Important!)

> **This is the core quality control mechanism. README diagrams must show this.**

**How it works:**
```
Round 1:
  @coder submits code
  @validator reviews → "NEEDS REVISION: Missing random seed, edge cases not handled"

Round 2:
  @coder revises → "Fixed random_state=42, added edge case handling"
  @coder MUST request: "Director, please send to @validator for RE-VERIFICATION"
  @validator re-reviews → "APPROVED: All tests passed"

Round 3 (if needed):
  Continue loop until APPROVED
```

**Same pattern for @writer ↔ @advisor:**
- @writer submits paper
- @advisor reviews → "NEEDS REVISION: Missing sensitivity analysis"
- @writer revises → requests re-verification
- @advisor approves or continues loop

**Key Rules:**
- ❌ WRONG: Agent says "revisions complete" → Director moves on without re-checking
- ✅ CORRECT: Agent says "revisions complete" → Director automatically calls reviewing agent for re-verification
- 🔄 LOOP: Continue until reviewing agent explicitly states "APPROVED"

### 2. Mandatory Consultation Protocol

> **Model design decisions REQUIRE multi-agent consultation. Single-agent work produces weak models.**

**When @modeler designs a model:**

```
Step 1: @modeler writes initial proposal → output/consultations/proposal_model1.md

Step 2: Director requests feedback from multiple agents:
  @researcher: "Is this method appropriate? Any precedents in O-Prize papers?"
  @coder: "Is this feasible given our data and compute constraints?"
  @advisor: "Is this sophisticated enough for O-Prize quality?"

Step 3: @modeler integrates all feedback → final design in output/model_design.md

Step 4: Include "Consultation Summary" section documenting what feedback was received
```

**Example Feedback Format:**
```
@researcher: "Random Forest is appropriate. Consider adding XGBoost for comparison."
@coder: "Feasible. We have 35 years of data. RF runs in <1min on CPU."
@advisor: "Too simple alone. Suggest hybrid approach or ensemble method."
```

### 3. Iteration Loop for Results

```
@modeler designs model
  ↓
@coder implements and runs
  ↓
Results check: Good enough?
  ↓ No
Back to @modeler: refine assumptions/approach
  ↓
@coder re-implements
  ↓
Repeat until results satisfactory
```

### 4. Parallel Work Tracks

**Phase 1 allows parallel execution:**
```
Track A (Core Modeling):          Track B (Background Drafting):
  @modeler designs models           @writer drafts Introduction
  @coder implements                 @writer drafts Assumptions
  @validator verifies               @writer drafts Problem Background
```

---

## 📊 Complete Workflow Diagram

```mermaid
graph TB
    subgraph "Phase 0: Understanding"
        D[Director] --> R[@reader]
        R --> Res[@researcher]
    end

    subgraph "Phase 1: Design & Consultation"
        Res --> |proposal| M[@modeler]
        M --> |feedback?| Res
        M --> |feasibility?| C[@coder]
        M --> |quality?| A[@advisor]
        C --> M
        A --> M
    end

    subgraph "Phase 2: Implementation & Iteration"
        M --> C
        C --> V[@validator]
        V --> |NEEDS REVISION| C
        C --> |re-verify| V
        V --> |APPROVED| Vi[@visualizer]
    end

    subgraph "Phase 3: Paper Assembly"
        Vi --> W[@writer]
        W --> S[@summarizer]
        S --> E[@editor]
        E --> A
        A --> |NEEDS REVISION| W
        W --> |re-verify| A
        A --> |APPROVED| D
    end

    style V fill:#ff6b6b
    style A fill:#ff6b6b
```

**Legend:**
- Red boxes (V, A) = Quality gates with revision loops
- Dashed lines = Revision-verification cycles
- All agent interactions require Director orchestration

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.10+ | Code execution |
| **Claude Code** | Latest | Multi-agent orchestration |
| **Docling MCP** | Latest | Accurate PDF reading |
| **LaTeX** | TeX Live / MiKTeX | Paper compilation (optional) |

### Setup (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/hlife0/MCM-Killer.git
cd MCM-Killer

# 2. Navigate to workspace
cd workspace/2025_C

# 3. Unzip data
unzip 2025_Problem_C_Data.zip

# 4. Run Claude Code
claude
```

### Running the Agents

**In Claude Code:**
```
Read CLAUDE.md. You are the Director.
Start by calling @reader to extract requirements.
```

**Example workflow:**
```bash
# Step 1: Extract requirements
@reader

# Step 2: Brainstorm methods
@researcher

# Step 3: Design models (with consultation)
@modeler  # Director asks @researcher, @coder, @advisor for feedback

# Step 4: Implement
@coder

# Step 5: Verify (may need multiple rounds)
@validator  # If NEEDS REVISION, @coder fixes and requests re-verification

# Step 6: Visualize
@visualizer

# Step 7: Write paper
@writer

# Step 8: Summarize
@summarizer

# Step 9: Edit
@editor

# Step 10: Final review
@advisor  # If NEEDS REVISION, @writer fixes and requests re-verification
```

---

## ⚖️ Academic Integrity & AI Use Policy

> [!WARNING]
> **CRITICAL: You MUST follow these guidelines.**

### AI Use Disclosure Requirements

**For MCM/ICM Competitions:**
- **AI IS permitted** by COMAP
- **AI Use Report is REQUIRED** (does not count toward 25-page limit)
- Report must follow [COMAP AI Use Policy](https://www.comap.com/undergraduate/contests/mcm/instructions.html#AI)

**What You Must Disclose:**
- ✅ Which AI tools you used (Claude Code CLI, model version)
- ✅ What tasks AI assisted with
- ✅ How you verified and refined AI-generated content
- ✅ Your role in directing and validating the work

**Example AI Use Report:**
```markdown
# AI Use Report

## Tools Used
- Claude Code CLI (Model: Claude Opus 4.5)
- 10 specialized agents within the framework

## AI-Assisted Tasks
1. Problem requirement extraction (@reader)
2. Mathematical method brainstorming (@researcher)
3. Model design and formulation (@modeler)
4. Python code implementation (@coder)
5. Code verification (@validator)
6. Visualization design (@visualizer)
7. LaTeX paper writing (@writer)
8. Summary creation (@summarizer)
9. Language editing (@editor)
10. Quality review (@advisor)

## Human Verification
- All models were reviewed for mathematical correctness
- All code was tested and debugged
- Paper content was thoroughly edited
- Final submission was approved by human team members

## Responsibility Statement
We take full responsibility for this submission.
The AI framework served as a productivity aid.
We directed the agents and validated all outputs.
```

### Consequences of Misuse

- ❌ **Academic misconduct** if you fail to disclose AI use
- ❌ **Disqualification** from competitions
- ❌ **Reputation damage** to you and your institution

---

## ⚠️ Disclaimer & Liability

> [!DANGER]
> **READ THIS SECTION CAREFULLY**

### Research-Only Status

**This project is in R&D stage.**
- ❌ NOT production-ready
- ❌ NOT suitable for unattended use
- ❌ NOT a substitute for human reviewers
- ✅ Intended for research and educational purposes only

### Reliability Warnings

**AI-generated content is fundamentally unreliable:**

| Risk | Description |
|------|-------------|
| **Hallucinations** | AI may generate false citations, incorrect math, fabricated data |
| **Logical Errors** | Reasoning may be flawed |
| **Code Bugs** | Generated code may contain errors |
| **Quality Variance** | Output quality varies between runs |

### No Warranty

**THIS PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**

THE DEVELOPERS:
- ❌ Do NOT guarantee correctness of AI-generated content
- ❌ Do NOT guarantee suitability for any purpose
- ❌ Do NOT guarantee competition results
- ❌ Will NOT be liable for any damages

### Your Responsibility

By using this project, you agree that:
1. **YOU are solely responsible** for verifying all AI-generated content
2. **YOU must conduct human review** before submission
3. **YOU take full liability** for consequences
4. **YOU will not hold developers liable** for any damages

### Recommended Usage

**✅ DO:**
- Use as productivity aid
- Verify all mathematical derivations
- Test all code thoroughly
- Review and edit all text
- Disclose AI use honestly
- Conduct multiple quality checks

**❌ DON'T:**
- Blindly trust AI-generated content
- Submit without human review
- Use AI to cheat or plagiarize
- Hide AI assistance
- Skip verification steps

---

## 🤖 AI Tools & Models

### 🔧 Development Tools (Framework Creation)

Tools used to BUILD the MCM-Killer framework:

| Tool | LLM Backend | Role in Development |
|------|-------------|-------------------|
| **Claude Code CLI** | GLM-4.7 / GLM-4.6 | Architecture design, prompt engineering |
| **Antigravity** | Claude Sonnet 4.5 | Prototyping, exploration |
| **GitHub Copilot** | Claude Sonnet 4.5 | Code completion |

**Transparency Note**: Framework development used AI tools. This is documented here. Framework commits use clean commit messages.

---

### 🚀 Runtime Configuration (Your Usage)

**When YOU use MCM-Killer, YOU control the AI backend:**

#### Supported LLM Backends

| LLM | Provider | Characteristics |
|-----|----------|-----------------|
| **Claude Opus/Sonnet** | Anthropic | Excellent for complex reasoning |
| **GPT-4 Turbo** | OpenAI | Fast, strong coding |
| **GLM-4** | Zhipu AI | Cost-effective |

#### You Decide

- **Choice of Model**: Your budget, quality requirements
- **Usage Pattern**: How you orchestrate agents
- **Strategic Decisions**: You direct the workflow
- **Output Ownership**: The paper belongs to **YOU**
- **AI Co-authorship**: **YES - You MUST report AI use**

---

## 📂 Directory Structure

```
MCM-Killer/
│
├── student paper/              # Few-Shot Corpus (O-Prize papers)
│   └── YYYY/A-F/*.pdf
│
├── problems and results/       # Benchmark Set (READ-ONLY)
│   └── YYYY/*.pdf, *.zip
│
├── LaTeX__Template_for_MCM_ICM/  # LaTeX template
│   └── mcmthesis.cls
│
├── workspace/                  # Generated Workspace
│   └── 2025_C/
│       ├── 2025_MCM_Problem_C.pdf
│       ├── 2025_Problem_C_Data.zip
│       ├── reference_papers/   # 33 O-Prize papers
│       ├── latex_template/
│       ├── CLAUDE.md           # Director instructions
│       ├── .claude/
│       │   └── agents/         # 10 agent configurations
│       ├── .mcp.json
│       └── output/             # YOUR work products
│           ├── requirements_checklist.md
│           ├── research_notes.md
│           ├── model_design.md
│           ├── consultations/  # Multi-agent consultation logs
│           ├── code/
│           ├── figures/
│           ├── paper.tex       # YOUR final paper
│           └── validation_report.md
│
└── .gitignore
```

---

## 🗺️ Roadmap

- [x] **Phase 1**: Data Collection & Standardization
- [x] **Phase 2**: Multi-Agent Architecture Design
- [ ] **Phase 3**: Successful Problem Solving (in progress)
- [ ] **Phase 4**: O-Prize Quality Validation

---

## 📄 License

**This project is for research and educational purposes only.**

By using this project, you agree to:
1. Research/Educational use only
2. Follow all competition AI use policies
3. Take full responsibility for generated content
4. Accept NO liability from developers

Commercial use is prohibited without explicit permission.

---

## 📞 Contact

For questions about appropriate use, consult with:
- Your academic advisor
- Competition officials
- Your institution's research ethics board

**For technical questions or licensing inquiries, contact the framework developers.**
