# Modeler Anti-Simplification Requirements (v2.5.4)

> **Critical Enhancement**: v2.5.4
> **Purpose**: Prevent @modeler from producing lightweight models that waste token budget
> **Status**: MANDATORY for Phase 1

---

## Problem Statement

**Issue Discovered**:
```
@modeler completion metrics:
- Time worked: 40 minutes
- Expected time: 2-6 hours
- Token usage: ~30k tokens
- Expected token usage: 80-120k tokens
- Result: Models too simple for O-Prize level competition
```

**Impact**:
- Models insufficiently sophisticated
- Methodology scores suffer
- Token budget wasted
- Competition potential reduced

---

## Root Cause Analysis

### Why @modeler Oversimplifies

1. **"Degrade Don't Skip" Principle Abused**
   - v2.5.0 introduced "Tier 2 lightweight model" and "Tier 3 minimal model"
   - @modeler misinterprets this as permission to oversimplify
   - No minimum complexity requirements defined

2. **Missing Quality Standards**
   - No clear definition of "sufficiently complex model"
   - No checklist of required components
   - Director has no objective way to detect oversimplification

3. **Time Pressure Misapplied**
   - @modeler rushes to "complete quickly"
   - Misunderstands "efficient" as "minimal"
   - No correlation between work quality and time spent

---

## Solution: Modeler Quality Requirements

### Minimum Work Standards (v2.5.4)

**Expected Time Investment**: 2-6 hours (full model design)

**Token Usage Guidelines**:
- **Minimum**: 50k tokens
- **Expected**: 80-120k tokens
- **Maximum**: 200k tokens (Director should intervene if exceeded)

**Deliverable Requirements**:
- At least **3 mathematical models** (unless problem requires fewer)
- Each model must be **fully specified** (see Required Components below)
- Total model design document should be **substantial** (not 1-2 paragraphs per model)

---

## Required Model Components

### Every Model MUST Include

#### 1. Mathematical Formulation (MANDATORY)

**Complete equations in LaTeX format**

```markdown
## Mathematical Formulation

### Core Model

The relationship between response variable $Y$ and predictors $\mathbf{X}$ is modeled as:

$$
Y_i = \beta_0 + \sum_{j=1}^{p} \beta_j X_{ij} + \epsilon_i
$$

where:
- $Y_i$ is the response for observation $i$
- $\mathbf{X}_i = (X_{i1}, \ldots, X_{ip})$ are predictor variables
- $\boldsymbol{\beta} = (\beta_0, \beta_1, \ldots, \beta_p)$ are coefficients
- $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ is the error term

### Hierarchical Extension

For grouped data, we extend to hierarchical model:

$$
Y_{ij} = \beta_0 + \sum_{k=1}^{p} \beta_k X_{ijk} + u_{0j} + \sum_{k=1}^{q} u_{kj} Z_{ijk} + \epsilon_{ij}
$$

where:
- $u_{0j} \sim \mathcal{N}(0, \tau_0^2)$ are random intercepts
- $u_{kj} \sim \mathcal{N}(0, \tau_k^2)$ are random slopes
- $\epsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$ is residual error
```

**Quality Indicators**:
- ✅ Uses proper mathematical notation
- ✅ Clearly defines all symbols
- ✅ Shows derivation steps if applicable
- ✅ Includes extensions/variations
- ❌ One-line equation with no explanation
- ❌ Missing symbol definitions
- ❌ Text-only description ("use regression")

#### 2. Variables Table (MANDATORY)

**Complete variable definitions with types and ranges**

```markdown
## Variables

| Symbol | Description | Type | Range/Values | Source |
|--------|-------------|------|--------------|--------|
| $Y_{ijt}$ | Medal count for country $i$ in sport $j$ at year $t$ | Integer | $[0, \infty)$ | medal_counts.csv |
| $X_{1it}$ | GDP per capita for country $i$ at year $t$ | Continuous | $(0, \infty)$ | world_bank.csv |
| $X_{2it}$ | Population (log) for country $i$ at year $t$ | Continuous | $\mathbb{R}$ | world_bank.csv |
| $X_{3it}$ | Host nation indicator | Binary | $\{0, 1\}$ | hosts.csv |
| $X_{4it}$ | Previous medal count | Integer | $[0, \infty)$ | lagged from $Y$ |
| $\beta_0$ | Intercept coefficient | Real | $\mathbb{R}$ | To estimate |
| $\beta_1, \ldots, \beta_p$ | Slope coefficients | Real | $\mathbb{R}$ | To estimate |
| $\sigma^2$ | Residual variance | Real | $(0, \infty)$ | To estimate |
| $u_{0j}$ | Sport-specific random effect | Real | $\mathbb{R}$ | To estimate |
```

**Quality Indicators**:
- ✅ Every symbol defined
- ✅ Types specified (continuous, integer, binary, categorical)
- ✅ Ranges or values indicated
- ✅ Data sources identified
- ❌ Missing symbols
- ❌ Vague descriptions ("predictor variables")
- ❌ No type/range information

#### 3. Assumptions List (MANDATORY)

**All assumptions with justifications**

```markdown
## Assumptions

### Core Assumptions

1. **Linearity**: Relationship between predictors and response is linear
   - **Justification**: Allows interpretable coefficients; supported by exploratory analysis
   - **Validation**: Will check residual plots for non-linearity
   - **Violation handling**: Add polynomial terms or use GAM if violated

2. **Independence**: Observations are independent conditional on random effects
   - **Justification**: Countries' performances are independent given covariates
   - **Validation**: Check autocorrelation in residuals
   - **Violation handling**: Add temporal correlation structure

3. **Homoscedasticity**: Residual variance is constant across predictions
   - **Justification**: Standard assumption for linear models
   - **Validation**: Plot residuals vs fitted values
   - **Violation handling**: Use variance-stabilizing transformation

4. **Normality**: Errors are normally distributed
   - **Justification**: Enables inference (confidence intervals, p-values)
   - **Validation**: Q-Q plot of residuals
   - **Violation handling**: Use bootstrap or robust standard errors

### Data Assumptions

5. **No multicollinearity**: Predictors are not perfectly correlated
   - **Justification**: Required for coefficient interpretability
   - **Validation**: Calculate VIF; values < 5 acceptable
   - **Violation handling**: Remove or combine collinear predictors

6. **Missing at random**: Missing data mechanism is ignorable
   - **Justification**: Early years have less complete data
   - **Validation**: Compare patterns of missingness
   - **Violation handling**: Multiple imputation or selection model
```

**Quality Indicators**:
- ✅ 5-10 assumptions listed
- ✅ Each assumption has justification
- ✅ Validation method specified
- ✅ Violation handling plan included
- ❌ No assumptions listed
- ❌ Assumptions without justification
- ❌ No validation plan

#### 4. Solution Method (MANDATORY)

**Detailed algorithm or approach**

```markdown
## Solution Method

### Estimation Approach

We use **Restricted Maximum Likelihood (REML)** to estimate model parameters:

**Algorithm**:
1. Initialize $\boldsymbol{\beta}^{(0)}$ using OLS estimates
2. For iteration $t = 1, 2, \ldots$:
   a. Given current variance estimates $\boldsymbol{\theta}^{(t-1)}$, update $\boldsymbol{\beta}^{(t)}$:
      $$
      \boldsymbol{\beta}^{(t)} = (\mathbf{X}^\top \mathbf{V}^{-1} \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{V}^{-1} \mathbf{y}
      $$
      where $\mathbf{V}$ is the covariance matrix from random effects
   b. Update variance components $\boldsymbol{\theta}^{(t)}$ using EM algorithm
   c. Check convergence: $||\boldsymbol{\beta}^{(t)} - \boldsymbol{\beta}^{(t-1)}|| < \epsilon$
3. Return final estimates $\hat{\boldsymbol{\beta}}$, $\hat{\boldsymbol{\theta}}$

**Computational Details**:
- **Software**: Python `statsmodels` MixedLM
- **Convergence tolerance**: $\epsilon = 10^{-6}$
- **Max iterations**: 1000
- **Optimization method**: L-BFGS-B (bounded optimization)

**Inference**:
- Wald tests for fixed effects: $H_0: \beta_j = 0$
- Confidence intervals: $\hat{\beta}_j \pm 1.96 \times SE(\hat{\beta}_j)$
- Likelihood ratio tests for random effects
```

**Quality Indicators**:
- ✅ Specific algorithm named (not "use regression")
- ✅ Implementation details provided
- ✅ Software/tools specified
- ✅ Convergence criteria defined
- ❌ Vague ("fit the model using software")
- ❌ No computational details
- ❌ No inference method

#### 5. Complexity Analysis (MANDATORY)

**Time and space complexity**

```markdown
## Complexity Analysis

### Computational Complexity

**Time Complexity**:
- Let $n$ be number of observations, $p$ be number of fixed effects, $q$ be number of random effects
- Per-iteration cost: $O(np^2 + p^3 + nq^2 + q^3)$
  - $np^2$: Fixed effects design matrix operations
  - $p^3$: Inverting $(p \times p)$ matrix
  - $nq^2$: Random effects operations
  - $q^3$: Inverting $(q \times q)$ matrix
- Typical case: $n \approx 1000$, $p \approx 10$, $q \approx 5$
  - Per iteration: $\approx 10^5 - 10^6$ operations
  - Total (100 iterations): $\approx 10^7 - 10^8$ operations
  - Estimated time: 1-5 seconds on modern CPU

**Space Complexity**:
- Store design matrices: $O(np + nq)$
- Store covariance matrices: $O(p^2 + q^2)$
- Total: $O(np)$ dominates
- Typical case: $\approx 10^5$ entries, < 1 MB memory

**Scalability**:
- Linear in $n$ (observations)
- Cubic in $p$ and $q$ (number of effects)
- Practical limit: $p, q \leq 100$ on standard hardware
```

**Quality Indicators**:
- ✅ Big-O notation used correctly
- ✅ Concrete estimates for typical case
- ✅ Scalability limitations discussed
- ❌ No complexity analysis
- ❌ Vague ("computationally feasible")

#### 6. Validation Approach (MANDATORY)

**How to verify model correctness**

```markdown
## Validation Approach

### Model Validation

**1. Cross-Validation**:
- Method: 5-fold cross-validation
- Metric: RMSE, $R^2$, MAE
- Procedure:
  a. Randomly split data into 5 folds
  b. For each fold $i$:
     - Train on 4 folds
     - Predict on fold $i$
     - Compute prediction metrics
  c. Average metrics across folds
- Success criterion: CV $R^2$ > 0.7

**2. Residual Diagnostics**:
- Plot residuals vs fitted values (check homoscedasticity)
- Q-Q plot of residuals (check normality)
- Autocorrelation plot (check independence)
- Leverage vs squared residuals (check outliers)

**3. Sensitivity Analysis**:
- Vary key assumptions:
  - Different random effect structures
  - Different covariance matrices
  - With/without outlier removal
- Compare coefficient stability
- Success criterion: Coefficients change by < 20%

**4. Out-of-Sample Prediction**:
- Hold out most recent year (2024)
- Train on 1992-2020 data
- Predict 2024 medals
- Compare predictions to actual
- Success criterion: Prediction error < 15%

**5. Comparison to Baselines**:
- Compare to simple mean model
- Compare to linear regression (no random effects)
- Compare to naive forecast (previous year = current year)
- Success criterion: Our model outperforms all baselines
```

**Quality Indicators**:
- ✅ Multiple validation methods specified
- ✅ Success criteria defined
- ✅ Concrete procedures described
- ❌ No validation plan
- ❌ Vague ("validate the model")

---

## Forbidden Simplifications

### ❌ DO NOT Do This

**Overly Simple Model**:
```markdown
## Model Design

We'll use linear regression to predict medals.

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \epsilon$$

Where $Y$ is medals, $X$ are predictors.

Code will use sklearn's LinearRegression.
```

**Problems**:
- No variable definitions table
- No assumptions listed
- No solution method details
- No complexity analysis
- No validation approach
- Single paragraph, not substantial

**Token Usage**: < 5k tokens
**Time Invested**: < 10 minutes
**Verdict**: ❌ UNACCEPTABLE

---

### ✅ DO This Instead

**Complete Model Specification**:
```markdown
## Model Design #3: Hierarchical Bayesian Medal Count Model

### Problem Statement
[Two paragraphs explaining what problem this solves]

### Variables
[Complete table with 15+ variables]

### Mathematical Formulation
[Full LaTeX equations with extensions]

### Assumptions
[8 assumptions with justifications and validation plans]

### Solution Method
[Detailed REML algorithm with pseudocode]

### Complexity Analysis
[Big-O complexity with concrete estimates]

### Required Features
[Table of 10 features with sources]

### Expected Output
[Detailed description of predictions with uncertainty]

### Validation Approach
[5 validation methods with success criteria]
```

**Token Usage**: 15-25k tokens per model
**Time Invested**: 45-90 minutes per model
**Total for 3 models**: 50-80k tokens, 2-3 hours
**Verdict**: ✅ ACCEPTABLE

---

## Director Oversight Mechanisms

### Pre-Submission Checklist

Before accepting @modeler's submission, Director MUST verify:

**1. Token Usage Check**:
```python
if modeler_token_usage < 50000:
    # Suspiciously low
    query_modeler_for_completeness()
```

**2. File Size Check**:
```bash
# Check if model_design files are substantial
wc -l output/model/model_design_*.md

# Expected: 100-300 lines per model
# If < 50 lines: Query for completeness
```

**3. Component Presence Check**:
```
Read each model_design_{i}.md
Verify contains:
  - [ ] Mathematical formulation (LaTeX equations)
  - [ ] Variables table (symbol, description, type, range)
  - [ ] Assumptions list (with justifications)
  - [ ] Solution method (algorithm/approach)
  - [ ] Complexity analysis (time/space)
  - [ ] Validation approach (multiple methods)
```

**4. Quality Spot-Check**:
```
Randomly select one model_design_{i}.md
Check for:
  - [ ] Not just 1-2 paragraphs
  - [ ] Has actual LaTeX equations (not text description)
  - [ ] Variables are clearly defined
  - [ ] Assumptions have justifications (not just listed)
  - [ ] Solution method is specific (not "use sklearn")
```

---

## Query Protocol for Suspicious Submissions

When Director suspects oversimplification:

**Template Query**:
```
@modeler:

Your submission appears too simple for this MCM problem.

Concerns:
1. Token usage: {actual}k (expected: 80-120k)
2. File sizes: {file_sizes} (expected: 100-300 lines each)
3. Time worked: {actual_time} (expected: 2-6 hours)

Please verify you included ALL required components for EACH model:

**Mathematical Formulation**:
- [ ] Complete LaTeX equations (not text descriptions)
- [ ] All symbols defined
- [ ] Extensions/variations included

**Variables Table**:
- [ ] Symbol, description, type, range for ALL variables
- [ ] Data sources identified

**Assumptions**:
- [ ] 5-10 assumptions listed
- [ ] Each has justification
- [ ] Validation method specified
- [ ] Violation handling plan

**Solution Method**:
- [ ] Specific algorithm named (not "use regression")
- [ ] Implementation details provided
- [ ] Software/tools specified
- [ ] Convergence criteria defined

**Complexity Analysis**:
- [ ] Big-O notation used
- [ ] Concrete estimates for typical case

**Validation Approach**:
- [ ] Multiple validation methods
- [ ] Success criteria defined

**Anti-Simplification Rule**:
You may DEGRADE (Tier 2: reduce complexity slightly) but you may NOT:
- Skip required components
- Provide 1-paragraph model descriptions
- Use only simple methods when advanced methods are appropriate
- Omit mathematical formulation

If you cannot complete full models due to time constraints:
1. clearly state which TIER you're using (Tier 1/2/3)
2. Document limitations in detail
3. Explain why Tier 1 is not feasible

Please expand your submission to meet these requirements.
```

---

## Tier System Clarification

### When to Use Each Tier

**Tier 1: Full Model** (default)
- Use when: Normal circumstances, sufficient time
- Complexity: Full method with all components
- Time: 2-6 hours per model
- Tokens: 20-40k per model

**Tier 2: Lightweight Model** (degrade)
- Use when: Time pressure, but still want quality
- Complexity: Core method, reduced extensions
- Time: 1-2 hours per model
- Tokens: 10-15k per model
- **Requirement**: Must still have ALL 6 components, just less detail

**Tier 3: Minimal Model** (last resort)
- Use when: Extreme time pressure, < 1 hour left
- Complexity: Basic method with essential components only
- Time: 20-30 minutes per model
- Tokens: 5-8k per model
- **Requirement**: Must have ALL 6 components, minimal detail

**Tier 3 Example** (acceptable but minimal):
```markdown
## Model Design #1: Basic Poisson Regression

### Variables
[Table with 5 core variables only]

### Mathematical Formulation
$$Y_i \sim \text{Poisson}(\lambda_i)$$
$$\log(\lambda_i) = \beta_0 + \sum_{j=1}^{p} \beta_j X_{ij}$$

### Assumptions
1. Poisson distribution
2. Log link function
3. Independence

### Solution Method
Use `statsmodels.GLM` with family=Poisson
Default convergence settings

### Complexity Analysis
Time: O(np), Space: O(n)
Estimated: < 1 second

### Validation
Check deviance residuals
Compare to null model

**Limitations**:
- Does not account for overdispersion
- No random effects
- No temporal correlation
- Should extend to negative binomial if time permits
```

**This is Tier 3**: Minimal but still has all 6 components.

---

## Quality Indicators Summary

| Indicator | Minimal (Tier 3) | Expected (Tier 1) | Excellent |
|-----------|------------------|-------------------|-----------|
| **Tokens per model** | 5-8k | 20-40k | 40k+ |
| **Lines per model** | 50-80 | 100-200 | 200+ |
| **Equations** | 1-2 core | 3-5 with extensions | 5+ with derivations |
| **Variables** | 5-10 | 10-20 | 20+ |
| **Assumptions** | 3-5 | 5-10 | 10+ |
| **Validation methods** | 1-2 | 3-5 | 5+ |

**Director Decision Guide**:
- Below minimal row: **REJECT** (too simple)
- Minimal to Expected: **ACCEPT** if time pressure documented
- Expected to Excellent: **APPROVE**

---

## Testing Checklist

Before implementing, verify:

- [ ] Token usage thresholds defined
- [ ] Required components checklist created
- [ ] Director query template written
- [ ] Tier system clarified with examples
- [ ] Anti-patterns documented
- [ ] Quality indicators matrix defined

---

**Document Version**: v2.5.4
**Created**: 2026-01-16
**Status**: MANDATORY for Phase 1 (Model Design)
