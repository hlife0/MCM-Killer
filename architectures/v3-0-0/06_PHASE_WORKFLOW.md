# Phase Workflow

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete workflow specification for all 10 phases

---

## Phase Overview

| Phase | Name | Main Agent | Validation Gate | Time Estimate |
|-------|------|-----------|-----------------|---------------|
| **0** | Problem Understanding | reader, researcher | - | 1-2 hours |
| **0.5** | Model Methodology Quality Gate | @advisor, @validator | ✅ METHODOLOGY | 30-60 min |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | 2-4 hours |
| 1.5 | Time Estimate Validation | @time_validator | ✅ TIME_CHECK | 30-60 min |
| 2 | Feasibility Check | feasibility_checker | - | 30-60 min |
| 3 | Data Processing | data_engineer | ✅ DATA (self) | 1-2 hours |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | 2-4 hours per model |
| **4.5** | Implementation Fidelity | @time_validator | ✅ FIDELITY | 30-60 min per model |
| 5A | Quick Training | model_trainer | ✅ TRAINING | ~30 min per model |
| 5B | Full Training | model_trainer | ✅ TRAINING | 6-48 hours per model |
| **5.5** | Data Authenticity | @time_validator | ✅ ANTI_FRAUD | 30 min per model |
| 6 | Visualization | visualizer | - | 30-60 min |
| 6.5 | Visual Quality Gate | visualizer, Director | ✅ VISUAL | 15 min |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | 2-3 hours (first pass) |
| 7.5 | LaTeX Compilation Gate | writer, Director | ✅ LATEX | 15 min |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | 30-60 min |
| 9 | Polish | editor | ✅ FINAL (3 agents) | 1-2 hours |
| 9.5 | Editor Feedback Enforcement | Director, multiple agents | ✅ EDITOR | 1-2 hours |
| 10 | Final Review | advisor | - | 30-60 min |

**Total Time**: ~20-30 hours (excluding Phase 5B parallel time)

---

## Phase 0: Problem Understanding

### Purpose
Understand the problem, extract requirements, suggest methods

### Participants
- **@reader**: Read PDF, extract requirements
- **@researcher**: Suggest modeling methods

### Tasks

**@reader**:
1. Read problem PDF from `output/problem/`
2. Extract ALL requirements (MANDATORY, not optional)
3. Organize by category
4. Write to `output/docs/research_notes.md`

**@researcher**:
1. Read @reader's extracted requirements
2. Brainstorm 3-6 modeling methods
3. For each method, provide:
   - Method description
   - Justification
   - Expected computational complexity
   - O-Prize competitiveness assessment
4. Write to `output/docs/research_notes.md`

### Output
`output/docs/research_notes.md`

### Decision
- ✅ PROCEED to Phase 0.5

### Key Constraints
- **@reader**: ALL requirements are MANDATORY
- **@researcher**: Methods must be O-Prize competitive

---

## Phase 0.5: Model Methodology Quality Gate ⭐

### Purpose
Evaluate methodology quality BEFORE implementation starts

### Participants
- **@advisor**: Quality assessment
- **@validator**: Validation

### Tasks

**@director**:
1. Call @advisor: "Read `output/docs/research_notes.md` and evaluate methodology quality"
2. Call @validator: "Read `output/docs/research_notes.md` and evaluate methodology quality"
3. **DO NOT read research_notes.md yourself** (Protocol 1: File Reading Ban)

**@advisor and @validator**:
1. Read `output/docs/research_notes.md`
2. For each proposed method, evaluate:
   - Sophistication level (basic / moderate / advanced)
   - Computational intensity (expected training time)
   - O-Prize competitiveness (weak / moderate / strong)
3. Assign grade (1-10) for each method
4. Calculate average grade
5. Provide feedback on weak methods
6. Write brief format in chat
7. Write detailed report to `output/docs/validations/methodology_evaluation_1.md`

### Decision Criteria
- **Average grade >= 9/10**: ✅ PROCEED to Phase 1
- **Average grade 7-8/10**: ⚠️ ADVISE @researcher to enhance methods (optional)
- **Average grade < 7/10**: ❌ REWIND to Phase 0 (@researcher MUST brainstorm better methods)

### Output
`output/docs/validations/methodology_evaluation_1.md`

### Key Protocols
- **Protocol 1**: @director file reading ban
- **Protocol 9**: Brief format for @advisor and @validator

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
2. For each model, write draft proposal:
   - Model overview
   - Mathematical formulation
   - Design Expectations Table (Protocol 8)
   - Justification
3. Save to `output/model/model_proposals/model_X_draft.md`

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
2. Provide feedback:
   - Strengths
   - Weaknesses
   - Suggestions for improvement
3. Save to `output/docs/consultations/feedback_model_1_{agent_name}.md`

**@modeler**:
1. Read all 5 feedback files
2. Incorporate feedback
3. Write final model design to `output/model/model_design_1.md`

### Design Expectations Table (Protocol 8)
```markdown
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |
```

### Output
- Draft proposals: `output/model/model_proposals/model_X_draft.md`
- Final designs: `output/model/model_design_X.md`
- Consultation feedback: `output/docs/consultations/feedback_model_X_*.md`

### Validation Gate
✅ MODEL (5 agents provide feedback)

### Key Protocols
- **Protocol 8**: Design Expectations Table (MUST be included)
- **Feedback File Standardization**: Canonical path + naming

---

## Phase 1.5: Time Estimate Validation

### Purpose
Validate time estimates before implementation

### Participants
- **@time_validator**

### Tasks

**@director**:
1. Call @time_validator with explicit file paths:
   ```
   @time_validator: "Validate time estimates for Phase 5B.

   Read:
   - output/model/model_design_*.md
   - output/implementation/data/features_*.pkl (check shape/size)
   - output/implementation/code/model_*.py (line-by-line analysis)

   Provide:
   1. Per-model time estimate
   2. Total time estimate
   3. Algorithm fidelity check
   4. Feature completeness check
   5. Recommendation: APPROVE/REJECT/ESCALATE"
   ```

**@time_validator**:
1. Read 3 file types for each model:
   - Model design: `output/model/model_design_{i}.md`
   - Dataset: `output/implementation/data/features_{i}.pkl` (check shape/size)
   - Implementation: `output/implementation/code/model_{i}.py` (line-by-line analysis)
2. Analyze code line-by-line:
   - Import statements (which library?)
   - Model definition (what algorithm?)
   - Sampling parameters (how many iterations?)
   - Loops (nested = O(n²) or O(n³)?)
3. Use empirical table:
   | Algorithm | Dataset | Samples | Expected Time |
   |-----------|---------|---------|---------------|
   | PyMC hierarchical | 5000×50 | 10000×4 | **12-15 hours** |
   | sklearn.LinearRegression | ANY | ANY | **<0.1 hours** |
4. Provide per-model and total time estimates
5. Algorithm fidelity check
6. Feature completeness check
7. Clear recommendation: APPROVE/REJECT/ESCALATE

### Decision
- **Total estimate ≤ 48 hours**: ✅ PROCEED to Phase 2
- **Total estimate > 48 hours**:
  - If competition remaining ≥ estimate × 1.2 → PROCEED
  - If competition remaining ≥ estimate → PROCEED_WITH_CAUTION
  - If competition remaining < estimate → CONSULT_MODELER

### Output
`output/docs/validation/time_validator_model_1.md`

### Validation Gate
✅ TIME_CHECK

### Key Protocols
- **Protocol 3**: Enhanced Analysis - Read 3 files, line-by-line
- **Protocol 6**: 48-Hour Escalation - Decision framework
- **Protocol 7**: Handoff - Standardized communication

---

## Phase 2: Feasibility Check

### Purpose
Assess technical feasibility of proposed models

### Participants
- **@feasibility_checker**

### Tasks

**@feasibility_checker**:
1. Read model designs
2. Assess technical feasibility:
   - Can algorithms be implemented?
   - Are data requirements realistic?
   - Are computational requirements feasible?
3. Identify potential implementation challenges
4. Provide feasibility assessment

### Output
`output/model/feasibility_{i}.md`

### Validation Participation
- **Model validation**: Technical feasibility
- **Code validation**: Implementation feasibility

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
5. Ensure data integrity:
   - Check for missing values
   - Check for outliers
   - Verify data types
   - Validate data ranges
6. Save features to disk:
   - `output/implementation/data/features_{i}.pkl` (Pickled)
   - `output/implementation/data/features_{i}.csv` (CSV for inspection)

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
2. Write Python code implementing the design:
   ```python
   # model_{i}.py

   import [required libraries]

   def load_data():
       """Load features from disk"""
       ...

   def preprocess_data():
       """Preprocess data"""
       ...

   def build_model():
       """Build model as specified in design"""
       ...

   def train_model():
       """Train model with parameters from design"""
       ...

   def evaluate_model():
       """Evaluate model performance"""
       ...

   if __name__ == "__main__":
       # Main execution
       ...
   ```
3. Report completion

**@director**:
1. Call @modeler: "Read `output/implementation/code/model_1.py` and validate"
2. Call @validator: "Read `output/implementation/code/model_1.py` and validate"

**@modeler and @validator**:
1. Read code
2. Validate against design:
   - Algorithm matches design?
   - All features included?
   - Parameters as specified?
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

## Phase 4.5: Implementation Fidelity Check

### Purpose
Validate implementation fidelity against design

### Participants
- **@time_validator**

### Tasks

**@director**:
1. Call @time_validator:
   ```
   @time_validator: "Validate implementation fidelity.

   Read:
   - output/model/model_design_1.md (Design Expectations Table)
   - output/implementation/code/model_1.py

   Provide:
   1. Comparison table (Design vs Actual vs Tolerance vs Verdict)
   2. Overall score
   3. Recommendation: APPROVE/REJECT"
   ```

**@time_validator**:
1. Read Design Expectations Table from Phase 1
2. Read implementation code
3. Create comparison table:
   | Parameter | Design | Actual | Diff | Tolerance | Verdict |
   |-----------|--------|--------|------|-----------|---------|
   | Sampler | NUTS | Slice | Changed | Exact | ❌ FAIL |
   | Chains | 4 | 2 | -50% | ±20% | ❌ FAIL |
4. Calculate overall score
5. Apply "one fail = all fail" rule:
   ```python
   if ANY critical_param FAIL:
       return "REJECT"
   elif overall_score < 0.8:
       return "REJECT"
   else:
       return "APPROVE"
   ```
6. Provide recommendation

### STRICT MODE (Protocol 2)
- **Training Duration Red Line**: Auto-reject if < 30% of expected
- **Algorithm Match**: Must be exact match
- **Feature Completeness**: All features must be present
- **Iterations**: Must be ≥ 80% of specified

### Re-Validation (Protocol 12)
If @code_translator fixes bug during training:
1. @code_translator MUST provide CHANGES SUMMARY
2. @director analyzes CHANGES SUMMARY
3. IF parameter changes → Trigger re-validation
4. @time_validator runs Phase 4.5 on reworked code

### Output
`output/docs/validation/time_validator_code_{i}.md`

### Validation Gate
✅ FIDELITY

### Key Protocols
- **Protocol 2**: STRICT MODE - Training duration red line
- **Protocol 8**: Design Expectations - Systematic validation
- **Protocol 12**: Re-Validation - Validate code fixes

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
3. Start quick training (reduced iterations):
   - Example: If design specifies 10000 iterations, use 1000
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
4. Enter "watch mode":
   ```python
   while True:
       check_process_status()
       check_log_file_for_errors()

       if error_detected:
           report_to_director()
           await_guidance()

       if training_complete:
           report_completion()
           break

       sleep(60)  # Check every 60 seconds
   ```
5. Report status every 30 minutes
6. When complete, report training summary

**Watch Mode** (Protocol 10):
- AI session does NOT exit
- Training runs in background
- Continuous monitoring for errors
- Immediate error notification

**Error Resolution**:
- Detect error → Report to @director
- @director delegates fix:
  - Implementation error → @code_translator
  - Data error → @data_engineer
  - Design issue → @modeler
- Fix applied → Resume training (no restart from scratch)

**Emergency Delegation** (Protocol 11):
**When to Use** (ALL criteria):
1. Error Category: Convergence (Category 4)
2. Severity: CRITICAL (R-hat > 1.3 OR 12h elapsed OR >10% divergent)
3. @modeler is available and responsive
4. Fix is well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**:
```
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix (within 10 minutes)
@director → retroactive approval (within 1 hour)
@model_trainer → resumes training
```

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

## Phase 5.5: Data Authenticity Gate

### Purpose
Verify training authenticity and prevent fraud

### Participants
- **@time_validator** (primary)
- **@director**

### Tasks

**@time_validator**:
1. **Training Skip Detection**:
   - Verify training log contains actual iteration progress
   - Check if epochs/iterations were actually executed
   - Look for "faked" logs (copied output without real training)

2. **Training Duration Verification**:
   - Calculate expected duration based on method complexity
   - Compare to actual training duration
   - Flag if training was suspiciously fast (< 30% of expected)

3. **Result Authenticity**:
   - Verify results match model type (Bayesian should have uncertainty)
   - Check if convergence criteria were actually met
   - Validate intermediate results (checkpoints if available)

4. **Code-Result Consistency**:
   - Spot-check: Run code on subset, compare to CSV
   - Verify randomness (if random seed set, results should be reproducible)

### Decision Criteria
- **All checks pass**: ✅ AUTHENTIC → Proceed to Phase 6
- **1-2 checks fail**: ⚠️ SUSPICIOUS → Investigate, may request re-run
- **3+ checks fail**: ❌ FABRICATED → Re-run with verification

### Output
`output/docs/validation/time_validator_data_{i}.md`

### Validation Gate
✅ ANTI_FRAUD

### Key Protocols
- **Protocol 2**: STRICT MODE - Training duration red line (< 30% = auto-reject)

---

## Phase 6: Visualization

### Purpose
Generate figures from model results

### Participants
- **@visualizer**

### Tasks

**First Pass** (with quick results from Phase 5A):
1. Read `results_quick_{i}.csv`
2. Generate figures:
   - Scatter plots (predictions vs actual)
   - Histograms (residuals, distributions)
   - Line plots (time series, convergence)
   - Bar charts (feature importance)
   - Heatmaps (correlation matrices)
   - Box plots (distributions by category)
   - etc.
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

## Phase 6.5: Visual Quality Gate

### Purpose
Verify all images are present and valid

### Participants
- **@visualizer**
- **@director**

### Tasks

1. Verify all images exist
2. Check for corrupted images:
   ```python
   from PIL import Image

   for img_path in glob.glob("output/figures/*.png"):
       try:
           img = Image.open(img_path)
           img.verify()
       except Exception as e:
           print(f"Corrupted image: {img_path}")
   ```
3. Count images: `ls -1 output/figures/*.png | wc -l`
4. Verify image quality

### Decision
- **All images present and valid**: ✅ PASS → Proceed to Phase 7
- **Corrupted images detected**: ❌ FAIL → Regenerate

### Validation Gate
✅ VISUAL

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
3. Write complete LaTeX paper:
   - Abstract
   - Introduction
   - Methods
   - Results (with quick results)
   - Discussion
   - Conclusion
   - References
4. Compile LaTeX to PDF
5. Verify PDF generated successfully

**Second Pass** (when Phase 5B completes):
1. Read final results
2. Update Results section with final results
3. Update figures if needed
4. Recompile LaTeX
5. Verify PDF generated successfully

### Paper Structure
```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}

\title{[Title]}
\author{[Authors]}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
[Abstract]
\end{abstract}

\section{Introduction}
[Introduction]

\section{Methods}
[Methods]

\section{Results}
[Results]

\section{Discussion}
[Discussion]

\section{Conclusion}
[Conclusion]

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### Output
`output/paper/paper.pdf`

### Validation Gate
✅ PAPER (4 agents: @writer + @visualizer + @summarizer + @editor)

---

## Phase 7.5: LaTeX Compilation Gate

### Purpose
Verify LaTeX compiles successfully

### Participants
- **@writer**
- **@director**

### Tasks

1. Compile LaTeX document:
   ```bash
   cd output/paper
   pdflatex paper.tex
   bibtex paper
   pdflatex paper.tex
   pdflatex paper.tex
   ```
2. Check for compilation errors
3. Verify PDF generated successfully

### Decision
- **LaTeX compiles without errors**: ✅ PASS → Proceed to Phase 8
- **Compilation errors**: ❌ FAIL → Fix and recompile

### Validation Gate
✅ LATEX

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
2. Extract key information:
   - Problem statement
   - Methods used
   - Key results
   - Main conclusions
3. Write 1-page summary
4. Compile to PDF

**@editor**:
1. Review summary
2. Verify 1-page constraint
3. Check clarity and accuracy

### Summary Structure
```markdown
# Summary

## Problem
[Brief problem statement]

## Methods
[Methods used, 2-3 sentences]

## Key Results
[Main findings, bullet points]

## Conclusions
[Main conclusions, 2-3 sentences]
```

### Output
`output/paper/summary.pdf`

### Validation Gate
✅ SUMMARY (2 agents: @summarizer + @editor)

### Constraint
1-page maximum

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
2. Review for:
   - Grammar errors
   - Style inconsistencies
   - Clarity issues
   - Formatting problems
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

## Phase 9.5: Editor Feedback Enforcement

### Purpose
Ensure editor feedback is addressed

### Participants
- **@director**
- Multiple agents (as needed)

### Tasks

1. @editor provides feedback
2. @director coordinates rework:
   - If grammar/style issues → @editor fixes
   - If content issues → Coordinate with @writer, @summarizer, etc.
3. Multiple agents revise as needed
4. Re-verify changes

### Validation Gate
✅ EDITOR

### Key Protocol
Multi-agent rework (all relevant agents participate)

---

## Phase 10: Final Review

### Purpose
Final quality assessment

### Participants
- **@advisor**

### Tasks

**@advisor**:
1. Read final paper
2. Assess overall quality:
   - Problem understanding
   - Methodological sophistication
   - Result quality
   - Paper clarity
   - O-Prize competitiveness
3. Provide final grade and feedback

### Output
Final assessment report

### Key Protocol
@advisor MUST report which file was read (Protocol 1)

---

## Phase Completion Checklist

Before moving to next phase, verify:

**Phase 0**:
- [ ] All requirements extracted
- [ ] 3-6 methods proposed
- [ ] All methods O-Prize competitive

**Phase 0.5**:
- [ ] @advisor and @validator evaluated
- [ ] Average grade >= 9/10
- [ ] Feedback documented

**Phase 1**:
- [ ] All models have Design Expectations Table
- [ ] 5 consultants provided feedback
- [ ] Final designs incorporate feedback

**Phase 1.5**:
- [ ] @time_validator read 3 file types
- [ ] Line-by-line analysis performed
- [ ] Empirical table used
- [ ] Clear recommendation provided

**Phase 2**:
- [ ] Feasibility assessed for all models
- [ ] Challenges identified

**Phase 3**:
- [ ] All features from design created
- [ ] Data integrity verified
- [ ] Features saved to disk

**Phase 4**:
- [ ] Code matches design (algorithm, features, parameters)
- [ ] @modeler and @validator validated
- [ ] No unauthorized simplifications

**Phase 4.5**:
- [ ] Comparison table created
- [ ] Overall score >= 80%
- [ ] No critical parameter failures

**Phase 5A**:
- [ ] Quick training completed
- [ ] Results saved

**Phase 5B**:
- [ ] Full training completed
- [ ] Training duration >= 30% of expected
- [ ] Watch mode maintained
- [ ] Errors resolved

**Phase 5.5**:
- [ ] Training authenticity verified
- [ ] Duration within acceptable range
- [ ] Results consistent with code

**Phase 6**:
- [ ] All figures generated
- [ ] Image naming standards followed

**Phase 6.5**:
- [ ] All images present
- [ ] No corrupted images

**Phase 7**:
- [ ] Paper complete
- [ ] All sections present
- [ ] Figures included

**Phase 7.5**:
- [ ] LaTeX compiles successfully
- [ ] PDF generated

**Phase 8**:
- [ ] Summary created
- [ ] 1-page constraint met

**Phase 9**:
- [ ] Grammar/style reviewed
- [ ] Paper polished

**Phase 9.5**:
- [ ] Editor feedback addressed
- [ ] Multi-agent rework completed

**Phase 10**:
- [ ] Final review completed
- [ ] Grade assigned

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `07_validation_gates.md` for validation gate specifications
