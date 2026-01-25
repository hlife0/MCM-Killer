# Template: Development Diary Entry

> **Purpose**: Document struggles for insight extraction
> **Written By**: @code_translator
> **Used By**: @metacognition_agent for narrative_arc.md

---

## File Location

```
output/docs/insights/dev_diary_{model_number}.md
```

---

## Header Template

```markdown
# Development Diary: Model {i}

> **Model**: {Model Name}
> **Phase**: {Phase 4/5A/5B}
> **Implementation Start**: {YYYY-MM-DD HH:MM}
> **Status**: [In Progress / Complete / Blocked]

---
```

---

## Entry Template

```markdown
## Entry {N}: {YYYY-MM-DD HH:MM}

### Context
[1-2 sentences: What was I trying to accomplish?]

### The Struggle
**Symptom**: [One sentence describing the problem]

**Error Message** (if applicable):
```
[Exact error text or log output]
```

**Metrics** (if applicable):
| Metric | Expected | Actual |
|--------|----------|--------|
| [Metric 1] | [Value] | [Value] |
| [Metric 2] | [Value] | [Value] |

### The Investigation
[What diagnostic steps were taken?]

- Tried: [Action 1]
  - Result: [What happened]
- Tried: [Action 2]
  - Result: [What happened]
- Tried: [Action 3]
  - Result: [What happened]

### The Fix
**Solution**: [One sentence describing the fix]

**Code Change**:
```python
# Before
[original code]

# After
[modified code]
```

**Configuration Change** (if applicable):
```yaml
# Before
parameter: old_value

# After
parameter: new_value
```

### The Why (My Hypothesis)
[2-3 sentences explaining why this happened]

**Physical Interpretation**:
[What does this reveal about the data/model/problem in domain terms?]

### Time Spent
| Phase | Duration |
|-------|----------|
| Diagnosis | {X} min |
| Fix | {Y} min |
| Verification | {Z} min |
| **Total** | {X+Y+Z} min |

### Flag for @metacognition_agent
[Yes/No] - [If yes, why is this significant for the paper narrative?]

---
```

---

## Struggle Categories

When documenting, classify the struggle:

| Category | Symptoms | Likely Physical Meaning |
|----------|----------|------------------------|
| **CONVERGENCE** | R-hat > 1.05, loss divergence, oscillation | Data heterogeneity, model misspecification |
| **NUMERICAL** | NaN, Inf, overflow, underflow | Scale mismatch, wrong functional form |
| **PERFORMANCE** | Too slow, OOM, timeout | Complexity exceeds resources |
| **LOGIC** | Wrong output, unexpected behavior | Assumption violation |
| **DATA** | Missing values, format errors, outliers | Real-world data messiness |
| **INTEGRATION** | API mismatch, dependency conflict | Technical debt |

---

## Example: Complete Entry

```markdown
## Entry 3: 2026-01-25 14:32

### Context
Training the SIR-Network model with Adam optimizer, initial learning
rate 0.01. Expected smooth convergence within 100 epochs.

### The Struggle
**Symptom**: Loss exploded to Inf at epoch 5, training crashed

**Error Message**:
```
RuntimeWarning: overflow encountered in exp
Epoch 5/100 - Loss: inf
Training terminated: non-finite loss detected
```

**Metrics**:
| Metric | Expected | Actual |
|--------|----------|--------|
| Loss @ epoch 5 | < 10 | inf |
| Gradient norm | < 100 | 1.2e38 |

### The Investigation
- Tried: Reducing learning rate to 0.001
  - Result: Still exploded, just delayed to epoch 12
- Tried: Gradient clipping (max_norm=1.0)
  - Result: Stabilized but loss oscillated wildly (±50%)
- Tried: Examining parameter values before explosion
  - Result: β grew to 15.7 (unrealistic for transmission rate)
- Tried: Log-transform on β parameter
  - Result: Stable training, loss converged smoothly

### The Fix
**Solution**: Applied log-transform to transmission rate β to ensure
positivity and stabilize optimization landscape

**Code Change**:
```python
# Before
self.beta = nn.Parameter(torch.tensor(0.5))
# Used directly: rate = self.beta * S * I / N

# After
self.log_beta = nn.Parameter(torch.tensor(-0.69))  # log(0.5)
self.beta = torch.exp(self.log_beta)  # Ensures β > 0
# Used: rate = self.beta * S * I / N
```

### The Why (My Hypothesis)
The gradient explosion occurred because β interacts multiplicatively
with S and I. When β is parameterized additively (raw value), the
optimizer can push it arbitrarily large, causing exponential growth
in the rate term. Log-transform makes the optimization landscape
more uniform—a 10% change in log_beta has proportional effect
regardless of the absolute value.

**Physical Interpretation**:
Transmission rates have multiplicative effects—doubling β doubles
the infection rate. The original parameterization ignored this
multiplicative structure. The fix respects the inherent multiplicative
nature of epidemic transmission.

### Time Spent
| Phase | Duration |
|-------|----------|
| Diagnosis | 25 min |
| Fix | 10 min |
| Verification | 15 min |
| **Total** | 50 min |

### Flag for @metacognition_agent
**Yes** - This reveals that epidemic parameters have multiplicative
structure. The gradient explosion is not just a numerical issue—it
reflects the underlying mathematical structure of the problem. This
could support a paragraph in Section 3.3 about respecting parameter
structure.
```

---

## Summary Section Template

At the end of the diary, include:

```markdown
---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Entries | {N} |
| Total Struggles | {M} |
| Time on Debugging | {X} hours |
| Most Common Category | {Category} |
| Entries Flagged for @metacognition | {K} |

---

## Key Insights for Paper Narrative

1. **Insight 1**: [Summary of major struggle and what it revealed]
2. **Insight 2**: [Summary of pattern across struggles]
3. **Insight 3**: [Key learning for methodology section]

---

## Recommended Narrative Hooks

Based on documented struggles, suggest:

1. > "[Quote for Section 3.2: The Challenge]"
2. > "[Quote for Section 3.3: Metacognitive Analysis]"
3. > "[Quote for Section 5.1: Limitations as Insights]"
```

---

## Quality Standards

### MUST Include
- Timestamp for every entry
- Specific error messages (copy-paste, don't paraphrase)
- Actual code changes (before/after)
- Hypothesis about physical meaning

### SHOULD Include
- Time spent breakdown
- Multiple investigation steps
- Flag for significant insights

### NICE TO HAVE
- Screenshots of plots showing the issue
- Links to relevant HMML method files
- References to similar issues in literature

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
