# Phase 5B Timeline Management Protocol

**Version**: 1.0
**Date**: January 28, 2026
**Purpose**: Strategic decision framework for handling Phase 5B training timeline overruns

---

## Problem Statement

Phase 5B full training requires 80-112 hours on Windows (vs 20-28 hours on Linux), potentially exceeding the 72-hour competition window.

### Root Causes

1. **Windows PyMC multiprocessing incompatibility**: 5× slowdown vs Linux
2. **Complex Bayesian models**: 5 models with 40K+ MCMC samples each
3. **Convergence issues**: Re-sampling required when R-hat > 1.05
4. **No early stopping**: Fixed iteration counts regardless of convergence

---

## Pre-Competition Assessment (Phase 0)

**Checklist** (complete BEFORE starting Phase 1):

- [ ] **Platform**: Windows or Linux? (Run `python -c "import platform; print(platform.system())"`)
- [ ] **Algorithm**: PyMC, NumPyro, Stan, or other?
- [ ] **Model count**: How many models? (affects total training time)
- [ ] **Complexity**: Iterations, chains, parameters per model?
- [ ] **Deadline**: Hard 72-hour deadline or flexible?

### Platform Detection Script

```python
import platform
import os

print("=" * 60)
print("PLATFORM DETECTION")
print("=" * 60)
print(f"OS: {platform.system()}")
print(f"CPU cores: {os.cpu_count()}")
print(f"Architecture: {platform.machine()}")

# Check for PyMC/NumPyro availability
try:
    import pymc
    print("✅ PyMC available")
except ImportError:
    print("❌ PyMC not available")

try:
    import numpyro
    print("✅ NumPyro available")
except ImportError:
    print("❌ NumPyro not available (install for Windows speedup)")

# Estimate training time
if platform.system() == 'Windows':
    try:
        import numpyro
        print("\n📊 Estimated training time (NumPyro): 5-6 hours per model")
    except ImportError:
        print("\n📊 Estimated training time (PyMC): 16-22 hours per model")
        print("⚠️  RECOMMENDATION: Install NumPyro for 4× speedup")
elif platform.system() == 'Linux':
    print("\n📊 Estimated training time (PyMC): 4-6 hours per model")
else:
    print("\n📊 Platform not recognized - assuming worst case")
```

---

## Decision Tree

```
START
  │
  ├─→ Linux + PyMC → Option 1: Native training (4-6h/model) ✅
  │
  ├─→ Windows + PyMC
  │   ├─→ 72h deadline?
  │   │   ├─→ YES → Option 3: Reduce iterations (8-12h/model) ⚠️
  │   │   └─→ NO → Option 4: Parallel workflow (submit with 5A) ✅
  │   │
  │   └─→ NumPyro available?
  │       ├─→ YES → Option 2: NumPyro migration (5-6h/model) ✅
  │       └─→ NO → Install NumPyro or use Option 4
  │
  └─→ Other algorithms → Assess case-by-case
```

---

## Strategic Options

### Option 1: Native Linux Training (RECOMMENDED - Best Performance)

**Approach**: Use Linux environment for optimal PyMC performance

**Pros**:
- 5× speed improvement vs Windows PyMC (80-112h → 16-22h)
- Native multiprocessing support
- Better convergence with parallel chains
- No code changes needed

**Cons**:
- Requires Linux access
- Data transfer overhead
- Platform testing required

**Implementation Options**:

#### Option 1A: WSL2 (Windows Subsystem for Linux)

```bash
# Install WSL2 on Windows
wsl --install -d Ubuntu

# Inside WSL2 Ubuntu:
sudo apt update
sudo apt install python3 python3-venv
python3 -m venv venv
source venv/bin/activate
pip install pymc numpy pandas

# Run training (full parallel speed)
python output/implementation/code/model_1.py
```

#### Option 1B: Google Colab (Free Linux CPU/GPU)

```python
# Upload model file to Colab
# Run in notebook:
!pip install pymc
!python model_1.py

# Download results when complete
from google.colab import files
files.download('results_1.csv')
```

#### Option 1C: Cloud VM (AWS/GCP/Azure)

- Spin up Linux VM (Ubuntu 20.04, 4-8 cores)
- Install dependencies: `pip install pymc numpy pandas`
- Upload data/code: `scp -r output/ user@vm:/home/user/`
- Run training at full speed
- Download results: `scp user@vm:/home/user/output/results_*.csv ./`

**Timeline Impact**: Fits within 72 hours (5 models × 5h = 25h total)

**Verdict**: ✅ **RECOMMENDED** if Linux access available

---

### Option 2: NumPyro Migration (RECOMMENDED - Windows Solution)

**Approach**: Switch PyMC → NumPyro (better Windows support via JAX)

**Pros**:
- Windows-optimized JAX backend
- GPU acceleration possible (if needed)
- 4-5× faster than PyMC on Windows (same speed as Linux)
- Identical NUTS sampler implementation

**Cons**:
- Requires code rewrite (5 models × ~500 lines each)
- Learning curve for NumPyro API
- 2-3 hours development time
- Risk of new bugs

**Migration Steps**:

1. **Install NumPyro**:
   ```bash
   pip install numpyro jax[cpu]
   ```

2. **Use platform-adaptive sampling** (already implemented):
   ```python
   from implementation.code.platform_adaptive_sampling import PlatformAdaptiveSampler

   sampler_config = PlatformAdaptiveSampler().get_optimal_config(n_chains=4)

   if sampler_config['use_numpyro']:
       # Use NumPyro (Windows fast path)
       import numpyro
       import numpyro.distributions as dist
       from jax import random
       from numpyro.infer import MCMC, NUTS

       def model_func(features, target=None):
           # NumPyro model definition
           pass

       kernel = NUTS(model_func)
       mcmc = MCMC(kernel, num_warmup=2000, num_samples=10000, num_chains=4)
       mcmc.run(random.PRNGKey(0), features, target)
   ```

3. **Verify performance matches Linux**:
   ```python
   assert sampler_config['expected_hours'] == 5.0, "NumPyro should match Linux speed"
   ```

**Reference**: See `docs/pymc_to_numpyro_migration_guide.md` for detailed migration guide

**Timeline Impact**: 2-3h dev + 20-28h training = 22-31h total (acceptable)

**Verdict**: ✅ **RECOMMENDED** for Windows users without Linux access

---

### Option 3: Iteration Reduction (FALLBACK - Quality Risk)

**Approach**: Reduce MCMC iterations to meet deadline

**Current**: 2000 tune + 10000 draws = 12000 samples/chain × 4 chains = 48000 samples
**Reduced**: 1000 tune + 5000 draws = 6000 samples/chain × 4 chains = 24000 samples

**Pros**:
- Simple parameter change
- 2× faster (80-112h → 40-56h)
- Fits 72-hour window
- No code rewrite

**Cons**:
- Reduced convergence quality
- Wider prediction intervals
- Must verify R-hat < 1.05 still achieved
- May need more tuning iterations

**Acceptance Criteria**:

```python
# After training, verify convergence:
import arviz as az

# Load trace
trace = az.from_netcdf('trace.nc')

# Check R-hat
r_hat = az.rhat(trace).x
assert np.all(r_hat < 1.05), "R-hat too high - increase iterations"

# Check ESS (effective sample size)
ess = az.ess(trace).x
assert np.all(ess > 400), "ESS too low - increase draws"

print("✅ Convergence checks passed with reduced iterations")
```

**Implementation**:

```python
# In model_{i}.py, modify sampling parameters:
trace = pm.sample(
    draws=5000,      # Reduced from 10000
    tune=1000,       # Reduced from 2000
    chains=4,
    cores=1,         # Windows limitation
    target_accept=0.95
)
```

**Timeline Impact**: 5 models × 8-12h = 40-60h total (fits 72h)

**Verdict**: ⚠️ **ACCEPTABLE** if NumPyro migration not possible, but verify convergence

---

### Option 4: Parallel Early-Stage Training (CURRENT REALITY)

**Approach**: Run Phase 5A (quick) + Phase 6-7 (paper) in parallel with Phase 5B (full)

**Current Workflow** (Sequential):
```
Phase 5A (30 min) → Phase 5B (80h) → Phase 6 (30 min) → Phase 7 (3h) = 84 hours
```

**Optimized Workflow** (Parallel):
```
Phase 5A (30 min) → [Phase 5B (80h) || Phase 6+7 (3.5h)] = 80.5 hours
                       ↓
                 Continue in background,
                 update paper when complete
```

**Pros**:
- No algorithm changes
- Full-quality training
- Paper submitted on time (with quick results)
- Full results ready ~8 hours after submission (can be updated if allowed)

**Cons**:
- Submission uses quick results (not full convergence)
- Last-minute paper update stressful
- May miss submission window if Phase 5B delayed

**Implementation** (Automatic Rule 3):

```python
# @director automatically executes this workflow:
Phase 5A complete → Launch Phase 5B in background → IMMEDIATELY proceed to Phase 6-7

# Phase 5B background execution:
@model_trainer: Run full training in background (run_in_background=True)
@director: Monitor progress every 2 hours
@writer: Update paper when Phase 5B completes (if time permits)
```

**Timeline**: ~35 hours to submission-ready draft, full results when complete

**Verdict**: ✅ **ALREADY IMPLEMENTED** (Automatic Rule 3)

---

## Protocol Enforcement

### Phase 0.5 (Methodology Gate)

**@advisor must ask**:

1. "What platform will training run on?"
2. "What is the total expected training time?"
3. "Does this fit the 72-hour window?"

**If NO** → @director MUST choose option before Phase 4.

### Phase 2 (Feasibility Check)

**@feasibility_checker must run**:

```python
check_training_timeline(platform, algorithm, model_count, iterations)
# Returns: hours_needed, fits_deadline (bool), recommended_option
```

**Document decision in**: `output/docs/training_strategy.md`

### Decision Documentation Template

```markdown
# Training Strategy Decision

## Platform Assessment
- **OS**: [Windows/Linux/macOS]
- **CPU Cores**: [count]
- **Algorithm**: [PyMC/NumPyro/Other]
- **NumPyro Available**: [Yes/No]

## Timeline Analysis
- **Models**: [count]
- **Estimated Time per Model**: [hours]
- **Total Training Time**: [hours]
- **Fits 72h Deadline**: [Yes/No]

## Decision
**Selected Option**: [1/2/3/4]

**Rationale**:
- [Why this option was chosen]
- [Trade-offs accepted]
- [Risk mitigation strategies]

## Implementation Plan
- [Step 1]
- [Step 2]
- [Step 3]

## Contingency Plan
If training exceeds timeline:
- [Fallback strategy]
- [Communication plan]
```

---

## Communication to Team

**If Option 4 (Parallel workflow) chosen**:

```
@writer: Use Phase 5A quick results for initial paper draft.
         Update with Phase 5B full results when available.

@visualizer: Generate figures from Phase 5A results.
             Regenerate when Phase 5B completes.

@summarizer: Draft summary with quick results.
             Update numbers before final submission.
```

**If Option 2 (NumPyro migration) chosen**:

```
@code_translator: Migrate all models to NumPyro (use platform-adaptive sampling).
                 Ensure fallback to PyMC if NumPyro unavailable.

@model_trainer: Test NumPyro sampling on Model 1 first.
                Verify convergence matches PyMC expectations.

@validator: Validate NumPyro implementation produces equivalent results.
```

---

## Verification Tests

### Test 1: Platform Detection

```python
from implementation.code.platform_adaptive_sampling import PlatformAdaptiveSampler

sampler = PlatformAdaptiveSampler()
config = sampler.get_optimal_config(n_chains=4)

print(f"Platform: {config['platform']}")
print(f"Expected time per model: {config['expected_hours']} hours")
print(f"Parallel: {config['parallel']}")

# Verify constraints
if config['platform'] == 'Windows':
    assert config['expected_hours'] <= 20.0, "Windows config too slow!"
    if config.get('use_numpyro'):
        assert config['expected_hours'] == 5.0, "NumPyro should match Linux"
    print("✅ Windows configuration acceptable")
elif config['platform'] == 'Linux':
    assert config['expected_hours'] == 5.0, "Linux should be fastest"
    print("✅ Linux configuration optimal")
```

### Test 2: Timeline Estimation

```python
# Estimate total training time
num_models = 5
hours_per_model = config['expected_hours']
total_hours = num_models * hours_per_model

print(f"\n📊 Timeline Estimate:")
print(f"   Models: {num_models}")
print(f"   Hours per model: {hours_per_model}")
print(f"   Total training time: {total_hours} hours")
print(f"   Fits 72h deadline: {'✅ YES' if total_hours <= 72 else '❌ NO'}")

if total_hours > 72:
    print(f"\n⚠️  WARNING: Training exceeds 72-hour deadline by {total_hours - 72} hours")
    print("   Recommend: Use Option 2 (NumPyro) or Option 4 (Parallel workflow)")
```

---

## Summary and Recommendations

| Option | Platform | Time per Model | Total Time (5 models) | Quality | Verdict |
|--------|----------|----------------|----------------------|---------|---------|
| **1: Linux** | Linux | 4-6h | 20-30h | Full | ✅ **BEST** (if available) |
| **2: NumPyro** | Windows | 5-6h | 25-30h | Full | ✅ **RECOMMENDED** (Windows) |
| **3: Reduce** | Windows | 8-12h | 40-60h | Reduced | ⚠️ **FALLBACK** (verify convergence) |
| **4: Parallel** | Any | N/A | 35h to draft | Full (eventually) | ✅ **DEFAULT** (auto-implemented) |

**Decision Matrix**:

1. **Linux available?** → Use Option 1 (native training)
2. **Windows only?** → Use Option 2 (NumPyro migration) OR Option 4 (parallel workflow)
3. **Tight deadline?** → Use Option 4 (submit with 5A, update later)
4. **Quality critical?** → Use Option 1 or 2 (full training)

**Key Principle**: Never sacrifice data integrity (Protocol 26) or model completeness (Protocol 27) for timeline speed. Use platform-optimized solutions instead.
