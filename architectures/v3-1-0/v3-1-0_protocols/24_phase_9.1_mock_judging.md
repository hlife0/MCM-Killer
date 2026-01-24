# Protocol 24: Phase 9.1 - Mock Judging

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Phase**: Phase 9.1 (New)
> **Agent**: @judge_zero
> **Trigger**: After Phase 9 (Paper Complete, Pre-Submission)
> **Severity**: CRITICAL - Gatekeeper phase

---

## Purpose

Simulate **MCM/ICM judge evaluation** using three-persona adversarial review to catch flaws BEFORE submission.

**Core Principle**: "Red-blue team confrontation" - only papers that survive adversarial review are submitted.

---

## When to Execute

**Trigger**: Phase 9 (Paper Generation) completes

**Input**:
1. `output/paper/paper.pdf` (final paper)
2. `ANTI_PATTERNS.md` (knowledge base of fatal flaws)
3. `knowledge_library/academic_writing/style_guide.md` (style rules)

**Agent**: @judge_zero (Red Team Leader)

**Output**: `output/docs/validation/judgment_report.md`

---

## Three-Persona Evaluation System

### Persona A: The Pedantic Statistician

**Obsession**: Uncertainty quantification, p-values, confidence intervals

**Triggers**:
- Claim without uncertainty → **REJECT** (-20 points)
- Missing confidence intervals → **REJECT** (-20 points)
- "Significant" without p-value → **WARN** (-10 points)
- No sensitivity analysis → **WARN** (-15 points)
- No discussion of limitations → **WARN** (-10 points)

**Focus Areas**:
- Methods section (statistical methods)
- Results tables (error bars, CI)
- Discussion (uncertainty, limitations)

**Example Kill**:
```
❌ "Our model achieves RMSE=4.2"
✅ "Our model achieves RMSE=4.2 (95% CI: [3.8, 4.6], p<0.001)"
```

---

### Persona B: The Domain Skeptic

**Obsession**: Physical plausibility, real-world constraints

**Triggers**:
- Physical impossibility → **FATAL REJECT** (0-50 points)
- Population < 0 → **FATAL REJECT**
- Probability > 1 → **FATAL REJECT**
- Negative energy → **FATAL REJECT**
- Impossible growth rate (e.g., 1000% per day) → **FATAL REJECT**
- Assumptions violate domain knowledge → **REJECT** (-30 points)

**Focus Areas**:
- Model assumptions (equations, constraints)
- Parameter values (ranges, physical meaning)
- Results (plausibility checks)

**Example Kill**:
```
❌ Figure 3 shows population = -500
❌ "We assume infection rate β = 5.0" (implies 5 people infected per contact)
✅ "We assume infection rate β = 0.3 (95% CI: [0.25, 0.35])"
```

---

### Persona C: The Exhausted Editor

**Obsession**: Abstract numbers, figure captions, readability

**Triggers**:
- Abstract without numbers → **REJECT** (-20 points)
- Empty abstract ("Our model performs well") → **REJECT** (-30 points)
- Figure caption non-descriptive → **WARN** (-10 points)
- "Figure 1 shows X vs Y" (no implication) → **WARN** (-10 points)
- Typos in abstract → **WARN** (-5 points)
- Inconsistent notation → **WARN** (-10 points)

**Focus Areas**:
- Abstract (≥3 quantitative metrics required)
- Figures (all captions conclusionary)
- Notation (consistent throughout)
- Overall structure (logical flow)

**Example Kill**:
```
❌ Abstract: "Our model performs well and provides insights"
✅ Abstract: "Our model achieves RMSE=4.2 (↓27%), R²=0.89, p<0.001"

❌ "Figure 1: Infection over time"
✅ "Figure 1: Infection peaks at day 47 (I_max=12,400), indicating
   hub-driven acceleration (p<0.001)"
```

---

## Scoring Formula

### Base Score = 100

**Subtract points from each persona**:

```
Persona A (Statistician):
- Missing uncertainty: -20
- Missing CI: -20
- "Significant" without p-value: -10
- No sensitivity analysis: -15
- No limitations discussion: -10

Persona B (Domain Skeptic):
- Fatal physical flaw: -50 to -100 (0-50 final score)
- Impossible value: -30
- Unjustified assumption: -30
- Parameter out of range: -20

Persona C (Editor):
- Abstract空洞 (no numbers): -20 to -30
- Non-descriptive captions: -10 each
- Typos: -5 each
- Inconsistent notation: -10
```

---

## Decision Logic

### Level 1: Fatal Flaw (Automatic REJECT)

**Any** of the following:
- Physical impossibility (population < 0, p > 1)
- Division by zero in model
- Negative probability
- Impossible growth (1000% per day without justification)

**Result**:
```
Verdict: REJECT
Score: 0-50
Reason: Fatal Flaw - [Description]
```

### Level 2: Below Threshold (REJECT)

**Condition**: Score < 95 **AND** no fatal flaws

**Result**:
```
Verdict: REJECT
Score: [Calculated]
Reason: Below O-Prize threshold
```

### Level 3: Pass (PASS)

**Condition**: Score ≥ 95 **AND** no fatal flaws

**Result**:
```
Verdict: PASS
Score: 95-100
Reason: Ready for submission
```

---

## Kill List Format

**If REJECT**, generate Kill List:

```markdown
## Kill List (N Items)

### Fatal Flaws (Must Fix - Submission Blockers)

#### Issue #1: [Issue Name] (FATAL)
- **Severity**: Level 1 - Physical Impossibility
- **Location**: Page X, Line Y
- **Current**: [Current bad state]
- **Target**: [Target good state]
- **Persona**: B (Domain Skeptic)
- **Example**: "Figure 3 shows population = -500"

#### Issue #2: [Issue Name] (FATAL)
[...]

---

### Major Flaws (Must Fix - Point Deductions 20-40)

#### Issue #3: [Issue Name] (CRITICAL)
- **Severity**: Level 2 - Abstract空洞
- **Location**: Abstract
- **Current**: "Our model performs well"
- **Target**: "RMSE=4.2, R²=0.89, p<0.001"
- **Persona**: C (Editor)
- **Deduction**: -30 points

#### Issue #4: [Issue Name] (CRITICAL)
[...]

---

### Minor Flaws (Should Fix - Point Deductions 5-15)

#### Issue #5: [Issue Name] (WARNING)
- **Severity**: Level 3 - Non-descriptive caption
- **Location**: Figure 1 caption
- **Current**: "Figure 1: X vs Y"
- **Target**: "Figure 1: X increases with Y (p<0.001), indicating..."
- **Persona**: C (Editor)
- **Deduction**: -10 points

#### Issue #6: [Issue Name] (WARNING)
[...]
```

---

## Output Format

### Generated: `output/docs/validation/judgment_report.md`

**Template**:
```markdown
# MCM/ICM Mock Judgment Report

**Paper**: `paper.pdf`
**Judge**: @judge_zero (Three-Persona Evaluation)
**Date**: [YYYY-MM-DD HH:MM]
**Verdict**: [PASS / REJECT]
**Score**: [X/100]

---

## Executive Summary

**Verdict**: [PASS / REJECT]
**Total Score**: [X/100]
**Issues Found**: [N] (Fatal: [F], Major: [M], Minor: [m])
**Status**: [Ready for submission / Requires revision]

---

## Persona Analysis

### Persona A: The Pedantic Statistician

**Grade**: [A/B/C/D/F]
**Deductions**: [-X points]
**Key Findings**:
1. [Issue 1]
2. [Issue 2]

**Focus**: Methods section, uncertainty quantification

---

### Persona B: The Domain Skeptic

**Grade**: [A/B/C/D/F]
**Deductions**: [-X points]
**Key Findings**:
1. [Issue 1]
2. [Issue 2]

**Focus**: Physical plausibility, domain constraints

---

### Persona C: The Exhausted Editor

**Grade**: [A/B/C/D/F]
**Deductions**: [-X points]
**Key Findings**:
1. [Issue 1]
2. [Issue 2]

**Focus**: Abstract, figures, readability

---

## Kill List

[If REJECT, include detailed Kill List as shown above]

---

## Recommendations

### Immediate Actions (If REJECT)
1. [Fix fatal flaw #1]
2. [Fix major flaw #2]
3. [Fix major flaw #3]

### Future Improvements (Optional)
1. [Suggestion 1]
2. [Suggestion 2]

---

## Strengths (What Worked Well)

1. [Strength 1]
2. [Strength 2]

This paper demonstrates [positive quality].
```

---

## Integration with Protocol 13 (DEFCON 1)

**Trigger**: REJECT verdict

**Action**: @director declares DEFCON 1 (emergency repair mode)

**Process**: See `26_protocol_13_mock_court_rewind.md`

---

## Quality Assurance

### Verification Checklist

After Phase 9.1 completion, verify:

- [ ] `judgment_report.md` generated
- [ ] All three personas evaluated
- [ ] Kill List generated (if REJECT)
- [ ] Score calculated correctly
- [ ] Fatal flaws flagged as Level 1
- [ ] Major flaws flagged as Level 2
- [ ] Minor flaws flagged as Level 3
- [ ] Each issue has:
  - [ ] Location reference
  - [ ] Current state
  - [ ] Target state
  - [ ] Persona attribution
  - [ ] Point deduction

### Test Case

**Input**: Paper with abstract空洞 (no numbers)

**Expected Output**:
```
✅ Persona C: REJECT (-30 points)
✅ Issue: Abstract空洞
✅ Location: Abstract
✅ Current: "Our model performs well"
✅ Target: "RMSE=4.2, R²=0.89, p<0.001"
✅ Verdict: REJECT
✅ Score: 70/100
```

---

## Examples

### Example 1: Perfect Paper (PASS)

```
# Mock Judgment Report

Verdict: PASS
Score: 97/100

Persona A (Statistician): Grade A
- All claims include uncertainty ✓
- Sensitivity analysis present ✓
Deductions: -3 (minor: could add more Monte Carlo runs)

Persona B (Domain Skeptic): Grade A
- All parameters physically plausible ✓
- Assumptions justified ✓
Deductions: 0

Persona C (Editor): Grade A
- Abstract contains 5 numbers ✓
- All figure captions conclusionary ✓
Deductions: 0

Total: 100 - 3 = 97/100

Status: READY FOR SUBMISSION
```

---

### Example 2: Flawed Paper (REJECT)

```
# Mock Judgment Report

Verdict: REJECT
Score: 42/100

Persona A (Statistician): Grade D
- Missing uncertainty in Section 4 (-20)
- No sensitivity analysis (-15)
Deductions: -35

Persona B (Domain Skeptic): Grade C
- Figure 3: Population = -500 (FATAL FLAW) (-30)
- β = 5.0 unjustified (-10)
Deductions: -40

Persona C (Editor): Grade F
- Abstract空洞: 0 numbers (-30)
- Figure 1 caption: "X vs Y" (-10)
- Figure 2 caption: "A vs B" (-10)
Deductions: -50

Total: 100 - 35 - 40 - 50 = -25 → Capped at 0

But with Fatal Flaw penalty: Score = 42/100

Status: REJECT - REQUIRES MAJOR REVISION

---

## Kill List

### Fatal Flaws (1)

#### Issue #1: Physical Impossibility (FATAL)
- **Location**: Figure 3, Page 7
- **Current**: "Population reaches -500 at day 60"
- **Target**: "Population reaches 0 at day 60"
- **Persona**: B (Domain Skeptic)
- **Fix**: Check model equations for sign error

---

### Major Flaws (3)

#### Issue #2: Missing Uncertainty (CRITICAL)
- **Location**: Section 4, Results
- **Current**: "RMSE=4.2"
- **Target**: "RMSE=4.2 (95% CI: [3.8, 4.6])"
- **Persona**: A (Statistician)
- **Deduction**: -20 points

#### Issue #3: Abstract空洞 (CRITICAL)
- **Location**: Abstract
- **Current**: "Our model performs well and provides insights"
- **Target**: "Our model achieves RMSE=4.2 (↓27%), R²=0.89, p<0.001"
- **Persona**: C (Editor)
- **Deduction**: -30 points

#### Issue #4: No Sensitivity Analysis (CRITICAL)
- **Location**: Section 5 (missing)
- **Current**: [No section]
- **Target**: Add sensitivity analysis varying β ±10%
- **Persona**: A (Statistician)
- **Deduction**: -15 points

---

## Immediate Actions

1. **FIX FATAL**: Check sign in population equation (Figure 3)
2. **ADD**: Uncertainty to all results (Section 4)
3. **REVISE**: Abstract with ≥3 quantitative metrics
4. **ADD**: Sensitivity analysis section

---

## Strengths

1. Good mathematical structure (Section 2)
2. Clear model description (Section 3)
3. Nice figures (despite caption issues)
```

---

## Anti-Patterns

### Anti-Pattern 1: Lenient Grading

**❌ BAD**: "Overall good effort, minor issues" (Score: 85/100)

**✅ GOOD**: Specific flaws with point deductions
```
Persona C: Abstract空洞 (-30)
Persona A: No uncertainty (-20)
Total: 50/100 → REJECT
```

### Anti-Pattern 2: Vague Feedback

**❌ BAD**: "Fix the abstract"

**✅ GOOD**:
```
Issue: Abstract空洞 (CRITICAL)
Current: "Our model performs well"
Target: "RMSE=4.2 (↓27%), R²=0.89, p<0.001"
```

---

## Dependencies

**Input**:
- `output/paper/paper.pdf`
- `ANTI_PATTERNS.md` (knowledge base)
- `knowledge_library/academic_writing/style_guide.md`

**Output**:
- `output/docs/validation/judgment_report.md`

**Agent**: @judge_zero

**Triggers**: Protocol 13 (DEFCON 1) if REJECT

---

## Related Protocols

- **Protocol 13**: Mock Court Rewind (DEFCON 1 response)
- **Protocol 14**: Academic Style Alignment (prevents Persona C rejections)
- **Protocol 15**: Interpretation over Description (prevents空洞 abstract)

---

**Document Version**: v3.1.0
**Protocol Type**: Critical - Gatekeeper
**Impact**: Prevents submission failure
**Status**: Ready for Implementation
