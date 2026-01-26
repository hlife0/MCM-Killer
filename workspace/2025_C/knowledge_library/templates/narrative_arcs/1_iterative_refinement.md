# Narrative Template: Iterative Refinement (formerly Hero's Journey)

> **Best For**: Models that evolved through specific technical limitations
> **Logical Arc**: Baseline Model → Limitation Observed → Mechanism Identified → Refinement Implemented
> **O-Prize Value**: Very High (shows rigorous abduction)

---

## When to Use

Use the Iterative Refinement template when:
- The initial model failed or performed sub-optimally
- You can pinpoint specific technical reasons for the failure
- The "failure" revealed a domain insight
- You want to demonstrate the scientific method in action

## ⚠️ STYLE WARNING: Academic Objectivity

**The "Struggle" is Intellectual, not Emotional.**

- **DO NOT** use emotional language ("We were lost...", "In a stroke of genius...").
- **DO NOT** dramatize trivial bugs.
- **DO** focus on the **Technical Limitation**: "The linear assumption failed to capture saturation effects..."
- **DO** maintain Academic Solemnity: Objective, precise, and professional.

---

## The Four Stages

### Stage 1: The Baseline (Initial Model)

**Purpose**: Establish the starting point and its rationale.

**Template**:
```markdown
We began with [Model Description], a [methodology type] approach that
assumes [Key Assumption 1] and [Key Assumption 2].

**Rationale**:
1. [Theoretical justification]
2. [Practical consideration]
3. [Literature support]

**Specification**:
[Mathematical formulation]
```

---

### Stage 2: The Limitation (Observed Symptom)

**Purpose**: objective identification of where the baseline failed.

**Template**:
```markdown
However, [Specific Limitation] emerged during validation.

**Objective Evidence**:
- [Metric 1]: [Value] (threshold: [Expected])
- [Error/Symptom]: [Description]

**Diagnosis**:
Initial investigation ruled out [Hypothesis A] and [Hypothesis B], pointing to
[Fundamental Issue] as the root cause.
```

---

### Stage 3: The Implication (Mechanism Insight)

**Purpose**: The technical insight derived from the limitation.

**Template**:
```markdown
The [Symptom] indicated a fundamental mismatch in [Domain Principle].

**Abductive Analysis**:
- **Observation**: [What was seen]
- **Implication**: [What it means for the system mechanics]
- **Validation**: [Evidence]

**Key Insight**:
> "[One-sentence summary of the technical discovery]"
```

---

### Stage 4: The Revision (Refined Model)

**Purpose**: The solution derived from the insight.

**Template**:
```markdown
Informed by this insight, we refined the model to [Improved Approach].

**Specific Changes**:
| Component | Baseline | Revised | Rationale |
|-----------|----------|---------|-----------|
| [Part 1]  | [Old]    | [New]   | [Why]     |
| [Part 2]  | [Old]    | [New]   | [Why]     |

**Result**:
- [Convergence metric]: [Improved value]
- [Performance metric]: [Improved value]
```

---

## Complete Template Example

```markdown
# Model Evolution: [Model Name]

## 1. Baseline Approach
We began with a standard SIR model assuming homogeneous mixing.
**Rationale**: Simplicity and standard epidemiological practice.

## 2. Observed Limitation
However, R-hat divergence (1.37) in Asia-Pacific regions persisted.
**Diagnosis**: Global parameter sharing failed to account for regional heterogeneity.

## 3. Mechanism Insight
The divergence revealed that transmission dynamics are qualitatively different based on cultural factors.
**Key Insight**: "One-size-fits-all epidemic models fail when transmission mechanisms differ qualitatively between subgroups."

## 4. Refined Model
We refined to a Hierarchical Bayesian SIR.
**Changes**:
- **Structure**: Flat -> Hierarchical (Global -> Cluster -> Region)
- **Priors**: Fixed -> Adaptive
**Result**: R-hat < 1.02, RMSE reduced by 27%.
```
