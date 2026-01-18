# Feedback File Standardization Protocol (v2.5.6)

> **Purpose**: Establish systematic rules for consultation feedback file positioning and naming
> **Status**: MANDATORY for all agent consultation workflows
> **Fixes Issue**: @modeler cannot find feedback files from consulted agents

---

## Problem Summary

### v2.5.5 Issue

**Error Observed**:
```
@modeler tries to read:
  output/docs/consultations/feedback_model_1_researcher.md
  output/docs/consultations/feedback_model_1_feasibility_checker.md
  output/docs/consultations/feedback_model_1_data_engineer.md
  output/docs/consultations/feedback_model_1_code_translator.md
  output/docs/consultations/feedback_model_1_advisor.md

All return: Error: File does not exist.

Then tries:
  output/docs/consultations/feedback_researcher.md
  output/docs/consultations/feedback_feasibility_checker.md
  (etc.)

Still: Error: File does not exist.
```

**Root Causes**:
1. **No canonical path**: Different agents use different paths
2. **No enforced naming**: Inconsistent file naming
3. **No verification**: @director doesn't confirm files exist before @modeler reads them
4. **Agents may not write**: No guarantee that consulted agents actually write feedback

**Impact**:
- @modeler cannot read feedback
- Consultation mechanism fails
- Model design proceeds without expert input
- Quality suffers

---

## v2.5.6 Solution

### Canonical Path (MANDATORY)

**All consultation feedback files MUST be written to**:
```
output/docs/consultations/
```

**Rationale**:
- Consistent with other documentation (validation/, rewind/)
- Clear separation from implementation code
- Easy to find and verify

### Naming Convention (MANDATORY)

**Format**:
```
feedback_model_{model_number}_{agent_name}.md
```

**Components**:
- `feedback_model_`: Fixed prefix
- `{model_number}`: Model being reviewed (1, 2, 3, etc.)
- `{agent_name}`: Agent providing feedback (researcher, feasibility_checker, data_engineer, code_translator, advisor)
- `.md`: Markdown extension

**Examples**:
```
feedback_model_1_researcher.md
feedback_model_1_feasibility_checker.md
feedback_model_1_data_engineer.md
feedback_model_1_code_translator.md
feedback_model_1_advisor.md

feedback_model_2_researcher.md
feedback_model_2_feasibility_checker.md
(etc.)
```

**Forbidden Names** (DO NOT USE):
- ❌ `feedback_researcher.md` (missing model number)
- ❌ `feedback_model_1.md` (missing agent name)
- ❌ `consultation_researcher_model1.md` (wrong format)
- ❌ `feedback_model_1_researcher_final.md` (no suffixes)

---

## Complete Consultation Workflow (v2.5.6)

### Step 1: @modeler Writes Draft Proposal

**Action**: @modeler writes draft to `output/model_proposals/model_X_draft.md`

**Report to @director**:
```
Director, I have completed draft proposal for Model {X}.

Draft: output/model_proposals/model_{X}_draft.md

I request MANDATORY CONSULTATION from:
- @researcher
- @feasibility_checker
- @data_engineer
- @code_translator
- @advisor

Please send the draft to these agents for feedback.
```

### Step 2: @director Sends Draft to Agents (PARALLEL)

**Action**: @director calls all 5 agents in parallel

**Instructions to each agent**:
```
@{agent}, please review the draft proposal:

Input: output/model_proposals/model_{X}_draft.md

Your task: Provide feedback from your {agent} expertise perspective.

Output: output/docs/consultations/feedback_model_{X}_{agent}.md

MANDATORY: You MUST write your feedback to the specified path.
```

### Step 3: Each Agent Writes Feedback (PARALLEL)

**Action**: Each agent independently writes feedback

**Path** (MANDATORY):
```
output/docs/consultations/feedback_model_{X}_{agent}.md
```

**Format** (each agent uses their own template):
```markdown
# Feedback on Model {X} Draft - @{agent}

## Overall Assessment
- **Verdict**: [NEEDS_REVISION / ACCEPTABLE]

## Strengths
1. [Strength]

## Concerns
1. [Concern]

## Recommendations
[Specific recommendations]

## Summary
[Brief summary]
```

**Report to @director** (each agent):
```
Director, I have completed my review of Model {X} draft.

Feedback: output/docs/consultations/feedback_model_{X}_{agent}.md
Verdict: [NEEDS_REVISION / ACCEPTABLE]
Summary: [2-3 sentence assessment]
```

### Step 4: @director Verifies All Files Exist (MANDATORY)

**Action**: @director verifies all 5 feedback files exist

**Verification Command**:
```bash
# Count feedback files for model X
ls -1 output/docs/consultations/feedback_model_{X}_*.md | wc -l
```

**Expected Output**: `5`

**If count < 5**:
- Identify which agents haven't submitted
- Re-call missing agents with reminder:
  ```
  @{agent}, you haven't submitted your feedback yet.
  Please write to: output/docs/consultations/feedback_model_{X}_{agent}.md
  ```
- Wait for all 5 files to exist
- Re-verify

**If count = 5**:
- Verify each filename matches expected agent
- Proceed to Step 5

### Step 5: @director Confirms to @modeler

**Action**: @director tells @modeler all feedback is ready

**Message**:
```
@modeler, all 5 consultation feedback files have been received.

Feedback location: output/docs/consultations/feedback_model_{X}_*.md

Files:
- feedback_model_{X}_researcher.md ✅
- feedback_model_{X}_feasibility_checker.md ✅
- feedback_model_{X}_data_engineer.md ✅
- feedback_model_{X}_code_translator.md ✅
- feedback_model_{X}_advisor.md ✅

Please read all 5 feedback files and incorporate the feedback into your final design.
```

### Step 6: @modeler Reads All Feedback

**Action**: @modeler reads all 5 feedback files

**Read Commands**:
```
Read: output/docs/consultations/feedback_model_{X}_researcher.md
Read: output/docs/consultations/feedback_model_{X}_feasibility_checker.md
Read: output/docs/consultations/feedback_model_{X}_data_engineer.md
Read: output/docs/consultations/feedback_model_{X}_code_translator.md
Read: output/docs/consultations/feedback_model_{X}_advisor.md
```

**Processing**:
- Extract strengths (keep in final design)
- Extract weaknesses (fix in final design)
- Extract suggestions (incorporate if valuable)

### Step 7: @modeler Writes Final Design

**Action**: @modeler writes final design to `output/model/model_design.md`

**Must Include**:
```markdown
# Mathematical Model Design

## Consultation Summary

### Original Proposal
[Brief summary of draft]

### Feedback Received

#### @researcher
- Strengths: [list]
- Weaknesses: [list]
- Suggestions: [list]
✅ Incorporated: [what you included]

#### @feasibility_checker
- [Same format]

#### @data_engineer
- [Same format]

#### @code_translator
- [Same format]

#### @advisor
- [Same format]

### Final Design Changes
Based on feedback, I made the following changes:
1. [Change 1]
2. [Change 2]
3. [Change 3]

---
## [Rest of model design...]
```

**Report to @director**:
```
Director, I have completed the final model design.

Design: output/model/model_design.md

I incorporated feedback from all 5 consulted agents:
- @researcher: [summary of feedback]
- @feasibility_checker: [summary of feedback]
- @data_engineer: [summary of feedback]
- @code_translator: [summary of feedback]
- @advisor: [summary of feedback]

Final design is ready for feasibility assessment.
```

---

## Agent-Specific Instructions

### @modeler

**When reading feedback**:
- **ALWAYS** read from `output/docs/consultations/feedback_model_{X}_{agent}.md`
- **NEVER** read from `output/consultations/` (old path, deprecated)
- **NEVER** proceed without reading all 5 feedback files

**Incorporation Requirements**:
- MUST address all NEEDS_REVISION concerns
- SHOULD incorporate ACCEPTABLE suggestions
- MUST document what was incorporated and why

### @researcher

**When writing feedback**:
- **ALWAYS** write to `output/docs/consultations/feedback_model_{X}_researcher.md`
- MUST use the feedback template
- MUST provide specific, actionable feedback
- MUST report verdict to @director

### @feasibility_checker

**When writing feedback**:
- **ALWAYS** write to `output/docs/consultations/feedback_model_{X}_feasibility_checker.md`
- Focus on technical feasibility
- Assess computational requirements
- Verify 2-6 hour training time

### @data_engineer

**When writing feedback**:
- **ALWAYS** write to `output/docs/consultations/feedback_model_{X}_data_engineer.md`
- Focus on data availability
- Assess feature engineering feasibility
- Flag any data quality concerns

### @code_translator

**When writing feedback**:
- **ALWAYS** write to `output/docs/consultations/feedback_model_{X}_code_translator.md`
- Focus on mathematical implementation
- Assess computational complexity
- Verify formulas are implementable

### @advisor

**When writing feedback**:
- **ALWAYS** write to `output/docs/consultations/feedback_model_{X}_advisor.md`
- Focus on O-Prize competitiveness
- Assess sophistication level
- Identify weaknesses and suggest improvements

### @director

**Verification Responsibilities**:
1. Send draft to all 5 agents in parallel
2. Wait for all 5 to complete
3. Verify all 5 files exist in `output/docs/consultations/`
4. Only then tell @modeler to read feedback
5. Track which agents haven't submitted
6. Re-call missing agents if needed

---

## File Path Reference

| Purpose | Path | Format |
|---------|------|--------|
| **Draft Proposal** | `output/model_proposals/` | `model_{X}_draft.md` |
| **Feedback Files** | `output/docs/consultations/` | `feedback_model_{X}_{agent}.md` |
| **Final Design** | `output/model/` | `model_design.md` |
| **Feasibility Report** | `output/model/` | `feasibility_{i}.md` |

---

## Troubleshooting

### Issue: File Not Found

**Symptom**: @modeler gets "Error: File does not exist"

**Diagnosis**:
```bash
# Check if file exists
ls -la output/docs/consultations/feedback_model_1_*.md

# Expected: 5 files
# If < 5: Some agents haven't written feedback
```

**Solution**:
1. @director checks which agents haven't submitted
2. @director re-calls missing agents
3. Wait for all 5 files to exist
4. @modeler tries again

### Issue: Wrong Path

**Symptom**: Agent writes to wrong location

**Solution**:
1. @director verifies correct path in instructions
2. Re-send instructions with explicit path
3. Agent writes to correct path
4. Verify file exists

### Issue: Wrong Naming

**Symptom**: File exists but with wrong name

**Solution**:
1. Agent renames file to correct format
2. OR agent rewrites to new file with correct name
3. Verify all 5 files follow naming convention

---

## Verification Checklist

Before deploying v2.5.6, verify:

- [ ] Canonical path documented: `output/docs/consultations/`
- [ ] Naming convention documented: `feedback_model_{X}_{agent}.md`
- [ ] All agents updated with correct paths
- [ ] @modeler reads from correct location
- [ ] All consulted agents write to correct location
- [ ] @director verifies files exist before @modeler reads them
- [ ] Troubleshooting guide documented
- [ ] File path reference table created

---

**Document Version**: v2.5.6
**Created**: 2026-01-18
**Status**: MANDATORY for all consultation workflows
