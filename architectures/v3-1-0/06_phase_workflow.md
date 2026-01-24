# Phase Workflow v3.1.0

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Purpose**: Complete guide to 13-phase workflow with detailed descriptions

---

## Overview

v3.1.0 features **13 phases** (vs 10 in v3.0.0), organized into 5 stages:

1. **Pre-Competition** (Phase -1)
2. **Understanding & Design** (Phases 0-1.5)
3. **Implementation** (Phases 2-5.8)
4. **Results & Paper** (Phases 6-9.1)
5. **Submission & Evolution** (Phases 9.5-11)

---

## Phase Matrix

### Agent Participation

| Phase | Primary Agents | Supporting Agents | Output | Validation |
|-------|---------------|-------------------|--------|------------|
| **-1** | @knowledge_librarian | - | style_guide.md | - |
| **0** | @reader, @researcher | @director | problem_statement.md | - |
| **0.2** | @knowledge_librarian | @researcher | suggested_methods.md | - |
| **0.5** | @researcher, @advisor | @summarizer | feasibility_report.md | ✅ Gate |
| **1** | @modeler | @researcher | model_design.md | - |
| **1.5** | @advisor | @director | validation_report.md | ✅ Gate |
| **2-3** | @data_engineer | @validator | processed_data | - |
| **4** | @code_translator | @modeler | code + dev_diary | - |
| **4.5** | @validator | @code_translator | validation_report.md | ✅ Gate |
| **5** | @model_trainer | @code_translator | trained models | - |
| **5.5** | @validator | @model_trainer | validation_report.md | ✅ Gate |
| **5.8** | @metacognition_agent | @code_translator | narrative_arc.md | - |
| **6** | @validator | @model_trainer | results.csv | - |
| **7** | @narrative_weaver, @writer | @metacognition_agent | paper.tex | - |
| **9** | @summarizer | @writer | summary.pdf | - |
| **9.1** | @judge_zero | @director | judgment_report.md | ✅ Gate |
| **9.5** | @director | All | submission.zip | - |
| **10** | @director | - | SUBMITTED | - |
| **11** | @knowledge_librarian | @director | weakness_analysis.md | - |

---

## Detailed Phase Descriptions

### Stage 1: Pre-Competition

#### Phase -1: Style Guide Generation

**Purpose**: Generate academic style guide from O-Prize papers before competition begins.

**Agent**: @knowledge_librarian (Mode 1: Pre-Game)

**Tool**: `tools/style_analyzer.py`

**Input**:
- `reference_papers/*.pdf` (2-3 O-Prize papers)

**Output**: `knowledge_library/academic_writing/style_guide.md`

**Process**:
1. Collect reference papers
2. Run style analyzer
3. Extract vocabulary, abstract rules, sentence templates
4. Generate style_guide.md

**Trigger**:
- Manual trigger before competition
- Auto-detect new PDFs in `reference_papers/`

**Quality Check**:
- [ ] style_guide.md generated
- [ ] Contains ≥10 recommended verbs
- [ ] Contains ≥3 abstract rules
- [ ] Contains ≥2 sentence templates

---

### Stage 2: Understanding & Design

#### Phase 0: Problem Understanding

**Purpose**: Extract requirements and constraints from problem statement.

**Agents**: @reader, @researcher

**Input**: Problem PDF

**Output**: `output/docs/requirements/problem_statement.md`

**Process**:
1. @reader extracts text from PDF
2. @researcher analyzes requirements
3. Identify explicit requirements (must-have)
4. Identify implicit requirements (nice-to-have)
5. Extract keywords for domain identification

**Duration**: 30-60 minutes

---

#### Phase 0.2: Active Knowledge Retrieval (NEW)

**Purpose**: Proactively push advanced methods, prevent "safe but mediocre" choices.

**Agent**: @knowledge_librarian (Mode 2: In-Game)

**Input**: `problem_statement.md`

**Output**: `output/docs/knowledge/suggested_methods.md`

**Process**:
1. Identify domain from keywords
2. **BAN** simple methods (Linear Regression, Basic SIR, ARIMA)
3. **PUSH** advanced methods (SIR-Network, SDE, ABM)
4. Provide mathematical justification
5. Cite O-Prize examples

**Philosophy**: "Good is the enemy of great."

**Quality Check**:
- [ ] Contains "❌ AVOID" section
- [ ] Contains "✅ RECOMMEND" section with ≥3 methods
- [ ] Each method has mathematical + narrative justification

---

#### Phase 0.5: Feasibility Check

**Purpose**: Validate that proposed methods are feasible within competition timeframe.

**Agents**: @researcher, @advisor, @summarizer

**Input**: Proposed methods from @researcher

**Output**: `output/docs/reports/feasibility_report.md`

**Process**:
1. @researcher proposes methods
2. @advisor evaluates technical feasibility
3. @summarizer assesses time requirements
4. Generate feasibility verdict

**Validation Gate**:
- **PASS**: Proceed to Phase 1
- **FAIL**: Re-design methods

**Advisor Checklist**:
- [ ] Data requirements met?
- [ ] Computational resources sufficient?
- [ ] Time constraints feasible?
- [ ] Methods appropriate for problem?

---

#### Phase 1: Model Design

**Purpose**: Design mathematical models with equations and assumptions.

**Agent**: @modeler

**Input**: `problem_statement.md`, `suggested_methods.md`

**Output**: `output/model/model_{i}/design.md`

**Process**:
1. Select method(s) from suggested_methods.md
2. Define mathematical formulation (equations)
3. State assumptions explicitly
4. Identify parameters to calibrate
5. Create design expectations table

**Output Template**:
```markdown
# Model {i}: [Name]

## Mathematical Formulation
[Equations in LaTeX]

## Assumptions
1. [Assumption 1]
2. [Assumption 2]

## Parameters
| Parameter | Symbol | Estimate | Source |
|-----------|--------|----------|--------|
| [Name] | [Symbol] | [Value] | [Source] |

## Design Expectations
| Metric | Target | Rationale |
|--------|--------|-----------|
| [Name] | [Value] | [Why] |
```

---

#### Phase 1.5: Design Validation

**Purpose**: Validate model designs before implementation.

**Agent**: @advisor

**Input**: Model designs from @modeler

**Output**: `output/docs/validation/design_validation_report.md`

**Process**:
1. Review mathematical formulation (correctness?)
2. Check assumptions (plausible?)
3. Verify parameters (identifiable?)
4. Assess complexity (feasible?)

**Validation Gate**:
- **PASS**: Proceed to Phase 2
- **FAIL**: Re-design models

**Advisor Checklist**:
- [ ] Equations mathematically correct?
- [ ] Assumptions physically plausible?
- [ ] Parameters can be estimated from data?
- [ ] Model not over-complex (identifiable)?

---

### Stage 3: Implementation

#### Phase 2-3: Data Processing

**Purpose**: Clean, transform, and prepare data for modeling.

**Agent**: @data_engineer

**Input**: Raw problem data

**Output**: `output/implementation/data/{train,test,processed}.{csv,pkl}`

**Process**:
1. Load raw data
2. Clean (handle missing values, outliers)
3. Feature engineering
4. Normalize/scale
5. Split train/test
6. Save processed data

**Quality Checks**:
- [ ] No missing values in processed data
- [ ] Outliers handled appropriately
- [ ] Features normalized (if required)
- [ ] Data integrity verified

---

#### Phase 4: Code Translation

**Purpose**: Translate mathematical models to Python code.

**Agent**: @code_translator

**Input**: Model designs from @modeler

**Output**:
- `output/implementation/code/main_{i}.py`
- `output/implementation/code/dev_diary_{i}.md` (NEW)

**Process**:
1. Translate equations to Python
2. Implement numerical solver (ODE solver, optimization, etc.)
3. Add parameter calibration
4. Include error handling
5. Document in dev_diary.md (NEW requirement)

**dev_diary.md Template**:
```markdown
## [YYYY-MM-DD HH:MM] Issue: [Short Description]

### The Struggle
- **Symptom**: What error occurred?
- **Context**: What was happening?

### The Fix
- **Technical Solution**: What was done?

### The Why (Research Value)
- **Physical Meaning**: What does this reveal?
```

**Quality Check**:
- [ ] Code runs without errors
- [ ] Equations correctly implemented
- [ ] dev_diary.md maintained
- [ ] Code documented

---

#### Phase 4.5: Code Validation

**Purpose**: Validate code correctness before training.

**Agent**: @validator

**Input**: Python code from @code_translator

**Output**: `output/docs/validation/code_validation_report.md`

**Process**:
1. Syntax check
2. Logic check (equations vs code)
3. Test with synthetic data
4. Verify outputs are physically plausible

**Validation Gate**:
- **PASS**: Proceed to Phase 5
- **FAIL**: Re-write code

**Validator Checklist**:
- [ ] Code runs without errors?
- [ ] Equations correctly implemented?
- [ ] Outputs physically plausible (no negative populations, etc.)?
- [ ] Edge cases handled?

---

#### Phase 5: Model Training

**Purpose**: Train models and generate results.

**Agent**: @model_trainer

**Input**: Code, processed data

**Output**:
- `output/implementation/models/model_{i}.pkl`
- `output/implementation/logs/training_full.log`
- `output/implementation/logs/summary.json` (via log_analyzer.py)

**Process**:
1. Load processed data
2. Calibrate parameters (fit to data)
3. Run simulation/optimization
4. Save trained model
5. Log everything

**Modes**:
- **Watch Mode**: Monitor training, detect issues early
- **Emergency Delegation**: If stuck, delegate to @code_translator

**Quality Check**:
- [ ] Model converged
- [ ] Parameters calibrated successfully
- [ ] Training log complete
- [ ] summary.json generated

---

#### Phase 5.5: Post-Training Validation

**Purpose**: Validate results before proceeding to paper.

**Agent**: @validator

**Input**: Trained models, results

**Output**: `output/docs/validation/post_training_validation_report.md`

**Process**:
1. Verify results are physically plausible
2. Check performance metrics
3. Validate against design expectations
4. Assess uncertainty quantification

**Validation Gate**:
- **PASS**: Proceed to Phase 6
- **FAIL**: Re-train or re-design

**Validator Checklist**:
- [ ] Results physically plausible?
- [ ] Performance targets met?
- [ ] Uncertainty quantified?
- [ ] No numerical instabilities?

---

#### Phase 5.8: Insight Extraction (NEW)

**Purpose**: Transform technical struggles into research insights.

**Agent**: @metacognition_agent

**Input**:
- `logs/summary.json` (compressed training data)
- `dev_diary_{i}.md` (subjective struggles)
- HMML 2.0 (theoretical context)

**Output**: `output/docs/insights/narrative_arc_{i}.md`

**Process**:
1. Identify symptoms (loss oscillation, gradient explosion, etc.)
2. Hypothesize physical causes
3. Validate against dev_diary
4. Formulate insights
5. Extract narrative arc

**Quality Rule**: NEVER say "fixed a bug" → ALWAYS say "refined to capture physical reality"

**Output Template**: Hero's Journey
```markdown
# Narrative Arc: Model {i}

## The Call
[Problem statement]

## The Ordeal
[Technical struggles]

## The Revelation
[Physical mechanism discovered]

## The Resolution
[Technical fix + physical justification]

## The Treasure
[Scientific contribution + narrative leverage]
```

**Quality Check**:
- [ ] ≥3 insights extracted
- [ ] No "bug fixing" language
- [ ] Each insight has observation + mechanism + value
- [ ] Uses narrative template

---

### Stage 4: Results & Paper

#### Phase 6: Result Generation

**Purpose**: Generate final results from trained models.

**Agent**: @validator

**Input**: Trained models

**Output**:
- `output/implementation/data/results.csv`
- `output/implementation/data/processed_data.pkl`

**Process**:
1. Run model on test data
2. Generate predictions
3. Calculate performance metrics
4. Save results

**Quality Check**:
- [ ] Results saved in CSV
- [ ] All metrics calculated
- [ ] Results reproducible

---

#### Phase 7: Paper Generation

**Purpose**: Generate LaTeX paper with cognitive narrative.

**Agents**: @narrative_weaver (outline), @writer (content)

**Input**:
- `narrative_arc_{i}.md` (from Phase 5.8)
- Model designs
- Results
- Figures list

**Output**:
- `paper_outline.md` (detailed plan)
- `output/paper/main.tex`
- `output/paper/paper.pdf`

**Process**:

**Step 1**: @narrative_weaver generates outline
- Select narrative template (Hero's Journey, Onion Peeling, Comparative)
- Structure paper sections
- Plan figures (ensure all support narrative)
- Check figure captions (all conclusionary per Protocol 15)

**Step 2**: @writer writes content
- Load style_guide.md as System Context (Protocol 14)
- Follow Observation-Implication structure (Protocol 15)
- Include ≥3 numbers in abstract
- Use recommended vocabulary

**Quality Check**:
- [ ] Abstract contains ≥3 quantitative metrics
- [ ] All figure captions conclusionary
- [ ] Observation-Implication structure used
- [ ] No banned vocabulary (show, get, say)
- [ ] LaTeX compiles successfully

---

#### Phase 9: Summary Generation

**Purpose**: Generate 1-page summary.

**Agent**: @summarizer

**Input**: Final paper

**Output**: `output/paper/summary.pdf`

**Process**:
1. Extract key points from paper
2. Summarize methods, results, conclusions
3. Format to 1 page
4. Load style_guide.md for consistency

**Quality Check**:
- [ ] Length ≤ 1 page
- [ ] Contains ≥3 quantitative metrics
- [ ] Mentions key insights

---

#### Phase 9.1: Mock Judging (NEW)

**Purpose**: Adversarial review to catch flaws before submission.

**Agent**: @judge_zero (Three-Persona Evaluation)

**Input**: `output/paper/paper.pdf`

**Output**: `output/docs/validation/judgment_report.md`

**Process**:

**Persona A**: The Pedantic Statistician
- Obsession: Uncertainty quantification
- Checks: p-values, confidence intervals, sensitivity analysis

**Persona B**: The Domain Skeptic
- Obsession: Physical plausibility
- Checks: Impossible values, unjustified assumptions

**Persona C**: The Exhausted Editor
- Obsession: Abstract numbers, figure captions
- Checks: Abstract空洞, non-descriptive captions

**Scoring**:
- Base Score = 100
- Subtract deductions from each persona
- Any fatal flaw → Score 0-50
- Score < 95 → REJECT

**Validation Gate**:
- **PASS** (≥95): Proceed to Phase 9.5
- **REJECT** (<95): DEFCON 1 (Protocol 13)

**Quality Check**:
- [ ] All three personas evaluated
- [ ] Kill List generated (if REJECT)
- [ ] Score calculated correctly
- [ ] Fatal flaws flagged

---

### Stage 5: Submission & Evolution

#### Phase 9.5: Final Package

**Purpose**: Assemble final submission package.

**Agent**: @director

**Input**: Paper, summary, code

**Output**: `output/package/submission.zip`

**Contents**:
- paper.pdf
- summary.pdf
- code.zip (all Python code)
- README.md

**Process**:
1. Verify all components present
2. Check file sizes (within limits)
3. Create submission.zip
4. Verify zip integrity

---

#### Phase 10: Submission

**Purpose**: Submit to MCM/ICM.

**Agent**: @director

**Action**: Upload submission.zip to MCM/ICM website

**Post-Submission**:
- Log submission timestamp
- Update VERSION_MANIFEST.json
- Archive workspace

---

#### Phase 11: Self-Evolution (NEW)

**Purpose**: Learn from competition to improve system.

**Tool**: `tools/mmbench_score.py`

**Input**: `output/paper/paper.pdf`

**Output**:
- `automated_score.json`
- `violation_history.json`
- `weakness_analysis.md`

**Process**:

**Step 1**: Automated scoring
- Parse paper PDF
- Score against O-Prize criteria (0-100)
- Extract violations

**Step 2**: Violation tracking
- Aggregate violations across competitions
- Identify systematic weaknesses

**Step 3**: Pattern identification
- Which agents cause issues?
- Which protocols are ineffective?

**Step 4**: Update knowledge bases
- ANTI_PATTERNS.md (new flaws)
- style_guide.md (new banned words)
- Agent prompts (based on performance)

**Step 5**: Meta-learning
- Correlate automated scores with official results
- Calibrate scoring formula

**Timing**: Post-competition (after official results available)

**Quality Check**:
- [ ] mmbench_score.py executed
- [ ] violation_history.json updated
- [ ] weakness_analysis.md generated
- [ ] ANTI_PATTERNS.md updated
- [ ] Agent prompts revised

---

## Phase Dependencies

### Sequential Order (Protocol 2)

**Phases MUST execute in order**:
```
-1 → 0 → 0.2 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5 → 5.5 → 5.8 → 6 → 7 → 9 → 9.1 → 9.5 → 10 → 11
```

**Never skip phases** unless explicitly approved by @director.

**Previous phase must be fully complete before entering next phase.**

### Validation Gates

**5 Mandatory Gates**:
1. **Gate 0.5**: Feasibility Check
2. **Gate 1.5**: Design Validation
3. **Gate 4.5**: Code Validation
4. **Gate 5.5**: Post-Training Validation
5. **Gate 9.1**: Mock Judging

**FAIL → Re-work phase, RE-EVALUATE**

---

## Timeline

### Typical Competition Schedule (96 hours)

**Day 1** (Hours 0-24):
- Phase -1: Pre-comp (already done)
- Phase 0: Problem understanding (1-2 hours)
- Phase 0.2: Method retrieval (1 hour)
- Phase 0.5: Feasibility check (1-2 hours)
- Phase 1: Model design (3-4 hours)
- Phase 1.5: Design validation (1 hour)

**Day 2** (Hours 24-48):
- Phase 2-3: Data processing (2-3 hours)
- Phase 4: Code translation (4-6 hours)
- Phase 4.5: Code validation (1-2 hours)

**Day 3** (Hours 48-72):
- Phase 5: Model training (6-10 hours)
- Phase 5.5: Post-training validation (1-2 hours)
- Phase 5.8: Insight extraction (2-3 hours)
- Phase 6: Result generation (1-2 hours)

**Day 4** (Hours 72-96):
- Phase 7: Paper generation (4-6 hours)
- Phase 9: Summary (1 hour)
- Phase 9.1: Mock judging (1-2 hours) ← May trigger DEFCON 1
- Phase 9.5: Final package (1 hour)
- Phase 10: Submission (buffer time)

**Post-Competition**:
- Phase 11: Self-evolution (after official results)

---

## Quality Assurance

### Phase Completion Checklist

**For Each Phase**:
- [ ] All outputs generated
- [ ] Outputs validated
- [ ] VERSION_MANIFEST.json updated
- [ ] Checkpoint created

### Pre-Submission Checklist

**Before Phase 10**:
- [ ] All phases complete
- [ ] All validation gates passed
- [ ] Phase 9.1 PASS (≥95)
- [ ] No DEFCON 1 active
- [ ] Paper matches CSV data
- [ ] All figures conclusionary
- [ ] Abstract contains ≥3 numbers

---

## Related Documents

- `00_architecture.md` - Overall architecture
- `07_validation_gates.md` - Detailed gate specifications
- `08_output_structure.md` - Output file specifications
- Protocol 2: Phase Sequential Order
- Protocol 13: Mock Court Rewind (DEFCON 1)

---

**Document Version**: v3.1.0
**Last Updated**: 2026-01-24
**Status**: Complete ✅
