# Task Management Guide

> **Source**: CLAUDE.md v3.2.0 Task Management
> **Purpose**: Detailed reference for Director's task management throughout competition

---

## Overview

As Director, you manage the 72-hour competition timeline by:
1. Assigning tasks to appropriate agents
2. Monitoring progress and identifying blockers
3. Adjusting strategy based on actual progress
4. Ensuring no agent sits idle when work is available

---

## Start of Competition

### Phase 1: Initial Setup (First 30 minutes)

**Step 1: Call @reader**
```
@reader: Read the problem PDF from output/problem/
Extract ALL requirements (treat all as MANDATORY).
Write to output/docs/research_notes.md
```

**Expected output**: `output/docs/requirements_checklist.md`

**Step 2: Call @researcher**
```
@researcher: Read @reader's extracted requirements.
Brainstorm 3-6 modeling methods for each requirement.
For each method: description, justification, complexity, O-Prize assessment.
Append to output/docs/research_notes.md
```

**Expected output**: Updated `output/docs/research_notes.md`

**Step 3: Review and Identify Parallel Opportunities**

Ask yourself:
- Which requirements are independent? → Can be modeled in parallel
- Which require sequential data? → Must be ordered
- What can @writer start while models are being designed?

---

## During Competition

### Continuous Monitoring Questions

Ask yourself these questions every 30-60 minutes:

| Question | If Yes → Action |
|----------|-----------------|
| Is any agent idle? | Give them a task from the queue |
| Is @model_trainer producing weak results? | Call @modeler for iteration |
| Is @writer waiting for results? | Have them draft background sections |
| Running low on time? | Call @advisor for early review |
| Does @advisor find issues? | Assign specific fixes to relevant agents |
| Is Phase 5 taking too long? | Check for errors, consider simplification |
| Are validation gates failing repeatedly? | Investigate root cause, consider rewind |

### Task Queue Management

Maintain a mental (or documented) task queue:

**Priority 1 (Critical Path)**:
- Tasks that block other work
- Validation gates
- Phase transitions

**Priority 2 (Important)**:
- Model development
- Data processing
- Code translation

**Priority 3 (Background)**:
- Paper drafting (Introduction, Background)
- Documentation
- Quality checks

### Agent Idle Detection

**Signs an agent might be idle**:
- No output files updated recently
- Waiting for input from another agent
- Completed assigned work

**Actions when agent is idle**:
1. Check if their primary task is complete
2. Assign next task in their specialty
3. If no immediate task, assign background work:
   - @writer → Draft Introduction, Literature Review
   - @researcher → Deeper literature search
   - @advisor → Early review of completed sections

---

## Checkpoints

### Checkpoint 1: After @reader completes (Phase 0)

- [ ] `requirements_checklist.md` exists
- [ ] All requirements extracted (count matches problem statement)
- [ ] Requirements categorized (mandatory vs optional)
- [ ] No ambiguous requirements (clarify if needed)

**If issues**: Have @reader re-read specific sections

### Checkpoint 2: After first model design (Phase 1)

- [ ] `model_design_1.md` exists with full specification
- [ ] Design Expectations Table included
- [ ] All 5 consultants provided feedback
- [ ] @modeler incorporated feedback

**If issues**: Request specific revisions based on consultant feedback

**Also**: Call @advisor for quick review
```
@advisor: Quick review of model_design_1.md
Focus: Mathematical rigor, O-Prize competitiveness
Time: 5-10 minutes
```

### Checkpoint 3: After 50% requirements (Phase 1-4)

- [ ] At least half of models designed
- [ ] Data processing keeping pace with model design
- [ ] No major blockers identified
- [ ] Timeline on track

**If behind schedule**:
1. Identify bottlenecks
2. Consider simplifying remaining models (with @modeler consultation)
3. Adjust time allocation for remaining phases

### Checkpoint 4: Before @writer finishes (Phase 7)

Pre-flight check before paper completion:

- [ ] All results available in `output/implementation/data/`
- [ ] All figures generated in `output/figures/`
- [ ] No pending model fixes
- [ ] Validation gates passed

**If issues**:
1. Prioritize blocking items
2. @writer can work around missing items temporarily
3. Update paper when items complete

---

## Time Allocation Guidelines

### Suggested Time Budget (72 hours total)

| Phase Group | Allocation | Hours |
|-------------|------------|-------|
| Problem Understanding (0-0.5) | 5% | 3.6h |
| Model Design (1-2) | 15% | 10.8h |
| Implementation (3-4.5) | 20% | 14.4h |
| Training (5-5.8) | 25% | 18h |
| Writing (6-7.5) | 20% | 14.4h |
| Polish & Review (8-11) | 15% | 10.8h |

### Time Monitoring

Update `output/docs/orchestration_log.md` every 4-6 hours:

```markdown
## Timeline Update - Hour {X}

| Phase | Status | Hours Spent | Budget | Variance |
|-------|--------|-------------|--------|----------|
| 0-0.5 | Complete | 3.5h | 3.6h | +0.1h |
| 1-2 | In Progress | 8h | 10.8h | +2.8h remaining |
| 3-4.5 | Pending | 0h | 14.4h | - |
| ... | ... | ... | ... | ... |

Buffer remaining: {X} hours
Burn rate: {X}h/phase vs {Y}h/phase expected
```

---

## Parallel Work Patterns

### Pattern 1: Background Work in Parallel

While @modeler + team work on Model 1:
- @writer drafts Introduction
- @writer drafts Background/Literature Review
- @writer drafts Assumptions section

**Why**: These sections don't depend on specific model results

### Pattern 2: Multiple Models in Parallel

If requirements are independent:
1. @modeler designs Model A and Model B simultaneously
2. @feasibility_checker reviews both in parallel
3. @data_engineer prepares features for both
4. @code_translator implements (sequential if resource-limited, parallel if possible)

**Example**:
- Model A: Medal prediction (independent)
- Model B: Country ranking (independent)
- Model C: Host country advantage (depends on A results) → Sequential

### Pattern 3: Early Advisory Review

After first major section complete:
1. @advisor reviews draft (10-15 minutes)
2. Feedback informs remaining work
3. Prevents major revisions at end

**When to use**:
- After first model design
- After Phase 5 (first training results)
- After Phase 7C (results integrated)

---

## Emergency Procedures

### Agent Timeout (3+ consecutive failures)

1. Try alternative approach (simpler prompt)
2. Try breaking task into smaller chunks
3. If still failing, document and work around
4. Continue to next phase if possible

### Critical Convergence Failure

**Trigger**: R-hat > 1.3 OR 12+ hours without convergence

**Emergency flow**:
```
@model_trainer → @modeler → @code_translator
(Bypasses @director for speed)
```

**Director oversight**: Retroactive approval within 1 hour

### Running Out of Time

If at Hour 60+ and Phase 7 not started:
1. Simplify remaining models (with @modeler approval)
2. Use preliminary results in paper
3. Document limitations clearly
4. Focus on complete, polished submission over comprehensive analysis

---

*Reference: CLAUDE.md - Task Management*
