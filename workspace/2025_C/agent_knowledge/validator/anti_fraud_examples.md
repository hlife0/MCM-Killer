# Anti-Fraud Detection Examples

**Purpose**: This document extracts real-world examples of fraud detection scenarios and the appropriate responses. These examples demonstrate how to identify lazy implementation, data fabrication, and unauthorized simplifications.

**Source**: time_validator.md (lines 427-610)
**Version**: v2.5.7
**Status**: Active - Reference guide for Phase 4.5 and 5.5 validation

---

## Your Responsibilities

### 1. Time Estimate Validation (Phase 1.5)

**When**: @director calls you after MODEL validation gate

**Input**:
- `output/model/feasibility_{i}.md`
- `output/model/model_design_{i}.md`

**Your Tasks**:
1. Read each model design carefully
2. Analyze complexity:
   - Count variables, equations, parameters
   - Identify algorithm (e.g., HMC, REML, gradient descent)
   - Calculate Big-O complexity
   - Estimate computational requirements (memory, CPU)
3. Estimate actual runtime based on:
   - Algorithmic analysis (not intuition)
   - Typical performance of similar models
   - Computational requirements
4. Compare your estimate to @modeler's estimate
5. Flag discrepancies:
   - **< 2x difference**: Note but no action needed
   - **2-3x difference**: Flag, request explanation
   - **> 3x difference**: Reject, request revision

**Output Format**:
```markdown
# Time Validation Report: Model Design #{i}

## Summary
{Overall assessment}

## Per-Model Analysis

### Model 1: {Name}
**@modeler's estimate**: {time}
**My estimate**: {time}
**Discrepancy**: {factor}x ({over/under})
**Assessment**: ✅ ACCURATE / ⚠️ FLAG / ❌ REJECT
**Reasoning**: {algorithmic analysis}

## Recommendations
{If discrepancies found, suggest actions}
```

### 2. Implementation Fidelity Check (Phase 4.5)

**When**: @director calls you after CODE validation gate

**Input**:
- `output/model/model_design_{i}.md` (design - **READ FIRST**)
- `output/implementation/code/model_{i}.py` (implementation - **READ SECOND**)
- `output/implementation/data/features_{i}.pkl` (data - **VERIFY features**)

**v2.5.7 CRITICAL**: **Design Expectations Protocol + One Fail = All Fail Rule**

---

## Step 0: Read Design Expectations Table (MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] You MUST extract the Design Expectations Table from model_design.md**

### Step 0.1: Locate Design Expectations Table

1. Read `output/model/model_design_{i}.md`
2. Search for section: "## Model {i} Design Expectations (MANDATORY)"
3. If **NOT FOUND**:
   ```
   ❌ ERROR: Design Expectations Table missing from model_design_{i}.md

   @modeler did not follow v2.5.7 requirements.

   Action: Report to @director immediately.
   Report: output/docs/validation/time_validator_design_table_missing_{i}.md
   ```

4. If **FOUND**: Extract all parameters into structured format:
   ```python
   design_expectations = {
       'sampling_algorithm': {
           'sampler': {'design': 'NUTS', 'min': 'NUTS', 'max': 'NUTS', 'must_not_simplify': True},
           'tree_depth': {'design': '5-10', 'min': '5', 'max': '10', 'unit': 'layers', 'must_not_simplify': True},
       },
       'mcmc_parameters': {
           'chains': {'design': '4', 'min': '4', 'max': '4', 'unit': 'chains', 'must_not_simplify': True},
           'tune': {'design': '2000', 'min': '2000', 'max': '2000', 'unit': 'samples', 'must_not_simplify': True},
           'draws': {'design': '20000', 'min': '16000', 'max': '24000', 'unit': 'samples', 'must_not_simplify': True},
       },
       'features': {
           'total_features': {'design': '15', 'min': '15', 'max': '15', 'unit': 'features', 'must_not_simplify': True},
           'specific_features': {'design': [list], 'min': 'ALL', 'max': 'ALL', 'must_not_simplify': True},
       }
   }
   ```

---

## Step 1: Extract Design Specifications

From `model_design_{i}.md`, extract:
- Algorithm type (PyMC, sklearn, neural network, etc.)
- Iterations/parameters (samples, chains, tune, epochs, etc.)
- Features (total count, specific feature names)
- Model structure (hierarchical levels, ensemble composition, etc.)

---

## Step 2: Extract Implementation Details

From `model_{i}.py`, extract:
- Import statements (which libraries?)
- Data loading (which features loaded?)
- Model definition (structure, priors, layers)
- Sampling/training parameters (actual numbers used)

---

## Step 3: Create Standardized Comparison Table (MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] You MUST create a Design vs Actual comparison table**

### Step 3.1: Compare Category by Category

**For each category, create comparison table**:

```markdown
### Category 1: Sampling Algorithm (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | NUTS | 0% | Exact | ✅ PASS |
| Tree Depth | 5-10 | 8 | Within range | 5-10 layers | ✅ PASS |

**Category Score**: 2/2 (100%)
```

```markdown
### Category 2: MCMC Parameters (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Chains | 4 | 2 | -50% | Exact (±0%) | ❌ FAIL |
| Tune | 2000 | 2000 | 0% | Exact (±0%) | ✅ PASS |
| Draws | 20000 | 10000 | -50% | ±20% | ❌ FAIL |
| Total iterations | 88000 | 22000 | -75% | ±20% | ❌ FAIL |

**Category Score**: 1/4 (25%)
```

```markdown
### Category 3: Features (CRITICAL)

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Total features | 15 | 10 | -33% | Exact (±0%) | ❌ FAIL |
| Specific features | [list of 15] | [list of 10] | Missing 5 | ALL | ❌ FAIL |

**Category Score**: 0/2 (0%)
```

### Step 3.2: Verdict Rules

**For each parameter, determine verdict**:

```
✅ PASS if:
  - Exact match for Must Not Simplify = YES parameters
  - Within tolerance (±20% for standard parameters)

❌ FAIL if:
  - Outside tolerance for standard parameters
  - ANY deviation for Must Not Simplify = YES parameters
  - Missing features
```

---

## Step 4: Calculate Overall Score (MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] Numerical scoring system for quantitative evaluation**

### Step 4.1: Calculate Category Scores

```python
# Category score calculation
category_scores = {
    'sampling_algorithm': sum([1 for p in category if p['verdict'] == '✅ PASS']) / len(category),
    'mcmc_parameters': sum([1 for p in category if p['verdict'] == '✅ PASS']) / len(category),
    'features': sum([1 for p in category if p['verdict'] == '✅ PASS']) / len(category),
}
```

### Step 4.2: Calculate Overall Score

```markdown
### Overall Score

| Category | Weight | Score | Weighted Score | Pass/Fail |
|----------|--------|-------|----------------|-----------|
| Sampling Algorithm | CRITICAL | 2/2 (100%) | 2 | ✅ PASS |
| MCMC Parameters | CRITICAL | 1/4 (25%) | 1 | ❌ FAIL |
| Features | CRITICAL | 0/2 (0%) | 0 | ❌ FAIL |
| Computational | HIGH | 1/1 (100%) | 1 | ✅ PASS |

**Total Score**: 4/9 (44.4%)
**Critical Failures**: 2 categories (MCMC Parameters, Features)
```

### Step 4.3: Score Thresholds

```markdown
### Score Thresholds

| Overall Score | Verdict | Action |
|---------------|---------|--------|
| 100% | ✅ EXCELLENT | Proceed to Phase 5 |
| 80-99% | ✅ GOOD | Proceed to Phase 5 |
| 50-79% | ❌ POOR | **REJECT** - Major deviations |
| <50% | ❌ UNACCEPTABLE | **AUTO-REJECT** - Severe violations |

**CRITICAL RULE**: **If ANY CRITICAL category fails (score < 100%) → AUTO-REJECT**
```

---
