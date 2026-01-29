# MCM-Specific Template Documentation

## Overview

This document provides MCM-specific guidance for creating publication-quality figures using SciencePlots templates.

---

## Template Philosophy

MCM figures serve three purposes:

1. **Communication** - Convey complex results clearly to judges
2. **Credibility** - Demonstrate rigorous analysis
3. **Competition** - Stand out from 10,000+ submissions

Every figure should be **O-Prize quality** - worthy of an Outstanding Winner award.

---

## Template Structure

All SciencePlots templates follow this structure:

```python
# -*- coding: utf-8 -*-
"""
Template Name: [Brief description]
Model Number: [Which model uses this]
Output: [Expected figure filename]
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Add tools to path
sys.path.insert(0, '../../tools')
import mpl_config

# Apply research style
scienceplots_available = mpl_config.apply_research_style()

# Load data
data = pd.read_csv('output/results_1.csv', encoding='utf-8')

# Create figure
fig, ax = plt.subplots()

# [PLOT-SPECIFIC CODE HERE]

# Save with verification
output_path = 'output/figures/model_X_figure_description.png'
success, msg = mpl_config.save_figure(fig, output_path)

if success:
    print(f"✓ {output_path}")
else:
    print(f"✗ Error: {msg}")
```

---

## Template 1: Performance Comparison

**Purpose**: Compare multiple models or methods on the same metrics

**When to Use**:
- Comparing Model 1 vs Model 2 vs Model 3
- Showing performance on different test cases
- Evaluating sensitivity to parameters

**Input Data**: CSV with columns like `['model', 'metric', 'value', 'error']`

**Output**: Grouped bar chart with error bars

**Key Features**:
- Grouped bars for direct comparison
- Error bars showing uncertainty
- Consistent color scheme
- Clear legend

**Template File**: `knowledge_library/templates/scienceplots/performance_comparison_template.py`

**Example Usage**:
```python
# Input data format:
# model,metric,value,error
# Model_1,Accuracy,0.85,0.03
# Model_1,R_squared,0.78,0.05
# Model_2,Accuracy,0.82,0.04
# Model_2,R_squared,0.75,0.06
```

**Customization**:
- Adjust bar width for more/less models
- Change color palette using `mpl_config.get_color_palette()`
- Rotate x-axis labels if metric names are long

---

## Template 2: Time Series with Confidence Intervals

**Purpose**: Show trends over time with uncertainty bounds

**When to Use**:
- Predictions over years (e.g., medal counts 1992-2024)
- Training progress over epochs
- Forecasting with prediction intervals

**Input Data**: CSV with columns like `['year', 'predictions', 'PI_2.5', 'PI_97.5']`

**Output**: Line plot with shaded confidence band

**Key Features**:
- Main line showing point estimates
- Shaded region showing confidence intervals
- Gridlines for readability
- Clear axis labels

**Template File**: `knowledge_library/templates/scienceplots/time_series_ci_template.py`

**Example Usage**:
```python
# Input data format:
# year,predictions,PI_2.5,PI_97.5
# 1992,105,98,112
# 1994,108,100,116
# 1996,115,107,123
```

**Customization**:
- Change confidence level (90%, 95%, 99%)
- Add multiple lines (e.g., actual vs predicted)
- Add vertical lines for events (e.g., rule changes)
- Use logarithmic scale if needed

---

## Template 3: Predictions vs Actual (Scatter)

**Purpose**: Validate model predictions against ground truth

**When to Use**:
- Model validation
- Checking prediction accuracy
- Identifying outliers

**Input Data**: CSV with columns like `['actual', 'predicted']`

**Output**: Scatter plot with diagonal reference line

**Key Features**:
- Scatter points with transparency
- Diagonal reference line (y = x)
- R² correlation coefficient
- Color-coded deviations

**Template File**: `knowledge_library/templates/scienceplots/scatter_predictions_template.py`

**Example Usage**:
```python
# Input data format:
# actual,predicted
# 105,108
# 98,95
# 112,118
```

**Customization**:
- Color points by residual magnitude
- Add error bars if available
- Use different markers for different categories
- Add marginal histograms (optional)

---

## Template 4: Residual Distribution (Histogram)

**Purpose**: Check if residuals are normally distributed (zero mean, constant variance)

**When to Use**:
- Model diagnostic
- Checking assumptions
- Identifying bias

**Input Data**: CSV with column `['residuals']`

**Output**: Histogram with mean/median reference lines

**Key Features**:
- Normalized density
- Mean reference line
- Optional normal distribution overlay
- Clear labeling

**Template File**: `knowledge_library/templates/scienceplots/histogram_residuals_template.py`

**Example Usage**:
```python
# Input data format:
# residuals
# -3.2
# 1.5
# 0.8
# -1.2
```

**Customization**:
- Adjust number of bins
- Add Q-Q plot (normality test)
- Overlay theoretical normal distribution
- Use kernel density estimate (KDE) for smooth curve

---

## Template 5: Feature Correlation Heatmap

**Purpose**: Show correlations between features (detect multicollinearity)

**When to Use**:
- Feature selection
- Identifying redundant features
- Explaining model behavior

**Input Data**: CSV with numeric feature columns

**Output**: Heatmap with annotated correlations

**Key Features**:
- Diverging colormap (coolwarm)
- Values shown in cells
- Symmetric matrix
- Colorbar with label

**Template File**: `knowledge_library/templates/scienceplots/heatmap_correlation_template.py`

**Example Usage**:
```python
# Input data format:
# GDP,Population,Medals,Host
# 1.2e12,5e7,105,0
# 3.4e12,1e8,120,1
# 8e11,3e7,98,0
```

**Customization**:
- Mask upper triangle (avoid redundancy)
- Use hierarchical clustering (reorder features)
- Change colormap (RdBu, seismic, etc.)
- Add significance stars for correlations

---

## Template 6: Multi-Panel Results Summary

**Purpose**: Show multiple aspects of model performance in one figure

**When to Use**:
- Comprehensive model overview
- Paper main figures (e.g., Figure 1, Figure 2)
- Executive summary

**Input Data**: Multiple CSV files or combined CSV with multiple metrics

**Output**: 2x2 or 3x1 multi-panel figure

**Key Features**:
- Panel labels (A, B, C, ...)
- Consistent styling across panels
- Shared axes when appropriate
- Compact layout

**Template File**: `knowledge_library/templates/scienceplots/multipanel_results_template.py`

**Example Layout**:
```
┌─────────────────────┬─────────────────────┐
│   Panel A:          │   Panel B:          │
│   Time series       │   Scatter           │
├─────────────────────┼─────────────────────┤
│   Panel C:          │   Panel D:          │
│   Residuals         │   Feature import.   │
└─────────────────────┴─────────────────────┘
```

**Customization**:
- Adjust panel count (2x2, 3x1, 2x3)
- Change figure size for aspect ratio
- Use shared x/y axes
- Add overall title

---

## MCM-Specific Best Practices

### 1. Figure Numbering and Referencing

**In Paper (LaTeX)**:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/model_1_scatter_predictions_vs_actual.png}
    \caption{Model 1 predictions demonstrate strong correlation with actual medal counts ($R^2 = 0.87$), indicating accurate performance estimation.}
    \label{fig:model1_predictions}
\end{figure}

See Figure \ref{fig:model1_predictions} for validation results.
```

**Figure Naming**: Follow convention `model_X_figure_type_description.png`

### 2. Caption Writing (Protocol 15)

**Required Format**: "[Observation], indicating [Implication]. Key detail: [quantified comparison]."

**Examples**:
- ✅ "Figure 3 shows Model 1 predictions closely track actual medal counts from 1992-2024, indicating robust temporal accuracy. Key detail: Mean absolute error of 3.2 medals per country-year."
- ❌ "Figure 3 shows predictions vs actual."

### 3. Color Accessibility

**ALWAYS** use colorblind-friendly palettes:
- `'colorblind'` - Paul Tol's scheme (default)
- `'viridis'` - Perceptually uniform
- `'coolwarm'` - Diverging, good for heatmaps

**AVOID**:
- Rainbow/red-green schemes (hard for colorblind users)
- Similar colors for adjacent categories

### 4. Font Sizes and Legibility

**Publication Standards**:
- Axis labels: 12-14 pt (bold)
- Tick labels: 10-12 pt
- Legend: 10-11 pt
- Title: 14-16 pt (bold)

**For Poster Presentations**: Increase all by 2-4 pt

### 5. Figure Resolution

**IEEE Requirements**:
- Line art: 600-1200 DPI
- Grayscale: 300-600 DPI
- Color: 300 DPI minimum

**MCM-Killer Default**: 300 DPI (acceptable for most journals)

**To Increase DPI**:
```python
mpl_config.apply_research_style(dpi=600, figsize=(10, 6))
```

### 6. Aspect Ratio

**Common Ratios**:
- **16:9** (wide): Presentations, posters
- **4:3** (standard): Papers, reports
- **1:1** (square): Social media, supplementary

**Default**: 10x6 inches (5:3 ratio, golden ratio adjacent)

**Adjust for Content**:
```python
# Wide figure (time series)
mpl_config.apply_research_style(figsize=(12, 5))

# Tall figure (horizontal bar chart)
mpl_config.apply_research_style(figsize=(8, 10))
```

---

## Template Customization Workflow

### Step 1: Select Template

Choose based on data type and goal (see `plot_type_guide.md`)

### Step 2: Copy Template

Copy from `knowledge_library/templates/scienceplots/` to working directory

### Step 3: Update Paths

```python
# Update input data path
data = pd.read_csv('output/results_1.csv', encoding='utf-8')

# Update output path
output_path = 'output/figures/model_1_scatter_predictions_vs_actual.png'
```

### Step 4: Customize Plot

```python
# Adjust colors
colors = mpl_config.get_color_palette('colorblind')
ax.bar(categories, values, color=colors[0])

# Add annotations
ax.annotate('Peak', xy=(max_year, max_value), xytext=(max_year+1, max_value+10),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adjust limits
ax.set_xlim(1990, 2025)
ax.set_ylim(0, 150)
```

### Step 5: Test and Verify

```bash
python template_name.py
```

**Check Output**:
- [ ] Figure saved successfully
- [ ] `verify_figure_quality()` passed
- [ ] No visual artifacts
- [ ] Correct data shown

### Step 6: Integrate into Paper

Add to LaTeX:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/model_1_scatter_predictions_vs_actual.png}
    \caption{Your caption here following Protocol 15}
    \label{fig:model1_predictions}
\end{figure}
```

---

## Common Customization Tasks

### Add Secondary Y-Axis

```python
ax2 = ax.twinx()
ax2.plot(years, gdp, 'r-', label='GDP')
ax2.set_ylabel('GDP (USD)', color='r')
ax2.tick_params(axis='y', labelcolor='r')
```

### Add Vertical Annotations

```python
# Mark rule change
ax.axvline(x=2000, color='gray', linestyle='--', linewidth=2)
ax.text(2001, ax.get_ylim()[1], 'Rule Change', rotation=90, verticalalignment='top')
```

### Highlight Specific Data Points

```python
# Find max value
max_idx = data['value'].idxmax()
ax.scatter(data.loc[max_idx, 'year'], data.loc[max_idx, 'value'],
           s=200, c='red', marker='*', zorder=5, label='Peak')
```

### Add Inset (Zoom)

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Create inset
axins = inset_axes(ax, width="40%", height="40%", loc='lower right')
axins.plot(x_zoom, y_zoom)
axins.set_xlim(2000, 2005)
axins.set_ylim(90, 110)
```

---

## Troubleshooting Templates

### Issue: Template fails to execute

**Check**:
- Input CSV exists and has correct columns
- UTF-8 encoding specified
- All required libraries installed

**Fix**:
```python
# Add error handling
try:
    data = pd.read_csv('output/results_1.csv', encoding='utf-8')
except FileNotFoundError:
    print("Error: Input file not found")
    sys.exit(1)
```

### Issue: Figure looks wrong (wrong data shown)

**Check**:
- Column names match CSV
- Data loaded correctly (`print(data.head())`)
- Plot type matches data relationship

**Fix**:
```python
# Debug: Print data info
print("Columns:", data.columns.tolist())
print("Shape:", data.shape)
print("First few rows:\n", data.head())
```

### Issue: Figure fails quality verification

**Check**:
- File size > 0 bytes
- Image dimensions ≥ 100x100
- No corruption (all pixels same color)

**Fix**:
```python
# Increase figure size
mpl_config.apply_research_style(figsize=(12, 8))

# Ensure tight_layout
plt.tight_layout()

# Verify before saving
fig.canvas.draw()
```

---

## Additional Resources

- **Templates**: `knowledge_library/templates/scienceplots/`
- **Protocols**: `agent_knowledge/scienceplots/protocols.md`
- **Plot Selection**: `agent_knowledge/scienceplots/plot_type_guide.md`
- **Main Config**: `tools/9_mpl_config.py`
- **Controller**: `tools/scienceplots_controller.py`

---

## Version History

- **v3.1.0** (2025-01-29): Initial template documentation
  - Performance comparison template
  - Time series with CI template
  - MCM-specific best practices
  - Customization workflow
