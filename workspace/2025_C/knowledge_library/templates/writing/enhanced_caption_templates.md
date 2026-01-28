# Enhanced Caption Templates for O-Prize Quality Papers

**Purpose**: Create complete, compelling captions that explain, interpret, and contextualize
**Usage**: Apply to all figures and tables
**Goal**: Every caption is a self-contained unit that tells a complete story

**Key Principle from Reference Paper Analysis**: Reference papers use a **3-sentence structure**:
1. What the figure shows (with specific numbers)
2. Key insight or pattern revealed
3. Implications or why it matters

**NOT** a rigid 4-element formula, but a natural flow from observation → insight → implication.

---

## Reference Paper Caption Examples (Actual Quotes)

### From 2425454.pdf (Urban Logistics):
> "Figure 3: Heat map of delivery density vs. environmental impact across 12 metropolitan areas. The sharp transition zone at 1.7 packages/km² represents the efficiency threshold beyond which marginal increases in density disproportionately increase emissions. This critical parameter enables city planners to design optimal delivery zones."

**Structure**:
- Sentence 1: What figure shows (12 metro areas, heat map)
- Sentence 2: Key insight (1.7 packages/km² threshold, disproportionate increase)
- Sentence 3: Implication (enables city planners to design zones)

### From 2002116.pdf (Network Resilience):
> "Figure 7: Comparison of predicted vs. actual cascade magnitudes using three different models. The tight clustering along the diagonal line indicates our method's superior accuracy, particularly in the high-magnitude failure range where precision matters most for infrastructure planning."

**Structure**:
- Sentence 1: What figure shows (3 models, predicted vs actual)
- Sentence 2: Key insight (tight clustering = superior accuracy, especially high-magnitude)
- Sentence 3: Why it matters (precision critical for infrastructure planning)

---

## Caption Template: 3-Sentence Structure

### Structure

```latex
\caption{[Sentence 1: What figure/table shows with specific numbers]. [Sentence 2: Key insight,
pattern, or relationship revealed]. [Sentence 3: Implication, why it matters, or what it enables].}
```

### Example 1: Quantitative Finding (Olympic)

```latex
\caption{Prediction interval width by country size tier, showing small nations face 99.3\%
relative uncertainty compared to 78.4\% for superpowers. This inverse relationship indicates
that prediction error scales with country size, challenging the intuition that larger
datasets should reduce relative uncertainty. Small NOCs must employ flexible funding models
rather than fixed medal targets.}
```

**Breakdown**:
- Sentence 1: What figure shows (99.3% vs 78.4%, small vs large nations)
- Sentence 2: Key insight (inverse relationship, challenges intuition about large datasets)
- Sentence 3: Implication (small NOCs need flexible funding)

### Example 2: Model Comparison

```latex
\caption{Comparison of predicted vs. actual medal counts using three different models.
Our hierarchical hurdle model achieves RMSE of 2.3 medals, outperforming the standard
Poisson model (RMSE: 4.7) and negative binomial model (RMSE: 3.9). This 51\% improvement
demonstrates that explicitly modeling the zero-inflation threshold is critical for
accurate predictions.}
```

**Breakdown**:
- Sentence 1: What figure shows (3 models, predicted vs actual)
- Sentence 2: Key insight (RMSE values, 51% improvement over Poisson)
- Sentence 3: Why it matters (modeling zero-inflation threshold is critical)

### Example 1: Quantitative Finding

```latex
\caption{Prediction interval width by country size tier, showing small nations face 99.3\%
relative uncertainty compared to 78.4\% for superpowers. This inverse relationship indicates
that prediction error scales with country size, challenging the intuition that larger
datasets should reduce relative uncertainty. Small NOCs must employ flexible funding models
with tiered commitments rather than fixed medal targets. Key number: 99.3\% CI width for
2.5-medal countries vs. 78.4\% for 38.2-medal countries.}
```

### Example 2: Model Comparison

```latex
\caption{Comparison of predicted vs. actual medal counts using three different models.
Our hierarchical hurdle model achieves RMSE of 2.3 medals, outperforming the standard
Poisson model (RMSE: 4.7) and negative binomial model (RMSE: 3.9). This 51\% improvement
over Poisson demonstrates that explicitly modeling the zero-inflation threshold is critical
for accurate predictions. Key number: 51\% RMSE reduction from baseline.}
```

### Example 3: Pattern Discovery

```latex
\caption{Revealed Comparative Advantage (RCA) heatmap displaying sport specialization patterns.
China shows extreme concentration in diving (RCA = 4.2), table tennis (RCA = 3.8), and
badminton (RCA = 3.5), while Kenya dominates distance running (RCA = 5.6). This
specialization pattern contradicts the expectation that large nations should compete
across all sports, suggesting that targeted investment in specific disciplines yields
higher returns than broad participation. Key number: China's 4.2 RCA in diving indicates
4.2x higher medal rate than global average.}
```

### Example 4: Temporal Dynamics

```latex
\caption{Time series decomposition of medal counts for representative countries, displaying
trend, seasonal, and residual components. The trend component explains 67\% of variance
for emerging powers but only 23\% for established powers, indicating that growth trajectories
dominate performance for developing nations while cyclical effects prevail for superpowers.
This challenges the assumption that all countries follow similar temporal patterns. Key
number: 67\% trend variance for emerging nations vs. 23\% for superpowers.}
```

---

## Caption Templates by Figure Type

### Template A: Bar Chart / Histogram

```latex
\caption{[Y-axis variable] by [X-axis categories], showing [key pattern with numbers].
This [relationship/trend] indicates that [interpretation]. The [surprising element/contrast]
suggests [takeaway for decision-making]. Key number: [most important metric].}
```

**Example**:
```latex
\caption{Medal count distribution by country tier, showing 79 countries (51\% of NOCs)
clustered at the 2.0-medal floor. This extreme concentration indicates that the model
cannot distinguish between half of all nations, assigning them identical conservative
predictions. The artificial nature of this ceiling suggests that targeted bronze
conversion strategies could help small nations break through. Key number: 51\% of
countries stuck at 2.0-medal prediction.}
```

### Template B: Line Chart / Time Series

```latex
\caption{[Y-axis variable] over [time period/condition], demonstrating [trend with numbers].
The [pattern/change] reveals [mechanism/relationship]. This [challenges expectation/
confirms hypothesis], indicating [implication]. Key number: [critical rate/change].}
```

**Example**:
```latex
\caption{Host nation medal counts over 8 Olympic Games (1988--2020), demonstrating
diminishing home-nation advantage from +12.5\% in 1988 to +3.2\% in 2020. The
negative trend (slope: -0.4\% per Olympics) reveals that globalization of coaching
and reduced travel barriers have eroded traditional home-field benefits. This contradicts
the persistence of 10--20\% host advantages cited in literature, suggesting that
historical advantage estimates may not apply to modern Games. Key number: 74\% reduction
in host advantage since 1988.}
```

### Template C: Scatter Plot

```latex
\caption{[Y-axis] vs. [X-axis], showing [relationship type with correlation coefficient].
The [positive/negative] correlation (r = [value]) indicates that [interpretation].
[Surprising pattern/outliers] suggest [mechanism/implication]. Key number: [r-value
or effect size].}
```

**Example**:
```latex
\caption{Investment (\$ millions) vs. medal gain (2016--2024), showing strong positive
correlation (r = 0.73) for middle-power nations but weak correlation (r = 0.12) for
superpowers. The divergent slopes indicate diminishing returns on investment for
already-successful nations, challenging the assumption that funding linearly translates
to medals. This suggests that NOCs should target middle-power countries for investment
efficiency. Key number: 6.1x higher ROI for middle-powers vs. superpowers.}
```

### Template D: Heat Map

```latex
\caption{Heat map of [metric] across [dimensions], revealing [pattern with specific values].
The [clustering/gradient] indicates [relationship/structure]. [Unexpected regions/
values] suggest [insight about underlying mechanism]. Key number: [highest/lowest value].}
```

**Example**:
```latex
\caption{Coach effect magnitude heatmap across 200 country-sport pairs, revealing 18
documented regime changes with effect sizes ranging from +1.8 to +8.2 medals. The
concentration of high-impact changes in specific sports (volleyball, gymnastics, swimming)
indicates that coaching expertise transfers more effectively in technique-intensive
disciplines. The sparsity of detectable changes (18 out of 10,000 pairs) suggests that
"great coach" effects are rare but highly impactful when they occur. Key number: +8.2
medal effect from Lang Ping's China volleyball tenure.}
```

### Template E: Multi-Panel Figure

```latex
\caption{Multi-panel comparison of [aspect across panels]: (Panel A) [description with key
number], (Panel B) [description with key number], (Panel C) [description with key number].
Together, these panels demonstrate [integrated insight]. The [contrast/consistency] across
panels reveals [broader pattern/mechanism]. Key number: [most critical metric].}
```

**Example**:
```latex
\caption{Model performance comparison across five validation metrics: (Panel A) RMSE by
country size (hurdle model: 2.3 vs. Poisson: 4.7), (Panel B) Prediction interval
coverage (95\% intervals contain 92\% of actual outcomes), (Panel C) Calibration plots
(observed vs. predicted quantiles), (Panel D) Residual diagnostics, (Panel E) Time-based
validation (2016--2024 performance). Together, these panels demonstrate that the hurdle
structure successfully captures the threshold-governed nature of Olympic success while
maintaining well-calibrated uncertainty estimates. Key number: 51\% RMSE reduction from
Poisson baseline.}
```

---

## Table Caption Templates

### Template F: Results Table

```latex
\caption{[Table description] for [entities compared]. [Key finding with numbers]. This
[relationship/pattern] indicates [interpretation]. [Unexpected element/ranking] suggests
[takeaway]. Key number: [most important metric].}
```

**Example**:
```latex
\caption{Top 10 countries by predicted medal count for 2028 Los Angeles, with 95\%
prediction intervals and comparison to 2024 Paris results. The United States maintains
its lead despite China's sustained competitiveness, with the top 3 nations (USA, China,
ROC) projected to win 277 medals combined (21.6\% of global total). This continued
superpower concentration suggests that systemic advantages compound over time, making
it difficult for emerging nations to break into the top tier. Key number: 21.6\% of
medals controlled by just 3 nations.}
```

---

## Caption Quality Checklist

**Every caption must**:
- ✅ Include specific numbers (at least one quantitative metric)
- ✅ Explain what the figure/table shows (clear observation)
- ✅ Interpret what it means (implication)
- ✅ Explain why it matters (story/challenge)
- ✅ Provide actionable takeaway (so what?)
- ✅ Be concise (2-4 sentences maximum)

**Avoid**:
- ❌ Generic descriptions ("Figure 3 shows X vs. Y")
- ❌ Missing numbers (unsubstantiated claims)
- ❌ Captions that only describe without interpreting
- ❌ Captions longer than 4 sentences (too verbose)
- ❌ Captions that don't answer "so what?"

---

## Caption Comparison: Before vs. After

### Before (Generic, Uninformative)

```latex
\caption{Bar chart of medal counts by country.}
```

**Problems**:
- No numbers
- No interpretation
- No insight
- No takeaway

### After (Complete, Compelling)

```latex
\caption{Medal count distribution by country tier, showing 79 countries (51\% of NOCs)
clustered at the 2.0-medal floor. This extreme concentration indicates that the model
cannot distinguish between half of all nations. The artificial nature of this ceiling
suggests that targeted bronze conversion strategies could help small nations break through.
Key number: 51\% of countries stuck at 2.0-medal prediction.}
```

**Improvements**:
- Specific number: 79 countries, 51\%
- Interpretation: model cannot distinguish
- Story: artificial ceiling
- Takeaway: bronze conversion strategies
- Key number highlighted

---

## Quick Reference: Caption Selection Guide

| Figure Type | Use Template | Key Element |
|-------------|--------------|-------------|
| Bar chart / histogram | Template A | Distribution pattern with percentages |
| Line chart / time series | Template B | Trend with slope/rate of change |
| Scatter plot | Template C | Correlation coefficient |
| Heat map | Template D | Clustering or extreme values |
| Multi-panel figure | Template E | Integrated insight across panels |
| Results table | Template F | Ranking or comparison metrics |

---

**Phase 2 Complete**: Template file created
**Alignment**: Based on analysis of O-Prize reference papers
**Techniques**: 4-element structure (observation, implication, story, takeaway)
**Key Principle**: Every caption tells a complete story with specific numbers
