# Platform-Adaptive Sampling Configuration

> **Purpose**: This knowledge file documents the mandatory platform-adaptive sampling protocol. Code translators MUST implement platform-specific configurations to ensure the system works efficiently on both Linux and Windows platforms.
>
> **Source**: Extracted from code_translator.md lines 370-466
>
> **Critical**: This prevents Windows systems from being 4× slower than Linux by using NumPyro backend when appropriate, or adjusting sampling parameters for PyMC.

---

## 🔧 Platform-Adaptive Sampling

> [!CRITICAL]
> **[MANDATORY] You MUST use platform-adaptive sampling for ALL training code.**
>
> This ensures the system works efficiently on BOTH Linux and Windows platforms.

### Platform Detection and Configuration

**At the TOP of EVERY model file**, after imports:

```python
# Platform-adaptive sampling
from implementation.code.platform_adaptive_sampling import PlatformAdaptiveSampler

# Get optimal config for current platform
sampler_config = PlatformAdaptiveSampler().get_optimal_config(n_chains=4)

print(f"Platform: {sampler_config['platform']}")
print(f"Expected training time: {sampler_config['expected_hours']} hours")
print(f"Parallel sampling: {sampler_config['parallel']}")
```

### Conditional Backend Selection

**If NumPyro recommended for Windows** (faster):

```python
if sampler_config.get('use_numpyro'):
    # Use NumPyro for Windows (same speed as Linux)
    import numpyro
    import numpyro.distributions as dist
    from jax import random
    from numpyro.infer import MCMC, NUTS

    def model_func(features, target=None):
        # Define model using NumPyro API
        # ... (similar to PyMC but with NumPyro syntax)
        pass

    # Sample with NumPyro
    kernel = NUTS(model_func)
    mcmc = MCMC(kernel, num_warmup=sampler_config['tune'],
                num_samples=sampler_config['draws'],
                num_chains=sampler_config['chains'])
    mcmc.run(random.PRNGKey(0), features, target)

else:
    # Use PyMC (Linux or optimized Windows)
    import pymc as pm

    with pm.Model() as model:
        # Define model using PyMC API
        # ... (standard PyMC code)
        pass

        # Sample with platform-optimal config
        trace = pm.sample(
            draws=sampler_config['draws'],
            tune=sampler_config['tune'],
            chains=sampler_config['chains'],
            cores=sampler_config['cores'],
            target_accept=sampler_config['target_accept']
        )
```

### Verification

**After implementing platform-adaptive sampling**:

```python
# Verify config meets constraints
if sampler_config['platform'] == 'Windows':
    assert sampler_config['expected_hours'] <= 20.0, "Windows config too slow!"
    if sampler_config.get('use_numpyro'):
        assert sampler_config['expected_hours'] == 5.0, "NumPyro should match Linux speed"
    print("✅ Windows configuration acceptable")
elif sampler_config['platform'] == 'Linux':
    assert sampler_config['expected_hours'] == 5.0, "Linux should be fastest"
    print("✅ Linux configuration optimal")
```


### Mandatory Platform Config Table

You MUST verify your implementation matches this table:

| Platform | Algorithm | Config | Expected Time | Action |
|----------|-----------|--------|---------------|--------|
| Linux | PyMC | chains=4, cores=4 | 5h/model | ✅ Proceed |
| Windows | NumPyro | chains=4, cores=4 | 5h/model | ✅ Proceed |
| Windows | PyMC | chains=2, cores=1, draws=20000 | 20h/model | ⚠️ Accept if ≤2 models |
| macOS (M1/M2) | PyMC | chains=4, cores=4 | 4h/model | ✅ Proceed |
| macOS (Intel) | PyMC | chains=2, cores=1 | 20h/model | ⚠️ Accept if ≤2 models |

**If your config doesn't match**: Report to @director immediately.
