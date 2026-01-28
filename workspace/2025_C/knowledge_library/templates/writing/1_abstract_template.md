# Abstract Template for MCM Papers

## Purpose
This template provides structure and guidelines for writing effective MCM paper abstracts.

## Abstract Structure

### Length: 250-350 words
### Structure: Background → Methods → Results → Implications

---

## Template

### Paragraph 1: Problem Context (2-3 sentences)
- Briefly describe the problem domain
- State the core challenge or question
- Mention why this problem matters

**Example**: "Olympic medal prediction represents a complex stochastic system where individual athlete performances aggregate to country-level outcomes, emerging from structural factors including host advantage, coaching quality, and historical performance patterns."

### Paragraph 2: Methods Overview (1 sentence per model)
- Summarize your approach
- Name each model and its purpose
- Keep it concise (5 models = 5 sentences)

**Example**: "We employ a modular Bayesian approach where each model addresses a specific aspect: (1) a hurdle model capturing the threshold effect between non-medalists and medalists, (2) survival analysis predicting first-time medalist probabilities, (3) latent factor analysis quantifying country sport specializations, (4) Bayesian change-point detection identifying coach effects, and (5) a BSTS ensemble synthesizing predictions."

### Paragraph 3: Key Results with Specific Numbers (3-4 metrics)
- Present your most important findings
- Include specific quantitative metrics (numbers, percentages, intervals)
- Be precise and data-driven

**Example**: "The model predicts the United States will win 127.9 medals (95% PI: 77.8-178.1) in 2028, maintaining top position despite China's projected 83.7 medals (50.9-116.5). We identify 79 countries (51% of all NOCs) predicted to win exactly 2.0 medals, revealing a self-reinforcing medal floor that constrains small nations. Survival analysis estimates 3-5 countries will earn their first Olympic medal in 2028, with 12 nations exceeding 15% breakthrough probability."

### Paragraph 4: Implications and Conclusions (2-3 sentences)
- What do these results mean?
- What are the broader implications?
- What recommendations emerge?

**Example**: "Host advantage contributes only +1.5% medal increase for the United States, contradicting conventional wisdom. Our analysis reveals Olympic success follows distinct tiers requiring different optimization strategies, with middle-power nations offering the highest investment efficiency."

---

## Quality Checklist

### Content Requirements
- [ ] 250-350 words total
- [ ] 3-5 quantitative metrics (numbers, %, intervals)
- [ ] All models mentioned by name
- [ ] Specific numerical results included
- [ ] Clear implications stated

### Style Requirements
- [ ] Use active voice: "We develop", "We employ"
- [ ] Use strong verbs: "quantify", "demonstrate", "reveal"
- [ ] Avoid weak verbs: "use", "show", "make"
- [ ] Be precise: "127.9 medals (95% PI: 77.8-178.1)"
- [ ] Avoid vague statements: "significantly increases"

### Structure Requirements
- [ ] Paragraph 1: Problem context (2-3 sentences)
- [ ] Paragraph 2: Methods overview (1 sentence per model)
- [ ] Paragraph 3: Key results with numbers (3-4 metrics)
- [ ] Paragraph 4: Implications (2-3 sentences)

---

## Common Mistakes to Avoid

1. **Too long**: >400 words → Keep it 250-350 words
2. **Too vague**: "Our model works well" → "Our model achieves RMSE of 3.2"
3. **Missing numbers**: No quantitative metrics → Include 3-5 specific numbers
4. **Wrong structure**: Results before methods → Follow Background → Methods → Results → Implications
5. **Weak verbs**: "use", "show", "make" → Replace with "employ", "demonstrate", "construct"
6. **Repetition**: Same word in 3 consecutive sentences → Vary vocabulary
7. **No models**: Don't name your models → List each model by name

---

## Good vs. Bad Examples

### Bad Abstract
```
We created a model to predict Olympic medals. It uses statistics
and machine learning. Our results show that the US will win
many medals in 2028. China will also win a lot of medals.
The model is comprehensive and addresses all requirements well.
```

**Problems**:
- Too vague ("many medals", "a lot")
- No model names
- No quantitative metrics
- Weak verbs
- Wrong structure

### Good Abstract
```
We develop a hierarchical Bayesian framework to model Olympic
medal counts, quantifying uncertainty for 2028 Los Angeles
projections while addressing six analytical tasks. Our approach
combines five specialized models: (1) a hurdle model capturing
the threshold effect between non-medalists and medalists,
(2) survival analysis predicting first-time medalist probabilities,
(3) latent factor analysis quantifying country sport specializations,
(4) Bayesian change-point detection identifying "great coach" effects,
and (5) a BSTS ensemble synthesizing predictions. The model predicts
the United States will win 127.9 medals (95% PI: 77.8-178.1) in 2028,
maintaining top position despite China's projected 83.7 medals
(50.9-116.5). We identify 79 countries (51% of all NOCs) predicted
to win exactly 2.0 medals, revealing a self-reinforcing "medal floor"
that constrains small nations. Host advantage contributes only +1.5%
medal increase, contradicting conventional wisdom of 10-20% home-
nation advantages. Our analysis reveals Olympic success follows
distinct tiers requiring different optimization strategies.
```

**Strengths**:
- Specific numbers (127.9, 95% PI, 83.7, 51%)
- All models named
- Strong verbs (develop, combine, predict, identify, reveals)
- Correct structure (Background → Methods → Results → Implications)
- Appropriate length (280 words)

---

**Template Version**: 1.0
**Last Updated**: 2026-01-28
**Reference**: Based on analysis of 40+ O-Prize winning papers
