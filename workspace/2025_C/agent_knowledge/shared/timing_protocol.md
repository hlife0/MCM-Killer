# Shared Timing Protocol for All Agents (v3.2.0)

> **Purpose**: Common timing and consultation export requirements for all agents.
> This file is referenced by each agent to ensure consistent phase timing and documentation.

---

## Overview

Every agent MUST:
1. Track their own phase timing using `time_tracker.py`
2. Export a consultation document after completing work
3. Include timing information in completion reports

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

## Phase Time Requirements

| Phase | Name | Min Time | Max Time | Threshold |
|-------|------|----------|----------|-----------|
| 0 | Problem Understanding | 20 min | 30 min | 14 min (70%) |
| 0.2 | Knowledge Retrieval | 7 min | 15 min | 5 min (70%) |
| 0.5 | Methodology Gate | 10 min | 20 min | 7 min (70%) |
| 1 | Model Design | 90 min | 360 min | 63 min (70%) |
| 1.5 | Time Validation | 4 min | 10 min | 3 min (60%) |
| 2 | Feasibility Check | 20 min | 30 min | 14 min (70%) |
| 3 | Data Processing | 40 min | 120 min | 28 min (70%) |
| 4 | Code Translation | 40 min | 120 min | 28 min (70%) |
| 4.5 | Fidelity Check | 4 min | 10 min | 3 min (60%) |
| 5 | Model Training | 360 min | 2880 min | 108 min (30%) |
| 5.5 | Data Authenticity | 4 min | 10 min | 3 min (60%) |
| 5.8 | Insight Extraction | 10 min | 20 min | 7 min (70%) |
| 6 | Visualization | 20 min | 30 min | 14 min (70%) |
| 6.5 | Visual Gate | 4 min | 10 min | 3 min (60%) |
| 7A | Paper Framework | 10 min | 15 min | 7 min (70%) |
| 7B | Model Sections | 30 min | 40 min | 21 min (70%) |
| 7C | Results Integration | 15 min | 20 min | 11 min (70%) |
| 7D | Analysis Sections | 10 min | 15 min | 7 min (70%) |
| 7E | Conclusions | 10 min | 15 min | 7 min (70%) |
| 7F | LaTeX Compilation | 5 min | 10 min | 3 min (60%) |
| 7.5 | LaTeX Gate | 4 min | 10 min | 3 min (60%) |
| 8 | Summary | 20 min | 30 min | 14 min (70%) |
| 9 | Polish | 20 min | 30 min | 14 min (70%) |
| 9.1 | Mock Judging | 10 min | 30 min | 7 min (70%) |
| 9.5 | Editor Feedback | 10 min | 60 min | 5 min (50%) |
| 10 | Final Review | 20 min | 30 min | 14 min (70%) |
| 11 | Self-Evolution | 4 min | 10 min | 3 min (60%) |

**Threshold**: Minimum acceptable time = min_time × threshold_percentage

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

## Completion Report Format (v3.2.0)

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

## Minimum Time Awareness

**Know Your Phase Minimum**: Each phase has a minimum time requirement.

If you finish significantly faster than the minimum:
- You likely missed something important
- Use remaining time for: Double-checking work, considering edge cases, improving quality
- DO NOT rush to completion just to save time
- Quality is more important than speed

**Time is a signal**: Completing too quickly often indicates:
- Incomplete analysis
- Simplified implementation
- Skipped validation steps
- Missing edge cases

---

## Reference

- Full timing tool: `tools/time_tracker.py`
- CLAUDE.md Phase Completion Protocol: workspace/2025_C/CLAUDE.md
- Phase details: knowledge_base/phase_details.md
