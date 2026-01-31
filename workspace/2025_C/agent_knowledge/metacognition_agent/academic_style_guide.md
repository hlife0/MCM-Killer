# Academic Style Guide for Insights

> **Purpose**: Language patterns and anti-patterns for research insight documentation
> **Reference**: metacognition_agent.md Academic Style Constraints section

---

## Core Principle

Your insights will appear in the Discussion section of an academic paper. Language must be professional, precise, and impersonal.

---

## Forbidden Language Patterns

### Emotional/Dramatic Words

| ❌ Forbidden | ✅ Replace With |
|--------------|-----------------|
| "The ordeal" | "The technical challenge" |
| "The struggle" | "The implementation process" |
| "The revelation" | "The analysis revealed" |
| "The treasure" | "The key finding" |
| "Epiphany" | "This analysis suggested" |
| "Breakthrough" | "Methodological refinement" |
| "Disaster" | "Systematic discrepancy" |
| "Crisis" | "Convergence challenge" |
| "Miracle" | "Unexpected improvement" |
| "Nightmare" | "Persistent issue" |

### Emotional Framing

| ❌ Forbidden | ✅ Replace With |
|--------------|-----------------|
| "We battled the bug" | "Diagnostic analysis identified" |
| "We overcame the challenge" | "We addressed this by" |
| "We conquered the problem" | "The issue was resolved through" |
| "We finally solved" | "Investigation revealed that" |
| "After struggling for days" | "After systematic investigation" |
| "The eureka moment came" | "Analysis indicated that" |
| "We were thrilled to discover" | "Results demonstrated" |
| "Frustratingly, the model" | "The model exhibited" |

### Colloquial Language

| ❌ Forbidden | ✅ Replace With |
|--------------|-----------------|
| "The model went haywire" | "The model exhibited instability" |
| "Numbers were all over the place" | "Values showed high variance" |
| "It just worked" | "Convergence was achieved" |
| "We got lucky" | "The approach proved effective" |
| "Things fell into place" | "The methodology yielded consistent results" |

---

## Required Language Patterns

### Technical Challenge Description

```markdown
✅ GOOD:
"The model exhibited convergence challenges characterized by
R-hat values exceeding 1.3 for 40% of parameters."

❌ BAD:
"We struggled with the model for three days before it finally worked."
```

### Discovery/Finding

```markdown
✅ GOOD:
"Analysis revealed that regional heterogeneity accounts for
the observed parameter divergence."

❌ BAD:
"We discovered an amazing insight about regional differences."
```

### Solution/Resolution

```markdown
✅ GOOD:
"We addressed this by implementing a hierarchical structure
with regional random effects, reducing divergent parameters to 0%."

❌ BAD:
"We finally conquered the problem by adding regional effects."
```

### Insight/Implication

```markdown
✅ GOOD:
"This finding suggests that global pooling assumptions are
inappropriate for cross-national Olympic medal prediction."

❌ BAD:
"This was a huge revelation that changed everything about our model."
```

---

## Sentence Templates

### For Technical Challenges

```markdown
- "The model exhibited [specific symptom] characterized by [metric]."
- "Initial attempts resulted in [quantified outcome]."
- "Diagnostic analysis identified [root cause]."
- "The [component] showed [behavior] under [conditions]."
```

### For Methodological Refinements

```markdown
- "We addressed this by implementing [solution]."
- "This challenge was resolved through [approach]."
- "The issue was mitigated by [change], resulting in [improvement]."
- "Modification of [component] yielded [quantified improvement]."
```

### For Insights

```markdown
- "Analysis revealed that [finding]."
- "Investigation demonstrated that [relationship]."
- "Results indicated that [pattern]."
- "This finding suggests that [implication]."
- "The [observation] implies that [inference]."
```

### For Research Value

```markdown
- "This has implications for [domain/policy/methodology]."
- "These results contribute to understanding of [phenomenon]."
- "The finding informs [application/theory]."
- "Future work should consider [direction]."
```

---

## Complete Example Transformation

### ❌ Before (Emotional)

```markdown
After three days of struggling with the model, we finally had our
breakthrough moment! The culprit was regional heterogeneity - African
and European countries were fighting against each other in our global
model. Once we conquered this problem by splitting into regional models,
everything fell beautifully into place. We were thrilled to see R-hat
values drop from nightmare levels of 1.5+ down to perfect 1.01 scores.
This was truly a eureka moment that revealed the treasure hidden in
our data: you can't treat all countries the same way!
```

### ✅ After (Academic)

```markdown
Initial convergence diagnostics revealed elevated R-hat values (>1.3)
for 40% of country-level parameters, indicating potential model
misspecification. Systematic investigation of parameter trace plots
identified bimodal posterior distributions corresponding to
continental groupings. This convergence challenge reflected
substantive data heterogeneity: African and European nations exhibit
fundamentally different medal-GDP relationships (β_Africa = 0.32,
β_Europe = 0.71). We addressed this by implementing a hierarchical
model with continental random effects, achieving full convergence
(all R-hat < 1.01) and revealing interpretable between-region
variation (σ_region = 2.4, 95% CI: [1.8, 3.2]). This finding
suggests that global pooling assumptions are inappropriate for
cross-national Olympic prediction, with implications for how
international sports bodies benchmark national performance.
```

---

## Reference Paper Alignment

Emulate the style of winning MCM papers:

### 2009116.pdf Style Elements

1. **Transparent limitations**: Acknowledge challenges directly
2. **Structured presentation**: Use clear headings and bullets
3. **Balanced tone**: Professional confidence without arrogance
4. **Quantified claims**: Every statement backed by numbers
5. **Implication focus**: Connect findings to real-world meaning

### Example Limitation Statement

```markdown
✅ GOOD (2009116 style):
"A key limitation of our approach is the assumption of temporal
stationarity in the GDP-medal relationship. Evidence of structural
breaks around 1990 (post-Cold War) suggests this assumption may be
violated. However, subsample analysis indicates that post-1990 data
alone yields similar coefficient estimates (Δβ < 0.05), suggesting
our findings are robust to this concern for contemporary prediction."
```

---

## Quality Checklist

Before finalizing your output:

- [ ] No emotional/dramatic words used
- [ ] No first-person emotional statements ("we were thrilled")
- [ ] All findings quantified with specific numbers
- [ ] Technical terms used precisely
- [ ] Passive voice used appropriately for objectivity
- [ ] Every insight has "so what?" implication
- [ ] Language suitable for journal publication
- [ ] Consistent with reference paper style
