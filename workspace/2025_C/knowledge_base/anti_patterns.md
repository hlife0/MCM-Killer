# Anti-Patterns Guide

> **Source**: CLAUDE.md v3.2.0 Anti-Patterns to Avoid
> **Full Reference**: templates/writing/6_anti_patterns.md
> **Purpose**: Detailed guide on patterns that lead to failure and how to avoid them

---

## Overview

Anti-patterns are common behaviors that seem reasonable but lead to systematic failures. As Director, recognizing and preventing these patterns is critical to competition success.

---

## Pattern 1: Rubber-Stamp Quality Gates

### Description

Letting phases proceed without properly meeting quality criteria. The Director approves work superficially without verifying requirements.

### Examples

**Bad Behavior**:
- "Looks good, proceed to next phase."
- Approving validation gates without reading agent reports
- Accepting "APPROVED" verdicts without verifying evidence
- Rushing through gates when behind schedule

**Warning Signs**:
- Validation takes < 2 minutes
- Agent verdicts are single sentences
- No specific file/line references in approvals
- Downstream phases immediately encounter issues

### Why This Fails

Downstream phases receive inadequate inputs:
- @code_translator gets incomplete model_design.md → Guesses implementation
- @writer gets incomplete results → Makes up data
- @validator catches fabricated data → Rejection cascade

### Prevention

1. **Enforce minimum verdict standards**:
   - 3+ sentences required
   - Specific file locations cited
   - Evidence quoted from files

2. **Director checklist before approving gate**:
   - [ ] All required files exist?
   - [ ] Agents provided specific evidence?
   - [ ] No "NEEDS_REVISION" unaddressed?

3. **If verdict seems too brief**:
   ```
   @{agent}: Your approval is too brief.
   Please provide:
   1. Which files you reviewed
   2. What specific evidence supports approval
   3. Confirmation no regressions introduced
   ```

---

## Pattern 2: Ignoring Protocol Violations

### Description

Allowing agents to skip protocols "just this once" due to time pressure or convenience. Exceptions accumulate into systematic failures.

### Examples

**Bad Behavior**:
- "Skip Phase 0.5 this time, we're behind schedule."
- "Don't bother with the 5-agent consultation, @modeler knows best."
- "The validation gate passed with 6/10, close enough."
- "@time_validator says training too short, but results look fine."

**Warning Signs**:
- "Just this once" appears in reasoning
- Protocol steps skipped without documentation
- Gate thresholds relaxed mid-competition
- Agents operating without required inputs

### Why This Fails

Protocols exist to prevent systematic failures:
- Phase 0.5 catches weak methods BEFORE 20+ hours of work
- 5-agent consultation catches blind spots
- Validation gates ensure downstream compatibility
- Time validation prevents fraudulent shortcuts

### Prevention

1. **Zero tolerance policy**:
   - Document ANY protocol deviation in `known_issues.md`
   - Require explicit justification
   - Log who approved and why

2. **Escalation protocol**:
   - If time pressure forces deviation, document trade-off
   - Consider which failure mode is more acceptable
   - Never silently skip

3. **If tempted to skip**:
   Ask: "What is this protocol protecting against?"
   If the answer involves data integrity → NEVER skip

---

## Pattern 3: No Timeline Monitoring

### Description

Only checking progress at the end of the competition, making it impossible to recover from delays.

### Examples

**Bad Behavior**:
- "Let's see where we are at Hour 60."
- No updates to orchestration_log.md
- Surprise at Phase 5 taking 30+ hours
- Discovering at Hour 68 that paper writing hasn't started

**Warning Signs**:
- No timestamps in logs
- orchestration_log.md empty or outdated
- Director doesn't know current phase
- Agents working without time awareness

### Why This Fails

You cannot recover from delays detected late:
- Hour 70 is too late to simplify models
- Hour 68 is too late to restart training
- Hour 65 is too late for major revisions

### Prevention

1. **Update dashboard every 4-6 hours**:
   ```markdown
   ## Timeline Check - Hour {X}
   Current Phase: {X}
   Hours Elapsed: {Y}/72
   Hours Remaining: {Z}
   Status: ON_TRACK / BEHIND / AHEAD
   ```

2. **Set phase deadlines**:
   - Phase 0-2: Complete by Hour 15
   - Phase 3-4.5: Complete by Hour 30
   - Phase 5: Complete by Hour 54
   - Phase 6-7.5: Complete by Hour 65
   - Phase 8-11: Complete by Hour 72

3. **Automatic checkpoints**:
   - Hour 12: Are we past Phase 0.5?
   - Hour 24: Is Phase 3 started?
   - Hour 36: Is training running?
   - Hour 48: Are preliminary results available?
   - Hour 60: Is paper writing started?

---

## Pattern 4: Single-Point Verification

### Description

Only the rejecting agent re-verifies after rework, missing regressions introduced by fixes.

### Examples

**Bad Behavior**:
- @validator rejects code, @code_translator fixes, only @validator re-checks
- Fix introduces bug in area @modeler reviewed, but @modeler not re-called
- "The rejector approved, we're done."

**Warning Signs**:
- Only 1 agent re-verifies after rework
- Other validators skip second review
- Regressions discovered in Phase 9

### Why This Fails

Fixes often introduce new issues:
- Fixing algorithm might break feature usage
- Fixing one model might affect shared utilities
- @validator might approve code change that @modeler would reject

### Prevention

1. **ALL validators must re-verify**:
   - Not just the rejector
   - All agents who participated in the gate

2. **Re-verification checklist**:
   - [ ] Original issue fixed?
   - [ ] No regression in my review area?
   - [ ] Still meets my approval criteria?

3. **Director coordination**:
   ```
   Rework complete. Calling ALL validators for re-verification:
   @validator: Re-verify code correctness
   @modeler: Re-verify algorithm alignment
   @feasibility_checker: Re-verify technical feasibility

   All must explicitly approve before proceeding.
   ```

---

## Pattern 5: Accepting Superficial Work

### Description

Accepting agent work that appears complete but lacks depth or rigor.

### Examples

**Bad Behavior**:
- Model design with "See literature" instead of equations
- Code with TODO comments left in
- Paper sections that are placeholder text
- Results tables with missing values

**Warning Signs**:
- Documents are suspiciously short
- Key sections say "to be completed"
- Equations reference undefined variables
- Code has untested branches

### Why This Fails

Superficial work creates technical debt that explodes later:
- @code_translator can't implement undefined equations
- @model_trainer can't run incomplete code
- @writer can't cite missing results
- @validator catches issues, cascade of rework

### Prevention

1. **Spot-check outputs**:
   - Read first and last 10 lines of each file
   - Verify equations are complete
   - Check code runs without errors

2. **Completeness checklist per phase**:
   - Phase 1: All equations defined? Variables listed?
   - Phase 3: All designed features created?
   - Phase 4: Code runs? Tests pass?
   - Phase 5: Results complete? No NaN values?

3. **Quality bar**:
   "Would this be acceptable in a submitted paper?"
   If no → Request rework before proceeding

---

## Pattern 6: Data Fabrication Under Pressure

### Description

Creating fake data or results when training takes too long or fails.

### Examples

**Bad Behavior**:
- "Training is taking too long, let's estimate the results."
- Copying results from a similar model
- Generating synthetic results that "look reasonable"
- Skipping failed training and using placeholder values

**Warning Signs**:
- Results appear before training completes
- Results are suspiciously clean (no noise)
- Time mismatch (30 min training, 48 hour expected)
- Results don't match code parameters

### Why This Fails

This is academic fraud:
- @time_validator will detect and reject
- Paper will contain false claims
- Judges may detect inconsistencies
- Competition integrity violated

### Prevention

1. **Phase 5 is BLOCKING**:
   - Paper writing CANNOT start with fake data
   - Wait for real results, however long

2. **Time validation is mandatory**:
   - Training duration must be ≥30% of expected
   - Algorithm must match code
   - Results must be traceable to training logs

3. **If training fails**:
   - Fix the issue and retry
   - Simplify model if necessary (with approval)
   - Document limitations honestly
   - NEVER fabricate data

---

## Quick Reference Table

| Pattern | Detection | Prevention |
|---------|-----------|------------|
| Rubber-Stamp Gates | Brief verdicts, quick approvals | Enforce 3+ sentence minimum |
| Ignoring Violations | "Just this once" reasoning | Zero tolerance, document all |
| No Timeline Monitoring | Surprise delays at end | Update every 4-6 hours |
| Single-Point Verification | Only rejector re-verifies | ALL validators must re-verify |
| Accepting Superficial Work | Placeholder text, TODOs | Spot-check all outputs |
| Data Fabrication | Time mismatch, clean results | Enforce time validation |

---

*Reference: CLAUDE.md - Anti-Patterns to Avoid*
*Full Reference: templates/writing/6_anti_patterns.md*
