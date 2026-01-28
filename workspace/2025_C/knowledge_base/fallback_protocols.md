# Fallback Protocols - Automatic Decision Rules

**Purpose**: Enable fully autonomous 72-hour competition execution
**Version**: 1.0.0
**Date**: 2026-01-28

---

## Overview

These protocols define **automatic actions** for unexpected situations. The Director agent follows these rules **without stopping to ask the user**.

**Philosophy**: Document → Assess → Workaround → Continue
**Goal**: Zero workflow interruptions during 72-hour competition

---

## Rule 1: Phase 5B Timeline Exceeded

### Trigger Conditions
- Training duration >48 hours (predicted or actual)
- Windows compatibility issues detected
- Memory overflow errors
- MCM/Stan initialization failures on Windows

### Automatic Action Sequence
1. **Document**: Create entry in `output/docs/known_issues.md`
   - Issue ID: ISSUE-001
   - Description: Phase 5B timeline/platform issue
   - Impact: Medium (5A results sufficient)

2. **Assess**: Does this block submission?
   - Answer: NO (Phase 5A provides valid results)

3. **Workaround**:
   - Use Phase 5A quick training results for paper
   - Let Phase 5B continue in background (run_in_background=true)
   - Proceed immediately to Phase 6-7

4. **Continue**: DO NOT stop workflow

### Example Entry in known_issues.md
```markdown
## ISSUE-001 - Phase 5B Windows Compatibility
**Phase**: 5B
**Timestamp**: 2026-01-28 14:30
**Trigger**: MCM initialization failure on Windows platform
**Automatic Action**: Rule 1 applied
**Workaround**: Proceeding with Phase 5A results (raster_search completed successfully)
**Impact**: Medium (5A provides valid results, 5B continues background)
**Status**: Mitigated
```

---

## Rule 2: Agent Timeout (3+ Attempts)

### Trigger Conditions
- Any agent times out 3 consecutive times
- "Maximum token limit" errors
- Session crashes during agent execution

### Automatic Action Sequence
1. **Document**: Create entry in `output/docs/known_issues.md`
   - Issue ID: ISSUE-002
   - Agent name: [@agent_name]
   - Error type: Timeout/Token limit

2. **Assess**: Does this block submission?
   - Answer: NO (alternative approaches available)

3. **Workaround** (try in order):
   - **Option A**: Simplify prompt (reduce complexity)
   - **Option B**: Break task into 2-3 smaller chunks
   - **Option C**: Use alternative agent
   - **Option D**: Skip non-critical output, continue

4. **Continue**: DO NOT stop workflow

### Example Entry in known_issues.md
```markdown
## ISSUE-002 - @writer Timeout (3rd Attempt)
**Phase**: 7
**Timestamp**: 2026-01-28 18:45
**Trigger**: @writer exceeded token limit 3× consecutively
**Automatic Action**: Rule 2 applied (Option C)
**Workaround**: Delegated to @narrative_weaver for outline, will retry @writer with simplified prompt
**Impact**: Low (workaround available)
**Status**: Mitigated
```

---

## Rule 3: Phase 5B Parallel Execution

### Trigger Conditions
- Phase 5A completes successfully
- `results_quick_{i}.csv` exists and validated

### Automatic Action Sequence
1. **Launch 5B in Background**:
   ```python
   Task tool: run_in_background=true
   Agent: @model_trainer
   Task: "Phase 5B: Full training (may take 6-48h)"
   ```

2. **Proceed Immediately**:
   - Move to Phase 6 (Visualization) using 5A results
   - Begin Phase 7 (Paper Writing) in parallel

3. **Monitor**:
   - Check 5B status every 2 hours
   - If 5B completes before paper → Update results
   - If 5B still running → Submit with 5A results

4. **Continue**: DO NOT wait for 5B

### Example Entry in known_issues.md
```markdown
## ISSUE-003 - Phase 5B Background Execution
**Phase**: 5B → 6
**Timestamp**: 2026-01-28 12:00
**Trigger**: Phase 5A completed successfully
**Automatic Action**: Rule 3 applied
**Workaround**: Launched 5B in background (task_id: xyz), proceeding to Phase 6-7 with 5A results
**Impact**: Low (parallel workflow)
**Status**: Monitoring (check every 2h)
```

---

## Rule 4: Unexpected Issues (Default Protocol)

### Trigger Conditions
- Any unanticipated problem not covered by Rules 1-3
- File corruption
- Validation failures
- Unexpected errors

### Automatic Action Sequence
1. **Document**: Create entry in `output/docs/known_issues.md`
   - Issue ID: ISSUE-00X
   - Description: Unexpected error
   - Error details (if available)

2. **Assess**: Does this block submission?
   - **If YES**: Can we proceed without this output?
     - If YES → Document, apply workaround, continue
     - If NO → Document, apply best available workaround, continue
   - **Only stop if 100% blocked** (no workaround exists)

3. **Workaround Options**:
   - Use alternative file/method
   - Simplify output requirements
   - Skip non-critical component
   - Use placeholder/dummy data (with documentation)
   - Proceed with degraded quality

4. **Continue**: Always continue unless 100% blocked

### Example Entry in known_issues.md
```markdown
## ISSUE-004 - Figure Generation Failed
**Phase**: 6
**Timestamp**: 2026-01-28 20:15
**Trigger**: @visualizer unable to generate heatmap (missing data column)
**Automatic Action**: Rule 4 applied
**Workaround**: Proceeded with alternative visualization type (line plot), documented in paper
**Impact**: Low (alternative visualization acceptable)
**Status**: Resolved
```

---

## Implementation Notes

### When to Apply These Rules
- **Rule 1**: Phase 5B timeline/platform issues
- **Rule 2**: Agent timeouts (3+ attempts)
- **Rule 3**: Phase 5A completion (automatic parallel)
- **Rule 4**: All other unexpected issues (default)

### Decision Flowchart
```
Unexpected Issue → Document → Assess (blocks submission?)
├─ NO → Apply workaround → Continue
└─ YES → Workaround exists?
    ├─ YES → Apply workaround → Continue
    └─ NO → Document → Apply best available → Continue (99.9% of cases)
```

### Key Principle
**"Continue at all costs"** - The competition deadline is absolute. A degraded submission is better than no submission.

---

## Testing These Protocols

Before the actual competition, test these rules by:
1. Intentionally triggering Rule 1 (use Windows for Phase 5B)
2. Intentionally triggering Rule 2 (create complex task for timeout)
3. Verifying Rule 3 (confirm 5B runs in background)
4. Creating unexpected issues for Rule 4

**Expected Result**: System handles all issues automatically, never asks "What would you like me to do?"

---

## Template: known_issues.md

Copy this template to `output/docs/known_issues.md` at competition start:

```markdown
# Known Issues - [Competition Name]

**Competition Start**: [YYYY-MM-DD HH:MM]
**Director**: [@director]
**Status**: Active

---

## Issue Summary
| Issue ID | Phase | Impact | Status |
|----------|-------|--------|--------|
| ISSUE-001 | 5B | Medium | Mitigated |
| ISSUE-002 | 7 | Low | Resolved |

---

## [Issue ID] - [Brief Title]
**Phase**: X.X
**Timestamp**: YYYY-MM-DD HH:MM
**Trigger**: [What caused this issue]
**Automatic Action**: Rule X applied
**Workaround**: [What was done]
**Impact**: Low/Medium/High (does this block submission?)
**Status**: Mitigated/Monitoring/Resolved

---
```
