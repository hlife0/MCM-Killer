# Phase 0.5: Model Methodology Quality Gate (v2.5.6)

> **Purpose**: Evaluate model methodology quality BEFORE implementation begins
> **Status**: MANDATORY for all new model development workflows
> **Fixes Issue**: Weak model methodologies only discovered in Phase 10, wasting 20+ hours

---

## Problem Summary

### v2.5.5 Issue

**Workflow**:
```
Phase 0: @reader + @researcher complete
  ↓
Phase 1: @modeler designs models based on @researcher's suggestions
  ↓
Phase 2-5: Implementation (20+ hours of work)
  ↓
Phase 10: @advisor reviews final paper
  ↓
@advisor: "This model is too simple for O-Prize. You need Bayesian MCMC."
  ↓
REWIND to Phase 1: 20+ hours wasted
```

**Problem**: No quality gate on model methodology BEFORE @modeler starts implementation

**Impact**:
- @researcher suggests weak methods (e.g., Ridge regression)
- @modeler implements them (20+ hours of work)
- @advisor only discovers in Phase 10 that methods are too weak
- Must rewind, wasting all implementation work

**Example**:
```
@researcher's research_notes.md:
  "For Requirement 1, use Ridge regression."
  "For Requirement 2, use basic Random Forest."

@modeler implements:
  Model 1: Ridge regression
  Model 2: Random Forest with default parameters

@advisor in Phase 10:
  "These are too basic for O-Prize. You need:
   - Bayesian Hierarchical Models with MCMC
   - Or Deep Neural Networks with extensive training
   - Or Large-Scale Ensemble with bootstrap"

Result: 20+ hours wasted, must rewind to Phase 1
```

---

## v2.5.6 Solution

### New Phase 0.5: Model Methodology Quality Gate

**Purpose**: Evaluate methodology quality AFTER @researcher but BEFORE @modeler

**Timing**:
```
Phase 0: @reader + @researcher complete
  ↓
Phase 0.5: @advisor + @validator evaluate methodology quality (NEW)
  ↓
If grade < 7/10:
  Rewind to Phase 0.5 → @researcher provides better methods
  ↓
If grade >= 9/10:
  Phase 1: @modeler starts design (high-quality methods assured)
```

---

## Phase 0.5 Workflow

### Step 1: @researcher Completes research_notes.md

**Output**: `output/research_notes.md`

**Content**: For each requirement, proposes methods:
```markdown
### Requirement 1: Medal Count Prediction
**Method Options**:
1. Ridge Regression
2. Bayesian Hierarchical Negative Binomial Model
3. Deep Neural Network

**Recommendation**: Ridge Regression because simple and effective
```

### Step 2: @director Calls @advisor + @validator

**Action**: Call both agents in PARALLEL

**Instructions to @advisor**:
```
@advisor, please evaluate the methodology quality:

Input: output/research_notes.md

Your task: Assess whether the proposed methods are sophisticated enough for O-Prize competition.

Output: output/docs/validation/methodology_evaluation_{i}_advisor.md

For each method, grade:
- Sophistication level (1-10)
- Computational intensity (1-10)
- O-Prize competitiveness (1-10)

Overall verdict:
- Grade >= 9/10: ✅ EXCELLENT - Proceed to Phase 1
- Grade 7-8/10: ⚠️ ACCEPTABLE - But recommend enhancements
- Grade < 7/10: ❌ WEAK - Must propose better methods
```

**Instructions to @validator**:
```
@validator, please evaluate the methodology quality:

Input: output/research_notes.md

Your task: Assess whether the proposed methods are technically sound and rigorous.

Output: output/docs/validation/methodology_evaluation_{i}_validator.md

For each method, grade:
- Mathematical rigor (1-10)
- Computational feasibility (1-10)
- Validation approach (1-10)

Overall verdict: Same grading scale as @advisor
```

### Step 3: @advisor and @validator Evaluate (PARALLEL)

**Criteria**:

**@advisor evaluates**:
1. **Sophistication Level** (1-10):
   - 1-3: Basic methods (Ridge, basic sklearn)
   - 4-6: Moderate methods (tuned sklearn, simple ensembles)
   - 7-8: Advanced methods (Bayesian MCMC, deep learning)
   - 9-10: State-of-the-art (novel hybrid approaches)

2. **Computational Intensity** (1-10):
   - 1-3: < 1 hour (too fast, violates v2.5.5 requirements)
   - 4-6: 1-2 hours (acceptable but not ideal)
   - 7-8: 2-4 hours (good)
   - 9-10: 4-6 hours (excellent, meets v2.5.5 requirements)

3. **O-Prize Competitiveness** (1-10):
   - 1-3: Weak (unlikely to win)
   - 4-6: Moderate (decent but not outstanding)
   - 7-8: Strong (competitive)
   - 9-10: Excellent (O-Prize material)

**@validator evaluates**:
1. **Mathematical Rigor** (1-10):
   - Does the method have solid theoretical foundation?
   - Are assumptions justified?
   - Is uncertainty quantified?

2. **Computational Feasibility** (1-10):
   - Can the method be implemented?
   - Are computational resources sufficient?
   - Is time estimate realistic?

3. **Validation Approach** (1-10):
   - Is there a validation strategy?
   - Are there multiple validation methods?
   - Is sensitivity analysis planned?

### Step 4: @director Collects Evaluations

**Read both evaluation files**:
```
Read: output/docs/validation/methodology_evaluation_{i}_advisor.md
Read: output/docs/validation/methodology_evaluation_{i}_validator.md
```

**Calculate average grade**:
```python
# Extract grades from both evaluations
advisor_grades = [grade for each method in advisor_evaluation]
validator_grades = [grade for each method in validator_evaluation]

# Calculate averages
advisor_avg = mean(advisor_grades)
validator_avg = mean(validator_grades)

# Overall average
overall_avg = (advisor_avg + validator_avg) / 2
```

### Step 5: @director Makes Decision

**Decision Criteria**:

| Overall Grade | Verdict | Action |
|---------------|---------|--------|
| **>= 9/10** | ✅ **EXCELLENT** | Proceed to Phase 1 |
| **7-8/10** | ⚠️ **ACCEPTABLE** | Advise enhancements, proceed |
| **< 7/10** | ❌ **WEAK** | Rewind to Phase 0.5 |

### Step 6A: If Grade >= 9/10 (EXCELLENT)

**Action**: Proceed to Phase 1

**Message to @modeler**:
```
@modeler, Phase 0.5 methodology evaluation complete.

Verdict: ✅ EXCELLENT (grade {X}/10)

@advisor and @validator both agree the proposed methods are sophisticated enough for O-Prize.

You may proceed to Phase 1: Model Design.

Use the methods from research_notes.md as the foundation for your model design.
```

**@modeler proceeds**:
- Reads `research_notes.md` (high-quality methods)
- Writes draft proposal to `output/model_proposals/model_X_draft.md`
- Continues with consultation workflow

### Step 6B: If Grade 7-8/10 (ACCEPTABLE)

**Action**: Advise enhancements, proceed (optional)

**Message to @modeler**:
```
@modeler, Phase 0.5 methodology evaluation complete.

Verdict: ⚠️ ACCEPTABLE (grade {X}/10)

The methods are acceptable but could be more sophisticated.

Optional enhancements recommended by @advisor and @validator:
{list of enhancements}

You may proceed to Phase 1, but consider incorporating these enhancements.
```

**@modeler proceeds** (with option to enhance):
- Reads `research_notes.md`
- Considers recommended enhancements
- Writes draft proposal (with or without enhancements)

### Step 6C: If Grade < 7/10 (WEAK)

**Action**: Rewind to Phase 0.5

**Message to @researcher**:
```
@researcher, Phase 0.5 methodology evaluation complete.

Verdict: ❌ WEAK (grade {X}/10)

@advisor and @validator both agree the proposed methods are NOT sophisticated enough for O-Prize.

Issues identified:
{list of issues from @advisor and @validator}

Please revise research_notes.md with more sophisticated methods.

Requirements for revision:
- Use computationally intensive methods (2-6 hours training)
- Ensure Bayesian MCMC / Deep Learning / Large-Scale Ensemble approaches
- Include uncertainty quantification
- Plan comprehensive validation

Rewind: Phase 0.5 → Provide new methods within 1 attempt.
```

**@researcher revises**:
- Reads current `research_notes.md`
- Identifies weak methods
- Replaces with more sophisticated alternatives
- Writes revised `research_notes.md`
- Reports back to @director

**Re-evaluation**:
- @director calls @advisor + @validator again
- Re-evaluate revised methods
- If grade >= 9/10: Proceed to Phase 1
- If grade < 7/10: After 2nd attempt, @director decides whether to:
  - Proceed with caution (document limitations)
  - Continue brainstorming (3rd attempt)

---

## Evaluation Report Format

### @advisor's Report

```markdown
# Methodology Evaluation - @advisor

**Input**: research_notes.md
**Date**: {timestamp}
**Evaluator**: @advisor

## Overall Assessment
**Average Grade**: {X}/10
**Verdict**: ✅ EXCELLENT / ⚠️ ACCEPTABLE / ❌ WEAK

---

## Per-Method Evaluation

### Requirement 1: {Name}

**Proposed Method**: {from research_notes.md}

**Sophistication Level** ({X}/10):
- Assessment: {Basic / Moderate / Advanced / State-of-the-art}
- Reasoning: {why this grade}
- O-Prize comparison: {How does this compare to winning papers?}

**Computational Intensity** ({X}/10):
- Expected training time: {X hours}
- Assessment: {Meets / Does not meet} 2-6h requirement
- Reasoning: {why this grade}

**O-Prize Competitiveness** ({X}/10):
- Assessment: {Weak / Moderate / Strong / Excellent}
- Reasoning: {Why this would/wouldn't win O-Prize}
- Improvements needed: {if any}

**Grade for Method**: {X}/10

---

### Requirement 2: {Name}
{Same format}

---

## Summary

**Strengths**:
{What's good about the proposed methods}

**Weaknesses**:
{What needs improvement}

**Recommendations**:
{Specific suggestions for enhancement}

**If ACCEPTABLE or EXCELLENT**:
The methods are {acceptable / excellent}. Proceed to Phase 1.

**If WEAK**:
The methods are too weak for O-Prize. Suggest revisions:
1. {Revision 1}
2. {Revision 2}
3. {Revision 3}
```

### @validator's Report

```markdown
# Methodology Evaluation - @validator

**Input**: research_notes.md
**Date**: {timestamp}
**Evaluator**: @validator

## Overall Assessment
**Average Grade**: {X}/10
**Verdict**: ✅ EXCELLENT / ⚠️ ACCEPTABLE / ❌ WEAK

---

## Per-Method Evaluation

### Requirement 1: {Name}

**Proposed Method**: {from research_notes.md}

**Mathematical Rigor** ({X}/10):
- Theoretical foundation: {Solid / Weak / Missing}
- Assumptions: {Well-justified / Unjustified / Missing}
- Uncertainty quantification: {Included / Missing}
- Reasoning: {why this grade}

**Computational Feasibility** ({X}/10):
- Can be implemented: {Yes / No / Needs clarification}
- Resources sufficient: {Yes / No}
- Time estimate realistic: {Yes / No}
- Reasoning: {why this grade}

**Validation Approach** ({X}/10):
- Validation strategy: {Comprehensive / Basic / Missing}
- Multiple methods: {Yes / No}
- Sensitivity analysis: {Planned / Missing}
- Reasoning: {why this grade}

**Grade for Method**: {X}/10

---

### Requirement 2: {Name}
{Same format}

---

## Summary

**Strengths**:
{What's technically sound}

**Weaknesses**:
{What needs improvement}

**Recommendations**:
{Specific technical suggestions}

**If ACCEPTABLE or EXCELLENT**:
The methods are technically {acceptable / excellent}. Proceed to Phase 1.

**If WEAK**:
The methods have significant technical issues. Suggest revisions:
1. {Revision 1}
2. {Revision 2}
3. {Revision 3}
```

---

## Rewind Protocol (Phase 0.5 Loop)

### Trigger

@advisor OR @validator gives grade < 7/10

### Action

**Rewind to Phase 0.5**:
- Target: @researcher
- Purpose: Provide better methods
- Max attempts: 2-3

### Process

```
@director: "@researcher, methods too weak. Please revise."

@researcher:
  - Reads current research_notes.md
  - Identifies weak methods
  - Replaces with sophisticated alternatives
  - Writes revised research_notes.md
  - Reports: "Revision complete, grade should now be {X}/10"

@director:
  - Calls @advisor + @validator again
  - Re-evaluates revised methods
  - If grade >= 9/10: Proceed to Phase 1
  - If grade < 7/10: After 2nd attempt, decides next action
```

### After 2-3 Attempts

**If still < 7/10 after 2 attempts**:
- @director consults with @advisor + @validator
- Options:
  1. **Proceed with caution**: Document limitations, accept weaker methods
  2. **Continue brainstorming**: 3rd attempt with explicit guidance
  3. **Escalate**: Bring in external expertise (reference papers)

**Decision factors**:
- Time remaining in competition
- How close to threshold (6.5 vs 4.0)
- Specific issues (can be fixed vs fundamental)

---

## Integration with Existing Workflow

### Updated Phase Sequence

```
Phase 0: Problem Understanding
  ├─ @reader: Extract requirements
  └─ @researcher: Brainstorm methods

Phase 0.5: Model Methodology Quality Gate (NEW)
  ├─ @advisor: Evaluate sophistication
  ├─ @validator: Evaluate rigor
  └─ @director: Make decision

  If grade >= 9/10:
    → Phase 1: Model Design
  If grade < 7/10:
    → Rewind to Phase 0.5 (max 2-3 attempts)

Phase 1: Model Design
  ├─ @modeler: Design models (high-quality methods assured)
  └─ [Rest of workflow unchanged]
```

---

## Examples

### Example 1: EXCELLENT (9/10)

**research_notes.md**:
```markdown
### Requirement 1: Medal Count Prediction

**Method Options**:
1. Bayesian Hierarchical Negative Binomial Model with MCMC
   - PyMC with NUTS sampler
   - 2000 samples × 4 chains
   - Hierarchical priors for country effects
   - Training time: 4-5 hours

2. Deep Neural Network with Dropout
   - 3 hidden layers (256-128-64)
   - 5000 epochs with early stopping
   - Bayesian dropout for uncertainty
   - Training time: 3-4 hours

3. Large-Scale Ensemble with Bootstrap
   - 1000 bootstrap samples
   - Gradient Boosting base learners
   - Grid search hyperparameter tuning
   - Training time: 2-3 hours

**Recommendation**: Bayesian Hierarchical Model because:
- Most sophisticated (MCMC sampling)
- Full uncertainty quantification
- Interpretable parameters
- O-Prize competitive
```

**@advisor evaluation**:
- Sophistication: 9/10 (Bayesian MCMC is excellent)
- Computational: 10/10 (4-5 hours meets requirement)
- Competitiveness: 9/10 (O-Prize material)
- **Average**: 9.3/10

**@validator evaluation**:
- Rigor: 9/10 (Solid theoretical foundation)
- Feasibility: 9/10 (Implementable with PyMC)
- Validation: 9/10 (Comprehensive approach)
- **Average**: 9/10

**Overall**: 9.2/10 → ✅ EXCELLENT → Proceed to Phase 1

### Example 2: WEAK (5/10)

**research_notes.md**:
```markdown
### Requirement 1: Medal Count Prediction

**Method Options**:
1. Ridge Regression
2. Lasso Regression
3. Linear Regression

**Recommendation**: Ridge Regression because simple and fast.
```

**@advisor evaluation**:
- Sophistication: 2/10 (Too basic for O-Prize)
- Computational: 1/10 (Trains in seconds, violates 2-6h requirement)
- Competitiveness: 2/10 (Unlikely to win)
- **Average**: 1.7/10

**@validator evaluation**:
- Rigor: 4/10 (Mathematically sound but simplistic)
- Feasibility: 10/10 (Very implementable)
- Validation: 3/10 (Basic validation only)
- **Average**: 5.7/10

**Overall**: 3.7/10 → ❌ WEAK → Rewind to Phase 0.5

**@researcher revises** with Bayesian MCMC → Grade becomes 9/10 → Proceed

---

## Troubleshooting

### Issue: @advisor and @validator Disagree

**Symptom**: @advisor gives 9/10, @validator gives 5/10

**Solution**:
1. @director reviews both evaluations
2. Identifies specific disagreements
3. Consults both agents for clarification
4. Makes judgment call:
   - If technical concern dominates: Follow @validator
   - If competitiveness concern dominates: Follow @advisor
   - If both valid: Use lower grade (more conservative)

### Issue: Can't Reach >= 9/10 After 2 Attempts

**Symptom**: @researcher tries twice, still getting 6-7/10

**Solution**:
1. @director assesses situation:
   - How much time remaining?
   - How close to threshold?
   - What specific issues remain?
2. Options:
   - **Proceed with caution**: If 6.5-7/10 and time is limited
   - **3rd attempt**: If specific guidance can help
   - **Escalate**: Consult reference papers for inspiration

### Issue: @researcher Can't Think of Better Methods

**Symptom**: @researcher exhausted, can't propose sophisticated methods

**Solution**:
1. @director consults @advisor for specific suggestions
2. @advisor provides concrete examples:
   - "Use PyMC with NUTS, 2000 samples × 4 chains"
   - "Use Deep Neural Network with 3 hidden layers, 5000 epochs"
   - "Use Ensemble with 1000 bootstrap samples"
3. @researcher incorporates suggestions

---

**Document Version**: v2.5.6
**Created**: 2026-01-18
**Status**: MANDATORY for all new model development
