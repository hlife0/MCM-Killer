# Narrative Template: Onion Peeling

> **Best For**: Multi-faceted problems with distinct analytical layers
> **Logic Flow**: Surface → Depth → Core
> **O-Prize Value**: High (shows progressive understanding)

---

## When to Use

Use the Onion Peeling template when:
- The problem has multiple interacting factors
- Analysis progressively deepens understanding
- Each layer reveals new mechanisms
- Simple explanations are insufficient

---

## The Four Layers

### Layer 0: The Surface (First-Order Effects)

**Purpose**: Start with the obvious, establish baseline understanding

**Template**:
```markdown
## Surface Analysis: First-Order Effects

At the surface level, [Dependent Variable] correlates with [Primary Factor].

**Observation**:
- [Metric]: [Value] (correlation: r = [X])
- [Pattern description]

**Initial Model**:
Y = β₀ + β₁X₁ + ε

**Result**:
- R² = [Value]
- RMSE = [Value]

**Interpretation**:
This suggests that [Primary Factor] explains [X]% of variation, but
leaves [Y]% unexplained. What drives the residual?
```

**Example**:
```markdown
## Surface Analysis: First-Order Effects

At the surface level, epidemic spread correlates with population density.

**Observation**:
- Correlation: r = 0.67 (p < 0.001)
- Denser regions show faster initial spread

**Initial Model**:
log(Cases) = β₀ + β₁(Density) + ε

**Result**:
- R² = 0.45
- RMSE = 12.3

**Interpretation**:
Population density explains 45% of variation in spread, but leaves 55%
unexplained. What drives the residual variation?
```

---

### Layer 1: The First Depth (Second-Order Effects)

**Purpose**: Reveal interactions and moderating factors

**Template**:
```markdown
## Deeper Analysis: Second-Order Effects

Deeper analysis reveals that [Secondary Factor] modulates the primary effect.

**Observation**:
- When [Condition A]: [Effect 1]
- When [Condition B]: [Effect 2]
- Interaction term: [Significance]

**Enhanced Model**:
Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁ × X₂) + ε

**Result**:
- R² = [Improved Value] (↑[X]% from Layer 0)
- RMSE = [Improved Value]
- Interaction p-value = [Value]

**Interpretation**:
The [Primary Factor] effect is conditional on [Secondary Factor].
This explains why [Initial Puzzle from Layer 0].
```

**Example**:
```markdown
## Deeper Analysis: Second-Order Effects

Deeper analysis reveals that network topology modulates the density effect.

**Observation**:
- High density + hub city: 3.2x faster spread
- High density + peripheral city: 1.4x faster spread
- Interaction term: β₃ = 0.87 (p < 0.001)

**Enhanced Model**:
log(Cases) = β₀ + β₁(Density) + β₂(Centrality) + β₃(Density × Centrality) + ε

**Result**:
- R² = 0.72 (↑27% from Layer 0)
- RMSE = 7.8
- Interaction p-value < 0.001

**Interpretation**:
Density alone doesn't drive spread—it's density at network hubs that
matters. This explains why some dense cities (peripheral) showed slow
spread while less dense hub cities showed rapid spread.
```

---

### Layer 2: The Second Depth (Third-Order Effects)

**Purpose**: Reveal emergent properties and non-linear dynamics

**Template**:
```markdown
## Emergent Analysis: Third-Order Effects

Most surprisingly, [Emergent Property] creates [Unexpected Effect].

**Observation**:
- [Non-linear pattern]
- [Threshold behavior]
- [Cascading effect]

**Complex Model**:
[More sophisticated formulation - could be ODE, agent-based, or non-linear]

**Result**:
- [Performance improvement]
- [New insight metric]

**Emergence Mechanism**:
This [Emergent Property] arises because:
1. [Micro-mechanism 1] → [Aggregate effect 1]
2. [Micro-mechanism 2] → [Aggregate effect 2]
3. These combine to produce [Emergent behavior]

**Interpretation**:
Simple factor analysis misses this emergence. Only by modeling
[Full System Dynamics] can we capture [Key Insight].
```

**Example**:
```markdown
## Emergent Analysis: Third-Order Effects

Most surprisingly, hub-seeding creates cascading effects that
dominate both density and topology in later stages.

**Observation**:
- Early outbreak at hub: 5.2x total cases vs. peripheral start
- Cascade timing: hub spreads to 3+ secondary hubs within 2 weeks
- Threshold behavior: hub infection >10% triggers exponential cascade

**Complex Model**:
SIR-Network with adjacency matrix A:
dI_i/dt = β S_i Σⱼ Aᵢⱼ Iⱼ - γ Iᵢ

**Result**:
- R² = 0.89 (↑17% from Layer 1)
- RMSE = 4.2
- Captures cascade timing within 3 days accuracy

**Emergence Mechanism**:
The cascade emerges because:
1. Hubs have high out-degree → seed multiple regions simultaneously
2. Secondary hubs amplify → exponential rather than linear growth
3. Peripheral regions become trapped by surrounding infected hubs

**Interpretation**:
Aggregate density/centrality metrics miss cascade dynamics. Only
network simulation with explicit topology captures the emergent
super-linear spread from hub-seeding.
```

---

### Layer 3: The Core (Fundamental Insight)

**Purpose**: Extract the deepest understanding

**Template**:
```markdown
## Core Insight: Fundamental Understanding

These layers combine to reveal that [Core Insight].

**Synthesis**:
| Layer | Factor | Contribution | Mechanism |
|-------|--------|--------------|-----------|
| 0 | [Primary] | [X]% | [Mechanism] |
| 1 | [Interaction] | [Y]% | [Mechanism] |
| 2 | [Emergence] | [Z]% | [Mechanism] |

**The Core Truth**:
> "[One-sentence fundamental insight]"

**Why This Matters**:
Traditional approaches that only consider Layer 0 miss [X]% of the
phenomenon. The [Interaction/Emergence] effects are not secondary—
they are essential for [Accurate Prediction / Policy Design / Understanding].

**Implications**:
1. **Methodological**: [What modeling approach is required?]
2. **Policy**: [What intervention strategy follows?]
3. **Theoretical**: [What does this add to domain knowledge?]
```

**Example**:
```markdown
## Core Insight: Fundamental Understanding

These layers combine to reveal that epidemic control requires targeting
network structure, not just reducing contacts.

**Synthesis**:
| Layer | Factor | Contribution | Mechanism |
|-------|--------|--------------|-----------|
| 0 | Density | 45% | More contacts per unit area |
| 1 | Topology | 27% | Hub amplification |
| 2 | Cascade | 17% | Emergent super-linear spread |
| - | Residual | 11% | Unmodeled factors |

**The Core Truth**:
> "Epidemic spread is fundamentally a network phenomenon—aggregate
> measures like density are proxies for the underlying topology that
> actually drives transmission dynamics."

**Why This Matters**:
Traditional approaches that only consider population density miss 44%
of the phenomenon (Layers 1+2). The topology and cascade effects are
not secondary—they are essential for accurate prediction and effective
intervention design.

**Implications**:
1. **Methodological**: Network-aware models are necessary, not optional
2. **Policy**: Target hub nodes (airports, transit centers) for maximum impact
3. **Theoretical**: Epidemic modeling must incorporate explicit spatial structure
```

---

## Complete Template

```markdown
# Onion Peeling Analysis: [Problem Name]

## Layer 0: Surface
[Primary factor] explains [X]% of variation.
R² = [Value], RMSE = [Value]
But [Y]% remains unexplained...

## Layer 1: First Depth
[Secondary factor] modulates the primary effect.
R² improves to [Value] (↑[Z]%)
The interaction reveals [Mechanism].

## Layer 2: Second Depth
[Emergent property] dominates in [Condition].
R² reaches [Value]
Emergence arises from [Micro-mechanisms].

## Layer 3: Core
**The Core Truth**: "[Fundamental insight]"

**Synthesis**: [Table of layer contributions]

**Implications**:
- Methodological: [Required approach]
- Policy: [Actionable recommendation]
- Theoretical: [Contribution to knowledge]
```

---

## Visual Representation

```
┌─────────────────────────────────────┐
│        SURFACE (Layer 0)            │
│   Primary factors, obvious effects  │
│          R² = 0.45                  │
│   ┌─────────────────────────────┐   │
│   │      DEPTH 1 (Layer 1)      │   │
│   │   Interactions, moderators  │   │
│   │        R² = 0.72            │   │
│   │   ┌─────────────────────┐   │   │
│   │   │   DEPTH 2 (Layer 2) │   │   │
│   │   │   Emergent effects  │   │   │
│   │   │      R² = 0.89      │   │   │
│   │   │   ┌─────────────┐   │   │   │
│   │   │   │    CORE     │   │   │   │
│   │   │   │  (Layer 3)  │   │   │   │
│   │   │   │ Fundamental │   │   │   │
│   │   │   │   Insight   │   │   │   │
│   │   │   └─────────────┘   │   │   │
│   │   └─────────────────────┘   │   │
│   └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
