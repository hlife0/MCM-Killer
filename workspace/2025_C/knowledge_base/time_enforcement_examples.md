# Time Enforcement Examples

> **Version**: 2.0.0
> **Purpose**: Examples of correct and incorrect time enforcement behavior

---

## The Problem

In previous runs, phases completed in 2-10 minutes when MINIMUM is 25-120 minutes. This completely undermines system integrity and produces garbage output.

**Root Cause**: Director proceeded to next phase without checking duration against MINIMUM.

---

## Phase Time MINIMUM Table

| Phase | MIN | Phase | MIN | Phase | MIN |
|-------|-----|-------|-----|-------|-----|
| 0 | **35m** | 4.5 | 10m | 7D | 25m |
| 0.1 | 15m | 5 | **180m (3h)** | 7E | **32m** |
| 0.2 | **20m** | 5.5 | 10m | 7F | 15m |
| 0.5 | **25m** | 5.8 | **25m** | 7.5 | 10m |
| 1 | **120m (2h)** | 6 | **35m** | 8 | **35m** |
| 1.5 | 10m | 6.5 | 10m | 9 | **35m** |
| 2 | **35m** | 7A | **25m** | 9.1 | **20m** |
| 3 | **75m** | 7B | **60m** | 9.5 | 20m |
| 4 | **75m** | 7C | **45m** | 10 | **35m** |
| | | | | 11 | 10m |

**TOTAL MINIMUM: 520m (~8.5 hours)**

---

## Example 1: Phase 0 (Problem Understanding)

### WRONG (what was happening)

```
Phase 0 complete. Duration: 9 min.
Director: "Proceeding to Phase 0.2..."
```

**Why Wrong**: 9m < 35m MINIMUM. Director skipped time validation entirely.

### CORRECT (what must happen)

```
Phase 0 complete. Duration: 9 min.

Director: [Reads phase_0_timing.json]
Director: [Compares: 9m < 35m MINIMUM]
Director: "REJECT. Duration 9m < MINIMUM 35m. @reader: RERUN Phase 0."

@reader: [Reruns phase with deeper analysis]
Phase 0 complete. Duration: 38 min.

Director: [Reads updated timing]
Director: [Compares: 38m >= 35m MINIMUM]
Director: "@time_validator: Validate Phase 0 (38m vs 35m MIN)"

@time_validator: "APPROVE. Duration 38m >= 35m. Work quality verified."

Director: "Proceeding to Phase 0.2..."
```

---

## Example 2: Phase 1 (Model Design)

### WRONG

```
Phase 1 complete. Duration: 45 min.
Director: "Model design complete. Moving to Phase 1.5..."
```

**Why Wrong**: 45m < 120m (2h) MINIMUM. Rushed design leads to weak models.

### CORRECT

```
Phase 1 complete. Duration: 45 min.

Director: [Reads timing]
Director: "REJECT. Duration 45m < MINIMUM 120m (2h)."
Director: "@modeler: Phase 1 rejected. Duration 45m insufficient."
Director: "Required: Deeper model exploration, alternative formulations, edge case analysis."
Director: "RERUN Phase 1."

@modeler: [Expands analysis, considers 3+ alternative formulations]
Phase 1 complete. Duration: 142 min.

Director: "@time_validator: Validate Phase 1 (142m vs 120m MIN)"
@time_validator: "APPROVE. Duration 142m >= 120m. Model depth verified."

Director: "Proceeding to Phase 1.5..."
```

---

## Example 3: Phase 5 (Training)

### WRONG

```
Phase 5 complete. Duration: 25 min.
Director: "Training complete. Results look good. Proceeding to Phase 5.5..."
```

**Why Wrong**: 25m < 180m (3h) MINIMUM. Training cannot be valid in 25 minutes.

### CORRECT

```
Phase 5 started.
@model_trainer: [Coordinates 5 workers]
@model_trainer1-5: [Training in parallel/sequential as needed]

[3+ hours of actual training]

Phase 5 complete. Duration: 218 min.

Director: [Reads timing]
Director: [Compares: 218m >= 180m MINIMUM]
Director: "@time_validator: Validate Phase 5 (218m vs 180m MIN)"

@time_validator: [Checks training logs, convergence, iterations]
@time_validator: "APPROVE. Duration 218m >= 180m. Convergence achieved. Results authentic."

Director: "Proceeding to Phase 5.5..."
```

---

## Example 4: Multiple Rejections (Loop Until Pass)

```
Phase 3 complete. Duration: 12 min.
Director: "REJECT. 12m < 75m MIN. @data_engineer: RERUN."

@data_engineer: [Reruns]
Phase 3 complete. Duration: 45 min.
Director: "REJECT. 45m < 75m MIN. @data_engineer: RERUN. Include all feature engineering."

@data_engineer: [Expands scope]
Phase 3 complete. Duration: 78 min.
Director: "@time_validator: Validate Phase 3 (78m vs 75m MIN)"
@time_validator: "APPROVE."

Director: "Proceeding to Phase 4..."
```

**Key Point**: Director LOOPS until duration >= MINIMUM. No exceptions.

---

## Example 5: @time_validator Rejection (Quality Check)

Even when duration >= MINIMUM, @time_validator can reject on quality grounds:

```
Phase 4 complete. Duration: 82 min.
Director: [82m >= 75m MIN, passes self-check]
Director: "@time_validator: Validate Phase 4 (82m vs 75m MIN)"

@time_validator: [Reviews model_1.py]
@time_validator: "REJECT. Duration passes but implementation is simplified."
@time_validator: "Found: Linear approximation instead of specified non-linear solver."
@time_validator: "@code_translator must implement exact specification."

Director: "@code_translator: Rejected by @time_validator. Implement exact non-linear solver."

@code_translator: [Corrects implementation]
Phase 4 complete. Duration: 95 min.

Director: "@time_validator: Re-validate Phase 4"
@time_validator: "APPROVE. Implementation matches specification."

Director: "Proceeding to Phase 4.5..."
```

---

## What To Do When Duration < MINIMUM

1. **DO NOT PROCEED** to next phase
2. **DO NOT ASK USER** what to do
3. **FORCE AGENT TO RERUN** the phase
4. **LOOP** until duration >= MINIMUM
5. **THEN** call @time_validator for final approval
6. **ONLY ON APPROVE** update orchestration_log.md and proceed

---

## Checklist for Director

Before calling ANY next agent:

```
STEP 1: Read phase timing log
   → cat output/implementation/logs/phase_{X}_timing.json
   → IF FILE DOES NOT EXIST: STOP. Phase is INVALID.

STEP 2: Extract duration from JSON
   → duration_minutes: {value}

STEP 3: Compare against MINIMUM (from table)
   → IF duration < MINIMUM: AUTO-REJECT. FORCE agent to RERUN.
   → IF duration >= MINIMUM: PROCEED to Step 4.

STEP 4: Call @time_validator (BLOCKING)
   → Wait for verdict: APPROVE / REJECT
   → IF REJECT: FORCE RERUN. Loop until APPROVE.
   → IF APPROVE: Update orchestration_log.md, THEN call next agent.
```

---

## Common Failure Patterns

| Pattern | What Happens | Why It's Wrong |
|---------|--------------|----------------|
| No time check | Director skips to next phase | Duration never validated |
| Self-approve | Director says "looks good" | No @time_validator call |
| Ignore rejection | Director proceeds after REJECT | Violates blocking gate |
| User escalation | Director asks user what to do | System must be autonomous |
| Partial rerun | Agent redoes only part | Full phase must rerun |

---

## Severity: Academic Fraud

Insufficient time = Academic fraud because:
- Results cannot be validated in rushed timeframes
- Model quality degrades with insufficient analysis
- Training accuracy is impossible without adequate iterations
- The output is effectively fabricated

**The BLOCKING TIME GATE MUST BE ENFORCED. NO EXCEPTIONS.**
