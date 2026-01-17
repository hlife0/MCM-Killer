# Multi-Agent Parallel Rework Protocol (v2.5.4)

> **Critical Enhancement**: v2.5.4
> **Purpose**: Fix multi-agent rework coordination failures
> **Status**: MANDATORY for all validation gates

---

## Problem Statement

**Issue Discovered**:
```
Validation Gate results:
  @feasibility_checker: NEEDS_REVISION
  @advisor: NEEDS_REVISION
  @data_engineer: FEASIBLE 8/10
  @code_translator: APPROVED

Current (WRONG) behavior:
  "Now sending to @feasibility_checker for re-verification"

Expected (CORRECT) behavior:
  "Sending to BOTH @feasibility_checker AND @advisor for parallel rework"
```

**Impact**:
- Some agents' feedback never addressed
- Incomplete fixes
- Validation gate purpose defeated
- Quality issues persist

---

## Root Cause Analysis

### Old Protocol (v2.5.3) Limitations

**Assumption**: Only one agent would return NEEDS_REVISION at a time.

**Reality**: Multiple agents often identify different issues simultaneously.

**Missing Mechanism**:
1. No parallel rework coordination
2. No multi-agent re-verification
3. Director must manually choose which agent to send back to

---

## Solution: Enhanced Multi-Agent Rework Protocol

### Protocol Overview

```
Validation Gate completes
    ↓
Collect ALL agent verdicts
    ↓
Identify ALL agents returning NEEDS_REVISION/CRITICAL
    ↓
Determine rework strategy:
  - 1 agent → Standard rework
  - 2-3 agents → Parallel rework
  - 4+ agents → Consider rewind
    ↓
Send revision requests to ALL identified agents (in parallel)
    ↓
Wait for ALL agents to complete revisions
    ↓
Send ALL to relevant validators for RE-VERIFICATION
    ↓
Wait for ALL re-verifications to complete
    ↓
Check if ALL approve:
  - YES → Proceed to next phase
  - NO → Loop back (max 3 iterations)
```

---

## Implementation Details

### Step 1: Collect All Verdicts

After validation gate completes, Director MUST collect all verdicts:

```python
# Pseudocode
validation_results = {
  "@feasibility_checker": {
    "verdict": "NEEDS_REVISION",
    "issues": ["Computational time 6-10h", "Use hybrid approach"]
  },
  "@advisor": {
    "verdict": "NEEDS_REVISION",
    "issues": ["Causal claims too strong", "7.5/10 potential"]
  },
  "@data_engineer": {
    "verdict": "CONDITIONAL",  # FEASIBLE 8/10
    "issues": ["NOC mapping required"]
  },
  "@code_translator": {
    "verdict": "APPROVED",
    "issues": []
  }
}
```

### Step 2: Identify Agents Needing Rework

```python
# Identify agents that NEED revision
rework_agents = []
for agent, result in validation_results.items():
    if "NEEDS_REVISION" in result["verdict"] or "CRITICAL" in result["verdict"]:
        rework_agents.append(agent)

# Result: ["@feasibility_checker", "@advisor"]

# Note: @data_engineer is CONDITIONAL (not mandatory rework)
#       @code_translator is APPROVED (no rework needed)
```

**Rework Categories**:

| Verdict | Action | Example |
|---------|--------|---------|
| `APPROVED` | No action | Proceed |
| `CONDITIONAL` | Optional rework | Address if easy, note if not |
| `NEEDS_REVISION` | **MANDATORY rework** | Must fix |
| `CRITICAL_ISSUES` | **MANDATORY rework** | Must fix immediately |

### Step 3: Determine Rework Strategy

```python
num_agents = len(rework_agents)

if num_agents == 0:
    # All approved, proceed
    proceed_to_next_phase()
elif num_agents == 1:
    # Single agent rework (standard protocol)
    standard_single_agent_rework(rework_agents[0])
elif num_agents <= 3:
    # Multi-agent parallel rework
    parallel_multi_agent_rework(rework_agents)
else:
    # Too many issues, consider rewind
    consider_rewind()
```

**Decision Matrix**:

| # Agents | Strategy | Rationale |
|----------|----------|-----------|
| 0 | Proceed | All approved |
| 1 | Standard rework | Old protocol works fine |
| 2-3 | Parallel rework | Manageable coordination |
| 4+ | Consider rewind | Too many issues, fundamental problem |

### Step 4: Parallel Rework Execution

```python
def parallel_multi_agent_rework(agents):
    """Execute parallel rework for multiple agents"""

    # Step 4a: Send revision requests to all agents
    revision_requests = {}
    for agent in agents:
        issues = validation_results[agent]["issues"]
        request = f"""
        Director: Your work was reviewed in the validation gate.
        Verdict: NEEDS_REVISION
        Issues to fix:
        {format_issues(issues)}

        Please revise your work and report back when complete.
        """
        revision_requests[agent] = send_to_agent(agent, request)

    # Step 4b: Wait for ALL agents to complete
    completed_agents = []
    while len(completed_agents) < len(agents):
        for agent in agents:
            if agent not in completed_agents:
                if check_agent_complete(agent):
                    completed_agents.append(agent)

    # Step 4c: Collect all revisions
    revisions = {}
    for agent in agents:
        revisions[agent] = get_agent_revision(agent)

    return revisions
```

**Example Revision Request**:
```
@feasibility_checker:

Director: Your feasibility assessment was reviewed in the MODEL validation gate.

Verdict: NEEDS_REVISION

Issues to fix:
1. Computational time 6-10h is too long
   - Suggestion: Use frequentist + bootstrap instead of full MCMC

2. Model complexity may not be justified
   - Suggestion: Add cost-benefit analysis

Please revise your feasibility assessment (output/model/feasibility_{i}.md)
and report back when complete with: "Revisions complete, please send to [validator] for re-verification"
```

### Step 5: Multi-Agent Re-verification

```python
def multi_agent_re_verification(agents, revisions):
    """Re-verify all agents' revisions"""

    # Step 5a: Determine who should verify each agent
    verifier_map = {
      "@feasibility_checker": "@modeler",  # Modeler reviews feasibility
      "@advisor": "@reader",               # Reader reviews advisor
      "@modeler": "@advisor",              # Advisor reviews modeler
      # Add more mappings as needed
    }

    # Step 5b: Send all revisions for re-verification
    re_verifications = {}
    for agent in agents:
        verifier = verifier_map.get(agent, "@validator")
        request = f"""
        Director: Please re-verify @{agent}'s revisions.

        Original issues:
        {format_original_issues(agent)}

        Revisions made:
        {format_revisions(revisions[agent])}

        Please provide your verdict: APPROVED or NEEDS_REVISION
        """
        re_verifications[agent] = send_to_agent(verifier, request)

    # Step 5c: Wait for ALL re-verifications to complete
    completed_verifications = []
    while len(completed_verifications) < len(agents):
        for agent in agents:
            if agent not in completed_verifications:
                if check_verification_complete(agent):
                    completed_verifications.append(agent)

    # Step 5d: Collect all verdicts
    verdicts = {}
    for agent in agents:
        verdicts[agent] = get_verification_verdict(agent)

    return verdicts
```

**Example Re-verification Request**:
```
@modeler:

Director: Please re-verify @feasibility_checker's revisions.

Original issues (from MODEL validation gate):
1. Computational time 6-10h is too long
2. Model complexity may not be justified

Revisions made by @feasibility_checker:
- Updated feasibility assessment in output/model/feasibility_{i+1}.md
- Changed to frequentist + bootstrap approach
- Added cost-benefit analysis
- New estimated time: 2-3 hours

Please review the revised file and provide your verdict:
  - APPROVED: Issues resolved, proceed
  - NEEDS_REVISION: Issues persist, specify remaining problems
```

### Step 6: Final Decision

```python
def check_re_verifications(verdicts):
    """Check if all re-verifications passed"""

    all_approved = True
    for agent, verdict in verdicts.items():
        if "APPROVED" not in verdict:
            all_approved = False
            print(f"@{agent}'s revisions NOT approved: {verdict}")

    if all_approved:
        print("All revisions approved. Proceeding to next phase.")
        return True
    else:
        print("Some revisions not approved. Starting next iteration.")
        return False
```

**Decision Flow**:
```
All re-verifications complete
    ↓
Check verdicts:
  ALL "APPROVED"?
    ↓ YES                   ↓ NO
  Proceed to next      Check iteration count:
  phase                      < 3?          ≥ 3?
                              ↓             ↓
                          Loop back      Pause for
                          to Step 4     user intervention
```

---

## Complete Example Scenario

### Scenario: MODEL Validation Gate with Multiple Issues

**Initial Validation Results**:
```
@researcher:          ✅ APPROVED (A-)
  ZINB recommended, synthetic control OK with fallback

@feasibility_checker: ⚠️ NEEDS_REVISION
  Computational time 6-10h (too long) - use hybrid approach

@data_engineer:       ⚠️ CONDITIONAL (FEASIBLE 8/10)
  NOC mapping required, near-miss feature NOT available

@code_translator:     ✅ IMPLEMENTABLE
  PyMC recommended, 22-28h coding time

@advisor:             ⚠️ NEEDS_REVISION
  Causal claims too strong, 7.5/10 O-Prize potential
```

**Director's Response** (CORRECT - v2.5.4):
```
Collecting all validation feedback...

Agents needing MANDATORY rework:
1. @feasibility_checker (NEEDS_REVISION)
2. @advisor (NEEDS_REVISION)

Agents with CONDITIONAL verdict (optional):
3. @data_engineer (CONDITIONAL - may address if easy)

Agents APPROVED (no action):
4. @researcher
5. @code_translator

Strategy: Parallel multi-agent rework (2 agents)

=== Sending revision requests ===

@feasibility_checker:
  Issues:
  1. Computational time 6-10h is too long
     Fix: Use frequentist + bootstrap instead of full MCMC
  2. Add cost-benefit analysis

@advisor:
  Issues:
  1. Causal claims too strong
     Fix: Soften language for coach effect
  2. Improve methodology to reach 8.5/10+ potential

@data_engineer (optional):
  Note: Near-miss feature not available
  Action: Alternative feature suggestions welcome but not mandatory

=== Waiting for all agents to complete ===
```

**After Revisions Complete**:
```
All revisions received.

=== Sending for re-verification ===

@modeler: Please re-verify @feasibility_checker's revisions
  - Changed to frequentist + bootstrap
  - New time estimate: 2-3 hours
  - Added cost-benefit analysis

@reader: Please re-verify @advisor's revisions
  - Softened causal language
  - Added sensitivity analysis
  - Improved methodology explanation

=== Waiting for all re-verifications ===
```

**After Re-verification**:
```
All re-verifications received:

@modeler's verdict on @feasibility_checker: ✅ APPROVED
@reader's verdict on @advisor: ✅ APPROVED

Decision: ALL revisions approved
Action: Proceeding to Phase 2
```

---

## Protocol Integration

### Update Auto-Reverification Protocol

**OLD (v2.5.3)**:
```markdown
## Auto-Reverification Protocol

1. Agent reports "revisions complete"
2. Send to original validator for re-verification
3. Wait for verdict
4. If APPROVED → proceed
5. If NEEDS_REVISION → loop back (max 3 iterations)
```

**NEW (v2.5.4)**:
```markdown
## Enhanced Multi-Agent Re-verification Protocol

### Single-Agent Rework (1 agent)
1. Agent reports "revisions complete"
2. Send to original validator for re-verification
3. Wait for verdict
4. If APPROVED → proceed
5. If NEEDS_REVISION → loop back (max 3 iterations)

### Multi-Agent Rework (2-3 agents)
1. Collect ALL validation verdicts
2. Identify ALL agents needing rework
3. Send parallel revision requests to ALL agents
4. Wait for ALL agents to complete revisions
5. Send ALL agents for re-verification (relevant validators)
6. Wait for ALL re-verifications to complete
7. If ALL approve → proceed
8. If any not approve → loop back (max 3 iterations)

### Large-Scale Failure (4+ agents)
Consider rewind to earlier phase
```

---

## Anti-Patterns to Avoid

❌ **WRONG**: Only send to first agent with NEEDS_REVISION
```
"Now sending to @feasibility_checker for re-verification"
```
✅ **CORRECT**: Send to ALL agents with NEEDS_REVISION
```
"Sending to @feasibility_checker AND @advisor for parallel rework"
```

❌ **WRONG**: Ignore CONDITIONAL verdicts
```
"Ignoring @data_engineer's suggestions since they passed"
```
✅ **CORRECT**: Consider CONDITIONAL suggestions
```
"@data_engineer's suggestions are optional but valuable"
```

❌ **WRONG**: Proceed when some re-verifications fail
```
"@feasibility_checker approved but @advisor not, proceeding anyway"
```
✅ **CORRECT**: ALL must approve before proceeding
```
"Waiting for ALL re-verifications to approve"
```

---

## Testing Checklist

Test protocol with scenarios:

- [ ] 1 agent NEEDS_REVISION (should use standard protocol)
- [ ] 2 agents NEEDS_REVISION (should use parallel rework)
- [ ] 3 agents NEEDS_REVISION (should use parallel rework)
- [ ] Mix of APPROVED, CONDITIONAL, NEEDS_REVISION (should handle correctly)
- [ ] 4+ agents NEEDS_REVISION (should recommend rewind)
- [ ] Iteration 2: Some agents approve, some don't (should loop correctly)
- [ ] Iteration 3: Final check before giving up

---

**Document Version**: v2.5.4
**Created**: 2026-01-16
**Status**: MANDATORY for all validation gates
