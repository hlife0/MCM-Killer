# SciencePlots Visualization Protocols

## Overview

These 10 protocols ensure consistent, publication-quality visualizations across all MCM-Killer figures. Every visualization agent MUST follow these protocols.

---

## Protocol 1: Figure Initialization

> **"Every figure starts with proper configuration."**

### Rules

1. **ALWAYS** apply research style before creating figures
2. **ALWAYS** specify DPI (300 for publication)
3. **ALWAYS** specify figure size (default: 10x6 inches)
4. **NEVER** use matplotlib defaults

### Code Template

```python
import sys
sys.path.insert(0, '../../tools')
import mpl_config

# Apply research style (with fallback)
scienceplots_available = mpl_config.apply_research_style(dpi=300, figsize=(10, 6))

# Create figure
fig, ax = plt.subplots()
```

### Verification

- [ ] Style applied before figure creation
- [ ] DPI set to 300
- [ ] Figure size appropriate for content
- [ ] No matplotlib default styling remains

---

## Protocol 2: Data Preparation

> **"Clean data prevents plotting errors."**

### Rules

1. **ALWAYS** read CSV with UTF-8 encoding
2. **ALWAYS** handle missing values (NaN, Inf)
3. **ALWAYS** validate data types before plotting
4. **NEVER** assume data is clean

### Code Template

```python
import pandas as pd
import numpy as np

# Read with UTF-8 encoding
data = pd.read_csv('output/results_1.csv', encoding='utf-8')

# Handle missing values
data = data.replace([np.inf, -np.inf], np.nan)
data = data.dropna()

# Validate types
assert data['year'].dtype in [int, float], "Year must be numeric"
assert data['predictions'].dtype in [int, float], "Predictions must be numeric"
```

### Verification

- [ ] UTF-8 encoding specified
- [ ] NaN/Inf values handled
- [ ] Data types validated
- [ ] No plotting errors due to data issues

---

## Protocol 3: Plot Selection

> **"Match plot type to data relationship."**

### Decision Tree

```
Data → What is the relationship?
│
├─ Trend over time → Line plot
├─ Comparison between groups → Bar chart
├─ Correlation between variables → Scatter plot
├─ Distribution of single variable → Histogram/Box plot
├─ Matrix of relationships → Heatmap
├─ Geographic data → Map
└─ Model architecture → Flowchart (Mode B: Mermaid)
```

### Plot Types

| Data Type | Plot Type | Protocol Reference |
|-----------|-----------|-------------------|
| Time series | Line | Protocol 4 |
| Categorical comparison | Bar | Protocol 5 |
| Correlation | Scatter | Protocol 6 |
| Distribution | Histogram | Protocol 7 |
| Multi-variable | Heatmap | Protocol 8 |

### Verification

- [ ] Plot type matches data relationship
- [ ] Alternative plot types considered
- [ ] Plot type documented in figure caption

---

## Protocol 4: Line Plots (Time Series)

> **"Show trends with confidence intervals."**

### Rules

1. **ALWAYS** include confidence intervals when available
2. **ALWAYS** label axes with units
3. **ALWAYS** use gridlines for readability
4. **PREFER** shaded bands for confidence intervals

### Code Template

```python
fig, ax = plt.subplots()

# Main line
ax.plot(data['year'], data['predictions'], 'o-', linewidth=2, markersize=6, label='Predictions')

# Confidence interval (if available)
if 'PI_2.5' in data.columns and 'PI_97.5' in data.columns:
    ax.fill_between(data['year'], data['PI_2.5'], data['PI_97.5'], alpha=0.3, label='95% CI')

# Labels
ax.set_xlabel('Year', fontweight='bold')
ax.set_ylabel('Predicted Medal Count', fontweight='bold')
ax.set_title('Model 1: Medal Count Predictions (1992-2024)', fontweight='bold')
ax.legend(loc='best')
ax.grid(True, alpha=0.3)

plt.tight_layout()
```

### Verification

- [ ] Time variable on x-axis
- [ ] Confidence intervals shown (if available)
- [ ] Axes labeled with units
- [ ] Gridlines present
- [ ] Legend positioned appropriately

---

## Protocol 5: Bar Charts (Comparisons)

> **"Group related bars, add error bars."**

### Rules

1. **ALWAYS** group related categories
2. **ALWAYS** add error bars when available
3. **ALWAYS** rotate labels if needed for readability
4. **NEVER** use 3D bars (hard to read)

### Code Template

```python
fig, ax = plt.subplots()

# Grouped bar chart
x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, group1_values, width, label='Model 1', yerr=group1_errors, capsize=5)
bars2 = ax.bar(x + width/2, group2_values, width, label='Model 2', yerr=group2_errors, capsize=5)

# Labels
ax.set_xlabel('Country', fontweight='bold')
ax.set_ylabel('Performance Metric', fontweight='bold')
ax.set_title('Model Performance Comparison', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
```

### Verification

- [ ] Categories grouped logically
- [ ] Error bars shown (if applicable)
- [ ] Labels readable (no overlap)
- [ ] Y-axis gridlines present
- [ ] Legend identifies all groups

---

## Protocol 6: Scatter Plots (Correlations)

> **"Show relationship, add reference line."**

### Rules

1. **ALWAYS** add diagonal reference line (y=x)
2. **ALWAYS** use transparency for overlapping points
3. **ALWAYS** label both axes clearly
4. **CONSIDER** adding correlation coefficient

### Code Template

```python
fig, ax = plt.subplots()

# Scatter with transparency
ax.scatter(data['actual'], data['predicted'], alpha=0.6, s=50)

# Reference line (y=x)
min_val = min(data['actual'].min(), data['predicted'].min())
max_val = max(data['actual'].max(), data['predicted'].max())
ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')

# Labels
ax.set_xlabel('Actual Medal Count', fontweight='bold')
ax.set_ylabel('Predicted Medal Count', fontweight='bold')
ax.set_title('Model 1: Predictions vs Actual', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Calculate R²
correlation = np.corrcoef(data['actual'], data['predicted'])[0, 1]
r_squared = correlation ** 2
ax.text(0.05, 0.95, f'$R^2 = {r_squared:.3f}$', transform=ax.transAxes,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
```

### Verification

- [ ] Diagonal reference line present
- [ ] Points have transparency (alpha < 1)
- [ ] Both axes labeled with same units
- [ ] Correlation coefficient shown
- [ ] Gridlines present

---

## Protocol 7: Histograms (Distributions)

> **"Show distribution shape, add reference line."**

### Rules

1. **ALWAYS** choose appropriate number of bins
2. **ALWAYS** add vertical line for mean/median
3. **ALWAYS** label x-axis clearly
4. **PREFER** density plot for smooth distribution

### Code Template

```python
fig, ax = plt.subplots()

# Histogram
n, bins, patches = ax.hist(data['residuals'], bins=30, density=True, alpha=0.7, edgecolor='black')

# Reference line (mean)
mean_val = data['residuals'].mean()
ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_val:.2f}')

# Labels
ax.set_xlabel('Residual Value', fontweight='bold')
ax.set_ylabel('Density', fontweight='bold')
ax.set_title('Model 1: Residual Distribution', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
```

### Verification

- [ ] Appropriate number of bins (15-50)
- [ ] Mean/median reference line present
- [ ] Density shown (normalized)
- [ ] X-axis labeled with units
- [ ] Gridlines on y-axis

---

## Protocol 8: Heatmaps (Correlations)

> **"Show patterns, use diverging colormap."**

### Rules

1. **ALWAYS** use diverging colormap for correlations
2. **ALWAYS** add colorbar with label
3. **ALWAYS** show values in cells
4. **NEVER** use sequential colormap for correlations

### Code Template

```python
fig, ax = plt.subplots(figsize=(10, 8))

# Calculate correlation matrix
corr_matrix = data.corr()

# Heatmap
im = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')

# Colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Correlation Coefficient', rotation=-90, va='bottom')

# Show values
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                      ha='center', va='center', color='black', fontsize=8)

# Labels
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_yticks(range(len(corr_matrix.index)))
ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
ax.set_yticklabels(corr_matrix.index)
ax.set_title('Feature Correlation Matrix', fontweight='bold')

plt.tight_layout()
```

### Verification

- [ ] Diverging colormap (coolwarm, RdBu)
- [ ] Colorbar with label present
- [ ] Values shown in cells
- [ ] Labels readable (rotated if needed)
- [ ] Symmetric for correlation matrix

---

## Protocol 9: Multi-Panel Figures

> **"Arrange panels logically, label consistently."**

### Rules

1. **ALWAYS** use shared axes when appropriate
2. **ALWAYS** label panels (A, B, C, ...)
3. **ALWAYS** maintain consistent styling across panels
4. **PREFER** 2x2 or 3x1 layouts

### Code Template

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Panel A: Line plot
axes[0, 0].plot(data['year'], data['predictions'])
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Predictions')
axes[0, 0].set_title('(A) Time Trend', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Panel B: Scatter plot
axes[0, 1].scatter(data['actual'], data['predicted'])
axes[0, 1].set_xlabel('Actual')
axes[0, 1].set_ylabel('Predicted')
axes[0, 1].set_title('(B) Predictions vs Actual', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Panel C: Histogram
axes[1, 0].hist(data['residuals'], bins=30)
axes[1, 0].set_xlabel('Residuals')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('(C) Residual Distribution', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Panel D: Bar chart
axes[1, 1].bar(categories, values)
axes[1, 1].set_xlabel('Category')
axes[1, 1].set_ylabel('Value')
axes[1, 1].set_title('(D) Comparison', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
```

### Verification

- [ ] Panels arranged logically
- [ ] Each panel labeled (A, B, C, ...)
- [ ] Consistent styling across panels
- [ ] No overlapping elements
- [ ] Shared axes used when appropriate

---

## Protocol 10: Export and Verification

> **"Save with verification, catch corruption."**

### Rules

1. **ALWAYS** use `mpl_config.save_figure()` with verification
2. **ALWAYS** specify output path with naming convention
3. **ALWAYS** call `verify_figure_quality()` after saving
4. **NEVER** assume save succeeded without verification

### Code Template

```python
import mpl_config

# Save with automatic verification
success, msg = mpl_config.save_figure(fig, 'output/figures/model_1_scatter_predictions_vs_actual.png')

if success:
    print(f"Success: {msg}")
else:
    print(f"Error: {msg}")
    # Handle error (retry, rewind, etc.)
```

### Verification Checklist

- [ ] Output path follows naming convention
- [ ] File saved successfully
- [ ] `verify_figure_quality()` returns True
- [ ] File size > 0 bytes
- [ ] Image dimensions appropriate (≥100x100)
- [ ] No pixel corruption detected

---

## Protocol Compliance Summary

Every figure generated by MCM-Killer MUST comply with:

- [ ] Protocol 1: Figure initialization
- [ ] Protocol 2: Data preparation
- [ ] Protocol 3: Plot selection
- [ ] Protocol 4-8: Plot-specific rules
- [ ] Protocol 9: Multi-panel rules (if applicable)
- [ ] Protocol 10: Export and verification

**Non-compliance → Visual quality gate failure → Rewind required**
