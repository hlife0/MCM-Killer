# Protocol 22: Phase 0.2 - Active Knowledge Retrieval

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Phase**: Phase 0.2 (New)
> **Agent**: @knowledge_librarian
> **Trigger**: After Phase 0 (Problem Understanding)

---

## Purpose

**Proactively push advanced O-Prize-level methods** to @researcher and @modeler, preventing them from choosing "safe but mediocre" methods (Linear Regression, Basic SIR, ARIMA).

This is **"anti-mediocrity enforcement"** - the system actively prevents choosing methods that are too simple for the problem complexity.

---

## When to Execute

**Trigger**: Phase 0 (Problem Understanding) completes

**Input**: @reader's `output/docs/requirements/problem_statement.md`

**Agent**: @knowledge_librarian (Mode 2: In-Game)

---

## Process

### Step 1: Analyze Problem Requirements

**Read**: `output/docs/requirements/problem_statement.md`

**Extract Keywords**:
- Domain keywords (epidemic, network, time-series, optimization, etc.)
- Problem complexity indicators (data size, multi-factor, spatial-temporal, etc.)
- Explicit requirements (must-have vs nice-to-have)

### Step 2: Identify Domain

**Keyword Mapping**:
```
"epidemic", "disease", "infection" → Epidemiology / Network Science
"route", "shortest path", "logistics" → Optimization / Network Science
"forecast", "trend", "time-series" → Time Series / Stochastic Processes
"network", "graph", "connection" → Network Science / Graph Theory
"classification", "prediction" → Machine Learning
```

### Step 3: Retrieve Methods from HMML 2.0

**Query**: `knowledge_library/methods/index.md`

**Filter by Domain**: Retrieve methods from matching domains

**Filter by Complexity**: Prioritize High/Very High complexity methods

### Step 4: Apply Anti-Mediocrity Filter

**Banned Methods** (require explicit justification):
- Linear Regression (for complex dynamics)
- Basic SIR/SEIR (when network structure available)
- ARIMA (for network dynamics)
- Simple Logistic Regression
- Dijkstra (for simple routing problems)

**Reason**: These methods are "baseline" - too common in MCM, not O-Prize-winning unless justified

### Step 5: Recommend Advanced Methods

**Push Excellence Methods**:

| Domain | Advanced Methods | O-Prize Narrative Value |
|--------|-----------------|-------------------------|
| **Epidemic** | SIR-Network, SDE, ABM | High: Topology, uncertainty, micro-foundations |
| **Time Series** | SDE, Transformer, State-Space | High: Stochasticity, deep learning |
| **Network** | GNN, ABM, Network Optimization | Very High: Modern methods |
| **Optimization** | Genetic Algorithm, Simulated Annealing, Multi-Objective | Medium: Heuristics |

### Step 6: Provide Mathematical Justification

For each recommended method, explain:
1. **Why this method?** (Theoretical advantage)
2. **What papers used it?** (O-Prize examples)
3. **What's the narrative value?** (How to "sell" it)

**Example**:
```
✅ RECOMMEND: SIR-Network Model ⭐⭐⭐⭐⭐

Mathematical Foundation:
dS_i/dt = -β S_i Σ_j A_ij (I_j / N_j)
dI_i/dt = β S_i Σ_j A_ij (I_j / N_j) - γ I_i

Why This Method Wins:
1. **Topological Insight**: "Our model captures how hub seeding accelerates spread by 43%"
2. **Intervention Leverage**: "Network centrality identifies critical nodes for targeted vaccination"
3. **Uncertainty Quantification**: "We propagate parameter uncertainty, generating 95% CI bands"

O-Prize Examples:
- 2019 Problem D (Ecosystem) - Network model won O-Prize
- 2022 Problem F (Disinformation) - SIR-Network variant
```

---

## Output Format

### Generated: `output/docs/knowledge/suggested_methods.md`

**Structure**:
```markdown
# Suggested Methods for {Problem}

## Problem Analysis
- **Domain**: [Epidemic + Network + Time-Series]
- **Complexity**: High (multi-factor, spatial-temporal)
- **O-Prize Potential**: Very High

## ❌ AVOID (Mediocrity Alert)

### Banned Methods (Without Strong Justification)
1. **Basic SIR/SEIR**
   - **Why**: Too common, seen in 40%+ MCM papers
   - **Unless**: You combine with novel network structure

2. **ARIMA / Linear Regression**
   - **Why**: Inappropriate for network dynamics
   - **Unless**: For baseline comparison only (not primary model)

## ✅ RECOMMENDED (O-Prize Level)

### Method 1: SIR-Network Model ⭐⭐⭐⭐⭐
- **Domain**: Differential Equations + Network Science
- **Narrative Value**: **High** - Demonstrates understanding of topology effects
- **Complexity**: High (requires adjacency matrix, ODE solver)
- **O-Prize Examples**: [List papers]

### Method 2: Stochastic Differential Equations (SDE) ⭐⭐⭐⭐⭐
- **Domain**: Advanced Statistics
- **Narrative Value**: **Very High** - Enables uncertainty discussion
- **Complexity**: High (requires Euler-Maruyama, calibration)

### Method 3: Agent-Based Model (ABM) ⭐⭐⭐⭐⭐
- **Domain**: Computational Modeling
- **Narrative Value**: **Very High** - Shows micro-foundations
- **Complexity**: Very High (individual rules, emergent behavior)

## Integration Strategy
**Recommended Hybrid**: SIR-Network (macro) + ABM (micro validation)

Rationale: SIR-Network provides efficient simulation; ABM validates micro-assumptions.

## Common Pitfalls to Avoid
1. Over-Complexity: ABM with 1000+ parameters → Unidentifiable
2. Network Quality: Using synthetic/unrealistic network
3. SDE Calibration: Choosing σ arbitrarily
```

---

## Quality Assurance

### Verification Checklist

After Phase 0.2 completion, verify:

- [ ] `suggested_methods.md` generated
- [ ] Contains "❌ AVOID" section with banned methods
- [ ] Contains "✅ RECOMMENDED" section with ≥3 advanced methods
- [ ] Each recommended method has:
  - [ ] Mathematical formulation
  - [ ] O-Prize examples
  - [ ] Narrative value explanation
- [ ] Integration strategy provided

### Test Case

**Input**: Problem about "Epidemic spread on airline network"

**Expected Output**:
```
✅ Domain: Epidemic + Network
✅ Banned: Basic SIR
✅ Recommended: SIR-Network, SDE, ABM
✅ Justification: Network structure critical for topology effects
```

---

## Dependencies

**Input**:
- `output/docs/requirements/problem_statement.md`
- `knowledge_library/methods/index.md` (HMML 2.0 catalog)

**Output**:
- `output/docs/knowledge/suggested_methods.md`

**Agent**: @knowledge_librarian

---

## Anti-Patterns

### Anti-Pattern 1: Passive Search Engine

**❌ BAD**: @knowledge_librarian acts as passive search engine
> "You asked for time series methods. Here are some methods: ARIMA, SARIMA, VAR..."

**✅ GOOD**: @knowledge_librarian acts as opinionated expert
> "ARIMA is banned. For network data, use SIR-Network or ABM. Here's why..."

### Anti-Pattern 2: No Mathematical Justification

**❌ BAD**: "We recommend SIR-Network because it's good."

**✅ GOOD**: "We recommend SIR-Network because:
1. It captures network topology effects (Figure X shows...)
2. O-Prize 2019D used it successfully
3. It enables discussion of targeted intervention (critical for policy)
"

---

## Integration with Other Protocols

### Protocol 1: File Reporting

When @knowledge_librarian outputs `suggested_methods.md`, it must state:
```
I have read: knowledge_library/methods/index.md
I have written: output/docs/knowledge/suggested_methods.md
```

### Protocol 8: Model Design Expectations

@modeler's design expectations table should reference methods from `suggested_methods.md`.

### Protocol 15: Interpretation over Description

When recommending methods, explain the physical meaning, not just the math.

---

## Success Criteria

Phase 0.2 is successful when:

1. ✅ `suggested_methods.md` generated
2. ✅ Contains banned methods list with justification
3. ✅ Contains ≥3 advanced method recommendations
4. ✅ Each recommendation has mathematical + narrative justification
5. ✅ @modeler uses recommended methods in design
6. ✅ @researcher doesn't propose basic methods without justification

---

## Impact

**Without Phase 0.2**:
- @researcher proposes: "Linear Regression for epidemic prediction"
- Model is "correct but boring" - no O-Prize potential

**With Phase 0.2**:
- @knowledge_librarian pushes: "SIR-Network or ABM"
- Model is "insightful and competitive" - O-Prize level

**Value**: **Transforms "correct" papers into "insightful" papers.**

---

**Document Version**: v3.1.0
**Related Protocols**: Protocol 14 (Style Alignment), Protocol 15 (Interpretation)
**Related Agents**: @knowledge_librarian, @researcher, @modeler
