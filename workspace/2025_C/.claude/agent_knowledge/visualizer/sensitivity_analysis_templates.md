# Sensitivity Analysis Visualization Templates

> **"Sensitivity analysis is MANDATORY for every MCM paper. Judges expect to see how predictions change when assumptions change. These templates make sensitivity figures publication-ready in minutes."**

This guide provides copy-paste-ready Python templates for sensitivity analysis visualizations, following O-Prize standards.

---

## Overview: Sensitivity Analysis Figure Types

| Figure Type | Use Case | When to Use |
|-------------|----------|-------------|
| Tornado Diagram | One-at-a-time (OAT) sensitivity | Show relative importance of parameters |
| Spider Plot | Multi-parameter sensitivity | Compare parameter effects on single metric |
| Sensitivity Heatmap | Two-parameter interaction | Show combined effects on output |
| Morris Screening Plot | Global sensitivity (many parameters) | Identify most influential parameters |
| Sobol Indices Bar Chart | Variance-based sensitivity | Quantify main vs interaction effects |

---

## Template 1: Tornado Diagram (One-at-a-Time Sensitivity)

**Purpose**: Show how much the output changes when each parameter varies by ±X% from baseline.

**When to Use**:
- Parameter importance ranking
- Identifying critical assumptions
- Communicating risk factors to non-technical readers

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_tornado_diagram(
    parameters: list,
    low_values: list,
    high_values: list,
    baseline: float,
    output_path: str = "sensitivity_tornado.png",
    title: str = "Tornado Diagram: Parameter Sensitivity",
    xlabel: str = "Predicted Medal Count"
):
    """
    Create a tornado diagram for one-at-a-time sensitivity analysis.

    Parameters:
    -----------
    parameters : list of str
        Parameter names (e.g., ["GDP Growth", "Population", "Host Effect"])
    low_values : list of float
        Output values when parameter is at -X% (e.g., -20%)
    high_values : list of float
        Output values when parameter is at +X% (e.g., +20%)
    baseline : float
        Baseline output value (center line)
    output_path : str
        Path to save the figure
    title : str
        Figure title
    xlabel : str
        X-axis label (the output metric)

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """

    # Calculate ranges and sort by total swing
    ranges = np.array(high_values) - np.array(low_values)
    sort_idx = np.argsort(ranges)[::-1]  # Largest swing first

    parameters = [parameters[i] for i in sort_idx]
    low_values = [low_values[i] for i in sort_idx]
    high_values = [high_values[i] for i in sort_idx]

    n_params = len(parameters)
    y_pos = np.arange(n_params)

    # Professional color scheme
    color_negative = '#e53e3e'  # Red for decrease
    color_positive = '#38a169'  # Green for increase

    fig, ax = plt.subplots(figsize=(10, max(6, n_params * 0.5)))

    # Draw bars
    for i, (param, low, high) in enumerate(zip(parameters, low_values, high_values)):
        # Bar from low to baseline (negative effect)
        ax.barh(i, baseline - low, left=low, height=0.6,
                color=color_negative, alpha=0.8, edgecolor='white', linewidth=1)
        # Bar from baseline to high (positive effect)
        ax.barh(i, high - baseline, left=baseline, height=0.6,
                color=color_positive, alpha=0.8, edgecolor='white', linewidth=1)

        # Value annotations
        ax.annotate(f'{low:.1f}', (low - 0.5, i), ha='right', va='center',
                   fontsize=9, fontweight='bold')
        ax.annotate(f'{high:.1f}', (high + 0.5, i), ha='left', va='center',
                   fontsize=9, fontweight='bold')

    # Baseline vertical line
    ax.axvline(baseline, color='#2d3748', linestyle='--', linewidth=2,
               label=f'Baseline: {baseline:.1f}')

    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels(parameters, fontsize=11)
    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='lower right', fontsize=10)

    # Clean up
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    # Example: Olympic medal prediction sensitivity
    parameters = [
        "GDP per Capita (±20%)",
        "Sports Investment (±20%)",
        "Historical Performance (±20%)",
        "Host Advantage (±50%)",
        "Population (±20%)",
        "Climate Similarity (±30%)"
    ]

    baseline = 42.0  # Baseline prediction

    # Low and high values when each parameter changes
    low_values = [38.2, 39.5, 35.8, 40.1, 41.2, 41.0]
    high_values = [46.8, 44.5, 48.2, 48.9, 43.1, 43.5]

    create_tornado_diagram(
        parameters=parameters,
        low_values=low_values,
        high_values=high_values,
        baseline=baseline,
        output_path="model_1_sensitivity_tornado.png",
        title="Sensitivity Analysis: 2028 LA Medal Prediction",
        xlabel="Predicted Total Medals (USA)"
    )
```

**Caption Template**:
"Figure X: Tornado diagram reveals historical performance (±12.4 medals) and host advantage (±8.8 medals) as the two most influential parameters. GDP and sports investment show moderate sensitivity (±4-5 medals), while population has minimal impact, suggesting that *development intensity* matters more than *population size* for medal success."

---

## Template 2: Spider/Radar Plot (Multi-Parameter Sensitivity)

**Purpose**: Show how multiple parameters affect the output simultaneously on a radial plot.

**When to Use**:
- Comparing sensitivity profiles across scenarios
- Showing parameter balance/trade-offs
- Presenting multi-criteria decision analysis

```python
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_spider_plot(
    categories: list,
    scenarios: dict,
    output_path: str = "sensitivity_spider.png",
    title: str = "Multi-Parameter Sensitivity Profile"
):
    """
    Create a spider/radar plot for multi-parameter sensitivity.

    Parameters:
    -----------
    categories : list of str
        Parameter names (e.g., ["GDP", "Population", "Investment", ...])
    scenarios : dict
        {scenario_name: [values]} where values are normalized 0-1 or percentages
        Example: {"Baseline": [0.5, 0.6, 0.4, ...], "Optimistic": [0.8, 0.7, 0.6, ...]}
    output_path : str
        Path to save the figure
    title : str
        Figure title

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """

    n_params = len(categories)

    # Calculate angle for each parameter
    angles = [n / float(n_params) * 2 * pi for n in range(n_params)]
    angles += angles[:1]  # Complete the circle

    # Professional color palette
    colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5', '#ed8936']

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    for idx, (scenario_name, values) in enumerate(scenarios.items()):
        values_closed = values + values[:1]  # Complete the circle
        color = colors[idx % len(colors)]

        ax.plot(angles, values_closed, 'o-', linewidth=2,
                label=scenario_name, color=color, markersize=6)
        ax.fill(angles, values_closed, alpha=0.15, color=color)

    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11, fontweight='bold')

    # Styling
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.1), fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Set radial limits
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    categories = [
        "GDP Impact",
        "Population\nImpact",
        "Historical\nPerformance",
        "Investment\nLevel",
        "Host\nAdvantage",
        "Climate\nFactor"
    ]

    scenarios = {
        "Baseline": [0.50, 0.35, 0.80, 0.55, 0.40, 0.30],
        "Optimistic (+GDP)": [0.85, 0.40, 0.82, 0.70, 0.45, 0.35],
        "Pessimistic (-Invest)": [0.45, 0.30, 0.75, 0.25, 0.38, 0.28]
    }

    create_spider_plot(
        categories=categories,
        scenarios=scenarios,
        output_path="model_1_sensitivity_spider.png",
        title="Sensitivity Profile: USA 2028 Predictions"
    )
```

**Caption Template**:
"Figure X: Spider plot compares sensitivity profiles across three economic scenarios. The optimistic scenario (blue) shows amplified GDP impact (85% vs 50% baseline) propagating to investment levels, while the pessimistic scenario (red) reveals that reduced investment (-30%) disproportionately affects predicted performance despite stable historical factors."

---

## Template 3: Sensitivity Heatmap (Two-Parameter Interaction)

**Purpose**: Show how output varies across a 2D parameter grid, revealing interactions.

**When to Use**:
- Exploring parameter interactions
- Finding optimal parameter combinations
- Identifying threshold effects

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_sensitivity_heatmap(
    param1_values: np.ndarray,
    param2_values: np.ndarray,
    output_grid: np.ndarray,
    param1_name: str = "Parameter 1",
    param2_name: str = "Parameter 2",
    output_name: str = "Output",
    output_path: str = "sensitivity_heatmap.png",
    title: str = "Two-Parameter Sensitivity Analysis",
    baseline_point: tuple = None,
    contour_levels: list = None
):
    """
    Create a heatmap for two-parameter sensitivity analysis.

    Parameters:
    -----------
    param1_values : np.ndarray
        Values for x-axis parameter
    param2_values : np.ndarray
        Values for y-axis parameter
    output_grid : np.ndarray
        2D array of output values [len(param2), len(param1)]
    param1_name, param2_name : str
        Parameter labels
    output_name : str
        Colorbar label
    output_path : str
        Path to save figure
    title : str
        Figure title
    baseline_point : tuple (x, y)
        Coordinates of baseline scenario to highlight
    contour_levels : list
        Optional contour lines to draw

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    # Custom diverging colormap (blue-white-red)
    cmap = LinearSegmentedColormap.from_list(
        'sensitivity',
        ['#2c5282', '#90cdf4', '#ffffff', '#fed7aa', '#c05621']
    )

    # Create heatmap
    im = ax.imshow(output_grid, aspect='auto', origin='lower',
                   extent=[param1_values.min(), param1_values.max(),
                          param2_values.min(), param2_values.max()],
                   cmap=cmap, interpolation='bilinear')

    # Add contour lines if specified
    if contour_levels:
        X, Y = np.meshgrid(param1_values, param2_values)
        cs = ax.contour(X, Y, output_grid, levels=contour_levels,
                       colors='#2d3748', linewidths=1, linestyles='--')
        ax.clabel(cs, inline=True, fontsize=9, fmt='%.0f')

    # Highlight baseline point
    if baseline_point:
        ax.plot(baseline_point[0], baseline_point[1], 'ko', markersize=12,
               markerfacecolor='white', markeredgewidth=2,
               label=f'Baseline ({baseline_point[0]:.1f}, {baseline_point[1]:.1f})')
        ax.legend(loc='upper right', fontsize=10)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8, aspect=20)
    cbar.set_label(output_name, fontsize=11, fontweight='bold')

    # Labels and styling
    ax.set_xlabel(param1_name, fontsize=12, fontweight='bold')
    ax.set_ylabel(param2_name, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    # Create parameter grids
    gdp_range = np.linspace(-30, 30, 25)  # GDP change (%)
    invest_range = np.linspace(-30, 30, 25)  # Investment change (%)

    # Simulated output: medals as function of GDP and investment
    X, Y = np.meshgrid(gdp_range, invest_range)
    # Model: medals = 42 + 0.15*GDP + 0.12*Invest + 0.003*GDP*Invest
    output_grid = 42 + 0.15*X + 0.12*Y + 0.003*X*Y

    create_sensitivity_heatmap(
        param1_values=gdp_range,
        param2_values=invest_range,
        output_grid=output_grid,
        param1_name="GDP Change (%)",
        param2_name="Sports Investment Change (%)",
        output_name="Predicted Medals",
        output_path="model_1_sensitivity_heatmap.png",
        title="Two-Way Sensitivity: GDP × Investment Interaction",
        baseline_point=(0, 0),
        contour_levels=[35, 40, 45, 50]
    )
```

**Caption Template**:
"Figure X: Heatmap reveals synergistic interaction between GDP and investment: simultaneous +30% increases yield 52 medals (vs 42 baseline), exceeding the sum of individual effects (+4.5 + +3.6 = 50.1). The contour at 45 medals shows that high investment can compensate for moderate GDP decline, suggesting policy resilience up to -15% GDP."

---

## Template 4: Morris Screening Plot (Elementary Effects)

**Purpose**: Identify influential parameters using Morris method (screening for many parameters).

**When to Use**:
- Initial screening of 10+ parameters
- Distinguishing linear vs non-linear effects
- Computationally cheap global sensitivity

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_morris_plot(
    parameters: list,
    mu_star: list,
    sigma: list,
    output_path: str = "sensitivity_morris.png",
    title: str = "Morris Screening: Parameter Importance",
    threshold_mu: float = None,
    threshold_sigma: float = None
):
    """
    Create a Morris screening plot (μ* vs σ).

    Parameters:
    -----------
    parameters : list of str
        Parameter names
    mu_star : list of float
        Mean absolute elementary effect for each parameter
    sigma : list of float
        Standard deviation of elementary effect for each parameter
    output_path : str
        Path to save figure
    title : str
        Figure title
    threshold_mu : float
        Horizontal line for μ* importance threshold
    threshold_sigma : float
        Vertical line for σ interaction threshold

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects

    Interpretation:
    - High μ*, Low σ: Linear effect, influential
    - High μ*, High σ: Non-linear/interactive, influential
    - Low μ*, Low σ: Negligible effect
    - Low μ*, High σ: Interaction effect only
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    # Scatter plot with size based on importance
    sizes = np.array(mu_star) * 50 + 100
    colors = np.array(sigma)

    scatter = ax.scatter(sigma, mu_star, s=sizes, c=colors,
                        cmap='viridis', alpha=0.7, edgecolors='#2d3748', linewidth=1.5)

    # Add parameter labels
    for i, param in enumerate(parameters):
        ax.annotate(param, (sigma[i], mu_star[i]),
                   xytext=(5, 5), textcoords='offset points',
                   fontsize=9, fontweight='bold')

    # Threshold lines
    if threshold_mu:
        ax.axhline(threshold_mu, color='#e53e3e', linestyle='--',
                  linewidth=2, label=f'Importance threshold (μ*={threshold_mu})')
    if threshold_sigma:
        ax.axvline(threshold_sigma, color='#805ad5', linestyle='--',
                  linewidth=2, label=f'Interaction threshold (σ={threshold_sigma})')

    # Quadrant labels
    max_mu = max(mu_star) * 1.1
    max_sigma = max(sigma) * 1.1
    ax.text(max_sigma * 0.15, max_mu * 0.85, "Linear\nInfluential",
           ha='center', fontsize=10, style='italic', color='#276749')
    ax.text(max_sigma * 0.85, max_mu * 0.85, "Non-linear\nInfluential",
           ha='center', fontsize=10, style='italic', color='#c05621')
    ax.text(max_sigma * 0.15, max_mu * 0.15, "Negligible",
           ha='center', fontsize=10, style='italic', color='#718096')
    ax.text(max_sigma * 0.85, max_mu * 0.15, "Interaction\nOnly",
           ha='center', fontsize=10, style='italic', color='#805ad5')

    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label('σ (Variability)', fontsize=11)

    # Labels and styling
    ax.set_xlabel('σ (Standard Deviation of Elementary Effects)', fontsize=12, fontweight='bold')
    ax.set_ylabel('μ* (Mean Absolute Elementary Effect)', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, max_sigma)
    ax.set_ylim(0, max_mu)
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    parameters = [
        "GDP", "Population", "Investment", "Historical",
        "Host", "Climate", "Altitude", "Coach Quality",
        "Facilities", "Youth Programs", "Doping Control", "Media Coverage"
    ]

    # μ* = mean absolute elementary effect (higher = more influential)
    mu_star = [4.2, 1.8, 3.9, 5.1, 2.8, 0.9, 0.4, 2.1, 2.5, 1.2, 0.6, 0.3]

    # σ = standard deviation (higher = more non-linear/interactive)
    sigma = [1.5, 0.8, 2.2, 1.2, 3.1, 0.6, 0.3, 1.8, 1.4, 0.9, 0.5, 0.2]

    create_morris_plot(
        parameters=parameters,
        mu_star=mu_star,
        sigma=sigma,
        output_path="model_1_sensitivity_morris.png",
        title="Morris Screening: 12-Parameter Sensitivity",
        threshold_mu=2.0,
        threshold_sigma=1.5
    )
```

**Caption Template**:
"Figure X: Morris screening identifies 5 influential parameters (μ* > 2.0) from 12 candidates. Historical performance shows highest linear effect (μ*=5.1, σ=1.2), while host advantage exhibits strong interaction effects (μ*=2.8, σ=3.1), suggesting its impact depends on other factors. Altitude and media coverage fall below the negligibility threshold."

---

## Template 5: Sobol Indices Bar Chart

**Purpose**: Show decomposition of output variance into main effects and interactions.

**When to Use**:
- Quantitative attribution of uncertainty
- Distinguishing first-order vs total effects
- Communicating variance-based sensitivity to reviewers

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_sobol_plot(
    parameters: list,
    S1: list,
    ST: list,
    output_path: str = "sensitivity_sobol.png",
    title: str = "Sobol Sensitivity Indices",
    confidence_S1: list = None,
    confidence_ST: list = None
):
    """
    Create a Sobol indices bar chart (S1 and ST).

    Parameters:
    -----------
    parameters : list of str
        Parameter names
    S1 : list of float
        First-order Sobol indices (main effect)
    ST : list of float
        Total-order Sobol indices (main + all interactions)
    output_path : str
        Path to save figure
    title : str
        Figure title
    confidence_S1, confidence_ST : list of float
        95% confidence interval half-widths (optional)

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects

    Interpretation:
    - S1: Variance explained by parameter alone
    - ST: Variance explained by parameter + all its interactions
    - ST - S1: Interaction contribution
    - Sum(S1) < 1 indicates interactions are significant
    """

    n_params = len(parameters)
    x = np.arange(n_params)
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))

    # Colors
    color_s1 = '#4a90d9'  # Blue for first-order
    color_st = '#e53e3e'  # Red for total-order

    # Bars
    bars1 = ax.bar(x - width/2, S1, width, label='First-order (S₁)',
                   color=color_s1, edgecolor='white', linewidth=1)
    bars2 = ax.bar(x + width/2, ST, width, label='Total-order (Sᴛ)',
                   color=color_st, edgecolor='white', linewidth=1, alpha=0.8)

    # Error bars if confidence intervals provided
    if confidence_S1:
        ax.errorbar(x - width/2, S1, yerr=confidence_S1, fmt='none',
                   color='#2d3748', capsize=3, capthick=1)
    if confidence_ST:
        ax.errorbar(x + width/2, ST, yerr=confidence_ST, fmt='none',
                   color='#2d3748', capsize=3, capthick=1)

    # Add value labels on bars
    for bar, val in zip(bars1, S1):
        ax.annotate(f'{val:.2f}', (bar.get_x() + bar.get_width()/2, bar.get_height()),
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
    for bar, val in zip(bars2, ST):
        ax.annotate(f'{val:.2f}', (bar.get_x() + bar.get_width()/2, bar.get_height()),
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Reference line at 1.0
    ax.axhline(1.0, color='#718096', linestyle=':', linewidth=1, alpha=0.7)

    # Sum annotations
    sum_s1 = sum(S1)
    sum_st = sum(ST)
    ax.text(0.98, 0.98, f'ΣS₁ = {sum_s1:.2f}\nΣSᴛ = {sum_st:.2f}',
           transform=ax.transAxes, ha='right', va='top', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    # Labels and styling
    ax.set_xlabel('Parameters', fontsize=12, fontweight='bold')
    ax.set_ylabel('Sobol Index', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(parameters, rotation=45, ha='right', fontsize=10)
    ax.set_ylim(0, max(max(ST), 1.0) * 1.15)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', alpha=0.3)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    parameters = ["GDP", "Population", "Investment", "Historical", "Host", "Climate"]

    # First-order indices (main effect only)
    S1 = [0.25, 0.08, 0.22, 0.31, 0.05, 0.02]

    # Total-order indices (main + interactions)
    ST = [0.32, 0.12, 0.35, 0.38, 0.18, 0.05]

    # 95% confidence intervals (optional)
    conf_S1 = [0.03, 0.02, 0.04, 0.03, 0.02, 0.01]
    conf_ST = [0.04, 0.03, 0.05, 0.04, 0.03, 0.02]

    create_sobol_plot(
        parameters=parameters,
        S1=S1,
        ST=ST,
        output_path="model_1_sensitivity_sobol.png",
        title="Sobol Indices: Variance Decomposition",
        confidence_S1=conf_S1,
        confidence_ST=conf_ST
    )
```

**Caption Template**:
"Figure X: Sobol indices quantify variance attribution across 6 parameters. Historical performance dominates (S₁=0.31, Sᴛ=0.38), with 7% variance from interactions. The gap between Sᴛ and S₁ for Investment (0.35 vs 0.22) reveals significant 2nd-order effects, while Host advantage shows disproportionate interaction contribution (Sᴛ=0.18 vs S₁=0.05), consistent with the Morris screening results."

---

## Template 6: Parameter Sweep Line Plot

**Purpose**: Show how output changes across the full range of a single parameter.

**When to Use**:
- Exploring threshold effects
- Showing diminishing returns
- Comparing model behavior across parameter ranges

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_parameter_sweep(
    param_values: np.ndarray,
    outputs: dict,
    param_name: str = "Parameter",
    output_name: str = "Output",
    output_path: str = "sensitivity_sweep.png",
    title: str = "Parameter Sweep Analysis",
    baseline_value: float = None,
    shade_uncertainty: bool = True,
    uncertainty_low: dict = None,
    uncertainty_high: dict = None
):
    """
    Create a parameter sweep line plot.

    Parameters:
    -----------
    param_values : np.ndarray
        Values of the swept parameter
    outputs : dict
        {scenario_name: output_values} for each scenario/model
    param_name : str
        X-axis label
    output_name : str
        Y-axis label
    output_path : str
        Path to save figure
    title : str
        Figure title
    baseline_value : float
        Vertical line at baseline parameter value
    shade_uncertainty : bool
        Whether to shade uncertainty bands
    uncertainty_low, uncertainty_high : dict
        Lower and upper bounds for uncertainty shading

    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5', '#ed8936']

    for idx, (scenario, values) in enumerate(outputs.items()):
        color = colors[idx % len(colors)]
        ax.plot(param_values, values, '-', linewidth=2.5,
               label=scenario, color=color, marker='o', markersize=4)

        # Uncertainty shading
        if shade_uncertainty and uncertainty_low and uncertainty_high:
            if scenario in uncertainty_low and scenario in uncertainty_high:
                ax.fill_between(param_values,
                               uncertainty_low[scenario],
                               uncertainty_high[scenario],
                               alpha=0.2, color=color)

    # Baseline vertical line
    if baseline_value is not None:
        ax.axvline(baseline_value, color='#2d3748', linestyle='--',
                  linewidth=2, alpha=0.7, label=f'Baseline ({param_name}={baseline_value})')

    # Labels and styling
    ax.set_xlabel(param_name, fontsize=12, fontweight='bold')
    ax.set_ylabel(output_name, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    gdp_multiplier = np.linspace(0.5, 2.0, 20)

    outputs = {
        "Hurdle Model": 25 + 15 * np.log(gdp_multiplier + 0.5),
        "Hierarchical Model": 28 + 12 * gdp_multiplier ** 0.8,
        "Ensemble": 26 + 14 * np.sqrt(gdp_multiplier)
    }

    # Uncertainty bands (95% CI)
    uncertainty_low = {
        "Hurdle Model": outputs["Hurdle Model"] - 3,
        "Hierarchical Model": outputs["Hierarchical Model"] - 4,
        "Ensemble": outputs["Ensemble"] - 2.5
    }
    uncertainty_high = {
        "Hurdle Model": outputs["Hurdle Model"] + 3,
        "Hierarchical Model": outputs["Hierarchical Model"] + 4,
        "Ensemble": outputs["Ensemble"] + 2.5
    }

    create_parameter_sweep(
        param_values=gdp_multiplier,
        outputs=outputs,
        param_name="GDP Multiplier",
        output_name="Predicted Medals",
        output_path="model_1_sensitivity_sweep.png",
        title="GDP Sensitivity: Model Comparison",
        baseline_value=1.0,
        shade_uncertainty=True,
        uncertainty_low=uncertainty_low,
        uncertainty_high=uncertainty_high
    )
```

**Caption Template**:
"Figure X: Parameter sweep reveals diminishing returns above GDP multiplier 1.5× across all models. The Hurdle model (blue) shows log-linear response, predicting 42 medals at baseline but only 48 medals at 2× GDP (+14%), while the Hierarchical model exhibits steeper response at low GDP (critical for developing nations). Shaded regions represent 95% credible intervals."

---

## Naming Convention

Following the standardized format:

```
{model_number}_sensitivity_{type}.png
```

**Examples**:
- `model_1_sensitivity_tornado.png`
- `model_1_sensitivity_spider.png`
- `model_1_sensitivity_heatmap.png`
- `model_2_sensitivity_morris.png`
- `model_3_sensitivity_sobol.png`
- `model_0_sensitivity_sweep.png` (for overall model)

---

## Integration with Other Knowledge Base Files

- **Professional Styling**: See `professional_styling_guide.md` for color palettes
- **Rendering**: See `rendering_best_practices.md` for DPI and resolution
- **Captions**: Follow 4-element structure from `conceptual_figures_guide.md`

---

## Quality Checklist

Before submitting sensitivity figures:

- [ ] Baseline clearly marked (vertical line, highlighted point)
- [ ] Parameter ranges are realistic (check data)
- [ ] Units and scales labeled on all axes
- [ ] Color scheme consistent with other paper figures
- [ ] 300 DPI, minimum 2400px width
- [ ] Caption includes: observation, implication, story, takeaway
- [ ] Referenced in text before appearing

