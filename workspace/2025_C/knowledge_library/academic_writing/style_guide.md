# O-Prize Style Guide (Auto-Generated)

> **Generated**: 2026-01-27 05:48
> **Source**: 44 reference papers
> **Version**: 1.0

---

## Purpose

This style guide captures the linguistic patterns and structural conventions
observed in O-Prize winning papers. All writing agents (@writer, @editor,
@narrative_weaver) MUST adhere to these guidelines.

---

## 1. Vocabulary Constraints

### 1.1 High-Value Academic Verbs (RECOMMENDED)

Use these verbs to elevate academic tone. Frequency per 10,000 words:

| Verb | Frequency | Usage |
|------|-----------|-------|
| **quantify** | 1.02 | "We quantify the effect of X on Y..." |
| **demonstrate** | 0.55 | "Our results demonstrate that..." |
| **validate** | 0.16 | "We validate our model using..." |
| **characterize** | 0.12 | "We characterize that..." |
| **synthesize** | 0.12 | "We synthesize that..." |
| **extrapolate** | 0.04 | "We extrapolate that..." |
| **posit** | 0.04 | "We posit that..." |
| **ascertain** | 0.04 | "We ascertain that..." |
| **corroborate** | 0.04 | "These findings corroborate previous..." |
| **illuminate** | 0.04 | "We illuminate that..." |

### 1.2 Medium-Value Verbs (ACCEPTABLE)

| Verb | Frequency |
|------|-----------|
| determine | 4.64 |
| analyze | 4.56 |
| evaluate | 2.56 |
| identify | 2.32 |
| establish | 1.97 |
| indicate | 1.61 |
| compare | 1.38 |
| assess | 1.26 |
| suggest | 1.22 |
| observe | 1.14 |

### 1.3 Weak Verbs (AVOID)

Replace these with stronger alternatives:

| Weak Verb | Replacement |
|-----------|-------------|
| show (3.66/10k) | demonstrate, reveal, illustrate |
| get (4.88/10k) | obtain, acquire, achieve |
| do (4.29/10k) | perform, execute, conduct |
| make (7.59/10k) | construct, generate, produce |
| use (16.68/10k) | employ, utilize, leverage |
| have (20.89/10k) | possess, exhibit, contain |
| be (40.52/10k) | constitute, represent, serve as |
| find (6.33/10k) | identify, discover, determine |
| see (2.48/10k) | observe, perceive, note |

### 1.4 Academic Connectors

Use these to strengthen logical flow:

| Connector | Frequency | Usage |
|-----------|-----------|-------|
| therefore | 13.89 | Logical consequence |
| however | 6.96 | Contrast with previous statement |
| thus | 6.81 | Summarize logical conclusion |
| moreover | 1.77 | Emphasize additional evidence |
| specifically | 1.69 | Logical transition |
| hence | 1.57 | Direct causal relationship |
| furthermore | 1.53 | Additional supporting point |
| accordingly | 0.9 | Logical transition |
| thereby | 0.67 | Means by which result achieved |
| conversely | 0.51 | Logical transition |

---

## 2. Abstract Requirements

### 2.1 Quantitative Content (MANDATORY)

- **79.5%** of reference abstracts contain numerical results
- Average of **4.7** numerical values per abstract

**RULE**: Abstract MUST contain **≥3 quantitative metrics**

Examples of required metrics:
- Performance: RMSE, R², accuracy, F1-score
- Comparison: "↓27% from baseline", "3x improvement"
- Significance: p-values, confidence intervals

### 2.2 Structure Template

```
[1-2 sentences: Problem importance and gap]
[1 sentence: Our approach and key innovation]
[1-2 sentences: Main results with NUMBERS]
[1 sentence: Broader implication or policy insight]
```

### 2.3 Examples

**GOOD** (contains 5 numbers):
> We develop a hierarchical SIR-network model that achieves **RMSE = 4.2**
> (↓27% from baseline), **R² = 0.89** (p < 0.001), and identifies **3 critical
> hub nodes** for targeted intervention, potentially reducing spread by **34%**.

**BAD** (contains 0 numbers):
> We develop a novel model to predict epidemic spread. Our approach
> incorporates network structure and performs well on test data.

---

## 3. Sentence Patterns

### 3.1 Observation-Implication Pattern (Protocol 15)

Every data statement MUST follow the Observation-Implication structure:

```
[OBSERVATION: What the data shows]
    +
[IMPLICATION: What this means physically/economically]
```

**Templates**:

1. "This indicates that the gaming ability of the
enthusiastic fans is also slowly improving, and it also shows that this ga..." (2 occurrences)

2. "And
the value of [X]indicates "very unsatisfied" while the value of [X]indicating "very satisfied"" (1 occurrences)

3. "wCase [X]and [X]shows multiple peaks and valleys, indicating that the
valueof𝑁 istakentoosmall" (1 occurrences)

4. "Moreover, when the price fluctuates greatly near [X], the model does not
have a large tracking error, indicating that th..." (1 occurrences)

5. "This indicates that our
strategy is more stable overall and has a better advantage compared to a single indicator" (1 occurrences)

### 3.2 Figure Reference Patterns

- "Team#[N] Page[N]of[N]
Figure [N] and Figure [N] shows that the predicted price curve coincides with th"
- "• Volatilityofthenumberofreportedresults
As Figure [N] shown before, the difference between the daily "
- "Figure [N] shows
thecorrelationofeachfeaturewithworddifficulty"

### 3.3 Comparison Patterns

- ">([X]-star rating): This dryer is not quiet but
the noise is so much more tolerable compared to some d"
- "Since the output values cannot be directly used as percentages, as their sum may exceed or
belesstha"
- "⚫ The ARIMA-LSTM model can be used to forecast the future trend of stock prices simply
国
by using th"

---

## 4. Figure Caption Standards

Reference paper statistics:
- **2.8%** of captions are conclusionary (not just descriptive)
- **62.8%** of captions contain numerical findings

### 4.1 Caption Requirements

**MANDATORY**: Every caption must:
1. State a finding (not just label the figure)
2. Include at least one number or quantitative comparison
3. Connect to the physical/domain meaning

### 4.2 Examples

**BAD** (descriptive only):
> "Weobservethatbabypacifiers
have received the highest percentage of high star rating, while microwaves a lower star rating."
> "Starratingdistributionofpacifier,microwaveandhairdryerbasedonthegivendata."

**GOOD** (conclusionary with numbers):
> "Varietyofprofitonlastdaywithrespecttoradioofbuyinggold(𝛿%)
w
The figure shows that the final return is maximum for 𝛿 = 2."
> "shows that the p-values of the residual test of the models at different times are all
greater than 0."

---

## 5. Writing Constraints

### 5.1 Banned Phrases

| Banned | Replacement |
|--------|-------------|
| "We used X" | "We employed X to achieve Y" |
| "The results are good" | "The results demonstrate [specific improvement]" |
| "Our model works" | "Our model achieves RMSE=X (↓Y% from baseline)" |
| "Clearly shows" | "Demonstrates (p<0.05)" |
| "Very significant" | "Statistically significant (p<0.001)" |

### 5.2 Tense Guidelines

| Section | Tense | Example |
|---------|-------|---------|
| Abstract | Present/Past | "We develop... achieves..." |
| Introduction | Present | "This problem affects..." |
| Methods | Past | "We employed... constructed..." |
| Results | Past | "The model achieved... Figure 2 showed..." |
| Discussion | Present | "These findings suggest... This implies..." |

### 5.3 Uncertainty Language

Always acknowledge uncertainty appropriately:

| Certainty Level | Language |
|-----------------|----------|
| Strong evidence | "demonstrates", "confirms", "establishes" |
| Moderate evidence | "suggests", "indicates", "implies" |
| Weak evidence | "may", "could", "potentially" |
| Speculation | "we hypothesize", "one possible explanation" |

---

## 6. Protocol 14: Academic Style Alignment

All writing agents MUST load this style guide and comply with:

1. **Vocabulary**: Use high-value verbs, avoid weak verbs
2. **Abstract**: ≥3 quantitative metrics required
3. **Sentences**: Follow Observation-Implication pattern
4. **Captions**: Conclusionary format with numbers
5. **Tone**: Academic and objective, avoid hyperbole

**Violation of these rules is equivalent to a syntax error.**

---

*Generated by style_analyzer.py on 2026-01-27*