# Time Enforcement Gap Analysis

**Date**: 2026-02-01
**Issue**: Agents not following minimum time requirements despite emphasis in CLAUDE.md
**Status**: ✅ FIXED (2026-02-01)

---

## Fix Applied

The following changes were made to resolve the gap:

1. **`workspace/2025_C/tools/time_tracker.py`**:
   - Updated all `min_min` values to match CLAUDE.md
   - Set `threshold_pct` to 1.0 (no reduction)
   - Changed enforcement logic to use min_min directly as the hard floor
   - Added Phase 0.1 which was previously missing

2. **`workspace/2025_C/agent_knowledge/shared/timing_protocol.md`**:
   - Updated to v3.3.0
   - Replaced threshold-based table with HARD MINIMUM table
   - Added explicit language that MINIMUM is the hard floor with no exceptions

---

## Executive Summary

The system has two conflicting timing systems:
1. **Documentation (CLAUDE.md, time_validator.md)** states strict MINIMUM times
2. **Enforcement code (time_tracker.py)** uses different base values + threshold percentages

Result: A phase can complete in **half the documented minimum** and still be APPROVED.

---

## Root Cause: The Code Doesn't Match the Documentation

### What CLAUDE.md Says (Lines 219-234)

```markdown
| Phase | MIN | Phase | MIN | Phase | MIN |
|-------|-----|-------|-----|-------|-----|
| 0 | **35m** | 4.5 | 10m | 7D | 25m |
| 0.1 | 15m | 5 | **180m (3h)** | 7E | **32m** |
| 0.2 | **20m** | 5.5 | 10m | 7F | 15m |
| 0.5 | **25m** | 5.8 | **25m** | 7.5 | 10m |
| 1 | **120m (2h)** | 6 | **35m** | 8 | **35m** |
```

### What time_tracker.py Actually Enforces (Lines 26-52)

```python
PHASE_TIME_REQUIREMENTS = {
    "0":   {"name": "Problem Understanding",   "min_min": 20,  "max_min": 30,   "threshold_pct": 0.70},
    "0.2": {"name": "Knowledge Retrieval",     "min_min": 7,   "max_min": 15,   "threshold_pct": 0.70},
    "0.5": {"name": "Methodology Gate",        "min_min": 10,  "max_min": 20,   "threshold_pct": 0.70},
    "1":   {"name": "Model Design",            "min_min": 90,  "max_min": 360,  "threshold_pct": 0.70},
    "2":   {"name": "Feasibility Check",       "min_min": 20,  "max_min": 30,   "threshold_pct": 0.70},
    "3":   {"name": "Data Processing",         "min_min": 40,  "max_min": 120,  "threshold_pct": 0.70},
    "4":   {"name": "Code Translation",        "min_min": 40,  "max_min": 120,  "threshold_pct": 0.70},
    "5":   {"name": "Model Training",          "min_min": 360, "max_min": 2880, "threshold_pct": 0.30},
    # ... etc
}
```

### The Actual Threshold Calculation (Lines 126-127)

```python
min_threshold = data['expected_min'] * data['threshold_pct']
data['min_threshold'] = min_threshold
```

### Enforcement Logic (Lines 192-195)

```python
if duration < min_threshold:
    result['verdict'] = "REJECT_INSUFFICIENT_TIME"
    result['action'] = "RERUN_REQUIRED"
```

---

## Full Discrepancy Table

| Phase | CLAUDE.md MIN | time_tracker.py min_min | threshold_pct | **Actual Threshold** | **Gap** |
|-------|---------------|-------------------------|---------------|----------------------|---------|
| 0 | 35m | 20 | 70% | **14m** | 21m lower |
| 0.1 | 15m | (not defined) | - | - | No enforcement |
| 0.2 | 20m | 7 | 70% | **4.9m** | 15.1m lower |
| 0.5 | 25m | 10 | 70% | **7m** | 18m lower |
| 1 | 120m | 90 | 70% | **63m** | 57m lower |
| 2 | 35m | 20 | 70% | **14m** | 21m lower |
| 3 | 75m | 40 | 70% | **28m** | 47m lower |
| 4 | 75m | 40 | 70% | **28m** | 47m lower |
| 5 | **180m** | 360 | 30% | **108m** | **72m lower** |
| 5.8 | 25m | 10 | 70% | **7m** | 18m lower |
| 6 | 35m | 20 | 70% | **14m** | 21m lower |
| 7A | 25m | 10 | 70% | **7m** | 18m lower |
| 7B | 60m | 30 | 70% | **21m** | 39m lower |
| 7C | 45m | 15 | 70% | **10.5m** | 34.5m lower |
| 7D | 25m | 10 | 70% | **7m** | 18m lower |
| 7E | 32m | 10 | 70% | **7m** | 25m lower |
| 8 | 35m | 20 | 70% | **14m** | 21m lower |
| 9 | 35m | 20 | 70% | **14m** | 21m lower |
| 9.1 | 20m | 10 | 70% | **7m** | 13m lower |
| 10 | 35m | 20 | 70% | **14m** | 21m lower |

---

## Example: Phase 5 Scenario

**Documentation says:**
> Phase 5 MINIMUM: 180 minutes (3 hours)
> "Insufficient time = ACADEMIC FRAUD"

**What actually happens:**
1. Agent completes Phase 5 in 110 minutes
2. time_tracker.py calculates: 360 × 0.30 = 108 minutes threshold
3. 110 > 108, so verdict = "APPROVE"
4. Phase 5 passes despite being 70 minutes below documented minimum

---

## Secondary Issues

### 1. Most Agents Don't Know About Minimums

| Agent | Has MIN in prompt? |
|-------|-------------------|
| reader.md | YES (lines 33-49) |
| time_validator.md | YES (lines 129-144) |
| model_trainer.md | YES (lines 36-44) |
| modeler.md | **NO** |
| writer.md | **NO** (has estimates, not minimums) |
| code_translator.md | **NO** |
| data_engineer.md | **NO** |
| visualizer.md | **NO** |
| summarizer.md | **NO** |
| validator.md | **NO** |
| researcher.md | **NO** |
| editor.md | **NO** |
| feasibility_checker.md | **NO** |
| advisor.md | **NO** |

### 2. Conflicting Documentation Versions

- `timing_protocol.md` (v3.2.0): Uses threshold-based system
- `phase_completion_protocol.md` (v3.3.0): Says "NO THRESHOLD BUFFER"
- Python code: Still uses thresholds

Evidence from `phase_completion_protocol.md` line 107:
```markdown
**MINIMUM IS the hard floor** - NO threshold buffer (-30% concept REMOVED)
```

But `time_tracker.py` still implements threshold buffers.

### 3. Phase 0.1 "Empty Inbox" Exception

From `time_validator.md` line 946:
```markdown
4. **If inbox is empty**: Phase 0.1 may complete in < 10 min (ACCEPTABLE)
```

### 4. Single Point of Enforcement Failure

From `time_validator.md` lines 122-128:
```markdown
> [!CRITICAL]
> **IDENTIFIED FAILURE**: In previous runs, Director proceeded to next phase
> WITHOUT calling @time_validator. Phases completed in 2-10 minutes when
> MINIMUM was 25-120 minutes. This is ACADEMIC FRAUD.
```

---

## Files That Need Fixing

| File | Problem | Fix |
|------|---------|-----|
| `workspace/2025_C/tools/time_tracker.py` | min_min values don't match CLAUDE.md | Update min_min to match documented MINIMUMs |
| `workspace/2025_C/tools/time_tracker.py` | threshold_pct reduces minimums | Remove threshold_pct, use min_min directly |
| `workspace/2025_C/agent_knowledge/shared/timing_protocol.md` | v3.2.0, uses old threshold system | Update to v3.3.0, remove threshold references |
| Most `.claude/agents/*.md` files | No minimum time requirements | Add MINIMUM table to each agent |

---

## Recommended Fixes

### Fix 1: Update time_tracker.py min_min Values

Change from:
```python
"0":   {"name": "Problem Understanding",   "min_min": 20,  ...
"1":   {"name": "Model Design",            "min_min": 90,  ...
"5":   {"name": "Model Training",          "min_min": 360, ...
```

To match CLAUDE.md:
```python
"0":   {"name": "Problem Understanding",   "min_min": 35,  ...
"1":   {"name": "Model Design",            "min_min": 120, ...
"5":   {"name": "Model Training",          "min_min": 180, ...
```

### Fix 2: Remove Threshold Percentage

Change enforcement from:
```python
min_threshold = data['expected_min'] * data['threshold_pct']
```

To:
```python
min_threshold = data['expected_min']  # No threshold reduction
```

### Fix 3: Add Minimums to All Agent Files

Add to each agent file:
```markdown
## Your Phase Time Requirements

| Your Phase(s) | MINIMUM Time |
|---------------|--------------|
| Phase X | XX minutes |

**You MUST NOT complete before reaching MINIMUM time.**
```

### Fix 4: Add Agent Self-Check

Agents should verify their own duration before reporting completion.

---

## Conclusion

The root cause is simple: **the Python code uses different numbers than the documentation**.

- CLAUDE.md says Phase 5 minimum is 180 minutes
- time_tracker.py calculates 360 × 0.30 = 108 minutes as threshold
- Any duration ≥ 108 minutes passes, even if it's 72 minutes below documented minimum

The documentation creates an expectation that is never enforced by the code.
