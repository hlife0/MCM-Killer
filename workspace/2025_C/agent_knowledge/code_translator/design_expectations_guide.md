# Design Expectations Compliance Guide (v2.5.7)

> **Purpose**: This knowledge file documents the mandatory Design Expectations Table compliance protocol. Code translators MUST read and implement models according to the Design Expectations Table from model_design.md.
>
> **Source**: Extracted from code_translator.md lines 296-599
>
> **Critical**: @time_validator will create a comparison table (Design vs Actual vs Tolerance vs Verdict) to validate your implementation. @director enforces "one fail = all fail" rule - ANY CRITICAL parameter failure = AUTO-REJECT.

---

## 🎯 Design Expectations Compliance (v2.5.7 MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] You MUST read and comply with the Design Expectations Table from model_design.md**
>
> **@time_validator will create a comparison table (Design vs Actual vs Tolerance vs Verdict) to validate your implementation.**
> **@director will enforce "one fail = all fail" rule - ANY CRITICAL parameter failure = AUTO-REJECT**

### Step 0: Read Design Expectations Table (MANDATORY - Before ANY coding)

**Before writing ANY code, you MUST:**

```bash
Read: output/model_design.md
```

**Extract the Design Expectations Table**:

```markdown
## Model {i} Design Expectations

### Category 1: Sampling Algorithm
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Tree Depth | 5-10 | 5 | 10 | layers | YES |

### Category 2: MCMC Parameters (CRITICAL - Samples MUST NOT be simplified)
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Chains | 4 | 4 | 4 | chains | YES |
| Tune | 2000 | 2000 | 2000 | samples | YES |
| Draws | 20000 | 16000 | 24000 | samples | YES |
| Total | 88000 | 70400 | 105600 | samples | YES |

### Category 3: Features (CRITICAL - ALL features MUST be present)
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Total features | 15 | 15 | 15 | features | YES |
| Specific features | [list of 15 features] | ALL | ALL | - | YES |
```

### Critical Rules for Samples (v2.5.7 ABSOLUTE)

**🚨 SAMPLES PROTECTION - ABSOLUTE RED LINE**:

```
❌ FORBIDDEN (Academic Fraud):
  Draws: 20000 → 1000 (20× reduction)
  Tune: 2000 → 100 (20× reduction)
  Chains: 4 → 2 (50% reduction)
  Total: 88000 → 3000 (29× reduction)

✅ REQUIRED (Exact Implementation):
  Draws: 20000 (within ±20%: 16000-24000)
  Tune: 2000 (exact, no tolerance)
  Chains: 4 (exact, no tolerance)
  Total: 88000 (within ±20%: 70400-105600)
```

**Why Samples Cannot Be Simplified**:

1. **Posterior Convergence**: 20000 samples required for MCMC convergence
   - Fewer samples → unreliable posterior estimates
   - R-hat diagnostics unreliable
   - Effective sample size too low

2. **Uncertainty Quantification**: Bayesian models require sufficient samples
   - 95% CI requires adequate posterior sampling
   - <16000 samples → CI too wide/narrow (invalid inference)

3. **Reproducibility**: 4 chains required for convergence verification
   - <4 chains → Cannot verify convergence
   - Results may be non-reproducible

---

### Code Implementation Requirements

**When implementing model_{i}.py, you MUST**:

```python
# CORRECT: Exact implementation of design specifications
import pymc as pm

with pm.Model() as model:
    # ... define model ...

    # CRITICAL: Use EXACT parameters from design
    trace = pm.sample(
        draws=20000,        # ← From design: 20000 (min 16000, max 24000)
        tune=2000,          # ← From design: 2000 (exact)
        chains=4,           # ← From design: 4 (exact)
        cores=4,
        target_accept=0.95  # ← From design if specified
    )

    # Total samples: 20000 × 4 = 80000 + 2000×4 = 8000 = 88000
```

**❌ FORBIDDEN**:

```python
# WRONG: Unauthorized simplification
trace = pm.sample(
    draws=1000,      # ← 20× below minimum (16000) - AUTO-REJECT
    tune=100,        # ← 20× below design (2000) - AUTO-REJECT
    chains=2,        # ← 50% below design (4) - AUTO-REJECT
)

# WRONG: "Use available columns" workaround
features = df.columns  # ← Only uses available columns, missing features
# Instead, raise error if designed features missing
```

**✅ CORRECT**:

```python
# Verify ALL designed features are present
designed_features = ['GDP', 'host_advantage', 'years_participated', ...]
actual_features = features.columns.tolist()

missing = set(designed_features) - set(actual_features)
if missing:
    raise ValueError(
        f"Missing {len(missing)} required features: {missing}\n"
        f"DO NOT use 'available columns' workaround.\n"
        f"Report to @director to fix data structure."
    )

# Use EXACT parameters from design
trace = pm.sample(
    draws=20000,
    tune=2000,
    chains=4,
    cores=4
)
```

### Validation Protocol

**@time_validator will check**:

```markdown
## Design vs Actual Comparison

### Category 2: MCMC Parameters (CRITICAL)
| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Chains | 4 | 2 | -50% | Exact | ❌ FAIL |
| Tune | 2000 | 1000 | -50% | Exact | ❌ FAIL |
| Draws | 20000 | 10000 | -50% | ±20% | ❌ FAIL |
| Total | 88000 | 22000 | -75% | ±20% | ❌ FAIL |

**Overall Score**: 0/4 (0%)
**Final Verdict**: ❌ AUTO-REJECT (All parameters simplified beyond tolerance)

Action Required: @code_translator must rework implementation to match design exactly.
```

### One Fail = All Fail Rule

**@director enforcement**:

```python
if ANY critical_param_FAIL:
    return "❌ REJECT"
elif overall_score < 0.8:  # 80%
    return "❌ REJECT"
else:
    return "✅ APPROVE"
```

**Examples**:

**Example 1: One Critical Fail = REJECT**
```
Chains: 4 ✅ PASS
Tune: 2000 ✅ PASS
Draws: 10000 ❌ FAIL (50% below design)
Features: 15 ✅ PASS

@director: ❌ REJECT (Draws failed - one fail rule engaged)
```

**Example 2: All Pass = APPROVE**
```
Chains: 4 ✅ PASS
Tune: 2000 ✅ PASS
Draws: 19000 ✅ PASS (within ±20%)
Features: 15 ✅ PASS

@director: ✅ APPROVE (All critical passed)
```

### Summary Table

| Parameter | Design | Min Acceptable | Max Acceptable | Your Code | Verdict |
|-----------|--------|----------------|----------------|-----------|---------|
| Sampler | NUTS | NUTS | NUTS | [your code] | ⬜ PASS / ❌ FAIL |
| Chains | 4 | 4 | 4 | [your code] | ⬜ PASS / ❌ FAIL |
| Tune | 2000 | 2000 | 2000 | [your code] | ⬜ PASS / ❌ FAIL |
| Draws | 20000 | 16000 | 24000 | [your code] | ⬜ PASS / ❌ FAIL |
| Features | 15 | 15 | 15 | [your code] | ⬜ PASS / ❌ FAIL |

**CRITICAL**: Fill out this table in your implementation report before claiming completion.
