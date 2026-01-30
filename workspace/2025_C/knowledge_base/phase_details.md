# Phase Details: Quality Gates and Procedures

> **Source**: CLAUDE.md v3.1.0 phase descriptions
> **Purpose**: Detailed reference for quality gate procedures and phase implementation

---

## Phase 0: Problem Understanding

**Purpose**: Understand the problem, extract requirements, suggest methods

**Participants**: @reader (Read PDF, extract requirements) | @researcher (Suggest modeling methods)

**Tasks**:
- **@reader**: Read problem PDF from `output/problem/` | Extract ALL requirements (MANDATORY) | Organize by category | Write to `output/docs/research_notes.md`
- **@researcher**: Read @reader's extracted requirements | Brainstorm 3-6 modeling methods | For each: description, justification, complexity, O-Prize assessment | Write to `output/docs/research_notes.md`

**Output**: `output/docs/research_notes.md`

**Decision**: ✅ PROCEED to Phase 0.2

**Key Constraints**: @reader: ALL requirements MANDATORY | @researcher: O-Prize competitive methods

---

## Phase 0.2: Knowledge Retrieval (Protocol 20)

> [!CAUTION] **[MANDATORY] Before strategy formulation, retrieve advanced domain knowledge.**

**Purpose**: Ensure state-of-the-art mathematical foundations

**Implementation**: Call @knowledge_librarian: "Search for advanced methods related to [Problem Keywords]" | Review `output/docs/suggested_methods.md` | Pass to @researcher

**Exit**: `suggested_methods.md` exists with ≥3 advanced papers/methods

---

## Phase 0.5: Model Methodology Quality Gate

> [!CAUTION] **[MANDATORY] After @researcher, BEFORE @modeler, evaluate methodology quality.**
> **[CRITICAL] @director CANNOT read research_notes.md before delegating.**

### Purpose
Catch weak model methods BEFORE 20+ hours of implementation work.

### Entry Criteria
- @researcher completed `output/docs/research_notes.md` | Methods proposed for all requirements

### @director's Tasks (MANDATORY)

**Protocol 1: @director file reading ban**

1. **DO NOT READ research_notes.md** - Your job is coordination, not verification | Reading the file contaminates agent evaluations | Agents must read the file independently

2. **Call @advisor + @validator in PARALLEL with EXPLICIT file paths**:
   ```
   "@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10 grade). Report which file you read at the start of your response.
   "@validator: Read output/docs/research_notes.md and evaluate technical rigor (1-10 grade). Report which file you read at the start of your response."
   ```

3. **Verify both agents read the correct file**: [ ] @advisor specified: "File: output/docs/research_notes.md, Size: X lines" | [ ] @validator specified: "File: output/docs/research_notes.md, Size: X lines" | [ ] File sizes match (e.g., 843 lines) | [ ] Evaluation content references specific file content

   **If verification fails**: Re-call agent with explicit instruction: "Please read output/docs/research_notes.md and report which file you read."

4. **Wait for both evaluations**: Check `output/docs/validation/methodology_evaluation_{i}_*.md`

5. **Calculate average grade**: (advisor_avg + validator_avg) / 2

6. **Decision**:

| Average Grade | Verdict | Action |
|---------------|---------|--------|
| **>= 9/10** | ✅ EXCELLENT | Proceed to Phase 1 (high-quality methods assured) |
| **7-8/10** | ⚠️ ACCEPTABLE | Advise enhancements, proceed (optional) |
| **< 7/10** | ❌ WEAK | **Rewind to Phase 0.5** → @researcher provides better methods |

### Exit Conditions
- [ ] Both @advisor + @validator evaluations complete
- [ ] Average grade >= 9/10 OR @director decides to proceed with caution
- [ ] methodology_evaluation_{i}_advisor.md and methodology_evaluation_{i}_validator.md exist
- [ ] If rewound: @researcher revised methods within 2-3 attempts

### Rewind Protocol (Phase 0.5 Loop)
- Trigger: @advisor OR @validator gives grade < 7/10
- Action: @researcher revises `research_notes.md` with more sophisticated methods
- Re-evaluate until grade >= 9/10 OR 2-3 attempts exhausted
- If 3 attempts exhausted: @director decides (proceed with caution vs continue brainstorming)

---

## Phase 1: Model Design

### Purpose
Design mathematical models based on @researcher's methods

### Participants
- **@modeler** (primary)
- **@researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor** (consultants)

### Tasks

**@modeler**:
1. Read `output/docs/research_notes.md`
2. For each model, write draft proposal: Model overview | Mathematical formulation | Design Expectations Table (Protocol 8) | Justification
3. Save to `output/model_proposals/model_X_draft.md`

**@director**:
1. After all drafts written, call 5 consultants in PARALLEL:
   ```
   @researcher: "Read output/model/model_proposals/model_1_draft.md and provide feedback"
   @feasibility_checker: "Read output/model/model_proposals/model_1_draft.md and provide feedback"
   @data_engineer: "Read output/model/model_proposals/model_1_draft.md and provide feedback"
   @code_translator: "Read output/model/model_proposals/model_1_draft.md and provide feedback"
   @advisor: "Read output/model/model_proposals/model_1_draft.md and provide feedback"
   ```
2. Wait for all 5 feedback files

**Consultants**:
1. Read assigned draft proposal
2. Provide feedback: Strengths | Weaknesses | Suggestions for improvement
3. Save to `output/docs/consultations/feedback_model_1_{agent_name}.md`

**@modeler**:
1. Read all 5 feedback files
2. Incorporate feedback
3. Write final model design to `output/model/model_design_1.md`

### Design Expectations Table (Protocol 8)
Each model must include a Design Expectations Table specifying sampler, chains, draws, features, and computational requirements.

For the full template and examples, see `.claude/agents/modeler.md` and `.claude/agents/time_validator.md`.

### Output
- Draft proposals: `output/model_proposals/model_X_draft.md`
- Final designs: `output/model/model_design_X.md`
- Consultation feedback: `output/docs/consultations/feedback_model_X_*.md`

### Validation Gate
✅ MODEL (5 agents provide feedback)

### Key Protocols
- **Protocol 8**: Design Expectations Table (MUST be included)
- **Feedback File Standardization**: Canonical path + naming

---

## Phase 1.5: Time Estimate Validation Gate

> [!CAUTION] **[MANDATORY] After MODEL gate, validate @modeler's time estimates.**

**Entry**: 5 agents completed MODEL validation | All verdicts collected | feasibility/model_design exist

**@director Tasks**:
1. Review MODEL verdicts (2+ reject → rework first)
2. Call @time_validator: "Validate time estimates in feasibility_{i}.md and model_design_{i}.md"
3. Review report: `output/docs/validation/time_validator_{i}.md`

**Decision**:
- 4-5 approve + @time_validator OK → ✅ PROCEED Phase 2
- 4-5 approve + 1-2 models > 2x → ⚠️ QUERY @modeler
- 4-5 approve + 3+ models > 3x → ⏸️ CONSULT @advisor
- 2-3 reject → ⚠️ RETURN to @modeler (ALL 5 re-verify)
- 0-1 approve → ⏪ REWIND Phase 1

**Exit**: 4-5 approved | @time_validator report reviewed | No major discrepancies | time_validator_{i}.md exists

---

## Phase 2: Feasibility Check

**Purpose**: Assess technical feasibility of proposed models

**Participants**: @feasibility_checker

**Tasks**: Read model designs | Assess: algorithms implementable? data requirements realistic? computational requirements feasible? | Identify challenges | Provide assessment

**Output**: `output/model/feasibility_{i}.md`

**Validation**: Model validation (technical feasibility) | Code validation (implementation feasibility)

---

## Phase 3: Data Processing

### Purpose
Process data, create features, ensure data integrity

### Participants
- **@data_engineer**

### Tasks

**@data_engineer**:
1. Read problem data from `output/problem/`
2. Read model designs to understand required features
3. Create features as specified in model designs
4. Perform feature engineering
5. Ensure data integrity: Check for missing values | Check for outliers | Verify data types | Validate data ranges
6. Save features to disk: `output/implementation/data/features_{i}.pkl` (Pickled) | `output/implementation/data/features_{i}.csv` (CSV for inspection)

### Feature Creation Rules
- **ALL features from design MUST be present** (no "use available columns")
- If data is missing, MUST consult @director before proceeding
- MUST provide feature summary (count, types, ranges)

### Output
- `output/implementation/data/features_{i}.pkl`
- `output/implementation/data/features_{i}.csv`

### Validation Gate
✅ DATA (self-validation)

### Key Constraints
- **Protocol 2**: All features from design MUST be present
- No "use available columns" - if data missing, consult @director

---

## Phase 4: Code Translation

### Purpose
Translate model designs into Python code

### Participants
- **@code_translator** (primary)
- **@modeler** (consultant)
- **@validator** (validator)

### Tasks

**@code_translator**:
1. Read model design from `output/model/model_design_{i}.md`
2. Write Python code implementing the design with standard structure: imports | load_data() | preprocess_data() | build_model() | train_model() | evaluate_model() | main execution
3. Report completion

**@director**:
1. Call @modeler: "Read `output/implementation/code/model_1.py` and validate"
2. Call @validator: "Read `output/implementation/code/model_1.py` and validate"

**@modeler and @validator**:
1. Read code
2. Validate against design: Algorithm matches design? | All features included? | Parameters as specified?
3. Provide brief format report
4. If validation fails → Rewind to Phase 4

### Idealistic Mode (Protocol 5)
```
@code_translator: "I am an idealist, a perfectionist"
- Token cost is irrelevant
- Training time is irrelevant
- ONLY thing that matters: Implement design perfectly

❌ NEVER simplify without @director approval
❌ NEVER "use available columns" when features missing
❌ NEVER switch libraries (PyMC → sklearn)
✅ ALWAYS report errors to @director
✅ ALWAYS wait for guidance before proceeding
```

### Output
`output/implementation/code/model_{i}.py`

### Validation Gate
✅ CODE (2 agents: @modeler + @validator)

### Key Protocols
- **Protocol 5**: Idealistic Mode - Perfect implementation
- **Protocol 2**: Simplification = Academic Fraud

---

## Phase 4.5: Implementation Fidelity Check Gate

> [!CAUTION] **[MANDATORY] After CODE gate, check for lazy implementation.**
> **[STRICT MODE] @time_validator will AUTO-REJECT ALL unauthorized simplifications.**

### Entry Criteria
- 2 agents (@modeler, @validator) completed CODE gate | model_design + model_{i}.py exist

### @director's Tasks (MANDATORY)

1. **Review CODE verdicts**: If either rejects → rework first
2. **Call @time_validator with STRICT MODE**:
   ```
   "@time_validator: STRICT MODE check for model_{i}.py
    Verify:
    1. Algorithm match (design vs code) - PyMC must be PyMC, not sklearn
    2. Feature completeness (all designed features present) - NO 'use available columns'
    3. Iterations/parameters (within ±20% tolerance) - 10000 samples, not 1000
    4. NO unauthorized simplifications detected
    Report: output/docs/validation/time_validator_code_{i}.md"
   ```
3. **Review report**: Check output/docs/validation/time_validator_code_{i}.md
4. **Decision**:

| Condition | Action |
|-----------|--------|
| ✅ All checks pass | ✅ PROCEED Phase 5 |
| ❌ Algorithm mismatch | **AUTO-REJECT**: @code_translator must rework using correct algorithm |
| ❌ Missing features | **AUTO-REJECT**: @code_translator must include all designed features |
| ❌ Iterations reduced > 20% | **AUTO-REJECT**: @code_translator must use specified iterations |
| ⚠️ Minor tweaks (±10%) | ⚠️ NOTE and proceed (document) |

### Exit Conditions
- [ ] Both @modeler + @validator approved (or revised + re-verified)
- [ ] @time_validator strict mode report reviewed
- [ ] NO algorithm mismatches OR rework completed
- [ ] NO missing features OR rework completed
- [ ] NO unauthorized simplifications OR rework completed
- [ ] time_validator_code_{i}.md exists

**Strict Mode: Forbidden Simplifications = Academic Fraud**
- **PyMC → sklearn**: ❌ AUTO-REJECT (lazy implementation)
- **10000 → 1000 iterations**: ❌ AUTO-REJECT (10× reduction)
- **15 → 10 features**: ❌ AUTO-REJECT (incomplete)
- **"Use available columns"**: ❌ AUTO-REJECT (data structure workaround)

---

## Phase 5 Special Handling

> [!CRITICAL] **Phase 5 is BLOCKING** - Paper writing (Phase 6-7) CANNOT start until ALL models complete training successfully. No parallel workflow.

### Director Entry Point

**Director MUST call @model_trainer (coordinator) first**:
```
@model_trainer: Phase 5 Training Mission Analysis

Read all model_design_{i}.md files.
Count models, analyze dependencies, verify code/feature files exist.
Report: model count, dependencies, execution recommendation.
```

**DO NOT skip the coordinator** - @model_trainer analyzes dependencies before workers are assigned.

### Coordinator-Worker Workflow

1. @director calls @model_trainer (coordinator)
2. @model_trainer reads model_design_{i}.md, counts models, analyzes dependencies
3. @model_trainer verifies all files exist:
   - `output/implementation/code/model_{i}.py` for each model
   - `output/implementation/data/features_{i}.pkl` for each model
4. @model_trainer reports to @director with execution recommendation
5. @director delegates to workers based on dependency analysis:
   - **INDEPENDENT**: Assign all workers in PARALLEL
   - **SEQUENTIAL**: Assign workers in dependency order, wait between each
   - **MIXED**: Execute parallel batches, then sequential dependencies
6. Each worker trains ONE model → reports completion
7. @director waits for ALL workers to complete
8. Verify all results_{i}.csv files exist
9. ONLY THEN proceed to Phase 5.5

### Time Expectations

- **Minimum**: 6 hours per model
- **Typical**: 8-12 hours per model
- **Maximum**: 48 hours (with @director approval)

### Critical Requirements

- ❌ NO partial results (all models must complete)
- ❌ NO data fabrication (if training fails, fix and retry)
- ❌ NO early stopping without convergence
- ❌ NO proceeding with failures
- ❌ NO skipping @model_trainer coordinator step

### Sanity Check (Director must verify)
- [ ] No duplicate NOC/country names | [ ] No dissolved countries
- [ ] Strong countries in reasonable ranges | [ ] Host > non-host average
- [ ] Gold < Total | [ ] PI_97.5 ≥ Mean ≥ PI_2.5

**Any fail** → Block Phase 6 → Require @model_trainer fix

**See: knowledge_base/director_examples.md#emergency-protocol-examples**

### Phase 4.5 Re-Validation Trigger

> [!CAUTION] **When @code_translator modifies code during training, re-validation is REQUIRED.**
> **Purpose**: Prevent lazy implementation through hidden parameter simplifications during training.

### When Re-Validation Is Triggered

**@code_translator implements fix** → Provides CHANGES SUMMARY

**@director MUST check**:
1. Review @code_translator's CHANGES SUMMARY
2. Identify design parameter changes: **Sampling parameters** (tune, chains, draws, target_accept, treedepth) | **Algorithm changes** (NUTS → Metropolis, etc.) | **Feature additions/removals** (New features added or designed features removed)

### @director's Decision Protocol

**IF parameter changes detected in CHANGES SUMMARY**:
```
@time_validator: RE-VALIDATION REQUIRED

@code_translator has modified model_{i}.py:
Changes: {list of parameter changes}

Please run Phase 4.5 validation on reworked code:
- Check against Design Expectations Table
- Create comparison table (Design vs Actual vs Tolerance vs Verdict)
- Calculate overall score
- Return APPROVE/REJECT decision

DO NOT allow training to resume until validation complete.
```

**Training MUST NOT resume** until @time_validator completes re-validation and returns ✅ APPROVE.

**IF no parameter changes** (simple bug fix only): Allow training to resume without re-validation | Document: "Simple bug fix, no parameter changes - re-validation not required"

**See: knowledge_base/director_examples.md#re-validation-trigger-examples**

---

## Phase 5: Full Model Training (BLOCKING)

> [!CRITICAL] **Phase 5 is BLOCKING** - DO NOT proceed to Phase 6 until ALL models complete training successfully.

### Purpose
Train all models with full iterations to completion. No shortcuts, no parallel paper writing.

### Participants
- **@model_trainer** (coordinator - analyzes missions)
- **@model_trainer1-5** (workers - execute training)
- **@director** (coordination and delegation)
- **@modeler** (consultation for errors)
- **@code_translator** (fix implementation errors)

### Coordinator-Worker Workflow

1. **@director calls @model_trainer (coordinator)**:
   ```
   @model_trainer: Phase 5 Training Mission Analysis

   Read all model_design_{i}.md files.
   Count models, analyze dependencies, verify code/feature files exist.
   Report: model count, dependencies, execution recommendation.
   ```

2. **@model_trainer (coordinator) reports**:
   - Total models to train
   - Dependencies (INDEPENDENT / SEQUENTIAL / MIXED)
   - File verification (all model_{i}.py and features_{i}.pkl exist)
   - Execution recommendation

3. **@director delegates to workers**:
   - INDEPENDENT: Assign @model_trainer1-N in PARALLEL
   - SEQUENTIAL: Assign in dependency order, wait between each
   - MIXED: Parallel batches, then sequential dependencies

4. **Each worker (@model_trainer1-5)**:
   - Read code from `output/implementation/code/model_{i}.py`
   - Read data from `output/implementation/data/features_{i}.pkl`
   - Execute full training (complete iterations)
   - Enter "watch mode": Check process status every 60 seconds
   - Report completion to @director

5. **@director waits for ALL workers**:
   - Verify all results_{i}.csv files exist
   - ONLY THEN proceed to Phase 5.5

### Watch Mode (Protocol 10)
- AI session does NOT exit
- Training runs in background
- Continuous monitoring for errors
- Immediate error notification

### Error Resolution
```
Detect error → Report to @director
@director delegates fix:
  Implementation error → @code_translator
  Data error → @data_engineer
  Design issue → @modeler
Fix applied → Resume training (no restart from scratch)
```

### Emergency Delegation (Protocol 11)
**When to Use** (ALL criteria):
- Error Category: Convergence (Category 4)
- Severity: CRITICAL (R-hat > 1.3 OR 12h elapsed OR >10% divergent)
- @modeler is available and responsive
- Fix is well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**: @model_trainer → @modeler (direct escalation) | @modeler → @code_translator (direct delegation) | @code_translator → implements fix (within 10 minutes) | @director → retroactive approval (within 1 hour) | @model_trainer → resumes training

### Output
- Results: `output/implementation/data/results_{i}.csv`
- Training log: `output/implementation/logs/training_{i}.log`
- Convergence log: `output/implementation/logs/convergence_{i}.log` (if applicable)

### Validation Gate
✅ TRAINING

### Time Estimate
- Minimum: 6 hours per model
- Typical: 8-12 hours per model
- Maximum: 48 hours (with @director approval)

### Key Protocols
- **Protocol 10**: Watch Mode - AI session does NOT exit
- **Protocol 11**: Emergency Delegation - 8× faster critical error response
- **BLOCKING**: NO parallel paper writing until Phase 5 completes

---

## Phase 5.5: Enhanced Data Authenticity Verification Gate

> [!CAUTION] **[MANDATORY] After TRAINING, comprehensive anti-fraud verification.**
> **[STRICT MODE] Training Duration Red Line: < 30% of expected = AUTO-REJECT.**

### Entry Criteria
- 2 agents (@modeler, @validator) completed TRAINING | model_{i}.py + results_{i}.csv + training_{i}.log exist

### @director's Tasks (MANDATORY)

1. **Review TRAINING verdicts**: If either rejects → rework first
2. **Call @time_validator with STRICT MODE**:
   ```
   "@time_validator: STRICT MODE check for training_{i}.log
    Verify:
    1. Training Duration Red Line: actual >= 30% of expected (AUTO-REJECT if below)
    2. Training Skip Detection: iterations actually executed? convergence achieved?
    3. Algorithm Match: code uses designed algorithm (not simplified)?
    4. Feature Completeness: all designed features used?
    5. Result Authenticity: results match model type? (Bayesian has uncertainty)
    6. Code-Result Consistency: spot-check passes?
    Report: output/docs/validation/time_validator_data_{i}.md"
   ```
3. **Review report**: Check output/docs/validation/time_validator_data_{i}.md
4. **Decision**:

| Condition | Action |
|-----------|--------|
| ✅ All checks pass | ✅ PROCEED Phase 6 |
| ❌ Training < 30% of expected | **AUTO-REJECT**: Re-run with correct implementation (lazy detected) |
| ❌ Algorithm mismatch | **AUTO-REJECT**: Re-run using correct algorithm |
| ❌ Features missing | **AUTO-REJECT**: Re-run with all features |
| ⚠️ 30-70% of expected | ⚠️ INVESTIGATE: May indicate optimization or lazy |
| ⚠️ 1-2 checks fail | ⚠️ INVESTIGATE: Request explanation |

### Exit Conditions
- [ ] Both agents approved (or revised + re-verified)
- [ ] @time_validator strict mode report reviewed
- [ ] Training duration >= 30% of expected (red line passed)
- [ ] NO algorithm mismatches OR re-run completed
- [ ] NO missing features OR re-run completed
- [ ] time_validator_data_{i}.md exists
- [ ] All enhanced checks pass or issues resolved

**Strict Mode: Training Duration Red Line**
- **Red Line**: actual_hours >= 30% of minimum expected_hours
- **Example**: Expected 12-18h → Minimum acceptable: 3.6h
- **43 minutes (0.72h) vs 12-18h**: **5× below threshold → AUTO-REJECT**
- **Rationale**: Catches lazy implementations (simplified algorithms, reduced iterations)

**Enhanced Checks**:
- **Training Duration Red Line**: Actual >= 30% of expected? (AUTO-REJECT if below)
- **Algorithm Match**: Code uses designed algorithm? (PyMC, not sklearn)
- **Feature Completeness**: All designed features present? (NO "available columns")
- **Training Skip Detection**: Iterations executed? Convergence achieved?
- **Result Authenticity**: Results match model type? (Bayesian has uncertainty)
- **Code-Result Consistency**: Spot-check passes?

**Red Flags = AUTO-REJECT**:
- Training < 30% of expected (e.g., 43 min vs 12-18h)
- Algorithm mismatch (sklearn vs PyMC)
- Missing features (10/15 features)
- No iteration markers
- Point estimates from Bayesian
- Results don't match code

---

## Phase 5.8: Methodology Evolution Documentation

> [!CAUTION] **[MANDATORY] Convert technical struggles into research insights.**

### Purpose
Document technical challenges, methodological refinements, and domain insights using academic discourse (not narrative storytelling).

### Implementation
1. **Call @metacognition_agent**: "Analyze dev_diary.md and logs for research insights."
2. **Output**: `output/docs/methodology_evolution_{i}.md`
3. **Usage**: @writer incorporates insights into Discussion section (≤2 sentences per item)

### Template and Resources
- **Main Template**: `knowledge_library/templates/methodology_evolution_template.md`
- **Quick Reference**: See `knowledge_library/templates/methodology_evolution_template.md` for structure, examples, and quality checklist
- **Agent Instructions**: `.claude/agents/metacognition_agent.md` (template reference on line 210)
- **Integration Guide**: `.claude/agents/writer.md` (Phase 7E guidance on line 574)

### Academic Standards
- Use neutral technical language (no "journey," "epiphany," "treasure")
- Present limitations transparently but briefly
- Focus on methodological progression, not storytelling
- Align with reference paper style (e.g., 2009116.pdf limitations section)

### Exit Conditions
- [ ] `methodology_evolution_{i}.md` exists in `output/docs/`
- [ ] At least 1 technical challenge → insight mapping identified
- [ ] Language is technical and neutral (no emotional framing)
- [ ] All claims supported by quantitative data

---

## Phase 6: Visualization

### Purpose
Generate figures from model results

### Participants
- **@visualizer**

### Tasks

**First Pass** (with quick results from Phase 5A):
1. Read `results_quick_{i}.csv`
2. Generate figures: Scatter plots (predictions vs actual) | Histograms (residuals, distributions) | Line plots (time series, convergence) | Bar charts (feature importance) | Heatmaps (correlation matrices) | Box plots (distributions by category) | etc.
3. Save with standard naming: `{model_number}_{figure_type}_{description}.png`
4. Verify image quality (check for corruption)

**Second Pass** (when Phase 5B completes):
1. Read `results_{i}.csv` (final results)
2. Regenerate all figures with final data
3. Update all figures

### Image Naming Standards
```
{model_number}_{figure_type}_{description}.png

Examples:
- model_1_scatter_predictions_vs_actual.png
- model_1_histogram_residuals.png
- model_1_trace_plot.png
- model_2_bar_feature_importance.png
- model_2_line_convergence.png
```

### Output
`output/figures/*.png`

### Key Protocols
- Image naming standards
- Quality verification

---

## Phase 6.5: Visualization Quality Gate

> [!CAUTION] **[MANDATORY] After @visualizer, verify image quality.**

### Implementation

1. **Request verification**: "@visualizer: Run image quality verification on all figures. Report file size, dimensions, corruption."
2. **Verify**:
```bash
# Count all PNG files
ls -1 output/figures/*.png | wc -l

# Verify image quality
python3 -c "
from PIL import Image
import os

corrupted = []
for f in sorted(os.listdir('output/figures')):
    if f.endswith('.png'):
        try:
            img = Image.open(os.path.join('output/figures', f))
            img.verify()
            img = Image.open(os.path.join('output/figures', f))
            print(f'{f}: {img.size[0]}x{img.size[1]} - OK')
        except Exception as e:
            print(f'{f}: CORRUPTED - {e}')
            corrupted.append(f)

if corrupted:
    print(f'\\nCORRUPTED IMAGES: {len(corrupted)}')
    exit(1)
"
```
3. **If corruption**: @visualizer regenerates (max 2) | If 2 failures → request rewind
4. **Rewind targets**: Phase 5 (invalid results) | Phase 3 (data corrupted) | Phase 1 (unvisualizable)

### Exit Conditions
- ✅ **PASS**: All valid, non-zero, proper dimensions → Phase 7
- ❌ **FAIL**: Corruption → Rewind or regenerate

**Rewind Triggers**: Negative values (Phase 5) | NaN/Inf (Phase 3) | 0 bytes (Phase 5/3) | All pixels same (Phase 5/3) | Unplottable (Phase 1)

---

## Phase 7: Paper Writing (SPLIT INTO 7A-7F)

> [!CAUTION] **[CRITICAL] Phase 7 is split into 6 sub-phases (7A-7F) to prevent timeouts.**
> **Each sub-phase is called separately and checkpoints progress.**

### Purpose
Write complete 25-page LaTeX paper from results using incremental sub-phases

### Participants
- **@writer** (primary)
- **@director** (orchestrates sub-phases)

### Why Split Into Sub-Phases?
**Root Cause**: Previous attempts to write 25-page paper (5000+ words) in single agent call consistently timed out after 4-5 hours, wasting all previous work.

**Solution**: Break into 6 manageable chunks (7A-7F), each 10-40 minutes, with checkpoint/resume capability.

**Benefits**:
- Each sub-phase completes in 10-40 minutes (manageable)
- Can resume from failed sub-phase (don't lose previous work)
- Progress visible incrementally
- Follows writer.md's section-by-section protocol
- Expected time reduction: 28% (115-150 min → 80-115 min)

---

### Sub-Phase Overview

| Sub-Phase | Sections | Est. Time | Output | Checkpoint |
|-----------|----------|-----------|--------|------------|
| **7A** | Abstract + Introduction + Notation | 10-15 min | paper.tex (framework) | 7A complete |
| **7B** | Model sections (5 models) | 30-40 min | paper.tex (appended) | 7A-7B complete |
| **7C** | Results section (data + figures) | 15-20 min | paper.tex (appended) | 7A-7C complete |
| **7D** | Sensitivity + Strengths/Weaknesses | 10-15 min | paper.tex (appended) | 7A-7D complete |
| **7E** | Discussion + Conclusions + Bibliography | 10-15 min | paper.tex (complete) | 7A-7E complete |
| **7F** | LaTeX compilation to PDF | 5-10 min | paper.pdf | 7A-7F complete |

**Total Estimated Time**: 80-115 minutes

---

### Phase 7A: Paper Framework

**Purpose**: Write Abstract + Introduction + Notation sections

**Input Files**:
- `output/docs/research_notes.md`
- `output/docs/requirements_checklist.md`
- `output/docs/methodology_evolution_{i}.md` (from Phase 5.8)

**Director Call**:
```
@writer: Phase 7A - Write paper framework

Write the following sections for output/paper/paper.tex:
1. Abstract (250-350 words, 3-5 quantitative metrics)
   - Structure: Background → Methods → Results → Implications
   - Use active voice and strong verbs
   - Template reference: knowledge_library/templates/writing/1_abstract_template.md
2. Introduction (2-2.5 pages)
   - Problem Background (1 paragraph)
   - Restatement of Problem (1 paragraph with 6 requirements bulleted)
   - Our Approach (1 sentence per model = 5 sentences)
3. Notation table (if not in template)

Requirements:
- Use \documentclass{mcmthesis}
- Include \mcmsetup{} with team number and problem
- Write \begin{abstract}...\end{abstract}
- Include \tableofcontents

DO NOT write model sections yet (that's Phase 7B).

After completion, report:
- Sections written
- Word count
- Confirm paper.tex created
```

**Output**: `output/paper/paper.tex` (~200-300 lines)

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7A.status = "completed"

---

### Phase 7B: Model Sections

**Purpose**: Write complete model sections (5 models with full mathematical detail)

**Input Files**:
- `output/paper/paper.tex` (from Phase 7A)
- `output/model/model_design.md` (CRITICAL - copy equations WORD-FOR-WORD)

**Director Call**:
```
@writer: Phase 7B - Write model sections

Read output/paper/paper.tex to verify Phase 7A is complete.

Then APPEND model sections following this structure FOR EACH MODEL:

## Model Section Template (1.5-2.5 pages per model, NOT 2-3 pages)

### Subsection 1: Model Overview (2-3 sentences)
- What the model does
- Which requirement(s) it addresses
- Why this approach is appropriate

### Subsection 2: Mathematical Formulation (0.75-1 page)
- Present key equations in \begin{align}...\end{align}
- Number all equations: \label{eq:name}
- Define parameters IMMEDIATELY after each equation (inline, not separate tables)
  where:
  \begin{itemize}
    \item $X$ is [definition]
    \item $Y$ denotes [definition]
  \end{itemize}

### Subsection 3: Solution Approach (4-6 steps)
\begin{enumerate}
  \item [Step 1: Brief title] - 1-2 sentence description
  \item [Step 2: Brief title] - 1-2 sentence description
  ...
\end{enumerate}

### Subsection 4: Model Justification (1 paragraph)
- Link to problem requirements
- Mention why this approach is better than alternatives
- Note any limitations (briefly)

CRITICAL REQUIREMENTS:
- Copy equations WORD-FOR-WORD from model_design.md
- Define ALL parameters inline (after equations), NOT in separate tables
- Each model: 1.5-2.5 pages TOTAL (not 2-3 pages)
- DO NOT summarize equations
- DO NOT create separate notation tables

After writing, read back paper.tex to verify no corruption.
```

**Output**: `output/paper/paper.tex` (~600-800 lines total)

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7B.status = "completed"

---

### Phase 7C: Results Integration

**Purpose**: Integrate results data and figures

**Input Files**:
- `output/paper/paper.tex` (from Phase 7B)
- `output/implementation/data/results_quick_*.csv`
- `output/figures/*.png` (22 figures)

**Director Call**:
```
@writer: Phase 7C - Integrate results data and figures

Read output/paper/paper.tex to verify Phases 7A-7B are complete.

Then APPEND Results section following this structure:

## Results Section Template (4-5 pages)

### Section 1: Results Overview (1 paragraph)
- Summary of key findings
- Mention 2-3 most important metrics

### Section 2: Requirement-Specific Results (repeat for each requirement)

#### Title
**Context** (1-2 sentences): What this addresses

**Quantitative Findings** (2-3 paragraphs):
- Start with specific numbers
- Integrate tables/figures HERE (at first mention, not at end)
- Reference format: "Figure X shows Y (Observation), indicating Z (Implication)"

**Table/Figure Integration**:
Use [H] placement and relative path ../figures/

\begin{table}[H]
\centering
\begin{tabular}{lcc}
\toprule
Column 1 & Column 2 & Column 3 \\
\midrule
Data 1 & 123.4 & 45.6 \\
Data 2 & 234.5 & 56.7 \\
\bottomrule
\end{tabular}
\caption{[Specific finding] (Observation), indicating [implication] (Implication).
Key metric: [number].}
\label{tab:name}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
\caption{[Observation with number], indicating [implication].}
\label{fig:name}
\end{figure}

**Key Insights** (bulleted):
- Item 1: [Specific number] → [Implication]
- Item 2: [Specific number] → [Implication]

### Section 3: Unexpected Findings (1-2 paragraphs)
- What surprised you
- Why it matters

CRITICAL REQUIREMENTS:
- Every claim must have a number
- Place figures/tables at first mention using [H]
- Use relative path: ../figures/ (NOT figures/)
- All captions follow Observation → Implication format
- Each figure/table referenced in text BEFORE it appears

After writing, read back paper.tex to verify no corruption.
```

**Output**: `output/paper/paper.tex` (~800-1000 lines total)

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7C.status = "completed"

---

### Phase 7D: Analysis Sections

**Purpose**: Write Sensitivity Analysis + Strengths/Weaknesses sections

**Input Files**:
- `output/paper/paper.tex` (from Phase 7C)
- `output/model/model_design.md` (sensitivity plans)

**Director Call**:
```
@writer: Phase 7D - Write analysis sections

Read output/paper/paper.tex to verify Phases 7A-7C are complete.

Then APPEND analysis sections:

## Sensitivity Analysis Section (1-1.5 pages)

For each model (1-2 paragraphs per model):
- Parameter tested
- Range tested
- Results observed (with specific numbers)
- Implications for model robustness

## Strengths and Weaknesses Section (1-1.5 pages)

### Strengths (3-4 focused items)
\begin{itemize}
  \item \textbf{[Strength 1 Title]}\\
  [Explanation with specific example or number]
  \item \textbf{[Strength 2 Title]}\\
  [Explanation with specific example or number]
\end{itemize}

### Weaknesses (2-3 honest limitations with mitigations)
\begin{itemize}
  \item \textbf{[Weakness 1 Title]}\\
  [Explanation + mitigation strategy]
  \item \textbf{[Weakness 2 Title]}\\
  [Explanation + mitigation strategy]
\end{itemize}

CRITICAL REQUIREMENTS:
- Be specific (include numbers where possible)
- Avoid generic strengths ("our model is comprehensive")
- Be honest about weaknesses but provide mitigations
- Reference sensitivity analysis plans from model_design.md
- Anti-patterns reference: knowledge_library/templates/writing/6_anti_patterns.md

After writing, read back paper.tex to verify no corruption.
```

**Output**: `output/paper/paper.tex` (~1000-1200 lines total)

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7D.status = "completed"

---

### Phase 7E: Conclusions

**Purpose**: Write Discussion + Conclusions + Bibliography

**Input Files**:
- `output/paper/paper.tex` (from Phase 7D)
- `output/docs/methodology_evolution_{i}.md` (from Phase 5.8)

**Director Call**:
```
@writer: Phase 7E - Write conclusions and bibliography

Read output/paper/paper.tex to verify Phases 7A-7D are complete.

Then APPEND final sections:

## Discussion and Conclusions Section (2.5-3 pages)

### Synthesis and Conclusions (1 paragraph)
- Primary conclusions linked to specific results
- How results validate/challenge expectations

### Response to Each Requirement (1 paragraph each)
\subsubsection{Response to Requirement 1}
[Clear, direct answer with numerical result]

\subsubsection{Response to Requirement 2}
[Clear, direct answer with numerical result]

[Continue for all 6 requirements]

### Evaluation and Bias Analysis (1-1.5 paragraphs)
- Model effectiveness (accuracy, robustness, efficiency)
- Potential biases: Data, Model, Computational
- Mitigation strategies employed

### Implications (1 paragraph)
- Broader implications for the field
- Societal, economic, or environmental relevance
- Unexpected outcomes

### Final Recommendations (1 paragraph)
- Key takeaways
- Contribution to solving the problem
- Next steps for investigation

## Bibliography (1-1.5 pages)

\begin{thebibliography}{9}

\bibitem{ref1}
Author, A.~A., (Year). ``Title of Paper,'' \textit{Journal Name}, Vol.~X, No.~Y, pp.~123--145.

[Add 8-12 references for methods, data sources, etc.]

\end{thebibliography}

CRITICAL REQUIREMENTS:
- Each requirement response: Start with specific numerical answer
- Total length: 2.5-3 pages (not 4-5 pages)
- Include 8-12 references
- DO NOT repeat results (synthesize, don't restate)
- Brevity constraint: Max 2 sentences per methodology evolution item from Phase 5.8

After writing, do final read of entire paper.tex to verify completeness.
```

**Output**: `output/paper/paper.tex` (complete, ~1200-1400 lines)

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7E.status = "completed"

---

### Phase 7F: LaTeX Compilation

**Purpose**: Compile LaTeX to PDF and verify

**Input Files**:
- `output/paper/paper.tex` (complete from Phase 7E)

**Director Call**:
```
@writer: Phase 7F - Compile LaTeX to PDF

Read output/paper/paper.tex to verify it's complete.

Pre-compilation checks:
- [ ] All \includegraphics use ../figures/ (not figures/)
- [ ] All figures referenced in text before they appear
- [ ] All tables/figures have descriptive captions
- [ ] Paper ≤25 pages (excluding summary sheet)

Then compile LaTeX:
cd output/paper
pdflatex paper.tex
pdflatex paper.tex  # Run twice for references

Check exit code:
- 0 = Success
- Non-zero = Compilation failed

If failed:
1. Check paper.log for errors: grep -i "error" paper.log
2. Common issues to fix:
   - Missing } or \end{env}
   - Math mode errors (_ or ^ outside $...$)
   - File not found (check figure paths)
3. Fix errors (max 3 attempts total)
4. Retry compilation

After success:
- Verify PDF exists: ls -lh paper.pdf
- Check page count: pdfinfo paper.pdf | grep Pages
- Verify figures render (not placeholders)

Report compilation status:
SUCCESS: paper.pdf generated (N pages, M MB)
FAILURE: errors encountered, specify errors

After success, paper.pdf is ready for Phase 7.5 (LaTeX Gate).
```

**Output**: `output/paper/paper.pdf`

**Checkpoint**: Update `VERSION_MANIFEST.json` with phase_7_subphases.7F.status = "completed"

---

### Checkpoint/Resume Protocol

**Checkpoint Tracking**: After each Phase 7 sub-phase (7A-7F), update `VERSION_MANIFEST.json`:

```json
{
  "phase_7_subphases": {
    "7A": {
      "name": "Paper Framework",
      "status": "completed",
      "timestamp": "2026-01-28T14:30:00Z",
      "output_file": "output/paper/paper.tex",
      "sections": ["Abstract", "Introduction", "Notation"]
    },
    "7B": {
      "name": "Model Sections",
      "status": "completed",
      "timestamp": "2026-01-28T15:15:00Z",
      "output_file": "output/paper/paper.tex",
      "sections": ["Model Development"]
    },
    "7C": {
      "name": "Results Integration",
      "status": "in_progress",
      "timestamp": "2026-01-28T15:30:00Z",
      "output_file": "output/paper/paper.tex",
      "sections": ["Results"]
    }
  },
  "phase_7_resume_point": "7C"
}
```

**Resume Protocol**: If timeout occurs at Phase 7C:
1. Check `VERSION_MANIFEST.json` for last completed sub-phase
2. Resume from Phase 7C (skip 7A-7B, already done)
3. Read `paper.tex` to verify current state
4. Continue from where work stopped

---

### Output Files
- `output/paper/paper.tex` - Complete LaTeX source
- `output/paper/paper.pdf` - Compiled PDF (after Phase 7F)

### Template References
- Full LaTeX template: `.claude/agents/writer.md` (lines 614-967)
- Abstract template: `knowledge_library/templates/writing/1_abstract_template.md`
- Anti-patterns guide: `knowledge_library/templates/writing/6_anti_patterns.md`
- Methodology evolution: `knowledge_library/templates/methodology_evolution_template.md`

### Validation Gate
✅ PAPER (4 agents: @writer + @visualizer + @summarizer + @editor)

---

## Phase 7.5: LaTeX Compilation Gate

> [!CAUTION] **[MANDATORY] After @writer, verify LaTeX compiles.**

### Implementation

1. **Request**: "@writer: Compile paper_{i}.tex, report SUCCESS/FAILURE"
2. **Verify**: `ls -lh output/paper/paper_{i}.pdf && file output/paper/paper_{i}.pdf && grep -i "error" output/paper/paper_{i}.log`
3. **If FAIL**: @writer fixes (max 3) | If 3 failures → Rewind Phase 7
4. **If SUCCESS**: Proceed Phase 8

### Exit Conditions
- ✅ **PASS**: PDF valid, no errors → Phase 8
- ❌ **FAIL**: 3 failures → Rewind Phase 7

---

## Phase 8: Summary

### Purpose
Create 1-page summary of paper

### Participants
- **@summarizer** (primary)
- **@editor** (review)

### Tasks

**@summarizer**:
1. Read paper
2. Extract key information: Problem statement | Methods used | Key results | Main conclusions
3. Write 1-page summary
4. Compile to PDF

**@editor**:
1. Review summary
2. Verify 1-page constraint
3. Check clarity and accuracy

---

## Phase 9: Polish

### Purpose
Polish paper for grammar, style, and consistency

### Participants
- **@editor** (primary)
- **@writer** (review)
- **@summarizer** (review)

### Tasks

**@editor**:
1. Read paper
2. Review for: Grammar errors | Style inconsistencies | Clarity issues | Formatting problems
3. Make corrections
4. Provide feedback for multi-agent rework
5. Finalize paper

**@writer and @summarizer**:
1. Review @editor's changes
2. Provide feedback
3. Collaborate on final version

### Output
Polished `output/paper/paper.pdf`

### Validation Gate
✅ FINAL (3 agents: @editor + @writer + @summarizer)

---

## Phase 9.1: Mock Judging (Protocol 13 / DEFCON 1)

> [!CAUTION] **[MANDATORY] Subject the paper to adversarial review BEFORE final polish.**

### Implementation
1. **Call @judge_zero**: "Review output/paper/paper.pdf using 3 personas (O-Prize, Technical, Clarity)."
2. **Review Report**: `output/docs/judgment_report.md`
3. **Verdict**: PASS / REJECT

### DEFCON 1 Protocol (If REJECTED)
- **Halt Progress**: Stop all Phase 10 activities.
- **Kill List**: Identify the "Fatal Flaws" (max 3).
- **Repair Tickets**: Assign specific agents to fix ONLY the fatal flaws.
- **Re-Judge**: @judge_zero reviews ONLY the fixes.
- **Mercy Rule**: After 3 rejects, Conditional Pass.

In practice:
1. Parse judgment_report.md into 1–3 concrete repair tickets, each with a responsible agent.
2. Run ticket fixes in parallel, then have @editor integrate and sanity-check.
3. Resubmit to @judge_zero focusing on the fixed items only.
4. If still REJECTED, repeat (max 3 total cycles, then apply Mercy Rule).

**See: knowledge_base/director_examples.md#mock-court-defcon-1-examples**

---

## Phase 9.5: Editor Feedback Enforcement

> [!CAUTION] **[MANDATORY] Enforce appropriate action for @editor verdict.**

### Verdict Categories

| Verdict | Meaning | Action |
|---------|---------|--------|
| **APPROVED** | No issues | → Phase 10 |
| **MINOR_REVISION** | Small polish | @writer fixes → **@editor re-verifies** → APPROVED → Phase 10 |
| **CRITICAL_ISSUES** | Major | Multi-agent rework |

**MINOR_REVISION Flow** (Critical):
```
@editor: MINOR_REVISION → @writer fixes → **@editor re-verifies** (NOT self-verify!)
→ APPROVED → Phase 10
```

**Multi-Agent Rework**:
1. Parse @editor's report by responsible agent
2. Send parallel revision requests
3. Wait for ALL to complete
4. Send to @editor for RE-VERIFICATION
5. Loop until APPROVED (max 3)

---

## Phase 10: Final Review

### Purpose
Final quality assessment

### Participants
- **@advisor**

### Tasks

**@advisor**:
1. Read final paper
2. Assess overall quality: Problem understanding | Methodological sophistication | Result quality | Paper clarity | O-Prize competitiveness
3. Provide final grade and feedback

### Output
Final assessment report

### Key Protocol
@advisor MUST report which file was read (Protocol 1)

---

## Phase 10 Rewind Rules

> [!CRITICAL] **[MANDATORY] When @advisor returns NEEDS_REVISION, modified paper MUST go back to Phase 9 (@editor).**

### Process Flow

```
Phase 10: @advisor identifies issues
  ↓
Categorize by agent (writing/data/methodology/results)
  ↓
Send to responsible agents for revisions
  ↓
**CRITICAL**: Modified paper → Phase 9 (@editor) re-review
  ↓
@editor: APPROVED → Back to Phase 10 re-verification
         NEEDS_REVISION → Loop (max 3)
  ↓
Phase 10: @advisor APPROVED → Submission ready
```

**Deadlock Prevention**:
- ❌ WRONG: @writer → directly to Phase 10 (skips @editor)
- ✅ CORRECT: @writer → @editor re-review → Phase 10

**Key Principle**: "ALL paper modifications must undergo @editor's final review"

---

## Phase 11: Self-Evolution

> [!CAUTION] **[MANDATORY] Capture lessons for the NEXT competition.**

### Implementation
1. **Director Analysis**: Review `VERSION_MANIFEST.json` and agent logs.
2. **Identify Patterns**: What worked? What failed? Which agent needs prompting updates?
3. **Write Report**: `output/docs/self_evolution_report.md`
4. **Update System**: (Optional) Propose changes to `CLAUDE.md` for v3.2.0.

---

*Reference: CLAUDE.md - Main operational documentation*
