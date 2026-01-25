# Narrative Template: Hero's Journey

> **Best For**: Models that failed initially, then evolved
> **Dramatic Arc**: Struggle → Revelation → Triumph
> **O-Prize Value**: Very High (shows metacognition)

---

## When to Use

Use the Hero's Journey when:
- Training initially failed (gradient explosion, divergence, NaN)
- Model required significant modification
- A major insight emerged from the struggle
- The "failure" revealed something important about the problem

---

## The Five Steps

### Step 1: The Call (Initial Approach)

**Purpose**: Establish the starting point

**Template**:
```markdown
We began with [Model Description], a [methodology type] approach that
assumes [Key Assumption 1] and [Key Assumption 2].

**Rationale**: This approach was chosen because:
1. [Reason 1 - theoretical justification]
2. [Reason 2 - practical consideration]
3. [Reason 3 - literature support]

The model specification is:
[Mathematical formulation]
```

**Example**:
```markdown
We began with a standard SIR compartmental model, assuming homogeneous
mixing and time-invariant transmission rates.

**Rationale**: This approach was chosen because:
1. SIR models are theoretically grounded in epidemiological literature
2. Compartmental dynamics simplify parameter estimation
3. Similar approaches succeeded in 2019 Problem D

The model specification is:
dS/dt = -βSI/N
dI/dt = βSI/N - γI
dR/dt = γI
```

---

### Step 2: The Ordeal (The Struggle)

**Purpose**: Create tension, show honest difficulty

**Template**:
```markdown
However, [Specific Problem] emerged during [Phase/Stage].

**Objective Evidence**:
- [Metric 1]: [Value] (threshold: [Expected])
- [Metric 2]: [Value] (threshold: [Expected])
- [Log excerpt or error message]

**Subjective Experience** (from development diary):
> "[Quote from @code_translator's dev_diary]"

This [symptom] was not immediately understood. Initial hypotheses included:
1. [Hypothesis A] - ruled out because [reason]
2. [Hypothesis B] - ruled out because [reason]
3. [Hypothesis C] - warranted further investigation
```

**Example**:
```markdown
However, R-hat divergence emerged during Bayesian inference.

**Objective Evidence**:
- R-hat (regions 5-8): 1.37 (threshold: <1.05)
- Effective sample size: 127 (minimum: 400)
- Error: "Chains have not mixed. Consider reparameterization."

**Subjective Experience** (from development diary):
> "Increasing samples to 20,000 didn't help. The Asia-Pacific regions
> simply refuse to converge. Something fundamental is wrong."

This divergence was not immediately understood. Initial hypotheses included:
1. Numerical instability - ruled out (same behavior with different seeds)
2. Weak priors - ruled out (stronger priors made it worse)
3. Data heterogeneity - warranted further investigation
```

---

### Step 3: The Revelation (The Insight)

**Purpose**: The "aha!" moment - turn failure into discovery

**Template**:
```markdown
The [Technical Symptom] was not a bug—it revealed **[Physical Insight]**.

**Abductive Analysis**:
- **Observation**: [What we saw]
- **Hypothesis**: [Best explanation]
- **Validation**: [Evidence supporting this explanation]

**Domain Mechanism**:
This indicates that [Domain Principle] is at play. Specifically:
- [Mechanism 1]: [Explanation]
- [Mechanism 2]: [Explanation]

**The Key Insight**:
> "[One-sentence summary of what the struggle revealed]"
```

**Example**:
```markdown
The R-hat divergence was not a numerical artifact—it revealed
**fundamental regional heterogeneity** in transmission dynamics.

**Abductive Analysis**:
- **Observation**: Only Asia-Pacific regions (5-8) diverged
- **Hypothesis**: These regions have qualitatively different dynamics
- **Validation**: Cultural factors (mask norms) and economic factors
  (healthcare access) differ systematically from other regions

**Domain Mechanism**:
This indicates that global pooling assumptions are violated. Specifically:
- **Cultural**: Collectivist societies show higher compliance
- **Economic**: Healthcare access affects recovery rates
- **Reporting**: Data collection methodologies vary by region

**The Key Insight**:
> "One-size-fits-all epidemic models fail when transmission mechanisms
> differ qualitatively between population subgroups."
```

---

### Step 4: The Resolution (The Evolution)

**Purpose**: Show how insight drove model improvement

**Template**:
```markdown
Informed by this insight, we refined the model to [Improved Approach].

**Specific Changes**:
| Component | Before | After | Rationale |
|-----------|--------|-------|-----------|
| [Component 1] | [Old] | [New] | [Why changed] |
| [Component 2] | [Old] | [New] | [Why changed] |

**Mathematical Formulation**:
[Updated equations]

**Result**:
- [Convergence metric]: [Improved value] (was: [old value])
- [Performance metric]: [Improved value] (↓X% from baseline)
- Training completed in [time]
```

**Example**:
```markdown
Informed by this insight, we refined the model to a two-cluster
hierarchical specification.

**Specific Changes**:
| Component | Before | After | Rationale |
|-----------|--------|-------|-----------|
| β prior | Single global | Two-cluster hierarchy | Respect heterogeneity |
| Pooling | Full | Partial (within cluster) | Allow regional variation |
| Structure | Flat | Nested (global → cluster → region) | Match data structure |

**Mathematical Formulation**:
β_developed ~ Normal(μ_dev, σ_dev)
β_developing ~ Normal(μ_developing, σ_developing)
μ_dev, μ_developing ~ Normal(μ_global, σ_global)

**Result**:
- R-hat (all regions): <1.02 (was: 1.37 for regions 5-8)
- RMSE: 4.2 (↓27% from baseline 5.8)
- Training completed in 2.3 hours
```

---

### Step 5: The Treasure (The Research Value)

**Purpose**: Extract lasting value from the journey

**Template**:
```markdown
### Methodological Insight
This evolution demonstrates that [Modeling Principle].

[Paragraph explaining the generalizable lesson]

### Domain Insight
[What does this reveal about the problem domain?]

[Paragraph with domain-specific implications]

### Policy/Theoretical Implication
[What should be done based on this finding?]

**Recommendation**: [Specific actionable recommendation]

**Expected Impact**: [Quantified benefit if applicable]

### Narrative Hook for Abstract
> "[One-sentence summary for the paper's opening]"
```

**Example**:
```markdown
### Methodological Insight
This evolution demonstrates that hierarchical models must respect
natural data structure—forcing global pooling when subgroups are
qualitatively distinct introduces systematic bias.

The shrinkage factor (κ = 0.73) quantifies the optimal balance:
borrow 73% of information across regions while preserving 27% of
regional specificity.

### Domain Insight
Host country effects on epidemic transmission vary systematically
by economic development level:
- **Developed**: Lower β (social distancing norms), higher γ (healthcare)
- **Developing**: Higher β (density), lower γ (resource constraints)

### Policy/Theoretical Implication
**Recommendation**: Deploy region-tailored intervention strategies:
- Developed regions: Focus on vaccine distribution (distancing already effective)
- Developing regions: Prioritize healthcare capacity + travel restrictions

**Expected Impact**: Targeted policies could reduce global mortality by
34% compared to uniform interventions (see Sensitivity Analysis).

### Narrative Hook for Abstract
> "Our region-specific hierarchical model reveals that assuming
> homogeneous transmission across culturally diverse regions introduces
> systematic bias—a finding with critical implications for global
> pandemic response policy."
```

---

## Complete Template

```markdown
# Model Evolution: [Model Name]

## 1. The Call
We began with [approach], assuming [assumptions].
[Rationale for choice]

## 2. The Ordeal
However, [problem] emerged.
**Evidence**: [metrics]
**Initial hypotheses**: [list]

## 3. The Revelation
The [symptom] revealed **[insight]**.
**Mechanism**: [explanation]
**Key insight**: "[summary]"

## 4. The Resolution
We refined to [improved approach].
**Changes**: [table]
**Result**: [improved metrics]

## 5. The Treasure
**Methodological**: [generalizable lesson]
**Domain**: [problem-specific insight]
**Policy**: [recommendation + impact]
**Hook**: "[abstract sentence]"
```

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
