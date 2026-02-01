# Phase Completion Protocol (v3.3.0 - STRICT TIME ENFORCEMENT)

> **Source**: CLAUDE.md v3.3.0 Phase Completion Protocol
> **Purpose**: Detailed reference for STRICT phase timing validation and completion reporting
> **CRITICAL**: 8.5-HOUR MINIMUM TOTAL WORKFLOW ENFORCED (520 minutes)

---

## FAILURE MODE ANALYSIS (V2.0)

> [!CRITICAL]
> **IDENTIFIED FAILURE**: In previous competition runs, phases completed in 2-10 minutes when MINIMUM was 25-120 minutes.
> This completely undermined system integrity and produced low-quality output.

### Evidence from Failed Run (output3_success1)

| Phase | Actual | MINIMUM | Violation |
|-------|--------|---------|-----------|
| 0 | 9.4m | 35m | **26m short** |
| 0.2 | 5.0m | 20m | **15m short** |
| 0.5 | 2.5m | 25m | **22.5m short** |
| 1 | 17.6m | 120m | **102.4m short** |
| 3 | 6.3m | 75m | **68.7m short** |
| 5 | 77.9m | 180m | **102.1m short** |
| 7A | 3.7m | 25m | **21.3m short** |
| 7B | 5.8m | 60m | **54.2m short** |
| 8 | 2.8m | 35m | **32.2m short** |

**Total workflow: 414m actual vs 520m MINIMUM (66m short)**

### Root Cause

1. **Director did not enforce SELF-CHECK** before calling next agent
2. **Director did not call @time_validator** for each phase
3. **Director proceeded immediately** despite duration < MINIMUM
4. **time_tracker.py was not used** to track actual timing

### Fix Applied (V2.0)

1. **MANDATORY Pre-Next-Phase Checklist** added to CLAUDE.md
2. **Protocol 22: Strict Time Enforcement** added as BLOCKING protocol
3. **Automatic Decision Rule 6** added for time enforcement
4. **Explicit examples** of WRONG vs CORRECT behavior added

---

## Overview

After EVERY phase completion, Director MUST validate time with @time_validator. This protocol ensures:
1. Agents spend **adequate time** on each phase (MINIMUM enforced, no threshold buffer)
2. Work is **NOT rushed** or shortcuts taken
3. Quality is maintained through **strict time accountability**
4. **8.5-hour minimum total workflow** is achieved
5. **Phase 5 (Model Training) requires 3 hours minimum**

**ENFORCEMENT RULE (ACCUMULATIVE TIME)**:
```
IF cumulative_duration < minimum_time:
    REJECT phase
    DO NOT STOP workflow
    FORCE agent to RERUN phase WITH PREVIOUS WORK REFERENCE

    RERUN COMMAND:
    python tools/time_tracker.py start --phase {X} --agent {agent} --rerun

    RERUN MESSAGE TO AGENT:
    "Your previous attempt contributed {current_attempt_duration}m.
     Cumulative time: {cumulative_duration}m. Minimum: {minimum_time}m.
     READ your previous work at: {previous_output_path}
     IMPROVE upon it, do not restart from scratch."

    Time ACCUMULATES: previous + current = cumulative
    Loop until cumulative_duration >= minimum_time
ENDIF
```

---

## BLOCKING TIME GATE Workflow (MANDATORY - ACCUMULATIVE TIME)

> [!CRITICAL] **This workflow is BLOCKING. Director CANNOT skip any step. Workflow NEVER stops on rejection - FORCE RERUN with --rerun flag instead. TIME ACCUMULATES across attempts.**

```
Agent completes phase → Reports to Director
                ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 7a: Director SELF-CHECK                                │
│ Compare CUMULATIVE duration vs MINIMUM from table           │
│ cumulative_duration >= MINIMUM?                             │
│ (Time accumulates across all rerun attempts)                │
└─────────────────────────────────────────────────────────────┘
        ↓ NO                              ↓ YES
┌───────────────────────────┐         ┌───────────────────────────────┐
│ STEP 7b: REJECT           │         │ STEP 7c: Call @time_validator │
│ Log rejection             │         │ Include cumulative_duration   │
│ DO NOT STOP WORKFLOW      │         └───────────────────────────────┘
│ FORCE RERUN with --rerun  │                     ↓
│ Include previous_output   │         ┌───────────────────────────────┐
│ LOOP until cumulative MIN │         │ STEP 7d: WAIT for verdict     │
└───────────────────────────┘         │ APPROVE / REJECT / INVESTIGATE│
                                      └───────────────────────────────┘
                                                  ↓
                    ┌─────────────────────────────┴─────────────────────┐
                    ↓ REJECT/INVESTIGATE                                ↓ APPROVE
        ┌───────────────────────────┐               ┌───────────────────────────┐
        │ STEP 7e: FORCE RERUN      │               │ STEP 7f: PROCEED          │
        │ Log rejection             │               │ → Step 8: Update log      │
        │ DO NOT STOP WORKFLOW      │               │ → Step 9: Update manifest │
        │ Agent MUST rerun phase    │               │ → Update cumulative time  │
        │ LOOP until APPROVE        │               │ → Call next agent         │
        └───────────────────────────┘               └───────────────────────────┘
```

**Key Points**:
- @time_validator is the **BLOCKING TIME GATE** - no progression without APPROVE
- Director self-check catches obvious violations immediately (cumulative_duration < MINIMUM)
- **MINIMUM IS the hard floor** - Time ACCUMULATES across all rerun attempts
- **Workflow NEVER stops on rejection** - FORCE RERUN with --rerun flag until APPROVE
- When rerunning, agent MUST reference previous work at `previous_output_path`
- Track **cumulative time** across all phases AND all attempts within a phase
- Skipping @time_validator = Academic Fraud

---

## Phase Time Requirements Table (STRICT MINIMUMS - NO UPPER LIMITS)

> [!CRITICAL] **8.5-HOUR MINIMUM TOTAL WORKFLOW (520 minutes)**
> **The MINIMUM column IS the hard floor. Duration < MINIMUM = REJECT + FORCE RERUN. NO EXCEPTIONS.**
> **Phase 5 MINIMUM: 3 hours (180 minutes)** - Model training requires substantial time.

| Phase | Name | MINIMUM TIME |
|-------|------|--------------|
| 0 | Problem Understanding | **35 min** |
| 0.1 | External Resource Processing | **15 min** |
| 0.2 | Knowledge Retrieval | **20 min** |
| 0.5 | Methodology Gate | **25 min** |
| 1 | Model Design | **120 min (2 hours)** |
| 1.5 | Time Validation | **10 min** |
| 2 | Feasibility Check | **35 min** |
| 3 | Data Processing | **75 min** |
| 4 | Code Translation | **75 min** |
| 4.5 | Fidelity Check | **10 min** |
| **5** | **Model Training** | **180 min (3 hours)** |
| 5.5 | Data Authenticity | **10 min** |
| 5.8 | Insight Extraction | **25 min** |
| 6 | Visualization | **35 min** |
| 6.5 | Visual Gate | **10 min** |
| 7A | Paper Framework | **25 min** |
| 7B | Model Sections | **60 min** |
| 7C | Results Integration | **45 min** |
| 7D | Analysis Sections | **25 min** |
| 7E | Conclusions | **32 min** |
| 7F | LaTeX Compilation | **15 min** |
| 7.5 | LaTeX Gate | **10 min** |
| 8 | Summary | **35 min** |
| 9 | Polish | **35 min** |
| 9.1 | Mock Judging (6-10 rejections) | **20 min** |
| 9.5 | Editor Feedback | **20 min** |
| 10 | Final Review | **35 min** |
| 11 | Self-Evolution | **10 min** |

**TOTAL MINIMUM: 520 min (~8.5 hours)**
**NO THRESHOLD BUFFER** - The MINIMUM is the rejection threshold. No -30% buffer.

---

## Completion Report Format

Agent completing a phase MUST report using this format:

```markdown
Director, Phase {X} COMPLETE.

## Timing
- Phase: {X} ({phase_name})
- Start: {ISO timestamp, e.g., 2026-01-30T14:30:00}
- End: {ISO timestamp, e.g., 2026-01-30T15:00:00}
- Duration: {XX} minutes
- MINIMUM Required: {min_time} minutes
- Cumulative Total: {ZZ} minutes / 520 minutes (8.5-hour minimum)

## Deliverables
- Output files: {list of files created/modified}
  - e.g., output/docs/research_notes.md
  - e.g., output/implementation/model_1.py
- Status: SUCCESS / PARTIAL / FAILED

## Self-Assessment
- Quality: HIGH / MEDIUM / LOW
- Confidence: {1-10}
- Issues encountered: {list or "None"}
```

### Example Completion Report

```markdown
Director, Phase 3 COMPLETE.

## Timing
- Phase: 3 (Data Processing)
- Start: 2026-01-30T10:00:00
- End: 2026-01-30T11:15:00
- Duration: 75 minutes
- MINIMUM Required: 75 minutes ✓
- Cumulative Total: 255 minutes / 520 minutes

## Deliverables
- Output files:
  - output/implementation/data/features_1.pkl
  - output/implementation/data/features_1.csv
  - output/implementation/data/features_2.pkl
  - output/implementation/data/features_2.csv
- Status: SUCCESS

## Self-Assessment
- Quality: HIGH
- Confidence: 9
- Issues encountered: None
```

---

## Director Time Validation Call (BLOCKING TIME GATE)

After receiving a completion report, Director calls @time_validator:

```
@time_validator: Phase Time Check (BLOCKING TIME GATE)

Phase: {X} ({phase_name})
Agent: @{agent_name}
Reported Duration: {XX} minutes
MINIMUM Required: {min_time} minutes
Cumulative Total: {ZZ} minutes / 520 minutes (8.5-hour minimum)

Check:
1. Query Python backend log at output/implementation/logs/phase_{X}_timing.json
2. Compare reported duration vs logged duration
3. Validate against MINIMUM (NO threshold buffer - MINIMUM IS the hard floor)
4. Track cumulative time toward 8.5-hour minimum

ENFORCEMENT: Duration < MINIMUM = REJECT + FORCE RERUN (workflow does NOT stop)

Return: APPROVE / REJECT_INSUFFICIENT_TIME / INVESTIGATE
```

### Validation Decision Rules (STRICT)

| Condition | Verdict | Action |
|-----------|---------|--------|
| Cumulative Duration >= MINIMUM | APPROVE | Proceed to next phase |
| **Cumulative Duration < MINIMUM** | **REJECT_INSUFFICIENT_TIME** | **FORCE RERUN with --rerun (do NOT stop)** |
| Logged != Reported (>10% diff) | INVESTIGATE | Verify timestamps, potential fraud |

**Time ACCUMULATES across attempts** - Attempt 1 (10m) + Attempt 2 (20m) = 30m cumulative.

---

## Rejection Protocol (DO NOT STOP - FORCE RERUN WITH PREVIOUS WORK REFERENCE)

When @time_validator returns `REJECT_INSUFFICIENT_TIME`:

> [!CRITICAL] **Workflow NEVER stops on rejection. FORCE agent to RERUN phase with --rerun flag. Agent MUST reference previous work.**

### Step 1: Log Rejection
Append to `output/docs/time_rejections.md`:

```markdown
## Rejection: Phase {X} - {timestamp}

- **Agent**: @{agent_name}
- **Attempt**: #{attempt_count}
- **This Attempt Duration**: {current_attempt_duration} minutes
- **Cumulative Duration**: {cumulative_duration} minutes
- **MINIMUM Required**: {YY} minutes
- **Additional Time Needed**: {MINIMUM - cumulative_duration} minutes
- **Reason**: Cumulative duration below MINIMUM
- **Action**: FORCE RERUN with --rerun flag (workflow continues)
- **Previous Output Path**: {previous_output_path}
```

### Step 2: FORCE Phase Rerun WITH PREVIOUS WORK REFERENCE

**Director command**:
```bash
python tools/time_tracker.py start --phase {X} --agent {agent_name} --rerun
```

**Message to agent**:
```
@{agent}: Phase {X} REJECTED - INSUFFICIENT CUMULATIVE TIME

Attempt #{attempt_count} completed. Duration breakdown:
- This attempt: {current_attempt_duration} min
- Previous attempts: {sum of previous} min
- Cumulative total: {cumulative_duration} min
- MINIMUM required: {minimum} min
- Additional time needed: {minimum - cumulative_duration} min

**CRITICAL: USE YOUR PREVIOUS WORK AS REFERENCE**

Your previous output is at: {previous_output_path}
1. READ your previous work first
2. IDENTIFY what can be improved, expanded, or deepened
3. Build upon your existing work, do NOT restart from scratch
4. Focus on the additional {minimum - cumulative_duration} minutes of substantive work

Time accumulates across attempts. Your goal is cumulative_duration >= {minimum}m.
```

### Step 3: Loop Until APPROVE
- **DO NOT STOP WORKFLOW** - rejection triggers rerun with --rerun flag, not halt
- Time ACCUMULATES across all attempts
- Agent MUST reference previous work at {previous_output_path}
- After 5 failed reruns, escalate to @director for investigation
- **Workflow cannot proceed** until APPROVE received

---

## Cumulative Time Tracking (8.5-HOUR MINIMUM)

> [!CRITICAL] **Even if all phases pass individually, cumulative time must reach 520 minutes (~8.5 hours).**

### Tracking Protocol
After each phase approval, update cumulative time:

```markdown
## Cumulative Time Tracker

| Phase | Duration | Cumulative | % of 8-Hour Minimum |
|-------|----------|------------|---------------------|
| 0 | 35m | 35m | 7.3% |
| 0.2 | 22m | 57m | 11.9% |
| 0.5 | 28m | 85m | 17.7% |
| 1 | 135m | 220m | 45.8% |
| ... | ... | ... | ... |
| **TOTAL** | **???m** | **???m** | **???%** |
```

### Final Workflow Gate
Before Phase 11 (Self-Evolution) completes:
```
IF cumulative_total < 520 minutes:
    REJECT workflow completion
    Identify underspent phases
    FORCE additional work on deficient phases
    Loop until cumulative_total >= 520 minutes
ENDIF
```

---

## Python Backend Integration

### Time Tracker Tool

Location: `tools/time_tracker.py`

**Agent Usage (at phase start)**:
```bash
python tools/time_tracker.py start --phase {X} --agent {agent_name}
```

**Agent Usage (at phase end)**:
```bash
python tools/time_tracker.py end --phase {X} --agent {agent_name}
```

**Validator Usage**:
```bash
python tools/time_tracker.py validate --phase {X}
```

### Log File Format

Path: `output/implementation/logs/phase_{X}_timing.json`

```json
{
  "phase": "3",
  "phase_name": "Data Processing",
  "agent": "@data_engineer",
  "start_time": "2026-01-30T10:00:00",
  "end_time": "2026-01-30T11:15:00",
  "duration_minutes": 75,
  "expected_min": 40,
  "expected_max": 120,
  "threshold_pct": 0.70,
  "min_threshold": 28,
  "status": "completed",
  "time_verdict": "ACCEPTABLE",
  "time_message": "Duration 75.0 min within acceptable range"
}
```

### Director Responsibility (MANDATORY)

> [!CRITICAL] **Director MUST manage time tracking, not just rely on agents.**

**Director workflow for EVERY phase**:
1. **BEFORE calling agent**:
   ```bash
   python tools/time_tracker.py start --phase {X} --agent {agent_name}
   ```
2. **Call agent** with instructions
3. **AFTER agent reports completion**:
   ```bash
   python tools/time_tracker.py end --phase {X} --agent {agent_name}
   ```
4. **Read timing from JSON log** (NOT manually type timestamps):
   ```bash
   cat output/implementation/logs/phase_{X}_timing.json
   ```
5. **Update orchestration_log.md** with values FROM the JSON:
   - Use `start_time` from JSON
   - Use `end_time` from JSON
   - Use `duration_minutes` from JSON
6. **Call time_validator** with the logged duration

**WHY THIS MATTERS**:
- Previously, Director was manually typing fake timestamps (e.g., `2026-01-31T08:00:00`)
- This allowed phases to "complete" in impossible times
- time_validator had NO_DATA to verify against
- This protocol ensures verifiable, auditable timing

**VIOLATION = ACADEMIC FRAUD**:
- Manually typing timestamps instead of reading from JSON
- Skipping `time_tracker.py start` before calling agent
- Skipping `time_tracker.py end` after agent completes
- Proceeding to next phase without timing log existing

---

## Special Cases

### Phase 5: Model Training (3-HOUR MINIMUM)

> [!CRITICAL] **Phase 5 requires MINIMUM 180 minutes (3 hours).**

- Phase 5 is the most time-intensive phase
- **MINIMUM: 180 minutes (3 hours)** - this is the hard floor
- **NO UPPER LIMIT** - training should take as long as needed for quality results
- Duration < 180 minutes = **AUTO-REJECT + FORCE RERUN**

### Gate Phases (Validation-Focused)

Gate phases (0.5, 1.5, 4.5, 5.5, 6.5, 7.5) have shorter minimums (10 min) because they are validation-focused, not implementation-focused. However, the MINIMUM is still enforced strictly.

### Phase 7 Sub-Phases

Each sub-phase (7A-7F) has its own MINIMUM requirement. Track separately:
- 7A: **25 min** (Abstract + Intro + Notation)
- 7B: **60 min** (Model sections - largest)
- 7C: **35 min** (Results integration)
- 7D: **25 min** (Analysis sections)
- 7E: **25 min** (Conclusions + Bibliography)
- 7F: **15 min** (LaTeX compilation)

**Total Phase 7 MINIMUM: 185 minutes**

---

## Integration with VERSION_MANIFEST.json

After successful time validation, update manifest with cumulative tracking:

```json
{
  "phase_3": {
    "status": "completed",
    "timestamp": "2026-01-30T11:15:00",
    "duration_minutes": 75,
    "minimum_required": 75,
    "time_validated": true,
    "cumulative_total": 255,
    "cumulative_percentage": 53.1
  }
}
```

---

## 8-Hour Minimum Enforcement Summary

> [!CRITICAL] **NO EXCEPTIONS TO THE 8.5-HOUR MINIMUM**

| Enforcement Point | Rule |
|-------------------|------|
| Each Phase | Duration >= MINIMUM (hard floor) |
| Rejection | DO NOT STOP workflow, FORCE RERUN |
| Cumulative | Track total toward 520 minutes |
| Final Gate | Workflow cannot complete if total < 520 minutes |
| Phase 5 | MINIMUM 180 minutes (3 hours) |

**INSUFFICIENT TIME = ACADEMIC FRAUD** - Rushing through phases produces low-quality work that contaminates downstream phases.

---

*Reference: CLAUDE.md v3.3.0 - Main operational documentation*
