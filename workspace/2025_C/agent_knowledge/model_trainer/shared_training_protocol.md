# Shared Training Protocol for Worker Agents

> **Purpose**: Common training logic shared by all model_trainer worker agents (1-5).
> This file is referenced by each worker to ensure consistent training execution.

---

## File Conventions

### Input Files
- `output/implementation/code/model_{i}.py` - Model code from @code_translator
- `output/implementation/data/features_{i}.pkl` - Features from @data_engineer
- `output/model/model_design_{i}.md` - Design reference from @modeler

### Output Files
- `output/implementation/data/results_{i}.csv` - Training results
- `output/implementation/logs/training_{i}.log` - Training log
- `output/implementation/logs/convergence_{i}.log` - Convergence diagnostics (if applicable)

---

## UTF-8 Enforcement (MANDATORY)

All Python file operations MUST use UTF-8 encoding:

```python
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read/write with UTF-8
df = pd.read_csv('data.csv', encoding='utf-8')
df.to_csv('output.csv', index=False, encoding='utf-8')

# Write text files
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
```

---

## Convergence Criteria

### Bayesian Models (PyMC)
- R-hat < 1.05 for all parameters
- Effective sample size > 400
- No divergences
- Chains mixed properly

### Optimization Models
- Objective function converged
- No gradient explosions
- Constraints satisfied
- Solution is stable

### Simulation Models
- All iterations completed
- Results stable across runs
- No numerical errors

---

## Sanity Checks (MANDATORY Before Saving)

Before saving `results_{i}.csv`, verify:

1. **No Negative Values** (for count data like medals)
2. **No NaN/Inf Values** in results
3. **Reasonable Ranges** (e.g., medals 0-150)
4. **Consistency Check** (Total = Gold + Silver + Bronze if applicable)

```python
def sanity_check(df):
    issues = []

    # Check for negative values
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if (df[col] < 0).any():
            issues.append(f"Negative values in {col}")

    # Check for NaN/Inf
    if df.isnull().any().any():
        issues.append("NaN values detected")
    if np.isinf(df.select_dtypes(include=['number'])).any().any():
        issues.append("Inf values detected")

    return issues
```

---

## Training Time Monitoring

```python
import time

def train_with_monitoring(model_func, *args, **kwargs):
    start_time = time.time()
    print(f"[{time.ctime()}] Training started")

    result = model_func(*args, **kwargs)

    elapsed_hours = (time.time() - start_time) / 3600
    print(f"[{time.ctime()}] Training completed in {elapsed_hours:.2f} hours")

    return result, elapsed_hours
```

---

## Error Handling

### On Training Failure
1. Document error in `output/implementation/logs/training_{i}.log`
2. Report immediately to @director
3. Do NOT proceed with fabricated data
4. Wait for fix instructions

### On Slow Training (>24 hours for single model)
1. Report progress to @director
2. Continue training (do NOT stop early)
3. Provide estimated completion time

---

## Worker Completion Report Format

Upon completion, report to @director:

```markdown
Director, Model {i} Training Complete.

## Model Summary
- Model ID: {i}
- Model Type: [type from design]
- Training Method: [Bayesian/Optimization/Simulation]

## Training Results
- Training Time: {X.XX} hours
- Convergence: ✅ Achieved / ❌ Failed
- Iterations Completed: {N}

## Output Files
- results_{i}.csv: ✅ Created ({rows} rows, {cols} columns)
- training_{i}.log: ✅ Created
- convergence_{i}.log: ✅ Created (if applicable)

## Sanity Checks
- No negative values: ✅
- No NaN/Inf: ✅
- Reasonable ranges: ✅

## Status
COMPLETE - Ready for next model or Phase 5.5 validation.
```

---

## Zero Tolerance Policy

**ABSOLUTE REQUIREMENTS**:
- ❌ NO partial results
- ❌ NO data fabrication
- ❌ NO early stopping without convergence
- ❌ NO proceeding with failures

**MUST DO**:
- ✅ Wait for full convergence
- ✅ Verify all sanity checks pass
- ✅ Report failures immediately
- ✅ Document everything in logs

---

## Reference Files

For additional details, consult:
- `watch_mode_protocol.md` - Watch mode for long training
- `emergency_convergence_fix.md` - Critical failure handling
- `sanity_checks.md` - Detailed validation logic
- `o_award_training.md` - O Award documentation guidelines

---

## Enhanced Anti-Fraud Protocol (v3.2.0)

> [!CRITICAL] **All training workers MUST follow this protocol to ensure data authenticity.**

### Pre-Training Verification

Before starting training:

1. **Record phase start time via time_tracker.py**:
   ```bash
   python tools/time_tracker.py start --phase 5 --agent model_trainer{N}
   ```

2. **Verify input integrity**:
   ```python
   # Check features file hash
   import hashlib
   with open('features_{i}.pkl', 'rb') as f:
       input_hash = hashlib.md5(f.read()).hexdigest()
   print(f"Input hash: {input_hash}")
   ```

3. **Record expected metrics**:
   - Expected training time (from model_design)
   - Expected convergence criteria
   - Expected output dimensions

### During Training

1. **Continuous logging** (every 60 seconds):
   ```python
   import time
   import json

   def log_progress(epoch, loss, elapsed_time, log_file):
       entry = {
           "timestamp": time.time(),
           "epoch": epoch,
           "loss": loss,
           "elapsed_seconds": elapsed_time
       }
       with open(log_file, 'a', encoding='utf-8') as f:
           f.write(json.dumps(entry) + '\n')
   ```

2. **Training markers** (non-fakeable):
   - GPU/CPU utilization logs
   - Memory usage over time
   - Intermediate checkpoint files with timestamps

### Post-Training Verification

1. **Record phase end time**:
   ```bash
   python tools/time_tracker.py end --phase 5 --agent model_trainer{N}
   ```

2. **Time authenticity check**:
   ```python
   # Verify log entries are temporally consistent
   with open('training_log.jsonl', encoding='utf-8') as f:
       entries = [json.loads(line) for line in f]

   # Check time spacing (should be ~60s between entries)
   for i in range(1, len(entries)):
       gap = entries[i]['timestamp'] - entries[i-1]['timestamp']
       if gap < 30 or gap > 120:
           print(f"SUSPICIOUS: {gap}s gap at entry {i}")
   ```

3. **Result consistency check**:
   ```python
   # Verify results match expected dimensions and ranges
   results = pd.read_csv('results_{i}.csv', encoding='utf-8')

   # Check dimensions
   assert results.shape[0] > 0, "Empty results"

   # Check for synthetic patterns
   # Real training has noise; fake data is often too clean
   std_per_column = results.std()
   if (std_per_column == 0).any():
       print("SUSPICIOUS: Zero variance columns detected")
   ```

4. **Checkpoint verification**:
   - Verify intermediate checkpoints exist
   - Compare checkpoint timestamps with log timestamps
   - Verify model weights change between checkpoints

### Red Flags (Automatic Rejection by @time_validator)

| Red Flag | Detection | Action |
|----------|-----------|--------|
| Training < 30% expected time | time_tracker.py validation | REJECT, rerun |
| No intermediate checkpoints | Missing files | REJECT, investigate |
| Temporal gaps in logs | Log analysis | REJECT, investigate |
| Zero-variance columns | Stats check | REJECT, investigate |
| Results before training | Timestamp mismatch | REJECT, investigate |
| Log entries too close together | <30s gaps | REJECT, investigate |

### Self-Timing Protocol (Mandatory for ALL Workers)

#### At Phase Start

1. Record start time via time_tracker.py:
   ```bash
   python tools/time_tracker.py start --phase 5 --agent model_trainer{N}
   ```

2. Also log internally:
   ```python
   import time
   phase_start = time.time()
   print(f"[{time.ctime()}] Training started for Model {i}")
   ```

#### At Phase End

1. Record end time via time_tracker.py:
   ```bash
   python tools/time_tracker.py end --phase 5 --agent model_trainer{N}
   ```

2. Include duration in completion report:
   ```markdown
   ## Timing
   - Start: {ISO timestamp}
   - End: {ISO timestamp}
   - Duration: {XX} minutes
   - Expected: {min}-{max} minutes
   ```

### Consultation Export (Mandatory)

After training completes, export consultation document:

```bash
# Generate timestamp
TIMESTAMP=$(date +%Y-%m-%dT%H-%M-%S)

# Create consultation file
echo "Creating: output/docs/consultations/phase_5_model_trainer{N}_${TIMESTAMP}.md"
```

Document must include:
- Training duration
- Model type and parameters
- Convergence status
- Output files created
- Any issues encountered
