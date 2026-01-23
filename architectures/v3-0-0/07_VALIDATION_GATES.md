# Validation Gates

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete specification of all 7 mandatory validation gates

---

## Validation Gate Overview

| Gate | Phase | Name | Participants | Criteria | Impact |
|------|-------|------|--------------|----------|--------|
| 1 | 0.5 | METHODOLOGY | @advisor, @validator | Avg grade ≥ 9/10 | Ensures O-Prize competitive methods |
| 2 | 1 | MODEL | 5 agents | Feedback provided | Multi-agent consultation |
| 3 | 1.5 | TIME_CHECK | @time_validator | APPROVE/REJECT | Realistic time estimates |
| 4 | 3 | DATA | @data_engineer (self) | All features present | Feature completeness |
| 5 | 4 | CODE | @modeler, @validator | Matches design | Implementation fidelity |
| 6 | 4.5 | FIDELITY | @time_validator | Score ≥ 80%, no critical failures | Strict compliance |
| 7 | 5A/5B | TRAINING | @model_trainer (self) | Completion verified | Training success |
| 8 | 5.5 | ANTI_FRAUD | @time_validator | All checks pass | Academic integrity |
| 9 | 6.5 | VISUAL | @visualizer, @director | All images valid | Figure quality |
| 10 | 7 | PAPER | 4 agents | Complete paper | Paper quality |
| 11 | 7.5 | LATEX | @writer, @director | Compiles successfully | PDF generation |
| 12 | 8 | SUMMARY | 2 agents | 1-page constraint met | Summary quality |
| 13 | 9 | FINAL | 3 agents | Polish complete | Document quality |
| 14 | 9.5 | EDITOR | @director, agents | Feedback addressed | Multi-agent rework |

---

## Gate 1: METHODOLOGY (Phase 0.5)

### Purpose
Evaluate methodology quality BEFORE implementation starts

### Participants
- **@advisor**: Quality assessment
- **@validator**: Validation

### Evaluation Criteria

For each proposed method, evaluate:
1. **Sophistication Level**:
   - Basic: Simple regression, basic statistics
   - Moderate: Multiple regression, basic ML
   - Advanced: Bayesian methods, deep learning, ensemble methods

2. **Computational Intensity**:
   - Low: < 1 hour training
   - Medium: 1-6 hours training
   - High: > 6 hours training

3. **O-Prize Competitiveness**:
   - Weak: Basic methods, unlikely to be competitive
   - Moderate: Good methods, some competitive potential
   - Strong: Advanced methods, highly competitive

### Grading Scale
- **10/10**: Advanced sophistication, High computational intensity, Strong competitiveness
- **9/10**: Advanced/Moderate sophistication, Medium/High intensity, Strong/Moderate competitiveness
- **8/10**: Moderate sophistication, Medium intensity, Moderate competitiveness
- **7/10**: Moderate/Basic sophistication, Low/Medium intensity, Moderate/Weak competitiveness
- **≤ 6/10**: Basic sophistication, Low intensity, Weak competitiveness

### Decision Criteria
- **Average grade ≥ 9/10**: ✅ PROCEED to Phase 1
- **Average grade 7-8/10**: ⚠️ ADVISE @researcher to enhance methods (optional)
- **Average grade < 7/10**: ❌ REWIND to Phase 0 (@researcher MUST brainstorm better methods)

### Output Format
```markdown
# Methodology Evaluation Report

## Overall Assessment
Average Grade: [X.X/10]
Verdict: ✅ PROCEED / ⚠️ ADVISE / ❌ REWIND

## Method-by-Method Evaluation

### Method 1: [Name]
- Sophistication: [Basic/Moderate/Advanced]
- Computational Intensity: [Low/Medium/High] (~[X] hours)
- O-Prize Competitiveness: [Weak/Moderate/Strong]
- Grade: [X/10]

### Method 2: [Name]
...

## Feedback
[Weaknesses and suggestions for improvement]
```

### Key Protocols
- **Protocol 1**: @director file reading ban - @director CANNOT read research_notes.md
- **Protocol 9**: Brief format - First 4 lines in chat, detailed report to file

---

## Gate 2: MODEL (Phase 1)

### Purpose
Multi-agent consultation for model design feedback

### Participants (5 consultants)
- **@researcher**: Method alignment and quality
- **@feasibility_checker**: Technical feasibility
- **@data_engineer**: Data requirements and feature engineering
- **@code_translator**: Implementation feasibility
- **@advisor**: Overall quality and O-Prize competitiveness

### Consultation Process

1. **@modeler** writes draft proposals
2. **@director** sends to 5 consultants in PARALLEL
3. Each consultant provides feedback:
   - Strengths
   - Weaknesses
   - Suggestions for improvement
4. **@modeler** reads all feedback
5. **@modeler** writes final designs incorporating feedback

### Feedback Format
```markdown
# Feedback: Model [N] - [Agent Name]

## Strengths
1. [Strength 1]
2. [Strength 2]

## Weaknesses
1. [Weakness 1]
2. [Weakness 2]

## Suggestions for Improvement
1. [Suggestion 1]
2. [Suggestion 2]
```

### Decision Criteria
- **All 5 feedback files present**: ✅ PROCEED to Phase 1.5
- **Missing feedback**: @director MUST request from missing consultant

### Key Protocols
- **Feedback File Standardization**: Canonical path + naming
- **Protocol 8**: Design Expectations Table MUST be included

---

## Gate 3: TIME_CHECK (Phase 1.5)

### Purpose
Validate time estimates before implementation

### Participant
- **@time_validator**

### Validation Criteria

**Per-Model Analysis**:
1. **Algorithm Type**: Identify algorithm (e.g., PyMC hierarchical, sklearn, neural network)
2. **Dataset Size**: Check dimensions (e.g., 5000×50)
3. **Parameters**: Check iterations, chains, epochs
4. **Complexity**: Estimate O(n) complexity

**Time Estimation**:
Use empirical table:
| Algorithm | Dataset | Samples | Expected Time |
|-----------|---------|---------|---------------|
| PyMC hierarchical | 5000×50 | 10000×4 | 12-15 hours |
| sklearn.LinearRegression | ANY | ANY | <0.1 hours |
| Random Forest | 5000×50 | 100 trees | 0.5-1 hours |
| Neural Network | 5000×50 | 1000 epochs | 2-4 hours |

**Fidelity Checks**:
1. **Algorithm Match**: Does code use designed algorithm?
2. **Feature Completeness**: Are all features included?
3. **Iteration/Parameter**: Are parameters as specified?

### Decision Criteria
- **Total estimate ≤ 48 hours**: ✅ PROCEED to Phase 2
- **Total estimate > 48 hours**:
  - If competition remaining ≥ estimate × 1.2 → PROCEED (20% buffer)
  - If competition remaining ≥ estimate → PROCEED_WITH_CAUTION (tight)
  - If competition remaining < estimate → CONSULT_MODELER (need prioritization)

### Output Format
```markdown
# Time Validation Report

## Per-Model Estimates
- Model 1: [X-Y] hours (algorithm, dataset, params)
- Model 2: [X-Y] hours (...)
...

## Total Estimate
[X-Y] hours (range: [min] - [max])

## Fidelity Checks
- Algorithm Match: ✅ All models use designed algorithms
- Feature Completeness: ✅ All features present
- Iteration/Parameter: ✅ Within tolerance

## Recommendation
✅ APPROVE / ❌ REJECT / ⚠️ ESCALATE

## Rationale
[Explanation for recommendation]
```

### Key Protocols
- **Protocol 3**: Enhanced Analysis - Read 3 files, line-by-line
- **Protocol 6**: 48-Hour Escalation - Decision framework
- **Protocol 7**: Handoff - Standardized communication

---

## Gate 4: DATA (Phase 3)

### Purpose
Validate data integrity and feature completeness

### Participant
- **@data_engineer** (self-validation)

### Validation Criteria

**Feature Completeness**:
- [ ] All features from design present
- [ ] No "use available columns" shortcuts
- [ ] If data missing, consulted @director

**Data Integrity**:
- [ ] No missing values (or properly handled)
- [ ] No obvious outliers (or properly handled)
- [ ] Data types correct
- [ ] Data ranges reasonable

**Data Quality**:
- [ ] Feature count matches design
- [ ] Feature types match design
- [ ] Feature statistics calculated

### Self-Validation Report
```markdown
# Data Validation Report: Model [N]

## Feature Completeness
- Total features in design: [N]
- Total features created: [N]
- Verdict: ✅ ALL PRESENT / ❌ MISSING FEATURES

## Data Integrity
- Missing values: [None / Handled]
- Outliers: [None / Handled]
- Data types: ✅ Correct / ❌ Issues
- Data ranges: ✅ Reasonable / ❌ Issues

## Feature Summary
| Feature | Type | Count | Range | Missing |
|---------|------|-------|-------|---------|
| ... | ... | ... | ... | ... |

## Verdict
✅ PASS / ❌ FAIL
```

### Decision Criteria
- **All features present + data integrity OK**: ✅ PROCEED to Phase 4
- **Missing features or data issues**: ❌ REWIND to Phase 3

### Key Protocols
- **Protocol 2**: All features from design MUST be present
- No "use available columns" - if data missing, consult @director

---

## Gate 5: CODE (Phase 4)

### Purpose
Validate code correctness against design

### Participants
- **@modeler**: Design alignment
- **@validator**: Code correctness

### Validation Criteria

**Design Alignment** (@modeler):
- [ ] Algorithm matches design
- [ ] All features included
- [ ] Parameters as specified
- [ ] Library matches design (e.g., PyMC vs sklearn)

**Code Correctness** (@validator):
- [ ] Code syntax correct
- [ ] No obvious bugs
- [ ] Logic correct
- [ ] Error handling present

### Validation Report Format
```markdown
# Code Validation Report: Model [N]

## @modeler Evaluation
- Algorithm Match: ✅ / ❌
- Feature Completeness: ✅ / ❌
- Parameter Match: ✅ / ❌
- Library Match: ✅ / ❌
- Grade: [X.X/10]

## @validator Evaluation
- Syntax: ✅ / ❌
- Logic: ✅ / ❌
- Error Handling: ✅ / ❌ / ⚠️ (not needed)
- Grade: [X.X/10]

## Issues Found
1. [Issue 1]
2. [Issue 2]

## Verdict
✅ PASS / ❌ FAIL
```

### Decision Criteria
- **Both @modeler and @validator PASS**: ✅ PROCEED to Phase 4.5
- **Either FAIL**: ❌ REWIND to Phase 4

### Key Protocols
- **Protocol 5**: Idealistic Mode - Perfect implementation
- **Protocol 2**: Simplification = Academic Fraud

---

## Gate 6: FIDELITY (Phase 4.5)

### Purpose
Strict validation of implementation fidelity against design

### Participant
- **@time_validator**

### Validation Criteria

**Comparison Table**:
| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | NUTS | 0% | Exact | ✅ PASS |
| Chains | 4 | 2 | -50% | ±20% | ❌ FAIL |
| Draws | 20000 | 20000 | 0% | ±0 | ✅ PASS |

**Scoring System**:
- **CRITICAL parameters**: Auto-reject if fail
  - Sampler, Algorithm, Core features
- **HIGH parameters**: ±20% tolerance
  - Draws, Tune, Iterations
- **Overall score**: Must be ≥80%
- **Rule**: One fail = all fail

**Decision Logic**:
```python
if ANY critical_param FAIL:
    return "REJECT"  # No exceptions
elif overall_score < 0.8:
    return "REJECT"
else:
    return "APPROVE"
```

### STRICT MODE (Protocol 2)
- **Training Duration Red Line**: Auto-reject if < 30% of expected
- **Algorithm Match**: Must be exact match
- **Feature Completeness**: All features must be present
- **Iterations**: Must be ≥ 80% of specified

### Output Format
```markdown
# Implementation Fidelity Report: Model [N]

## Comparison Table
[Table as above]

## Overall Score
[X.X%]

## Critical Failures
- [List any critical failures]

## Recommendation
✅ APPROVE / ❌ REJECT

## Rationale
[Explanation]
```

### Decision Criteria
- **No critical failures AND score ≥ 80%**: ✅ PROCEED to Phase 5A
- **Critical failure OR score < 80%**: ❌ REWIND to Phase 4

### Key Protocols
- **Protocol 2**: STRICT MODE - Training duration red line
- **Protocol 8**: Design Expectations - Systematic validation
- **Protocol 12**: Re-Validation - Validate code fixes during training

---

## Gate 7: TRAINING (Phase 5A/5B)

### Purpose
Verify training completion

### Participant
- **@model_trainer** (self-validation)

### Validation Criteria

**Phase 5A (Quick Training)**:
- [ ] Training completed
- [ ] Results saved: `results_quick_{i}.csv`
- [ ] No critical errors

**Phase 5B (Full Training)**:
- [ ] Training completed
- [ ] Results saved: `results_{i}.csv`
- [ ] Training log saved
- [ ] Model saved: `model_{i}_full.pkl`
- [ ] No critical errors (or errors resolved)

### Training Report Format
```markdown
# Training Report: Model [N]

## Phase 5A (Quick Training)
- Status: ✅ Complete / ❌ Failed
- Time: [X] minutes
- Results: results_quick_{i}.csv
- Errors: [None / Description]

## Phase 5B (Full Training)
- Status: ✅ Complete / ❌ Failed
- Time: [X] hours
- Results: results_{i}.csv
- Model: model_{i}_full.pkl
- Training Log: training_{i}_full.log
- Errors: [None / Description + Resolution]

## Verdict
✅ PASS / ❌ FAIL
```

### Decision Criteria
- **Training completed successfully**: ✅ PROCEED
- **Training failed**: ❌ Retry or escalate

### Key Protocols
- **Protocol 10**: Watch Mode - AI session does NOT exit
- **Protocol 11**: Emergency Delegation - 8× faster critical error response

---

## Gate 8: ANTI_FRAUD (Phase 5.5)

### Purpose
Verify training authenticity and prevent academic fraud

### Participant
- **@time_validator**

### Validation Criteria

**1. Training Skip Detection**:
- [ ] Training log contains actual iteration progress
- [ ] Epochs/iterations were actually executed
- [ ] No "faked" logs (copied output without real training)

**2. Training Duration Verification**:
- [ ] Actual duration ≥ 30% of expected duration
- [ ] Duration consistent with method complexity

**3. Result Authenticity**:
- [ ] Results match model type (Bayesian has uncertainty, not point estimates)
- [ ] Convergence criteria were met
- [ ] Intermediate results valid (checkpoints if available)

**4. Code-Result Consistency**:
- [ ] Spot-check: Code on subset matches CSV results
- [ ] Random seed results reproducible (if seed set)

### Decision Criteria
- **All checks pass**: ✅ AUTHENTIC → Proceed to Phase 6
- **1-2 checks fail**: ⚠️ SUSPICIOUS → Investigate, may request re-run
- **3+ checks fail**: ❌ FABRICATED → Re-run with verification

### Output Format
```markdown
# Data Authenticity Report: Model [N]

## Training Skip Detection
- Iteration progress: ✅ Verified / ❌ Missing
- Verdict: ✅ Authentic / ❌ Fabricated

## Training Duration Verification
- Expected: [X] hours
- Actual: [Y] hours
- Ratio: [Y/X]%
- Verdict: ✅ Valid / ❌ Suspicious (< 30%)

## Result Authenticity
- Match model type: ✅ / ❌
- Convergence met: ✅ / ❌ / ⚠️ Partial
- Verdict: ✅ Authentic / ❌ Fabricated

## Code-Result Consistency
- Spot-check: ✅ Consistent / ❌ Inconsistent
- Verdict: ✅ Authentic / ❌ Fabricated

## Overall Verdict
✅ AUTHENTIC / ⚠️ SUSPICIOUS / ❌ FABRICATED

## Recommendation
PROCEED / INVESTIGATE / RE-RUN
```

### Key Protocols
- **Protocol 2**: STRICT MODE - Training duration red line (< 30% = auto-reject)

---

## Gate 9: VISUAL (Phase 6.5)

### Purpose
Verify all images are present and valid

### Participants
- **@visualizer**
- **@director**

### Validation Criteria

**Image Count**:
- [ ] Expected count generated
- [ ] `ls -1 output/figures/*.png | wc -l` matches expected

**Image Quality**:
- [ ] No corrupted images (PIL verify)
- [ ] All images viewable
- [ ] Image sizes reasonable

**Image Naming**:
- [ ] Naming standard followed: `{model_number}_{figure_type}_{description}.png`
- [ ] No generic names (e.g., `figure1.png`)

### Quality Check Script
```python
from PIL import Image
import glob

corrupted = []
for img_path in glob.glob("output/figures/*.png"):
    try:
        img = Image.open(img_path)
        img.verify()
    except Exception as e:
        corrupted.append(img_path)

if corrupted:
    print(f"Corrupted images: {corrupted}")
else:
    print("All images valid")
```

### Decision Criteria
- **All images present and valid**: ✅ PROCEED to Phase 7
- **Corrupted images**: ❌ REGENERATE

---

## Gate 10: PAPER (Phase 7)

### Purpose
Validate paper completeness

### Participants (4 agents)
- **@writer**: Paper completeness
- **@visualizer**: Figure quality and integration
- **@summarizer**: Summary alignment
- **@editor**: Language and style

### Validation Criteria

**@writer**:
- [ ] All sections present (Abstract, Introduction, Methods, Results, Discussion, Conclusion, References)
- [ ] Content complete
- [ ] LaTeX syntax correct

**@visualizer**:
- [ ] All figures included
- [ ] Figure captions present
- [ ] Figures referenced in text

**@summarizer**:
- [ ] Summary aligns with paper
- [ ] Key points captured

**@editor**:
- [ ] Grammar acceptable
- [ ] Style consistent
- [ ] No major language issues

### Decision Criteria
- **All 4 agents PASS**: ✅ PROCEED to Phase 7.5
- **Any agent FAIL**: ❌ REWIND to Phase 7

---

## Gate 11: LATEX (Phase 7.5)

### Purpose
Verify LaTeX compilation

### Participants
- **@writer**
- **@director**

### Validation Criteria

**Compilation**:
- [ ] `pdflatex paper.tex` succeeds
- [ ] `bibtex paper` succeeds
- [ ] No LaTeX errors
- [ ] PDF generated successfully

**PDF Quality**:
- [ ] PDF viewable
- [ ] All pages present
- [ ] Figures appear correctly
- [ ] No formatting issues

### Decision Criteria
- **LaTeX compiles successfully**: ✅ PROCEED to Phase 8
- **Compilation errors**: ❌ FIX and recompile

---

## Gate 12: SUMMARY (Phase 8)

### Purpose
Validate summary completeness

### Participants
- **@summarizer**
- **@editor**

### Validation Criteria

**@summarizer**:
- [ ] Summary complete
- [ ] All key points included

**@editor**:
- [ ] 1-page constraint met
- [ ] Language acceptable
- [ ] Clear and concise

### Decision Criteria
- **Summary complete + 1-page constraint**: ✅ PROCEED to Phase 9
- **Issues**: ❌ REWIND to Phase 8

---

## Gate 13: FINAL (Phase 9)

### Purpose
Validate final paper quality

### Participants (3 agents)
- **@editor**: Grammar, style, consistency
- **@writer**: Content, structure
- **@summarizer**: Alignment with summary

### Validation Criteria

**@editor**:
- [ ] Grammar reviewed
- [ ] Style consistent
- [ ] Clarity acceptable

**@writer**:
- [ ] Content accurate
- [ ] Structure logical
- [ ] All requirements addressed

**@summarizer**:
- [ ] Paper aligns with summary
- [ ] Key messages consistent

### Decision Criteria
- **All 3 agents PASS**: ✅ PROCEED to Phase 9.5
- **Any agent FAIL**: ❌ REWIND to Phase 9

---

## Gate 14: EDITOR (Phase 9.5)

### Purpose
Ensure editor feedback is addressed

### Participants
- **@director**
- Multiple agents (as needed)

### Validation Criteria

**Feedback Addressed**:
- [ ] All grammar issues fixed
- [ ] All style issues fixed
- [ ] All clarity issues addressed
- [ ] All formatting issues fixed

**Multi-Agent Rework**:
- [ ] @editor feedback documented
- [ ] Relevant agents coordinated
- [ ] Changes implemented
- [ ] Changes verified

### Decision Criteria
- **All feedback addressed**: ✅ PROCEED to Phase 10
- **Outstanding issues**: ❌ CONTINUE Phase 9.5

---

## Validation Gate Relationships

```
Gate 1 (METHODOLOGY)
    ↓
Gate 2 (MODEL)
    ↓
Gate 3 (TIME_CHECK)
    ↓
Gate 4 (DATA)
    ↓
Gate 5 (CODE)
    ↓
Gate 6 (FIDELITY) ←→ Gate 8 (ANTI_FRAUD) [Re-validation via Protocol 12]
    ↓
Gate 7 (TRAINING) ←→ Gate 10 (WATCH MODE) [Protocol 10]
    ↓
Gate 8 (ANTI_FRAUD)
    ↓
Gate 9 (VISUAL)
    ↓
Gate 10 (PAPER)
    ↓
Gate 11 (LATEX)
    ↓
Gate 12 (SUMMARY)
    ↓
Gate 13 (FINAL)
    ↓
Gate 14 (EDITOR)
    ↓
Phase 10 (Final Review)
```

---

## Common Validation Patterns

### Brief Format Protocol (Protocol 9)
**Applicable to**: Gate 1, Gate 5, Gate 8

**Format**:
```
Grade: 9.0/10 | Verdict: ✅ PASS
Justification: [One sentence]
File verified: [file_path] ([line_count] lines)
Detailed report written to: [report_path]
```

### File Reading Ban Protocol (Protocol 1)
**Applicable to**: All gates where @director delegates evaluation

**Rule**: @director CANNOT read files that agents will evaluate

### Design Expectations Protocol (Protocol 8)
**Applicable to**: Gate 2, Gate 6

**Requirement**: MUST include Design Expectations Table

### STRICT MODE Protocol (Protocol 2)
**Applicable to**: Gate 6, Gate 8

**Rules**:
- Training duration red line: < 30% = auto-reject
- Algorithm match: Must be exact
- Feature completeness: All present
- Iterations: ≥ 80% of specified

---

## Validation Gate Failures

### Failure Handling

**Gate 1 (METHODOLOGY)**:
- **REWIND to Phase 0**: @researcher MUST brainstorm better methods

**Gate 2 (MODEL)**:
- **COLLECT missing feedback**: @director MUST request from missing consultant

**Gate 3 (TIME_CHECK)**:
- **REJECT**: Re-evaluate model designs, simplify if needed
- **ESCALATE**: Consult @modeler for prioritization

**Gate 4 (DATA)**:
- **REWIND to Phase 3**: Fix data issues

**Gate 5 (CODE)**:
- **REWIND to Phase 4**: Fix code issues

**Gate 6 (FIDELITY)**:
- **REWIND to Phase 4**: Fix implementation to match design

**Gate 7 (TRAINING)**:
- **RETRY**: Fix error, retry training
- **ESCALATE**: Use emergency delegation (Protocol 11)

**Gate 8 (ANTI_FRAUD)**:
- **RE-RUN**: Re-train with verification
- **INVESTIGATE**: Check for issues

**Gate 9-14**: **REWIND to respective phase**: Fix issues

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `08_output_structure.md` for output directory structure
