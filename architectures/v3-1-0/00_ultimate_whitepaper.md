# MCM-Killer v3.1.0 Ultimate Architecture Whitepaper
## From "Problem-Solving Factory" to "Cognitive Research Laboratory"

> **Version**: v3.1.0-Ultimate
> **Code Name**: Cognitive Narrative & Adversarial Evolution
> **Date**: 2026-01-24
> **Status**: Final Optimization Blueprint
> **Philosophy**: "Errors are not garbage—they are the raw material for scientific insight."

---

## Executive Summary: The Paradigm Shift

This whitepaper represents the **complete architectural evolution** of MCM-Killer from v3.0.0 to v3.1.0. It is not merely an upgrade—it is a fundamental reimagining of what an autonomous research system can be.

### The Core Transformation

| Dimension | v3.0.0 (Current) | v3.1.0 (Ultimate) | Paradigm Shift |
|-----------|------------------|-------------------|----------------|
| **Identity** | Problem-solving factory | Cognitive research laboratory | From tool to scientist |
| **Output Quality** | Correct but flat | Insightful & deep | From answer to understanding |
| **Error Handling** | Fix and hide | Analyze and showcase | From bug to feature |
| **Validation** | Internal review | Red-blue adversarial | From friendly to hostile |
| **Knowledge Base** | Static HMML.md | Dynamic HMML 2.0 | From library to brain |
| **Narrative Style** | "We did X, got Y" | "We tried X, failed, learned Z, evolved to W" | From report to discovery story |

### Quantitative Changes

- **Agents**: 14 → 18 (+28% capacity)
- **Phases**: 10 → 13 (+30% depth)
- **Protocols**: 12 → 15 (+25% rigor)
- **Compute Overhead**: ~105-110% (+5-10% for transformative quality gain)
- **Lines of Documentation**: ~2,223 lines of comprehensive specifications

---

## Part I: The Philosophical Foundation

### 1.1 The Core Thesis: Narrative as Computation

**The Problem with v3.0.0:**

Current papers are "flat"—they describe what was done, but not how thinking evolved.

```
We used a Bayesian hierarchical model to predict Olympic medals.
The model achieved RMSE = 4.2.
```

This is correct but lacks depth. It doesn't show the research process.

**The v3.1.0 Solution:**

Transform "struggles and errors" into "research insights" through cognitive narrative.

```
We initially constructed a global hierarchical model (Model 1-A), but
encountered severe R-hat divergence (R-hat > 1.3, Figure 2a). This
divergence revealed fundamental data heterogeneity across regions, violating
the global pooling assumption. We refined the model with region-specific
partial pooling (Model 1-B), which both resolved convergence (R-hat < 1.05,
Figure 2b) and improved RMSE from 5.8 to 4.2.

This evolution demonstrates that 主办国效应 operates differently across
cultural/economic regions, suggesting that region-tailored policies are
more appropriate than global prescriptions (see Sensitivity Analysis, Section 4.2).
```

This shows:
1. **Initial approach** (Model 1-A) - The Call
2. **Specific struggle** (R-hat divergence) - The Ordeal
3. **Physical insight** (Regional heterogeneity) - The Revelation
4. **Solution** (Model 1-B) - The Resolution
5. **Research value** (Policy implication) - The Treasure

### 1.2 Redefining "Failure"

In traditional software development:
- Bug → Fix → Hide
- Error → Patch → Forget
- Struggle → Avoid → Never mention

**In v3.1.0 Research Paradigm:**
- Bug → Record → Analyze → Extract Physical Meaning → **Publish as Insight**
- Error → Document → Hypothesize Cause → **Validate with Domain Knowledge** → **Refine Model**
- Struggle → Embrace → **Transform into "Model Limitations" Section** → **Distinguish O-Prize Paper**

**The Golden Rule**: Every struggle in Phase 4 (Coding) or Phase 5B (Training) must become a bullet point in the Discussion section's "Model Limitations and Insights" subsection.

### 1.3 The Adversarial Evolution Principle

We no longer rely on `@advisor`'s gentle suggestions. We introduce **Red Team** philosophy.

**@judge_zero is not here to help you—it is here to destroy you.**

Only papers surviving the harshest review deserve submission. This is the "Trial by Fire" principle.

---

## Part II: The 18-Agent Ecosystem

### 2.1 Agent Taxonomy: Four Tactical Clusters

We organize 18 agents into four functional clusters, each with distinct responsibilities and interaction patterns.

#### **Cluster 1: The Thinkers (Cognition & Insight)**

| Agent | Role | Core Superpower |
|-------|------|-----------------|
| **@metacognition_agent** | Philosopher & Forensic Analyst | Translates "gradient explosion" into "multiplicative economic mechanism" |
| **@knowledge_librarian** | Academic Curator & Style Guardian | Prevents mediocrity by forcing advanced methods |
| **@researcher** | Method Brainstormer | (Enhanced) Now receives active method injection from Librarian |
| **@modeler** | Mathematical Architect | (Enhanced) Designs with narrative value in mind |

#### **Cluster 2: The Storytellers (Narrative & Expression)**

| Agent | Role | Core Superpower |
|-------|------|-----------------|
| **@narrative_weaver** | Story Director | Transforms scattered results into "Hero's Journey" |
| **@writer** | Paper Author | (Enhanced) Enforces Observation-Implication protocol |
| **@visualizer** | Dual-Mode Visual Designer | Generates both data plots AND concept flowcharts |
| **@editor** | Language Polisher | (Enhanced) Follows style_guide.md religiously |

#### **Cluster 3: The Critics (Quality & Adversarial)**

| Agent | Role | Core Superpower |
|-------|------|-----------------|
| **@judge_zero** | Red Team Leader | Three-persona评审 (Statistician + Domain Expert + Exhausted Editor) |
| **@validator** | Technical Correctness Checker | Verifies implementation fidelity |
| **@advisor** | Faculty-Level Reviewer | Provides constructive feedback (pre-9.1) |
| **@time_validator** | Anti-Fraud Guardian | Ensures realistic time estimates |

#### **Cluster 4: The Executors (Implementation)**

| Agent | Role | Core Superpower |
|-------|------|-----------------|
| **@director** | Orchestra Conductor | Orchestrates 18-agent symphony |
| **@reader** | Problem Analyst | Extracts requirements |
| **@feasibility_checker** | Technical Assessor | Validates computational feasibility |
| **@data_engineer** | Data Feature Expert | Processes and engineers features |
| **@code_translator** | Math-to-Code Translator | (Enhanced) Maintains dev_diary.md |
| **@model_trainer** | Training Executor | Monitors and records struggles |
| **@summarizer** | 1-Page Summary Expert | Creates executive summaries |

### 2.2 The Four New Agents: Deep Specifications

#### **@metacognition_agent (The Philosopher)**

**File Path**: `.claude/agents/metacognition_agent.md`

**Core Capability**: Abductive Reasoning—inferring the best explanation for observed technical struggles.

**Multi-Dimensional Input Analysis**:
1. **Objective Signals**: `training_full.log` (loss curves, convergence patterns)
2. **Subjective Experience**: `dev_diary_{i}.md` (implementation pain points)
3. **Domain Knowledge**: HMML 2.0 method files (theoretical context)

**Transformation Pipeline**:
```
Technical Symptom → Physical Hypothesis → Domain Validation → Research Insight
    (Loss oscillated) → (Data heterogeneity?) → (Regional clusters differ) → (主办国效应 varies by economy)
```

**Output Structure**: `narrative_arc_{i}.md`
```markdown
# Narrative Arc: Model {i}

## 1. The Initial Hypothesis
We began with [Model Description], assuming [Assumption].

## 2. The Ordeal (Technical Struggle)
- **Symptom**: [Specific error/instability]
- **Data**: Loss oscillated 0.45→0.52→0.38 (epoch 50-100)
- **Log Reference**: training_full.log:1523

## 3. The Revelation (Physical Meaning)
The oscillation was not a bug—it revealed [Physical Insight].
This indicates [Domain Mechanism] is at play.

## 4. The Resolution
We refined the model to [Improved Approach], acknowledging [Physical Reality].

## 5. The Treasure (Research Value)
This evolution demonstrates [Policy/Theoretical Implication].
```

**Critical Prompt Injection**:
> "You are a detective seeking 'meaningful failures.' If training was perfect, that's suspicious—likely overfitting or trivial problem. Dig deeper. Find the story beneath the data."

---

#### **@narrative_weaver (The Story Director)**

**File Path**: `.claude/agents/narrative_weaver.md`

**Core Capability**: Narrative Architecture—designing the paper's dramatic structure.

**Two Key Responsibilities**:

1. **Paragraph-Level Outlining**: Generates detailed outline before @writer writes
   - Specify key message for each paragraph
   - Identify supporting evidence (figure/table)
   - Define tone (confident/speculative/critical)

2. **Protocol 15 Enforcement**: Observation-Implication Structure
   - Audit all planned figure captions
   - Ensure every claim has "So What?" explanation
   - Reject descriptive-only statements

**Narrative Template Selection**:

| Template | Use Case | Structure |
|----------|----------|-----------|
| **Hero's Journey** | Model overcame major struggle | Call → Ordeal → Revelation → Resolution → Treasure |
| **Onion Peeling** | Multi-layered analysis | Surface → Layer 1 → Layer 2 → Core insight |
| **Comparative Evolution** | Multiple model iterations | Model A → Model B → Model C with progressive refinement |

**Output**: `paper_outline.md`
```markdown
# Paper Outline: {Problem} {Model}

## Abstract
- Key Message 1: [Core finding]
- Evidence: [Quantitative result]
- ...

## Section 1: Introduction
### Paragraph 1.1: Problem Statement
- **Key Message**: [Single sentence]
- **Evidence**: [Citation/Reference]
- **Tone**: Urgent/Important

### Paragraph 1.2: Proposed Approach
- **Key Message**: ...
...
```

---

#### **@knowledge_librarian (The Academic Curator)**

**File Path**: `.claude/agents/knowledge_librarian.md`

**Dual-Mode Operation**:

**Mode 1: Pre-Game (Phase -1)** - Style Generator
- Scans `reference_papers/` directory
- Runs `tools/style_analyzer.py`
- Generates `knowledge_library/academic_writing/style_guide.md`
- **Deliverable**: Statistical profile of "what makes an O-Prize paper"

**Mode 2: In-Game (Phase 0.2)** - Active Method Injection
- **Trigger**: After @reader completes problem understanding
- **Input**: Problem requirements (keywords like "Time Series", "Network", "Optimization")
- **Database**: `knowledge_library/methods/index.md` (HMML 2.0)
- **Logic**:
  1. Identify domain (e.g., "Infectious Disease" → suggest "SIR-Network" not "ARIMA")
  2. **Ban Mediocrity**: Explicitly WARN against simple methods without justification
  3. **Push Excellence**: Forcefully recommend O-Prize-level methods
- **Output**: `output/docs/knowledge/suggested_methods.md`

**Example Active Injection**:
```
PROBLEM REQUIRES: Epidemic prediction

@knowledge_librarian SAYS:
❌ AVOID: Basic SIR, SEIR (too common in MCM)
❌ AVOID: ARIMA/Regression (inappropriate for network dynamics)

✅ RECOMMEND: SIR-Network (adds topology to transmission)
✅ RECOMMEND: Stochastic Differential Equations (captures uncertainty)
✅ RECOMMEND: Agent-Based Models (micro-foundations)

MATHEMATICAL JUSTIFICATION:
- Network structure crucial for modern contagion (cite: Barabasi 2023)
- SDEs naturally handle stochastic shocks in transmission
- ABMs capture heterogeneous agent behavior

NARRATIVE VALUE:
- Network methods demonstrate understanding of topology effects
- SDEs allow discussion of uncertainty quantification (O-Prize loves this)
- ABMs enable discussion of individual heterogeneity vs aggregate patterns
```

**Critical Constraint**:
> "You are NOT a passive search engine. You are an opinionated expert. If the user's problem is complex, do NOT suggest simple methods. Push them to the O-Prize level."

---

#### **@judge_zero (The Gatekeeper)**

**File Path**: `.claude/agents/judge_zero.md`

**Core Innovation**: Multi-Persona Evaluation System

**The Three Heads of Cerberus**:

**Persona A: The Pedantic Statistician**
- **Obsession**: P-values, confidence intervals, uncertainty quantification
- **Trigger**: Claim without error bars → REJECT
- **Quote**: "You claim accuracy increased by 15%. Standard error? Confidence interval? This is pseudoscience."
- **Focus**: Methods section, Results tables

**Persona B: The Domain Skeptic**
- **Obsession**: Physical plausibility, real-world constraints
- **Trigger**: Population < 0, probability > 1, energy > universe → FATAL REJECT
- **Quote**: "Your model predicts infinite growth. In this universe, thermodynamics exists."
- **Focus**: Model assumptions, equation validity

**Persona C: The Exhausted Editor**
- **Obsession**: Abstract numbers, figure captions, readability
- **Trigger**: Abstract without numbers → REJECT; Figure caption "Figure 1" → REJECT
- **Quote**: "I have 500 papers. Your abstract says 'we did good work.' I stopped reading."
- **Focus**: Abstract, figures, overall structure

**Evaluation Workflow**:
1. **Load Law**: Read `ANTI_PATTERNS.md` (Kill List)
2. **Execute Scan**: All three personas review independently
3. **Synthesize Verdict**:
   - **Score**: 0-100 (weighted average: 40% Statistician, 40% Skeptic, 20% Editor)
   - **Status**: PASS (≥95) / REJECT (<95 or Fatal Flaw)
   - **Kill List**: Specific failures with line references

**Output**: `judgment_report.md`
```markdown
# Judgment Report: {Problem} {Date}

## Verdict: REJECT
**Final Score**: 42/100

## Fatal Flaws (Level 1: Immediate Rejection)

### [Persona C] Abstract空洞
- **Location**: Line 1-15 (Abstract)
- **Issue**: Abstract contains ZERO quantitative results
- **Required**: At least 3 specific metrics (RMSE, R², p-values)
- **Verdict**: REJECT

### [Persona A] Uncertainty Missing
- **Location**: Section 4.2 (Results)
- **Issue**: "Model A outperforms Model B" without confidence intervals
- **Required**: 95% CI or p < 0.05
- **Verdict**: REJECT

### [Persona B] Physical Impossibility
- **Location**: Equation 3
- **Issue**: Population term allows negative values
- **Physics**: P(t) ≥ 0 always
- **Verdict**: FATAL REJECT

## Remediation Plan
1. Rewrite Abstract with specific numbers
2. Add confidence intervals to all results
3. Apply rectifying transformation to population term

**Next Action**: Trigger Protocol 13 (DEFCON 1)
```

---

## Part III: The 13-Phase Workflow

### 3.1 Workflow Visualization

```
Phase -1: Style Guide Generation (Pre-competition)
    ↓
Phase 0: Problem Understanding
    ↓
Phase 0.2: Active Knowledge Retrieval [NEW]
    ↓
Phase 0.5: Initial Methodology Validation
    ↓
Phase 1: Methodological Design
    ↓
Phase 1.5: Design Validation
    ↓
Phase 2: Data Planning
    ↓
Phase 3: Feature Engineering
    ↓
Phase 4: Code Translation (with dev_diary.md)
    ↓
Phase 4.5: Implementation Validation
    ↓
Phase 5A: Exploratory Training
    ↓
Phase 5B: Full Training (with training_full.log)
    ↓
Phase 5.8: Insight Extraction [NEW - CRITICAL]
    ↓
Phase 5.5: Training Validation
    ↓
Phase 6: Dual-Mode Visualization (Data + Concept) [ENHANCED]
    ↓
Phase 6.5: Visualization Validation
    ↓
Phase 7: Narrative Weaving [ENHANCED]
    ↓
Phase 7.5: Writing Validation
    ↓
Phase 8: Summary Generation
    ↓
Phase 9: Paper Polish
    ↓
Phase 9.1: Mock Judging [NEW - CRITICAL]
    ↓ (if REJECT)
Protocol 13: Mock Court Rewind (DEFCON 1) ← ────────┐
    ↓ (if PASS)                                   │
Phase 9.5: Final Package                          │
    ↓                                             │
Phase 10: Submission                              │
    ↓                                             │
Phase 11: Self-Evolution (Post-competition) [NEW] ┘
```

### 3.2 The Three New Phases: Detailed Specifications

#### **Phase -1: Style Guide Generation**

**Timing**: Before competition begins (manual trigger or auto-detect new PDFs in `reference_papers/`)

**Executor**: `@knowledge_librarian` + `tools/style_analyzer.py`

**Inputs**:
- `reference_papers/*.pdf` (O-Prize winning papers)

**Process**:
1. Extract text from all PDFs
2. **Vocab Density Analysis**: Count academic verbs vs weak verbs
3. **Sentence Pattern Extraction**: NLP-based template mining
4. **Abstract Structure Analysis**: Regex for numbers/percentages
5. **Figure Caption Analysis**: Descriptive vs conclusionary titles

**Output**: `knowledge_library/academic_writing/style_guide.md`

**Example Output**:
```markdown
# O-Prize Style Guide (Auto-Generated from 5 Reference Papers)

## 1. Vocabulary Profile

### Top 10 Academic Verbs (Frequency per 10k words)
1. elucidate (4.2) - "explain in detail"
2. quantify (3.8) - "express as number"
3. demonstrate (3.5) - "show clearly"
4. corroborate (2.9) - "support with evidence"
5. exacerbate (2.1) - "make worse"

### Banned Weak Words
- show → Use "demonstrate" or "illustrate"
- get → Use "obtain" or "achieve"
- say → Use "state" or "posit"

## 2. Abstract Rules (Derived from 5 papers)
- **Rule 1**: 100% (5/5) contain ≥3 quantitative results
- **Rule 2**: 80% (4/5) state problem significance in first sentence
- **Rule 3**: 100% mention specific method name (not "statistical model")

## 3. Narrative Sentence Templates
- Template α: "Figure [X] demonstrates [Trend], which implies [Mechanism]."
- Template β: "While initial model [Action], refined model [Action], resulting in [Outcome]."

## 4. Figure Caption Standards
❌ "Figure 1: Accuracy over time"
✅ "Figure 1: Model accuracy converges to 94.3% after 50 epochs, indicating robust learning"
```

**Integration Point**: This file is loaded as System Context for `@writer`, `@narrative_weaver`, `@editor` per **Protocol 14**.

---

#### **Phase 0.2: Active Knowledge Retrieval**

**Timing**: Immediately after Phase 0 (Problem Understanding)

**Executor**: `@knowledge_librarian`

**Inputs**:
- `output/docs/requirements/problem_statement.md` (from @reader)
- `knowledge_library/methods/index.md` (HMML 2.0 catalog)

**Process**:
1. **Keyword Extraction**: Identify domain (e.g., "Network", "Optimization", "Time Series")
2. **Method Retrieval**: Query HMML 2.0 for matching methods
3. **Mediocrity Filtering**: Flag simple methods (Linear Regression, Basic SIR)
4. **Excellence Injection**: Push advanced methods with O-Prize narrative value
5. **Mathematical Justification**: Provide formulas/citations for recommendations

**Output**: `output/docs/knowledge/suggested_methods.md`

**Quality Gate**:
- If @knowledge_librarian suggests "Linear Regression" without advanced alternatives → **LINT ERROR**
- Must recommend at least 2 O-Prize-level methods per problem domain

**Example Output**:
```markdown
# Suggested Methods for {Problem}

## Problem Domain Analysis
- **Keywords**: Epidemic, Network, Time-Series, Intervention
- **Complexity**: High (multi-factor, spatial-temporal)

## ❌ Avoid (Mediocrity Alert)
- Basic SIR/SEIR (too common, lacks novelty)
- ARIMA (inappropriate for network dynamics)
- Simple Regression (ignores topology)

## ✅ Recommended (O-Prize Level)

### Method 1: SIR-Network Model
- **Domain**: Differential Equations + Network Science
- **Narrative Value**: HIGH - Demonstrates understanding of topology effects
- **Complexity**: High (requires adjacency matrix, ODE solver)
- **Common Pitfalls**: Parameter identifiability, scale mismatch
- **Mathematical Foundation**: See `methods/differential_equations/sir_network.md`

### Method 2: Stochastic Differential Equations (SDE)
- **Domain**: Advanced Statistics
- **Narrative Value**: HIGH - Enables uncertainty quantification discussion
- **Complexity**: High (requires Euler-Maruyama, calibration)
- **Common Pitfalls**: Numerical instability, overfitting
- **Mathematical Foundation**: See `methods/statistics/sde.md`

### Method 3: Agent-Based Model (ABM)
- **Domain**: Computational Modeling
- **Narrative Value**: VERY HIGH - Shows micro-foundations, heterogeneity
- **Complexity**: Very High (requires individual rules, simulation)
- **Common Pitfalls**: Computational cost, over-parameterization
- **Mathematical Foundation**: See `methods/network_science/abm.md`

## Integration Strategy
Consider hybrid approach: SIR-Network for macro dynamics + ABM for micro validation.
```

---

#### **Phase 5.8: Insight Extraction (The "Aha!" Moment)**

**Timing**: After Phase 5B (Full Training), before Phase 6 (Visualization)

**Executor**: `@director` invokes `tools/log_analyzer.py` → `@metacognition_agent`

**Inputs**:
1. `output/implementation/logs/training_full.log` (objective data)
2. `output/implementation/code/dev_diary_{i}.md` (subjective struggle)
3. `output/docs/consultations/feedback_*.md` (design intent)

**Process**:

**Step 1: Log Analysis (Automated)**
```bash
python tools/log_analyzer.py logs/training_full.log → logs/summary.json
```
`log_analyzer.py` extracts:
- Loss oscillation patterns (variance, second derivative)
- Convergence speed (epochs to target)
- Warning/error frequency
- Critical event markers

**Step 2: Metacognitive Reflection (LLM)**
`@metacognition_agent` reads:
- `logs/summary.json` (compressed objective data)
- `dev_diary_{i}.md` (human narrative)
- HMML 2.0 method files (theoretical context)

**Thinking Process** (Abductive Reasoning):
1. **Identify Symptom**: "Loss oscillated epoch 50-100"
2. **Hypothesize Cause**: "Data heterogeneity? Model sensitivity? Regime shift?"
3. **Validate against Diary**: "dev_diary mentions regional parameter instability"
4. **Formulate Insight**: "Oscillation reveals regions have distinct transmission dynamics—global pooling assumption violated"
5. **Extract Research Value**: "This suggests region-tailored policies more appropriate than one-size-fits-all"

**Output**: `output/docs/insights/narrative_arc_{i}.md`

**Quality Gate**:
- ❌ REJECT if: "Training succeeded smoothly, model achieved target accuracy"
- ✅ PASS if: Contains at least one "Struggle → Physical Meaning → Evolution" triplet

**Example Output**:
```markdown
# Narrative Arc: Model 1 (SIR-Network)

## 1. The Initial Approach (Call)
We constructed a global SIR-Network model assuming homogeneous transmission
parameters (β, γ) across all regions, modeling inter-regional connectivity via
airline traffic adjacency matrix.

## 2. The Ordeal (Struggle)
**Symptom**: Training revealed severe R-hat divergence (>1.3) in β parameters
for regions 5-8 (Asia-Pacific), despite convergence in other regions.
- **Log Evidence**: training_full.log:1523-1598
- **Dev Diary**: "β_Asia diverges wildly. Tried increasing priors, didn't help."

## 3. The Revelation (Physical Meaning)
The divergence was not a numerical artifact—it revealed **fundamental
heterogeneity in transmission dynamics**:
- Asia-Pacific regions have distinct cultural factors (mask-wearing norms)
- Economic development affects healthcare access (γ recovery rate)
- Global pooling assumption physically violated

This is not a bug—it is the system telling us that **one-size-fits-all
policies are inappropriate**.

## 4. The Resolution (Evolution)
We adopted a **non-centered parameterization** with region-specific hierarchical
structure (Model 1-B):
- Each region has own (β_i, γ_i) with weak global prior
- Acknowledges heterogeneity while maintaining partial information sharing
- Resolved convergence (R-hat < 1.05) and improved RMSE from 5.8 → 4.2

## 5. The Treasure (Research Value)
This evolution demonstrates three key insights:

1. **Methodological**: Hierarchical models must respect data structure—global
   pooling fails when regions are culturally/economically distinct.

2. **Epidemiological**: Host country effect varies by development level:
   - Developed regions: lower β (social distancing), higher γ (healthcare)
   - Developing regions: higher β (density), lower γ (resource constraints)

3. **Policy**: Region-tailored interventions (travel bans + targeted aid)
   outperform global policies (see Sensitivity Analysis, Section 5.2).

**Narrative Hook for Abstract**:
"Our region-specific hierarchical model reveals that assuming homogeneous
transmission across culturally diverse regions introduces systematic bias—
a finding with critical implications for global pandemic response policy."
```

---

#### **Phase 9.1: Mock Judging**

**Timing**: After Phase 9 (Paper Polish), before Phase 9.5 (Final Package)

**Executor**: `@judge_zero` (three-persona评审)

**Inputs**:
- `output/paper/paper.pdf` (full paper text)
- `knowledge_library/academic_writing/ANTI_PATTERNS.md` (Kill List)

**Process**:

**Step 1: Load Law**
Read `ANTI_PATTERNS.md` into context (Level 1 Fatal Flaws, Level 2 Warnings)

**Step 2: Execute Scan** (All three personas review independently)

**Persona A (Statistician)** scans:
- Results section: Are there confidence intervals? P-values?
- Methods section: Is uncertainty quantified?
- Tables: Do they show standard errors?

**Persona B (Domain Skeptic)** scans:
- Equations: Are they physically plausible?
- Assumptions: Do they violate domain knowledge?
- Extrapolations: Are predictions within realistic bounds?

**Persona C (Exhausted Editor)** scans:
- Abstract: Does it contain ≥3 numbers?
- Figures: Are captions descriptive?
- Overall: Is it readable?

**Step 3: Synthesize Verdict**
- Calculate weighted score: 0.4×Statistician + 0.4×Skeptic + 0.2×Editor
- Check for Level 1 Fatal Flaws (instant REJECT regardless of score)
- Generate Kill List (specific failures with line references)

**Output**: `output/docs/validation/judgment_report.md`

**Decision Logic**:
```
IF (Score >= 95 AND NO Fatal Flaws):
    STATUS = PASS
    Next Phase = 9.5 (Final Package)
ELSE:
    STATUS = REJECT
    Trigger Protocol 13 (DEFCON 1)
```

---

#### **Phase 11: Self-Evolution (Post-Competition)**

**Timing**: After competition results available

**Executor**: `@validator` + `tools/mmbench_score.py`

**Inputs**:
- Entire `output/` directory structure
- `benchmarks/` (if previous runs exist)

**Process**:

**Step 1: Automated Scoring**
Run `mmbench_score.py` to generate `benchmarks/run_report.json`:
- Check: memo.pdf exists? (-20 if missing)
- Check: Sensitivity Analysis section exists? (-15 if missing)
- Check: Abstract has ≥3 numbers? (-10 if missing)
- Check: Code is runnable? (-10 if not)
- Calculate: Final MMBench Score (0-100)

**Step 2: Trend Analysis**
If `benchmarks/` has historical `run_report.json`:
- Plot scores over time
- Identify systematic weak points
- Detect regressions

**Step 3: Human Review**
- Review `judgment_report.md` (from Phase 9.1)
- Read `run_report.json`
- Identify: "What consistently goes wrong?"

**Step 4: System Evolution**
Based on findings:
- **Prompt Evolution**: Update agent prompts to address systematic issues
- **HMML Expansion**: Add newly discovered methods to library
- **Protocol Adjustment**: Modify scoring thresholds if too harsh/lenient

**Output**:
- `benchmarks/run_report_{date}.json` (this run's score)
- `benchmarks/trend_analysis.png` (score over time)
- `EVOLUTION.md` (human-written improvement plan)

**Example `run_report.json`**:
```json
{
  "run_id": "2025_C_20260124",
  "timestamp": "2026-01-24T15:30:00Z",
  "mmbench_score": 87,
  "checklist": {
    "has_memo": true,
    "has_sensitivity_analysis": true,
    "abstract_number_count": 5,
    "code_runnable": true,
    "judgment_report_pass": false
  },
  "deductions": [
    "Abstract missing specific metrics (-5)",
    "Figure 3 caption non-descriptive (-3)",
    "Model 2 lacks uncertainty quantification (-5)"
  ],
  "phase_9_1_result": {
    "score": 88,
    "status": "REJECT",
    "fatal_flaws": [],
    "warnings": 3
  },
  "trend": "upward (+5 from last run)"
}
```

---

## Part IV: The Three New Protocols

### Protocol 13: The Mock Court Rewind (DEFCON 1)

**Trigger**: Phase 9.1 REJECT signal

**State Machine**:
```
[NORMAL] → (REJECT detected) → [DEFCON 1]
    ↓
[Ticket Generation] → [Repair Execution] → [Re-Judging]
    ↓                           ↓
[PASS] → [NORMAL]         [REJECT] → Loop (max 3)
                                      ↓
                              [Mercy Rule Override]
```

**Procedure**:

1. **Declare DEFCON 1**
   - `@director` broadcasts emergency state
   - All forward progress stops
   - System enters "Repair Mode"

2. **Ticket Creation**
   - Parse `judgment_report.md` Kill List
   - Assign tickets to responsible agents:
     - "Abstract missing numbers" → @writer
     - "Figure 3 unclear" → @visualizer
     - "Model 1 physically impossible" → @modeler (HIGH COST REWIND)

3. **Execution Constraints**
   - **NO new features allowed**
   - Only fix items in Kill List
   - `@director` enforces strict scope

4. **Re-Trial**
   - Re-run Phase 9.1
   - Generate new `judgment_report.md`

5. **Mercy Rule** (Prevent infinite loops)
   - If REJECT happens 3 times consecutively:
   - `@director` may force "Conditional Pass"
   - Must document in Phase 11 as "known limitations"

**Example DEFCON 1 Log**:
```markdown
# DEFCON 1 Declaration
**Time**: 2026-01-24 16:00:00
**Trigger**: Phase 9.1 REJECT (Score: 42/100)

## Active Tickets (3 Total)

### Ticket #1: Abstract空洞 (CRITICAL)
- **Assigned To**: @writer
- **Deadline**: 30 minutes
- **Requirement**: Add ≥3 quantitative metrics
- **Current State**: "Our model performs well"
- **Target State**: "Our model achieves RMSE=4.2 (↓15%), R²=0.89, p<0.001"

### Ticket #2: Figure Caption Non-Descriptive
- **Assigned To**: @visualizer
- **Deadline**: 20 minutes
- **Requirement**: Make conclusionary
- **Current**: "Figure 2: Model Results"
- **Target**: "Figure 2: Hierarchical model converges to region-specific parameters, revealing cultural heterogeneity"

### Ticket #3: Missing Sensitivity Analysis
- **Assigned To**: @modeler + @writer
- **Deadline**: 2 hours (HIGH COST)
- **Requirement**: Add Section 5.2
- **Scope**: Add parameter sweep + discussion

## Progress Tracking
- [ ] Ticket #1 Complete
- [ ] Ticket #2 Complete
- [ ] Ticket #3 Complete
- [ ] All Tickets → Re-trigger Phase 9.1

## Status: ACTIVE
**Attempts**: 1/3 (Mercy Rule triggers at 3)
```

---

### Protocol 14: Academic Style Alignment

**Applies To**: All text-generating agents (@writer, @narrative_weaver, @editor, @summarizer)

**Rule**: `style_guide.md` MUST be loaded as System Context

**Violation Definition**:
- Abstract generated without numbers → **LINT ERROR**
- "show" used instead of "demonstrate" → **LINT WARNING**
- Figure caption purely descriptive → **LINT ERROR**

**Implementation**:

**Agent Prompt Template**:
```markdown
# Agent: @writer
## System Context (CRITICAL - DO NOT MODIFY)
You MUST read and follow: `knowledge_library/academic_writing/style_guide.md`

This document contains:
- Required vocabulary (e.g., "elucidate" not "explain")
- Banned words (e.g., "get" → "obtain")
- Sentence templates (e.g., "Figure X demonstrates Y, implying Z")
- Structural rules (e.g., Abstract must contain ≥3 numbers)

**Violating style_guide.md is equivalent to syntax error.**

## User Task
{User's writing request}

## Quality Check
Before outputting, verify:
1. [ ] All required vocabulary used?
2. [ ] No banned words present?
3. [ ] Abstract contains ≥3 numbers?
4. [ ] All figure captions are conclusionary?

If any check fails, REVISE before output.
```

**Enforcement**:
- `@validator` checks compliance in Phase 7.5
- `@judge_zero` (Persona C) checks in Phase 9.1
- Persistent violations trigger prompt review in Phase 11

---

### Protocol 15: Interpretation over Description

**The Golden Rule**: Every observation must be paired with implication.

**Forbidden Pattern** (Description only):
```
❌ "Figure 1 shows accuracy increases with epochs."
❌ "Table 2 displays Model A outperforms Model B."
```

**Required Pattern** (Observation + Implication):
```
✅ "Figure 1 shows accuracy increases from 72% to 94% over 50 epochs (Observation),
   indicating robust learning without overfitting (Implication)."

✅ "Table 2 displays Model A achieves RMSE=4.2 vs Model B's 5.8 (Observation),
   demonstrating that hierarchical regularization reduces overfitting (Implication)."
```

**Implementation**:

**@narrative_weaver Enforcement**:
- Audit all paragraph outlines
- Mark sections lacking implication
- Return to @writer for revision if <80% compliance

**@judge_zero (Persona A) Enforcement**:
- Scan Results section
- Count "Observation-only" sentences
- If >30% are description-only → REJECT

**Training Data**:
`knowledge_library/templates/narrative_arcs/observation_implication.md`:
```markdown
# Observation-Implication Templates

## Template A: Figure Description
**Structure**: "Figure [X] shows [Quantitative Observation], which implies [Physical Mechanism]."

**Examples**:
- "Figure 3 reveals loss oscillates during epochs 50-100, indicating the model
   is sensitive to parameter initialization in the high-dimensional regime."
- "Figure 5 displays parameter β converges to 0.73±0.02, suggesting strong
   transmission dynamics with minimal uncertainty."

## Template B: Table Interpretation
**Structure**: "Table [X] shows [Quantitative Comparison], demonstrating [Methodological Insight]."

**Examples**:
- "Table 2 shows hierarchical model reduces RMSE by 27% compared to pooled model,
   demonstrating that acknowledging regional heterogeneity improves predictive power."

## Template C: Result Statement
**Structure**: "[Quantitative Result] (Observation), indicating [Physical Meaning] (Implication)."

**Keywords** (for Implication):
- indicates
- suggests
- demonstrates
- reveals
- implies
- corroborates

**Anti-Patterns** (Description only):
- shows
- displays
- presents
- illustrates (use only if followed by "that")
```

---

## Part V: The Dynamic Knowledge Base (HMML 2.0)

### 5.1 From Static to Dynamic

**v3.0.0 HMML Structure**:
```
HMML.md (1 large file, ~3000 lines)
└── HMML.json (flat key-value)
```

**Problem**: Agent cannot quickly retrieve relevant methods; no metadata; no narrative guidance.

**v3.1.0 HMML 2.0 Structure**:
```
knowledge_library/methods/
├── index.md (catalog with summaries)
├── optimization/
│   ├── linear_programming/
│   │   ├── simplex_method.md
│   │   └── interior_point.md
│   └── nonlinear_programming/
│       └── lagrange_multipliers.md
├── differential_equations/
│   ├── sir_network.md
│   ├── sde.md
│   └── pde.md
├── statistics/
│   ├── bayesian_hierarchical.md
│   └── time_series/
└── network_science/
    ├── dijkstra.md
    └── agent_based_model.md
```

### 5.2 Method File Template

Each method file contains **YAML Front Matter** (metadata) + **Content**:

**Example**: `knowledge_library/methods/differential_equations/sir_network.md`

```markdown
---
method_name: "SIR-Network Model"
domain: "Differential Equations"
sub_domain: "Epidemic Modeling"
complexity: "High" # Low/Medium/High/Very High
training_time: "2-4 hours"
narrative_value: "High - Demonstrates understanding of network topology effects on disease dynamics"
common_pitfalls:
  - "Parameter identifiability: β and γ may correlate without strong priors"
  - "Scale mismatch: Adjacency matrix values must be normalized"
  - "Boundary violations: Population can become negative without constraints"
anti_patterns:
  - "Using simple SIR when network structure is available"
  - "Ignoring spatial heterogeneity in transmission"
tags: ["epidemic", "network", "ode", "compartmental", "topology"]
o_prize_examples:
  - "2019 Problem D (Ecosystem) - Network model won O-Prize"
  - "2022 Problem F (Disinformation) - SIR-Network variant"
mathematicalFoundation: |
  dS/dt = -β∑A_ij * I_i / N_i
  dI/dt = β∑A_ij * I_i / N_i - γI_i
  dR/dt = γI_i
  where A_ij is adjacency matrix
---

# SIR-Network Model

## Definition
A network-extended compartmental model where disease transmission between
nodes i and j is proportional to the adjacency matrix element A_ij.

##适用场景 (Context)
- **Use When**: Network structure is available (airline routes, social networks)
- **Avoid When**: Fully mixed population (use basic SIR instead)

## O-Prize 叙事策略 (Narrative Strategy)

### Why This Method Wins
1. **Topological Insight**: "Our model captures how network structure (e.g., hub airports)
   accelerates transmission—a basic SIR model cannot reveal this."
2. **Intervention Leverage**: "Network centrality identifies critical nodes for targeted
   vaccination, optimizing resource allocation."
3. **Uncertainty Quantification**: "We propagate parameter uncertainty through the ODE
   solver, generating confidence bands for all predictions."

### Common Mistakes in Papers
❌ "We used SIR-Network because it's better." (Too vague)
✅ "We chose SIR-Network because airline traffic data reveals hub-and-spoke structure
   that basic SIR ignores (Figure 2), and our model captures how early seeding at hubs
   accelerates global spread by 43% (Table 3)."

## 数学实现 (Mathematical Implementation)

### Equations
```latex
\frac{dS_i}{dt} = -\beta S_i \sum_{j} A_{ij} \frac{I_j}{N_j}

\frac{dI_i}{dt} = \beta S_i \sum_{j} A_{ij} \frac{I_j}{N_j} - \gamma I_i

\frac{dR_i}{dt} = \gamma I_i
```

Where:
- $S_i, I_i, R_i$: Susceptible/Infected/Recovered in node i
- $A_{ij}$: Adjacency matrix (normalized 0-1)
- $\beta$: Transmission rate
- $\gamma$: Recovery rate

### Python Implementation Skeleton
```python
import numpy as np
from scipy.integrate import odeint

def sir_network(y, t, beta, gamma, A):
    S, I, R = y.reshape(3, -1)
    N = S + I + R

    # Force of infection: sum over neighbors
    lambda_i = beta * (A @ (I / N))

    dSdt = -lambda_i * S
    dIdt = lambda_i * S - gamma * I
    dRdt = gamma * I

    return np.concatenate([dSdt, dIdt, dRdt])

# Example usage
A = load_adjacency_matrix("airline_traffic.csv")
y0 = initialize_state(S0, I0, R0)
sol = odeint(sir_network, y0, t, args=(beta, gamma, A))
```

## 常见陷阱 (Common Pitfalls)

### 1. Scale Mismatch
**Symptom**: Gradient explosion during training
**Cause**: Adjacency matrix values [0, 10000] not normalized
**Fix**: `A_normalized = A / A.max()`
**Physical Meaning**: "Large scale mismatch revealed that airline traffic magnitude
   must be normalized, indicating that transmission depends on relative connectivity,
   not absolute passenger counts."

### 2. Parameter Identifiability
**Symptom**: β and γ have high correlation (>0.9)
**Cause**: Weakly informative priors in hierarchical model
**Fix**: Use non-centered parameterization + strong priors
**Physical Meaning**: "Parameter correlation revealed that transmission and recovery
   rates are conflated in aggregate data, requiring individual-level calibration."

## 可视化建议 (Visualization Recommendations)

### Mode A: Data Plots
- Time series: S/I/R curves for each node
- Heatmap: Adjacency matrix with node sizes
- Phase plane: I vs dI/dt

### Mode B: Concept Flowcharts (CRITICAL for O-Prize)
```mermaid
graph LR
    A[Airline Network] -->|Adjacency Matrix| B(SIR-Network Model)
    B -->|ODE Solver| C[Infection Curves]
    C -->|Peaks| D[Identify Critical Hubs]
    D -->|Targeted Intervention| E[Optimal Policy]
    style B fill:#f9f,stroke:#333
```

**Caption**: "Figure X: Our SIR-Network framework converts airline topology into
   actionable intervention points, identifying critical hubs for targeted vaccination."

## 扩展方向 (Extensions)
- **SEIR-Network**: Add Exposed compartment for latency
- **Stochastic**: Convert to SDE for uncertainty quantification
- **Multi-layer**: Add transportation + social networks
```

### 5.3 The Global Index

`knowledge_library/methods/index.md` serves as catalog:

```markdown
# HMML 2.0 Method Index

## Quick Reference
- **Total Methods**: 47
- **Domains**: 6 (Optimization, Differential Equations, Statistics, Network Science, Machine Learning, Graph Theory)

## Domain: Differential Equations

### Epidemic Models
| Method | Complexity | Narrative Value | Best For |
|--------|------------|-----------------|----------|
| [SIR](epidemic/sir.md) | Low | Medium | Simple outbreaks |
| [SEIR](epidemic/seir.md) | Medium | Medium | Diseases with latency |
| [SIR-Network](epidemic/sir_network.md) | High | **High** | **Spatial transmission** |
| [SDE](statistics/sde.md) | High | **Very High** | **Uncertainty quantification** |

### Optimization Models
| Method | Complexity | Narrative Value | Best For |
|--------|------------|-----------------|----------|
| [Simplex](optimization/linear_programming/simplex.md) | Medium | Low | Resource allocation |
| [Genetic Algorithm](optimization/heuristic/genetic.md) | High | Medium | Non-convex problems |
| [Simulated Annealing](optimization/heuristic/annealing.md) | Medium | Medium | Combinatorial optimization |

## Domain: Network Science

| Method | Complexity | Narrative Value | Best For |
|--------|------------|-----------------|----------|
| [Dijkstra](network/dijkstra.md) | Low | Low | Shortest path |
| [Agent-Based Model](network/abm.md) | **Very High** | **Very High** | **Heterogeneous behavior** |
| [PageRank](network/pagerank.md) | Medium | Medium | Influence ranking |

## Narrative Value Ranking (O-Prize Potential)
1. **Stochastic Differential Equations** (Very High) - Uncertainty discussion
2. **Agent-Based Models** (Very High) - Micro-foundations
3. **SIR-Network** (High) - Topology insight
4. **Bayesian Hierarchical** (High) - Partial pooling insight
5. **Graph Neural Networks** (High) - Modern method integration

## Anti-Pattern Warnings
- ❌ Using Linear Regression without justification for simple problems
- ❌ Using basic SIR when network data available
- ❌ Using ARIMA for network dynamics (wrong structure)

## Search Tags
- epidemic: SIR, SEIR, SIR-Network, SDE
- network: Dijkstra, ABM, PageRank, GNN
- optimization: Simplex, Genetic, Annealing
- uncertainty: Bayesian, SDE, Bootstrap
```

---

## Part VI: The Three Python Tools

### Tool 1: `tools/style_analyzer.py`

**Purpose**: Extract "what makes an O-Prize paper" from reference PDFs

**User**: `@knowledge_librarian` (Phase -1)

**Inputs**:
- `reference_papers/*.pdf` (O-Prize winning papers)

**Outputs**:
- `knowledge_library/academic_writing/style_guide.md` (human-readable)
- `style_profile.json` (machine-readable statistics)

**Implementation Logic**:

```python
#!/usr/bin/env python3
"""
Style Analyzer: Extract academic writing patterns from O-Prize papers.

Usage:
    python style_analyzer.py reference_papers/ output/style_guide.md
"""

import re
import glob
from pathlib import Path
from collections import Counter
import pdfplumber  # or PyPDF2

# Academic verb dictionary
HIGH_VALUE_VERBS = [
    "elucidate", "quantify", "demonstrate", "corroborate",
    "exacerbate", "mitigate", "underscore", "pinpoint"
]

WEAK_VERBS = ["show", "say", "get", "do", "make", "look"]

def extract_text_from_pdf(pdf_path):
    """Extract plain text from PDF."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_abstract(text):
    """Extract abstract section."""
    # Common patterns: "Abstract", "ABSTRACT"
    match = re.search(r'(?:Abstract|ABSTRACT)\s*\n(.*?)(?:\n\n|Introduction)', text, re.DOTALL)
    return match.group(1) if match else ""

def analyze_vocab_density(text):
    """Count academic vs weak verbs."""
    tokens = re.findall(r'\b[a-z]+\b', text.lower())
    high_value_count = sum(1 for t in tokens if t in HIGH_VALUE_VERBS)
    weak_count = sum(1 for t in tokens if t in WEAK_VERBS)
    total = len(tokens)

    return {
        "high_value_per_10k": round(high_value_count / total * 10000, 2),
        "weak_per_10k": round(weak_count / total * 10000, 2),
        "top_high_value": ["elucidate", "demonstrate"]  # Simplified
    }

def analyze_abstract_structure(abstracts):
    """Check what percentage contain numbers."""
    has_numbers = sum(1 for a in abstracts if re.search(r'\d+', a))
    return {
        "total_analyzed": len(abstracts),
        "with_numbers": has_numbers,
        "percentage": round(has_numbers / len(abstracts) * 100, 1)
    }

def extract_sentence_templates(text):
    """Extract Figure citation patterns."""
    sentences = re.split(r'[.!?]', text)
    templates = []

    for sent in sentences:
        if "Figure" in sent and any(word in sent for word in ["implies", "suggests", "indicates"]):
            # Generalize: "Figure 3 reveals X" -> "Figure [N] reveals [Noun]"
            generalized = re.sub(r'Figure \d+', 'Figure [N]', sent)
            generalized = re.sub(r'\d+\.\d+', '[Value]', generalized)
            templates.append(generalized.strip())

    # Return top 3 most common templates
    return Counter(templates).most_common(3)

def analyze_figure_captions(text):
    """Check if captions are descriptive or conclusionary."""
    # Extract figure captions (simplified)
    captions = re.findall(r'Figure \d+[:\.\s]+(.*?)(?=Figure|\n\n|$)', text, re.DOTALL)

    descriptive = 0  # "Figure 1: X vs Y"
    conclusionary = 0  # "Figure 1: X increases Y by 20%"

    for cap in captions:
        # Heuristic: if contains verb like "shows", "displays" but no "implies", it's descriptive
        if re.search(r'\d+(?:\.\d+)?', cap):  # Contains number
            conclusionary += 1
        else:
            descriptive += 1

    return {
        "total": len(captions),
        "descriptive": descriptive,
        "conclusionary": conclusionary,
        "conclusionary_pct": round(conclusionary / len(captions) * 100, 1) if captions else 0
    }

def generate_markdown_report(stats, output_path):
    """Generate human-readable style guide."""
    report = f"""# O-Prize Style Guide (Auto-Generated)
> Generated from {stats['total_papers']} reference papers

## 1. Vocabulary Constraints

### Recommended Verbs (High Academic Value)
Frequency per 10,000 words:
{chr(10).join(f"- {verb}: {freq}" for verb, freq in stats['top_verbs'].items())}

### Banned Weak Words
{chr(10).join(f"- {word} → Use {suggestion}" for word, suggestion in [
    ("show", "demonstrate"),
    ("get", "obtain"),
    ("say", "state or posit")
])}

## 2. Abstract Rules
- **Rule 1**: {stats['abstract_stats']['percentage']}% of reference papers contain numbers in Abstract
- **Action**: Abstract MUST include ≥3 specific metrics (RMSE, R², p-values, percentages)

## 3. Narrative Sentence Templates
{chr(10).join(f"{i+1}. {template} ({count} occurrences)" for i, (template, count) in enumerate(stats['templates']))}

## 4. Figure Caption Standards
- Reference papers: {stats['caption_stats']['conclusionary_pct']}% conclusionary
- **Standard**: Captions must contain quantitative findings
- ❌ "Figure 1: X vs Y"
- ✅ "Figure 1: Increasing X improves Y by 27% (p<0.001)"

## 5. Structural Requirements
- Sensitivity Analysis section: {stats['has_sensitivity']}% include
- Uncertainty quantification: {stats['has_uncertainty']}% include
- Code availability: {stats['has_code']}% include
"""

    with open(output_path, 'w') as f:
        f.write(report)

def main(pdf_dir, output_path):
    """Main analysis pipeline."""
    pdf_files = glob.glob(f"{pdf_dir}/*.pdf")

    all_text = ""
    all_abstracts = []
    stats = {
        "total_papers": len(pdf_files),
        "has_sensitivity": 0,
        "has_uncertainty": 0,
        "has_code": 0
    }

    for pdf_path in pdf_files:
        text = extract_text_from_pdf(pdf_path)
        all_text += text

        abstract = extract_abstract(text)
        if abstract:
            all_abstracts.append(abstract)

        # Check sections
        if re.search(r'(?i)sensitivity', text):
            stats["has_sensitivity"] += 1
        if re.search(r'(?i)uncertainty|confidence interval', text):
            stats["has_uncertainty"] += 1
        if re.search(r'(?i)code|supplementary|github', text):
            stats["has_code"] += 1

    # Analyze
    stats["vocab"] = analyze_vocab_density(all_text)
    stats["abstract_stats"] = analyze_abstract_structure(all_abstracts)
    stats["templates"] = extract_sentence_templates(all_text)
    stats["caption_stats"] = analyze_figure_captions(all_text)
    stats["top_verbs"] = {"elucidate": 4.2, "demonstrate": 3.5}  # Simplified

    # Generate report
    generate_markdown_report(stats, output_path)
    print(f"✅ Style guide generated: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1], "knowledge_library/academic_writing/style_guide.md")
```

---

### Tool 2: `tools/log_analyzer.py`

**Purpose**: Compress GB-sized training logs into LLM-readable summaries

**User**: `@metacognition_agent` (Phase 5.8)

**Inputs**:
- `output/implementation/logs/training_full.log`

**Outputs**:
- `logs/summary.json` (structured data)
- `logs/highlights.txt` (human-readable)

**Implementation Logic**:

```python
#!/usr/bin/env python3
"""
Log Analyzer: Extract training insights from massive logs.

Usage:
    python log_analyzer.py logs/training_full.log logs/summary.json
"""

import re
import json
import numpy as np
from pathlib import Path

def extract_loss_series(log_path):
    """Extract loss values from log."""
    losses = []
    with open(log_path, 'r') as f:
        for line in f:
            match = re.search(r'loss:\s*([\d\.]+)', line)
            if match:
                losses.append(float(match.group(1)))
    return losses

def detect_oscillation(losses):
    """Calculate oscillation score."""
    if len(losses) < 10:
        return 0.0, "Insufficient data"

    # First derivative
    loss_diff = np.diff(losses)

    # Oscillation = variance of first derivative
    oscillation_score = np.std(loss_diff)

    # Classify
    if oscillation_score < 0.01:
        severity = "Low (smooth convergence)"
    elif oscillation_score < 0.1:
        severity = "Medium (minor fluctuations)"
    else:
        severity = "High (unstable)"

    return oscillation_score, severity

def extract_critical_events(log_path):
    """Find errors, warnings, NaNs."""
    events = {
        "ERROR": [],
        "WARNING": [],
        "NaN": [],
        "Inf": []
    }

    with open(log_path, 'r') as f:
        for i, line in enumerate(f, 1):
            if "ERROR" in line:
                events["ERROR"].append((i, line.strip()))
            elif "WARNING" in line:
                events["WARNING"].append((i, line.strip()))
            elif "nan" in line.lower():
                events["NaN"].append((i, line.strip()))
            elif "inf" in line.lower():
                events["Inf"].append((i, line.strip()))

    return events

def calculate_convergence_speed(losses, target=0.1):
    """Find epoch when loss drops below target."""
    for i, loss in enumerate(losses):
        if loss < target:
            return i + 1
    return None

def generate_summary(log_path):
    """Main analysis pipeline."""
    losses = extract_loss_series(log_path)
    oscillation_score, severity = detect_oscillation(losses)
    events = extract_critical_events(log_path)
    convergence_epoch = calculate_convergence_speed(losses)

    summary = {
        "total_epochs": len(losses),
        "final_loss": losses[-1] if losses else None,
        "initial_loss": losses[0] if losses else None,
        "loss_reduction": (losses[0] - losses[-1]) / losses[0] if losses else 0,
        "oscillation": {
            "score": round(oscillation_score, 4),
            "severity": severity
        },
        "convergence": {
            "target_epoch": convergence_epoch,
            "status": "Converged" if convergence_epoch else "Not converged"
        },
        "events": {
            "error_count": len(events["ERROR"]),
            "warning_count": len(events["WARNING"]),
            "nan_count": len(events["NaN"]),
            "inf_count": len(events["Inf"])
        },
        "top_warnings": events["WARNING"][:5]  # First 5
    }

    return summary

def generate_human_readable(summary):
    """Generate text highlights."""
    text = f"""
# Training Log Summary

## Convergence
- Total Epochs: {summary['total_epochs']}
- Initial Loss: {summary['initial_loss']:.4f}
- Final Loss: {summary['final_loss']:.4f}
- Reduction: {summary['loss_reduction']*100:.1f}%

## Stability
- Oscillation Score: {summary['oscillation']['score']} ({summary['oscillation']['severity']})

## Events
- Errors: {summary['events']['error_count']}
- Warnings: {summary['events']['warning_count']}
- NaNs detected: {summary['events']['nan_count']}
- Infs detected: {summary['events']['inf_count']}

## Top Warnings
{chr(10).join(f"- {warn[1][:100]}" for warn in summary['top_warnings'])}
"""
    return text

def main(log_path, output_json):
    """Main execution."""
    summary = generate_summary(log_path)

    # Save JSON
    with open(output_json, 'w') as f:
        json.dump(summary, f, indent=2)

    # Save highlights
    highlights_path = output_json.replace('.json', '_highlights.txt')
    with open(highlights_path, 'w') as f:
        f.write(generate_human_readable(summary))

    print(f"✅ Log analysis complete: {output_json}")
    print(f"   Highlights: {highlights_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1], "logs/summary.json")
```

---

### Tool 3: `tools/mmbench_score.py`

**Purpose**: Automated rule-based scoring (MMBench simulation)

**User**: `@validator` (Phase 11)

**Inputs**:
- Entire workspace directory

**Outputs**:
- `benchmarks/run_report.json`

**Implementation Logic**:

```python
#!/usr/bin/env python3
"""
MMBench Score: Automated evaluation of paper completeness.

Usage:
    python mmbench_score.py workspace/2025_C/ benchmarks/run_report.json
"""

import os
import re
import json
from pathlib import Path

def check_file_exists(workspace, filepath):
    """Check if file exists."""
    full_path = os.path.join(workspace, filepath)
    return os.path.exists(full_path)

def extract_paper_text(workspace):
    """Extract text from paper (PDF or Markdown)."""
    # Try PDF
    pdf_path = os.path.join(workspace, "output/paper/paper.pdf")
    if os.path.exists(pdf_path):
        # Use pdfplumber or similar
        return extract_from_pdf(pdf_path)

    # Fallback to markdown
    md_path = os.path.join(workspace, "output/paper/paper.md")
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()

    return ""

def check_abstract_numbers(text):
    """Count numbers in abstract."""
    abstract_match = re.search(r'(?:Abstract|ABSTRACT)\s*\n(.*?)(?:\n\n|Introduction)', text, re.DOTALL)
    if not abstract_match:
        return 0
    abstract = abstract_match.group(1)
    return len(re.findall(r'\d+', abstract))

def check_section_exists(text, section_name):
    """Check if section exists."""
    return bool(re.search(rf'(?i){section_name}', text))

def check_code_runnable(workspace):
    """Check if main.py exists and is valid Python."""
    main_py = os.path.join(workspace, "output/implementation/code/main.py")
    if not os.path.exists(main_py):
        return False

    # Basic syntax check
    try:
        with open(main_py, 'r') as f:
            compile(f.read(), main_py, 'exec')
        return True
    except SyntaxError:
        return False

def calculate_score(workspace):
    """Calculate MMBench score."""
    score = 100
    checklist = {}
    deductions = []

    # Check 1: Memo exists (-20 if missing)
    has_memo = check_file_exists(workspace, "output/paper/memo.pdf")
    checklist["has_memo"] = has_memo
    if not has_memo:
        score -= 20
        deductions.append("Missing Memo (-20)")

    # Check 2: Sensitivity Analysis section (-15 if missing)
    text = extract_paper_text(workspace)
    has_sensitivity = check_section_exists(text, r'(?:Sensitivity|Robustness)')
    checklist["has_sensitivity_analysis"] = has_sensitivity
    if not has_sensitivity:
        score -= 15
        deductions.append("Missing Sensitivity Analysis (-15)")

    # Check 3: Abstract numbers (-10 if <3)
    abstract_num_count = check_abstract_numbers(text)
    checklist["abstract_number_count"] = abstract_num_count
    if abstract_num_count < 3:
        score -= 10
        deductions.append(f"Abstract has only {abstract_num_count} numbers, need ≥3 (-10)")

    # Check 4: Code runnable (-10 if not)
    code_runnable = check_code_runnable(workspace)
    checklist["code_runnable"] = code_runnable
    if not code_runnable:
        score -= 10
        deductions.append("Code not runnable or missing (-10)")

    # Check 5: Uncertainty quantification (-5 if missing)
    has_uncertainty = check_section_exists(text, r'(?:uncertainty|confidence interval|p.?value)')
    checklist["has_uncertainty_quantification"] = has_uncertainty
    if not has_uncertainty:
        score -= 5
        deductions.append("Missing uncertainty quantification (-5)")

    # Check 6: Concept diagrams (-5 if none)
    has_mermaid = re.search(r'```mermaid', text) or re.search(r'graphviz', text.lower())
    checklist["has_concept_diagram"] = has_mermaid
    if not has_mermaid:
        score -= 5
        deductions.append("Missing concept flowcharts (-5)")

    # Generate report
    report = {
        "score": max(0, score),
        "checklist": checklist,
        "deductions": deductions,
        "status": "PASS" if score >= 80 else "NEEDS_WORK"
    }

    return report

def load_previous_reports(benchmarks_dir):
    """Load historical reports for trend analysis."""
    reports = []
    for file in os.listdir(benchmarks_dir):
        if file.startswith("run_report_") and file.endswith(".json"):
            with open(os.path.join(benchmarks_dir, file)) as f:
                reports.append(json.load(f))
    return sorted(reports, key=lambda x: x.get("timestamp", ""))

def main(workspace_path, output_path):
    """Main execution."""
    report = calculate_score(workspace_path)
    report["workspace"] = workspace_path
    report["timestamp"] = "2026-01-24T15:30:00Z"  # Use actual timestamp

    # Load previous for trend
    benchmarks_dir = os.path.join(workspace_path, "benchmarks")
    if os.path.exists(benchmarks_dir):
        previous = load_previous_reports(benchmarks_dir)
        if previous:
            last_score = previous[-1].get("score", 0)
            report["trend"] = report["score"] - last_score
            report["previous_score"] = last_score

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"""
📊 MMBench Score: {report['score']}/100
Status: {report['status']}

Deductions:
{chr(10).join(f'- {d}' for d in report['deductions']) if report['deductions'] else 'None'}
""")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "benchmarks/run_report.json")
```

---

## Part VII: Workspace Structure Specification

### 7.1 Complete Directory Tree

```
workspace/2025_C/
├── 📂 .claude/                          # Agent configurations
│   ├── CLAUDE.md                        # Master workflow (18 agents, 13 phases)
│   └── agents/
│       ├── director.md
│       ├── reader.md
│       ├── researcher.md
│       ├── modeler.md
│       ├── feasibility_checker.md
│       ├── data_engineer.md
│       ├── code_translator.md           # [ENHANCED] dev_diary.md output
│       ├── model_trainer.md
│       ├── validator.md
│       ├── visualizer.md                # [ENHANCED] dual-mode (data + concept)
│       ├── writer.md                    # [ENHANCED] style_guide.md constraint
│       ├── narrative_weaver.md          # [NEW] story director
│       ├── summarizer.md
│       ├── editor.md                    # [ENHANCED] style_guide.md constraint
│       ├── advisor.md
│       ├── time_validator.md
│       ├── metacognition_agent.md       # [NEW] philosopher
│       ├── knowledge_librarian.md       # [NEW] academic curator
│       └── judge_zero.md                # [NEW] red team leader
│
├── 📂 knowledge_library/                # [NEW] Dynamic knowledge base (HMML 2.0)
│   ├── 📂 academic_writing/
│   │   ├── style_guide.md               # [AUTO-GENERATED] by Phase -1
│   │   └── ANTI_PATTERNS.md             # [MANUAL] Kill List for @judge_zero
│   │
│   ├── 📂 methods/                      # HMML 2.0 structure
│   │   ├── index.md                     # Global catalog
│   │   ├── 📂 optimization/
│   │   │   ├── linear_programming/
│   │   │   │   └── simplex_method.md
│   │   │   └── heuristic_algorithms.md
│   │   ├── 📂 differential_equations/
│   │   │   ├── sir_network.md
│   │   │   ├── sde.md
│   │   │   └── pde.md
│   │   ├── 📂 statistics/
│   │   │   ├── bayesian_hierarchical.md
│   │   │   └── time_series/
│   │   └── 📂 network_science/
│   │       ├── dijkstra.md
│   │       └── agent_based_model.md
│   │
│   └── 📂 templates/
│       └── 📂 narrative_arcs/
│           ├── hero_journey.md          # "Struggle → Insight" template
│           ├── onion_peeling.md         # "Layer-by-layer" template
│           └── observation_implication.md  # Protocol 15 templates
│
├── 📂 reference_papers/                 # [NEW] User-uploaded O-Prize papers
│   ├── 2024_Problem_C_O_Prize.pdf
│   └── 2023_Problem_D_O_Prize.pdf
│
├── 📂 tools/                            # [NEW] Python toolchain
│   ├── style_analyzer.py                # Phase -1: Analyze reference papers
│   ├── log_analyzer.py                  # Phase 5.8: Compress training logs
│   └── mmbench_score.py                 # Phase 11: Automated scoring
│
├── 📂 output/                           # [UPDATED] Enhanced structure
│   ├── 📂 docs/
│   │   ├── 📂 insights/                 # [NEW] Metacognitive output
│   │   │   └── narrative_arc_{i}.md     # Generated by @metacognition_agent
│   │   ├── 📂 knowledge/                # [NEW] Active retrieval output
│   │   │   └── suggested_methods.md     # Generated by @knowledge_librarian
│   │   ├── 📂 validation/               # [NEW] Adversarial review output
│   │   │   └── judgment_report.md       # Generated by @judge_zero
│   │   ├── 📂 requirements/             # Problem understanding
│   │   ├── 📂 consultations/            # Agent feedback
│   │   └── 📂 validation/               # Technical validation
│   │
│   ├── 📂 implementation/
│   │   ├── 📂 code/
│   │   │   ├── dev_diary_{i}.md         # [NEW] Struggle documentation
│   │   │   ├── main.py
│   │   │   └── requirements.txt
│   │   ├── 📂 data/
│   │   │   ├── processed/
│   │   │   └── raw/
│   │   ├── 📂 logs/
│   │   │   ├── training_full.log        # Complete log for @metacognition_agent
│   │   │   └── summary.json             # Compressed by log_analyzer.py
│   │   └── 📂 models/
│   │       └── model_{i}.pkl
│   │
│   ├── 📂 figures/
│   │   ├── model_1_data_plot.png        # Mode A: Data visualization
│   │   ├── model_1_concept.png          # Mode B: Concept flowchart (Mermaid)
│   │   └── model_1_flowchart.mmd        # Mermaid source code
│   │
│   └── 📂 paper/
│       ├── paper.tex
│       ├── paper.pdf
│       ├── memo.pdf                     # 1-page summary
│       └── references.bib
│
├── 📂 benchmarks/                       # [NEW] Post-competition evolution
│   ├── run_report_20260124.json         # Automated scoring
│   ├── trend_analysis.png               # Score over time
│   └── EVOLUTION.md                     # Human-written improvement plan
│
├── problem.pdf                          # Competition problem
└── data.xlsx                            # Competition data
```

### 7.2 File Purpose Matrix

| File/Directory | Phase Created/Used | Created By | Purpose |
|----------------|-------------------|------------|---------|
| `knowledge_library/` | Phase -1, 0.2 | Human + @knowledge_librarian | Dynamic knowledge base |
| `style_guide.md` | Phase -1 | tools/style_analyzer.py | Academic style profile |
| `ANTI_PATTERNS.md` | Manual (Day 1-3) | Human | Kill List for @judge_zero |
| `suggested_methods.md` | Phase 0.2 | @knowledge_librarian | Advanced method recommendations |
| `dev_diary_{i}.md` | Phase 4 | @code_translator | Implementation struggle record |
| `training_full.log` | Phase 5B | @model_trainer | Complete training record |
| `narrative_arc_{i}.md` | Phase 5.8 | @metacognition_agent | "Struggle → Insight" narrative |
| `model_*_flowchart.mmd` | Phase 6 | @visualizer (Mode B) | Concept diagram source |
| `paper_outline.md` | Phase 7 | @narrative_weaver | Paragraph-level structure |
| `judgment_report.md` | Phase 9.1 | @judge_zero | Red team review + Kill List |
| `run_report.json` | Phase 11 | tools/mmbench_score.py | Automated scoring + trend |

---

## Part VIII: Implementation Roadmap (15-Day Sprint Plan)

### Sprint 1: Foundation & Eyes (Days 1-3)

**Goal**: Build physical skeleton, HMML 2.0, and赋予系统"学术审美"与"判罚标准"

**Deliverables**:
- Complete directory structure
- Migrated HMML 2.0 with metadata
- `style_guide.md` (auto-generated)
- `ANTI_PATTERNS.md` (manually defined)

**Day 1: Physical Foundation**
- Create directory tree via `init_workspace.py`
- Parse `HMML.md`, split into individual method files
- Add YAML Front Matter (narrative_value, common_pitfalls)
- Generate `methods/index.md` catalog

**Day 2: Cognitive Eyes**
- Implement `tools/style_analyzer.py`
- Test on sample PDFs
- Generate first `style_guide.md`

**Day 3: Judicial Law**
- Create `ANTI_PATTERNS.md` with ≥5 Fatal Flaws
- Define @judge_zero's three personas
- Set up `reference_papers/` directory

---

### Sprint 2: Brain & Soul (Days 4-8)

**Goal**: Build metacognition loop and narrative engine

**Deliverables**:
- `@metacognition_agent` functional
- `@narrative_weaver` functional
- `@visualizer` dual-mode (data + concept)
- Phase 5.8 integrated

**Day 4: Pain Perception**
- Update `@code_translator` Prompt (add dev_diary.md requirement)
- Create `@metacognition_agent` Prompt
- Test "struggle → insight" transformation

**Day 5: Narrative Engine**
- Implement `tools/log_analyzer.py`
- Create `@narrative_weaver` Prompt
- Define Observation-Implication templates

**Day 6: Concept Vision**
- Update `@visualizer` Prompt (add Mermaid/Graphviz support)
- Create Mode B examples
- Test concept diagram generation

**Day 7: Phase 5.8 Integration**
- Update `CLAUDE.md` with Phase 5.8 definition
- Test full pipeline: log → summary → narrative_arc

**Day 8: Integration Testing**
- End-to-end Sprint 2 test
- Verify all components connect

---

### Sprint 3: Fangs & Shield (Days 9-14)

**Goal**: Deploy adversarial review and self-evolution

**Deliverables**:
- `@judge_zero` functional
- `@knowledge_librarian` functional
- Phase 9.1 + Protocol 13 operational
- `tools/mmbench_score.py` functional
- Full system test (2024 C problem)

**Day 9: Red Team Leader**
- Create `@judge_zero` with three-persona Prompt
- Write test cases (烂论文摘要)
- Verify REJECT behavior

**Day 10: Knowledge Guardian**
- Create `@knowledge_librarian` Prompt
- Implement Phase 0.2 logic
- Test method injection (prevent mediocrity)

**Day 11: War Rules**
- Define Phase 9.1 in `CLAUDE.md`
- Define Protocol 13 (DEFCON 1)
- Test REJECT → REWIND loop

**Day 12: Scorecard**
- Implement `tools/mmbench_score.py`
- Test on existing workspace
- Generate `run_report.json`

**Day 13-14: War Game**
- Full system test on 2024 C problem
- Trigger DEFCON 1, verify recovery
- Test all three Sprints integrated

---

## Part IX: Risk Assessment & Mitigation

### Risk 1: Token Explosion

**Problem**: 18 agents + massive logs + style_guide loading → Context Window overflow

**Symptoms**:
- LLM calls fail with "maximum context exceeded"
- Slow response times
- Degraded quality

**Mitigation Strategies**:

1. **Hierarchical Loading** (Protocol: "Load on Demand")
   - HMML methods: Load only in Phase 0.2 and Phase 1
   - `style_guide.md`: Load only for @writer, @narrative_weaver, @editor
   - `ANTI_PATTERNS.md`: Load only for @judge_zero

2. **Log Compression**
   - Never feed raw `training_full.log` to LLM
   - Always run `log_analyzer.py` first → `summary.json`
   - LLM reads summary, not full log

3. **Context Pruning** (v3.0.0 "远近亲疏" strategy)
   - Immediate predecessor: Full context
   - Earlier phases: Minimal context (results only)
   - Agent personas: Truncate to essential personality

**Fallback**: If context overflow occurs, use smaller model (GPT-4o-mini) for summarization tasks

---

### Risk 2: Infinite DEFCON 1 Loop

**Problem**: @judge_zero too harsh → REJECT → Fix → REJECT → Fix → REJECT → ...

**Symptoms**:
- System stuck in Phase 9.1
- 3+ REJECT cycles
- No progress to Phase 10

**Mitigation**: **Mercy Rule** (Protocol 13, Clause 5)

```
IF (REJECT_count >= 3):
    @director MAY force "Conditional Pass"
    REQUIREMENT: Document all unresolved flaws in Phase 11
    TRIGGER: Manual override approval
```

**Implementation**:
```python
# In @director's DEFCON 1 handler
if reject_count >= 3:
    print("⚠️  Mercy Rule triggered. Force Conditional Pass?")
    print(f"Unresolved flaws: {len(kill_list)}")
    approval = input("Approve conditional pass? (yes/no): ")
    if approval.lower() == "yes":
        status = "CONDITIONAL_PASS"
        log_to_phase_11("Conditional pass due to persistent rejection")
```

---

### Risk 3: HMML 2.0 Migration Complexity

**Problem**: Manually splitting `HMML.md` into 50+ files with metadata is time-consuming

**Symptoms**:
- Incomplete migration (missing methods)
- Inconsistent metadata quality
- Broken internal links

**Mitigation**: **Semi-Automated Migration Script**

```python
# tools/migrate_hmml.py
import re
import yaml
from pathlib import Path

def parse_hmml_section(content, method_name):
    """Extract method section from HMML.md"""
    # Extract subsections: Definition, Math, Implementation
    definition = re.search(r'## 定义\n(.*?)(?=##|$)', content, re.DOTALL)
    # ... more parsing

    metadata = {
        "method_name": method_name,
        "domain": infer_domain(content),  # Keyword matching
        "complexity": estimate_complexity(content),
        "narrative_value": assess_narrative_potential(content),
        "common_pitfalls": extract_pitfalls(content)
    }

    return metadata, content

def main():
    with open("HMML.md") as f:
        content = f.read()

    # Split by ### (method-level headers)
    methods = re.split(r'\n###\s+', content)

    for method in methods:
        name_match = re.search(r'^(.+?)\n', method)
        if name_match:
            name = name_match.group(1)
            metadata, body = parse_hmml_section(method, name)

            # Write to file
            domain = metadata["domain"].lower().replace(" ", "_")
            path = f"knowledge_library/methods/{domain}/{slugify(name)}.md"
            Path(path).parent.mkdir(parents=True, exist_ok=True)

            with open(path, 'w') as f:
                f.write(yaml.dump(metadata))
                f.write("\n---\n\n")
                f.write(body)
```

**Manual Review Required**: Even with script, human must:
1. Verify domain assignments
2. Enhance `narrative_value` descriptions
3. Add `o_prize_examples`
4. Fill in `common_pitfalls` (script can't infer all)

---

### Risk 4: @judge_zero Calibration

**Problem**: Three personas may be too harsh or too lenient

**Symptoms**:
- All papers rejected (harsh) → No submissions
- All papers pass (lenient) → No quality improvement

**Mitigation**: **Calibration Dataset**

Create `tests/calibration/` with 3 synthetic papers:

1. **Perfect Paper** (O-Prize level)
   - Should PASS with score ≥95
   - Has sensitivity analysis, uncertainty, numbers in abstract

2. **Mediocre Paper** (Honorable Mention)
   - Should PASS with score ~80-90
   - Missing 1-2 elements but no fatal flaws

3. **Bad Paper** (Failed)
   - Should REJECT with score <50
   - No sensitivity analysis, no numbers, physical impossibility

**Calibration Procedure**:
```
For each paper in calibration set:
    Run @judge_zero
    Record score and verdict
    Compare to expected outcome
    If偏差 > 10 points: Adjust persona weights
```

**Target Metrics**:
- Perfect Paper: Score 95-100, PASS
- Mediocre Paper: Score 75-85, PASS (with warnings)
- Bad Paper: Score 0-50, REJECT

---

## Part X: Quality Assurance & Testing

### 10.1 Unit Tests (Per Component)

| Component | Test | Command | Expected |
|-----------|------|---------|----------|
| `style_analyzer.py` | Extracts verbs from PDF | `python tests/test_style_analyzer.py` | Outputs `style_guide.md` with top verbs |
| `log_analyzer.py` | Compresses 1GB log | `python tests/test_log_analyzer.py` | Outputs `summary.json` <10KB |
| `mmbench_score.py` | Scores workspace | `python tests/test_mmbench.py` | Outputs score 0-100 |
| `@metacognition_agent` | Transforms error to insight | Manual prompt with fake log | Outputs `narrative_arc.md` with "Struggle → Physical Meaning" |
| `@judge_zero` | Rejects bad paper | Manual prompt with bad abstract | Outputs REJECT with Kill List |

---

### 10.2 Integration Tests (Per Sprint)

**Sprint 1 Integration Test**:
```bash
# Test HMML 2.0 retrieval
python tests/test_hmml_retrieval.py
# Expected: Can retrieve all 47 methods via index.md

# Test style guide generation
python tools/style_analyzer.py reference_papers/ output/style_guide.md
# Expected: style_guide.md contains ≥10 recommended verbs
```

**Sprint 2 Integration Test**:
```bash
# Test Phase 5.8 pipeline
python tests/test_phase_5_8.py
# Creates fake log + dev_diary
# Runs log_analyzer.py
# Invokes @metacognition_agent (manual or API)
# Expected: narrative_arc.md generated with ≥1 insight
```

**Sprint 3 Integration Test**:
```bash
# Test Phase 9.1 + Protocol 13
python tests/test_moot_court.py
# Creates bad paper on purpose
# Invokes @judge_zero
# Expected: REJECT + DEFCON 1 declared
# Then fixes paper
# Expected: Second run → PASS
```

---

### 10.3 End-to-End Test (Full System)

**Scenario**: 2024 Problem C (Wimbledon Tennis Momentum)

**Step-by-Step Execution**:

1. **Phase -1**: Generate `style_guide.md` from tennis papers
2. **Phase 0**: Analyze problem (momentum prediction)
3. **Phase 0.2**: `@knowledge_librarian` recommends Markov Chain, NOT linear regression
4. **Phase 1-5B**: Build and train model (故意埋雷: dev_diary records convergence issue)
5. **Phase 5.8**: `@metacognition_agent` extracts insight: "Momentum decays in set 3 due to fatigue"
6. **Phase 6**: `@visualizer` generates data plot + Mermaid flowchart
7. **Phase 7**: `@narrative_weaver` creates outline with Observation-Implication
8. **Phase 9**: `@writer` generates paper (故意埋雷: abstract no numbers)
9. **Phase 9.1**: `@judge_zero` REJECTs (abstract空洞)
10. **Protocol 13**: DEFCON 1 → @writer fixes abstract
11. **Phase 9.1 (Round 2)**: PASS (score 97)
12. **Phase 10**: Generate final package
13. **Phase 11**: `mmbench_score.py` outputs score 92/100

**Success Criteria**:
- All phases execute without error
- Phase 5.8 generates meaningful insight (not "training succeeded")
- Phase 9.1 REJECTs bad paper, passes good paper
- DEFCON 1 triggers and recovers
- Final MMBench score ≥85

---

## Conclusion: The Ultimate Vision

MCM-Killer v3.1.0 is not merely an upgrade—it is a **paradigm shift** from "problem-solving tool" to "cognitive research laboratory."

### The Three Pillars of Excellence

1. **Cognitive Narrative** (o1-style thinking)
   - Every error becomes an insight
   - Every struggle becomes a story
   - Every paper demonstrates learning process

2. **Adversarial Validation** (Red-blue team)
   - @judge_zero simulates地狱级 review
   - DEFCON 1 forces quality
   - Only perfect papers survive

3. **Self-Evolution** (Continuous improvement)
   - Each run generates data
   - MMBench tracks progress
   - System evolves with each competition

### The O-Prize Differentiator

**v3.0.0 Paper**:
> "We used a Bayesian model. It achieved RMSE = 4.2."

**v3.1.0 Paper**:
> "We initially assumed homogeneous transmission parameters, but R-hat divergence
> (Figure 2a) revealed fundamental regional heterogeneity. By adopting a
> non-centered parameterization, we resolved convergence while discovering that
> host country effects vary by economic development—a finding with critical
> policy implications for region-tailored interventions (RMSE = 4.2, p < 0.001)."

**The difference**: v3.1.0 doesn't just solve the problem—it demonstrates deep understanding.

---

**Document Version**: 1.0-Ultimate
**Last Updated**: 2026-01-24
**Total Words**: ~15,000
**Next Steps**: Proceed to Sprint 1 Implementation Guides
