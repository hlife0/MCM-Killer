# 48-Hour Escalation Protocol

**Purpose**: This document extracts the decision-making framework for handling training estimates that exceed 48 hours. It provides the "One Fail = All Fail" rule and escalation procedures.

**Source**: time_validator.md (lines 612-743)
**Version**: v2.5.7
**Status**: Active - Reference guide for Phase 1.5 and 4.5 validation

---

## Step 5: Apply "One Fail = All Fail" Rule (MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] "One Fail = All Fail" decision logic**

### Decision Logic

```python
def evaluate_implementation(comparison_table):
    """
    Apply "One Fail = All Fail" rule

    Returns: APPROVE / REJECT with rationale
    """

    # Check 1: CRITICAL parameters (auto-reject if ANY fail)
    critical_params = [p for p in all_params if p['must_not_simplify'] == True]

    for param in critical_params:
        if param['verdict'] == '❌ FAIL':
            return {
                'decision': '❌ REJECT',
                'rationale': f"CRITICAL parameter '{param['name']}' failed: {param['reason']}",
                'rule': 'One fail = all fail',
                'action': 'Rework required. No exceptions.'
            }

    # Check 2: Overall score threshold
    overall_score = total_weighted_score / max_possible_weighted_score

    if overall_score < 0.8:  # 80% threshold
        return {
            'decision': '❌ REJECT',
            'rationale': f"Overall score {overall_score*100:.1f}% below 80% threshold",
            'rule': 'Score threshold',
            'action': 'Significant deviations. Partial or complete rework required.'
        }

    # All checks passed
    return {
        'decision': '✅ APPROVE',
        'rationale': f"Overall score {overall_score*100:.1f}% meets 80% minimum",
        'rule': 'All checks passed',
        'action': 'Proceed to Phase 5A (Quick Training)'
    }
```

### Examples

**Example 1: One Critical Fail = REJECT**
```markdown
### Comparison Table

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | NUTS | 0% | Exact | ✅ PASS |
| Chains | 4 | 4 | 0% | Exact | ✅ PASS |
| Draws | 20000 | 10000 | -50% | ±20% | ❌ FAIL |
| Features | 15 | 15 | 0% | Exact | ✅ PASS |

**Overall Score**: 3/4 (75%)

### Final Verdict: ❌ REJECT

**Rationale**: CRITICAL parameter 'Draws' failed (50% below design).
**Rule**: One fail = all fail
**Action**: @code_translator must rework to use 16000-24000 samples
```

**Example 2: All Pass = APPROVE**
```markdown
### Comparison Table

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | NUTS | 0% | Exact | ✅ PASS |
| Chains | 4 | 4 | 0% | Exact | ✅ PASS |
| Draws | 20000 | 19000 | -5% | ±20% | ✅ PASS |
| Features | 15 | 15 | 0% | Exact | ✅ PASS |

**Overall Score**: 4/4 (100%)

### Final Verdict: ✅ APPROVE

**Rationale**: All CRITICAL parameters passed. Overall score 100% exceeds 80%.
**Rule**: All checks passed
**Action**: Proceed to Phase 5A (Quick Training)
```

**Example 3: Low Score = REJECT**
```markdown
### Comparison Table

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | Slice | Changed | Exact | ❌ FAIL |
| Chains | 4 | 2 | -50% | Exact | ❌ FAIL |
| Draws | 20000 | 8000 | -60% | ±20% | ❌ FAIL |
| Features | 15 | 12 | -20% | Exact | ❌ FAIL |

**Overall Score**: 0/4 (0%)

### Final Verdict: ❌ AUTO-REJECT

**Rationale**: Overall score 0% below 50% unacceptable threshold.
**Rule**: Score threshold
**Action**: Complete rework required. Multiple unauthorized simplifications detected.
```

---

## Step 6: Verify with Data File

```markdown
DESIGN: "Features: Gold, Silver, Bronze, years"
FEATURES.PKL: Check if these columns exist
→ If missing: ❌ DATA STRUCTURE MISMATCH (not @code_translator's fault, but Phase 3 issue)
→ If present: ✅ DATA OK
```

---

## Step 7: Note Any @director Approvals

- If simplification approved: ⚠️ NOTE (not lazy, approved workaround)
- If no approval: ❌ LAZY (unauthorized simplification)

---

## Output Format (MANDATORY)

```markdown
# Implementation Fidelity Report: Model {i}

**Date**: {current_date}
**Checked by**: @time_validator
**Version**: v2.5.7 Design Expectations Protocol

---

## Files Read

1. ✅ Model design: `output/model/model_design_{i}.md` ({N} lines)
2. ✅ Implementation: `output/implementation/code/model_{i}.py` ({N} lines)
3. ✅ Data file: `output/implementation/data/features_{i}.pkl` ({rows} × {cols})

---

## Design Expectations Table Verification

**Design Expectations Table**: ✅ FOUND / ❌ MISSING

If ❌ MISSING:
```
❌ ERROR: @modeler did not include Design Expectations Table in model_design_{i}.md
Action: Report to @director. @modeler must update model_design_{i}.md with required table.
```

---

## Design vs Actual Comparison

### Category 1: Sampling Algorithm (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| [rows...]

**Category Score**: X/Y (Z%)
**Verdict**: ✅ PASS / ❌ FAIL

### Category 2: MCMC Parameters (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| [rows...]

**Category Score**: X/Y (Z%)
**Verdict**: ✅ PASS / ❌ FAIL

### Category 3: Features (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| [rows...]

**Category Score**: X/Y (Z%)
**Verdict**: ✅ PASS / ❌ FAIL

### Category 4: Computational Requirements (HIGH)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| [rows...]

**Category Score**: X/Y (Z%)
**Verdict**: ✅ PASS / ❌ FAIL

---

## Overall Score

| Category | Weight | Score | Weighted Score | Verdict |
|----------|--------|-------|----------------|---------|
| Sampling Algorithm | CRITICAL | X/Y (Z%) | X | ✅/❌ |
| MCMC Parameters | CRITICAL | X/Y (Z%) | X | ✅/❌ |
| Features | CRITICAL | X/Y (Z%) | X | ✅/❌ |
| Computational | HIGH | X/Y (Z%) | X | ✅/❌ |

**Total Score**: A/B (C%)

**Critical Failures**: {count} categories failed

---

## Final Verdict

### Decision: ✅ APPROVE / ❌ REJECT

**Rationale**: {clear explanation based on comparison table}

**Rule Applied**:
- [ ] One fail = all fail (CRITICAL parameter failure)
- [ ] Score threshold (below 80%)
- [ ] All checks passed

**Action Required**:
- If ✅ APPROVE: Proceed to Phase 5A (Quick Training)
- If ❌ REJECT: {Specific rework requirements}

---

## Detailed Findings

### Strengths
1. {Strength 1}
2. {Strength 2}

### Issues (if any)
1. {Issue 1} - [severity: CRITICAL/HIGH/MEDIUM/LOW]
2. {Issue 2} - [severity: CRITICAL/HIGH/MEDIUM/LOW]

### Recommendations
{Specific recommendations for improvement}

---

## Deviations Summary (Legacy Format - Still Included)

| Check | Verdict | Severity |
|-------|---------|----------|
| Algorithm | ✅/❌ | HIGH/MED/LOW |
| Iterations | ✅/❌ | HIGH/MED/LOW |
| Features | ✅/❌ | HIGH/MED/LOW |

---

**Report Generated**: {timestamp}
**Agent**: @time_validator
**Version**: v2.5.7 Design Expectations Protocol
```

---
