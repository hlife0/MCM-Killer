# Emergency Convergence Delegation Protocol

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Source**: v2.5.8
> **Purpose**: Enable fast response (30-60 min) for critical convergence failures while maintaining @director coordination

---

## Protocol Purpose

**CRITICAL ISSUE**: Standard protocol takes 4-5 hours to resolve convergence failures, causing unacceptable delays during training.

**SOLUTION**: Emergency delegation protocol enables 30-60 minute response time (8x faster) while maintaining @director oversight through retroactive approval.

**SAFEGUARDS**: Single-use limit, severity thresholds, time limits, documentation, retroactive approval

---

## When to Use Emergency Protocol

### Criteria (ALL must be met)

1. **Error Category**: Convergence (Category 4)
2. **Severity**: CRITICAL
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. **@modeler is available and responsive**
4. **Fix is well-understood**
   - Parameter adjustment (tune, target_accept, draws)
   - NOT algorithm change (requires design review)
   - NOT feature addition/removal (violates design expectations)

### When NOT to Use (Use Standard Protocol Instead)

**❌ FORBIDDEN**:

1. **Algorithm changes**
   - Changing NUTS to Slice sampler
   - Adding/removing model components
   - **Reason**: Requires design review, violates design expectations

2. **Feature modifications**
   - Adding/removing features
   - Changing feature engineering
   - **Reason**: Violates design expectations table

3. **Non-critical convergence issues**
   - R-hat 1.1-1.3 (mild non-convergence)
   - <5% divergent transitions
   - **Reason**: Can wait for standard @director coordination

4. **Routine parameter tweaks**
   - Small adjustments (<20% change)
   - Hyperparameter tuning
   - **Reason**: Not urgent enough for emergency protocol

5. **When @modeler unavailable**
   - @modeler not responsive within 10 minutes
   - @modeler offline
   - **Reason**: Emergency protocol requires @modeler participation

---

## Emergency Flow (Bypasses Standard @director Delegation)

### Step 1: @model_trainer Escalates to @modeler Directly

```
@model_trainer: "@modeler: 🚨 EMERGENCY - Critical convergence failure

Model: {i}
Process ID: {pid}
Log file: output/implementation/logs/training_{i}_full.log

Severity Indicators:
- R-hat: {value} (threshold: 1.3)
- Divergent transitions: {count}/{total} ({percentage}%)
- Elapsed time: {time} / 12h
- Status: TRAINING HALTED

Requesting emergency fix authorization under v2.6.0 Protocol 11."
```

### Step 2: @modeler Analyzes and Delegates to @code_translator

```
@modeler: "@code_translator: 🚨 EMERGENCY FIX AUTHORIZED (v2.6.0 Protocol 11)

Model: {i}
Issue: {diagnosis}
Root Cause: {analysis}

Fix Required:
{specific parameter changes}

Implementation:
- File: model_{i}.py
- Line: {line_number}
- Change: {before} → {after}

Implement IMMEDIATELY.
Copy @director on completion.

Emergency Protocol Reference: v2.6.0 Protocol 11"
```

### Step 3: @code_translator Implements and Notifies @director

```
@code_translator: "🚨 Emergency fix implemented (v2.6.0 Protocol 11)

Model: {i}
Changes Applied:
1. {change_1}
2. {change_2}

Files Modified:
- output/implementation/code/model_{i}.py (lines {X}-{Y})

Authorization: @modeler ({timestamp})
Emergency Protocol: v2.6.0 Protocol 11

@director: Retroactive approval requested.
Training resumed: {timestamp}"
```

### Step 4: @director Reviews Retroactively

```
@director: "Retroactive review of emergency fix (v2.6.0 Protocol 11)

Model: {i}
Emergency Authorization: @modeler
Fix Applied: {summary}

Review Result:
✅ APPROVED - Fix was appropriate
OR
❌ REJECTED - Fix was incorrect, revert changes

Decision Basis: {rationale}

Action: {continue training / revert / restart}"

[If APPROVED: Document in VERSION_MANIFEST.json]
[If REJECTED: Revert changes, restart from checkpoint]
```

---

## Safeguards (MUST Be Enforced)

### 1. Single-Use Limit

**Emergency protocol can be used ONCE per model**

- If first emergency fix fails → Revert to standard protocol
- Prevents cascade of unauthorized fixes
- Tracks usage in VERSION_MANIFEST.json

### 2. Severity Threshold

**Must meet CRITICAL criteria**:

- R-hat > 1.3 (not just > 1.1)
- OR 12+ hours without convergence
- Routine convergence issues (R-hat 1.1-1.3) → Use standard protocol

### 3. Time Limit

**Fix must be implemented within 30 minutes**:

- From @model_trainer escalation to fix completion
- If exceeded → Revert to standard protocol

### 4. Retroactive Approval

**@director must review within 1 hour**:

- If @director not available → Emergency fix still stands
- If @director rejects → Revert and restart

### 5. Documentation

**All emergency fixes logged in VERSION_MANIFEST.json**:

```json
{
  "model": 1,
  "emergency_fix": true,
  "authorized_by": "@modeler",
  "implemented_by": "@code_translator",
  "timestamp": "2026-01-23T02:34:56Z",
  "severity": "R-hat > 1.3",
  "changes": ["tune: 2000→4000", "target_accept: 0.95→0.99"],
  "retroactive_approval": "@director (approved at 03:15)"
}
```

---

## Agent Responsibilities

### @model_trainer MUST

1. Monitor for critical convergence indicators (R-hat > 1.3, 12h elapsed)
2. Escalate to @modeler directly when emergency criteria met
3. Implement fix and resume training within 30 minutes
4. Document all emergency fixes in training log

### @modeler MUST

1. Be available for consultation (30-minute response time target)
2. Analyze convergence failure within 15 minutes of escalation
3. Recommend fix within 30 minutes (parameter adjustment or algorithm change)
4. Delegate to @code_translator if emergency criteria met
5. Document design issues if algorithm change needed

### @code_translator MUST

1. Implement emergency fix within 10 minutes of @modeler delegation
2. Copy @director on completion
3. Provide clear summary of changes made
4. Do NOT question @modeler's emergency authorization (implement first, review later)

### @director MUST

1. Review emergency fix retroactively within 1 hour
2. Approve or reject with clear rationale
3. Document decision in VERSION_MANIFEST.json
4. Revert changes if rejected

---

## Protocol Comparison

### Standard Protocol vs Emergency Protocol

| Aspect | Standard Protocol | Emergency Protocol |
|--------|------------------|---------------------|
| **Trigger** | Any error | R-hat > 1.3 OR 12h elapsed |
| **Delegation path** | @model_trainer → @director → @modeler → @director → @code_translator | @model_trainer → @modeler → @code_translator |
| **Response time** | 4-5 hours (typical) | 30-60 minutes |
| **@director involvement** | Real-time approval | Retroactive approval |
| **Scope** | All error types | Parameter adjustments only |
| **Usage limit** | Unlimited | Once per model |
| **Documentation** | Standard log | VERSION_MANIFEST.json + audit trail |

---

## Example Scenarios

### Scenario 1: Emergency Protocol Appropriate ✅

```
@model_trainer: "🚨 EMERGENCY
Model: 1
R-hat: 1.42 (threshold: 1.3)
Elapsed: 14h / 12h
Status: Complete convergence failure"

@modeler: "@code_translator: 🚨 EMERGENCY FIX AUTHORIZED
Issue: Insufficient tuning samples
Fix: tune: 2000 → 4000 (line 45)
Implement immediately."

[30 minutes later]

@code_translator: "Emergency fix implemented.
tune increased from 2000 to 4000.
Training resumed.

@director: Retroactive approval requested."

@director: "✅ APPROVED
Fix was appropriate for severity.
Documented in VERSION_MANIFEST.json"
```

### Scenario 2: Emergency Protocol NOT Appropriate ❌

```
@model_trainer: "Convergence issue
Model: 2
R-hat: 1.18 (threshold: 1.1)
Elapsed: 3h
Status: Mild non-convergence"

@director: "@modeler: Convergence issue in Model 2
R-hat: 1.18
Please analyze and recommend."

[Standard protocol - NOT emergency]
```

### Scenario 3: Algorithm Change - Use Standard Protocol ❌

```
@model_trainer: "🚨 EMERGENCY
Model: 3
R-hat: 1.45
NUTS sampler failing consistently"

@modeler: "@director: Analysis complete
NUTS sampler is incompatible with this model geometry.
Recommend changing to Slice sampler.
This is an algorithm change - requires design update.
Cannot use emergency protocol.

Recommend Phase 1 rewind to update design."
```

---

## Decision Flow

```
Convergence Error Detected
    ↓
Is R-hat > 1.3 OR 12h elapsed?
    ↓
YES → Is @modeler available?
    ↓
      YES → Is fix a simple parameter adjustment?
          ↓
            YES → ✅ USE EMERGENCY PROTOCOL
            NO → ❌ Use standard protocol (algorithm change)
      NO → ❌ Use standard protocol (@modeler unavailable)
NO → ❌ Use standard protocol (not critical enough)
```

---

**Document Version**: v2.6.0 (Inherited from v2.5.8)
**Last Updated**: 2026-01-23
**Status**: Active

**Response Time**: 30-60 minutes (8x faster than standard protocol)
