# Re-verification Strict Standards (v2.5.5)

> **Critical Enhancement**: v2.5.5
> **Purpose**: Prevent lazy approvals during re-verification
> **Status**: MANDATORY for all validation gates

---

## Problem Statement

**Issue Discovered**:
```
Re-verification frequently passes on first attempt with minimal review:

Validator (first round): "NEEDS_REVISION: Issues X, Y, Z"
After rework:
Validator (re-verification): "✅ APPROVED - Looks good, fixed."

Problem: "Looks good" provides no evidence of thorough checking.
       Validator spent 30 seconds instead of 5 minutes.
       Quality issues may persist.
```

**Root Cause**:
- No standard for re-verification thoroughness
- Validators treat re-verification as formality
- No requirement to provide evidence
- Easy to give lazy approval

**Impact**:
- Quality issues persist through to final output
- Validation gates become ineffective
- Competition score suffers

---

## Solution: Strict Re-verification Standards

### Core Principle

**Re-verification Must Be Equally or More Strict Than Initial Validation**

Validators MUST assume "issues likely remain" until proven otherwise.

---

## Approval Standards

### ❌ FORBIDDEN: Lazy Approvals

**One-sentence approvals** (INSUFFICIENT):
```
✅ "Looks good, approved."
✅ "Fixed the issues, good to go."
✅ "Changes look fine, proceed."
✅ "All set, no problems found."
✅ "Approved, thanks for the fixes."
```

**Vague approvals** (INSUFFICIENT):
```
✅ "The revisions address my concerns, approved."
✅ "Good work on the revisions, I'm satisfied."
✅ "Everything looks better now, approved."
```

### ✅ REQUIRED: Detailed Evidence-Based Approvals

**Minimum requirements**:
- At least 3 sentences
- Specific evidence of checking
- Reference to specific files/sections/lines
- Clear reasoning for approval

**Template**:
```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. [Issue 1 description]
2. [Issue 2 description]
3. [Issue 3 description]

### Verification Process
I verified the following:

**Issue 1**: [Checker re-verified specific location]
- Checked: [Specific file, line numbers]
- Evidence: [What I found]
- Status: ✅ RESOLVED

**Issue 2**: [Checker re-verified specific location]
- Checked: [Specific file, section]
- Evidence: [What I found]
- Status: ✅ RESOLVED

**Issue 3**: [Checker re-verified specific location]
- Checked: [Specific calculation, test]
- Evidence: [What I found]
- Status: ✅ RESOLVED

### Regression Check
I also verified that:
- [Check 1: No new issues introduced]
- [Check 2: Previously working parts still work]
- [Check 3: No side effects from changes]

### Conclusion
All issues resolved, no regressions detected. **APPROVED**.
```

**Concrete examples**:

#### Example 1: Model Design Re-verification

```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. Equation (1) uses undefined symbol $\theta$
2. Complexity analysis missing for Model 2
3. Assumption 4 lacks justification

### Verification Process

**Issue 1**: Undefined symbol $\theta$
- Checked: output/model/model_design_1.md, lines 45-67
- Evidence: Equation (1) now includes "$\theta \in \mathbb{R}^p$ is the parameter vector"
- Status: ✅ RESOLVED

**Issue 2**: Missing complexity analysis
- Checked: output/model/model_design_2.md, section "Complexity Analysis"
- Evidence: Added Big-O analysis: "Time: O(n^2p), Space: O(np)"
- Status: ✅ RESOLVED

**Issue 3**: Assumption 4 lacks justification
- Checked: output/model/model_design_1.md, lines 120-125
- Evidence: Added: "Justification: Required for identifiability; see Gelman et al. (2020)"
- Status: ✅ RESOLVED

### Regression Check
I also verified that:
- Model 1's core equations unchanged (verified line 40-50)
- Model 3's solution method still valid (checked section 5)
- No new undefined symbols introduced

### Conclusion
All 3 issues resolved, no regressions detected. **APPROVED**.
```

#### Example 2: Code Implementation Re-verification

```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. Model uses sklearn instead of designed PyMC
2. Sampling iterations reduced from 10000 to 1000
3. Missing feature: NOC mapping

### Verification Process

**Issue 1**: Wrong library (sklearn vs PyMC)
- Checked: implementation/code/model_1.py, lines 1-15
- Evidence: Imports now include "import pymc as pm; import arviz as az"
- Verified: Model defined using pm.Model() context (line 25)
- Status: ✅ RESOLVED

**Issue 2**: Sampling iterations
- Checked: implementation/code/model_1.py, line 85
- Evidence: "trace = pm.sample(10000, tune=2000, target_accept=0.95)"
- Verified: 10000 samples as designed (not 1000)
- Status: ✅ RESOLVED

**Issue 3**: Missing NOC mapping
- Checked: implementation/code/data_prep_1.py, lines 45-60
- Evidence: Added function "create_noc_mapping(hosts_df)" (line 47)
- Verified: Mapping applied in main pipeline (line 155)
- Status: ✅ RESOLVED

### Regression Check
I also verified that:
- Code compiles without errors (ran syntax check)
- Previous features still work (checked data loading, preprocessing)
- No new bugs introduced (reviewed diff between versions)

### Conclusion
All 3 issues resolved, code matches design. **APPROVED**.
```

#### Example 3: Paper Quality Re-verification

```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. Grammar errors in Section 3 (lines 45-67)
2. Table 2 doesn't match features_core.csv
3. Equation (1) references undefined symbol

### Verification Process

**Issue 1**: Grammar errors
- Checked: output/paper/paper_2.tex, lines 45-67
- Evidence:
  - Line 48: Added missing article "the"
  - Line 52: Fixed verb tense "shows" → "showed"
  - Line 61: Corrected subject-verb agreement
- Status: ✅ RESOLVED

**Issue 2**: Table 2 data mismatch
- Checked: output/paper/paper_2.tex, Table 2 (line 180)
- Compared to: implementation/data/features_core.csv
- Evidence:
  - Table shows mean GDP = 12500 (was 15000 incorrectly)
  - CSV shows mean GDP = 12500 → MATCH
  - All 5 table rows now match CSV values
- Status: ✅ RESOLVED

**Issue 3**: Undefined symbol in equation
- Checked: output/paper/paper_2.tex, Equation (1) (line 95)
- Evidence: Added "$\theta_i$ is the coach effectiveness parameter"
- Status: ✅ RESOLVED

### Regression Check
I also verified that:
- No new formatting errors introduced (checked compilation log)
- Previously correct tables unchanged (spot-checked Table 1)
- Paper still compiles successfully (verified PDF generation)

### Conclusion
All 3 issues resolved, paper quality maintained. **APPROVED**.
```

---

## Re-verification Protocol

### Step 1: Receive Re-verification Request

When Director sends re-verification request, it will include:
- Original issues raised
- Revisions made
- Files to check

### Step 2: Systematic Verification

For EACH original issue:

1. **Locate the fix**:
   - Find specific file, section, line numbers
   - Identify what was changed

2. **Verify the fix**:
   - Read the revised content
   - Check if it actually addresses the issue
   - Confirm it's correct

3. **Document evidence**:
   - What specific text/code did you check?
   - What did you find?
   - Is it resolved or not?

### Step 3: Regression Check

After verifying all issues, also check:
- [ ] No new issues introduced in revised sections
- [ ] Previously working parts still work
- [ ] No side effects from changes
- [ ] No inconsistencies with other parts

### Step 4: Provide Verdict

**If ALL issues resolved AND no regressions**:
```
✅ APPROVED with detailed evidence (see templates above)
```

**If ANY issue not resolved**:
```
❌ NEEDS_REVISION with specific details:
- Issue X still not resolved: [explain what's wrong]
- Issue Y partially resolved: [explain what's missing]
- Suggestion: [specific action to fix]
```

**If regressions detected**:
```
❌ NEEDS_REVISION with specific details:
- New issue detected: [describe regression]
- Location: [specific file/lines]
- Suggestion: [specific action to fix]
```

---

## Director Enforcement

### Mandatory Checks

When @director receives re-verification verdict:

**Check 1: Verdict Length**
```python
if len(verdict) < 300 characters:  # ~3 sentences
    # Suspiciously short
    director_query_for_details()
```

**Check 2: Evidence Presence**
```python
if "checked:" not in verdict.lower():
    # No evidence of checking
    director_query_for_details()

if "evidence:" not in verdict.lower():
    # No evidence provided
    director_query_for_details()
```

**Check 3: Specificity**
```python
if "line" not in verdict and "section" not in verdict:
    # No specific locations mentioned
    director_query_for_details()
```

### Director Query Template

```
@validator:

Your re-verification approval is too brief.

You provided: "[original verdict]"

I need detailed evidence:

For EACH original issue:
- What specific file/section/lines did you check?
- What did you find? (Quote the relevant content)
- Is it resolved? (YES/NO with evidence)

For regression check:
- What did you check for regressions?
- Did you find any? (YES/NO with evidence)

Please provide a detailed re-verification report using this format:
[See template above]
```

---

## Quality Metrics

### Validator Performance Tracking

@director should track for each validator:

| Metric | Target | Action if Below Target |
|--------|--------|------------------------|
| **Re-verification time** | > 3 minutes | Query for thoroughness |
| **Verdict length** | > 300 chars | Query for details |
| **Specific locations mentioned** | >= 3 | Require specificity |
| **Evidence citations** | >= 3 | Require evidence |
| **Regression check** | Present | Require regression check |

---

## Anti-Patterns to Avoid

❌ **WRONG**: Quick approval without checking
```
"@validator, please re-verify the revisions."
→ "✅ Approved, looks good!"
```
✅ **CORRECT**: Thorough evidence-based approval
```
"@validator, please re-verify the revisions."
→ "## Re-verification Verdict: ✅ APPROVED
   ### Verification Process
   **Issue 1**: Checked lines 45-67, found [specific evidence], RESOLVED
   **Issue 2**: Checked Table 2, compared to CSV, values match, RESOLVED
   ### Regression Check
   - Verified no new issues in revised sections
   - Confirmed previous features still work
   ### Conclusion
   All issues resolved, no regressions. APPROVED."
```

❌ **WRONG**: Assume fixes are correct without verifying
```
"The author said they fixed it, so I'll approve."
```
✅ **CORRECT**: Verify each fix personally
```
"I personally checked the revised code at line 85 and confirmed
 it now uses pm.sample(10000) as designed."
```

❌ **WRONG**: Skip regression check
```
"All original issues fixed, approved."
```
✅ **CORRECT**: Always check for regressions
```
"All original issues fixed. I also verified that:
 - No new bugs introduced in revised code
 - Previously working features still function
 - No side effects detected
Approved."
```

---

## Testing Checklist

Before implementing, verify:

- [ ] Forbidden approval patterns documented
- [ ] Required approval templates created
- [ ] Re-verification protocol specified
- [ ] Director enforcement checks defined
- [ ] Query template created
- [ ] Quality metrics defined
- [ ] Anti-patterns documented

---

## Integration with Existing Protocols

### Update Multi-Agent Rework Protocol

**v2.5.4**:
```
Wait for ALL re-verifications to complete
If ALL approve → proceed
```

**v2.5.5**:
```
Wait for ALL re-verifications to complete

For each re-verification:
  Check length >= 300 chars
  Check for evidence citations
  Check for specific locations
  If any check fails → Query for details

If ALL have detailed approvals → proceed
```

### Update Editor Feedback Enforcement

**v2.5.4**:
```
Send to @editor for re-verification
If approved → proceed
```

**v2.5.5**:
```
Send to @editor for re-verification

Check @editor's verdict:
  - Has at least 3 sentences? YES/NO
  - Lists specific checks? YES/NO
  - Provides evidence? YES/NO

If ALL YES → proceed
If any NO → Query for detailed re-verification
```

---

**Document Version**: v2.5.5
**Created**: 2026-01-17
**Status**: MANDATORY for all validation gates
