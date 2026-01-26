# Protocol 13: DEFCON 1 Emergency Oversight

> **Trigger**: @judge_zero REJECT (score < 50) or fatal flaw detected
> **Purpose**: Emergency recovery with time-limited revision
> **Owner**: @director

## Trigger Conditions

### Automatic DEFCON 1 Triggers

Any of these conditions trigger emergency mode:

1. **Narrative Vacuum**: Abstract contains zero quantitative metrics
2. **Interpretation Gap**: Any figure lacks Observation-Implication caption
3. **Sensitivity Blindness**: No sensitivity analysis section
4. **Physical Impossibility**: Model predicts negative populations, >100% percentages
5. **Uncertainty Blindness**: No confidence intervals on key predictions
6. **Visualization Silence**: No figures in entire paper
7. **Judge Score < 50**: Overall judgment score below threshold

## DEFCON 1 Process

### Step 1: Damage Assessment

@director receives `judgment_report.md` from @judge_zero containing:
- Score breakdown by persona
- List of fatal flaws
- Prioritized repair tickets

### Step 2: Time Budget Allocation

Calculate available time:
```
Available Time = Deadline - Current Time - Safety Buffer (2 hours)
```

Allocate based on priority:
- Priority 1 (Must Fix): 60% of available time
- Priority 2 (Should Fix): 30% of available time
- Priority 3 (Nice to Fix): 10% of available time

### Step 3: Triage Decision

| Available Time | Action |
|---------------|--------|
| < 2 hours | Cosmetic fixes only (captions, abstract) |
| 2-4 hours | Priority 1 fixes only |
| 4-8 hours | Priority 1 + critical Priority 2 |
| > 8 hours | Full repair (all priorities) |

### Step 4: Assign Repair Tickets

@director assigns each ticket to appropriate agent:
- Abstract/caption issues → @writer
- Figure issues → @visualizer
- Methodology issues → @modeler + @code_translator
- Results issues → @validator
- Physical impossibilities → @modeler

### Step 5: Execute Repairs

Agents execute fixes in parallel where possible.
Each agent must:
1. Read the ticket requirements
2. Make minimal targeted fix
3. Document change in repair_log.md
4. Signal completion to @director

### Step 6: Re-Judgment

After all Priority 1 fixes complete:
1. @director invokes @judge_zero again
2. If PASS → Proceed to Phase 9.5
3. If CONDITIONAL PASS → Accept and proceed
4. If REJECT again → Apply Mercy Rule

## The Mercy Rule

After 3 consecutive REJECTs:
1. Issue **Conditional Pass** with documented limitations
2. Add appendix section "Known Limitations"
3. Flag as "Best Effort Given Time Constraints"
4. Proceed to Phase 9.5 (Polish)

**Rationale**: Hard deadline exists. Flawed submission > No submission.

## Common DEFCON 1 Scenarios

### Scenario A: Missing Quantitative Abstract

**Fatal Flaw**: Abstract has 0 numbers
**Time to Fix**: 30 minutes
**Assignment**: @writer
**Fix**:
```
Before: "Our model achieves good performance."
After: "Our model achieves RMSE = 4.2 (↓27%), R² = 0.89, identifying 3 critical hubs."
```

### Scenario B: Descriptive Figure Captions

**Fatal Flaw**: Figures lack Observation-Implication
**Time to Fix**: 1 hour
**Assignment**: @writer + @editor
**Fix**:
```
Before: "Figure 3 shows RMSE vs epochs."
After: "Figure 3 shows RMSE decreasing from 7.2 to 4.2 (Observation),
       indicating network structure is essential (Implication)."
```

### Scenario C: Missing Sensitivity Analysis

**Fatal Flaw**: No sensitivity section
**Time to Fix**: 3-4 hours
**Assignment**: @validator + @code_translator
**Action**:
- Run parameter sweep on top 2 parameters
- Generate sensitivity plot
- Write 2-paragraph interpretation

### Scenario D: Physical Impossibility

**Fatal Flaw**: Model predicts negative population
**Time to Fix**: 2-3 hours
**Assignment**: @modeler + @code_translator
**Action**:
- Add boundary constraints
- Re-run model
- Update results section

## Communication Protocol

### @director Announcement

When entering DEFCON 1:
```
@all: DEFCON 1 ACTIVATED. @judge_zero rejected paper (score: X/100).
Fatal flaw: [Description]
Available time: X hours
Priority 1 tickets: Y
Focus on [specific fixes]. All other work PAUSED.
```

### Agent Response Format

```
@director: Ticket #X acknowledged.
Estimated time: Y minutes
Starting now.
```

### Completion Signal

```
@director: Ticket #X COMPLETE.
Change: [Brief description]
Logged in: repair_log.md
Ready for re-judgment.
```

## Quality Gates Before Re-Judgment

Before invoking @judge_zero again, verify:
- [ ] All Priority 1 tickets marked COMPLETE
- [ ] repair_log.md updated with all changes
- [ ] LaTeX compiles without errors
- [ ] All modified figures regenerated
- [ ] Abstract word count < 250 words

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
