# Quality Check Templates for Judge Zero

**Agent**: @judge_zero
**Purpose**: Standardized templates for page count, blank space, and content balance verification
**Last Updated**: 2026-02-01

---

## Page Count Verification Template

### Pre-Review Page Audit

```markdown
## Page Count Verification

**Paper**: {paper_path}
**Date**: {date}
**Reviewer**: @judge_zero

### Page Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total pages | {X} | 24-28 | {GREEN/YELLOW/RED} |
| Words per page (avg) | {X} | >=300 | {GREEN/YELLOW/RED} |
| Minimum words on any page | {X} | >=200 | {PASS/FAIL} |
| Pages with <200 words | {X} | 0 | {PASS/FAIL} |
| Max blank space % on any page | {X}% | <30% | {GREEN/YELLOW/RED} |

### Page Count Thresholds

| Status | Condition | Action |
|--------|-----------|--------|
| CRITICAL_UNDER | <20 pages | BLOCK, MUST expand immediately |
| RED_UNDER | 20-22 pages | Critical warning, expansion required |
| YELLOW_UNDER | 22-24 pages | Warning, recommend expansion |
| GREEN | 24-26 pages | Optimal range |
| YELLOW_OVER | 26-28 pages | Warning, review for consolidation |
| CRITICAL_OVER | >28 pages | BLOCK, MUST consolidate |

### Current Status: {STATUS}

**Action Required**: {action_description}
```

---

## Blank Space Audit Template

### Visual Density Assessment

```markdown
## Blank Space Audit

**Paper**: {paper_path}
**Date**: {date}
**Reviewer**: @judge_zero

### Per-Page Analysis

| Page | Words | Figures | Tables | Blank % | Status |
|------|-------|---------|--------|---------|--------|
| 1 | {X} | {Y} | {Z} | {W}% | {GREEN/YELLOW/RED} |
| 2 | {X} | {Y} | {Z} | {W}% | {GREEN/YELLOW/RED} |
| ... | ... | ... | ... | ... | ... |

### Blank Space Thresholds

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Words/page (avg) | >=300 | 250-300 | <250 |
| Max blank % on any page | <30% | 30-50% | >50% |
| Pages with <200 words | 0 | 1-2 | >=3 |

### Problem Pages Identified

| Page | Issue | Severity | Fix Recommendation |
|------|-------|----------|-------------------|
| {X} | {description} | {HIGH/MED/LOW} | {fix} |

### Summary

- Total problem pages: {X}
- Critical issues (>50% blank): {Y}
- Warning issues (30-50% blank): {Z}
- Action: {PASS / REVISE / BLOCK}
```

---

## Content Balance Assessment Template

### Section Proportion Analysis

```markdown
## Content Balance Assessment

**Paper**: {paper_path}
**Date**: {date}
**Reviewer**: @judge_zero

### Section Proportions (O-Prize Aligned)

| Section | Target % | Actual % | Deviation | Status |
|---------|----------|----------|-----------|--------|
| Framework (Abstract, Intro) | 10% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |
| Models | 44% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |
| Evidence (Data, Results) | 24% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |
| Analysis (Sensitivity, S/W) | 10% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |
| Synthesis (Discussion, Conclusions) | 10% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |
| Support (References, Appendix) | 6% | {X}% | {±Y}% | {BALANCED/MINOR/SIGNIFICANT/CRITICAL} |

### Deviation Severity Scale

| Deviation | Status | Action |
|-----------|--------|--------|
| <5% | BALANCED | No action needed |
| 5-10% | MINOR | Minor adjustment recommended |
| 10-15% | SIGNIFICANT | Rebalancing required |
| >15% | CRITICAL | Major restructuring needed |

### Imbalance Issues

| Issue | Current | Target | Gap | Priority |
|-------|---------|--------|-----|----------|
| {section} under-represented | {X}% | {Y}% | -{Z}% | {HIGH/MED/LOW} |
| {section} over-represented | {X}% | {Y}% | +{Z}% | {HIGH/MED/LOW} |

### Balance Correction Recommendations

1. **{Issue 1}**: {Specific correction action}
2. **{Issue 2}**: {Specific correction action}

### Overall Balance Verdict: {BALANCED / MINOR_ISSUES / NEEDS_REBALANCING / CRITICAL_IMBALANCE}
```

---

## Combined Quality Dashboard

### Quick Reference Dashboard

```markdown
## Quality Dashboard Summary

**Paper**: {paper_path}
**Date**: {date}

### Critical Metrics

| Category | Status | Details |
|----------|--------|---------|
| Page Count | {status} | {X} pages (target: 24-28) |
| Blank Space | {status} | Max {X}% blank (threshold: <30%) |
| Content Balance | {status} | {X} sections with >5% deviation |
| Words/Page | {status} | Avg {X} words (threshold: >=300) |

### DEFCON Status

- [ ] Trigger 7: Under-Length Paper (<24 pages)
- [ ] Trigger 8: Excessive Blank Space (>50% on any page)
- [ ] Trigger 9: Content Imbalance (>15% deviation)
- [ ] Trigger 10: Sparse Page (<200 words, no figure)

**DEFCON 1 Triggered**: {YES/NO}
**Trigger(s)**: {list if any}

### Recommended Actions

| Priority | Issue | Agent | Phase |
|----------|-------|-------|-------|
| P1 | {issue} | @{agent} | Phase {X} |
| P2 | {issue} | @{agent} | Phase {X} |
```

---

## Usage Notes

1. **When to use**: Apply these templates during Phase 9.1 Mock Judging
2. **Integration**: Results feed into judgment_report.md
3. **Automation**: Templates can be partially filled by LaTeX analysis tools
4. **Thresholds**: Based on O-Prize paper analysis (40+ papers)

---

**END OF QUALITY CHECK TEMPLATES**
