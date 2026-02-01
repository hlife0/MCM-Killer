# Model 6: Mechanism Design Framework

> **Purpose**: This file contains detailed specifications for the flagship Model 6 (Mechanism Design) that addresses the final question/policy recommendation.

## Overview

Model 6 is the FLAGSHIP model and must demonstrate the highest sophistication level. It uses mechanism design theory to optimize voting/scoring systems.

---

## Social Planner's Problem Formulation

### LaTeX Template

```latex
\max_{\theta} W(\theta) = \omega_F \cdot E[U_{fan}] + \omega_J \cdot E[U_{judge}] + \omega_P \cdot E[U_{prod}]

\text{subject to:}
\begin{align}
\text{(IC)}: & \text{ Incentive Compatibility} \\
\text{(IR)}: & \text{ Individual Rationality} \\
\text{(BB)}: & \text{ Budget Balance}
\end{align}
```

### Stakeholder Utility Functions

| Stakeholder | Utility Function | Description |
|-------------|------------------|-------------|
| Fan | $U_{fan}(x) = \alpha_{fan} \cdot \text{[fan engagement metrics]}$ | Measures viewer satisfaction and engagement |
| Judge | $U_{judge}(x) = \alpha_{judge} \cdot \text{[expertise influence]}$ | Measures expert input weight |
| Producer | $U_{prod}(x) = \alpha_{prod} \cdot \text{[simplicity + predictability]}$ | Measures operational efficiency |

---

## Control Variables (Mechanism Designer's Instruments)

| Variable | Description | Domain | Example Values |
|----------|-------------|--------|----------------|
| $\theta_1$ | Primary weight parameter (judge vs fan) | $[0.1, 0.9]$ | 0.35 |
| $\theta_2$ | Aggregation method | $\{0, 1, 2\}$ | 0=plurality, 1=Borda, 2=approval |
| $\theta_3$ | Temporal discount factor | $[0.5, 1.0]$ | 0.85 |
| $\theta_4$ | Threshold parameters | $[0, 0.2]$ | 0.08 |
| $\theta_5$ | Tiebreaker rules | $\{0, 1, 2\}$ | 0=fan, 1=judge, 2=random |

---

## Dedicated Variable Table (4 Categories)

You MUST create a separate `model_6_variable_table.md` file with these 4 categories:

### Category Structure

| Category | Description | Target Count |
|----------|-------------|--------------|
| **Control Variables** | Mechanism Designer's Instruments (θ₁ through θ₅+) | 5-8 |
| **State Variables** | Emergent Outcomes (utilities, correlations, rates) | 8-12 |
| **Exogenous Parameters** | Data Inputs from Other Models | 6-10 |
| **Auxiliary Variables** | Computational Tools (Lagrange multipliers, etc.) | 8-12 |

**Total: 30-40 variables with domains, optimal values, and data sources**

### Example Variable Table Format

```markdown
## Control Variables (Mechanism Designer's Instruments)
| Symbol | Name | Domain | Optimal | Description |
|--------|------|--------|---------|-------------|
| θ₁ | Judge score weight | [0.1, 0.9] | 0.35 | Weight on normalized judge scores |
| θ₂ | Vote aggregation | {0,1,2} | 1 | 0=plurality, 1=Borda, 2=approval |
| θ₃ | Temporal discount | [0.5, 1.0] | 0.85 | Decay factor for historical votes |
| θ₄ | Save threshold | [0, 0.2] | 0.08 | Minimum gap for judge save |
| θ₅ | Tiebreaker | {0,1,2} | 1 | 0=fan priority, 1=judge, 2=random |

## State Variables (Emergent Outcomes)
| Symbol | Name | Type | Description |
|--------|------|------|-------------|
| E[U_fan] | Expected fan utility | Derived | Average fan satisfaction |
| E[U_judge] | Expected judge utility | Derived | Average expert influence |
| τ_skill | Skill-outcome correlation | Derived | Kendall's tau between skill and placement |

## Exogenous Parameters (From Data)
| Symbol | Name | Source | Description |
|--------|------|--------|-------------|
| J_{i,t} | Judge scores | Raw CSV | Scores from each judge per episode |
| v_{i,t} | Vote shares | Model 1 | Estimated fan vote proportions |
| S_i | Latent skill | Model 4 | Contestant ability estimate |

## Auxiliary Variables (Computational)
| Symbol | Name | Domain | Description |
|--------|------|--------|-------------|
| λ | Lagrange multiplier (IC) | ℝ⁺ | Incentive compatibility shadow price |
| μ | Lagrange multiplier (IR) | ℝ⁺ | Individual rationality shadow price |
| ν | Lagrange multiplier (BB) | ℝ⁺ | Budget balance shadow price |
```

---

## KKT Derivation Requirements

For the flagship model, you MUST include complete optimality conditions:

### 1. Lagrangian Formulation

```latex
\mathcal{L}(\theta, \lambda, \mu, \nu) = W(\theta) + \lambda^T g(\theta) + \mu^T h(\theta)
```

### 2. First-Order Conditions (Stationarity)

```latex
\nabla_\theta \mathcal{L} = \nabla W(\theta) + \sum_i \lambda_i \nabla g_i(\theta) = 0
```

### 3. Second-Order Sufficient Conditions

```latex
\nabla^2 W(\theta^*) \preceq 0 \quad \text{(Negative Semi-Definite)}
```

### 4. Numerical Verification at Optimum

- Gradient norm: $\|\nabla W(\theta^*)\| < \epsilon$ (typically ε = 0.01)
- Hessian eigenvalues: all $\lambda_i \leq 0$

---

## Specific Mechanism Recommendation

You MUST propose a **concrete mechanism** with:

### Required Components

1. **Exact formula**:
   ```latex
   C_{i,t} = \theta_1 \cdot \tilde{J}_{i,t} + (1-\theta_1) \cdot \tilde{V}_{i,t}^{cumulative}
   ```

2. **Numerical parameter values**:
   - $\theta_1^* = 0.35$ (judge weight)
   - $\theta_3^* = 0.85$ (temporal discount)
   - $\theta_4^* = 0.08$ (save threshold)

3. **Prose description** (≤80 words):
   > "The Weighted Rank-Score Hybrid mechanism combines normalized judge scores (35% weight) with cumulative fan votes (65% weight), where historical votes decay at 15% per week. This balances expert judgment with audience engagement while preventing late-surge manipulation. Contestants scoring below 8% of the leader may be saved by judges, preserving competitive integrity."

---

## Backtesting Methodology

Design for counterfactual analysis:

### Requirements

- **Historical seasons**: Test on 20+ seasons (if available)
- **Elimination tracking**: Count changes vs. status quo
- **Statistical tests**:
  - McNemar test (paired nominal data)
  - Fisher's z transformation (correlation comparison)
  - Permutation test (distribution-free)

### Metrics to Track

| Metric | Description | Target |
|--------|-------------|--------|
| Elimination changes | Seasons with different outcomes | Document count |
| Welfare improvement | W(θ*) - W(θ_SQ) | Positive |
| Fairness delta | τ_skill improvement | > 0 |
| Engagement delta | Fan utility change | ≥ 0 |

---

## Model 6 Output Files

```
output/model/
├── model_design_6_v2.md      # Enhanced with mechanism design framing
├── model_6_variable_table.md # Dedicated 4-category variable taxonomy
└── model_6_proofs.md         # KKT derivations with numerical verification
```

---

## Required References (Include in Bibliography)

| Author | Year | Title | Key Contribution |
|--------|------|-------|------------------|
| Arrow | 1951 | Social Choice and Individual Values | Impossibility theorem |
| Myerson | 1981 | Optimal Auction Design | Revenue equivalence |
| Gibbard | 1973 | Manipulation of Voting Schemes | Strategy-proofness |
| Börgers | 2015 | Introduction to Mechanism Design | Textbook reference |
| Saari | 2001 | Decisions and Elections | Voting paradoxes |

### BibTeX Entries

```bibtex
@book{arrow1951,
  author = {Arrow, Kenneth J.},
  title = {Social Choice and Individual Values},
  year = {1951},
  publisher = {Wiley}
}

@article{myerson1981,
  author = {Myerson, Roger B.},
  title = {Optimal Auction Design},
  journal = {Mathematics of Operations Research},
  year = {1981},
  volume = {6},
  pages = {58--73}
}

@article{gibbard1973,
  author = {Gibbard, Allan},
  title = {Manipulation of Voting Schemes},
  journal = {Econometrica},
  year = {1973},
  volume = {41},
  pages = {587--601}
}

@book{borgers2015,
  author = {Börgers, Tilman},
  title = {An Introduction to the Theory of Mechanism Design},
  year = {2015},
  publisher = {Oxford University Press}
}

@book{saari2001,
  author = {Saari, Donald G.},
  title = {Decisions and Elections: Explaining the Unexpected},
  year = {2001},
  publisher = {Cambridge University Press}
}
```
