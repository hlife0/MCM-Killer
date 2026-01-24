# Protocol 26: Mock Court Rewind (Protocol 13 - DEFCON 1)

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Protocol Number**: 13
> **Trigger**: Phase 9.1 REJECT signal
> **Severity**: CRITICAL - Emergency response

---

## Purpose

When @judge_zero REJECTs a paper, trigger **DEFCON 1** state:
- All forward progress stops
- System enters "repair mode"
- All agents focus on fixing Kill List items
- Only when @judge_zero approves does system exit DEFCON 1

This is the "red-blue team confrontation" mechanism - only perfect papers survive.

---

## Trigger Conditions

**Trigger**: Phase 9.1 outputs:
```
Verdict: REJECT
Score: X/100 (<95 or Fatal Flaw)
```

**Agent**: @judge_zero

**Output**: `output/docs/validation/judgment_report.md` with Kill List

---

## DEFCON 1 State Machine

```
[NORMAL] → (REJECT detected) → [DEFCON 1]
    ↓
[Ticket Generation] → [Repair Execution] → [Re-Judging]
    ↓                           ↓
[PASS] → [NORMAL]         [REJECT] → Loop (max 3)
                                      ↓
                              [Mercy Rule Override]
```

---

## Step 1: Declare DEFCON 1

**Action**: @director broadcasts emergency state

**Message Template**:
```
⚠️  DEFCON 1 DECLARED ⚠️

Trigger: Phase 9.1 REJECT (Score: X/100)

Action: All agents HALT forward progress.
System entering "Repair Mode".

Next: Review judgment_report.md for Kill List.
```

---

## Step 2: Generate Tickets

**Parse Kill List** from `judgment_report.md`

**Ticket Format**:
```markdown
## Ticket #1: [Issue Name] (CRITICAL)
- **Severity**: Fatal / Level 2 / Level 3
- **Assigned To**: [Agent Name]
- **Deadline**: [Time estimate]
- **Requirement**: [What must be done?]
- **Current**: [Current bad state]
- **Target**: [Target good state]
```

**Ticket Assignment**:

| Issue Type | Assigned To | Typical Deadline |
|------------|-------------|-----------------|
| Abstract空洞 (no numbers) | @writer | 30 min |
| Figure caption non-descriptive | @visualizer | 20 min |
| Missing sensitivity analysis | @modeler + @writer | 2 hours |
| Missing uncertainty quantification | @writer + @validator | 1 hour |
| Physical impossibility (p > 1) | @modeler | 1 hour |
| Poor formatting | @editor | 30 min |

---

## Step 3: Execute Repairs

### Constraints During DEFCON 1

✅ **ALLOWED**:
- Fix items in Kill List
- Revise specific sections
- Add missing content
- Improve existing content

❌ **FORBIDDEN**:
- New features
- Exploratory analysis
- Model changes (unless Fatal flaw requires)

**@director Enforcement**:
- Monitor agent activities
- Block any non-essential work
- Track ticket completion

---

## Step 4: Re-Judging

**After all tickets complete**:

1. **Re-run Phase 9.1**: Invoke @judge_zero again
2. **Generate new** `judgment_report.md`
3. **Check status**:
   - **PASS**: Score ≥ 95, no Fatal Flaws → Exit DEFCON 1
   - **REJECT**: Score < 95 or Fatal Flaw → Continue DEFCON 1

---

## Step 5: Mercy Rule (Anti-Infinite Loop)

**Trigger**: REJECT occurs 3 times consecutively

**Options**:

**Option A**: Force Conditional Pass
- **Requirement**: Document all unresolved flaws in Phase 11
- **Condition**: Score ≥ 80 (but < 95)
- **Approval**: Manual override by @director

**Option B**: Continue Attempting
- **Risk**: Infinite loop possible
- **Benefit**: May achieve PASS eventually

**Decision Framework**:
```
IF (reject_count >= 3 AND score >= 80):
    Consider: "Is this paper good enough to submit?"
    IF (major_fatal_flaws == 0):
        Approve Conditional Pass
        Log unresolved issues in Phase 11
    ELSE:
        Continue attempting
ELSE:
    Continue attempting
```

---

## DEFCON 1 Log Template

**File**: `output/docs/DEFCON_1_LOG.md`

```markdown
# DEFCON 1 Log

**Declaration**: [Timestamp]
**Trigger**: Phase 9.1 REJECT (Score: X/100)

---

## Active Tickets (N Total)

### Ticket #1: [Issue] (CRITICAL)
- **Assigned To**: @agent
- **Status**: ⏳ In Progress / ✅ Complete
- **Fix**: [What was done]

---

## Progress
- [x] Ticket #1 Complete
- [x] Ticket #2 Complete
- [ ] Ticket #3 Complete

---

## Status: ACTIVE
**Attempts**: 1/3 (Mercy Rule at 3)
**Duration**: [Time elapsed]
**Next Action**: [What's next?]
```

---

## Exit Conditions

**System exits DEFCON 1 when**:
- [ ] @judge_zero returns PASS (Score ≥ 95)
- [ ] @director approves Conditional Pass (Mercy Rule)

**System resumes normal workflow**:
- Proceed to Phase 9.5 (Final Package)
- Document DEFCON 1 duration in Phase 11

---

## Quality Assurance

### Verification Checklist

During DEFCON 1, verify:

- [ ] DEFCON 1 properly declared
- [ ] All Kill List items have tickets
- [ ] Tickets assigned to correct agents
- [ ] No new features being developed
- [ ] @director monitoring active
- [ ] Log file maintained

### Test Case

**Scenario**: Paper rejected for abstract空洞 (no numbers)

**Expected Flow**:
1. @judge_zero: REJECT (Score: 45/100)
2. @director: Declares DEFCON 1
3. @director: Generates Ticket #1 (@writer, add numbers)
4. @writer: Adds RMSE=4.2, R²=0.89
5. @director: Ticket complete, re-trigger @judge_zero
6. @judge_zero: PASS (Score: 97/100)
7. @director: Exit DEFCON 1

**Time**: ~1 hour total

---

## Examples

### Example 1: Successful DEFCON 1 (1 iteration)

```
[16:00] Phase 9.1: REJECT (Score: 45/100)
Kill List: Abstract空洞 (0 numbers)

[16:05] @director: DEFCON 1 declared
[16:10] Ticket created: @writer to add numbers
[16:35] @writer: Complete (added RMSE=4.2, R²=0.89, p<0.001)
[16:40] All tickets complete

[16:45] Phase 9.1 re-run: PASS (Score: 97/100)
[16:50] DEFCON 1 exited

Duration: 50 minutes
```

### Example 2: DEFCON 1 with Mercy Rule (3 iterations)

```
[14:00] Phase 9.1: REJECT (Score: 78/100)

Iteration 1:
- [14:10] DEFCON 1 declared
- [15:30] Fix attempt 1 complete
- [15:45] Phase 9.1 re-run: REJECT (Score: 82/100)

Iteration 2:
- [15:50] Fix attempt 2 complete
- [16:25] Phase 9.1 re-run: REJECT (Score: 85/100)

Iteration 3:
- [16:30] Fix attempt 3 complete
- [17:05] Phase 9.1 re-run: REJECT (Score: 86/100)

[17:10] Mercy Rule triggered
- Score: 86 ≥ 80 (meets threshold)
- Major fatal flaws: 0 (only Level 2/3 flaws remaining)
- @director: Approve Conditional Pass

[17:15] DEFCON 1 exited (Conditional)
- Unresolved issues documented in Phase 11
```

---

## Impact

**Without Protocol 13**:
- Papers with flaws submitted
- Lower O-Prize chances
- Post-mortem analysis (too late)

**With Protocol 13**:
- Flawed papers caught before submission
- Forced improvement via DEFCON 1
- Only perfect papers survive
- Higher O-Prize chances

**Value**: **Prevents submission failure.**

---

## Risks & Mitigation

### Risk 1: Infinite DEFCON 1 Loop

**Problem**: Paper keeps failing @judge_zero review

**Mitigation**: Mercy Rule (max 3 attempts)

### Risk 2: Over-Engineering During Repairs

**Problem**: Agents add new features instead of fixing issues

**Mitigation**: @director strict enforcement of "no new features" rule

### Risk 3: Extended Time Impact

**Problem**: DEFCON 1 takes too long (4-5 hours)

**Mitigation**:
- Time cap: Max 3 iterations
- At 3 hours: Force decision (Conditional Pass or Abort)

---

## Dependencies

**Trigger**: Phase 9.1 REJECT
**Agents Involved**: All agents (depending on Kill List)
**Exit Condition**: @judge_zero PASS or Mercy Rule approval
**Logging**: `output/docs/DEFCON_1_LOG.md`

---

## Related Protocols

- **Protocol 9**: @validator/@advisor Brief Format (judgment report format)
- **Protocol 14**: Academic Style Alignment (prevents many rejections)
- **Protocol 15**: Interpretation over Description (prevents abstract空洞)

---

**Document Version**: v3.1.0
**Protocol Type**: Critical - Emergency Response
**Impact**: Prevents submission failure
**Status**: Ready for Implementation
