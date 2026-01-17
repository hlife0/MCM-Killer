# Editor Feedback Enforcement Mechanism (v2.5.4)

> **Critical Addition**: v2.5.4
> **Purpose**: Ensure @editor's critical issues are addressed through mandatory rework
> **Status**: MANDATORY for Phase 9

---

## Problem Statement

**Issue Discovered**:
```
@editor verdict: CRITICAL_ISSUES
  - Grammar errors throughout
  - Data inconsistencies between paper and CSV
  - Unclear methodology descriptions

Current behavior:
  [No mechanism to enforce fixes]
  Result: Critical issues not addressed, quality suffers

Expected behavior:
  [Mandatory multi-agent rework triggered]
  Result: All issues fixed, quality improved
```

**Impact**:
- Critical paper issues never fixed
- Quality gates bypassed
- Final submission quality suffers
- Competition score reduced

---

## Root Cause Analysis

### Why Editor Feedback Was Ignored

1. **No Mandatory Rework Trigger**
   - @editor returns verdict but no enforcement mechanism
   - Director may proceed to Phase 10 without fixes
   - No loop-back to relevant agents

2. **No Issue Categorization**
   - @editor identifies problems but doesn't specify who should fix
   - Unclear which agent is responsible for which issue
   - No systematic assignment of rework tasks

3. **No Re-verification Gate**
   - After agents revise, no gate to verify fixes
   - No feedback loop to ensure issues resolved
   - @editor never sees revised version

---

## Solution: Phase 9.5 Editor Feedback Enforcement

### Gate Location

```
Phase 9 (@editor) → Phase 9.5 (Editor Feedback Enforcement) → Phase 10 (@advisor)
                                      ↓ CRITICAL_ISSUES
                                Multi-agent rework
                                      ↓
                                Re-verification
                                      ↓
                                Loop until APPROVED
```

### Gate Rules

**MANDATORY**: @editor's verdict MUST trigger appropriate action.

**Verdict Categories**:

| Verdict | Meaning | Action Required |
|---------|---------|-----------------|
| `APPROVED` | No issues found | Proceed to Phase 10 |
| `MINOR_REVISION` | Small polish issues | @writer fixes, self-verify |
| `CRITICAL_ISSUES` | Major problems | Multi-agent rework + re-verification |

**Exit Conditions**:
- ✅ **APPROVED** → Proceed to Phase 10
- ⚠️ **MINOR_REVISION** → @writer fixes, verify, then proceed
- ❌ **CRITICAL_ISSUES** → Execute multi-agent rework protocol

---

## Implementation Protocol

### Step 1: @editor Provides Structured Feedback

@editor MUST categorize issues by responsible agent:

**Template**:
```markdown
# Editor Review Report

## Verdict
❌ CRITICAL_ISSUES

## Issue Breakdown

### Writing Issues (Responsibility: @writer)
1. Grammar errors in Section 3 (lines 45-67)
   - Missing articles, incorrect verb tense
   - Fix: Proofread and correct

2. Inconsistent terminology throughout
   - "medal count" vs "number of medals" used interchangeably
   - Fix: Use consistent terminology

### Data Issues (Responsibility: @data_engineer, @model_trainer)
3. Table 2 doesn't match features_core.csv
   - Table shows mean GDP = 15000, CSV shows 12500
   - Fix: Regenerate table from correct data

4. Figure 3 labels don't match legend
   - Fix: Correct figure labels

### Methodology Issues (Responsibility: @modeler, @researcher)
5. Model 1 explanation unclear
   - Equation (1) references undefined symbol $\theta$
   - Fix: Define all symbols in equations

6. Method selection not justified
   - Why ZINB instead of Poisson?
   - Fix: Add justification citing research

### Results Issues (Responsibility: @model_trainer, @validator)
7. Prediction intervals in Section 6 don't match results_1.csv
   - Paper: [12, 25], CSV: [10, 28]
   - Fix: Reconcile or explain discrepancy

## Recommendation
Send revision requests to:
- @writer (issues 1-2)
- @data_engineer, @model_trainer (issues 3-4)
- @modeler, @researcher (issues 5-6)
- @model_trainer, @validator (issue 7)

After revisions complete, send back to @editor for re-verification.
```

### Step 2: Director Analyzes Feedback

```python
# Parse @editor's report
editor_report = parse_editor_report()

# Group issues by responsible agent
issues_by_agent = {
  "@writer": [issue1, issue2],
  "@data_engineer": [issue3],
  "@model_trainer": [issue4, issue7],
  "@modeler": [issue5],
  "@researcher": [issue6],
  "@validator": [issue7]
}

# Determine strategy
num_agents = len(issues_by_agent)

if num_agents == 1:
    strategy = "single_agent_rework"
elif num_agents <= 4:
    strategy = "multi_agent_parallel_rework"
else:
    strategy = "consider_rewind"  # Too many issues
```

### Step 3: Send Revision Requests

**Single Agent Rework** (only @writer needs changes):
```
@writer:

Director: @editor found MINOR_REVISION issues in your paper.

Issues to fix:
1. Grammar errors in Section 3
2. Inconsistent terminology

Please fix these issues in paper_{i}.tex and report back when complete.
```

**Multi-Agent Parallel Rework** (multiple agents need changes):
```
=== Sending revision requests to 5 agents ===

@writer:
  Issues:
  1. Grammar errors in Section 3
  2. Inconsistent terminology
  Action: Fix in paper_{i}.tex

@data_engineer:
  Issues:
  3. Table 2 doesn't match features_core.csv
  Action: Regenerate table from correct data

@model_trainer:
  Issues:
  4. Figure 3 labels don't match legend
  7. Prediction intervals don't match results_1.csv
  Action: Fix figures and verify data consistency

@modeler:
  Issues:
  5. Equation (1) has undefined symbol
  Action: Add symbol definitions to paper

@researcher:
  Issues:
  6. Method selection not justified
  Action: Add justification to methodology section

=== Waiting for all agents to complete ===
```

### Step 4: Wait for All Revisions

```python
completed_agents = []
max_wait_time = 30  # minutes

start_time = time.now()
while len(completed_agents) < len(agents_to_fix):
    for agent in agents_to_fix:
        if agent not in completed_agents:
            if agent.reported_complete():
                completed_agents.append(agent)

    if time.now() - start_time > max_wait_time:
        # Timeout: Escalate to user
        alert_user("Editor feedback rework timeout")

    sleep(1)  # Check every second
```

### Step 5: Send to @editor for Re-verification

**All revisions complete**:
```
@editor:

Director: All agents have completed revisions based on your feedback.

Please re-verify the paper:

**Original Issues**:
1. Grammar errors in Section 3 → Fixed by @writer
2. Inconsistent terminology → Fixed by @writer
3. Table 2 data mismatch → Fixed by @data_engineer
4. Figure 3 labels → Fixed by @model_trainer
5. Equation (1) undefined symbol → Fixed by @modeler
6. Method selection not justified → Fixed by @researcher
7. Prediction intervals mismatch → Fixed by @model_trainer

**Revised Files**:
- paper_{i+1}.tex (updated by @writer, @modeler, @researcher)
- table_2_{i+1}.tex (updated by @data_engineer)
- figure_3_{i+1}.png (updated by @model_trainer)

Please provide your verdict:
- ✅ APPROVED: All issues resolved, proceed to Phase 10
- ⚠️ MINOR_REVISION: Small issues remaining, @writer should fix
- ❌ CRITICAL_ISSUES: Major issues remain, continue rework loop
```

### Step 6: Loop Until Approved

```python
max_iterations = 3
iteration = 0

while iteration < max_iterations:
    # Get @editor's re-verification verdict
    verdict = get_editor_verdict()

    if "APPROVED" in verdict:
        print("Editor approved. Proceeding to Phase 10.")
        break
    elif "MINOR_REVISION" in verdict:
        print("Minor revisions needed. Sending to @writer.")
        send_to_writer_for_minor_fixes()
    elif "CRITICAL_ISSUES" in verdict:
        print("Critical issues remain. Starting rework iteration " + str(iteration + 2))
        # Loop back to Step 2
        iteration += 1
        continue

if iteration == max_iterations:
    print("Max iterations reached. Escalating to user.")
    alert_user("Editor feedback rework: Max iterations reached")
```

---

## Issue Categorization Guide

### Writing Issues (@writer)

| Issue | Example | Action |
|-------|---------|--------|
| Grammar | Missing articles, wrong tense | Proofread and correct |
| Style | Inconsistent voice | Rewrite for consistency |
| Structure | Poor paragraph organization | Reorganize |
| Clarity | Confusing sentences | Rewrite for clarity |
| Typos | Spelling errors | Correct |
| Formatting | LaTeX formatting issues | Fix LaTeX code |

### Data Issues (@data_engineer, @model_trainer)

| Issue | Example | Action |
|-------|---------|--------|
| Table errors | Numbers don't match CSV | Regenerate from source |
| Figure errors | Labels wrong, data mismatch | Regenerate from source |
| Inconsistency | Paper says X but CSV shows Y | Reconcile or explain |
| Missing data | Table references non-existent data | Add data or remove reference |

### Methodology Issues (@modeler, @researcher)

| Issue | Example | Action |
|-------|---------|--------|
| Unclear explanation | Model description confusing | Rewrite with more detail |
| Undefined symbols | Equation uses $\theta$ without definition | Add symbol definitions |
| Missing justification | Why this method? | Add research citations |
| Incomplete derivation | Says "we derive" but shows no steps | Add derivation steps |

### Results Issues (@model_trainer, @validator)

| Issue | Example | Action |
|-------|---------|--------|
| Number mismatch | Paper says 15 but CSV shows 12 | Reconcile or correct |
| Interval mismatch | Paper: [10, 20], CSV: [12, 22] | Explain difference or correct |
| Inconsistency | Figure 1 contradicts Figure 2 | Resolve contradiction |
| Missing validation | No verification of predictions | Add validation analysis |

---

## Protocol Integration

### Update Phase 9 Description

**OLD (v2.5.3)**:
```
Phase 9: Polish
  @editor reviews paper.tex
  Output: polished paper.tex
  Next: Phase 10
```

**NEW (v2.5.4)**:
```
Phase 9: Polish
  @editor reviews paper.tex
  Output: editor review report

Phase 9.5: Editor Feedback Enforcement (MANDATORY)
  If @editor verdict is:
    - APPROVED → Proceed to Phase 10
    - MINOR_REVISION → @writer fixes, self-verify
    - CRITICAL_ISSUES → Multi-agent rework
        1. Categorize issues by responsible agent
        2. Send parallel revision requests
        3. Wait for all agents to complete
        4. Send to @editor for re-verification
        5. Loop until APPROVED (max 3 iterations)
  Output: Revised paper.tex, figures, tables
  Next: Phase 10
```

---

## Anti-Patterns to Avoid

❌ **WRONG**: Ignore @editor's CRITICAL_ISSUES verdict
```
"@editor found critical issues but let's proceed to @advisor anyway"
```
✅ **CORRECT**: Mandatory rework triggered
```
"@editor found CRITICAL_ISSUES. Initiating multi-agent rework protocol."
```

❌ **WRONG**: Send everything to @writer
```
"@editor found issues, sending all to @writer to fix"
```
✅ **CORRECT**: Categorize and assign to responsible agents
```
"@editor found issues:
  - Writing → @writer
  - Data → @data_engineer
  - Methodology → @modeler
  Sending to all responsible agents in parallel."
```

❌ **WRONG**: No re-verification
```
"All agents fixed issues. Proceeding to Phase 10."
```
✅ **CORRECT**: Send to @editor for re-verification
```
"All agents fixed issues. Sending to @editor for re-verification."
```

❌ **WRONG**: Single iteration only
```
"@editor still finds issues. Proceeding anyway (only 1 iteration allowed)"
```
✅ **CORRECT**: Loop until approved or max iterations
```
"@editor still finds issues. Starting iteration 2/3 of rework loop."
```

---

## Testing Checklist

Test protocol with scenarios:

- [ ] @editor returns APPROVED (should proceed immediately)
- [ ] @editor returns MINOR_REVISION (should send to @writer only)
- [ ] @editor returns CRITICAL_ISSUES for 1 agent (single-agent rework)
- [ ] @editor returns CRITICAL_ISSUES for 3 agents (parallel rework)
- [ ] @editor returns CRITICAL_ISSUES for 5 agents (consider rewind)
- [ ] Re-verification iteration 2: Some issues fixed, some remain (loop correctly)
- [ ] Re-verification iteration 3: Max iterations reached (escalate to user)

---

**Document Version**: v2.5.4
**Created**: 2026-01-16
**Status**: MANDATORY for Phase 9 → Phase 10 transition
