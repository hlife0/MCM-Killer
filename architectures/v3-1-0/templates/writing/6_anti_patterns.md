# ANTI_PATTERNS: The Kill List

> **Purpose**: Identify and eliminate fatal flaws before they kill your paper
> **Enforcement**: @judge_zero, @editor, @narrative_weaver
> **Philosophy**: "Good is the enemy of great."

---

## Overview

This document defines three levels of anti-patterns that must be detected and eliminated:

| Level | Severity | Impact | Response |
|-------|----------|--------|----------|
| **Level 1** | Fatal | Auto-reject | DEFCON 1 triggered |
| **Level 2** | Severe | Major point loss | Must fix before submission |
| **Level 3** | Minor | Polish issue | Fix if time permits |

---

## Level 1: Fatal Flaws (Auto-Reject)

These flaws trigger **immediate DEFCON 1** regardless of other scores.

### 1.1 Narrative Vacuum (叙事真空)

**Definition**: Abstract contains zero or insufficient quantitative metrics.

**Detection**:
```python
def check_narrative_vacuum(abstract: str) -> bool:
    numbers = re.findall(r'\d+\.?\d*%?', abstract)
    return len(numbers) < 3  # Fatal if fewer than 3 numbers
```

**Examples**:

❌ **Fatal**:
> "We develop a model to predict epidemic spread. Our approach
> considers multiple factors and produces accurate results."

✅ **Acceptable**:
> "Our model achieves RMSE = 4.2 (↓42% from baseline), R² = 0.89,
> and identifies 3 critical hub nodes."

**Fix**: Add at least 3 quantitative metrics to abstract.

---

### 1.2 Interpretation Gap (解释缺失)

**Definition**: Figures or tables lack Observation-Implication captions.

**Detection**:
- Captions use only descriptive verbs: "shows", "displays", "presents"
- No implication verbs: "indicates", "reveals", "demonstrates", "suggests"

**Examples**:

❌ **Fatal**:
> "Figure 3 shows the model performance over time."

✅ **Acceptable**:
> "Figure 3 shows RMSE decreasing from 7.2 to 4.2 over training,
> indicating that network structure captures previously missed dynamics."

**Fix**: Add implication clause to every figure/table caption.

---

### 1.3 Visualization Silence (可视化沉默)

**Definition**: Paper contains zero figures.

**Detection**:
```python
def check_visualization_silence(paper: str) -> bool:
    figures = re.findall(r'\\begin\{figure\}', paper)
    return len(figures) == 0  # Fatal if no figures
```

**Minimum Requirements**:
- At least 2 data figures (results plots)
- At least 1 concept figure (model architecture)

**Fix**: Add figures immediately. Prioritize:
1. Main results comparison
2. Model architecture diagram
3. Sensitivity analysis heatmap

---

### 1.4 Sensitivity Blindness (敏感性盲区)

**Definition**: No sensitivity analysis section.

**Detection**:
- Section 5.2 or equivalent missing
- No parameter sweep results
- No robustness discussion

**Requirements**:
- Vary at least 3 key parameters
- Show impact on key metrics
- Discuss implications of sensitivity

**Fix**: Add sensitivity analysis section with parameter sweep.

---

### 1.5 Physical Impossibility (物理谬误)

**Definition**: Model predicts physically impossible values.

**Examples**:
- Negative population
- Probability > 100%
- Negative transmission rate
- Infinite values in predictions
- Cases exceeding population

**Detection**:
```python
def check_physical_impossibility(predictions: dict) -> list:
    violations = []
    if any(p < 0 for p in predictions.get('population', [])):
        violations.append("Negative population predicted")
    if any(p > 1 for p in predictions.get('probability', [])):
        violations.append("Probability exceeds 100%")
    return violations
```

**Fix**: Add constraints to model (positivity, bounds).

---

### 1.6 Uncertainty Blindness (不确定性盲区)

**Definition**: No confidence intervals on key predictions.

**Detection**:
- Point estimates only
- No CI, SE, or credible intervals reported
- No uncertainty visualization

**Requirements**:
- 95% CI on main predictions
- Error bars on key figures
- Uncertainty discussion in text

**Fix**: Add bootstrap CI or Bayesian credible intervals.

---

## Level 2: Severe Warnings

These flaws cause **major point loss** but don't auto-reject.

### 2.1 Baseline Absence (基线缺失)

**Definition**: No comparison to simpler baseline model.

**Why It Matters**: Can't show improvement without baseline.

**Fix**: Add Model A (simple baseline) vs Model B (your approach).

---

### 2.2 Assumption Opacity (假设不透明)

**Definition**: Model assumptions not explicitly stated.

**Why It Matters**: Judges can't evaluate appropriateness.

**Fix**: Add numbered list of assumptions in Section 3.1.

---

### 2.3 Validation Weakness (验证薄弱)

**Definition**: No train/test split or cross-validation.

**Why It Matters**: Results may be overfit.

**Fix**: Add temporal or spatial holdout validation.

---

### 2.4 Policy Disconnect (政策断联)

**Definition**: Results not translated to actionable recommendations.

**Why It Matters**: MCM values real-world applicability.

**Fix**: Add policy implications section with specific recommendations.

---

### 2.5 Narrative Fragmentation (叙事碎片化)

**Definition**: Sections don't connect into coherent story.

**Why It Matters**: Paper reads as disconnected reports.

**Fix**: Add transition sentences, use narrative template structure.

---

### 2.6 Method Mediocrity (方法平庸)

**Definition**: Using only banned methods without justification.

**Examples**:
- Basic SIR without network (epidemic problems)
- ARIMA alone (time series)
- Linear regression only (any problem)

**Fix**: Upgrade to O-Prize level methods per @knowledge_librarian.

---

## Level 3: Minor Issues

These are **polish issues** to fix if time permits.

### 3.1 Passive Voice Overuse

**Threshold**: >30% of sentences in passive voice.

**Fix**: Convert to active voice where appropriate.

---

### 3.2 Jargon Without Definition

**Definition**: Technical terms used without explanation.

**Fix**: Define on first use or add glossary.

---

### 3.3 Inconsistent Notation

**Definition**: Same variable means different things.

**Fix**: Create notation table, use consistent symbols.

---

### 3.4 Orphaned References

**Definition**: Citations in text but not in bibliography (or vice versa).

**Fix**: Synchronize references.

---

### 3.5 Figure Quality Issues

**Definition**: Low resolution, missing labels, unclear legends.

**Fix**: Regenerate at 300 DPI, add proper labels.

---

### 3.6 Length Imbalance

**Definition**: Sections significantly disproportionate.

**Guidelines**:
- Introduction: 10-15% of paper
- Methods: 30-40% of paper
- Results: 25-35% of paper
- Discussion: 15-20% of paper

**Fix**: Redistribute content or summarize verbose sections.

---

## Detection Protocol

### Automated Checks (via mmbench_score.py)

| Flaw | Check Method | Threshold |
|------|--------------|-----------|
| Narrative Vacuum | Count numbers in abstract | < 3 = FAIL |
| Interpretation Gap | Search caption verbs | Missing "indicates" etc. = FAIL |
| Visualization Silence | Count figures | 0 = FAIL |
| Sensitivity Blindness | Search section headers | Missing 5.2 = FAIL |
| Uncertainty Blindness | Search for "CI", "±", "interval" | 0 occurrences = FAIL |

### Manual Checks (by @judge_zero)

| Flaw | Check Method |
|------|--------------|
| Physical Impossibility | Review all predictions for domain validity |
| Baseline Absence | Verify Model A vs B comparison exists |
| Policy Disconnect | Check Section 5.3 for recommendations |

---

## Response Matrix

| Flaw Level | Time > 12h | Time 6-12h | Time < 6h |
|------------|------------|------------|-----------|
| Level 1 | DEFCON 1 | DEFCON 1 | DEFCON 1 (expedited) |
| Level 2 | Must fix | Fix top 3 | Fix top 1 |
| Level 3 | Fix all | Fix critical | Skip |

---

## DEFCON 1 Trigger Sequence

When any Level 1 flaw is detected:

1. @judge_zero issues **REJECT** decision
2. @director receives `judgment_report.md` with fatal flaw identified
3. @director enters **Protocol 13** (DEFCON 1 mode)
4. Repair tickets created for specific agents
5. Time-boxed repair cycle begins
6. Re-review after repairs
7. Maximum 3 cycles (Mercy Rule activates after)

---

## Prevention Strategies

### Phase-Specific Prevention

| Phase | Flaw to Prevent | Prevention Action |
|-------|-----------------|-------------------|
| Phase 0.2 | Method Mediocrity | @knowledge_librarian review |
| Phase 3 | Assumption Opacity | @modeler documents assumptions |
| Phase 5B | Physical Impossibility | @validator constraint checks |
| Phase 7 | Interpretation Gap | @narrative_weaver enforces Protocol 15 |
| Phase 8 | Narrative Vacuum | @editor abstract review |
| Phase 9.1 | All Level 1 | @judge_zero comprehensive review |

### Agent-Specific Responsibilities

| Agent | Prevents |
|-------|----------|
| @knowledge_librarian | Method Mediocrity |
| @narrative_weaver | Interpretation Gap, Narrative Fragmentation |
| @writer | Narrative Vacuum, Passive Voice |
| @visualizer | Visualization Silence, Figure Quality |
| @validator | Physical Impossibility, Uncertainty Blindness |
| @editor | All Level 3 issues |

---

## Version History

- **v1.0** (2026-01-25): Initial specification from m-orientation Sprint 1
