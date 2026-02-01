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

---

## NEW DEFCON 1 Scenarios (E-G): Page Balance Issues

### Scenario E: Under-Length Paper (<24 pages)

**Fatal Flaw**: Paper below minimum page count
**Time to Fix**: 1-2 hours
**Assignment**: @writer + @visualizer
**Detection**: Total pages < 24

**Expansion Workflow**:
1. Diagnose page deficit (how many pages short?)
2. Select expansion strategies based on deficit:
   - 0-2 pages short: Expand discussions, add sensitivity details
   - 2-4 pages short: Add conceptual figures, expand model descriptions
   - 4+ pages short: Multiple strategies, full content review
3. Execute expansion (priority order):
   - Priority 1: Add conceptual figures (+1-2 pages) → @visualizer
   - Priority 2: Expand model descriptions (+1-2 pages) → @writer
   - Priority 3: Add sensitivity analysis details (+0.5-1 page) → @writer
   - Priority 4: Expand results interpretation (+0.5-1 page) → @writer
   - Priority 5: Add appendix content (+1-2 pages) → @writer
   - Priority 6: Expand discussion section (+0.5 page) → @writer
4. Recompile and verify page count >= 24
5. Re-run @judge_zero verification

**Reference**: `../../agent_knowledge/judge_zero/expansion_strategies.md`

**Fix Template**:
```
Before: 21 pages (3 pages under minimum)
Action: Added 2 conceptual figures (+1.5 pages), expanded Model 2 description (+1 page),
        added appendix section (+0.5 pages)
After: 24 pages (meets minimum)
```

---

### Scenario F: Excessive Blank Space (>50% on any page)

**Fatal Flaw**: Page with >50% whitespace
**Time to Fix**: 30-60 minutes
**Assignment**: @editor + @writer
**Detection**: Visual scan or automated density analysis

**Layout Fix Workflow**:
1. Identify problem pages (list page numbers with >50% blank)
2. Diagnose cause:
   - Orphaned figure/table (small visual, rest of page empty)
   - Premature page break
   - Short section ending
   - Poor float placement
3. Apply fixes by cause:
   - Orphaned visual: Adjust figure size or combine with adjacent content
   - Premature break: Remove `\newpage` or `\clearpage` commands
   - Short section: Merge with adjacent section or expand content
   - Poor float: Adjust `[H]`, `[htbp]` placement options
4. Recompile and verify all pages <30% blank space
5. Re-run @judge_zero verification

**Quantitative Thresholds**:
| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Words/page (avg) | >=300 | 250-300 | <250 |
| Max blank % on any page | <30% | 30-50% | >50% |
| Pages with <200 words | 0 | 1-2 | >=3 |

**Fix Template**:
```
Before: Page 12 has 65% blank space (only Figure 5 caption, rest empty)
Action: Resized Figure 5 from 0.4\textwidth to 0.7\textwidth,
        added 2 paragraphs of interpretation below
After: Page 12 now 25% blank space (within acceptable range)
```

---

### Scenario G: Content Imbalance (>15% deviation)

**Fatal Flaw**: Section proportion deviates >15% from O-Prize target
**Time to Fix**: 1-2 hours
**Assignment**: Depends on which section is imbalanced
**Detection**: Section page count analysis vs. target proportions

**Target Proportions (O-Prize aligned)**:
| Section | Target % | Acceptable Range |
|---------|----------|------------------|
| Framework (Abstract, Intro) | 10% | 8-12% |
| Models | 44% | 38-50% |
| Evidence (Data, Results) | 24% | 20-30% |
| Analysis (Sensitivity, S/W) | 10% | 8-14% |
| Synthesis (Discussion, Conclusions) | 10% | 8-14% |
| Support (References, Appendix) | 6% | 4-10% |

**Rebalance Routing**:
| Imbalance | Agent | Phase |
|-----------|-------|-------|
| Models under-represented | @writer | 7B |
| Results over-represented | @writer + @visualizer | 7C |
| Analysis under-represented | @writer + @validator | 7D |
| Synthesis under-represented | @writer | 7E |

**Rebalance Workflow**:
1. Calculate current section proportions
2. Identify sections with >15% deviation
3. Determine if expansion or consolidation needed:
   - Under target: Expand (add content)
   - Over target: Consolidate (reduce or move to appendix)
4. Route to appropriate agent for correction
5. Recompile and recalculate proportions
6. Verify all sections within acceptable range (±5% of target)
7. Re-run @judge_zero verification

**Reference**: Protocol 22 - Content Balance Verification

**Fix Template**:
```
Before: Models section = 32% (target 44%, deviation -12% → CRITICAL)
Action: Expanded Model 1 mathematical derivations (+1 page),
        Added algorithm pseudocode to Model 3 (+0.5 page),
        Included parameter justification tables (+0.5 page)
After: Models section = 42% (within acceptable range 38-50%)
```

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
