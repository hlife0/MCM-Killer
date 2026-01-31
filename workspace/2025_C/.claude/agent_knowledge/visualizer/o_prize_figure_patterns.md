# O-Prize Figure Patterns

> **"Judges remember papers with striking visuals. O-Prize figures communicate insights, not just data."**

## Lessons from O-Prize Winning Papers

Analysis of reference papers (2425454, 2401298, paper(1)) reveals consistent patterns in visual communication that distinguish O-Prize papers from ordinary submissions.

---

## Pattern 1: The "Hero Figure" Strategy

**What O-Prize Papers Do**: Every paper has 1-2 "hero figures" that capture the entire story at a glance. These appear early (usually Figure 1 or 2) and are referenced throughout.

**Example Hero Figure Types**:
1. **Overview Architecture**: Shows entire model pipeline from data to predictions
2. **Key Result with Context**: Main prediction with uncertainty and baselines
3. **Counterintuitive Finding**: Visual proof of the paper's main insight

**Why It Works**: Judges skim papers in 2-3 minutes. The hero figure makes your contribution immediately apparent.

**Implementation**:
```python
# Hero figures get special treatment
fig, ax = plt.subplots(figsize=(12, 8))  # Larger than typical
# ... detailed, polished visualization
plt.savefig('model_0_diagram_overview.png', dpi=300, bbox_inches='tight')
```

---

## Pattern 2: Conceptual-Statistical Pairing

**What O-Prize Papers Do**: Each model section contains BOTH a conceptual diagram AND statistical validation.

**Example Pairing**:
| Conceptual Figure | Statistical Figure |
|-------------------|-------------------|
| Model architecture diagram | Residual plot |
| Feature hierarchy | Feature importance bar chart |
| Decision flow | Confusion matrix |
| System dynamics | Time series forecast |

**Why It Works**: Conceptual figures explain HOW the model works; statistical figures prove it WORKS.

**Placement Rule**: Conceptual figure FIRST (explains approach), statistical figure SECOND (validates approach).

---

## Pattern 3: The "Aha Moment" Caption

**What O-Prize Papers Do**: Captions don't just describe—they reveal insights.

### Bad Caption (Generic)
```
Figure 3: Predicted vs. actual medal counts for the 2024 Paris Olympics.
```

### O-Prize Caption (4-Element Structure)
```
Figure 3: Model predictions achieve R² = 0.89 for 2024 Paris Olympics (Observation),
demonstrating that historical performance explains 89% of medal variance (Implication).
However, 23 countries fall outside the 95% prediction interval, concentrated among
nations with GDP growth >5% since 2020, suggesting economic momentum creates
unforecastable breakout potential (Story). Future models should incorporate
leading economic indicators rather than lagged averages (Takeaway).
```

**Caption Formula**:
1. **Observation**: What the data shows (with specific numbers)
2. **Implication**: What it means for the research question
3. **Story**: What's surprising or challenges expectations
4. **Takeaway**: What should be done differently / what to remember

---

## Pattern 4: Visual Consistency Across Figures

**What O-Prize Papers Do**: All figures share a consistent visual language.

**Consistency Checklist**:
- [ ] Same color palette across all figures
- [ ] Same font family and size hierarchy
- [ ] Same axis styling (ticks, labels, grids)
- [ ] Same legend positioning convention
- [ ] Same annotation style (arrows, boxes)

**Color Palette Recommendation**:
```python
# O-Prize palette: professional, colorblind-friendly
COLORS = {
    'primary': '#1f77b4',    # Blue - main data
    'secondary': '#ff7f0e',  # Orange - comparison
    'tertiary': '#2ca02c',   # Green - positive/good
    'quaternary': '#d62728', # Red - negative/caution
    'neutral': '#7f7f7f',    # Gray - baseline/reference
}
```

---

## Pattern 5: Quantitative Annotations

**What O-Prize Papers Do**: Figures include key numbers directly on the visual.

**Bad Practice**: Numbers only in caption or text
**Good Practice**: Annotate key values directly on figure

**Example Annotations**:
```python
# Annotate key finding directly on plot
ax.annotate(
    f'Peak: {peak_value:.1f}\n({peak_year})',
    xy=(peak_year, peak_value),
    xytext=(peak_year + 2, peak_value * 1.1),
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=10,
    fontweight='bold',
    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5)
)
```

**What to Annotate**:
- Maximum/minimum values
- Threshold crossings
- Inflection points
- Outliers worth discussing
- Comparative differences (e.g., "+12.3%")

---

## Pattern 6: Progressive Complexity

**What O-Prize Papers Do**: Visual complexity increases through the paper.

**Figure Progression**:
1. **Figure 1-2**: Simple, high-level (overview, problem statement)
2. **Figure 3-5**: Medium complexity (individual model components)
3. **Figure 6-8**: High complexity (detailed results, sensitivity)
4. **Figure 9-10**: Synthesis (summary, implications)

**Why It Works**: Mirrors the reader's learning curve. Early figures establish vocabulary for later figures.

---

## Pattern 7: The "Before/After" or "With/Without" Comparison

**What O-Prize Papers Do**: Show improvement explicitly through comparison figures.

**Comparison Types**:
1. **Baseline vs. Model**: Shows improvement over naive approach
2. **Before vs. After**: Shows effect of key feature/modification
3. **Ours vs. Literature**: Shows competitive advantage

**Implementation**:
```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Left: Baseline
axes[0].scatter(x, y_baseline, alpha=0.5)
axes[0].set_title('Baseline Model\nRMSE = 12.3', fontweight='bold')

# Right: Our model
axes[1].scatter(x, y_model, alpha=0.5, color='green')
axes[1].set_title('Hierarchical Model\nRMSE = 4.7 (-62%)', fontweight='bold')

plt.suptitle('Prediction Accuracy Improvement', fontweight='bold', fontsize=14)
```

---

## Pattern 8: Uncertainty Visualization

**What O-Prize Papers Do**: ALWAYS show uncertainty, not just point estimates.

**Methods**:
1. **Confidence/Prediction Bands**: For time series and regression
2. **Error Bars**: For point estimates
3. **Fan Charts**: For forecasts with increasing uncertainty
4. **Violin/Box Plots**: For distributions

**Example**:
```python
# Fan chart for forecast uncertainty
for i, alpha in enumerate([0.1, 0.3, 0.5, 0.7, 0.9]):
    lower = predictions - z_scores[i] * std
    upper = predictions + z_scores[i] * std
    ax.fill_between(years, lower, upper, alpha=0.2, color='blue')

ax.plot(years, predictions, 'b-', linewidth=2, label='Median Forecast')
ax.axvline(x=2024, color='gray', linestyle='--', label='Training Cutoff')
```

---

## Pattern 9: Geographic Awareness

**What O-Prize Papers Do**: If data has geographic dimension, at least one map figure appears.

**When to Use Maps**:
- Country-level predictions
- Spatial patterns in residuals
- Regional effects
- Trade/travel/migration flows

**Simple Map Approach**:
```python
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world.merge(predictions_df, left_on='iso_a3', right_on='country_code')

fig, ax = plt.subplots(figsize=(15, 10))
world.plot(column='predicted_medals', cmap='YlOrRd', legend=True, ax=ax)
ax.set_title('Predicted 2028 Medal Counts by Country', fontweight='bold')
```

---

## Pattern 10: Summary Infographic

**What O-Prize Papers Do**: Include a visual summary of key findings (often in Conclusions).

**Infographic Elements**:
1. **3-5 Key Numbers**: The most important quantitative findings
2. **Visual Hierarchy**: Most important finding is largest/most prominent
3. **Icons or Mini-Charts**: Visual representation of each finding
4. **Consistent Theme**: Ties back to paper narrative

**Implementation Approach**:
```python
fig = plt.figure(figsize=(14, 10))

# Create grid for infographic
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Hero metric
ax1 = fig.add_subplot(gs[0, :])
ax1.text(0.5, 0.5, 'R² = 0.89', fontsize=48, ha='center', va='center', fontweight='bold')
ax1.text(0.5, 0.2, 'Prediction Accuracy for 2028 Olympics', fontsize=16, ha='center')
ax1.axis('off')

# Supporting metrics
metrics = [
    ('79', 'Countries at\n"Medal Floor"'),
    ('+1.9', 'Host Advantage\n(medals)'),
    ('15%', 'Uncertainty\nReduction'),
]

for i, (value, label) in enumerate(metrics):
    ax = fig.add_subplot(gs[1, i])
    ax.text(0.5, 0.6, value, fontsize=36, ha='center', va='center', fontweight='bold', color='#1f77b4')
    ax.text(0.5, 0.2, label, fontsize=12, ha='center', va='center')
    ax.axis('off')
```

---

## Balance of Statistical vs. Conceptual Figures

### O-Prize Paper Figure Distribution

From analyzing winning papers:

| Section | Typical # Figures | % Conceptual | % Statistical |
|---------|-------------------|--------------|---------------|
| Introduction | 1 | 100% | 0% |
| Background | 1-2 | 50% | 50% |
| Model (each) | 2 | 50% | 50% |
| Results | 3-4 | 10% | 90% |
| Discussion | 1-2 | 50% | 50% |
| Conclusions | 0-1 | 100% | 0% |

**Overall Balance**: ~30% conceptual, ~70% statistical

### Common Mistake: All Statistical

**Anti-Pattern**: Paper has 10 figures, all scatter/bar/line plots

**Problem**:
- Judges don't understand HOW the model works
- Paper feels like data dump, not insight
- Methodology section is walls of text

**Fix**: Add 2-3 conceptual diagrams:
1. Model architecture (Section 3)
2. Data pipeline (Section 4)
3. Key insight summary (Section 6)

---

## Figure Placement Guidelines

### Text-Figure Integration

**Rule**: Every figure must be referenced in text BEFORE it appears.

**Good Pattern**:
```latex
Figure~\ref{fig:architecture} illustrates our three-stage model architecture.
The first stage (left panel) preprocesses raw data...

\begin{figure}[h]
\centering
\includegraphics[width=\textwidth]{model_1_diagram_architecture.png}
\caption{...}
\label{fig:architecture}
\end{figure}
```

**Bad Pattern**: Figure appears with no prior reference or explanation.

### Proximity Principle

- Figure should appear on same page or facing page as primary discussion
- If figure is referenced on page 5, it should not appear on page 8
- Use `[h]` or `[t]` placement, not `[b]` (readers shouldn't have to look back)

---

## What Makes Figures "Memorable"

After 6 months, judges remember:
1. **Counterintuitive visuals**: Results that surprised them
2. **Clean hero figures**: Single image that captures the paper
3. **Novel visualizations**: Creative approaches to showing data
4. **Quantitative annotations**: Specific numbers on the figure

Judges forget:
1. Generic scatter plots with no annotations
2. Busy figures with too many elements
3. Figures that require caption reading to understand
4. Statistical figures without interpretation
