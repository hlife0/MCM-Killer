# All Agents Re-verification Protocol (v2.5.5)

> **Critical Enhancement**: v2.5.5
> **Purpose**: Ensure ALL relevant agents participate in re-verification, preventing quality regression
> **Status**: MANDATORY for all validation gates

---

## Problem Statement

**Issue Discovered**:
```
MODEL Validation Gate results:
  @researcher:          ✅ APPROVED
  @feasibility_checker: ⚠️ NEEDS_REVISION (time too long)
  @data_engineer:       ✅ APPROVED
  @code_translator:     ✅ APPROVED
  @advisor:             ⚠️ NEEDS_REVISION (causal claims too strong)

Current (v2.5.4) behavior:
  Rework sent to: @feasibility_checker and @advisor
  Re-verification sent to: @feasibility_checker and @advisor

Problem: @researcher, @data_engineer, @code_translator
         do NOT see the revisions.
         Risk: Revisions may break what they approved.

Example scenario:
  @feasibility_checker simplifies model to reduce time
  @code_translator already approved implementation plan
  After revision: Implementation no longer matches!
  @code_translator never sees the change → approves old plan
  Result: Design-implementation mismatch
```

**Root Cause**:
- v2.5.4 protocol: "Only agents who rejected need to re-verify"
- Missing: "Agents who approved must verify revisions don't break their approval"

**Impact**:
- Quality regression: Changes break previously approved work
- Inconsistencies between models, code, data
- Wasted validation effort

---

## Solution: All Relevant Agents Re-verify

### Core Principle

**Re-verification Involves ALL Relevant Agents, Not Just Those Who Rejected**

**Relevant Agents =**
- **Primary agents**: Those who made revisions (rejected → fixed)
- **Secondary agents**: Those who approved original work
- **Re-verification set**: Primary ∪ Secondary = ALL relevant agents

---

## Protocol

### Step 1: Initial Validation (Same as v2.5.4)

```
Validation Gate completes
  ↓
Collect ALL agent verdicts
  ↓
Identify agents needing rework:
  - NEEDS_REVISION
  - CRITICAL_ISSUES
```

### Step 2: Parallel Rework (Same as v2.5.4)

```
Send revision requests to ALL agents who rejected
  ↓
Wait for ALL to complete revisions
```

### Step 3: Determine Re-verification Set (NEW)

```python
# Identify ALL agents who should re-verify

primary_agents = [agent for agent in validation_results
                  if "NEEDS_REVISION" in agent.verdict or
                     "CRITICAL" in agent.verdict]

secondary_agents = [agent for agent in validation_results
                    if "APPROVED" in agent.verdict or
                       "CONDITIONAL" in agent.verdict]

reverification_set = primary_agents + secondary_agents  # ALL agents
```

**Example**:
```
Original validation:
  @researcher:          APPROVED     → Secondary
  @feasibility_checker: NEEDS_REVISION → Primary
  @data_engineer:       APPROVED     → Secondary
  @code_translator:     APPROVED     → Secondary
  @advisor:             NEEDS_REVISION → Primary

Re-verification set:
  Primary:   @feasibility_checker, @advisor
  Secondary: @researcher, @data_engineer, @code_translator
  Total:     ALL 5 agents
```

### Step 4: Send to ALL for Re-verification (NEW)

```python
for agent in reverification_set:
    if agent in primary_agents:
        # Primary: Re-verify your own revisions
        request = f"""
        Director: Please re-verify your revisions.

        Original issues:
        {format_original_issues(agent)}

        Revisions you made:
        {format_revisions(revisions[agent])}

        Please verify:
        1. All issues fully resolved
        2. No regressions introduced
        3. Changes are consistent

        Provide detailed verdict with evidence.
        """
    else:  # Secondary
        # Secondary: Re-verify others' revisions
        request = f"""
        Director: Please re-verify revisions made by other agents.

        You originally APPROVED this work.

        Agents who made revisions:
        {list(primary_agents)}

        Summary of changes:
        {format_revision_summary(all_revisions)}

        Please verify:
        1. Revisions do NOT break what you approved
        2. Changes are consistent with your requirements
        3. No new issues introduced

        Provide detailed verdict with evidence.
        """

    send_to_agent(agent, request)
```

**Example Re-verification Requests**:

#### For Primary Agent (@feasibility_checker):
```
@feasibility_checker:

Director: Please re-verify your revisions.

Original issues (from MODEL validation):
1. Computational time 6-10h is too long
   - Suggestion: Use frequentist + bootstrap instead of MCMC

Revisions you made:
- Changed approach in output/model/feasibility_2.md
- From: Full Bayesian MCMC
- To: Frequentist ZINB + bootstrap CI
- New time estimate: 2-3 hours

Please verify:
1. [ ] Time issue fully resolved (2-3h is acceptable)
2. [ ] Method still valid for problem (frequentist appropriate)
3. [ ] No new issues introduced (approach still sound)

Provide detailed verdict with evidence.
```

#### For Secondary Agent (@code_translator):
```
@code_translator:

Director: Please re-verify revisions made by other agents.

You originally APPROVED this work with comment:
"IMPLEMENTABLE: PyMC recommended, 22-28h coding time"

Agents who made revisions:
- @feasibility_checker: Changed from Bayesian MCMC to frequentist
- @advisor: Softened causal language

Summary of changes:
- Model approach changed: PyMC MCMC → statsmodels ZINB
- Implications for your implementation:
  - No longer need PyMC
  - Use statsmodels instead
  - Bootstrap for CI (no MCMC sampling)

Please verify:
1. [ ] Revised approach is still implementable
2. [ ] Your coding time estimate still valid (22-28h?)
3. [ ] Implementation plan needs updating (NEW: statsmodels, not PyMC)

Provide detailed verdict:
- If implementable: APPROVE with updated plan
- If issues: NEEDS_REVISION with specific concerns
```

### Step 5: Wait for ALL Re-verifications

```python
completed_verifications = []

while len(completed_verifications) < len(reverification_set):
    for agent in reverification_set:
        if agent not in completed_verifications:
            if check_verification_complete(agent):
                completed_verifications.append(agent)
```

**Important**: Wait for ALL agents, not just primary agents.

### Step 6: Collect All Verdicts

```python
verdicts = {}
for agent in reverification_set:
    verdicts[agent] = get_verification_verdict(agent)

# Example output:
verdicts = {
  "@feasibility_checker": "✅ APPROVED - Time reduced to 2-3h, method valid",
  "@advisor": "✅ APPROVED - Causal language softened, all issues resolved",
  "@researcher": "✅ APPROVED - Frequentist approach valid, no concerns",
  "@data_engineer": "⚠️ NEEDS_REVISION - Bootstrap requires more data prep",
  "@code_translator": "✅ APPROVED - statsmodels implementable, updated plan"
}
```

### Step 7: Make Decision

```python
def check_all_verifications(verdicts):
    """Check if ALL agents approve"""

    all_approved = True
    issues = []

    for agent, verdict in verdicts.items():
        if "APPROVED" not in verdict:
            all_approved = False
            issues.append(f"{agent}: {verdict}")

    if all_approved:
        print("ALL agents approved. Proceeding to next phase.")
        return True
    else:
        print("Some agents did NOT approve:")
        for issue in issues:
            print(f"  - {issue}")
        return False
```

**Decision Flow**:
```
ALL re-verifications complete
  ↓
Check if ALL approve
  ↓ YES              ↓ NO
Proceed to next   Check iteration count:
phase                  < 3?          ≥ 3?
                    ↓             ↓
                Loop back      Pause for
                to Step 2     user intervention
```

---

## Complete Example

### Scenario: MODEL Gate with Multiple Revisions

**Initial Validation**:
```
@researcher:          ✅ APPROVED
  "ZINB recommended, synthetic control OK"

@feasibility_checker: ⚠️ NEEDS_REVISION
  "Computational time 6-10h, use hybrid approach"

@data_engineer:       ✅ APPROVED
  "All features available in hosts_clean.csv"

@code_translator:     ✅ APPROVED
  "IMPLEMENTABLE: PyMC, 22-28h coding time"

@advisor:             ⚠️ NEEDS_REVISION
  "Causal claims too strong, soften language"
```

**Director's Response** (v2.5.5):
```
Collecting all validation feedback...

Agents needing MANDATORY rework (Primary):
1. @feasibility_checker (NEEDS_REVISION)
2. @advisor (NEEDS_REVISION)

Agents who approved (Secondary - must re-verify):
3. @researcher (APPROVED)
4. @data_engineer (APPROVED)
5. @code_translator (APPROVED)

Strategy: Parallel rework → ALL 5 agents re-verify

=== Sending revision requests ===

@feasibility_checker:
  Issue: Computational time 6-10h
  Fix: Use frequentist + bootstrap

@advisor:
  Issue: Causal claims too strong
  Fix: Soften language

=== Waiting for revisions ===
[Revisions complete]
=== Sending for re-verification (ALL 5 agents) ===
```

**Re-verification Requests**:

```
@feasibility_checker (Primary):
  "Please re-verify your revisions:
   - Changed to frequentist + bootstrap
   - New time: 2-3 hours
   Verify: Time resolved, method still valid"

@advisor (Primary):
  "Please re-verify your revisions:
   - Softened causal language in Section 4
   Verify: All concerns addressed"

@researcher (Secondary):
  "You approved: 'ZINB recommended'
   Revisions made: @feasibility_checker changed to frequentist ZINB
   Please verify: Is frequentist approach still valid?"

@data_engineer (Secondary):
  "You approved: 'All features available'
   Revisions made: @feasibility_checker added bootstrap
   Please verify: Bootstrap data requirements satisfied?"

@code_translator (Secondary):
  "You approved: 'IMPLEMENTABLE: PyMC, 22-28h'
   Revisions made: Changed from PyMC to statsmodels
   Please verify: Implementable with statsmodels? Time estimate still valid?"

=== Waiting for ALL re-verifications ===
```

**Re-verification Results**:
```
@feasibility_checker: ✅ APPROVED
  "Time reduced to 2-3h ✅
   Method still valid ✅
   Checked: feasibility_2.md, lines 45-60"

@advisor: ✅ APPROVED
  "Language softened ✅
   Checked: paper_2.tex, Section 4, lines 120-135 ✅"

@researcher: ✅ APPROVED
  "Frequentist ZINB is appropriate ✅
   Bootstrap is standard approach ✅
   No issues with method change ✅"

@data_engineer: ⚠️ NEEDS_REVISION
  "Bootstrap requires resampling data
   Current data_prep doesn't support this
   Need to add resampling functionality"

@code_translator: ✅ APPROVED
  "statsmodels is implementable ✅
   Coding time reduces to 15-20h (no PyMC setup) ✅
   Updated implementation plan provided ✅"

Status: 4/5 APPROVED, 1 NEEDS_REVISION
Action: Loop back, send to @data_engineer for additional rework
```

---

## Validation Gate Specifications

Each validation gate must define:

### 1. Primary Agents (those who can trigger rework)
- Which agents can return NEEDS_REVISION?
- What types of issues can they raise?

### 2. Secondary Agents (those who must re-verify)
- Which agents originally approved?
- What aspects need re-verification?

### 3. Re-verification Set
- Complete list: Primary + Secondary
- Unique considerations for each

### Example: MODEL Validation Gate

```markdown
## MODEL Validation Gate (Phase 1.5)

### Participants (All 5 agents)
- @researcher: Validates methodology
- @feasibility_checker: Validates time/resource feasibility
- @data_engineer: Validates data availability
- @code_translator: Validates implementability
- @advisor: Validates innovation/quality

### Re-verification Protocol

**If any agent returns NEEDS_REVISION**:

Primary agents (who rejected):
  - Those who returned NEEDS_REVISION or CRITICAL_ISSUES
  - Must re-verify their own revisions

Secondary agents (who approved):
  - @researcher: Re-verify if methodology changed
  - @data_engineer: Re-verify if data requirements changed
  - @code_translator: Re-verify if implementation approach changed
  - @advisor: Re-verify if quality/innovation claims changed

**Re-verification set**: ALL 5 agents

**Exit condition**: ALL 5 approve
```

### Example: CODE Validation Gate

```markdown
## CODE Validation Gate (Phase 4.5)

### Participants (2 agents)
- @modeler: Validates code matches design
- @validator: Validates code correctness

### Re-verification Protocol

**If any agent returns NEEDS_REVISION**:

Primary agents (who rejected):
  - @modeler: Re-verify revisions
  - @validator: Re-verify revisions

Secondary agents:
  - None (only 2 agents in this gate)

**Re-verification set**: @modeler + @validator

**Exit condition**: Both approve
```

### Example: PAPER Validation Gate

```markdown
## PAPER Validation Gate (Phase 7)

### Participants (4 agents)
- @reader: Validates requirement compliance
- @validator: Validates data consistency
- @advisor: Validates quality
- @writer: Self-validation (author)

### Re-verification Protocol

**If any agent returns NEEDS_REVISION**:

Primary agents (who rejected):
  - Those who returned NEEDS_REVISION

Secondary agents:
  - @reader: Re-verify if requirements changed
  - @validator: Re-verify if data/figures changed
  - @advisor: Re-verify if content/claims changed
  - @writer: Re-verify if LaTeX structure changed

**Re-verification set**: ALL 4 agents

**Exit condition**: ALL 4 approve
```

---

## Integration with Other Protocols

### With Multi-Agent Rework Protocol

**v2.5.4**:
```
Step 4: Parallel Rework
Step 5: Multi-Agent Re-verification (only those who rejected)
```

**v2.5.5**:
```
Step 4: Parallel Rework
Step 5: Determine Re-verification Set (Primary + Secondary)
Step 6: Send to ALL for Re-verification
Step 7: Wait for ALL re-verifications
```

### With Strict Re-verification Standards

**v2.5.5**:
- ALL agents in re-verification set must provide detailed evidence
- Lazy approvals rejected by @director
- Minimum 3 sentences, specific locations, evidence citations

---

## Anti-Patterns to Avoid

❌ **WRONG**: Only primary agents re-verify
```
Re-verification set: @feasibility_checker, @advisor (who rejected)
```
✅ **CORRECT**: All agents re-verify
```
Re-verification set: @researcher, @feasibility_checker, @data_engineer,
                    @code_translator, @advisor (ALL 5 agents)
```

❌ **WRONG**: Secondary agents skip re-verification
```
"@researcher, you approved originally, no need to re-verify."
```
✅ **CORRECT**: Secondary agents verify no regressions
```
"@researcher, you approved originally, but revisions were made.
 Please verify changes don't break what you approved."
```

❌ **WRONG**: Proceed when only primary agents approve
```
"@feasibility_checker and @advisor approved, @data_engineer still reviewing.
 Let's proceed to save time."
```
✅ **CORRECT**: Wait for ALL agents
```
"Waiting for @data_engineer's re-verification before proceeding."
```

---

## Testing Checklist

Test protocol with scenarios:

- [ ] 1 agent NEEDS_REVISION (all agents re-verify)
- [ ] 3 agents NEEDS_REVISION (all agents re-verify)
- [ ] Primary agent resolves, secondary agent finds new issue (loop correctly)
- [ ] All approve after 1 iteration (proceed)
- [ ] Some reject after 1 iteration (loop back)
- [ ] Max iterations reached (escalate to user)

---

**Document Version**: v2.5.5
**Created**: 2026-01-17
**Status**: MANDATORY for all validation gates
