# Narrative Template: Comparative Evolution

> **Best For**: Comparing multiple model iterations with progressive refinement
> **Dramatic Arc**: Baseline → Enhancement → Final
> **O-Prize Value**: Medium-High (shows systematic improvement)

---

## When to Use

Use the Comparative Evolution template when:
- Multiple models were built and compared
- Each iteration improved on the previous
- You want to show the value of specific refinements
- The comparison itself is informative

---

## The Three-Model Structure

### Model A: The Baseline

**Purpose**: Establish a simple, understandable starting point

**Template**:
```markdown
## Model A: Baseline [Method Name]

### Specification
[Simple mathematical formulation]

### Assumptions
1. [Assumption 1 - simplifying]
2. [Assumption 2 - simplifying]
3. [Assumption 3 - simplifying]

### Implementation
- Algorithm: [Name]
- Parameters: [Count]
- Training time: [Duration]

### Results
| Metric | Value |
|--------|-------|
| RMSE | [Value] |
| R² | [Value] |
| MAE | [Value] |

### Limitations
This baseline model:
- ❌ [Limitation 1]
- ❌ [Limitation 2]
- ❌ [Limitation 3]

**Verdict**: Establishes baseline but insufficient for [Reason].
```

**Example**:
```markdown
## Model A: Baseline SIR

### Specification
dS/dt = -βSI/N
dI/dt = βSI/N - γI
dR/dt = γI

### Assumptions
1. Homogeneous mixing (all contacts equally likely)
2. Constant parameters (β, γ time-invariant)
3. Closed population (no births, deaths, migration)

### Implementation
- Algorithm: Runge-Kutta 4th order
- Parameters: 2 (β, γ)
- Training time: 5 minutes

### Results
| Metric | Value |
|--------|-------|
| RMSE | 7.2 |
| R² | 0.71 |
| MAE | 5.8 |

### Limitations
This baseline model:
- ❌ Ignores spatial structure (network topology)
- ❌ Cannot capture regional heterogeneity
- ❌ Misses hub-driven cascade dynamics

**Verdict**: Establishes baseline but insufficient for accurate
multi-region prediction.
```

---

### Model B: The Enhancement

**Purpose**: Show targeted improvement addressing specific limitation

**Template**:
```markdown
## Model B: Enhanced [Method Name]

### Motivation
Model A failed because [Specific Limitation]. To address this, we
incorporate [Enhancement].

### Specification
[Enhanced mathematical formulation]

### Key Change
| Aspect | Model A | Model B | Rationale |
|--------|---------|---------|-----------|
| [Aspect 1] | [Old] | [New] | [Why] |
| [Aspect 2] | [Old] | [New] | [Why] |

### Implementation
- Algorithm: [Name]
- Parameters: [Count]
- Training time: [Duration]
- Added complexity: [Brief description]

### Results
| Metric | Model A | Model B | Change |
|--------|---------|---------|--------|
| RMSE | [A] | [B] | ↓[X]% |
| R² | [A] | [B] | ↑[Y]% |
| MAE | [A] | [B] | ↓[Z]% |

### Improvement Analysis
The [Enhancement] addresses [Limitation] by:
1. [Mechanism 1]
2. [Mechanism 2]

**Remaining Limitations**:
- ❌ [Limitation still present]

**Verdict**: Significant improvement, but [Remaining Issue] suggests
further refinement needed.
```

**Example**:
```markdown
## Model B: SIR-Network

### Motivation
Model A failed because it ignored spatial structure. To address this,
we incorporate network topology via an adjacency matrix.

### Specification
dSᵢ/dt = -β Sᵢ Σⱼ Aᵢⱼ (Iⱼ/Nⱼ)
dIᵢ/dt = β Sᵢ Σⱼ Aᵢⱼ (Iⱼ/Nⱼ) - γ Iᵢ
dRᵢ/dt = γ Iᵢ

### Key Change
| Aspect | Model A | Model B | Rationale |
|--------|---------|---------|-----------|
| Mixing | Homogeneous | Network-structured | Capture spatial topology |
| β | Scalar | Scalar (shared) | Maintain parsimony |
| Regions | Aggregated | 8 explicit nodes | Enable regional analysis |

### Implementation
- Algorithm: Network ODE solver
- Parameters: 2 + adjacency matrix (8×8)
- Training time: 15 minutes
- Added complexity: Requires airline/contact network data

### Results
| Metric | Model A | Model B | Change |
|--------|---------|---------|--------|
| RMSE | 7.2 | 5.1 | ↓29% |
| R² | 0.71 | 0.82 | ↑15% |
| MAE | 5.8 | 4.2 | ↓28% |

### Improvement Analysis
The network structure addresses homogeneous mixing by:
1. Capturing hub amplification (central nodes spread faster)
2. Modeling geographic spread patterns (neighbors infected first)

**Remaining Limitations**:
- ❌ Single β assumes all regions have identical transmission rates

**Verdict**: Significant improvement (29% RMSE reduction), but regional
heterogeneity in β suggests further refinement needed.
```

---

### Model C: The Final Solution

**Purpose**: Present the fully refined solution

**Template**:
```markdown
## Model C: Final [Method Name]

### Motivation
Model B improved over A, but [Remaining Limitation] persisted. Our
final model incorporates [Final Enhancement].

### Specification
[Complete mathematical formulation]

### Complete Evolution
| Aspect | Model A | Model B | Model C |
|--------|---------|---------|---------|
| [Aspect 1] | [A] | [B] | [C] |
| [Aspect 2] | [A] | [B] | [C] |
| [Aspect 3] | [A] | [B] | [C] |

### Implementation
- Algorithm: [Name]
- Parameters: [Count]
- Training time: [Duration]
- Complexity: [Description]

### Results
| Metric | Model A | Model B | Model C | Total Improvement |
|--------|---------|---------|---------|-------------------|
| RMSE | [A] | [B] | [C] | ↓[X]% from baseline |
| R² | [A] | [B] | [C] | ↑[Y]% from baseline |
| MAE | [A] | [B] | [C] | ↓[Z]% from baseline |

### Why Model C Wins
1. **[Advantage 1]**: [Explanation with metric]
2. **[Advantage 2]**: [Explanation with metric]
3. **[Advantage 3]**: [Explanation with metric]

### Remaining Limitations (Acknowledged)
- [Limitation 1] - addressed in Discussion
- [Limitation 2] - future work

**Verdict**: Final model achieves [Key Accomplishment] with
[Performance Metric].
```

**Example**:
```markdown
## Model C: Hierarchical SIR-Network

### Motivation
Model B improved over A, but assumed identical β across regions.
Our final model incorporates hierarchical priors for region-specific
transmission rates.

### Specification
βᵢ ~ Normal(μ_cluster, σ_cluster)
μ_cluster ~ Normal(μ_global, σ_global)

dSᵢ/dt = -βᵢ Sᵢ Σⱼ Aᵢⱼ (Iⱼ/Nⱼ)
dIᵢ/dt = βᵢ Sᵢ Σⱼ Aᵢⱼ (Iⱼ/Nⱼ) - γᵢ Iᵢ
dRᵢ/dt = γᵢ Iᵢ

### Complete Evolution
| Aspect | Model A | Model B | Model C |
|--------|---------|---------|---------|
| Structure | Aggregate | Network | Hierarchical Network |
| β | Scalar | Scalar | Region-specific |
| Pooling | N/A | Full | Partial (by cluster) |
| Uncertainty | Point est. | Point est. | Bayesian posteriors |

### Implementation
- Algorithm: Bayesian ODE with NUTS sampler
- Parameters: 2 + 16 (regional) + 4 (hyperparameters)
- Training time: 2.3 hours
- Complexity: Requires hierarchical prior specification

### Results
| Metric | Model A | Model B | Model C | Total Improvement |
|--------|---------|---------|---------|-------------------|
| RMSE | 7.2 | 5.1 | 4.2 | ↓42% from baseline |
| R² | 0.71 | 0.82 | 0.89 | ↑25% from baseline |
| MAE | 5.8 | 4.2 | 3.4 | ↓41% from baseline |

### Why Model C Wins
1. **Heterogeneity**: Captures region-specific β (range: 0.3-0.7)
2. **Uncertainty**: 95% credible intervals enable risk assessment
3. **Robustness**: Partial pooling prevents overfitting while allowing variation

### Remaining Limitations (Acknowledged)
- Time-invariant parameters - addressed in Discussion Section 5.1
- Requires substantial data per region - future work

**Verdict**: Final model achieves 42% RMSE reduction while providing
principled uncertainty quantification.
```

---

## Summary Comparison Table

**Template**:
```markdown
## Model Comparison Summary

| Criterion | Model A | Model B | Model C |
|-----------|---------|---------|---------|
| **Complexity** | Low | Medium | High |
| **Assumptions** | Strong | Moderate | Weak |
| **Parameters** | [N] | [N] | [N] |
| **Training Time** | [T] | [T] | [T] |
| **RMSE** | [V] | [V] | [V] |
| **R²** | [V] | [V] | [V] |
| **Uncertainty** | No | No | Yes |
| **Interpretability** | High | Medium | Medium |

**Recommendation**:
- **If time < 6 hours**: Use Model B (good balance)
- **If time ≥ 12 hours**: Use Model C (best performance)
- **For explanation**: Show evolution A → B → C
```

---

## Visual Evolution Diagram

```
Model A ──────────────────────→ Model B ──────────────────────→ Model C
(Baseline)                      (Enhanced)                       (Final)

┌─────────────┐   +Network    ┌─────────────┐   +Hierarchy    ┌─────────────┐
│ Simple SIR  │──────────────→│ SIR-Network │───────────────→│ Hierarchical│
│ RMSE: 7.2   │               │ RMSE: 5.1   │                │ RMSE: 4.2   │
│ R²: 0.71    │               │ R²: 0.82    │                │ R²: 0.89    │
└─────────────┘               └─────────────┘                └─────────────┘
      ↓                             ↓                              ↓
  Limitation:                  Limitation:                    Final Model:
  No topology                  Homogeneous β                  Captures all
                                                              key effects
```

---

## Complete Template

```markdown
# Model Comparison: [Problem Name]

## Model A: Baseline
[Simple approach]
- RMSE: [Value]
- Limitation: [Key issue]

## Model B: Enhanced
[Targeted improvement]
- RMSE: [Value] (↓X%)
- Addresses: [Previous limitation]
- Remaining: [New limitation discovered]

## Model C: Final
[Complete solution]
- RMSE: [Value] (↓Y% from baseline)
- Captures: [All key effects]

## Comparison Summary
[Table of all metrics across models]

## Evolution Insight
> "The progression from A → B → C demonstrates that
> [Key methodological lesson]."
```

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
