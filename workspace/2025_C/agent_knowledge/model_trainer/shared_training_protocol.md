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
