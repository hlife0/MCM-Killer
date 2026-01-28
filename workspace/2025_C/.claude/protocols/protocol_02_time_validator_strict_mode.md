# Protocol 2: @time_validator Strict Mode

> **Purpose**: Ensure @time_validator rejects ALL lazy implementations, especially training duration shortcuts
> **Owner**: @time_validator
> **Scope**: Phases 4.5 (Implementation Fidelity), 5.5 (Data Authenticity)

## Problem Statement

Lazy implementations result in academic fraud:

```
Expected training: 12-18 hours
Actual training: 43 minutes
@time_validator: "Looks good"
Result: Academic fraud through simplification
```

## Rules

### Rule 1: Training Duration Red Line

**Thresholds**:
- Expected: 12-18 hours
- Minimum acceptable: 3.6 hours (30% of minimum expected)

**AUTO-REJECT if actual < 3.6 hours**:
- 43 minutes = 0.72 hours → 23× below threshold → AUTO-REJECT
- 2 hours = 120 minutes → Below threshold → REJECT

### Rule 2: Algorithm Match Verification

```
Design specifies: PyMC with HMC sampling
Code uses: sklearn.LinearRegression
Verdict: LAZY IMPLEMENTATION → REJECT
```

### Rule 3: Feature Completeness Check

```
Design: 15 features including X, Y, Z
Code: "Use available columns" (only 10 columns)
Verdict: INCOMPLETE → REJECT
```

### Rule 4: Iteration/Parameter Verification

```
Design: 10,000 MCMC samples
Code: pm.sample(1000)
Verdict: REDUCED BY 10× → LAZY → REJECT
```

## Decision Matrix

| Check | Pass Threshold | Fail Action |
|-------|---------------|-------------|
| Training duration | >= 30% of expected | Auto-reject |
| Algorithm match | Exact match | Reject |
| Features | All present | Reject |
| Iterations | >= 80% of specified | Reject |

## Consequences of Lazy Implementation

1. **First offense**: @code_translator must rework completely
2. **Second offense**: @director issues formal warning
3. **Third offense**: Consider agent replacement (reinitialize agent)

## Enforcement Mechanisms

### Phase 4.5: Implementation Fidelity Check

**@time_validator checks**:
1. Algorithm match: PyMC must be PyMC, not sklearn
2. Feature completeness: All designed features present
3. Iteration verification: Within ±20% tolerance
4. NO unauthorized simplifications

**Example validation**:
```
Design: PyMC hierarchical, 5000×50, 10000×4 chains
Code: PyMC, 5000×50, 10000×4 chains
Verdict: VALID → APPROVE

Design: PyMC hierarchical, 10000 samples
Code: sklearn.LinearRegression
Verdict: ALGORITHM MISMATCH → REJECT
```

### Phase 5.5: Data Authenticity Check

**@time_validator checks**:
1. Training Duration Red Line: actual >= 30% of expected
2. Training Skip Detection: iterations executed? convergence achieved?
3. Algorithm Match: Code uses designed algorithm
4. Feature Completeness: All designed features used

**Example validation**:
```
Expected: 12-18 hours training
Actual: 43 minutes (0.72 hours)
Verdict: 5× below threshold → AUTO-REJECT
```

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
