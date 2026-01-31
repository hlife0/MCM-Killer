# Figure Anti-Patterns: What NOT to Do

> **"Default matplotlib is the visual equivalent of submitting a first draft. Every figure must be enhanced."**

This guide documents common visualization mistakes that weaken MCM papers. Avoid these anti-patterns to produce O-Prize quality figures.

---

## Anti-Pattern 1: Generic Matplotlib Defaults

### The Problem
Using matplotlib without customization produces figures that look "unfinished" to judges.

### Visual Symptoms
- Default color cycle (blue-orange-green-red)
- Default font (DejaVu Sans)
- Default figure size (6.4 x 4.8)
- Heavy black axis lines
- No grid or heavy grid
- Default tick labels

### Example (Bad)
```python
# ❌ NEVER DO THIS
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Plot')
plt.savefig('figure.png')
```

### Fix
```python
# ✅ ALWAYS use SciencePlots or equivalent
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee', 'no-latex'])

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.plot(x, y, linewidth=2, label='Model prediction')
ax.set_xlabel('Year', fontweight='bold')
ax.set_ylabel('Medal Count', fontweight='bold')
ax.set_title('Olympic Medal Predictions 2028', fontweight='bold', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(frameon=True, fancybox=True)
plt.tight_layout()
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
```

---

## Anti-Pattern 2: Over-Reliance on Bar Charts

### The Problem
Using bar charts for everything makes the paper visually monotonous and often misrepresents relationships.

### When Bar Charts are Wrong
- Continuous data (use line plots)
- Time series (use line plots with markers)
- Correlations (use scatter plots)
- Distributions (use histograms/violin plots)
- Many categories (use horizontal bars or heatmaps)

### Example (Bad)
```python
# ❌ Bar chart for time series
years = [2000, 2004, 2008, 2012, 2016, 2020, 2024]
medals = [28, 35, 51, 38, 70, 38, 40]
plt.bar(years, medals)  # Wrong: bars imply discrete categories
```

### Fix
```python
# ✅ Line plot for time series
plt.plot(years, medals, marker='o', linewidth=2, markersize=8)
plt.fill_between(years, medals_lower, medals_upper, alpha=0.3)  # Add uncertainty
```

### Figure Type Decision Tree
```
Is it a time series?
  → YES: Use line plot
  → NO: Is it comparing categories?
    → YES: Are there >10 categories?
      → YES: Use horizontal bar or heatmap
      → NO: Bar chart is OK
    → NO: Is it showing distribution?
      → YES: Use histogram, violin, or box plot
      → NO: Is it showing relationship?
        → YES: Use scatter plot
        → NO: Consider conceptual diagram
```

---

## Anti-Pattern 3: Missing Conceptual Diagrams

### The Problem
Paper has only statistical figures, leaving readers to imagine the model architecture.

### Visual Symptoms
- Model section has equations but no diagram
- No pipeline/workflow visualization
- Methodology is "walls of text"
- Readers can't visualize the approach

### Example (Bad Paper Structure)
```
Section 3.1: Model 1
  - Figure 3.1: Residual plot
  - Figure 3.2: Prediction vs actual

Section 3.2: Model 2
  - Figure 3.3: Feature importance
  - Figure 3.4: Convergence trace

[NO conceptual diagrams anywhere]
```

### Fix (O-Prize Paper Structure)
```
Section 3.1: Model 1
  - Figure 3.1: Model architecture diagram (CONCEPTUAL)
  - Figure 3.2: Prediction vs actual (STATISTICAL)

Section 3.2: Model 2
  - Figure 3.3: Hierarchical structure diagram (CONCEPTUAL)
  - Figure 3.4: Feature importance (STATISTICAL)

Section 4: Data Pipeline
  - Figure 4.1: Data processing workflow (CONCEPTUAL)
```

---

## Anti-Pattern 4: Poor Labeling and Annotations

### The Problem
Figures require reading the caption or surrounding text to understand.

### Visual Symptoms
- Axes labeled with variable names (`x1`, `pred`, `obs`)
- No units on axes
- Legend uses cryptic codes (`m1`, `m2`, `baseline_v2`)
- No annotations on key features
- Title is missing or generic

### Example (Bad)
```python
# ❌ Cryptic labels
ax.set_xlabel('x1')
ax.set_ylabel('y_pred')
ax.legend(['m1', 'm2', 'bl'])
```

### Fix
```python
# ✅ Descriptive labels with units
ax.set_xlabel('GDP per Capita (USD, log scale)', fontweight='bold')
ax.set_ylabel('Predicted Medal Count', fontweight='bold')
ax.legend([
    'Hurdle Model (R²=0.89)',
    'Hierarchical Model (R²=0.87)',
    'Baseline Poisson (R²=0.72)'
], title='Model Comparison')

# Add key annotation
ax.annotate(
    'USA: 126 medals\n(3.2 std above trend)',
    xy=(usa_gdp, usa_medals),
    xytext=(usa_gdp*0.7, usa_medals*1.2),
    arrowprops=dict(arrowstyle='->', color='gray'),
    fontsize=10,
    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5)
)
```

---

## Anti-Pattern 5: Inconsistent Styling

### The Problem
Figures look like they came from different papers/authors.

### Visual Symptoms
- Different color schemes across figures
- Some figures have grids, others don't
- Font sizes vary wildly
- Legend positions are inconsistent
- Some figures are 72 DPI, others 300 DPI

### Fix: Create a Style Template
```python
# Create consistent style dictionary
STYLE = {
    'figure.figsize': (10, 6),
    'figure.dpi': 300,
    'font.size': 12,
    'font.weight': 'normal',
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.labelweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'legend.frameon': True,
    'legend.fancybox': True,
}

# Apply to all figures
plt.rcParams.update(STYLE)

# Or use SciencePlots for automatic consistency
plt.style.use(['science', 'ieee', 'no-latex'])
```

---

## Anti-Pattern 6: Figures That Don't Tell a Story

### The Problem
Figure shows data but doesn't guide interpretation.

### Visual Symptoms
- Raw data dump without highlighting patterns
- No trend lines or reference lines
- No grouping or separation of relevant clusters
- Caption just describes what's shown, not what it means

### Example (Bad Caption)
```latex
\caption{Scatter plot of GDP vs. medal count for 235 countries.}
```

### Fix (O-Prize Caption)
```latex
\caption{GDP per capita explains 67\% of medal variance (R²=0.67), with three
distinct clusters: (1) developing nations below the ``medal threshold'' at
\$15,000 GDP (gray, N=79), (2) emerging powers showing economic-athletic
decoupling (\$15K-\$40K, orange, N=111), and (3) established superpowers
(\$40K+, blue, N=45) where cultural investment becomes the differentiator.
The 23 outliers above the trend line (marked with $\star$) share a common
trait: per-capita sports investment exceeding 0.5\% of GDP.}
```

---

## Anti-Pattern 7: Too Many Elements

### The Problem
Figure is cluttered with overlapping elements that compete for attention.

### Visual Symptoms
- More than 7 series on one plot
- Overlapping labels
- Dense scatter plots without transparency
- Multiple y-axes
- Annotations blocking data

### Fix: Simplify or Split
```python
# ❌ 10 countries on one plot
for country in countries[:10]:
    ax.plot(years, data[country], label=country)

# ✅ Focus on key comparisons
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: Top 3 countries
for country in ['USA', 'China', 'Russia']:
    axes[0].plot(years, data[country], label=country, linewidth=2)
axes[0].set_title('Top 3 Countries')

# Panel 2: Host countries
for country in host_countries:
    axes[1].plot(years, data[country], label=country, linewidth=2)
axes[1].set_title('Host Country Effect')

# Panel 3: Aggregate trends
axes[2].plot(years, data.mean(), label='Average', linewidth=2)
axes[2].fill_between(years, data.quantile(0.25), data.quantile(0.75), alpha=0.3)
axes[2].set_title('Overall Trend (IQR shaded)')
```

---

## Anti-Pattern 8: Missing Uncertainty

### The Problem
Point estimates without uncertainty bands overstate confidence.

### Visual Symptoms
- Line plots without confidence intervals
- Bar charts without error bars
- Single predictions without prediction intervals
- No acknowledgment of model uncertainty

### Example (Bad)
```python
# ❌ Point estimates only
ax.plot(years, predictions)
ax.scatter(future_years, future_predictions)
```

### Fix
```python
# ✅ Show uncertainty
# Historical fit with confidence band
ax.plot(years, predictions, 'b-', linewidth=2, label='Model fit')
ax.fill_between(years, ci_lower, ci_upper, alpha=0.2, color='blue', label='95% CI')

# Future predictions with prediction intervals
ax.plot(future_years, future_predictions, 'r--', linewidth=2, label='Forecast')
ax.fill_between(future_years, pi_lower, pi_upper, alpha=0.2, color='red', label='95% PI')

# Vertical line at training cutoff
ax.axvline(x=2024, color='gray', linestyle=':', label='Training cutoff')
```

---

## Anti-Pattern 9: Low Resolution or Wrong Format

### The Problem
Figures are pixelated in the final PDF or have compression artifacts.

### Visual Symptoms
- Visible pixels when zoomed
- JPEG compression artifacts on line drawings
- Inconsistent resolution across figures
- File sizes vary from 10KB to 10MB

### Fix
```python
# ✅ Always save at 300 DPI as PNG
plt.savefig('figure.png', dpi=300, bbox_inches='tight', format='png')

# For vector graphics (diagrams), use PDF or SVG
plt.savefig('diagram.pdf', bbox_inches='tight', format='pdf')
```

### File Format Guide
| Content | Format | Why |
|---------|--------|-----|
| Statistical plots | PNG (300 DPI) | Good balance of quality/size |
| Line diagrams | PDF/SVG | Vector = infinite scaling |
| Photos/images | PNG or JPEG (high quality) | Depends on source |
| Final paper | Embed PNG/PDF | Consistent rendering |

---

## Anti-Pattern 10: Ignoring Colorblind Accessibility

### The Problem
~8% of male readers have some form of color blindness. Red-green schemes are problematic.

### Visual Symptoms
- Red vs. green to distinguish categories
- Light colors that wash out in grayscale
- No shape/marker differentiation

### Fix
```python
# ✅ Use colorblind-friendly palettes
import seaborn as sns

# Option 1: Colorblind palette
palette = sns.color_palette('colorblind')

# Option 2: Viridis family (perceptually uniform)
palette = plt.cm.viridis(np.linspace(0, 1, n_categories))

# Option 3: Different markers + colors
markers = ['o', 's', '^', 'D', 'v']
for i, (cat, marker) in enumerate(zip(categories, markers)):
    ax.scatter(x[cat], y[cat], marker=marker, label=cat, s=100)
```

---

## Anti-Pattern 11: Figure Not Referenced in Text

### The Problem
Figure exists but is never discussed in the paper body.

### Visual Symptoms
- No `Figure X` reference in surrounding paragraphs
- Figure appears but reader doesn't know why
- Caption is only explanation

### Fix
Every figure needs:
1. **Pre-reference**: "Figure X illustrates..." BEFORE the figure
2. **Post-reference**: Discussion of what to observe AFTER the figure
3. **Caption**: Standalone explanation for skimming readers

```latex
% Good pattern
As shown in Figure~\ref{fig:architecture}, our model consists of three stages.
The preprocessing stage (left panel) handles missing data imputation...

\begin{figure}
...
\end{figure}

The key insight from Figure~\ref{fig:architecture} is that the hurdle and
count components share the feature extraction layer, enabling joint learning.
```

---

## Quick Reference: Do's and Don'ts

| Don't | Do |
|-------|-----|
| Default matplotlib colors | SciencePlots or custom palette |
| Bar charts for everything | Match chart type to data type |
| Only statistical figures | 30% conceptual, 70% statistical |
| Cryptic axis labels | Descriptive labels with units |
| Inconsistent styling | Apply style template to all |
| Data dump without story | Guide interpretation with annotations |
| Cluttered 10-series plots | Split into panels or focus |
| Point estimates only | Always show uncertainty |
| 72 DPI JPEG | 300 DPI PNG |
| Red-green color scheme | Colorblind-friendly palette |
| Unreferenced figures | Pre-reference, post-discuss, caption |

---

## Self-Check Checklist Before Submission

For each figure, verify:

**Technical Quality**
- [ ] 300 DPI resolution
- [ ] PNG format (or PDF for diagrams)
- [ ] Standardized filename: `model_X_type_description.png`

**Visual Quality**
- [ ] SciencePlots or equivalent styling applied
- [ ] Consistent with other figures in paper
- [ ] Colorblind accessible
- [ ] Not cluttered (≤5 series per panel)

**Content Quality**
- [ ] Axes labeled with units
- [ ] Title is informative
- [ ] Legend is clear (no codes)
- [ ] Key features annotated
- [ ] Uncertainty shown where applicable

**Integration Quality**
- [ ] Referenced in text before appearing
- [ ] Caption follows 4-element structure
- [ ] Tells a story, not just shows data
- [ ] Contributes to paper narrative
