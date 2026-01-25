# Template: HMML 2.0 Method File

> **Purpose**: Standardized format for knowledge library method entries
> **Used By**: @knowledge_librarian, @researcher
> **Location**: `knowledge_library/methods/{domain}/{category}/{method}.md`

---

## YAML Front Matter (Required)

```yaml
---
name: "{Method Name}"
domain: "{Primary Domain}"
category: "{Subcategory}"
complexity: "{Very High / High / Medium / Low}"
implementation_time: "{X-Y hours}"
narrative_value: "{Very High / High / Medium / Low}"
o_prize_examples:
  - year: {YYYY}
    problem: "{Letter}"
    usage: "{Brief description}"
keywords:
  - "{keyword1}"
  - "{keyword2}"
  - "{keyword3}"
prerequisites:
  - "{prerequisite1}"
  - "{prerequisite2}"
common_pitfalls:
  - "{pitfall1}"
  - "{pitfall2}"
last_updated: "{YYYY-MM-DD}"
---
```

---

## Field Definitions

### Required Fields

| Field | Description | Valid Values |
|-------|-------------|--------------|
| `name` | Human-readable method name | Any string |
| `domain` | Primary domain classification | optimization, differential_equations, statistics, network_science, machine_learning, simulation |
| `category` | Subcategory within domain | Domain-specific |
| `complexity` | Implementation difficulty | Very High, High, Medium, Low |
| `implementation_time` | Typical time range | "X-Y hours" format |
| `narrative_value` | Value for paper narrative | Very High, High, Medium, Low |

### Optional Fields

| Field | Description |
|-------|-------------|
| `o_prize_examples` | List of O-Prize papers using this method |
| `keywords` | Search terms for retrieval |
| `prerequisites` | Required knowledge/methods |
| `common_pitfalls` | Mistakes to avoid |
| `last_updated` | Date of last revision |

---

## Body Structure Template

```markdown
# {Method Name}

> **Domain**: {domain}
> **Complexity**: {complexity}
> **Narrative Value**: {narrative_value}

---

## Overview

[2-3 sentence description of what this method does and when to use it]

---

## Mathematical Foundation

### Core Formulation

[LaTeX equations defining the method]

$$
[Main equation]
$$

### Key Variables

| Variable | Description | Typical Range |
|----------|-------------|---------------|
| $X$ | [Description] | [Range] |
| $Y$ | [Description] | [Range] |

### Assumptions

1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

---

## When to Use

### Good Fit
- [Scenario 1 where this method excels]
- [Scenario 2]
- [Scenario 3]

### Poor Fit
- [Scenario where this method fails]
- [Alternative to use instead]

---

## Implementation Guide

### Step 1: [First Step]
[Description and code snippet]

```python
# Example code
```

### Step 2: [Second Step]
[Description and code snippet]

### Step 3: [Third Step]
[Description and code snippet]

### Complete Example

```python
# Full working example
```

---

## Narrative Value

### Why This Wins O-Prize

[Explanation of what makes this method compelling for judges]

### Key Phrases for Paper

- "[Phrase 1 that sounds impressive and accurate]"
- "[Phrase 2]"
- "[Phrase 3]"

### Observation-Implication Templates

> "Our [method] achieves [metric] = [value] (Observation), indicating that
> [physical meaning] (Implication)."

> "[Method feature] enables [capability] (Observation), demonstrating
> [value proposition] (Implication)."

---

## Common Pitfalls

### Pitfall 1: [Name]
- **Symptom**: [What goes wrong]
- **Cause**: [Why it happens]
- **Fix**: [How to resolve]

### Pitfall 2: [Name]
- **Symptom**: [...]
- **Cause**: [...]
- **Fix**: [...]

---

## O-Prize Examples

### {Year} Problem {Letter}: {Title}

**Usage**: [How this method was applied]

**Key Innovation**: [What made it O-Prize worthy]

**Quote**: "[Relevant quote from paper]"

---

## Related Methods

- [{Related Method 1}](path/to/method1.md) - [Relationship]
- [{Related Method 2}](path/to/method2.md) - [Relationship]

---

## References

1. [Academic reference 1]
2. [Academic reference 2]

---

## Version History

- **v1.0** ({Date}): Initial entry
```

---

## Example: Complete Method File

```yaml
---
name: "SIR-Network Model"
domain: "differential_equations"
category: "epidemic"
complexity: "High"
implementation_time: "3-4 hours"
narrative_value: "Very High"
o_prize_examples:
  - year: 2019
    problem: "D"
    usage: "Ecosystem network dynamics"
  - year: 2022
    problem: "F"
    usage: "Disinformation spread modeling"
keywords:
  - "epidemic"
  - "network"
  - "SIR"
  - "transmission"
  - "compartmental"
prerequisites:
  - "Basic SIR model"
  - "Network/graph theory basics"
  - "ODE solving"
common_pitfalls:
  - "Using synthetic network instead of real data"
  - "Ignoring network sparsity"
  - "Not validating network structure"
last_updated: "2026-01-25"
---
```

```markdown
# SIR-Network Model

> **Domain**: differential_equations
> **Complexity**: High
> **Narrative Value**: Very High

---

## Overview

The SIR-Network model extends the classic SIR compartmental model by
incorporating explicit network topology. Instead of assuming homogeneous
mixing, transmission occurs through network edges (e.g., airline routes,
social connections). This enables identification of critical hub nodes
and captures cascade dynamics invisible to aggregate models.

---

## Mathematical Foundation

### Core Formulation

$$
\frac{dS_i}{dt} = -\beta S_i \sum_j A_{ij} \frac{I_j}{N_j}
$$

$$
\frac{dI_i}{dt} = \beta S_i \sum_j A_{ij} \frac{I_j}{N_j} - \gamma I_i
$$

$$
\frac{dR_i}{dt} = \gamma I_i
$$

Where $A_{ij}$ is the normalized adjacency matrix from network data.

### Key Variables

| Variable | Description | Typical Range |
|----------|-------------|---------------|
| $\beta$ | Transmission rate | 0.1 - 1.0 |
| $\gamma$ | Recovery rate | 0.05 - 0.5 |
| $A_{ij}$ | Adjacency weight | 0 - 1 (normalized) |
| $S_i, I_i, R_i$ | Compartment sizes | 0 - $N_i$ |

### Assumptions

1. Transmission through network edges only
2. Constant parameters (can be relaxed)
3. No vital dynamics (births/deaths)
4. Network structure is known

---

## When to Use

### Good Fit
- Epidemic/information spread with known network structure
- When hub identification is important
- Policy analysis requiring targeted interventions
- Data includes spatial/connectivity information

### Poor Fit
- No network data available → Use basic SIR
- Very dense networks (>50% connectivity) → Homogeneous mixing adequate
- Individual-level heterogeneity needed → Use Agent-Based Model

---

## Implementation Guide

### Step 1: Construct Adjacency Matrix

```python
import numpy as np
import pandas as pd

def build_adjacency(edges_df, n_nodes):
    """Build normalized adjacency matrix from edge data."""
    A = np.zeros((n_nodes, n_nodes))
    for _, row in edges_df.iterrows():
        A[row['source'], row['target']] = row['weight']
    # Normalize rows
    row_sums = A.sum(axis=1, keepdims=True)
    A = np.divide(A, row_sums, where=row_sums > 0)
    return A
```

### Step 2: Define ODE System

```python
def sir_network_ode(t, y, A, beta, gamma, N):
    """SIR-Network ODE system."""
    n = len(N)
    S, I, R = y[:n], y[n:2*n], y[2*n:]

    # Transmission term with network structure
    infection_pressure = A @ (I / N)
    dS = -beta * S * infection_pressure
    dI = beta * S * infection_pressure - gamma * I
    dR = gamma * I

    return np.concatenate([dS, dI, dR])
```

### Step 3: Solve and Analyze

```python
from scipy.integrate import solve_ivp

# Initial conditions
y0 = np.concatenate([S0, I0, R0])

# Solve
sol = solve_ivp(
    sir_network_ode,
    t_span=(0, 100),
    y0=y0,
    args=(A, beta, gamma, N),
    method='RK45'
)

# Extract results
S_t = sol.y[:n]
I_t = sol.y[n:2*n]
R_t = sol.y[2*n:]
```

---

## Narrative Value

### Why This Wins O-Prize

1. **Topological Insight**: Captures how network structure affects dynamics
2. **Policy Actionable**: Identifies hub nodes for targeted intervention
3. **Modern Methods**: Shows awareness of network science literature
4. **Visualization Rich**: Network diagrams are visually compelling

### Key Phrases for Paper

- "Network topology is a first-order effect on transmission dynamics"
- "Hub seeding accelerates epidemic spread by X%"
- "Centrality-based intervention prioritization"
- "The adjacency structure reveals cascade pathways"

### Observation-Implication Templates

> "Our SIR-Network model achieves RMSE = 4.2 (Observation), indicating
> that explicit network structure captures dynamics invisible to
> aggregate compartmental models (Implication)."

> "Hub cities (top 10% centrality) account for 67% of initial spread
> (Observation), demonstrating the leverage of targeted interventions
> at network hubs (Implication)."

---

## Common Pitfalls

### Pitfall 1: Synthetic Network
- **Symptom**: Model doesn't match real dynamics
- **Cause**: Using random/scale-free generator instead of real data
- **Fix**: Use actual airline traffic, social network, or contact data

### Pitfall 2: Ignoring Sparsity
- **Symptom**: Memory errors, slow computation
- **Cause**: Treating sparse network as dense matrix
- **Fix**: Use scipy.sparse for large networks

### Pitfall 3: Unvalidated Structure
- **Symptom**: Results sensitive to network choice
- **Cause**: Network may not represent actual transmission pathways
- **Fix**: Compare multiple network topologies, validate against data

---

## O-Prize Examples

### 2019 Problem D: Ecosystem Dynamics

**Usage**: Modeled species interactions as network edges

**Key Innovation**: Combined network SIR with trophic levels

**Quote**: "The network structure captures cascade effects in food web
disruption that aggregate models miss entirely."

---

## Related Methods

- [Basic SIR](../epidemic/sir_basic.md) - Simpler baseline
- [SEIR-Network](../epidemic/seir_network.md) - With exposed compartment
- [Agent-Based Model](../../machine_learning/abm/simple_abm.md) - Individual-level alternative

---

## References

1. Pastor-Satorras, R., & Vespignani, A. (2001). Epidemic spreading in scale-free networks. Physical Review Letters.
2. Newman, M. E. (2002). Spread of epidemic disease on networks. Physical Review E.

---

## Version History

- **v1.0** (2026-01-25): Initial entry from m-orientation
```

---

## Domain Hierarchy

```
knowledge_library/
├── methods/
│   ├── optimization/
│   │   ├── linear_programming/
│   │   ├── nonlinear_optimization/
│   │   └── heuristics/
│   ├── differential_equations/
│   │   ├── epidemic/
│   │   ├── sde/
│   │   └── pde/
│   ├── statistics/
│   │   ├── bayesian/
│   │   ├── frequentist/
│   │   └── time_series/
│   ├── network_science/
│   │   ├── centrality/
│   │   ├── community/
│   │   └── dynamics/
│   ├── machine_learning/
│   │   ├── supervised/
│   │   ├── unsupervised/
│   │   └── abm/
│   └── simulation/
│       ├── monte_carlo/
│       └── discrete_event/
└── index.md
```

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
