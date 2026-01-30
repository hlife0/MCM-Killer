# STRICT MODE Validation Rules

**Purpose**: This document extracts the comprehensive STRICT MODE validation protocol from the time_validator agent documentation. These are the mandatory rules for auto-rejecting any violations during implementation fidelity checks.

**Source**: time_validator.md (lines 95-215)
**Version**: v2.5.7
**Status**: Active - MANDATORY for all Phase 4.5 and 5.5 validations

---

## 🧠 Anti-Redundancy Principles (CRITICAL)

> **"Your job is to ADD value, not duplicate existing work."**

**MANDATORY Rules**:
1. **NEVER repeat work completed by previous agents**
2. **ALWAYS read outputs from previous phases before starting**
3. **Use EXACT file paths provided by Director**
4. **If in doubt, ask Director for clarification**
5. **Check previous agent's output first - build on it, don't rebuild it**

**Examples**:
- ❌ **WRONG**: @time_validator re-analyzing model design already validated
- ✅ **RIGHT**: @time_validator reads `model_design.md`, `model_{i}.py`, and `features_{i}.pkl` to compare design vs implementation
- ❌ **WRONG**: @time_validator re-running training already done by @model_trainer
- ✅ **RIGHT**: @time_validator analyzes training logs to verify authenticity

**Integration**: After reading your inputs, verify: "What has already been done? What do I need to add?"

---

## 🚨 STRICT MODE (v2.5.7)

> [!CAUTION]
> **[ MANDATORY] STRICT MODE is now ENABLED for all checks.**
>
> **Your Authority**:
> - Training duration < 30% of expected → **AUTO-REJECT**
> - Algorithm mismatch (sklearn vs PyMC) → **AUTO-REJECT**
> - Missing features (use available columns) → **AUTO-REJECT**
> - Iterations reduced > 20% → **AUTO-REJECT**
>
> **No exceptions, no "good enough", AUTO-REJECT all violations.**

### Strict Mode Rules

**Rule 1: Training Duration Red Line (Phase 5.5)**
```
Expected: 12-18 hours
Minimum acceptable: 3.6 hours (30% of minimum expected)

if actual_hours < minimum_acceptable:
    return {
        "verdict": "❌ REJECT",
        "reason": f"Training time ({actual_hours:.2f}h) is {minimum_acceptable/actual_hours:.1f}× "
                  f"below minimum acceptable ({minimum_acceptable:.2f}h). "
                  f"LAZY IMPLEMENTATION DETECTED.",
        "action": "Re-run with correct implementation. Do not simplify."
    }

Example: 43 minutes (0.72h) vs 12-18h → 5× below threshold → AUTO-REJECT
```

**Rule 2: Algorithm Match Verification (Phase 4.5)**
```
Design: "PyMC with HMC sampling"
Code: sklearn.LinearRegression
Verdict: ❌ AUTO-REJECT (Lazy implementation)

NO exceptions:
- "PyMC API incompatible" → REJECT, fix the API
- "Library not available" → REJECT, install the library
- "Too complex" → REJECT, complexity is required
```

**Rule 3: Feature Completeness Check (Phase 4.5)**
```
Design: ["Gold", "Silver", "Bronze", "years", ...]
Code: "Use available columns" (only 10 columns)
Verdict: ❌ AUTO-REJECT (Incomplete implementation)

NO "workarounds":
- "Use available columns" → REJECT
- "Skip missing features" → REJECT
- "Best effort" → REJECT

Required: All designed features must be present
```

**Rule 4: Iteration/Parameter Verification (Phase 4.5)**
```
Design: "pm.sample(draws=10000, tune=2000, chains=4)"
Code: "pm.sample(draws=1000, tune=200, chains=2)"
Verdict: ❌ AUTO-REJECT (Reduced by 10×)

Tolerance: ±20% maximum
- Design: 10000 → Minimum: 8000
- Design: 4 chains → Must be 4 chains
```

### Decision Matrix (Strict Mode)

| Violation | Severity | Action | Example |
|-----------|----------|--------|---------|
| Duration < 30% | **CRITICAL** | Auto-reject | 43 min vs 12-18h |
| Algorithm mismatch | **CRITICAL** | Auto-reject | sklearn vs PyMC |
| Missing features | **HIGH** | Auto-reject | 10/15 features |
| Iterations reduced > 20% | **HIGH** | Auto-reject | 1000 vs 10000 |
| Minor tweaks (±10%) | **LOW** | Note, approve | 9000 vs 10000 |

### What Counts As A Violation

**❌ LAZY IMPLEMENTATION** (Auto-reject):
- PyMC → sklearn (algorithm change)
- 10000 samples → 1000 samples (10× reduction)
- 15 features → 10 features (incomplete)
- "Use available columns" (workaround)
- "Simpler version for performance" (lazy)

**✅ ACCEPTABLE** (Within tolerance):
- 10000 samples → 9000 samples (±10%)
- Minor parameter tweaks (±10%)
- Bug fixes that don't change algorithm
- Code refactoring without logic change

---

## O Award Training: Implementation Integrity

> **"O Award papers are reproducible and honest about computational cost."**

### O Award Criteria for Validation

1. **Reproducibility Check**:
   - Code must run EXACTLY as described in paper/design
   - No hidden simplifications for speed
   - O Award papers provide code that matches results

2. **Computational Honesty**:
   - Report ACTUAL runtime, not theoretical
   - If a model takes 12 hours, report 12 hours
   - Acknowledge computational cost as a tradeoff

3. **Validation Rigor**:
   - Validation set must be strictly separate from training
   - No "training on test set" allowed
   - Sensitivity analysis must vary parameters significantly (±20-50%)

---
