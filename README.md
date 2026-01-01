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

## How It Works: The 10-Agent AI System

MCM-Killer uses **10 specialized AI agents** that work together autonomously:

| Agent | Role | What It Does |
|-------|------|--------------|
| **Reader** | Problem Analyst | Extracts all requirements from PDF |
| **Researcher** | Strategy Advisor | Brainstorms mathematical methods |
| **Modeler** | Mathematical Architect | Designs formal models with equations |
| **Coder** | Implementation Engineer | Writes and executes Python code |
| **Validator** | Quality Checker | Verifies code correctness and results |
| **Visualizer** | Graphics Designer | Creates publication-quality figures |
| **Writer** | Paper Author | Writes 25-page LaTeX paper |
| **Summarizer** | Summary Expert | Creates 1-page summary sheet |
| **Editor** | Language Polisher | Fixes grammar and style |
| **Advisor** | Faculty Reviewer | Final quality control |

### The AI Workflow (Automatic)

The AI agents follow this workflow automatically:

```
1. UNDERSTAND
   Reader → extracts requirements from PDF
   Researcher → proposes methods

2. DESIGN & VALIDATE
   Modeler → designs mathematical models
   (automatically consults with Researcher, Coder, Advisor for feedback)
   Coder → implements in Python
   Validator → checks correctness
   (if issues found → automatic revision loop)

3. VISUALIZE
   Visualizer → creates professional figures

4. WRITE & REVIEW
   Writer → writes LaTeX paper
   Summarizer → creates summary sheet
   Editor → polishes language
   Advisor → final quality check
   (if issues found → automatic revision loop)

5. COMPLETE
   Final paper ready for your review
```

### Key Quality Mechanisms (Built-in)

**Automatic Revision Loops**
- If Validator finds issues → Coder automatically fixes and re-submits
- If Advisor finds issues → Writer automatically fixes and re-submits
- This continues until quality gates are passed

**Multi-Agent Consultation**
- Modeler automatically gets feedback from 3 other agents before finalizing
- Prevents single-agent blind spots

**Environment Exploration**
- Coder and Validator automatically check system capabilities
- Adapt to your hardware and software

**Tool Usage Enforcement**
- Every agent must use actual tools (Read, Write, Bash, etc.)
- "0 tool uses" = automatic rejection and retry

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
- MCM-Killer autonomous multi-agent system
- Claude Code CLI (Model: Claude Opus 4.5)
- 10 specialized AI agents within the system

## AI-Assisted Tasks
The following tasks were performed autonomously by AI agents:
1. Problem requirement extraction from PDF
2. Mathematical method brainstorming
3. Model design and formulation
4. Python code implementation
5. Code verification and testing
6. Visualization design
7. LaTeX paper writing
8. Summary sheet creation
9. Language editing
10. Quality review

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

The system is orchestrated by an AI "Director" agent that:

- Automatically calls specialized agents in the correct order
- Manages parallel work streams
- Handles revision and verification loops
- Ensures quality gates are met
- Adapts to issues and retries automatically

### Agent Interaction Patterns

**1. Sequential Pipeline**
Reader → Researcher → Modeler → Coder → Validator → Visualizer → Writer → Summarizer → Editor → Advisor

**2. Revision Loops**
- Coder submits → Validator reviews → (if issues) Coder revises → Validator re-checks
- Writer submits → Advisor reviews → (if issues) Writer revises → Advisor re-checks

**3. Consultation**
- Modeler gets feedback from Researcher, Coder, and Advisor before finalizing
- Ensures models are theoretically sound, feasible, and high-quality

**4. Iteration**
- If results are unsatisfactory, the system automatically iterates
- Models are refined and re-implemented until quality thresholds are met

### Technology Stack

**Orchestration Layer:**
- Claude Code CLI (multi-agent coordination)

**AI Models:**
- Backend: User-configurable (Claude Opus/Sonnet, GPT-4, GLM-4, etc.)
- All agents use the same LLM backend

**Specialized Tools:**
- Docling MCP: Accurate PDF parsing
- Python + Scientific Stack: Code execution
- LaTeX: Paper generation
- Matplotlib/Seaborn: Visualization

---

## Project Status

**Current Phase**: Active Research & Development

Roadmap:
- [x] Phase 1: Data collection & agent system design
- [x] Phase 2: Implementation of 10-agent architecture
- [ ] Phase 3: Testing on real MCM/ICM problems
- [ ] Phase 4: Quality validation and optimization

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
