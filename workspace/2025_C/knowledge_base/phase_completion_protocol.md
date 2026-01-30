# Phase Completion Protocol (v3.2.0)

> **Source**: CLAUDE.md v3.2.0 Phase Completion Protocol
> **Purpose**: Detailed reference for phase timing validation and completion reporting

---

## Overview

After EVERY phase completion, Director MUST validate time with @time_validator. This protocol ensures:
1. Agents spend adequate time on each phase
2. Work is not rushed or shortcuts taken
3. Quality is maintained through time accountability

---

## Phase Time Requirements Table

| Phase | Name | Min Time | Max Time | -30% Threshold |
|-------|------|----------|----------|----------------|
| 0 | Problem Understanding | 20 min | 30 min | 14 min |
| 0.2 | Knowledge Retrieval | 7 min | 15 min | 5 min |
| 0.5 | Methodology Gate | 10 min | 20 min | 7 min |
| 1 | Model Design | 1.5 hours | 6 hours | 63 min |
| 1.5 | Time Validation | 4 min | 10 min | 3 min |
| 2 | Feasibility Check | 20 min | 30 min | 14 min |
| 3 | Data Processing | 40 min | 2 hours | 28 min |
| 4 | Code Translation | 40 min | 2 hours | 28 min |
| 4.5 | Fidelity Check | 4 min | 10 min | 3 min |
| 5 | Model Training | 6 hours | 48 hours | 252 min |
| 5.5 | Data Authenticity | 4 min | 10 min | 3 min |
| 5.8 | Insight Extraction | 10 min | 20 min | 7 min |
| 6 | Visualization | 20 min | 30 min | 14 min |
| 6.5 | Visual Gate | 4 min | 10 min | 3 min |
| 7A | Paper Framework | 10 min | 15 min | 7 min |
| 7B | Model Sections | 30 min | 40 min | 21 min |
| 7C | Results Integration | 15 min | 20 min | 10 min |
| 7D | Analysis Sections | 10 min | 15 min | 7 min |
| 7E | Conclusions | 10 min | 15 min | 7 min |
| 7F | LaTeX Compilation | 5 min | 10 min | 4 min |
| 7.5 | LaTeX Gate | 4 min | 10 min | 3 min |
| 8 | Summary | 20 min | 30 min | 14 min |
| 9 | Polish | 20 min | 30 min | 14 min |
| 9.1 | Mock Judging | 10 min | 30 min | 7 min |
| 9.5 | Editor Feedback | 10 min | Variable | 7 min |
| 10 | Final Review | 20 min | 30 min | 14 min |
| 11 | Self-Evolution | 4 min | 10 min | 3 min |

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
- Expected: {min_time}-{max_time} minutes

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
- Expected: 40-120 minutes

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

## Director Time Validation Call

After receiving a completion report, Director calls @time_validator:

```
@time_validator: Phase Time Check

Phase: {X} ({phase_name})
Agent: @{agent_name}
Reported Duration: {XX} minutes
Expected Range: {min_time}-{max_time} minutes
Threshold (-30%): {threshold} minutes

Check:
1. Query Python backend log at output/implementation/logs/phase_{X}_timing.json
2. Compare reported duration vs logged duration
3. Validate against -30% threshold

Return: APPROVE / REJECT_INSUFFICIENT_TIME / INVESTIGATE
```

### Validation Decision Rules

| Condition | Verdict | Action |
|-----------|---------|--------|
| Duration >= Min Time | APPROVE | Proceed to next phase |
| Duration >= Threshold AND < Min | APPROVE with NOTE | Proceed, but flag for quality review |
| Duration < Threshold | REJECT_INSUFFICIENT_TIME | Force phase rerun |
| Logged != Reported (>10% diff) | INVESTIGATE | Verify timestamps, potential fraud |

---

## Rejection Protocol

When @time_validator returns `REJECT_INSUFFICIENT_TIME`:

### Step 1: Log Rejection
Append to `output/docs/time_rejections.md`:

```markdown
## Rejection: Phase {X} - {timestamp}

- **Agent**: @{agent_name}
- **Reported Duration**: {XX} minutes
- **Threshold**: {YY} minutes
- **Reason**: Duration below -30% threshold
- **Action**: Forced rerun
```

### Step 2: Force Phase Rerun
Send message to agent:

```
@{agent}: Phase {X} REJECTED - Insufficient time.

Your reported duration ({actual} min) is below the threshold ({threshold} min).
This suggests your work may be incomplete or simplified.

Please rerun Phase {X} with full rigor:
1. Do not rush or skip steps
2. Complete all required tasks thoroughly
3. Report accurate timing

Expected duration: {min_time}-{max_time} minutes
```

### Step 3: Block Progression
- Do NOT proceed to next phase until time validation passes
- Allow maximum 2 reruns before escalation
- After 2 failed reruns, investigate root cause

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

---

## Special Cases

### Variable Duration Phases

Some phases have variable expected durations:
- **Phase 5 (Training)**: 6-48+ hours depending on model complexity
- **Phase 9.5 (Editor Feedback)**: Depends on number of issues found

For these phases, use the minimum threshold but allow extended time without penalty.

### Gate Phases

Gate phases (0.5, 1.5, 4.5, 5.5, 6.5, 7.5) have shorter expected times (4-10 min) because they are validation-focused, not implementation-focused.

### Phase 7 Sub-Phases

Each sub-phase (7A-7F) has its own timing requirements. Track separately:
- 7A: 10-15 min (Abstract + Intro + Notation)
- 7B: 30-40 min (Model sections - largest)
- 7C: 15-20 min (Results integration)
- 7D: 10-15 min (Analysis sections)
- 7E: 10-15 min (Conclusions + Bibliography)
- 7F: 5-10 min (LaTeX compilation)

---

## Integration with VERSION_MANIFEST.json

After successful time validation, update manifest:

```json
{
  "phase_3": {
    "status": "completed",
    "timestamp": "2026-01-30T11:15:00",
    "duration_minutes": 75,
    "time_validated": true
  }
}
```

---

*Reference: CLAUDE.md - Phase Completion Protocol (v3.2.0)*
