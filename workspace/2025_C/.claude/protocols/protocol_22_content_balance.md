# Protocol 22: Content Balance Verification

> **Purpose**: Ensure proportional section distribution aligned with O-Prize standards
> **Owners**: @judge_zero, @writer, @editor
> **Scope**: Phase 7.5, Phase 9.1

---

## Target Proportions (O-Prize Aligned)

Based on analysis of 40+ O-Prize winning papers:

| Section | Target % | Acceptable Range | Notes |
|---------|----------|------------------|-------|
| Framework (Abstract, Intro) | 10% | 8-12% | Problem setup and motivation |
| Models | 44% | 38-50% | **Largest section** - mathematical core |
| Evidence (Data, Results) | 24% | 20-30% | Data + all results presentation |
| Analysis (Sensitivity, S/W) | 10% | 8-14% | Robustness and limitations |
| Synthesis (Discussion, Conclusions) | 10% | 8-14% | Interpretation and implications |
| Support (References, Appendix) | 6% | 4-10% | Supplementary materials |

**Key Insight**: O-Prize papers allocate 44% to model development (NOT introduction or results). Model section should be detailed with full mathematics.

---

## Verification Process

### Step 1: Section Measurement

After Phase 7F compilation:

1. Count pages per section from compiled PDF
2. Calculate proportion: `section_pages / total_pages * 100`
3. Record in balance verification table

### Step 2: Deviation Classification

| Deviation | Status | Action Required |
|-----------|--------|-----------------|
| <5% | BALANCED | No action |
| 5-10% | MINOR | Recommend adjustment |
| 10-15% | SIGNIFICANT | Require adjustment before Phase 9.1 |
| >15% | CRITICAL | BLOCK progression, must rebalance |

### Step 3: Report Generation

Generate balance report in format:

```markdown
## Content Balance Report

| Section | Target | Actual | Deviation | Status |
|---------|--------|--------|-----------|--------|
| Framework | 10% | X% | ±Y% | STATUS |
| Models | 44% | X% | ±Y% | STATUS |
| Evidence | 24% | X% | ±Y% | STATUS |
| Analysis | 10% | X% | ±Y% | STATUS |
| Synthesis | 10% | X% | ±Y% | STATUS |
| Support | 6% | X% | ±Y% | STATUS |

**Overall Balance**: {BALANCED / NEEDS_ADJUSTMENT / CRITICAL}
```

### Step 4: Correction Routing

If imbalances detected, route to appropriate agent:

| Imbalance | Agent | Phase |
|-----------|-------|-------|
| Models under-represented | @writer | 7B |
| Results over-represented | @writer + @visualizer | 7C |
| Analysis under-represented | @writer + @validator | 7D |
| Synthesis under-represented | @writer | 7E |

---

## Enforcement Actions by Severity

### BALANCED (<5% deviation all sections)
- Proceed to next phase
- No action required

### MINOR (5-10% deviation)
- Flag in judgment report
- Recommend adjustment
- Can proceed with recommendation

### SIGNIFICANT (10-15% deviation)
- Create repair ticket
- Require adjustment before Phase 9.1 completion
- Block if >2 sections have significant deviation

### CRITICAL (>15% deviation)
- Trigger DEFCON 1 content balance recovery
- BLOCK progression
- Route to Phase 7 for major rewrite
- @director must approve rebalancing plan

---

## Integration with DEFCON 1 Triggers

Protocol 22 adds new DEFCON 1 trigger:

**Trigger 9: Content Imbalance**
- **Detection**: Any section >15% deviation from target
- **Action**: @writer rebalances, @editor verifies
- **Phase to Revisit**: Depends on which section

---

## Mandatory Balance Check Points

| Phase | Check | Agent |
|-------|-------|-------|
| 7.5 | Post-compilation balance scan | @writer self-check |
| 9.1 | Full balance verification | @judge_zero |
| 9.5 | Final balance confirmation | @editor |

---

## Balance Repair Workflow

When imbalance detected:

1. **Diagnose**: Identify which sections are over/under
2. **Quantify**: Calculate exact deviation
3. **Route**: Assign to appropriate agent
4. **Execute**: Agent adjusts content
5. **Verify**: Re-run balance check
6. **Approve**: Confirm all sections within range

---

## Common Imbalance Scenarios

### Scenario A: Models Under-Represented (<38%)

**Cause**: Rushed model sections, insufficient mathematical detail
**Fix**:
- Expand mathematical derivations
- Add algorithm pseudocode
- Include parameter justifications
- Detail model assumptions

**Agent**: @writer
**Phase**: 7B

### Scenario B: Results Over-Represented (>30%)

**Cause**: Too many figures/tables, insufficient interpretation
**Fix**:
- Consolidate similar figures
- Merge related tables
- Move detailed results to appendix
- Focus on key findings only

**Agent**: @writer + @visualizer
**Phase**: 7C

### Scenario C: Analysis Under-Represented (<8%)

**Cause**: Minimal sensitivity analysis, no robustness checks
**Fix**:
- Expand sensitivity discussion
- Add parameter variation analysis
- Include strengths/weaknesses detail
- Discuss model limitations

**Agent**: @writer + @validator
**Phase**: 7D

---

## Balance Check Template

```markdown
## Protocol 21 Balance Verification

**Paper**: {paper_path}
**Phase**: {phase}
**Date**: {date}

### Section Proportions

| Section | Pages | % | Target | Deviation | Status |
|---------|-------|---|--------|-----------|--------|
| Framework | X | Y% | 10% | ±Z% | {status} |
| Models | X | Y% | 44% | ±Z% | {status} |
| Evidence | X | Y% | 24% | ±Z% | {status} |
| Analysis | X | Y% | 10% | ±Z% | {status} |
| Synthesis | X | Y% | 10% | ±Z% | {status} |
| Support | X | Y% | 6% | ±Z% | {status} |

### Overall Assessment

- **Balance Score**: {X}/100
- **Sections in Range**: {Y}/6
- **Critical Deviations**: {Z}
- **Verdict**: {PASS / ADJUST / BLOCK}

### Repair Tickets (if any)

{List of issues requiring correction}
```

---

## Version History

- **v1.0** (2026-02-01): Initial protocol for content balance verification

---

**END OF PROTOCOL 21**
