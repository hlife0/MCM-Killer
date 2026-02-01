# Model 6: Flagship Visualization Requirements

> **Purpose**: This file contains specifications for the 4 required Model 6 visualizations demonstrating mechanism optimization, backtesting, and KKT verification.

## Overview

Model 6 (Mechanism Design) requires 4 specialized figures that demonstrate:
1. Mechanism comparison (parameters + performance + significance)
2. Counterfactual analysis (heatmap + scatter)
3. Welfare optimization surface (3D + contour)
4. KKT optimality verification (gradient + eigenvalues + conditions)

---

## Required Figures (4 Total)

### 1. Mechanism Comparison (`model_6_mechanism_comparison.png`)

**Layout**: 1×3 subplot
**Size**: `figsize=(12, 4)`

**Content**:
- **(a) Control Parameters**: Grouped bar chart comparing Status Quo vs Proposed parameters (θ₁, θ₂, θ₃, θ₄, θ₅)
- **(b) Performance Metrics**: Bar chart comparing Welfare, Fairness, Engagement scores
- **(c) Statistical Significance**: Bar chart with -log10(p-value) for McNemar, Fisher's z, Permutation tests

**Data Source**: `results/results_6_v2_recommendation.json`

```python
import matplotlib.pyplot as plt
import numpy as np

# Example implementation
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# (a) Parameter comparison
ax1 = axes[0]
params = ['θ₁\nJudge', 'θ₂\nAggr', 'θ₃\nDiscount', 'θ₄\nThresh', 'θ₅\nTie']
x = np.arange(len(params))
width = 0.35
sq_params = [0.50, 0, 1.0, 0.15, 0]  # Status quo
opt_params = [0.35, 1, 0.85, 0.08, 1]  # Optimal

ax1.bar(x - width/2, sq_params, width, label='Status Quo', color='#1f77b4', alpha=0.8)
ax1.bar(x + width/2, opt_params, width, label='Proposed', color='#2ca02c', alpha=0.8)
ax1.set_ylabel('Parameter Value')
ax1.set_title('(a) Control Parameters')
ax1.set_xticks(x)
ax1.set_xticklabels(params)
ax1.legend()

# (b) Performance metrics
ax2 = axes[1]
metrics = ['Welfare', 'Fairness', 'Engagement']
sq_perf = [0.558, 0.427, 0.750]
opt_perf = [0.612, 0.484, 0.785]
x = np.arange(len(metrics))

ax2.bar(x - width/2, sq_perf, width, label='Status Quo', color='#1f77b4', alpha=0.8)
ax2.bar(x + width/2, opt_perf, width, label='Proposed', color='#2ca02c', alpha=0.8)
ax2.set_ylabel('Score')
ax2.set_title('(b) Performance Metrics')
ax2.set_xticks(x)
ax2.set_xticklabels(metrics)
ax2.legend()

# (c) Statistical significance
ax3 = axes[2]
tests = ['McNemar', 'Fisher z', 'Permutation']
p_values = [0.0004, 0.021, 0.003]
neg_log_p = [-np.log10(p) for p in p_values]
colors = ['green' if p < 0.05 else 'red' for p in p_values]

ax3.bar(tests, neg_log_p, color=colors, alpha=0.8)
ax3.axhline(y=-np.log10(0.05), linestyle='--', color='gray', label='p = 0.05')
ax3.set_ylabel('-log₁₀(p-value)')
ax3.set_title('(c) Statistical Significance')
ax3.legend()

plt.tight_layout()
plt.savefig('output/figures/model_6_mechanism_comparison.png', dpi=300, bbox_inches='tight')
```

---

### 2. Counterfactual Heatmap (`model_6_counterfactual_heatmap.png`)

**Layout**: 1×2 subplot
**Size**: `figsize=(10, 5)`

**Content**:
- **(a) Elimination Changes Heatmap**: Grid showing changes by season (YlOrRd colormap)
- **(b) Performance Delta Scatter**: Δ_Fairness vs Δ_Engagement colored by elimination changes

**Data Source**: `results/counterfactual_analysis_6_v2.csv`

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Load data
cf_df = pd.read_csv('output/implementation/results/counterfactual_analysis_6_v2.csv')

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# (a) Heatmap - reshape to grid (e.g., 6x6 for 36 seasons)
ax1 = axes[0]
n_seasons = len(cf_df)
grid_size = int(np.ceil(np.sqrt(n_seasons)))
grid = np.zeros((grid_size, grid_size))
for i, row in cf_df.iterrows():
    r, c = divmod(i, grid_size)
    if r < grid_size and c < grid_size:
        grid[r, c] = row['elimination_changes']

sns.heatmap(grid, annot=True, fmt='.0f', cmap='YlOrRd', ax=ax1,
            cbar_kws={'label': 'Elimination Changes'})
ax1.set_title('(a) Elimination Changes by Season')
ax1.set_xlabel('Season Column')
ax1.set_ylabel('Season Row')

# (b) Scatter with quadrant labels
ax2 = axes[1]
scatter = ax2.scatter(cf_df['delta_fairness'], cf_df['delta_engagement'],
                      c=cf_df['elimination_changes'], cmap='coolwarm',
                      s=60, alpha=0.7, edgecolor='k', linewidth=0.5)
ax2.axhline(y=0, linestyle='--', color='gray', alpha=0.7)
ax2.axvline(x=0, linestyle='--', color='gray', alpha=0.7)
ax2.set_xlabel('Δ Fairness')
ax2.set_ylabel('Δ Engagement')
ax2.set_title('(b) Performance Deltas by Season')

# Add quadrant labels
ax2.text(0.05, 0.05, 'Win-Win', transform=ax2.transAxes, fontsize=9, color='green')
ax2.text(0.05, 0.95, 'Fairness ↓\nEngagement ↑', transform=ax2.transAxes,
         fontsize=8, va='top', color='orange')
ax2.text(0.95, 0.05, 'Fairness ↑\nEngagement ↓', transform=ax2.transAxes,
         fontsize=8, ha='right', color='orange')
ax2.text(0.95, 0.95, 'Lose-Lose', transform=ax2.transAxes,
         fontsize=9, ha='right', va='top', color='red')

plt.colorbar(scatter, ax=ax2, label='Elimination Changes')
plt.tight_layout()
plt.savefig('output/figures/model_6_counterfactual_heatmap.png', dpi=300, bbox_inches='tight')
```

---

### 3. Welfare Surface (`model_6_welfare_surface.png`)

**Layout**: 1×2 subplot
**Size**: `figsize=(12, 5)`

**Content**:
- **(a) 3D Surface Plot**: W(θ₁, θ₃) with viridis colormap, optimal point marked with red star
- **(b) Contour Plot**: Same data as 2D contour with arrow from Status Quo → Optimal

**Parameters**:
- X-axis: θ₁ (Judge Weight) ∈ [0.1, 0.9]
- Y-axis: θ₃ (Discount Factor) ∈ [0.5, 1.0]
- Z-axis: Welfare W(θ)

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create welfare surface (example: quadratic with maximum at optimal)
theta1 = np.linspace(0.1, 0.9, 50)
theta3 = np.linspace(0.5, 1.0, 50)
T1, T3 = np.meshgrid(theta1, theta3)

# Welfare function (example: peaked at optimal values)
theta1_opt, theta3_opt = 0.35, 0.85
W = 0.7 - 0.5 * ((T1 - theta1_opt)**2 + (T3 - theta3_opt)**2)

fig = plt.figure(figsize=(12, 5))

# (a) 3D surface
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(T1, T3, W, cmap='viridis', alpha=0.8, edgecolor='none')
ax1.scatter([theta1_opt], [theta3_opt], [W.max()], color='red', s=100, marker='*',
            label=f'θ* = ({theta1_opt}, {theta3_opt})', zorder=5)
ax1.set_xlabel('θ₁ (Judge Weight)')
ax1.set_ylabel('θ₃ (Discount)')
ax1.set_zlabel('Welfare W(θ)')
ax1.set_title('(a) Welfare Surface')
ax1.view_init(elev=25, azim=45)
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10, label='W(θ)')

# (b) Contour with optimization path
ax2 = fig.add_subplot(122)
contour = ax2.contourf(T1, T3, W, levels=20, cmap='viridis')
ax2.contour(T1, T3, W, levels=10, colors='white', alpha=0.5, linewidths=0.5)

# Mark optimal and status quo
theta1_sq, theta3_sq = 0.50, 1.0
ax2.scatter([theta1_opt], [theta3_opt], color='red', s=150, marker='*',
            label=f'Optimal θ* = ({theta1_opt}, {theta3_opt})', zorder=5, edgecolor='white')
ax2.scatter([theta1_sq], [theta3_sq], color='orange', s=100, marker='o',
            label=f'Status Quo = ({theta1_sq}, {theta3_sq})', zorder=5, edgecolor='white')

# Arrow from status quo to optimal
ax2.annotate('', xy=(theta1_opt, theta3_opt), xytext=(theta1_sq, theta3_sq),
             arrowprops=dict(arrowstyle='->', color='white', lw=2))

ax2.set_xlabel('θ₁ (Judge Weight)')
ax2.set_ylabel('θ₃ (Discount)')
ax2.set_title('(b) Optimization Path')
ax2.legend(loc='lower right', fontsize=8)
fig.colorbar(contour, ax=ax2, label='W(θ)')

plt.tight_layout()
plt.savefig('output/figures/model_6_welfare_surface.png', dpi=300, bbox_inches='tight')
```

---

### 4. KKT Verification (`model_6_kkt_verification.png`)

**Layout**: 1×3 subplot
**Size**: `figsize=(12, 4)`

**Content**:
- **(a) Gradient at θ***: Bar chart of ∂W/∂θⱼ with threshold lines at ±0.01
- **(b) Hessian Eigenvalues**: Bar chart with eigenvalues (green if ≤0, red if >0)
- **(c) KKT Conditions Checklist**: Horizontal bar with checkmarks

**Data Source**: `results/results_6_v2_recommendation.json` → `kkt_verification`

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# (a) Gradient components
ax1 = axes[0]
params_labels = ['θ₁', 'θ₂', 'θ₃', 'θ₄', 'θ₅']
gradients = [0.002, -0.001, 0.003, -0.001, 0.000]  # Near zero at optimum
colors = ['green' if abs(g) < 0.01 else 'red' for g in gradients]

ax1.bar(params_labels, gradients, color=colors, alpha=0.8, edgecolor='black')
ax1.axhline(y=0.01, linestyle='--', color='gray', alpha=0.7, label='±0.01 threshold')
ax1.axhline(y=-0.01, linestyle='--', color='gray', alpha=0.7)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.set_ylabel('∂W/∂θ')
ax1.set_title('(a) Gradient at θ*')

# Add gradient norm annotation
grad_norm = np.sqrt(sum(g**2 for g in gradients))
ax1.text(0.95, 0.95, f'||∇W|| = {grad_norm:.4f}', transform=ax1.transAxes,
         ha='right', va='top', fontsize=10, bbox=dict(boxstyle='round', facecolor='white'))

# (b) Eigenvalues
ax2 = axes[1]
eigenvalues = [-0.152, -0.083, -0.031, 0.0, 0.0]
eig_labels = [f'λ{i+1}' for i in range(len(eigenvalues))]
colors = ['green' if e <= 0 else 'red' for e in eigenvalues]

ax2.bar(eig_labels, eigenvalues, color=colors, alpha=0.8, edgecolor='black')
ax2.axhline(y=0, color='black', linewidth=1)
ax2.set_ylabel('Eigenvalue')
ax2.set_title('(b) Hessian Eigenvalues')
ax2.text(0.95, 0.05, 'All ≤ 0 ✓\n(Neg. Semi-Def.)', transform=ax2.transAxes,
         ha='right', va='bottom', fontsize=9, color='green',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

# (c) Condition checklist
ax3 = axes[2]
conditions = ['Stationarity', 'Primal\nFeasibility', 'Dual\nFeasibility',
              'Complementary\nSlackness', 'Second\nOrder']
satisfied = [True, True, True, True, True]  # All satisfied
colors = ['green' if s else 'red' for s in satisfied]

y_pos = np.arange(len(conditions))
ax3.barh(y_pos, [1]*len(conditions), color=colors, alpha=0.8, edgecolor='black')

# Add checkmarks
for i, (cond, sat) in enumerate(zip(conditions, satisfied)):
    symbol = '✓' if sat else '✗'
    ax3.text(0.5, i, symbol, ha='center', va='center', fontsize=16,
             color='white', fontweight='bold')

ax3.set_yticks(y_pos)
ax3.set_yticklabels(conditions)
ax3.set_xlim(0, 1)
ax3.set_xticks([])
ax3.set_title('(c) KKT Conditions')
ax3.text(0.95, 0.05, 'KKT Satisfied ✓', transform=ax3.transAxes,
         ha='right', va='bottom', fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.savefig('output/figures/model_6_kkt_verification.png', dpi=300, bbox_inches='tight')
```

---

## Figure Naming Convention

All Model 6 figures must follow this naming pattern:

| Filename | Content |
|----------|---------|
| `model_6_mechanism_comparison.png` | 1×3 comparison (params, metrics, significance) |
| `model_6_counterfactual_heatmap.png` | 1×2 (heatmap + scatter) |
| `model_6_welfare_surface.png` | 1×2 (3D surface + contour) |
| `model_6_kkt_verification.png` | 1×3 (gradient, eigenvalues, conditions) |

---

## Protocol 15 Captions (MANDATORY)

Each figure MUST have a 4-element caption following Protocol 15:

### Caption Structure

1. **Observation**: What the data shows (specific numbers)
2. **Implication**: What it means (interpretation)
3. **Story**: How it challenges expectations (narrative element)
4. **Takeaway**: Actionable insight (so what?)

### Example Captions

**Welfare Surface**:
```
Figure X: The welfare surface W(θ₁, θ₃) shows a unique maximum at θ* = (0.35, 0.85),
achieving W* = 0.67 (Observation), indicating that the optimal mechanism balances
35% judge influence with 15% weekly vote decay (Implication). This contradicts the
status quo assumption that full weight on current votes maximizes fairness (Story),
suggesting producers should implement gradual vote accumulation (Takeaway).
Key number: 9.7% welfare improvement over status quo.
```

**Mechanism Comparison**:
```
Figure X: The proposed mechanism reduces judge weight from 50% to 35% while
introducing Borda count aggregation (Observation), resulting in 5.4% higher welfare
and statistically significant improvements across all three tests (p < 0.05)
(Implication). Counter to intuition, reducing expert influence actually increases
outcome fairness (Story), recommending immediate adoption of the hybrid scoring
system (Takeaway). Key number: p = 0.0004 for McNemar test.
```

**Counterfactual Heatmap**:
```
Figure X: Across 34 seasons, the proposed mechanism would have changed 162
elimination decisions (Observation), with 82% of seasons falling in the "win-win"
quadrant showing improvements in both fairness and engagement (Implication).
Seasons 15 and 23 show the largest changes with 8 different eliminations each
(Story), demonstrating consistent improvement potential across diverse competitive
contexts (Takeaway). Key number: 4.8 average elimination changes per season.
```

**KKT Verification**:
```
Figure X: At the optimal point θ*, the gradient norm equals 0.0029 < 0.01 and all
Hessian eigenvalues are non-positive (Observation), confirming that the solution
satisfies both first-order stationarity and second-order sufficiency conditions
(Implication). This mathematical verification distinguishes our approach from
heuristic recommendations (Story), providing theoretical guarantees for the
proposed mechanism (Takeaway). Key number: ||∇W(θ*)|| = 0.0029.
```

---

## Verification Checklist

Before completing Phase 6 for Model 6:

- [ ] All 4 Model 6 figures generated
- [ ] Each figure saved at 300 DPI
- [ ] Correct naming convention used
- [ ] SciencePlots or fallback styling applied
- [ ] Protocol 15 caption drafted for each figure
- [ ] Figures verified with `mpl_config.save_figure()`
- [ ] No corrupted images (all files valid, readable)
