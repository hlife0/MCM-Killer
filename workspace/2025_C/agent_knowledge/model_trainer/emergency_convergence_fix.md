# Emergency Convergence Fix Protocol (v2.5.8)

**Purpose**: This document defines the emergency protocol for critical convergence failures during Phase 5B training. It enables rapid response (8× faster than standard workflow) for severe convergence issues while maintaining oversight and accountability.

**Source**: Extracted from model_trainer.md (v2.5.8)

**Context**: Standard @director coordination can take hours during critical convergence failures. This emergency protocol allows @model_trainer to escalate directly to @modeler for immediate fixes when specific criteria are met, with retroactive @director approval.

---

## 🚨 Emergency Convergence Fix Protocol (v2.5.8)

> [!CRITICAL] **[v2.5.8] EMERGENCY PROTOCOL for critical convergence failures**
>
> **Use ONLY when all criteria are met. This is an EXCEPTION to standard @director coordination.**

### When to Use Emergency Protocol

**CRITERIA** (ALL must be met):

1. ✅ Error Category: **Convergence (Category 4)**
2. ✅ Severity: **CRITICAL**
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. ✅ @modeler is **available and responsive**
4. ✅ Fix is **well-understood** (parameter adjustment, NOT algorithm change)

### Emergency Flow (Bypasses Standard @director Delegation)

**Step 1: @model_trainer escalates to @modeler directly**

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

Requesting emergency fix authorization under v2.5.8 protocol."
```

**Step 2: @modeler analyzes and delegates to @code_translator**

```
@modeler: "@code_translator: 🚨 EMERGENCY FIX AUTHORIZED (v2.5.8)

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
Copy @director on completion."
```

**Step 3: @code_translator implements and notifies @director**

```
@code_translator: "🚨 Emergency fix implemented (v2.5.8)

Model: {i}
Changes Applied:
{changes}

Files Modified:
- output/implementation/code/model_{i}.py (lines {X}-{Y})

Authorization: @modeler ({timestamp})
@dicator: Retroactive approval requested.
Training resumed: {timestamp}"
```

**Step 4: @director reviews retroactively**

```
@dicator: "Retroactive review of emergency fix (v2.5.8)

Model: {i}
Emergency Authorization: @modeler
Fix Applied: {summary}

Review Result:
✅ APPROVED - Fix was appropriate
OR
❌ REJECTED - Fix was incorrect, revert changes

Decision Basis: {rationale}"

[If APPROVED: Document in VERSION_MANIFEST.json]
[If REJECTED: Revert changes, restart from checkpoint]
```

### Safeguards (MUST be enforced)

1. **Single-Use Limit**: Emergency protocol can be used **ONCE per model**
   - If first emergency fix fails, revert to standard protocol
   - Prevents cascade of unauthorized fixes

2. **Severity Threshold**: Must meet **CRITICAL criteria**
   - R-hat > 1.3 (not just > 1.1)
   - OR 12+ hours without convergence
   - Routine convergence issues (R-hat 1.1-1.3) → Use standard protocol

3. **Time Limit**: Fix must be implemented within **30 minutes**
   - From @model_trainer escalation to fix completion
   - If exceeded → Revert to standard protocol

4. **Retroactive Approval**: @director must review within **1 hour**
   - If @director not available → Emergency fix still stands
   - If @director rejects → Revert and restart

5. **Documentation**: All emergency fixes logged in **VERSION_MANIFEST.json**
   ```json
   {
     "model": 1,
     "emergency_fix": true,
     "authorized_by": "@modeler",
     "implemented_by": "@code_translator",
     "timestamp": "2026-01-19T02:34:56Z",
     "severity": "R-hat > 1.3",
     "changes": ["tune: 2000→4000"],
     "retroactive_approval": "@director (approved at 03:15)"
   }
   ```

### When NOT to Use Emergency Protocol

**❌ FORBIDDEN** (Use standard @director coordination instead):

1. **Algorithm changes** - Changing NUTS to Slice sampler, adding/removing model components
2. **Feature modifications** - Adding/removing features, changing feature engineering
3. **Non-critical convergence issues** - R-hat 1.1-1.3, <5% divergent transitions
4. **Routine parameter tweaks** - Small adjustments (<20%), hyperparameter tuning
5. **When @modeler unavailable** - @modeler not responsive within 10 minutes

### Emergency Protocol Decision Tree

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

### Example: Emergency Protocol Appropriate ✅

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

@dicator: Retroactive approval requested."

@director: "✅ APPROVED
Fix was appropriate for severity.
Documented in VERSION_MANIFEST.json"
```

### Example: Emergency Protocol NOT Appropriate ❌

```
@model_trainer: "Convergence issue
Model: 2
R-hat: 1.18 (threshold: 1.1)
Elapsed: 3h
Status: Mild non-convergence"

@dicator: "@modeler: Convergence issue in Model 2
R-hat: 1.18
Please analyze and recommend."

[Standard protocol - NOT emergency]
```

### Training Phase Responsibilities (v2.5.8)

**@model_trainer MUST**:
1. Monitor for critical convergence indicators (R-hat > 1.3, 12h elapsed)
2. Escalate to @modeler directly when emergency criteria met
3. Resume training within 30 minutes of fix implementation
4. Document all emergency fixes in training log
