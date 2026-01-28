# Protocol 10: Phase 5B Error Monitoring

> **Purpose**: Prevent errors from being lost by keeping AI session active during training with watch mode
> **Owner**: @model_trainer
> **Scope**: Phase 5B (Full Training)

## Problem Statement

Training errors go undetected until too late:

```
@model_trainer: "Starting training...will take 12 hours"
[AI session exits]
[12 hours later]
@director: "How did training go?"
@model_trainer: "It crashed at hour 2 with CUDA error"
Result: 10 hours wasted, restart from scratch
```

## Rules

### Rule 1: AI Session Does NOT Exit

**Training runs in background**
**@model_trainer enters "watch mode"**
**Session stays active, monitoring for errors**

```
@model_trainer: "Starting Phase 5B full training.
Estimated: 12 hours.
Entering watch mode - session will remain active.
Will report errors immediately."
```

### Rule 2: Watch Mode Implementation

**Watch mode code**:
```python
def watch_mode(training_process, log_file, check_interval=60):
    """
    Monitor training process and log file for errors.

    Args:
        training_process: Subprocess running training
        log_file: Path to training log
        check_interval: Seconds between checks (default: 60)
    """
    while True:
        # Check process status
        poll_result = training_process.poll()

        if poll_result is not None:
            # Process finished
            if poll_result == 0:
                log_completion()
                break
            else:
                # Process failed
                log_error(f"Training process failed with code {poll_result}")
                report_to_director()
                break

        # Check log file for errors
        errors = check_log_for_errors(log_file)
        if errors:
            for error in errors:
                log_error(error)
                report_to_director(error)

        # Check if training complete (via log)
        if is_training_complete(log_file):
            log_completion()
            break

        # Wait before next check
        sleep(check_interval)
```

**Error detection patterns**:
```
ERROR patterns:
- "Error:", "ERROR:", "Exception:"
- "CUDA error", "GPU out of memory"
- "KeyError:", "ValueError:", "TypeError:"
- "RuntimeError:", "MemoryError:"
- "NaN detected", "Inf detected"
- "Divergence detected", "R-hat >"
- "Sampling failed"
```

### Rule 3: Error Resolution Workflow

**Error detected → Report → Delegate → Fix → Resume**

```
1. @model_trainer detects error → Reports to @director
2. @director delegates fix:
   - Implementation error → @code_translator
   - Data error → @data_engineer
   - Design issue → @modeler
3. Fix applied → Resume training (no restart from scratch)
```

**Example**:
```
@model_trainer: "ERROR detected at hour 3:
KeyError: 'Gold' not found in features
Error in: model_1.py line 42
Training halted awaiting fix"

@director: "@code_translator: Fix KeyError in model_1.py
Design requires 'Gold' feature but data missing.
Investigate and report fix."

@code_translator: "Issue: Data has 'gold' (lowercase) not 'Gold'
Fix: Add feature name normalization
Fixed in model_1.py line 42"

@model_trainer: "Fix applied. Resuming training from checkpoint..."
```

## Watch Mode Phases

### Phase 1: Initialization (First 5 minutes)

**@model_trainer**:
- Verify training script starts
- Verify log file created
- Verify no immediate errors
- Report "Training started successfully"

### Phase 2: Monitoring (Every 60 seconds)

**@model_trainer**:
- Check process status
- Scan log file for errors
- Report status every 30 minutes
- Immediate alert on error

**Status report template**:
```
@model_trainer: "Phase 5B Status Update - Model {i}
Elapsed: 3.5 hours / Estimated: 12 hours
Progress: 29%
Errors: None detected
Sampling: Chain 1/4, 2,143/10,000 iterations
Next update: 30 minutes"
```

### Phase 3: Error Handling (Immediate)

**When error detected**:
```
@model_trainer: "⚠️ ERROR DETECTED ⚠️
Model: {i}
Time: 3.2 hours into training
Error: CUDA out of memory
Location: model_1.py line 78
Action: Training paused, awaiting @director guidance"
```

### Phase 4: Completion (Final Report)

**When training completes**:
```
@model_trainer: "✅ TRAINING COMPLETE ✅
Model: {i}
Duration: 11.8 hours / Estimated: 12 hours
Iterations: 10,000 × 4 chains
Convergence: R-hat < 1.01 (all parameters)
Results: output/results/results_1.csv
Log: output/implementation/logs/training_1.log"
```

## Checkpoint/Resume Strategy

**Before training starts**:
```python
# Set up checkpointing
pm.sample(...,
         progressbar=True,
         trace=backend,
         checkpoint_dir="output/implementation/checkpoints/model_{i}")
```

**If error occurs**:
```
1. Error detected at hour 3
2. Fix applied
3. Resume from checkpoint (hour 3)
4. NOT restart from hour 0
```

**Benefit**: Save 3 hours of re-training

## Error Categories

### Category 1: Data Errors (Quick Fix)

**Examples**:
- KeyError, ValueError (feature names)
- Missing values, NaN issues
- Data type mismatches

**Handler**: @data_engineer
**Time**: 10-30 minutes fix
**Resume**: From start (data changed)

### Category 2: Implementation Errors (Quick Fix)

**Examples**:
- Syntax errors, import errors
- Bug in code logic
- Variable name errors

**Handler**: @code_translator
**Time**: 10-30 minutes fix
**Resume**: From checkpoint if possible

### Category 3: Convergence Errors (Long Fix)

**Examples**:
- R-hat > 1.1 (non-convergence)
- Divergent transitions
- Tree depth warnings

**Handler**: @modeler (consultation)
**Time**: 1-3 hours fix
**Resume**: From checkpoint (if param change only)

### Category 4: Critical Errors (Emergency Protocol)

**Examples**:
- R-hat > 1.3 (severe non-convergence)
- No convergence after 12 hours
- >10% divergent transitions

**Handler**: Emergency Delegation (Protocol 11)
**Time**: 30-60 minutes (8× faster)
**Resume**: From checkpoint

## Status Report Frequency

**Routine updates**: Every 30 minutes
**Error alerts**: Immediate
**Completion**: Once at end

**Status report includes**:
- Elapsed time / Estimated time
- Progress percentage
- Current iteration/sampling status
- Errors (if any)
- Next update time

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
