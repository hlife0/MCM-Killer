# Design Expectations Comparison Methodology

**Purpose**: This document extracts the systematic comparison table methodology for validating implementation fidelity. It provides the step-by-step process for comparing design specifications against actual implementation.

**Source**: time_validator.md (lines 221-425)
**Version**: v2.5.7
**Status**: Active - MANDATORY for Phase 4.5 validation

---

## 📊 Enhanced Analysis Protocol (v2.5.7)

> **[CRITICAL] Your time predictions have been wrong by 22× (16h predicted, 43min actual). You MUST read more files and analyze code line-by-line.**

### Phase 1.5: Time Estimate Validation (ENHANCED)

**OLD APPROACH (WRONG)**:
- Read only `model_design.md`
- Use generic time estimates
- Miss algorithm simplifications
- Result: 22× error

**NEW APPROACH (v2.5.7 REQUIRED)**:

#### Step 1: Read 3 File Types (MANDATORY)

**File 1: Model Design**
- Path: `output/model/model_design_{i}.md`
- Extract: Algorithm, iterations, complexity

**File 2: Dataset** (NEW - CRITICAL)
- Path: `output/implementation/data/features_{i}.pkl`
- Extract: Shape (rows × columns), memory size, data types
- Example: 5000 rows × 50 columns = 2.5 MB

**File 3: Implementation Code** (NEW - CRITICAL)
- Path: `output/implementation/code/model_{i}.py`
- Extract: Library, algorithm, iterations, loops
- Example: `pm.sample(draws=10000, tune=2000, chains=4)`

#### Step 2: Line-by-Line Code Analysis (MANDATORY)

> **[CRITICAL] You MUST compare model_design.md (设计) with model_{i}.py (实现)逐项对照**

**Process**:
1. Read `model_design_{i}.md` FIRST - Extract design specifications
2. Read `model_{i}.py` SECOND - Extract implementation details
3. **COMPARE** each design item with implementation - Detect any discrepancies
4. **REJECT** if implementation doesn't match design (lazy/simplified)

For each `model_{i}.py`, analyze:

**Design vs Code Comparison Checklist**:

1. **Import statements** (lines 1-10):
   ```python
   # DESIGN (from model_design.md):
   # "Use PyMC v5 with HMC sampling"

   # CODE CHECK:
   import pymc as pm  # ← CORRECT: PyMC
   # NOT: from sklearn.linear_model import LinearRegression  # ← WRONG: Simplified

   # VERDICT: ✅ MATCH if PyMC, ❌ LAZY if sklearn
   ```

2. **Data loading** (lines 10-20):
   ```python
   # DESIGN:
   # "Features: Gold, Silver, Bronze, years, host_country, GDP_per_capita..."
   # "Total: 15 features"

   # CODE CHECK:
   data = pd.read_pickle('features_1.pkl')
   rows, cols = data.shape  # ← Extract: 5000 × 50
   designed_features = ['Gold', 'Silver', 'Bronze', 'years', 'host_country', ...]
   actual_features = data.columns.tolist()

   # VERIFY: Are all designed features in actual_features?
   missing = set(designed_features) - set(actual_features)
   if missing:
       return ❌ INCOMPLETE (missing features)

   # VERDICT: ✅ COMPLETE if all features present, ❌ INCOMPLETE if missing
   ```

3. **Model definition** (lines 20-50):
   ```python
   # DESIGN:
   # "Hierarchical Bayesian model with 3 levels"
   # "Priors: Normal(0, 10)"

   # CODE CHECK:
   with pm.Model() as model:
       alpha = pm.Normal('alpha', mu=0, sigma=10)  # ← Matches design ✅
       beta = pm.Normal('beta', mu=0, sigma=10, shape=15)  # ← 15 features

   # VERIFY: Is structure hierarchical? Are priors correct?
   # VERDICT: ✅ MATCH if structure matches, ❌ LAZY if simplified
   ```

4. **Sampling parameters** (lines 50-60) - **CRITICAL**:
   ```python
   # DESIGN (from model_design.md):
   # "MCMC sampling: 10000 draws, 2000 tune, 4 chains"
   # "Total: 40000 samples"

   # CODE CHECK:
   trace = pm.sample(
       draws=10000,  # ← Extract: 10000 samples
       tune=2000,    # ← Extract: 2000 tuning steps
       chains=4,     # ← Extract: 4 chains
       cores=4
   )
   # Total: 40000 samples

   # VERIFY: Does code match design exactly?
   # VERDICT: ✅ MATCH if parameters match, ❌ REDUCED if less than 80%
   ```

5. **Loops** (anywhere) - Check complexity:
   ```python
   # O(n) loop → OK
   for i in range(len(data)):
       result[i] = compute(data[i])

   # O(n²) nested loop → EXPONENTIAL TIME
   for i in range(len(data)):
       for j in range(len(features)):
           result[i][j] = compute_slow(data[i], features[j])

   # DESIGN CHECK: Did design specify O(n²) complexity?
   # If not → ❌ UNEXPECTED COMPLEXITY (may indicate inefficient implementation)
   ```

#### Step 3: Use Empirical Time Estimation Table (NOT GUESSES)

| Algorithm | Dataset Size | Samples/Chains | Expected Time |
|-----------|--------------|----------------|---------------|
| sklearn.LinearRegression | ANY | ANY | **<0.1 hours** |
| PyMC simple | 1000×10 | 1000×2 | **0.5-1 hours** |
| PyMC simple | 5000×50 | 1000×4 | **2-3 hours** |
| PyMC simple | 5000×50 | 10000×4 | **6-8 hours** |
| **PyMC hierarchical** | **1000×10** | **1000×2** | **1-2 hours** |
| **PyMC hierarchical** | **5000×50** | **1000×4** | **3-4 hours** |
| **PyMC hierarchical** | **5000×50** | **10000×4** | **12-15 hours** |
| PyMC complex | 5000×50 | 10000×4 | **15-20 hours** |
| Neural Network | 5000×50 | 100 epochs | **2-4 hours** |
| XGBoost | 5000×50 | 1000 trees | **0.5-1 hours** |

**Target accuracy**: ±50% of actual (not 22× error)

#### Step 4: 48-Hour Escalation (NEW)

If total estimate > 48 hours:
```
⚠️ 48-HOUR THRESHOLD EXCEEDED

Total estimate: 78 hours
Models:
- Model 1: 15 hours (PyMC hierarchical, 5000×50, 10000×4)
- Model 2: 18 hours (PyMC hierarchical, 5000×50, 10000×4)
- Model 3: 20 hours (Ensemble, 4 models)
- Model 4: 25 hours (Neural Network + PyMC)

Algorithm fidelity: ✓ All match designs
Feature completeness: ✓ All features present
Issue: Model complexity (not lazy implementation)

Recommendation: ESCALATE_TO_DIRECTOR

Competition time remaining: [CHECK with @director]
Options:
1. PROCEED: If ≥90 hours remaining
2. PROCEED_WITH_CAUTION: If ≥78 hours remaining
3. CONSULT_MODELER: If <78 hours remaining
```

---
