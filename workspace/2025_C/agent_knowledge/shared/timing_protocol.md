# Shared Timing Protocol for All Agents (v3.3.0)

> **Purpose**: Common timing and consultation export requirements for all agents.
> This file is referenced by each agent to ensure consistent phase timing and documentation.
>
> **v3.3.0 CRITICAL CHANGE**: MINIMUM is now the HARD FLOOR. No threshold buffer.
> Duration < MINIMUM = REJECT. No exceptions.

---

## Overview

Every agent MUST:
1. Track their own phase timing using `time_tracker.py`
2. Export a consultation document after completing work
3. Include timing information in completion reports
4. **NEVER complete a phase below the MINIMUM time**

---

## Time Tracker Tool Usage

The `tools/time_tracker.py` script provides CLI commands for timing.

### Start a Phase

```bash
python tools/time_tracker.py start --phase {X} --agent {agent_name}
```

**Example**:
```bash
python tools/time_tracker.py start --phase 1 --agent modeler
```

### End a Phase

```bash
python tools/time_tracker.py end --phase {X} --agent {agent_name}
```

**Example**:
```bash
python tools/time_tracker.py end --phase 1 --agent modeler
```

### Validate Phase Timing (for @time_validator)

```bash
python tools/time_tracker.py validate --phase {X}
```

### List All Phase Logs

```bash
python tools/time_tracker.py list
```

---

## Phase Time Requirements (v3.3.0 - HARD MINIMUMS)

> **CRITICAL**: MINIMUM is the HARD FLOOR. No threshold buffer. Duration < MINIMUM = REJECT.

| Phase | Name | MINIMUM | Max Time | Notes |
|-------|------|---------|----------|-------|
| 0 | Problem Understanding | **35 min** | 60 min | HARD FLOOR |
| 0.1 | External Resources | **15 min** | 30 min | HARD FLOOR |
| 0.2 | Knowledge Retrieval | **20 min** | 30 min | HARD FLOOR |
| 0.5 | Methodology Gate | **25 min** | 40 min | HARD FLOOR |
| 1 | Model Design | **120 min (2h)** | 360 min | HARD FLOOR |
| 1.5 | Time Validation | **10 min** | 20 min | HARD FLOOR |
| 2 | Feasibility Check | **35 min** | 60 min | HARD FLOOR |
| 3 | Data Processing | **75 min** | 120 min | HARD FLOOR |
| 4 | Code Translation | **75 min** | 120 min | HARD FLOOR |
| 4.5 | Fidelity Check | **10 min** | 20 min | HARD FLOOR |
| 5 | Model Training | **180 min (3h)** | 2880 min | **CRITICAL - 3 HOURS MINIMUM** |
| 5.5 | Data Authenticity | **10 min** | 20 min | HARD FLOOR |
| 5.8 | Insight Extraction | **25 min** | 40 min | HARD FLOOR |
| 6 | Visualization | **35 min** | 60 min | HARD FLOOR |
| 6.5 | Visual Gate | **10 min** | 20 min | HARD FLOOR |
| 7A | Paper Framework | **25 min** | 40 min | HARD FLOOR |
| 7B | Model Sections | **60 min** | 90 min | HARD FLOOR |
| 7C | Results Integration | **45 min** | 60 min | HARD FLOOR |
| 7D | Analysis Sections | **25 min** | 40 min | HARD FLOOR |
| 7E | Conclusions | **32 min** | 45 min | HARD FLOOR |
| 7F | LaTeX Compilation | **15 min** | 30 min | HARD FLOOR |
| 7.5 | LaTeX Gate | **10 min** | 20 min | HARD FLOOR |
| 8 | Summary | **35 min** | 60 min | HARD FLOOR |
| 9 | Polish | **35 min** | 60 min | HARD FLOOR |
| 9.1 | Mock Judging | **20 min** | 45 min | HARD FLOOR |
| 9.5 | Editor Feedback | **20 min** | 60 min | HARD FLOOR |
| 10 | Final Review | **35 min** | 60 min | HARD FLOOR |
| 11 | Self-Evolution | **10 min** | 20 min | HARD FLOOR |

**ENFORCEMENT**: Duration < MINIMUM = REJECT_INSUFFICIENT_TIME. No threshold reduction. MINIMUM is the floor.

---

## Consultation Export Requirements

### File Path Convention

```
output/docs/consultations/phase_{X}_{agent}_{timestamp}.md
```

**Timestamp format**: `YYYY-MM-DDTHH-MM-SS` (hyphens instead of colons for filesystem safety)

**Examples**:
- `phase_0_reader_2026-01-30T14-30-00.md`
- `phase_1_modeler_2026-01-30T16-00-00.md`
- `phase_5_model_trainer1_2026-01-30T20-00-00.md`

### Generating Timestamp in Bash

```bash
TIMESTAMP=$(date +%Y-%m-%dT%H-%M-%S)
echo "phase_1_modeler_${TIMESTAMP}.md"
```

### Consultation Document Template

```markdown
# Phase {X} Consultation: @{agent_name}

**Timestamp**: {ISO timestamp}
**Phase**: {X} - {phase_name}
**Duration**: {XX} minutes

## Work Summary
{Brief description of what was done}

## Deliverables
- {file1.ext}: {description}
- {file2.ext}: {description}

## Key Decisions Made
1. {Decision 1 and rationale}
2. {Decision 2 and rationale}

## Issues Encountered
- {Issue 1}: {Resolution}
- {Issue 2}: {Resolution}
- None (if no issues)

## Recommendations for Next Phase
{What the next agent should know}

## Quality Self-Assessment
- Confidence: {1-10}
- Completeness: {percentage}
- Rigor: HIGH / MEDIUM / LOW
```

---

## Completion Report Format (v3.3.0)

All agents MUST include timing in their completion reports:

```markdown
Director, Phase {X} COMPLETE.

## Timing
- Phase: {X} ({name})
- Start: {ISO timestamp}
- End: {ISO timestamp}
- Duration: {XX} minutes
- Expected: {min}-{max} minutes

## Deliverables
- Output files: {list}
- Status: SUCCESS / PARTIAL / FAILED

## Self-Assessment
- Quality: HIGH / MEDIUM / LOW
- Confidence: {1-10}
- Issues encountered: {list or "None"}
```

---

## Verification Checklist

Before reporting phase completion:
- [ ] time_tracker.py start called at beginning
- [ ] time_tracker.py end called at completion
- [ ] Consultation document exported to output/docs/consultations/
- [ ] Duration included in completion report
- [ ] Self-assessment included

---

## Time Validation Flow

```
Agent completes Phase X
    ↓
Agent calls: python tools/time_tracker.py end --phase X --agent {name}
    ↓
Agent exports consultation to output/docs/consultations/
    ↓
Agent reports to @director with timing info
    ↓
@director calls @time_validator:
  "Phase X completed by @{agent}. Duration: {actual_time}.
   Expected range: {min_time} - {max_time}.
   Validate time reasonability."
    ↓
@time_validator:
  1. Runs: python tools/time_tracker.py validate --phase X
  2. Compares actual vs expected
  3. Returns APPROVE / REJECT_INSUFFICIENT_TIME / INVESTIGATE
    ↓
If REJECT: Force phase rerun
If APPROVE: Proceed to next phase
```

---

## Minimum Time Awareness (v3.3.0 - CRITICAL)

> **HARD RULE**: You MUST NOT complete your phase before reaching the MINIMUM time.
> Duration < MINIMUM = REJECT. No exceptions. No threshold buffer.

**Know Your Phase Minimum**: Each phase has a MINIMUM time requirement that is a HARD FLOOR.

If you finish significantly faster than the minimum:
- **You MUST continue working** until you reach the MINIMUM
- You likely missed something important
- Use remaining time for: Double-checking work, considering edge cases, improving quality
- DO NOT rush to completion just to save time
- Quality is more important than speed

**Time is a signal**: Completing too quickly often indicates:
- Incomplete analysis
- Simplified implementation
- Skipped validation steps
- Missing edge cases

**ENFORCEMENT (v3.3.0)**:
- Duration < MINIMUM = **REJECT_INSUFFICIENT_TIME**
- No threshold buffer (the old 70%/30% thresholds are REMOVED)
- MINIMUM IS the rejection threshold
- If rejected, you MUST RERUN the phase

---

## Reference

- Full timing tool: `tools/time_tracker.py`
- CLAUDE.md Phase Completion Protocol: workspace/2025_C/CLAUDE.md
- Phase details: knowledge_base/phase_details.md
