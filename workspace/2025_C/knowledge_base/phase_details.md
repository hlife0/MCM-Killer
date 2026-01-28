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

### Two-Stage Training

**Phase 5A (MANDATORY, ≤30 min)**: 10-20% data, reduced iterations, ensure viability → `results_quick_{i}.csv`
**Phase 5B (MANDATORY, >6 hours, runs in parallel)**: Full dataset, full convergence → `results_{i}.csv`

**PARALLEL WORKFLOW**: Phase 5A completes → **Proceed to Phase 6 (quick) and Phase 7 (draft) immediately** | Phase 5B runs in **parallel** with paper writing | When Phase 5B completes → Update figures and paper with final results

**Time Expectations**: Minimum: 6 hours per model | Typical: 8-12 hours per model | Maximum: 48 hours (with @director approval)

**❌ FORBIDDEN**: Skip Phase 5A or 5B | Use "time constraints" as excuse
**✅ REQUIRED**: Complete 5A → Proceed immediately to Phase 6-7 | Execute 5B in parallel with paper writing

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

## Phase 5A: Quick Training

### Purpose
Generate quick results to enable parallel paper writing

### Participants
- **@model_trainer**

### Tasks

**@model_trainer**:
1. Read code from `output/implementation/code/model_{i}.py`
2. Read data from `output/implementation/data/features_{i}.pkl`
3. Start quick training (reduced iterations): Example: If design specifies 10000 iterations, use 1000
4. Generate quick results: `results_quick_{i}.csv`
5. Report completion

### Output
`output/results/results_quick_{i}.csv`

### Validation Gate
✅ TRAINING

### Time Estimate
~30 minutes per model

### Key Decision
**PROCEED IMMEDIATELY to Phase 6** (don't wait for Phase 5B)

---

## Phase 5B: Full Training (Parallel with Paper)

### Purpose
Train models with full iterations while paper proceeds in parallel

### Participants
- **@model_trainer** (primary)
- **@director** (coordination)
- **@modeler** (consultation for errors)
- **@code_translator** (fix implementation errors)

### Tasks

**@model_trainer**:
1. Read code from `output/implementation/code/model_{i}.py`
2. Read data from `output/implementation/data/features_{i}.pkl`
3. Start full training in background
4. Enter "watch mode": Check process status every 60 seconds | Check log file for errors | If error detected → report_to_director() and await_guidance() | If training_complete → report_completion()
5. Report status every 30 minutes
6. When complete, report training summary

**Watch Mode** (Protocol 10): AI session does NOT exit | Training runs in background | Continuous monitoring for errors | Immediate error notification

**Error Resolution**: Detect error → Report to @director | @director delegates fix: Implementation error → @code_translator | Data error → @data_engineer | Design issue → @modeler | Fix applied → Resume training (no restart from scratch)

**Emergency Delegation** (Protocol 11):
**When to Use** (ALL criteria): Error Category: Convergence (Category 4) | Severity: CRITICAL (R-hat > 1.3 OR 12h elapsed OR >10% divergent) | @modeler is available and responsive | Fix is well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**: @model_trainer → @modeler (direct escalation) | @modeler → @code_translator (direct delegation) | @code_translator → implements fix (within 10 minutes) | @director → retroactive approval (within 1 hour) | @model_trainer → resumes training

### Output
- Trained model: `output/implementation/models/model_{i}_full.pkl`
- Training log: `output/implementation/logs/training_{i}_full.log`
- Results: `output/results/results_{i}.csv`

### Validation Gate
✅ TRAINING

### Time Estimate
- Minimum: 6 hours
- Typical: 8-12 hours
- Maximum: 48 hours (with @director approval)

### Key Protocols
- **Protocol 4**: Parallel Workflow - Paper proceeds immediately
- **Protocol 10**: Watch Mode - AI session does NOT exit
- **Protocol 11**: Emergency Delegation - 8× faster critical error response

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

## Phase 5.8: Insight Extraction (Narrative Arc)

> [!CAUTION] **[MANDATORY] Convert technical struggles into research insights.**

### Purpose
Transform "we had a bug" into "we discovered a fundamental constraint of the system."

### Implementation
1. **Call @metacognition_agent**: "Analyze dev_diary.md and logs for research insights."
2. **Output**: `output/docs/narrative_arc_{i}.md`
3. **Usage**: @writer MUST incorporate these insights into the Discussion/Conclusion.

### Exit Conditions
- [ ] `narrative_arc_{i}.md` exists.
- [ ] At least 1 "Failure -> Insight" mapping identified.

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

## Phase 7: Paper Writing

### Purpose
Write complete LaTeX paper from results

### Participants
- **@writer** (primary)
- **@visualizer** (figures)
- **@summarizer** (summary)
- **@editor** (review)

### Tasks

**First Pass** (with quick results from Phase 5A):
1. Read quick results
2. Read figures
3. Write complete LaTeX paper: Abstract | Introduction | Methods | Results (with quick results) | Discussion | Conclusion | References
4. Compile LaTeX to PDF
5. Verify PDF generated successfully

**Second Pass** (when Phase 5B completes):
1. Read final results
2. Update Results section with final results
3. Update figures if needed
4. Recompile LaTeX
5. Verify PDF generated successfully

### Paper Structure
At minimum, the paper must include sections for Abstract, Introduction, Methods, Results, Discussion, Conclusion, and References.

For the full LaTeX template and class file, see `.claude/agents/writer.md` and `latex_template/` (e.g., `mcmthesis-demo.tex`).

### Output
`output/paper/paper.pdf`

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
