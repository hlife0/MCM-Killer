# Protocol 11: Emergency Convergence Delegation

> **Purpose**: Enable fast response (30-60 min) for critical convergence failures while maintaining @director coordination
> **Owner**: @model_trainer (trigger) + @modeler (escalation) + @code_translator (fix) + @director (oversight)
> **Scope**: Phase 5B (Full Training) - critical convergence errors only

## Problem Statement

Standard error response too slow for critical convergence failures:

```
Standard protocol:
@model_trainer → @director → @modeler → @director → @code_translator → @director
Response time: 4-5 hours

But convergence critical:
R-hat > 1.3, training already 12+ hours
Need: 30-60 minutes
```

## When to Use

**When to Use** (ALL criteria must be met):

1. **Error Category**: Convergence (Category 4)
2. **Severity**: CRITICAL
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. **@modeler is available and responsive**
4. **Fix is well-understood** (parameter adjustment, NOT algorithm change)

**Example triggers**:
```
R-hat = 1.47 (>1.3 threshold) → EMERGENCY
12 hours elapsed, R-hat = 1.15 → EMERGENCY
Divergent transitions: 15% (>10% threshold) → EMERGENCY
```

## Emergency Flow

**Bypass @director for speed, maintain oversight for coordination**

```
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix (copies @director)
@director → retroactive approval (within 1 hour)
@model_trainer → resumes training
```

**Timeline**:
- 0-5 min: @model_trainer escalates to @modeler
- 5-15 min: @modeler diagnoses, delegates to @code_translator
- 15-30 min: @code_translator implements fix
- 30-45 min: Fix verified, training resumes
- **Total: 30-60 minutes (8× faster than standard)**

## Step-by-Step Process

### Step 1: @model_trainer Escalates Directly to @modeler

**Emergency escalation message**:
```
@model_trainer: "⚠️ EMERGENCY CONVERGENCE ⚠️
Protocol 11 activated

Model: {i}
Training duration: 14.3 hours
Issue: R-hat = 1.47 (>1.3 threshold)
Divergent transitions: 0%
Convergence status: SEVERE NON-CONVERGENCE

Direct escalation: @modeler, please diagnose and provide fix instructions.

@director: COPY - retroactive approval will be provided within 1 hour."
```

### Step 2: @modeler Diagnoses and Delegates Directly

**@modeler response** (within 10 minutes):
```
@modeler: "Diagnosis: Target acceptance too low (0.65)
Causes: Tree depth saturation, inefficient exploration

Fix: Increase target_accept to 0.90, increase max_treedepth to 15

@code_translator: Implement these changes in model_{i}.py:
- Line 42: target_accept=0.65 → target_accept=0.90
- Line 43: max_treedepth=10 → max_treedepth=15

@director: COPY - proposed fix for retroactive approval.
Rationale: Standard convergence issue, well-understood solution."
```

### Step 3: @code_translator Implements Fix (Copies @director)

**@code_translator action** (within 15 minutes):
```
@code_translator: "Implementing emergency fix:

Changes made to model_{i}.py:
- Line 42: target_accept changed from 0.65 to 0.90
- Line 43: max_treedept changed from 10 to 15

Rationale: Improve convergence efficiency (per @modeler diagnosis)

@model_trainer: Fix complete, resume training from checkpoint.
@director: COPY - fix implemented, awaiting retroactive approval."
```

### Step 4: @director Provides Retroactive Approval

**@director approval** (within 1 hour):
```
@director: "RETROACTIVE APPROVAL

Emergency Protocol 11 executed:
- Trigger: R-hat = 1.47 (>1.3 threshold)
- Diagnosis: @modeler (target_accept too low)
- Fix: @code_translator (target_accept 0.65→0.90, max_treedepth 10→15)

Approval: GRANTED
Rationale: Standard convergence issue, appropriate fix applied

@model_trainer: Resume training authorized.
@modeler: Thank you for rapid response.
@code_translator: Fix verified."

Logged in: VERSION_MANIFEST.json
```

### Step 5: @model_trainer Resumes Training

**@model_trainer action**:
```
@model_trainer: "Resuming training from checkpoint (hour 14.3)
Fix applied: target_accept=0.90, max_treedepth=15
Monitoring for improved convergence
Next status update: 30 minutes"
```

## Safeguards

### 1. Single-Use Limit

**Once per model only**

```
IF emergency_delegation_count[model_{i}] > 0:
    RETURN "Cannot use Protocol 11 again for this model
           Use standard protocol instead"
```

**Rationale**: Prevent abuse, ensure issues are genuinely fixed

### 2. Time Limit

**Fix must be implemented within 30 minutes**

```
IF time_elapsed > 30 minutes:
    @director: "Emergency protocol timed out
                Revert to standard protocol"
```

**Rationale**: If taking too long, no longer "emergency"

### 3. Severity Threshold

**R-hat > 1.3 (not just >1.1)**

```
R-hat = 1.15 → Use standard protocol
R-hat = 1.31 → Use emergency protocol
```

**Rationale**: Only for SEVERE issues

### 4. Documentation

**All emergency fixes logged in VERSION_MANIFEST.json**

```json
{
  "emergency_delegation": {
    "model": "model_1",
    "timestamp": "2026-01-28T14:30:00Z",
    "trigger": "R-hat = 1.47",
    "diagnosis": "@modeler: target_accept too low",
    "fix": "target_accept 0.65→0.90, max_treedepth 10→15",
    "approval": "@director: GRANTED",
    "duration": "22 minutes"
  }
}
```

### 5. Oversight

**@director retroactive approval required within 1 hour**

```
IF @director_approval NOT received within 1 hour:
    Training paused → @model_trainer reports timeout
    @director reviews → May reject fix → Standard protocol resumes
```

## Comparison: Emergency vs Standard

| Aspect | Standard Protocol | Emergency Protocol |
|--------|------------------|-------------------|
| Flow | @director-centered | @modeler-centered |
| Response time | 4-5 hours | 30-60 minutes |
| Rounds | 3-4 rounds | 1 round |
| Approval | Pre-approval | Retroactive |
| Use case | Most errors | Critical convergence only |
| Limit | None | Once per model |

## When NOT to Use

**Do NOT use emergency protocol for**:
- Data errors (use standard: @model_trainer → @director → @data_engineer)
- Syntax errors (use standard: @model_trainer → @director → @code_translator)
- Algorithm changes (require @director consultation)
- First convergence attempt (need to verify if real issue)

**Use standard protocol when**:
- Severity not critical (R-hat 1.1-1.3)
- Fix unclear (need investigation)
- @modeler not available
- Already used emergency protocol once for this model

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
