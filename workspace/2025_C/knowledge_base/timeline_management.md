# Timeline Management (v3.3.0 - STRICT TIME ENFORCEMENT)

> **Source**: Extracted from CLAUDE.md v3.3.0
> **Purpose**: Timeline tracking, escalation, and 8-HOUR MINIMUM enforcement

## 8-HOUR MINIMUM WORKFLOW REQUIREMENT

> [!CRITICAL] **Total workflow duration MUST reach 480 minutes (8 hours) minimum.**
> **Phase 5 (Model Training) MINIMUM: 180 minutes (3 hours)**

### Time Allocation Breakdown

| Category | Phases | MINIMUM Time |
|----------|--------|--------------|
| Problem Understanding | 0, 0.2, 0.5 | 80 min |
| Model Design & Validation | 1, 1.5, 2 | 165 min |
| Implementation | 3, 4, 4.5 | 160 min |
| **Model Training** | **5, 5.5, 5.8** | **215 min (3.5+ hours)** |
| Visualization | 6, 6.5 | 45 min |
| Paper Writing | 7A-7F, 7.5 | 195 min |
| Final Polish | 8, 9, 9.1, 9.5, 10, 11 | 175 min |
| **TOTAL MINIMUM** | **All phases** | **~1035 min (~17 hours)** |

**Note**: Individual phase minimums sum to ~17 hours. The 8-hour floor is an absolute minimum - actual work should far exceed this.

---

## Timeline Tracking

**Track Progress**: A simple timeline dashboard (table of phases vs. allocated/spent/remaining hours, status, and risk) is recommended for monitoring progress.

**Cumulative Time Tracking** (MANDATORY):
```markdown
| Phase | MINIMUM | Actual | Cumulative | % of 8-Hour Min |
|-------|---------|--------|------------|-----------------|
| 0 | 35m | ???m | ???m | ???% |
| 0.2 | 20m | ???m | ???m | ???% |
| ... | ... | ... | ... | ... |
| TOTAL | 480m | ???m | ???m | ???% |
```

**Use it to**:
- Track cumulative time toward 8-hour minimum
- Detect phases that are underspent
- Decide when to FORCE RERUN on underspent phases
- Ensure Phase 5 reaches 3-hour minimum

---

## Escalation Triggers (STRICT)

| Condition | Severity | Action |
|-----------|----------|--------|
| **Any phase duration < MINIMUM** | ❌ CRITICAL | **REJECT + FORCE RERUN** (do NOT stop workflow) |
| **Phase 5 < 180 minutes** | ❌ CRITICAL | **REJECT + FORCE RERUN** (3-hour minimum required) |
| **Cumulative < 480 minutes at Phase 11** | ❌ CRITICAL | **CANNOT complete workflow** - add time to deficient phases |
| Buffer drops below 5% (<3.6 hours) | ⚠️ WARNING | Activate emergency protocols |
| Any phase exceeds allocated time by >50% | ✅ OK | No penalty - quality over speed |

**NO UPPER LIMITS** - Agents should take as much time as needed for quality work.

---

## 72-Hour Competition Budget

**Total**: 72 hours
**8-Hour Minimum Workflow**: ENFORCED (first 8 hours are protected for quality work)
**Critical Path**: Phase 5 (training) - MINIMUM 3 hours, typically 8-12 hours per model

### Enforcement Rule

```
IF actual_duration < minimum_time:
    REJECT phase
    DO NOT STOP workflow
    FORCE agent to RERUN phase
    Agent MUST spend at least minimum_time
    Loop until duration >= minimum_time
ENDIF
```

---

## Phase 5 Time Enforcement

> [!CRITICAL] **Phase 5 MINIMUM: 180 minutes (3 hours)**

Phase 5 (Model Training) is the most critical phase for quality:
- **MINIMUM**: 180 minutes (3 hours) - hard floor
- **NO UPPER LIMIT** - training takes as long as needed
- Duration < 180 minutes = **INSUFFICIENT TIME = ACADEMIC FRAUD**
- Rushing training produces fabricated or incomplete results

---

*Reference: CLAUDE.md v3.3.0 - Main operational documentation*
