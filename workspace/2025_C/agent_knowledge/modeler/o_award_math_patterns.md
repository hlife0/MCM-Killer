# O Award Mathematical Examples

**Purpose**: This file contains patterns and anti-patterns from O Award-winning papers to guide mathematical model formulation. Use these examples to ensure your models meet O Award standards for clarity, rigor, and physical insight.

**Source**: Extracted from modeler.md lines 72-306

---

## O Award Training: Mathematical Rigor

> **"O Award papers balance mathematical sophistication with physical insight. Every equation tells a story."**

### Study Session: What O Award Math Looks Like

From analyzing reference papers 2425454, 2401298, and paper(1):

#### ✅ Pattern 1: Clean, Progressive Notation

**O Award Example** (2425454):
```
We begin with the basic SIR framework:

dS/dt = -βSI/N                    (1a)
dI/dt = βSI/N - γI                (1b)
dR/dt = γI                        (1c)

where:
- S(t), I(t), R(t): Susceptible, Infected, Recovered populations at time t
- β: transmission rate (infections per contact per day)
- γ: recovery rate (1/infectious period)
- N = S + I + R: total population (conserved)

We then extend to the network setting by allowing β to vary with network connectivity:

dS_i/dt = -S_i Σ_j β_ij I_j/N_i    (2a)
dI_i/dt = S_i Σ_j β_ij I_j/N_i - γ_i I_i    (2b)
dR_i/dt = γ_i I_i                   (2c)

where i indexes cities, β_ij = β₀·w_ij encodes transmission from city j to i weighted by air traffic flow w_ij.
```

**Why This Works**:
- ✅ Equations numbered consistently
- ✅ Variables defined BEFORE use
- ✅ Physical meaning explained
- ✅ Progressive complexity (basic → extended)
- ✅ Notation connects to parameters (β₀ is base rate, w_ij is weight)

#### ❌ Anti-Pattern 1: "Equation Dump"

**Bad Example**:
```
Our model is:

dS_i/dt = -S_i Σ_j β_ij I_j/N_i
dI_i/dt = S_i Σ_j β_ij I_j/N_i - γ_i I_i
dR_i/dt = γ_i I_i
dβ_ij/dt = α(w_ij - β_ij)

[No explanation, jumps to complex form immediately, variables undefined]
```

**Why This Fails**:
- ❌ Variables not defined
- ❌ No progression from simple to complex
- ❌ No physical interpretation
- ❌ Judges can't follow the logic

---

#### ✅ Pattern 2: Explicit Assumption Management

**O Award Example** (2401298):
```
## 3.2 Model Assumptions

We make the following simplifying assumptions, with justifications:

**Assumption 1**: Homogeneous mixing within cities
- **Statement**: Transmission within city i follows mass-action kinetics
- **Justification**: City-level is finest granularity in available data
- **Validity**: Tested in Section 5.2 with two-tier urban/rural model; results differ by <3%
- **Limitation**: Ignores neighborhood-level clustering (future work)

**Assumption 2**: Constant transmission rate β
- **Statement**: β does not vary with time or behavioral changes
- **Justification**: 90-day horizon is short relative to behavioral adaptation timescales (~6 months, per WHO 2020)
- **Validity**: Sensitivity analysis (Section 5.3) shows ±30% variation in β changes predictions by <15%
- **Limitation**: If intervention causes behavior change, model may overestimate spread

**Assumption 3**: Network structure remains static
- **Statement**: Air traffic matrix w_ij constant over forecast period
- **Justification**: Historical data shows <5% weekly variation except holidays
- **Validity**: Excluded Chinese New Year week from training (outlier)
- **Limitation**: Travel restrictions would invalidate this assumption
```

**Why This Works**:
- ✅ Each assumption has 4-part structure: Statement, Justification, Validity, Limitation
- ✅ Testable claims (validated in Section 5.2)
- ✅ Honest about what model CAN'T do
- ✅ Shows mature understanding of modeling trade-offs

#### ❌ Anti-Pattern 2: Hidden or Unjustified Assumptions

**Bad Example**:
```
We assume homogeneous mixing and constant parameters.
```

**Why This Fails**:
- ❌ No justification why assumptions are reasonable
- ❌ No discussion of when they'd break
- ❌ Judges wonder if you know the limitations

---

#### ✅ Pattern 3: Parameter Tables with Physical Ranges

**O Award Example** (2425454):
```
## 3.3 Parameter Definitions

| Parameter | Symbol | Physical Meaning | Typical Range | Units | Estimation Method |
|-----------|--------|------------------|---------------|-------|-------------------|
| Base transmission rate | β₀ | Infections per contact | 0.2-0.8 | day⁻¹ | MLE from data |
| Recovery rate | γ | Inverse infectious period | 0.1-0.3 | day⁻¹ | Literature (1/7 to 1/3 days) |
| Network weight | w_ij | Air traffic flow | 0-10,000 | passengers/day | Direct measurement |
| Hub amplification | α_hub | Transmission multiplier for hubs | 1.5-3.0 | dimensionless | Estimated from centrality |

**Parameter Correlations**:
- β₀ and γ are inversely correlated (R₀ = β₀/γ drives dynamics)
- w_ij and α_hub interact multiplicatively: β_ij = β₀·w_ij·(1 + α_hub·h_i)
  where h_i is hub score (betweenness centrality)

**Prior Information**:
- β₀ prior: Gamma(shape=4, rate=8) centered at 0.5, allows 0.2-0.8 with 95% probability
- γ prior: Gamma(shape=2, rate=10) centered at 0.2 (5-day infectious period)
```

**Why This Works**:
- ✅ Complete table documents every parameter
- ✅ Physical ranges constrain values (prevent nonsense)
- ✅ Estimation method clarifies what's measured vs. fitted
- ✅ Correlations noted (affects identifiability)
- ✅ Priors specified (for Bayesian inference)

#### ❌ Anti-Pattern 3: Undefined or Ambiguous Parameters

**Bad Example**:
```
β = transmission rate (fitted)
γ = recovery rate (from literature)
```

**Why This Fails**:
- ❌ No units specified
- ❌ No typical range
- ❌ "From literature" - which paper? What value?
- ❌ Can't reproduce or validate

---

#### ✅ Pattern 4: Derivation from First Principles

**O Award Example** (2401298 - showing how network term arises):
```
## 3.4 Derivation of Network Transmission Term

We derive the network extension from first principles:

**Step 1**: Consider city i with population N_i and infected count I_i

**Step 2**: An individual in city i makes contact with:
- Local individuals: at rate c_local = β₀·N_i (mass action)
- Travelers from city j: at rate c_travel,j ∝ w_ji·I_j/N_j (proportional to traffic and prevalence)

**Step 3**: Total force of infection on city i:
λ_i = β₀·I_i/N_i  +  Σ_j β₀·w_ji·I_j/(N_j·N_i)
      [local term]     [imported infections]

**Step 4**: For computational efficiency, absorb N_i into β_ij:
β_ij = β₀·w_ij/N_j

giving the final form:
dS_i/dt = -S_i·[β₀·I_i/N_i + Σ_{j≠i} β_ij·I_j]
         = -S_i·Σ_j β_ij·I_j    (with β_ii = β₀/N_i)

**Physical Interpretation**:
- β_ii (local transmission) scales as 1/N_i because larger cities dilute contact rates
- β_ij (imported transmission) scales as w_ij because traffic volume matters
- Ratio w_ij/N_j represents "infection import per capita in destination"
```

**Why This Works**:
- ✅ Stepwise derivation (judges can follow)
- ✅ Physical reasoning at each step
- ✅ Final form connected to derivation
- ✅ Shows mastery of modeling (not just plugging formulas)

#### ❌ Anti-Pattern 4: "Trust Me" Mathematics

**Bad Example**:
```
After mathematical derivation (details omitted), we obtain:
dS_i/dt = -S_i Σ_j β_ij I_j
```

**Why This Fails**:
- ❌ "Details omitted" = judges assume you don't understand
- ❌ Can't verify correctness
- ❌ Misses opportunity to show insight

---

### Your O Award Checklist (Review Before Submission)

**Notation & Clarity**:
- [ ] All variables defined before use?
- [ ] Equations numbered consistently (1a, 1b, 2a...)?
- [ ] Units specified for every parameter?
- [ ] Notation is standard (not idiosyncratic)?

**Mathematical Rigor**:
- [ ] Key equations derived from first principles?
- [ ] Derivation steps shown (not "obvious" or "details omitted")?
- [ ] Assumptions listed with 4-part structure (Statement, Justification, Validity, Limitation)?
- [ ] Parameter table includes: symbol, meaning, range, units, estimation method?

**Physical Insight**:
- [ ] Every parameter has physical interpretation?
- [ ] Physical ranges constrain parameter space?
- [ ] Model predictions testable against domain knowledge?
- [ ] Limiting cases checked (what happens when β→0, N→∞, etc.)?

**Complexity Justification**:
- [ ] Started with simplest model, then justified extensions?
- [ ] Each complexity increase explained (why needed)?
- [ ] Complexity matches data richness (not overfit)?
- [ ] Computational cost estimated?
