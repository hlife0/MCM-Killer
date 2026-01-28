# Timeline Management

> **Source**: Extracted from CLAUDE.md v3.1.0
> **Purpose**: Timeline tracking and escalation

## Timeline Tracking

**Track Progress**: A simple timeline dashboard (table of phases vs. allocated/spent/remaining hours, status, and risk) is recommended for monitoring progress.

**Use it to**:
- Track buffer and burn rate
- Detect phases that are overrunning
- Decide when to activate parallel work patterns or emergency protocols

## Escalation Triggers

| Condition | Severity | Action |
|-----------|----------|--------|
| Buffer drops below 5% (<3.6 hours) | ❌ CRITICAL | Activate emergency protocols |
| Any phase exceeds allocated time by >50% | ⚠️ WARNING | Investigate bottleneck |
| Critical path (Phase 5-6) delayed by >2 hours | ⚠️ WARNING | Consider Protocol 4 (parallel execution) |

## 72-Hour Competition Budget

**Total**: 72 hours
**Recommended Buffer**: 20% (~14.4 hours)
**Working Budget**: ~57.6 hours

**Critical Path**: Phase 5 (training) - typically 8-12 hours per model

---

*Reference: CLAUDE.md - Main operational documentation*
