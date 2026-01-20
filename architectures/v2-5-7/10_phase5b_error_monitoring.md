# Phase 5B Error Monitoring Protocol

> **Version**: v2.5.7
> **Date**: 2026-01-19
> **Purpose**: Define Phase 5B error handling with no-exit monitoring and immediate error resolution

---

## Problem Statement

**CRITICAL ISSUE**: Phase 5B (Full Training) is prone to errors, but AI session exits before errors can be addressed.

**Examples of Phase 5B Errors**:
```
Model 2 Failed: 'TensorVariable' object has no attribute 'logp'
- Error: Custom Zero-Truncated Poisson likelihood implementation error
- Current behavior: AI exits, task marked complete
- Result: Training fails silently, discovered too late

Model 3 Failed: 'Model3Config' object has no attribute 'n_sports'
- Error: Missing attribute in config
- Current behavior: AI exits, error lost
- Result: Wasted time, need to restart from scratch
```

**Root Causes**:
1. **AI session exits after starting training** - No monitoring during execution
2. **Errors not caught in real-time** - Training runs for hours before error discovered
3. **No error recovery protocol** - When errors occur, no clear action plan
4. **Agent handoff unclear** - Who monitors? Who fixes errors?

---

## Solution: Continuous Monitoring Protocol

### Core Principles

**Principle 1: AI Session Does NOT Exit**
- Phase 5B training runs in background
- AI session stays active, monitoring for errors
- Immediate error detection and reporting

**Principle 2: Error Watch Mode**
- @model_trainer enters "watch mode" during Phase 5B
- Monitor: Training log files for error patterns
- Monitor: Process status (running/failed/completed)
- Response: Immediate notification on error

**Principle 3: Error Resolution Without Exit**
- When error detected: Report to @director immediately
- @director coordinates fix (no session exit)
- Fix applied: Resume training (no restart from scratch)

---

## Phase 5B Workflow with Error Monitoring

### Step 1: Start Training (Background Process)

**@model_trainer starts training in background:**

```python
# Start training as background process
import subprocess
import time

log_file = 'output/implementation/logs/training_1_full.log'

# Start training in background
with open(log_file, 'w') as f:
    process = subprocess.Popen(
        ['python', 'output/implementation/code/model_1.py'],
        stdout=f,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

print(f"Training started with PID: {process.pid}")
print(f"Log file: {log_file}")
print(f"Entering watch mode...")
```

### Step 2: Enter Watch Mode

**@model_trainer monitors training:**

```python
def watch_training(process, log_file, check_interval=60):
    """
    Watch training process for errors.

    Args:
        process: Subprocess Popen object
        log_file: Path to training log
        check_interval: Seconds between checks (default: 60)
    """
    error_patterns = [
        'Error',
        'Exception',
        'Traceback',
        'Failed',
        'AttributeError',
        'KeyError',
        'ValueError',
        'TypeError',
        'RuntimeError',
    ]

    last_line_count = 0

    while True:
        # Check process status
        poll_result = process.poll()

        if poll_result is not None:
            # Process has exited
            if poll_result == 0:
                print("✅ Training completed successfully")
                return {'status': 'completed', 'exit_code': 0}
            else:
                print(f"❌ Training failed with exit code {poll_result}")
                return {'status': 'failed', 'exit_code': poll_result}

        # Check log file for errors
        try:
            with open(log_file, 'r') as f:
                lines = f.readlines()
                current_line_count = len(lines)

            # Check new lines since last check
            new_lines = lines[last_line_count:]
            last_line_count = current_line_count

            for line in new_lines:
                # Check for error patterns
                if any(pattern in line for pattern in error_patterns):
                    print(f"⚠️ ERROR DETECTED: {line.strip()}")

                    # Report to @director
                    error_report = {
                        'status': 'error',
                        'error_line': line.strip(),
                        'timestamp': time.time(),
                        'log_file': log_file,
                        'line_number': current_line_count
                    }

                    return error_report

        except Exception as e:
            print(f"⚠️ Error reading log file: {e}")
            # Continue monitoring (don't exit)

        # Wait before next check
        time.sleep(check_interval)
```

### Step 3: Error Detected → Report to @director

**When error detected:**

```
@model_trainer: "⚠️ ERROR DETECTED during Phase 5B training

Model: 1
Process ID: 12345
Log file: output/implementation/logs/training_1_full.log
Error: AttributeError: 'TensorVariable' object has no attribute 'logp'
Line: 45
Timestamp: 2026-01-19 15:34:12

Error Type: Implementation Error
Severity: CRITICAL (training halted)

Action Required: Fix and resume training

Awaiting @director guidance."
```

**@director response (NO EXIT):**

```
@director: "@code_translator: Error detected in model_1.py line 45
          Error: AttributeError: 'TensorVariable' object has no attribute 'logp'

          This is a PyMC API compatibility issue.

          Options:
          1. Fix PyMC version (upgrade/downgrade)
          2. Update code to use PyMC v5 API (pm.logp() instead of .logp)
          3. DO NOT simplify algorithm

          Please investigate and provide fix."
```

**@code_translator investigates and fixes:**

```
@code_translator: "Investigation complete:

Error cause: PyMC v5 changed API from .logp to pm.logp()

Line 45 (OLD):
  log_prob = latent_var.logp(observed)

Line 45 (FIXED):
  log_prob = pm.logp(latent_var, observed)

Fix applied to: output/implementation/code/model_1.py

Recommendation: Resume training from checkpoint (if available) or restart"
```

**@director decision:**

```
@director: "@model_trainer: Fix applied. Resume training.

          Actions:
          1. Kill current process (PID 12345)
          2. Restart training with fixed code
          3. Continue monitoring

          Report when training completes or new error detected."
```

### Step 4: Resume Training

**@model_trainer restarts training:**

```
@model_trainer: "Restarting training with fixed code...

Old process killed: PID 12345
New process started: PID 12346
Log file: output/implementation/logs/training_1_full.log (appending)

Entering watch mode...

Training resumed at: 2026-01-19 15:42:00"
```

---

## Error Categories and Responses

### Category 1: Implementation Errors (Fixable)

**Examples**:
- `AttributeError: 'TensorVariable' object has no attribute 'logp'`
- `KeyError: 'Gold'`
- `NameError: name 'prepare_factor_model' is not defined`

**Response Protocol**:
```
1. @model_trainer detects error → Reports to @director
2. @director → @code_translator: Investigate and fix
3. @code_translator → Provides fix
4. @director → @model_trainer: Apply fix, resume training
5. @model_trainer → Restarts training with fix
```

### Category 2: Data Errors (Fixable)

**Examples**:
- `ValueError: Input contains NaN`
- `KeyError: 'column_name'`
- `pd.errors.EmptyDataError`

**Response Protocol**:
```
1. @model_trainer detects error → Reports to @director
2. @director → @data_engineer: Investigate data issue
3. @data_engineer → Fixes data, regenerate features
4. @director → @model_trainer: Restart training with fixed data
5. @model_trainer → Restarts training
```

### Category 3: Resource Errors (Fixable)

**Examples**:
- `MemoryError`
- `RuntimeError: out of memory`
- `CUDA out of memory`

**Response Protocol**:
```
1. @model_trainer detects error → Reports to @director
2. @director → @code_translator: Optimize memory usage
3. @code_translator → Implements batch processing or reduces data size
4. @director → @model_trainer: Resume with optimized code
5. @model_trainer → Restarts training
```

### Category 4: Convergence Errors (May Need @modeler Consultation)

**Examples**:
- `RuntimeWarning: Maximum number of iterations reached`
- `Sampling not converged`
- `R-hat > 1.1`

**Response Protocol**:
```
1. @model_trainer detects warning → Reports to @director
2. @director → @modeler: Convergence issue, guidance needed
3. @modeler → Provides solution (increase iterations, adjust priors)
4. @director → @code_translator: Implement @modeler's solution
5. @model_trainer → Restart training
```

---

## Watch Mode Implementation

### Monitoring Frequency

**Standard Monitoring**:
- Check interval: 60 seconds (1 minute)
- Purpose: Balance responsiveness vs overhead

**Critical Phase Monitoring**:
- Check interval: 10 seconds
- Duration: First 10 minutes of training (when most errors occur)
- Purpose: Catch early errors quickly

### Log File Monitoring

**Log File Format**:
```python
# Training log should include:
timestamp=2026-01-19T15:34:12.123 level=INFO message="Starting training..."
timestamp=2026-01-19T15:34:15.456 level=ERROR message="AttributeError: 'TensorVariable' object has no attribute 'logp'"
timestamp=2026-01-19T15:34:15.457 level=ERROR line=45
```

**Error Pattern Matching**:
```python
ERROR_PATTERNS = [
    r'Error:',
    r'Exception:',
    r'Traceback',
    r'AttributeError',
    r'KeyError',
    r'ValueError',
    r'TypeError',
    r'RuntimeError',
    r'MemoryError',
    r'Failed',
]
```

### Status Reporting

**Regular Status Updates (Every 30 minutes)**:
```
@model_trainer: "Phase 5B Training Status Update

Model: 1
PID: 12345
Elapsed: 2h 30m / ~12h (21% complete)
Log file: output/implementation/logs/training_1_full.log
Status: ✅ Running normally
Last log line: [most recent log entry]

No errors detected. Continuing monitoring..."
```

---

## Communication Protocol

### @model_trainer → @director (Error Report)

```markdown
## Phase 5B Error Report

**Model**: {i}
**PID**: {process_id}
**Timestamp**: {error_time}

### Error Details
- **Type**: {error_type}
- **Message**: {error_message}
- **Line**: {line_number if applicable}
- **File**: {file_path if applicable}

### Log File
- **Path**: {log_file_path}
- **Context**: [5 lines before and after error]

### Current Status
- **Process**: {running/stopped/crashed}
- **Exit Code**: {exit_code if stopped}
- **Uptime**: {time_since_start}

### Recommended Action
{Suggested next step}

**Awaiting @director guidance**
```

### @director → @model_trainer (Action Command)

```markdown
## Phase 5B Action Command

**Action**: {RESTART/RESUME/TERMINATE/CONTINUE}

### Instructions
{Specific instructions}

### Changes Applied
- [ ] Code updated: {file_path}
- [ ] Data regenerated: {file_path}
- [ ] Configuration changed: {parameter}

### Next Steps
1. {Step 1}
2. {Step 2}

**Execute and report back**
```

### @model_trainer → @director (Completion Report)

```markdown
## Phase 5B Training Complete

**Model**: {i}
**Status**: ✅ SUCCESS / ❌ FAILED

### Training Summary
- **Total time**: {elapsed_time}
- **Samples**: {samples_generated}
- **Chains**: {num_chains}
- **Convergence**: {r_hat_stats}

### Output Files
- Results: output/results/results_{i}.csv
- Model: output/implementation/models/model_{i}_full.pkl
- Log: output/implementation/logs/training_{i}_full.log

### Errors Encountered and Resolved
1. {Error 1} → {Resolution}
2. {Error 2} → {Resolution}

**Ready for Phase 5.5 validation**
```

---

## No-Exit Guarantee

### Session Persistence

**AI Session MUST NOT Exit During Phase 5B**:

```
❌ FORBIDDEN:
@model_trainer: "Training started in background. Task complete."
[AI session exits]

✅ REQUIRED:
@model_trainer: "Training started in background (PID: 12345).
                Entering watch mode. Session active.
                Will report completion or errors."

[AI session stays active, monitoring]
```

### Timeout Protection

**If training takes longer than expected:**

```
@model_trainer: "⚠️ TIMEOUT WARNING

Model: 1
Expected time: 12-18 hours
Elapsed time: 24 hours (above maximum)

Status: Still running
Last log: [most recent entry]

Action: Continue monitoring or investigate?

Awaiting @director decision."
```

**@director options**:
1. Continue monitoring (if training progressing normally)
2. Investigate (check log for issues)
3. Terminate and restart (if stuck)

---

## Implementation Checklist

**For @model_trainer**:
- [ ] Start training as background process
- [ ] Capture PID for process control
- [ ] Enter watch mode (no session exit)
- [ ] Monitor log file for error patterns
- [ ] Report status every 30 minutes
- [ ] Report errors immediately to @director
- [ ] Await @director guidance on errors
- [ ] Apply fixes and resume training (no restart from scratch)
- [ ] Report completion with summary

**For @director**:
- [ ] Receive error reports from @model_trainer
- [ ] Coordinate fixes (delegate to appropriate agent)
- [ ] Provide clear action commands
- [ ] Ensure training continues (no session exit)
- [ ] Track all errors and resolutions

**For @code_translator**:
- [ ] Investigate implementation errors
- [ ] Provide fixes (not simplifications)
- [ ] Test fixes before deployment
- [ ] Document changes

**For @data_engineer**:
- [ ] Investigate data errors
- [ ] Regenerate features if needed
- [ ] Verify data integrity

---

## Example: Complete Error Resolution Workflow

```
T=0h: @model_trainer starts Phase 5B training
      "Training started (PID: 12345). Watch mode active."

T=2h: @model_trainer status update
      "Training 17% complete. No errors."

T=3h: @model_trainer detects ERROR
      "⚠️ ERROR: AttributeError: 'TensorVariable' object has no attribute 'logp'
       Line 45. Awaiting @director guidance."

T=3h: @director delegates to @code_translator
      "@code_translator: Investigate and fix PyMC API issue in model_1.py line 45"

T=3.1h: @code_translator provides fix
      "Issue: PyMC v5 API change. Fix: Use pm.logp() instead of .logp.
       Fixed code: [patch]. Ready to apply."

T=3.2h: @director commands restart
      "@model_trainer: Apply fix and restart training."

T=3.3h: @model_trainer applies fix, restarts
      "Fix applied. Training restarted (PID: 12346).
       Previous progress: 17%. Resuming from checkpoint.
       Watch mode active."

T=10h: @model_trainer status update
      "Training 83% complete. No new errors."

T=12h: @model_trainer completion report
      "✅ Training complete.
       Total time: 12.5 hours (including 30min error resolution)
       Samples: 20000 × 4 chains
       Convergence: R-hat < 1.01 (all parameters)
       Errors resolved: 1 (PyMC API compatibility)
       Ready for Phase 5.5 validation"
```

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
