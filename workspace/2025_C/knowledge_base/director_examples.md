# Director Agent Examples and Scenarios

This file contains detailed examples and scenarios extracted from CLAUDE.md to keep the main operational documentation concise while preserving all illustrative content.

---

## Table of Contents

1. [Phase Jump Decision Examples](#phase-jump-decision-examples)
2. [Re-validation Trigger Examples](#re-validation-trigger-examples)
3. [Emergency Protocol Examples](#emergency-protocol-examples)
4. [Multi-Agent Consultation Example](#multi-agent-consultation-example)
5. [Mock Court DEFCON 1 Examples](#mock-court-defcon-1-examples)
6. [Re-verification Approval Examples](#re-verification-approval-examples)
7. [Parallel Work Patterns](#parallel-work-patterns)
8. [Multi-Agent Rework and Decision Tree](#multi-agent-rework-and-decision-tree)
9. [Completion Report Format](#completion-report-format)
10. [Director Time Validation Call](#director-time-validation-call)
11. [Consultation Export Template](#consultation-export-template)
12. [Checkpoint Tracking](#checkpoint-tracking)
13. [Orchestration Log Examples](#orchestration-log-examples)
14. [Timestamps from Timing Log](#timestamps-from-timing-log)
15. [Issue Tracking Format](#issue-tracking-format)

---

## Phase Jump Decision Examples

### Example Scenarios

**Scenario 1**: @code_translator discovers formula(3) mathematically impossible
```
Director, I need to Rewind to Phase 1.
Problem: Formula(3) involves infinite summation, cannot implement.
Root Cause: Phase 1 didn't consider computational feasibility.
Impact: Phases 2-4 need redo (est. 3 hours)
Urgency: HIGH - Cannot continue Phase 4
Recommendation: Fix formula(3) to computable approximation
```

**Scenario 2**: @writer finds 15 countries with negative medal predictions
```
Director, I need to Rewind to Phase 5.
Problem: results_1.csv has negative predictions (impossible).
Root Cause: Phase 5 training or Phase 3 features may be wrong.
Impact: Phases 3-7 need redo (est. 6 hours)
Urgency: MEDIUM - Can write but data invalid
Recommendation: Check training code and features
```

### Rewind Decision Matrix

| Problem Severity | Rewind Cost | Urgency | Decision |
|-----------------|-------------|---------|----------|
| HIGH | LOW/MEDIUM | HIGH | **ACCEPT** |
| HIGH | HIGH | HIGH | Consider MODIFY |
| MEDIUM | LOW/MEDIUM | MEDIUM | **ACCEPT** |
| LOW | LOW | LOW | Consider |
| LOW | HIGH | LOW | **REJECT** |

**Cost Reference**: Low (1-2h): Phase 3→1/2 | Medium (2-4h): Phase 4→3 | High (4-8h): Phase 5→1 | Very High (8+h): Phase 10→1

---

## Re-validation Trigger Examples

### When Re-Validation Is Triggered

**@code_translator implements fix** (emergency OR standard protocol) → Provides CHANGES SUMMARY

**@director MUST check**:
1. Review @code_translator's CHANGES SUMMARY
2. Identify design parameter changes:
   - **Sampling parameters**: tune, chains, draws, target_accept, treedepth
   - **Algorithm changes**: NUTS → Metropolis, etc.
   - **Feature additions/removals**: New features added or designed features removed

### @director's Decision Protocol

**IF parameter changes detected in CHANGES SUMMARY**:
```
@time_validator: RE-VALIDATION REQUIRED

@code_translator has modified model_{i}.py:
Changes: {list of parameter changes}

Please run Phase 4.5 validation on reworked code:
- Check against Design Expectations Table
- Create comparison table (Design vs Actual vs Tolerance vs Verdict)
- Calculate overall score
- Return APPROVE/REJECT decision

DO NOT allow training to resume until validation complete.
```

**Training MUST NOT resume** until @time_validator completes re-validation and returns ✅ APPROVE.

**IF no parameter changes** (simple bug fix only):
- Allow training to resume without re-validation
- Document: "Simple bug fix, no parameter changes - re-validation not required"

### Examples

**Example 1: Parameter Change - RE-VALIDATION REQUIRED**
```
CHANGES SUMMARY:
- tune: 2000 → 2100 (+5%)
- draws: 20000 → 21000 (+5%)

@director Action:
→ CALL @time_validator for Phase 4.5 re-validation
→ Training PAUSED until @time_validator approves
```

**Example 2: Simple Bug Fix - NO RE-VALIDATION**
```
CHANGES SUMMARY:
- Fixed: pm.logp(var) → pm.logp(var, data) (API fix only)
- Parameters changed: NONE

@director Action:
→ Allow training to resume
→ Document: "API fix only, no parameter changes"
```

**Example 3: UNAUTHORIZED Simplification - REJECT**
```
CHANGES SUMMARY:
- tune: 2000 → 1000 (-50%)
- draws: 20000 → 1000 (-95%)
- chains: 4 → 2 (-50%)

@director Action:
→ CALL @time_validator for Phase 4.5 re-validation
→ @time_validator will REJECT (exceeds ±20% tolerance)
→ @code_translator must restore original parameters
```

### Why This Is Critical

**Without re-validation trigger**:
- @code_translator could simplify parameters during training
- Changes would be hidden in CHANGES SUMMARY but not validated
- Protocol 12's anti-fraud safeguard (40% → <5% fraud reduction) is bypassed
- Training completes with lazy implementation, detected only in Phase 5.5 (too late)

**With re-validation trigger**:
- ALL parameter changes during training are validated
- Hidden simplifications are caught BEFORE training resumes
- 8× fraud reduction (40% → <5%) is realized
- Implementation fidelity maintained throughout workflow

---

## Emergency Protocol Examples

### 🚨 Emergency Convergence Fix Protocol (v2.5.8)

**When to Use** (ALL criteria must be met):
1. ✅ R-hat > 1.3 (severe non-convergence)
   - OR 12+ hours without convergence
   - OR >10% divergent transitions
   - OR complete sampling failure
2. ✅ @modeler is available and responsive
3. ✅ Fix is simple parameter adjustment (NOT algorithm change)

**Emergency Flow** (bypasses standard @director coordination):
```
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix (copies @director)
@director → retroactive approval (within 1 hour)
@model_trainer → resumes training
```

**Safeguards**:
- **Single-use limit**: Once per model only
- **Time limit**: Fix must be implemented within 30 minutes
- **Severity threshold**: R-hat > 1.3 (not just >1.1)
- **Documentation**: All emergency fixes logged in VERSION_MANIFEST.json
- **Oversight**: @director retroactive approval required

**Response Time**:
- Standard protocol: 4-5 hours
- Emergency protocol: **30-60 minutes** (8x faster)

**See**: `model_trainer.md` lines 264-476 for complete protocol

### Integration with Emergency Protocol (v2.5.8)

**Emergency fixes ALSO require re-validation** if they change parameters:

```
Emergency flow (v2.5.8):
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix with CHANGES SUMMARY

@if CHANGES SUMMARY shows parameter changes:
  @director → @time_validator (RE-VALIDATION REQUIRED)
  @time_validator → validates against Design Expectations Table
  @time_validator → ✅ APPROVE / ❌ REJECT
  Training resumes ONLY if @time_validator approves

@if CHANGES SUMMARY shows no parameter changes:
  @director → allows training to resume
  (simple bug fix, API fix only, etc.)
```

---

## Multi-Agent Consultation Example

### Consultation Protocol (v2.5.6)

**BEFORE finalizing model design, you MUST**:

1. @modeler proposes → `output/model_proposals/model_X_draft.md`
2. **@director sends draft to 5 agents in PARALLEL**:
   - @researcher reviews (O-Prize alignment) → writes to `output/docs/consultations/feedback_model_X_researcher.md`
   - @feasibility_checker evaluates (tech feasibility) → writes to `output/docs/consultations/feedback_model_X_feasibility_checker.md`
   - @data_engineer reviews (data availability) → writes to `output/docs/consultations/feedback_model_X_data_engineer.md`
   - @code_translator assesses (implementability) → writes to `output/docs/consultations/feedback_model_X_code_translator.md`
   - @advisor critiques (weaknesses/improvements) → writes to `output/docs/consultations/feedback_model_X_advisor.md`
3. **@director verifies all 5 feedback files exist**:
   ```bash
   ls -1 output/docs/consultations/feedback_model_X_*.md | wc -l
   # Expected: 5
   ```
4. **If count < 5**: Re-call missing agents with reminder
5. **@director confirms to @modeler**: "All 5 feedback files received, please read them"
6. @modeler reads all feedback from `output/docs/consultations/feedback_model_X_*.md`
7. @modeler revises → final `model_design.md`

### Example Consultation (v2.5.6)

```
STEP 1: @modeler proposes → output/model_proposals/model_1_draft.md

STEP 2: @director sends to 5 agents in PARALLEL
  "@researcher: Review output/model_proposals/model_1_draft.md, write feedback to output/docs/consultations/feedback_model_1_researcher.md"
  "@feasibility_checker: Review output/model_proposals/model_1_draft.md, write feedback to output/docs/consultations/feedback_model_1_feasibility_checker.md"
  (same for @data_engineer, @code_translator, @advisor)

STEP 3: @director verifies all 5 feedback files exist
  ls -1 output/docs/consultations/feedback_model_1_*.md | wc -l
  Expected output: 5

STEP 4: @director confirms to @modeler
  "@modeler: All 5 feedback files received. Please read:
   - output/docs/consultations/feedback_model_1_researcher.md
   - output/docs/consultations/feedback_model_1_feasibility_checker.md
   - output/docs/consultations/feedback_model_1_data_engineer.md
   - output/docs/consultations/feedback_model_1_code_translator.md
   - output/docs/consultations/feedback_model_1_advisor.md"

STEP 5: @modeler reads all 5 feedback files, incorporates feedback

STEP 6: @modeler revises → output/model/model_design.md with "Consultation Summary"
```

### Consultation Triggers

| Decision | Who Must Consult | Why |
|----------|-----------------|-----|
| Model Selection | @researcher + @advisor | Appropriate/sophisticated |
| Feasibility | @feasibility_checker + @code_translator | Confirm tech feasibility |
| Assumptions | @modeler + @advisor | Justified/reasonable |
| Feature Engineering | @data_engineer + @modeler | Data + theorist agree |
| Data Availability | @data_engineer + @reader | Confirm exists/derivable |
| Implementation | @code_translator + @modeler | Math-to-code feasible |
| Visualization | @visualizer + @writer | Accurate + appealing |

---

## Mock Court DEFCON 1 Examples

### 🆕 Phase 9.1: Mock Judging (Protocol 13 / DEFCON 1)

> [!CAUTION] **[MANDATORY] Subject the paper to adversarial review BEFORE final polish.**

### Implementation
1. **Call @judge_zero**: "Review output/paper/paper.pdf using 3 personas (O-Prize, Technical, Clarity)."
2. **Review Report**: `output/docs/judgment_report.md`
3. **Verdict**: PASS / REJECT

### DEFCON 1 Protocol (If REJECTED)
- **Halt Progress**: Stop all Phase 10 activities.
- **Kill List**: Identify the "Fatal Flaws" (max 3).
- **Repair Tickets**: Assign specific agents to fix ONLY the fatal flaws.
- **Re-Judge**: @judge_zero reviews ONLY the fixes.
- **Mercy Rule**: After 3 rejects, Conditional Pass.

In practice:
1. Parse judgment_report.md into 1–3 concrete repair tickets, each with a responsible agent.
2. Run ticket fixes in parallel, then have @editor integrate and sanity-check.
3. Resubmit to @judge_zero focusing on the fixed items only.
4. If still REJECTED, repeat (max 3 total cycles, then apply Mercy Rule).

---

## Re-verification Approval Examples

### Global Re-Verification Standards

> [!CRITICAL] **ALL agents must re-verify, not just rejecters.**

**Protocol**:
- Re-verification set = ALL agents who participated in the gate (not just those who requested changes).
- Only proceed when ALL agents explicitly approve after rework.

**Strict Approval Standards**:
- **FORBIDDEN**: "Looks good, approved." | "Fixed issues, good to go."
- **REQUIRED**: 3+ sentences, specific file locations, evidence, no regression

### Example Good Approval (pattern):
```
I have reviewed the changes in output/docs/research_notes.md (lines 45-78, 120-145).

The methodological improvements address all previous concerns:
1. Added Bayesian hierarchical model (lines 50-65) - provides 9/10 sophistication
2. Included computational feasibility analysis (lines 130-145) - confirms <48h training
3. All three requirements now have advanced methods (not just basic regression)

No regressions detected - original content preserved, enhancements only strengthen the approach.

APPROVED - Ready for Phase 1.
```

### Example Multi-Agent Rework

**Scenario**: Validation gate completes with multiple NEEDS_REVISION

```
@feasibility_checker: NEEDS_REVISION
@advisor: NEEDS_REVISION
@data_engineer: FEASIBLE 8/10
@code_translator: APPROVED

YOU MUST:
1. Identify ALL agents with NEEDS_REVISION
2. Send parallel revision requests to ALL
3. Wait for ALL to complete
4. Send ALL for re-verification
5. Proceed only when ALL approve
```

**Decision Tree**:
```
Validation Gate → Collect verdicts
  0 agents NEEDS_REVISION → Proceed
  1 agent → Single-agent rework
  2-3 agents → Multi-agent parallel rework
  4+ agents → Consider rewind
```

**Required Verdict Checks**:
- @validator: "APPROVED" or "All tests passed" or "Ready"
- @advisor: "APPROVED" or "Ready for submission" or "Meets standards"
- If "NEEDS REVISION" or "REJECTED" → Cycle NOT complete, send back

**Director Enforcement**: If verdict < 300 chars → Query for details

---

## Parallel Work Patterns

### Pattern 1: Background in Parallel
```
While @modeler + team work on Model 1:
  → @writer drafts Introduction, Background, Assumptions
```

### Pattern 2: Multiple Models in Parallel
```
If requirements independent:
  → @modeler designs Model A + B simultaneously
  → @feasibility_checker checks both
  → @data_engineer prepares features for both
  → @code_translator implements sequentially/parallel
```

### Pattern 3: Early Review
```
After first major section:
  → @advisor reviews draft
  → Feedback informs remaining work
```

---

## Multi-Agent Rework and Decision Tree

### Multi-Agent Rework

**Scenario**: Validation gate completes with multiple NEEDS_REVISION

```
@feasibility_checker: NEEDS_REVISION
@advisor: NEEDS_REVISION
@data_engineer: FEASIBLE 8/10
@code_translator: APPROVED

YOU MUST:
1. Identify ALL agents with NEEDS_REVISION
2. Send parallel revision requests to ALL
3. Wait for ALL to complete
4. Send ALL for re-verification
5. Proceed only when ALL approve
```

**Decision Tree**:
```
Validation Gate → Collect verdicts
  0 agents NEEDS_REVISION → Proceed
  1 agent → Single-agent rework
  2-3 agents → Multi-agent parallel rework
  4+ agents → Consider rewind
```

**Required Verdict Checks**:
- @validator: "APPROVED" or "All tests passed" or "Ready"
- @advisor: "APPROVED" or "Ready for submission" or "Meets standards"
- If "NEEDS REVISION" or "REJECTED" → Cycle NOT complete, send back

---

## Completion Report Format

**Mandatory format for agent phase completion reports**:

```markdown
Director, Phase {X} COMPLETE.
## Timing
Phase: {X} ({name}) | Start: {ISO} | End: {ISO} | Duration: {XX}m | Expected: {min}-{max}m
## Deliverables
Output: {list} | Status: SUCCESS/PARTIAL/FAILED
## Self-Assessment
Quality: HIGH/MEDIUM/LOW | Confidence: {1-10} | Issues: {list or "None"}
```

---

## Director Time Validation Call

**BLOCKING TIME GATE prompt template**:

```
@time_validator: Phase Time Check (BLOCKING TIME GATE)
Phase: {X} ({name}) | Agent: @{agent} | Duration: {XX}m | MINIMUM: {YY}m
Cumulative Total: {ZZ}m / 480m (8-hour minimum)
Check: 1. Query output/implementation/logs/phase_{X}_timing.json 2. Compare vs logged 3. Validate against MINIMUM (no threshold buffer)
ENFORCEMENT: Duration < MINIMUM = REJECT + FORCE RERUN (workflow does NOT stop)
Return: APPROVE / REJECT_INSUFFICIENT_TIME / INVESTIGATE
```

---

## Consultation Export Template

**Path**: `output/docs/consultations/phase_{X}_{agent}_{YYYY-MM-DDTHH-MM-SS}.md`

**Template**:
```markdown
# Phase {X} Consultation: @{agent_name}
**Timestamp**: {ISO} | **Phase**: {X} - {name} | **Duration**: {XX} min

## Work Summary
{Brief description}

## Deliverables
- {file1}: {description}

## Key Decisions
1. {Decision + rationale}

## Issues
- {Issue}: {Resolution}

## Recommendations for Next Phase
{What next agent needs}

## Self-Assessment
Confidence: {1-10} | Completeness: {%} | Rigor: HIGH/MEDIUM/LOW
```

---

## Checkpoint Tracking

**VERSION_MANIFEST.json checkpoint format for Phase 7 sub-phases**:

```json
{ "phase_7a": {"status": "completed", "timestamp": "..."}, "phase_7b": {"status": "in_progress"} }
```

**Resume**: On timeout, check VERSION_MANIFEST.json → resume from last completed sub-phase.

---

## Orchestration Log Examples

**CORRECT behavior** (update after each phase):
```
Phase 0 completes → Director updates orchestration_log.md (Phase 0 row: COMPLETE) → THEN calls Phase 0.2
Phase 0.2 completes → Director updates orchestration_log.md (Phase 0.2 row: COMPLETE) → THEN calls Phase 0.5
```

**WRONG - will be REJECTED** (batch updates):
```
Phase 0 completes → Phase 0.2 completes → Phase 0.5 completes → Director batch updates all three
❌ REJECTED: Phases 0, 0.2, 0.5 were not individually logged
```

---

## Timestamps from Timing Log

**Timestamps MUST come from timing logs, NOT be manually typed**:

```bash
# After phase ends, read the timing log
cat output/implementation/logs/phase_0_timing.json
# Output: {"start_time": "2026-01-31T08:00:12", "end_time": "2026-01-31T08:35:47", "duration_minutes": 35.58, ...}
# Use THESE values in orchestration_log.md
```

**REJECT CONDITIONS**:
- Timestamps in orchestration_log.md that don't match timing JSON = FRAUD
- Timing JSON doesn't exist = PROTOCOL VIOLATION (Director skipped time_tracker.py)
- Manually typed timestamps (e.g., `2026-01-31T08:00:00` round numbers) = SUSPICIOUS

---

## Issue Tracking Format

**Format for `output/docs/known_issues.md`**:

```markdown
# Known Issues

## [Issue ID] - Brief Title
**Phase**: X.X
**Timestamp**: YYYY-MM-DD HH:MM
**Trigger**: What caused this issue
**Automatic Action**: Rule applied (1-4)
**Workaround**: What was done
**Impact**: Low/Medium/High (blocks submission?)
**Status**: Mitigated/Monitoring/Resolved
```

**Purpose**: Enables full autonomy by documenting issues instead of stopping to ask user.

---

*This file is a companion to CLAUDE.md. Refer to the main documentation for operational protocols, phase workflows, and validation gate procedures.*
