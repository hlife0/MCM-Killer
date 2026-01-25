# Template: Judgment Report

> **Purpose**: Document @judge_zero's three-persona review
> **Written By**: @judge_zero
> **Triggers**: PASS → Phase 9.5, REJECT → Protocol 13

---

## File Location

```
output/docs/reviews/judgment_report_{version}.md
```

---

## Header Template

```markdown
# Judgment Report: {Problem Title}

> **Paper Version**: {version number}
> **Final Score**: {Score}/100
> **Decision**: [PASS / CONDITIONAL PASS / REJECT]
> **Review Date**: {YYYY-MM-DD HH:MM}
> **Time Remaining**: {X hours until deadline}

---
```

---

## Score Breakdown Template

```markdown
## Score Breakdown

| Persona | Score | Weight | Weighted Score |
|---------|-------|--------|----------------|
| Statistician (A) | {A}/100 | 40% | {0.4×A} |
| Domain Skeptic (B) | {B}/100 | 40% | {0.4×B} |
| Exhausted Editor (C) | {C}/100 | 20% | {0.2×C} |
| **Total** | - | 100% | **{Final}/100** |

### Score Interpretation
- 90-100: Excellent - Minor polish only
- 70-89: Good - Addressable issues
- 50-69: Marginal - Significant revision needed
- 30-49: Weak - Major restructuring required
- 0-29: Unacceptable - Fundamental problems

---
```

---

## Persona Review Templates

### Persona A: Statistician

```markdown
## Persona A: Statistician Review

### Score: {A}/100

### Strengths
1. [Statistical strength 1]
2. [Statistical strength 2]

### Critical Issues

#### Issue A1: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: Section {X.Y}, Page {Z}
- **Problem**: [Specific description of statistical issue]
- **Required Fix**: [Concrete action to resolve]
- **Effort**: [X hours]

#### Issue A2: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: [...]
- **Problem**: [...]
- **Required Fix**: [...]
- **Effort**: [X hours]

### Methodology Checklist
| Criterion | Status | Notes |
|-----------|--------|-------|
| Assumptions stated | [✓/✗] | [Comment] |
| Uncertainty quantified | [✓/✗] | [Comment] |
| Sensitivity analysis | [✓/✗] | [Comment] |
| Validation methodology | [✓/✗] | [Comment] |
| Reproducibility | [✓/✗] | [Comment] |
| Appropriate tests | [✓/✗] | [Comment] |
| Multiple comparisons | [✓/✗] | [Comment] |
| Overfitting checked | [✓/✗] | [Comment] |

### Full Critique
[Paragraph-form detailed critique from the Statistician perspective]

---
```

### Persona B: Domain Skeptic

```markdown
## Persona B: Domain Skeptic Review

### Score: {B}/100

### Strengths
1. [Domain validity strength 1]
2. [Domain validity strength 2]

### Critical Issues

#### Issue B1: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: Section {X.Y}, Page {Z}
- **Problem**: [Specific domain validity issue]
- **Physical Concern**: [Why this violates domain knowledge]
- **Required Fix**: [Concrete action to resolve]
- **Effort**: [X hours]

#### Issue B2: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: [...]
- **Problem**: [...]
- **Physical Concern**: [...]
- **Required Fix**: [...]
- **Effort**: [X hours]

### Plausibility Checklist
| Criterion | Status | Notes |
|-----------|--------|-------|
| Physical units | [✓/✗] | [Comment] |
| Parameter magnitudes | [✓/✗] | [Comment] |
| Real data validation | [✓/✗] | [Comment] |
| Domain constraints | [✓/✗] | [Comment] |
| Prediction plausibility | [✓/✗] | [Comment] |
| Edge case handling | [✓/✗] | [Comment] |
| Literature comparison | [✓/✗] | [Comment] |
| Real-world applicability | [✓/✗] | [Comment] |

### Full Critique
[Paragraph-form detailed critique from the Domain Skeptic perspective]

---
```

### Persona C: Exhausted Editor

```markdown
## Persona C: Exhausted Editor Review

### Score: {C}/100

### Strengths
1. [Presentation strength 1]
2. [Presentation strength 2]

### Critical Issues

#### Issue C1: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: [Page/Section]
- **Problem**: [Specific readability issue]
- **Impact**: [How this affects comprehension]
- **Required Fix**: [Concrete action to resolve]
- **Effort**: [X hours]

#### Issue C2: [Issue Title] (Severity: [High/Medium/Low])
- **Location**: [...]
- **Problem**: [...]
- **Impact**: [...]
- **Required Fix**: [...]
- **Effort**: [X hours]

### First Impression Test
| Criterion | Result | Notes |
|-----------|--------|-------|
| 30-second scan | [Pass/Fail] | [Comment] |
| Key message clarity | [Clear/Unclear] | [Comment] |
| Visual appeal | [Professional/Amateur] | [Comment] |
| Abstract compelling | [Yes/No] | [Comment] |
| Would keep reading | [Yes/No] | [Comment] |

### Presentation Checklist
| Criterion | Status | Notes |
|-----------|--------|-------|
| Abstract ≥3 numbers | [✓/✗] | [Count: X] |
| Clear thesis | [✓/✗] | [Comment] |
| Conclusionary captions | [✓/✗] | [Count: X/Y figures] |
| Story arc evident | [✓/✗] | [Comment] |
| Sections connected | [✓/✗] | [Comment] |
| No orphaned elements | [✓/✗] | [Comment] |
| Appropriate length | [✓/✗] | [Page count] |
| Professional format | [✓/✗] | [Comment] |

### Full Critique
[Paragraph-form detailed critique from the Exhausted Editor perspective]

---
```

---

## Fatal Flaw Detection Template

```markdown
## Fatal Flaw Detection

### Level 1 Fatal Flaws (Auto-Reject)

| Flaw | Present? | Evidence |
|------|----------|----------|
| Narrative Vacuum | [Yes/No] | [Location or N/A] |
| Interpretation Gap | [Yes/No] | [Figures without O-I] |
| Sensitivity Blindness | [Yes/No] | [Section 5.2 status] |
| Physical Impossibility | [Yes/No] | [Specific prediction] |
| Uncertainty Blindness | [Yes/No] | [Missing CI locations] |
| Visualization Silence | [Yes/No] | [Figure count] |

### DEFCON 1 Status
- **Triggered**: [Yes/No]
- **Primary Reason**: [Fatal flaw name or "N/A"]
- **Secondary Concerns**: [List if applicable]

---
```

---

## Repair Tickets Template

```markdown
## Prioritized Repair Tickets

### Priority 1: Must Fix Before Resubmission

#### Ticket #1: [Issue Title]
- **Source Persona**: [A/B/C]
- **Issue Reference**: Issue [A/B/C][N]
- **Assigned To**: @[agent name]
- **Phase to Revisit**: Phase {X}
- **Estimated Effort**: {X} hours
- **Success Criteria**: [Measurable outcome]

#### Ticket #2: [Issue Title]
- **Source Persona**: [...]
- [...]

### Priority 2: Should Fix

#### Ticket #3: [Issue Title]
- [...]

### Priority 3: Nice to Fix

#### Ticket #4: [Issue Title]
- [...]

---
```

---

## Recommendations Template

```markdown
## Recommendations for @director

### Decision Summary
| Criterion | Value |
|-----------|-------|
| Final Score | {X}/100 |
| Decision | [PASS/CONDITIONAL PASS/REJECT] |
| Fatal Flaws | [Count] |
| Priority 1 Tickets | [Count] |

### Action Required

#### If PASS (Score ≥ 70, No Fatal Flaws)
- Proceed to Phase 9.5 (Polish)
- Address Priority 3 issues if time permits
- Estimated time: {X} hours

#### If CONDITIONAL PASS (Score 50-69, No Fatal Flaws)
- Allow {X} hours for minor fixes
- Re-review specific sections only
- Focus on Priority 1-2 tickets
- Estimated time: {X} hours

#### If REJECT (Score < 50 OR Fatal Flaws)
- Enter DEFCON 1 (Protocol 13)
- Assign all Priority 1 tickets immediately
- Set time limit: {X} hours
- Re-review full paper after fixes

### Time Budget
| Activity | Estimated Time |
|----------|---------------|
| Priority 1 Fixes | {X} hours |
| Priority 2 Fixes | {Y} hours |
| Re-review | {Z} hours |
| **Total** | {X+Y+Z} hours |

### Deadline Check
- Time Remaining: {X} hours
- Required Time: {Y} hours
- Buffer: {X-Y} hours
- Feasibility: [Feasible / Tight / Infeasible]

---
```

---

## Signature Template

```markdown
## Signature

**Reviewed By**: @judge_zero (三人格评审)
- Persona A: Statistician
- Persona B: Domain Skeptic
- Persona C: Exhausted Editor

**Paper Version**: {version}
**Review Date**: {YYYY-MM-DD}
**Next Action**: [Phase 9.5 / Protocol 13 / Conditional Review]

---

## Appendix: Full Review Notes

[Optional: Extended notes, annotated paper sections, etc.]
```

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
