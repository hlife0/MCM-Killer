# HMML 2.0 Specification

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Document Type**: Supporting Document
> **Purpose**: Complete specification of Hierarchical Mathematical Modeling Library 2.0

---

## Overview

**HMML 2.0** (Hierarchical Mathematical Modeling Library) is a dynamic, structured knowledge base for mathematical modeling methods with metadata-rich method nodes.

**Evolution from HMML 1.0**:
- **HMML 1.0**: Single static file (`HMML.md`)
- **HMML 2.0**: Structured directory with YAML front matter

---

## Key Improvements

### 1. Dynamic Structure

**HMML 1.0**:
```
HMML/
└── HMML.md (single 10,000+ line file)
```

**HMML 2.0**:
```
HMML/
├── 00_index.md (catalog)
├── differential_equations/
│   ├── 01_ode.md
│   ├── 02_pde.md
│   └── 03_sde.md
├── network_science/
│   ├── 01_graph_theory.md
│   ├── 02_network_dynamics.md
│   └── ...
└── ...
```

### 2. Metadata-Rich Method Nodes

**HMML 1.0**:
```markdown
## Method Name
Description text...
```

**HMML 2.0**:
```markdown
---
method_id: SIR-Network-001
narrative_value: High
complexity: High
common_pitfalls: "Choosing wrong network topology"
oprize_examples: "2019D, 2022F"
tags: [epidemic, network, topology]
---

# SIR-Network Model

Description...
```

### 3. Active Retrieval

**HMML 1.0**: Keyword-based search (passive)

**HMML 2.0**: @knowledge_librarian actively pushes advanced methods (anti-mediocrity enforcement)

---

## Directory Structure

```
knowledge_library/
└── methods/
    ├── 00_index.md                    # Master catalog
    │
    ├── differential_equations/         # Domain: Differential Equations
    │   ├── 01_ordinary_differential_equations.md
    │   ├── 02_partial_differential_equations.md
    │   ├── 03_stochastic_differential_equations.md
    │   └── 04_delay_differential_equations.md
    │
    ├── network_science/               # Domain: Network Science
    │   ├── 01_graph_theory.md
    │   ├── 02_network_dynamics.md
    │   ├── 03_spread_on_networks.md
    │   └── 04_network_optimization.md
    │
    ├── time_series_analysis/          # Domain: Time Series
    │   ├── 01_arima.md
    │   ├── 02_state_space_models.md
    │   ├── 03_spectral_analysis.md
    │   └── 04_transformer_models.md
    │
    ├── machine_learning/              # Domain: Machine Learning
    │   ├── 01_regression.md
    │   ├── 02_classification.md
    │   ├── 03_clustering.md
    │   └── 04_deep_learning.md
    │
    ├── optimization/                  # Domain: Optimization
    │   ├── 01_linear_programming.md
    │   ├── 02_nonlinear_programming.md
    │   ├── 03_heuristic_algorithms.md
    │   └── 04_multi_objective.md
    │
    ├── stochastic_processes/          # Domain: Stochastic Processes
    │   ├── 01_markov_chains.md
    │   ├── 02_poisson_processes.md
    │   ├── 03_random_walks.md
    │   └── 04_brownian_motion.md
    │
    └── agent_based_modeling/          # Domain: Agent-Based
        ├── 01_cellular_automata.md
        ├── 02_multi_agent_systems.md
        └── 03_individual_based_models.md
```

---

## Method Node Template

### YAML Front Matter

```yaml
---
method_id: UNIQUE-ID
domain: [domain_name]
subdomain: [subdomain_name]
narrative_value: Very High | High | Medium | Low | Baseline
complexity: Very High | High | Medium | Low
oprize_compatibility: Excellent | Good | Fair | Poor
common_pitfalls: |
  [List of common mistakes]
oprize_examples: |
  [List of O-Prize papers using this method]
tags: [tag1, tag2, tag3]
dependencies: [method_id1, method_id2]
last_updated: 2026-01-24
version: 2.0
---

# [Method Name]

## Mathematical Formulation

[Equations, definitions]

## Physical Interpretation

[What does this model represent?]

## When to Use This Method

[Appropriate use cases]

## Common Pitfalls

[What to avoid]

## Implementation Notes

[Practical tips]

## O-Prize Examples

[Papers that successfully used this method]

## References

[Academic references]
```

---

## Example Method Node

### SIR-Network Model

```markdown
---
method_id: SIR-NET-001
domain: differential_equations
subdomain: network_dynamics
narrative_value: Very High
complexity: High
oprize_compatibility: Excellent
common_pitfalls: |
  - Using synthetic/unrealistic network
  - Ignoring network topology effects
  - Not calibrating transmission parameter β
oprize_examples: |
  - 2019 Problem D (Ecosystem) - O-Prize winner
  - 2022 Problem F (Disinformation) - Meritorious
tags: [epidemic, network, topology, infectious_disease]
dependencies: [SIR-BASIC-001, GRAPH-THEORY-001]
last_updated: 2026-01-24
version: 2.0
---

# SIR-Network Model

## Mathematical Formulation

For each node *i* in network:

```
dS_i/dt = -β S_i Σ_j A_ij (I_j / N_j)
dI_i/dt = β S_i Σ_j A_ij (I_j / N_j) - γ I_i
dR_i/dt = γ I_i
```

Where:
- *S_i, I_i, R_i*: Susceptible, Infected, Recovered at node *i*
- *A_ij*: Adjacency matrix element (1 if connection, 0 otherwise)
- *N_j*: Total population at node *j*
- *β*: Transmission rate
- *γ*: Recovery rate

## Physical Interpretation

Standard SIR assumes homogeneous mixing - every individual has equal chance
of infecting every other individual.

**SIR-Network** recognizes that real populations have **network structure**:
- Individuals connected via transportation, social, communication links
- **Hub nodes** (airports, cities) accelerate spread
- **Topology matters** - network structure determines epidemic dynamics

## When to Use This Method

✅ **Use When**:
- Problem involves spatial or network structure
- Data includes connection information (routes, friendships, etc.)
- Interested in **topological effects** (hub influence, community structure)
- Want to identify **critical nodes** for intervention

❌ **Don't Use When**:
- Population is truly homogeneous (well-mixed)
- No network data available
- Standard SIR suffices (no topological insights needed)

## Common Pitfalls

### Pitfall 1: Synthetic Network
**Problem**: Using random network (Erdős-Rényi) for real-world problem

**Fix**: Use real network data (airline routes, social network, etc.)

**Narrative Damage**: Judges will recognize synthetic network - low credibility

### Pitfall 2: Ignoring Network Quality
**Problem**: Not validating network structure

**Fix**:
- Check degree distribution (real networks often scale-free)
- Verify clustering coefficient
- Compare with known network properties

### Pitfall 3: Arbitrary β Calibration
**Problem**: Choosing β without justification

**Fix**:
- Calibrate to early epidemic data
- Use literature values for similar diseases
- Perform sensitivity analysis (β ± 10%, ± 20%)

## Implementation Notes

### Step 1: Build Adjacency Matrix
```python
import numpy as np

# Load network data
A = np.load('network_adjacency.npy')

# Normalize by population
N = np.load('node_populations.npy')
A_normalized = A / N[np.newaxis, :]
```

### Step 2: Define ODE System
```python
def sir_network(y, t, beta, gamma, A_norm, N):
    S, I, R = y.reshape(3, -1)

    dSdt = -beta * S * (A_norm @ (I / N))
    dIdt = beta * S * (A_norm @ (I / N)) - gamma * I
    dRdt = gamma * I

    return np.concatenate([dSdt, dIdt, dRdt])
```

### Step 3: Solve
```python
from scipy.integrate import odeint

y0 = np.concatenate([S0, I0, R0])
t = np.linspace(0, 100, 1000)

solution = odeint(sir_network, y0, t, args=(beta, gamma, A_norm, N))
```

## O-Prize Examples

### 2019 Problem D (Ecosystem) - O-Prize Winner
**Problem**: Species extinction in island ecosystem

**Approach**:
- Modeled species migration as network flow
- Identified "hub islands" critical for survival
- Demonstrated network topology determines extinction cascades

**Key Insight**: "Protecting hub islands prevents 73% of extinctions"

### 2022 Problem F (Disinformation) - Meritorious
**Problem**: Disinformation spread on social network

**Approach**:
- SIR-Network for disinformation dynamics
- Identified "superspreaders" via network centrality
- Proposed intervention strategies

**Key Insight**: "Targeting top 5% of users reduces spread by 68%"

## Narrative Value

**High** - SIR-Network enables discussion of:

1. **Topological Insights**: "Hub nodes accelerate spread by 43%"
2. **Intervention Leverage**: "Network centrality identifies critical targets"
3. **Uncertainty Quantification**: "We propagate β uncertainty, generating 95% CI bands"
4. **Policy Implications**: "Targeted vaccination at hubs is 3.2x more effective than random"

## Comparison to Alternatives

| Method | Advantages | Disadvantages | O-Prize Value |
|--------|-----------|---------------|---------------|
| **Basic SIR** | Simple, fast | Ignores topology | Low (baseline only) |
| **SIR-Network** | Captures topology | Requires network data | **Very High** |
| **SIR-SDE** | Uncertainty quantification | Complex | High |
| **ABM** | Micro-foundations | Computationally expensive | Very High |

## References

1. Pastor-Satorras, R., et al. (2015). "Epidemic processes in complex networks"
2. Newman, M. (2002). "Spread of epidemic disease on networks"
3. Keeling, M. J., & Eames, K. T. (2005). "Networks and epidemic models"

---

**Version**: 2.0
**Last Updated**: 2026-01-24
**Contributors**: @knowledge_librarian, @researcher
```

---

## 00_index.md (Master Catalog)

### Structure

```markdown
# HMML 2.0 - Master Index

## Statistics
- **Total Methods**: 98+
- **Domains**: 7
- **Average Narrative Value**: High
- **Last Updated**: 2026-01-24

---

## Domain 1: Differential Equations

### 1.1 Ordinary Differential Equations
- **SIR-BASIC-001**: Basic SIR Model (Baseline)
- **SEIR-BASIC-002**: SEIR Model (Medium)
- **SIR-NET-001**: SIR-Network Model (**Very High** narrative value)

### 1.2 Partial Differential Equations
- **HEAT-EQN-001**: Heat Equation (Medium)
- **WAVE-EQN-001**: Wave Equation (Medium)
- **REACTION-DIFF-001**: Reaction-Diffusion (High)

### 1.3 Stochastic Differential Equations
- **SIR-SDE-001**: SIR with Noise (**High** narrative value)
- **GBM-001**: Geometric Brownian Motion (Medium)
- **LANGEVIN-001**: Langevin Equation (High)

---

## Domain 2: Network Science

### 2.1 Graph Theory
- **GRAPH-THEORY-001**: Centrality Measures (Medium)
- **COMMUNITY-001**: Community Detection (High)

### 2.2 Network Dynamics
- **SIR-NET-001**: SIR on Networks (**Very High**)
- **VOTER-MODEL-001**: Voter Model (Medium)
- **LINEAR-THRESHOLD-001**: Linear Threshold Model (High)

---

## Domain 3: Time Series Analysis

### 3.1 Classical Methods
- **ARIMA-001**: ARIMA (Baseline - **Low** O-Prize value)
- **SARIMA-001**: SARIMA (Low)
- **VAR-001**: Vector Autoregression (Medium)

### 3.2 Modern Methods
- **STATE-SPACE-001**: State-Space Models (High)
- **TRANSFORMER-001**: Transformer for Time Series (**High**)
- **SPECTRAL-001**: Spectral Analysis (Medium)

---

## Domain 4: Machine Learning

### 4.1 Supervised Learning
- **REGRESSION-001**: Linear Regression (Baseline)
- **RANDOM-FOREST-001**: Random Forest (Medium)
- **XGBOOST-001**: XGBoost (Medium)
- **NEURAL-NET-001**: Neural Networks (High)

### 4.2 Deep Learning
- **LSTM-001**: LSTM for Time Series (**High**)
- **CNN-SPATIAL-001**: CNN for Spatial Data (High)
- **GNN-001**: Graph Neural Networks (**Very High**)

---

## Domain 5: Optimization

### 5.1 Linear Optimization
- **LP-001**: Linear Programming (Medium)
- **INTEGER-LP-001**: Integer Programming (High)

### 5.2 Nonlinear Optimization
- **NLP-001**: Nonlinear Programming (High)
- **CONVEX-001**: Convex Optimization (Medium)

### 5.3 Heuristics
- **GA-001**: Genetic Algorithm (Medium)
- **SA-001**: Simulated Annealing (Medium)
- **PSO-001**: Particle Swarm Optimization (Medium)

---

## Domain 6: Stochastic Processes

### 6.1 Markov Processes
- **DTMC-001**: Discrete-Time Markov Chain (Medium)
- **CTMC-001**: Continuous-Time Markov Chain (High)
- **MCMC-001**: Markov Chain Monte Carlo (High)

### 6.2 Point Processes
- **POISSON-001**: Poisson Process (Medium)
- **HAWKES-001**: Hawkes Process (High)
- **COX-001**: Cox Process (Medium)

---

## Domain 7: Agent-Based Modeling

### 7.1 Cellular Automata
- **CA-EPIDEMIC-001**: Cellular Automata Epidemic (Medium)
- **CA-TRAFFIC-001**: Traffic CA (Medium)

### 7.2 Multi-Agent Systems
- **ABM-EPIDEMIC-001**: Agent-Based Epidemic (**Very High**)
- **ABM-ECONOMIC-001**: Economic ABM (High)
- **ABM-SOCIAL-001**: Social ABM (High)

---

## Narrative Value Ranking

### Very High Narrative Value (⭐⭐⭐⭐⭐)
- SIR-NET-001: SIR-Network Model
- SIR-SDE-001: SIR with Stochastic Differential Equations
- ABM-EPIDEMIC-001: Agent-Based Epidemic Model
- GNN-001: Graph Neural Networks
- HAWKES-001: Hawkes Processes

### High Narrative Value (⭐⭐⭐⭐)
- REACTION-DIFF-001: Reaction-Diffusion Equations
- STATE-SPACE-001: State-Space Models
- TRANSFORMER-001: Transformer for Time Series
- LSTM-001: LSTM for Time Series

### Baseline Methods (Use for comparison only)
- SIR-BASIC-001: Basic SIR Model
- REGRESSION-001: Linear Regression
- ARIMA-001: ARIMA

---

## Search by Problem Type

### Epidemic Problems
1. SIR-NET-001 (Network topology)
2. SIR-SDE-001 (Uncertainty)
3. ABM-EPIDEMIC-001 (Micro-foundations)

### Optimization Problems
1. GA-001 (Genetic Algorithm)
2. SA-001 (Simulated Annealing)
3. MULTI-OBJ-001 (Multi-Objective)

### Time Series Problems
1. STATE-SPACE-001 (State-Space)
2. SDE-001 (Stochastic Differential Equations)
3. TRANSFORMER-001 (Deep Learning)

### Network Problems
1. SIR-NET-001 (Epidemic on networks)
2. GNN-001 (Graph Neural Networks)
3. COMMUNITY-001 (Community Detection)

---

## Migration from HMML 1.0

See `tools/migrate_hmml.py` for automatic migration script.

**Usage**:
```bash
python tools/migrate_hmml.py HMML/HMML.md knowledge_library/methods/
```

**Output**: Structured directory with YAML front matter
```
knowledge_library/methods/
├── 00_index.md
├── differential_equations/
├── network_science/
└── ...
```

---

**Version**: 2.0
**Last Updated**: 2026-01-24
**Maintainer**: @knowledge_librarian
