# Protocol 8: Model Design Expectations Framework

> **Purpose**: Systematic validation of model designs against implementation with tolerance specifications
> **Owner**: @modeler (creation) + @time_validator (validation)
> **Scope**: Phase 1 (Model Design), Phase 4.5 (Implementation Fidelity)

## Problem Statement

Design-to-implementation gaps cause lazy implementation:

```
Design: "Use PyMC with 10,000 samples"
Code: sklearn.LinearRegression (no samples)
Result: Academic fraud through simplification
```

## Design Expectations Table

### Step 1: Mandatory Design Expectations Table (by @modeler)

**Every model_design_{i}.md MUST include**:

```markdown
## Design Expectations Table

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |
| Tune | 2000 | 2000 | 2000 | iterations | YES |
| Features | 15 | 15 | 15 | features | YES |
| Algorithm | PyMC | PyMC | PyMC | - | YES |
| Target Accept | 0.8 | 0.75 | 0.85 | probability | NO |
| Tree Depth | 10 | 8 | 12 | levels | NO |
```

### Table Column Definitions

- **Parameter**: What is being specified
- **Design Specification**: The exact value/choice
- **Min**: Minimum acceptable value (for tolerances)
- **Max**: Maximum acceptable value (for tolerances)
- **Unit**: What unit/choice
- **Must Not Simplify**: Can this be changed without @director approval?

## Scoring System

### Critical Parameters (Auto-Reject If Fail)

**CRITICAL parameters**: Fail = AUTO-REJECT
- Sampler (NUTS vs Metropolis)
- Algorithm (PyMC vs sklearn)
- Core features (Gold, Silver, Bronze, etc.)

**Rationale**: Changing these fundamentally changes the model

### High Parameters (±20% Tolerance)

**HIGH parameters**: ±20% tolerance allowed
- Draws (10,000 samples → 8,000-12,000 acceptable)
- Tune (2,000 iterations → 1,600-2,400 acceptable)
- Tree depth (10 → 8-12 acceptable)

**Rationale**: Minor tuning acceptable, major changes not

### Overall Score

**Calculation**:
```
Score = (Critical Parameters Passed / Total Critical) × 100%
      + (High Parameters Within Tolerance / Total High) × 100%
      Overall Score = Average of both × 100%

Must be >= 80% to PASS
```

### The "One Fail = All Fail" Rule

```
IF any Critical parameter fails:
    Overall score = 0% (AUTO-REJECT)

Rationale: Fundamental model change = not same model
```

## Validation Process

### Phase 1: @modeler Creates Table

**@modeler includes**:
- All critical parameters (sampler, algorithm, features)
- All high parameters (draws, tune, iterations)
- Clear min/max specifications
- "Must Not Simplify" column

**Example**:
```markdown
## Design Expectations Table

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Algorithm | PyMC (NUTS) | PyMC | PyMC | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 10000 | 10000 | 10000 | samples | YES |
| Tune | 2000 | 2000 | 2000 | iterations | YES |
| Features | 15 | 15 | 15 | features | YES |
```

### Phase 4.5: @time_validator Validates

**@time_validator compares**:
1. **Design specification** (from table)
2. **Actual implementation** (from model_{i}.py)
3. **Tolerance** (min/max from table)
4. **Verdict** (PASS/FAIL for each parameter)

**Validation output**:
```markdown
## Implementation Fidelity Check

Model: Model 1 (Hierarchical Bayesian)

| Parameter | Design | Actual | Tolerance | Verdict |
|-----------|---------|--------|-----------|---------|
| Algorithm | PyMC (NUTS) | PyMC (NUTS) | Exact | ✅ PASS |
| Chains | 4 | 4 | Exact | ✅ PASS |
| Draws | 10000 | 10000 | Exact | ✅ PASS |
| Tune | 2000 | 2000 | Exact | ✅ PASS |
| Features | 15 | 15 | Exact | ✅ PASS |

**Overall Score**: 100% (5/5 Critical + 0/0 High)
**Verdict**: APPROVED
```

**Example with violation**:
```markdown
## Implementation Fidelity Check

Model: Model 1 (Hierarchical Bayesian)

| Parameter | Design | Actual | Tolerance | Verdict |
|-----------|---------|--------|-----------|---------|
| Algorithm | PyMC (NUTS) | sklearn.LinearRegression | Exact | ❌ FAIL |
| Chains | 4 | N/A | Exact | ❌ FAIL |
| Draws | 10000 | N/A | Exact | ❌ FAIL |
| Tune | 2000 | N/A | Exact | ❌ FAIL |
| Features | 15 | 5 | Exact | ❌ FAIL |

**Overall Score**: 0% (Critical violation: Algorithm mismatch)
**Verdict**: REJECTED (Lazy implementation detected)
```

## Tolerance Guidelines

### Zero Tolerance (Must Not Simplify = YES)

**Algorithm**:
- PyMC must be PyMC (not sklearn)
- NUTS must be NUTS (not Metropolis)

**Features**:
- All designed features must be present
- No "use available columns"

**Core parameters**:
- Chains, draws, tune as specified

### ±20% Tolerance (Must Not Simplify = NO)

**Tuning parameters**:
- target_accept: 0.8 → 0.64-0.96 acceptable
- tree depth: 10 → 8-12 acceptable
- max treedepth: 15 → 12-18 acceptable

**Rationale**: These are tuning knobs, not fundamental design

## Enforcement

**Phase 4.5 validation**:
- @time_validator checks every parameter
- Compares actual vs design vs tolerance
- AUTO-REJECT if any Critical parameter fails
- Flag if any High parameter outside tolerance

**Consequences**:
- **Critical fail**: Full rework required (can't just "fix parameter")
- **High fail**: @director decides (adjust design or adjust code)

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
