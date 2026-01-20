# Model Design Expectations Validation Protocol

> **Version**: v2.5.7
> **Date**: 2026-01-19
> **Purpose**: Define strict validation protocol for model design expectations with scoring tables

---

## Problem Statement

**CRITICAL ISSUE**: No explicit model design expectations are listed, and validation is not systematic.

**Examples of Missing Validations**:
```
Model Design says: "NUTS sampler with 10000 draws"
Implementation: "Slice sampler with 1000 draws"
Current state: No systematic check, no scoring table, no auto-reject

Model Design says: "15 features including GDP, host advantage"
Implementation: "Uses available columns (10 features)"
Current state: No verification, no tolerance specification
```

**Root Causes**:
1. **No explicit design expectations documented** - Only vague descriptions
2. **No parameter tolerance specifications** - What's acceptable deviation?
3. **No scoring tables** - How to grade compliance?
4. **No systematic comparison** - Design vs Actual format missing
5. **No "one fail = all fail" enforcement** - Partial passes accepted

---

## Solution: Model Design Expectations Framework

### Framework Overview

**For every model design, a MANDATORY "Design Expectations Table" must be created:**

```markdown
## Model Design Expectations (MANDATORY)

### Category 1: Sampling Algorithm
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Sampler | NUTS (No-U-Turn Sampler) | NUTS | NUTS | - | YES |
| Gradient Calculation | ∂logp/∂θ (auto-diff) | ∂logp/∂θ | ∂logp/∂θ | - | YES |
| Tree Depth | 5-10 layers | 5 | 10 | layers | YES |
| Iterations per draw | ~100-200 | 80 | 200 | gradient evals | YES |

### Category 2: MCMC Parameters
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Chains | 4 | 4 | 4 | chains | YES |
| Tune samples | 2000 | 2000 | 2000 | samples | YES |
| Draw samples | 20000 | 20000 | 20000 | samples | YES |
| Total iterations | 88000 | 88000 | 88000 | samples | YES |

### Category 3: Features
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Total features | 15 | 15 | 15 | features | YES |
| Specific features | GDP, host_advantage, years, Gold, Silver, Bronze, ... | ALL | ALL | - | YES |

### Category 4: Computational Requirements
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Training time | 12-18 hours | 12 | 18 | hours | NO* |

*Training time has tolerance: if algorithm correct but faster/slower, investigate but don't auto-reject
```

---

## Validation Protocol

### Phase 1.5: Time Estimate Validation with Expectations Table

**@time_validator MUST create a comparison table:**

```markdown
## Model Design Expectations Validation Report

### Files Read
- ✓ Model design: output/model/model_design_{i}.md
- ✓ Dataset: output/implementation/data/features_{i}.pkl
- ✓ Implementation: output/implementation/code/model_{i}.py

### Design vs Actual Comparison

#### Category 1: Sampling Algorithm
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Sampler | NUTS | Slice | ❌ NO | Exact match required | ⚠️ SIMPLIFIED |
| Tree Depth | 5-10 | 3 | ❌ NO | 5-10 layers | ⚠️ SIMPLIFIED |
| Iterations per draw | 100-200 | ~50 | ❌ NO | 80-200 gradient evals | ⚠️ SIMPLIFIED |

**Verdict**: ❌ FAIL - Algorithm simplified beyond tolerance

#### Category 2: MCMC Parameters
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Chains | 4 | 2 | ❌ NO | Exact (4) | ❌ REJECT |
| Tune | 2000 | 1000 | ❌ NO | ±20% max | ❌ REJECT |
| Draws | 20000 | 10000 | ❌ NO | ±20% max | ❌ REJECT |
| Total | 88000 | 20000 | ❌ NO | ±20% max | ❌ REJECT |

**Verdict**: ❌ FAIL - All parameters simplified beyond tolerance

#### Category 3: Features
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Total features | 15 | 10 | ❌ NO | Exact (15) | ❌ INCOMPLETE |
| Specific features | GDP, host, years, Gold, Silver, Bronze | AthleteCount, EventCount, Years | ❌ NO | ALL required | ❌ INCOMPLETE |

**Verdict**: ❌ FAIL - Missing 5 critical features

#### Category 4: Computational Requirements
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Training time | 12-18 hours | 0.72 hours (43 min) | ❌ NO | ≥30% (3.6h min) | ❌ REJECT |

**Verdict**: ❌ FAIL - 5× below red line threshold

### Overall Score

| Category | Weight | Score | Weighted Score |
|----------|--------|-------|----------------|
| Sampling Algorithm | CRITICAL | 0/4 | 0 |
| MCMC Parameters | CRITICAL | 0/4 | 0 |
| Features | CRITICAL | 0/2 | 0 |
| Computational | HIGH | 0/1 | 0 |

**Total Score**: 0/11 (0%)

**Final Verdict**: ❌ **REJECT** - All categories failed

**Action Required**: @code_translator must rework implementation to match design specifications exactly.
```

---

## Scoring System

### Score Calculation

**Each parameter checked independently:**

```
Score per parameter:
  ✅ PASS = 1 point (within tolerance)
  ⚠️ WARNING = 0.5 points (minor deviation, note but approve)
  ❌ FAIL = 0 points (outside tolerance, auto-reject if critical)

Category score = (sum of parameter scores) / (total parameters)

Overall score = (weighted category scores) / (total weight)
```

### Pass/Fail Thresholds

**CRITICAL Parameters** (auto-reject if fail):
- Sampler type (NUTS vs Slice)
- Chains (must be exact)
- Features (must be all present)
- Algorithm (PyMC vs sklearn)

**HIGH Parameters** (warning if fail, may approve with justification):
- Iterations (±20% tolerance)
- Tree depth (±20% tolerance)
- Training time (≥30% red line)

**MEDIUM Parameters** (informational):
- Convergence metrics
- Effective sample size

### Decision Matrix

| Overall Score | Verdict | Action |
|---------------|---------|--------|
| 100% | ✅ APPROVE | Proceed to next phase |
| 80-99% | ⚠️ APPROVE WITH NOTE | Minor deviations noted, acceptable |
| 50-79% | ❌ REJECT | Significant deviations, rework required |
| <50% | ❌ AUTO-REJECT | Major violations, complete rework |

**CRITICAL RULE**: **If ANY CRITICAL parameter fails → AUTO-REJECT regardless of overall score**

---

## Tolerance Specifications

### Absolute Parameters (No Tolerance)

**These parameters MUST match exactly:**

| Parameter | Required Value | Acceptable Values | Tolerance |
|-----------|----------------|-------------------|-----------|
| Sampler type | NUTS | NUTS | 0% |
| Chains | 4 | 4 | 0% |
| Features (count) | 15 | 15 | 0% |
| Library | PyMC | PyMC | 0% |

### Narrow Tolerance Parameters (±10%)

**These parameters have narrow tolerance:**

| Parameter | Design | Acceptable Range | Tolerance |
|-----------|--------|------------------|-----------|
| Tree depth | 5-10 | 4.5-11 | ±10% |
| Target accept | 0.95 | 0.855-1.0 | ±10% |

### Standard Tolerance Parameters (±20%)

**These parameters have standard tolerance:**

| Parameter | Design | Acceptable Range | Tolerance |
|-----------|--------|------------------|-----------|
| Tune samples | 2000 | 1600-2400 | ±20% |
| Draw samples | 20000 | 16000-24000 | ±20% |
| Total iterations | 88000 | 70400-105600 | ±20% |

### Red Line Parameters (≥30%)

**These parameters have red line (minimum acceptable):**

| Parameter | Design | Red Line | Below Red Line = |
|-----------|--------|----------|-----------------|
| Training time | 12-18h | 3.6h (30%) | ❌ AUTO-REJECT |

---

## @director Enforcement Protocol

### One Fail = All Fail Rule

**@director's decision logic:**

```python
def evaluate_validation_report(validation_report):
    """
    @director's evaluation of validation report

    Returns: APPROVE / REJECT
    """
    # Check CRITICAL parameters first
    critical_params = validation_report['critical_parameters']
    for param in critical_params:
        if param['verdict'] == 'FAIL':
            return {
                'decision': 'REJECT',
                'rationale': f"CRITICAL parameter '{param['name']}' failed: {param['reason']}",
                'action': 'Rework required. No exceptions.',
                'one_fail_rule': 'ENGAGED'
            }

    # Check overall score
    overall_score = validation_report['overall_score']
    if overall_score < 0.5:  # 50%
        return {
            'decision': 'REJECT',
            'rationale': f"Overall score {overall_score*100:.0f}% below 50% threshold",
            'action': 'Major violations. Complete rework required.',
            'one_fail_rule': 'ENGAGED'
        }

    if overall_score < 0.8:  # 80%
        return {
            'decision': 'REJECT',
            'rationale': f"Overall score {overall_score*100:.0f}% below 80% threshold",
            'action': 'Significant deviations. Partial rework required.',
            'one_fail_rule': 'ENGAGED'
        }

    # All passed
    return {
        'decision': 'APPROVE',
        'rationale': f"Overall score {overall_score*100:.0f}% meets 80% minimum",
        'action': 'Proceed to next phase',
        'one_fail_rule': 'NOT ENGAGED'
    }
```

### Examples

**Example 1: One Critical Fail = REJECT**
```
@time_validator reports:
- Sampler: PASS ✅
- Chains: PASS ✅
- Features: FAIL ❌ (missing 5 features)
- Overall score: 75%

@director decision: ❌ REJECT
Rationale: CRITICAL parameter 'Features' failed. One fail rule engaged.
Action: Add missing 5 features. No exceptions.
```

**Example 2: All Pass = APPROVE**
```
@time_validator reports:
- Sampler: PASS ✅
- Chains: PASS ✅
- Features: PASS ✅
- Iterations: 95% of design (within ±20%)
- Overall score: 98%

@director decision: ✅ APPROVE
Rationale: All CRITICAL parameters passed. Overall score 98% exceeds 80%.
Action: Proceed to Phase 5B.
```

**Example 3: Low Score = REJECT**
```
@time_validator reports:
- Sampler: PASS ✅
- Chains: PASS ✅
- Features: PASS ✅
- Iterations: 50% of design (below ±20%)
- Tree depth: 50% of design (below ±10%)
- Overall score: 65%

@director decision: ❌ REJECT
Rationale: Overall score 65% below 80% threshold.
Action: Increase iterations and tree depth to within tolerance.
```

---

## @modeler Responsibility: Create Design Expectations

**When @modeler creates model_design_{i}.md, MUST include:**

### Section: Design Expectations Table (MANDATORY)

```markdown
## Design Expectations Table (MANDATORY)

### Must Be Included in Every Model Design

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Tune | 2000 | 2000 | 2000 | samples | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |
| Features | 15 | 15 | 15 | features | YES |
| Tree depth | 5-10 | 5 | 10 | layers | YES |
| Training time | 12-18h | 12 | 18 | hours | NO |

**All values are MANDATORY unless marked "Must Not Simplify = NO"**
```

### Section: Rationale for Specifications (MANDATORY)

```markdown
## Specification Rationale

### Sampler: NUTS (No-U-Turn Sampler)
**Why**: Hamiltonian Monte Carlo with automatic tuning
**Alternatives considered**: Slice (simpler), Metropolis-Hastings (less efficient)
**Cannot simplify to**: Slice, Metropolis-Hastings, sklearn

### Chains: 4
**Why**: Convergence diagnostics (R-hat) require ≥4 chains
**Cannot simplify to**: 2 chains (insufficient for R-hat)

### Iterations: 20000 draws + 2000 tune
**Why**: Posterior convergence requires 20000 samples
**Tolerance**: ±20% (16000-24000 acceptable)
**Cannot simplify to**: <16000 (below tolerance)
```

---

## @time_validator Responsibility: Enforce Expectations

**When @time_validator validates implementation, MUST:**

### Step 1: Read Design Expectations Table
```
Read: output/model/model_design_{i}.md
Extract: Design Expectations Table
```

### Step 2: Read Implementation Code
```
Read: output/implementation/code/model_{i}.py
Extract: Actual parameters used
```

### Step 3: Create Comparison Table
```markdown
| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| [rows...] |
```

### Step 4: Calculate Score
```python
critical_params_score = sum([p for p in critical_params if p['verdict'] == 'PASS']) / len(critical_params)
overall_score = weighted_average([category_scores])
```

### Step 5: Provide Recommendation
```
If ANY critical_param FAIL:
  return "❌ AUTO-REJECT: Critical parameter '{param}' failed"

Elif overall_score < 0.8:
  return "❌ REJECT: Score {score}% below 80% threshold"

Else:
  return "✅ APPROVE: Score {score}% meets requirements"
```

---

## Example: Complete Validation Report

**Model 1: Hierarchical Bayesian Medal Prediction**

```markdown
## Model Design Expectations Validation Report

### Files Read
- ✓ Model design: output/model/model_design_1.md (324 lines)
- ✓ Dataset: output/implementation/data/features_1.pkl (5000 rows × 50 columns)
- ✓ Implementation: output/implementation/code/model_1.py (142 lines)

### Design vs Actual Comparison

#### Category 1: Sampling Algorithm (CRITICAL)
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Sampler | NUTS | NUTS | ✅ YES | Exact | ✅ PASS |
| Tree Depth | 5-10 | 8 | ✅ YES | 5-10 | ✅ PASS |
| Grad evals/iter | ~150 | ~145 | ✅ YES | 100-200 | ✅ PASS |

**Score**: 3/3 (100%) | **Verdict**: ✅ PASS

#### Category 2: MCMC Parameters (CRITICAL)
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Chains | 4 | 4 | ✅ YES | Exact | ✅ PASS |
| Tune | 2000 | 2000 | ✅ YES | ±20% | ✅ PASS |
| Draws | 20000 | 20000 | ✅ YES | ±20% | ✅ PASS |
| Total | 88000 | 88000 | ✅ YES | ±20% | ✅ PASS |

**Score**: 4/4 (100%) | **Verdict**: ✅ PASS

#### Category 3: Features (CRITICAL)
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Total features | 15 | 15 | ✅ YES | Exact | ✅ PASS |
| Required features | GDP, host, years, Gold, Silver, Bronze | ALL present | ✅ YES | ALL | ✅ PASS |

**Score**: 2/2 (100%) | **Verdict**: ✅ PASS

#### Category 4: Computational (HIGH)
| Parameter | Design | Actual | Match? | Tolerance | Verdict |
|-----------|--------|--------|--------|-----------|---------|
| Training time | 12-18h | 14.2h | ✅ YES | 12-18h | ✅ PASS |

**Score**: 1/1 (100%) | **Verdict**: ✅ PASS

### Overall Score

| Category | Weight | Score | Weighted Score |
|----------|--------|-------|----------------|
| Sampling Algorithm | CRITICAL | 3/3 (100%) | 3 |
| MCMC Parameters | CRITICAL | 4/4 (100%) | 4 |
| Features | CRITICAL | 2/2 (100%) | 2 |
| Computational | HIGH | 1/1 (100%) | 1 |

**Total Score**: 10/10 (100%)

**Final Verdict**: ✅ **APPROVE**

**Summary**: All parameters match design specifications exactly. Implementation is faithful.

**Action**: Proceed to Phase 5B (Full Training)
```

---

## Implementation Checklist

**For @modeler:**
- [ ] Model design includes "Design Expectations Table" section
- [ ] All parameters have Min/Max/Unit specified
- [ ] "Must Not Simplify" flag set appropriately
- [ ] Rationale provided for all specifications

**For @time_validator:**
- [ ] Read design expectations table from model_design.md
- [ ] Read actual implementation from model_{i}.py
- [ ] Created comparison table (Design vs Actual vs Tolerance vs Verdict)
- [ ] Calculated scores for each category
- [ ] Checked CRITICAL parameters (auto-reject if fail)
- [ ] Checked overall score (reject if <80%)
- [ ] Provided clear recommendation with rationale

**For @director:**
- [ ] Verify validation report includes comparison table
- [ ] Verify ALL CRITICAL parameters passed
- [ ] Verify overall score ≥80%
- [ ] Apply "one fail = all fail" rule
- [ ] Provide clear decision (APPROVE/REJECT) with rationale

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
