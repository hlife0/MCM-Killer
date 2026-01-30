# Phase 5B Watch Mode Protocol (v2.5.7 MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] Phase 5B (Full Training) requires AI session to stay active in watch mode.**
>
> **AI session MUST NOT exit after starting training. You must monitor for errors and report immediately.**

## Phase 5B Error Monitoring (MANDATORY)

**Problem**: Phase 5B training runs for 6-12+ hours. Errors can occur (API incompatibility, data issues, convergence failures). If AI session exits, errors are discovered too late.

**Solution**: **Watch Mode** - AI session stays active, monitoring training in real-time.

## Watch Mode Implementation

**Step 1: Start Training in Background**

```python
#!/usr/bin/env python3
"""
Start Phase 5B training in background with monitoring
"""
import subprocess
import time
import os

log_file = 'output/implementation/logs/training_{i}_full.log'

# Start training as background process
with open(log_file, 'w') as f:
    process = subprocess.Popen(
        ['python', 'output/implementation/code/model_{i}.py'],
        stdout=f,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

print(f"✅ Training started with PID: {process.pid}")
print(f"📄 Log file: {log_file}")
print(f"🔄 Entering watch mode...")
```

**Step 2: Enter Watch Mode (NO EXIT)**

```python
def watch_training(process, log_file, check_interval=60):
    """
    Watch training process for errors.

    CRITICAL: This function keeps AI session active.
    DO NOT EXIT until training completes or error detected.
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
        'MemoryError',
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

                    # Report to @director immediately
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

        # Regular status update (every 30 minutes = 1800 seconds)
        if int(time.time()) % 1800 < check_interval:
            elapsed = time.time() - start_time
            print(f"📊 Status Update: Training running for {elapsed/3600:.1f}h")

        # Wait before next check
        time.sleep(check_interval)

# Start watch mode
print("🔄 Watch mode active. AI session will NOT exit.")
print("⏱️ Monitoring for errors...")

result = watch_training(process, log_file)
```

**Step 3: Error Detected → Report to @director**

**When error detected during watch mode**:

```
@model_trainer: "⚠️ ERROR DETECTED during Phase 5B training

Model: {i}
Process ID: {pid}
Log file: output/implementation/logs/training_{i}_full.log
Error: {error_message}
Line: {line_number}
Timestamp: {timestamp}

Error Type: {implementation / data / resource}
Severity: CRITICAL (training halted)

Action Required: Fix and resume training

Awaiting @director guidance."
```

**@director response (NO EXIT)**:

```
@director: "@code_translator: Error detected in model_{i}.py
          Error: {specific error}
          Line: {line_number}

          This is a {implementation / data} error.

          Please investigate and provide fix."
```

**@code_translator investigates and fixes**:

```
@code_translator: "Investigation complete:

Error cause: {root cause}
Line {line_number}: {what's wrong}

Fix: {specific fix}
Updated code: {patch}

📋 CHANGES SUMMARY (MANDATORY):
- Files modified: model_{i}.py (lines {X}-{Y})
- Parameters changed: {list all changed parameters}
  - Before: {value} → After: {value}
- Algorithm changed: YES/NO
- Features added/removed: YES/NO
- Design expectations compliance: {assessment}

Recommendation: Resume training from checkpoint (if available) or restart"
```

**@director decision (CRITICAL: Must validate reworked code)**:

```
@director: [ANALYZES @code_translator's CHANGES SUMMARY]

IF fix changes design parameters (tune, chains, draws, algorithm, features):
  "@time_validator: RE-VALIDATION REQUIRED

  @code_translator has modified model_{i}.py:
  Changes: {list of parameter changes}

  Please run Phase 4.5 validation on reworked code:
  - Check against Design Expectations Table
  - Create comparison table (Design vs Actual vs Tolerance vs Verdict)
  - Calculate overall score
  - Return APPROVE/REJECT decision

  Do NOT allow training to resume until validation complete."

  @time_validator runs Phase 4.5:
  - Read reworked model_{i}.py
  - Compare to Design Expectations Table
  - Generate comparison table
  - Return decision:
    - ✅ APPROVE: Changes within tolerance → Allow training
    - ❌ REJECT: Changes violate design → Full rework required

  IF @time_validator APPROVES:
    @director: "@model_trainer: Fix applied and validated. Resume training.

    Actions:
    1. Kill current process (PID: {old_pid})
    2. Restart training with fixed code
    3. Continue monitoring

    Report when training completes or new error detected."

  IF @time_validator REJECTS:
    @director: "@code_translator: Fix REJECTED by @time_validator

    Reason: {specific violation}
    Action: Full rework required to match design exactly.

    Please rewrite model_{i}.py to comply with Design Expectations Table."

ELSE (fix is simple bug fix, no parameter changes):
  @director: "@model_trainer: Fix applied. Resume training.

  Actions:
  1. Kill current process (PID: {old_pid})
  2. Restart training with fixed code
  3. Continue monitoring

  Report when training completes or new error detected."
```

**Step 4: Resume Training**

```
@model_trainer: "Restarting training with fixed code...

Old process killed: PID {old_pid}
New process started: PID {new_pid}
Log file: output/implementation/logs/training_{i}_full.log (appending)

Entering watch mode...

Training resumed at: {timestamp}"
```

## Error Categories and Responses

**Category 1: Implementation Errors (Fixable)**
- Examples: `AttributeError`, `KeyError`, `NameError`
- Response: @code_translator fixes → Resume training

**Category 2: Data Errors (Fixable)**
- Examples: `ValueError: Input contains NaN`, `KeyError: 'column_name'`
- Response: @data_engineer fixes data → Resume training

**Category 3: Resource Errors (Fixable)**
- Examples: `MemoryError`, `CUDA out of memory`
- Response: @code_translator optimizes → Resume training

**Category 4: Convergence Errors (May need @modeler)**
- Examples: `RuntimeWarning: Maximum iterations reached`, `R-hat > 1.1`
- Response: @modeler consulted → Adjust → Resume training

## Status Reporting Protocol

**Regular Updates (Every 30 minutes)**:

```
@model_trainer: "Phase 5B Training Status Update

Model: {i}
PID: {pid}
Elapsed: {time} / ~12h ({percentage}% complete)
Log file: output/implementation/logs/training_{i}_full.log
Status: ✅ Running normally
Last log line: [most recent entry]

No errors detected. Continuing monitoring..."
```

**Completion Report**:

```
@model_trainer: "✅ Phase 5B Training Complete

Model: {i}
Status: SUCCESS

Training Summary:
- Total time: {elapsed_time}
- Samples: {samples_generated}
- Chains: {num_chains}
- Convergence: {r_hat_stats}

Output Files:
- Results: output/results/results_{i}.csv
- Model: output/implementation/models/model_{i}_full.pkl
- Log: output/implementation/logs/training_{i}_full.log

Errors Encountered and Resolved:
1. {Error 1} → {Resolution}
2. {Error 2} → {Resolution}

Ready for Phase 5.5 validation"
```

## No-Exit Guarantee

**CRITICAL RULES**:

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

## Timeout Protection

**If training takes longer than expected**:

```
@model_trainer: "⚠️ TIMEOUT WARNING

Model: {i}
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

## Summary

**Watch Mode Protocol**:
1. Start training in background (capture PID)
2. Enter watch mode (NO EXIT)
3. Monitor log file for errors (every 60 seconds)
4. Report status every 30 minutes
5. Error detected → Report to @director immediately
6. Await fix → Resume training
7. Completion → Report summary

**Key Files**:
- Log: `output/implementation/logs/training_{i}_full.log`
- Results: `output/results/results_{i}.csv`
- Model: `output/implementation/models/model_{i}_full.pkl`
