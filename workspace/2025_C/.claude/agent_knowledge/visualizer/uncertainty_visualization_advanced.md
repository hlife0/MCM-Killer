# Advanced Uncertainty Visualization Templates

> **"Predictions without uncertainty are guesses. O-Prize papers distinguish themselves by showing *how confident* they are, not just *what* they predict."**

This guide provides copy-paste-ready Python templates for advanced uncertainty visualizations essential for Bayesian and probabilistic modeling in MCM papers.

---

## Overview: Uncertainty Figure Types

| Figure Type | Use Case | When to Use |
|-------------|----------|-------------|
| Monte Carlo Distribution | Simulation output analysis | After running MC simulations |
| Posterior Predictive Check | Bayesian model validation | Checking model fit to data |
| Uncertainty Decomposition | Epistemic vs Aleatoric | Understanding uncertainty sources |
| Prediction Interval Coverage | Interval accuracy assessment | Validating credible intervals |
| Fan Chart / Confidence Bands | Time series forecasting | Showing expanding uncertainty |
| Credible Interval Comparison | Multi-model comparison | Comparing uncertainty across models |

---

## Template 1: Monte Carlo Simulation Distribution

**Purpose**: Visualize the distribution of outcomes from Monte Carlo simulations.

**When to Use**:
- After running Monte Carlo simulations
- Showing outcome uncertainty
- Risk analysis and scenario planning

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_monte_carlo_distribution(
    samples: np.ndarray,
    output_path: str = "uncertainty_mc_distribution.png",
    title: str = "Monte Carlo Simulation Results",
    xlabel: str = "Outcome",
    ylabel: str = "Frequency",
    reference_value: float = None,
    percentiles: list = [5, 25, 50, 75, 95],
    n_simulations: int = None
):
    """
    Create a Monte Carlo distribution visualization.

    Parameters:
    -----------
    samples : np.ndarray
        MC simulation outcomes
    output_path : str
        Path to save figure
    title : str
        Figure title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    reference_value : float (optional)
        Reference line (e.g., baseline prediction)
    percentiles : list
        Percentiles to annotate
    n_simulations : int (optional)
        Number of simulations (for annotation)

    Returns:
    --------
    fig, ax : matplotlib figure and axis
    """

    fig, ax = plt.subplots(figsize=(12, 6))

    if n_simulations is None:
        n_simulations = len(samples)

    # Histogram
    n_bins = min(50, int(np.sqrt(len(samples))))
    counts, bins, patches = ax.hist(samples, bins=n_bins, density=True,
                                     alpha=0.6, color='#4a90d9',
                                     edgecolor='white', linewidth=0.5)

    # KDE overlay
    kde = stats.gaussian_kde(samples)
    x_range = np.linspace(samples.min(), samples.max(), 200)
    ax.plot(x_range, kde(x_range), color='#2c5282', linewidth=2.5, label='KDE')

    # Percentile lines
    colors_pct = ['#e53e3e', '#ed8936', '#38a169', '#ed8936', '#e53e3e']
    for i, pct in enumerate(percentiles):
        val = np.percentile(samples, pct)
        linestyle = '-' if pct == 50 else '--'
        linewidth = 2.5 if pct == 50 else 1.5
        ax.axvline(val, color=colors_pct[i], linestyle=linestyle,
                  linewidth=linewidth, alpha=0.8)
        ax.annotate(f'P{pct}: {val:.1f}', xy=(val, ax.get_ylim()[1] * 0.95),
                   xytext=(5, 0), textcoords='offset points',
                   fontsize=9, rotation=90, va='top')

    # Reference value
    if reference_value is not None:
        ax.axvline(reference_value, color='#805ad5', linestyle=':',
                  linewidth=2.5, label=f'Baseline: {reference_value:.1f}')

    # Shaded credible intervals
    p5, p95 = np.percentile(samples, [5, 95])
    ax.axvspan(p5, p95, alpha=0.15, color='#38a169', label='90% CI')

    p25, p75 = np.percentile(samples, [25, 75])
    ax.axvspan(p25, p75, alpha=0.15, color='#38a169')

    # Statistics box
    stats_text = (
        f"Monte Carlo Summary\n"
        f"{'─'*25}\n"
        f"N simulations: {n_simulations:,}\n"
        f"Mean: {np.mean(samples):.2f}\n"
        f"Median: {np.median(samples):.2f}\n"
        f"Std Dev: {np.std(samples):.2f}\n"
        f"90% CI: [{p5:.2f}, {p95:.2f}]\n"
        f"IQR: [{p25:.2f}, {p75:.2f}]"
    )
    ax.text(0.98, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', horizontalalignment='right',
           fontfamily='monospace',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, axis='y', alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    # Simulated MC output: medal count predictions
    samples = np.random.lognormal(mean=3.7, sigma=0.3, size=10000)

    create_monte_carlo_distribution(
        samples=samples,
        output_path="model_1_uncertainty_mc.png",
        title="Monte Carlo Simulation: 2028 LA Medal Predictions (USA)",
        xlabel="Predicted Total Medals",
        ylabel="Probability Density",
        reference_value=42,
        n_simulations=10000
    )
```

**Caption Template**:
"Figure X: Monte Carlo simulation (N=10,000) reveals right-skewed medal prediction distribution for USA in 2028. The median prediction (42 medals) exceeds the 2024 baseline (39 medals), but the 90% credible interval spans [35, 52], reflecting substantial uncertainty from GDP and investment scenarios. The long right tail suggests potential for exceptional performance under favorable conditions."

---

## Template 2: Posterior Predictive Check

**Purpose**: Compare model-generated data to observed data to validate model fit.

**When to Use**:
- After Bayesian model fitting
- Validating model adequacy
- Identifying model misspecification

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_posterior_predictive_check(
    y_observed: np.ndarray,
    y_replicated: np.ndarray,
    output_path: str = "uncertainty_ppc.png",
    title: str = "Posterior Predictive Check",
    n_samples_show: int = 50
):
    """
    Create a posterior predictive check visualization.

    Parameters:
    -----------
    y_observed : np.ndarray
        Observed data
    y_replicated : np.ndarray
        Shape (n_posterior_samples, n_observations) - replicated data from posterior
    output_path : str
        Path to save figure
    title : str
        Figure title
    n_samples_show : int
        Number of posterior samples to show in density overlay

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # ============ Panel 1: Density Overlay ============
    ax1 = axes[0, 0]

    # Plot subset of replicated densities
    sample_indices = np.random.choice(len(y_replicated), min(n_samples_show, len(y_replicated)), replace=False)
    for idx in sample_indices:
        try:
            kde = stats.gaussian_kde(y_replicated[idx])
            x_range = np.linspace(min(y_observed.min(), y_replicated.min()),
                                  max(y_observed.max(), y_replicated.max()), 100)
            ax1.plot(x_range, kde(x_range), color='#90cdf4', alpha=0.3, linewidth=0.5)
        except:
            pass

    # Observed data density
    kde_obs = stats.gaussian_kde(y_observed)
    x_range = np.linspace(y_observed.min(), y_observed.max(), 100)
    ax1.plot(x_range, kde_obs(x_range), color='#e53e3e', linewidth=3, label='Observed')

    ax1.set_xlabel('Value', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Density', fontsize=11, fontweight='bold')
    ax1.set_title('Density: Observed vs Replicated', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=10)
    ax1.grid(True, alpha=0.3)

    # ============ Panel 2: Test Statistic (Mean) ============
    ax2 = axes[0, 1]

    rep_means = np.mean(y_replicated, axis=1)
    obs_mean = np.mean(y_observed)

    ax2.hist(rep_means, bins=40, density=True, alpha=0.6, color='#4a90d9',
            edgecolor='white', label='Replicated Means')
    ax2.axvline(obs_mean, color='#e53e3e', linewidth=2.5, linestyle='--',
               label=f'Observed Mean: {obs_mean:.2f}')

    # p-value
    p_value = np.mean(rep_means >= obs_mean)
    p_value = min(p_value, 1 - p_value) * 2  # Two-tailed

    ax2.text(0.95, 0.95, f'Bayesian p-value: {p_value:.3f}',
            transform=ax2.transAxes, fontsize=10, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax2.set_xlabel('Mean', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Density', fontsize=11, fontweight='bold')
    ax2.set_title('Test Statistic: Mean', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3)

    # ============ Panel 3: Test Statistic (Std Dev) ============
    ax3 = axes[1, 0]

    rep_stds = np.std(y_replicated, axis=1)
    obs_std = np.std(y_observed)

    ax3.hist(rep_stds, bins=40, density=True, alpha=0.6, color='#38a169',
            edgecolor='white', label='Replicated Std Devs')
    ax3.axvline(obs_std, color='#e53e3e', linewidth=2.5, linestyle='--',
               label=f'Observed Std: {obs_std:.2f}')

    p_value_std = np.mean(rep_stds >= obs_std)
    p_value_std = min(p_value_std, 1 - p_value_std) * 2

    ax3.text(0.95, 0.95, f'Bayesian p-value: {p_value_std:.3f}',
            transform=ax3.transAxes, fontsize=10, ha='right', va='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax3.set_xlabel('Standard Deviation', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Density', fontsize=11, fontweight='bold')
    ax3.set_title('Test Statistic: Std Dev', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper left', fontsize=10)
    ax3.grid(True, alpha=0.3)

    # ============ Panel 4: Quantile Coverage ============
    ax4 = axes[1, 1]

    # Calculate empirical quantiles at various levels
    quantile_levels = np.linspace(0.05, 0.95, 19)
    observed_coverage = []

    for q in quantile_levels:
        rep_quantiles = np.percentile(y_replicated, q * 100, axis=1)
        coverage = np.mean(y_observed[:, None] <= rep_quantiles, axis=0).mean()
        observed_coverage.append(coverage)

    ax4.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Ideal')
    ax4.plot(quantile_levels, observed_coverage, 'o-', color='#4a90d9',
            linewidth=2, markersize=6, label='Observed')
    ax4.fill_between(quantile_levels, quantile_levels - 0.1, quantile_levels + 0.1,
                    alpha=0.2, color='#38a169', label='±10% band')

    ax4.set_xlabel('Theoretical Quantile', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Empirical Coverage', fontsize=11, fontweight='bold')
    ax4.set_title('Quantile Coverage', fontsize=12, fontweight='bold')
    ax4.legend(loc='lower right', fontsize=10)
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_aspect('equal')
    ax4.grid(True, alpha=0.3)

    fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    # Observed data
    y_observed = np.random.poisson(15, 100)

    # Replicated data from posterior (1000 posterior samples, 100 observations each)
    y_replicated = np.random.poisson(
        np.random.gamma(15, 1, 1000)[:, None],
        size=(1000, 100)
    )

    create_posterior_predictive_check(
        y_observed=y_observed,
        y_replicated=y_replicated,
        output_path="model_2_uncertainty_ppc.png",
        title="Posterior Predictive Check: Hierarchical Model"
    )
```

**Caption Template**:
"Figure X: Posterior predictive check confirms model adequacy. (Top-left) Replicated data densities (blue, N=50 shown) envelope the observed density (red), indicating good distributional fit. (Top-right, Bottom-left) Bayesian p-values for mean (0.47) and standard deviation (0.52) are well within [0.1, 0.9], showing no systematic misspecification. (Bottom-right) Quantile coverage tracks the diagonal, confirming calibrated prediction intervals."

---

## Template 3: Uncertainty Decomposition (Epistemic vs Aleatoric)

**Purpose**: Separate reducible (epistemic) from irreducible (aleatoric) uncertainty.

**When to Use**:
- Understanding uncertainty sources
- Guiding data collection strategy
- Communicating model limitations

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_uncertainty_decomposition(
    x_values: np.ndarray,
    y_mean: np.ndarray,
    epistemic_std: np.ndarray,
    aleatoric_std: np.ndarray,
    y_observed: np.ndarray = None,
    x_observed: np.ndarray = None,
    output_path: str = "uncertainty_decomposition.png",
    title: str = "Uncertainty Decomposition",
    xlabel: str = "Predictor",
    ylabel: str = "Outcome"
):
    """
    Create uncertainty decomposition visualization.

    Parameters:
    -----------
    x_values : np.ndarray
        X-axis values for prediction
    y_mean : np.ndarray
        Mean predictions
    epistemic_std : np.ndarray
        Standard deviation from model uncertainty (reducible)
    aleatoric_std : np.ndarray
        Standard deviation from data noise (irreducible)
    y_observed, x_observed : np.ndarray (optional)
        Observed data points
    output_path : str
        Path to save figure
    title : str
        Figure title
    xlabel, ylabel : str
        Axis labels

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    total_std = np.sqrt(epistemic_std**2 + aleatoric_std**2)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # ============ Left Panel: Stacked Uncertainty ============
    ax1 = axes[0]

    # Mean prediction
    ax1.plot(x_values, y_mean, color='#2c5282', linewidth=2.5, label='Mean Prediction')

    # Epistemic uncertainty (inner band) - reducible
    ax1.fill_between(x_values,
                     y_mean - 1.96 * epistemic_std,
                     y_mean + 1.96 * epistemic_std,
                     alpha=0.4, color='#805ad5', label='Epistemic (Model) ±1.96σ')

    # Total uncertainty (outer band) - includes aleatoric
    ax1.fill_between(x_values,
                     y_mean - 1.96 * total_std,
                     y_mean + 1.96 * total_std,
                     alpha=0.2, color='#ed8936', label='Total ±1.96σ')

    # Observed points
    if y_observed is not None and x_observed is not None:
        ax1.scatter(x_observed, y_observed, s=30, color='#e53e3e',
                   alpha=0.6, edgecolor='white', label='Observed', zorder=5)

    ax1.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax1.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax1.set_title('Prediction with Decomposed Uncertainty', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(True, alpha=0.3)

    # ============ Right Panel: Variance Breakdown ============
    ax2 = axes[1]

    epistemic_var = epistemic_std**2
    aleatoric_var = aleatoric_std**2
    total_var = total_std**2

    # Stacked area
    ax2.fill_between(x_values, 0, epistemic_var, alpha=0.7,
                     color='#805ad5', label='Epistemic (Reducible)')
    ax2.fill_between(x_values, epistemic_var, total_var, alpha=0.7,
                     color='#ed8936', label='Aleatoric (Irreducible)')

    # Proportion annotation
    mean_epistemic_ratio = np.mean(epistemic_var / total_var) * 100
    mean_aleatoric_ratio = 100 - mean_epistemic_ratio

    ax2.text(0.95, 0.95,
            f'Average Breakdown:\n'
            f'  Epistemic: {mean_epistemic_ratio:.1f}%\n'
            f'  Aleatoric: {mean_aleatoric_ratio:.1f}%',
            transform=ax2.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax2.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax2.set_ylabel('Variance', fontsize=12, fontweight='bold')
    ax2.set_title('Variance Decomposition', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3)

    fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    # Predictor values (e.g., GDP)
    x_values = np.linspace(0, 100, 100)

    # Mean prediction
    y_mean = 20 + 0.3 * x_values

    # Epistemic uncertainty: higher at extremes (less data)
    epistemic_std = 2 + 3 * np.exp(-((x_values - 50)**2) / 1000)
    epistemic_std = 5 - 0.03 * np.abs(x_values - 50)  # Higher at edges
    epistemic_std = np.clip(epistemic_std, 1, 10)

    # Aleatoric uncertainty: constant noise
    aleatoric_std = np.ones_like(x_values) * 4

    # Observed data
    x_observed = np.random.uniform(10, 90, 50)
    y_observed = 20 + 0.3 * x_observed + np.random.normal(0, 4, 50)

    create_uncertainty_decomposition(
        x_values=x_values,
        y_mean=y_mean,
        epistemic_std=epistemic_std,
        aleatoric_std=aleatoric_std,
        y_observed=y_observed,
        x_observed=x_observed,
        output_path="model_1_uncertainty_decomposition.png",
        title="Uncertainty Decomposition: Medal Prediction by GDP",
        xlabel="GDP per Capita ($1000s)",
        ylabel="Predicted Medals"
    )
```

**Caption Template**:
"Figure X: Uncertainty decomposition reveals that 62% of prediction variance is aleatoric (irreducible data noise) while 38% is epistemic (model uncertainty). The epistemic component increases at GDP extremes where training data is sparse, suggesting targeted data collection for very high/low GDP countries could reduce total uncertainty by up to 38%. The orange band represents the irreducible minimum prediction interval."

---

## Template 4: Prediction Interval Coverage Plot

**Purpose**: Assess whether credible intervals have correct coverage probability.

**When to Use**:
- Validating interval predictions
- Calibration assessment
- Comparing interval methods

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_coverage_plot(
    nominal_levels: np.ndarray,
    observed_coverage: dict,
    output_path: str = "uncertainty_coverage.png",
    title: str = "Prediction Interval Coverage"
):
    """
    Create a prediction interval coverage plot.

    Parameters:
    -----------
    nominal_levels : np.ndarray
        Array of nominal coverage levels (e.g., [0.5, 0.8, 0.9, 0.95])
    observed_coverage : dict
        {model_name: array of observed coverages at each nominal level}
    output_path : str
        Path to save figure
    title : str
        Figure title

    Returns:
    --------
    fig, ax : matplotlib figure and axis
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5', '#ed8936']

    # Perfect calibration line
    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Perfect Calibration', zorder=1)

    # Tolerance band (±5%)
    ax.fill_between([0, 1], [0-0.05, 1-0.05], [0+0.05, 1+0.05],
                   alpha=0.15, color='#38a169', label='±5% tolerance')

    # Each model
    for i, (model_name, coverages) in enumerate(observed_coverage.items()):
        ax.plot(nominal_levels, coverages, 'o-', color=colors[i % len(colors)],
               linewidth=2, markersize=10, label=model_name)

        # Annotate deviations
        for j, (nom, obs) in enumerate(zip(nominal_levels, coverages)):
            diff = obs - nom
            if abs(diff) > 0.05:  # Significant deviation
                ax.annotate(f'{diff:+.0%}', (nom, obs),
                           xytext=(5, 5), textcoords='offset points',
                           fontsize=8, color=colors[i % len(colors)])

    # Summary statistics
    summary_text = "Coverage Summary:\n"
    for model_name, coverages in observed_coverage.items():
        mean_abs_error = np.mean(np.abs(coverages - nominal_levels))
        calibration = "Well-calibrated" if mean_abs_error < 0.03 else "Under-confident" if np.mean(coverages) > np.mean(nominal_levels) else "Over-confident"
        summary_text += f"  {model_name}: MAE={mean_abs_error:.3f} ({calibration})\n"

    ax.text(0.02, 0.98, summary_text, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', fontfamily='monospace',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax.set_xlabel('Nominal Coverage Level', fontsize=12, fontweight='bold')
    ax.set_ylabel('Observed Coverage', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlim(0.4, 1.0)
    ax.set_ylim(0.4, 1.0)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    nominal_levels = np.array([0.50, 0.80, 0.90, 0.95, 0.99])

    observed_coverage = {
        "Hurdle Model": np.array([0.52, 0.78, 0.88, 0.93, 0.97]),
        "Hierarchical Bayes": np.array([0.51, 0.81, 0.91, 0.95, 0.98]),
        "Bootstrap": np.array([0.48, 0.74, 0.85, 0.91, 0.95])
    }

    create_coverage_plot(
        nominal_levels=nominal_levels,
        observed_coverage=observed_coverage,
        output_path="model_0_uncertainty_coverage.png",
        title="Prediction Interval Coverage: Model Comparison"
    )
```

**Caption Template**:
"Figure X: Coverage plot reveals the Hierarchical Bayesian model achieves near-perfect calibration (MAE=0.008), with observed coverage matching nominal levels at all confidence levels. The Bootstrap method is over-confident at higher levels (95% nominal yields only 91% coverage), producing narrower-than-warranted intervals. The Hurdle model shows slight under-coverage at 99% (-2%)."

---

## Template 5: Fan Chart (Expanding Uncertainty Bands)

**Purpose**: Show how uncertainty grows over prediction horizon.

**When to Use**:
- Time series forecasting
- Multi-step ahead predictions
- Communicating forecast degradation

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_fan_chart(
    time_history: np.ndarray,
    y_history: np.ndarray,
    time_forecast: np.ndarray,
    y_forecast_mean: np.ndarray,
    y_forecast_intervals: dict,
    output_path: str = "uncertainty_fan_chart.png",
    title: str = "Forecast with Uncertainty Bands",
    xlabel: str = "Time",
    ylabel: str = "Value"
):
    """
    Create a fan chart showing expanding uncertainty over forecast horizon.

    Parameters:
    -----------
    time_history : np.ndarray
        Historical time points
    y_history : np.ndarray
        Historical values
    time_forecast : np.ndarray
        Forecast time points
    y_forecast_mean : np.ndarray
        Mean forecast
    y_forecast_intervals : dict
        {confidence_level: (lower_bound, upper_bound)}
        e.g., {0.50: (lower, upper), 0.80: (lower, upper), 0.95: (lower, upper)}
    output_path : str
        Path to save figure
    title : str
        Figure title
    xlabel, ylabel : str
        Axis labels

    Returns:
    --------
    fig, ax : matplotlib figure and axis
    """

    fig, ax = plt.subplots(figsize=(14, 6))

    # Color gradient for bands (darker = narrower interval)
    colors = {
        0.50: '#2c5282',
        0.80: '#4a90d9',
        0.90: '#90cdf4',
        0.95: '#bee3f8',
        0.99: '#e6f3ff'
    }

    # Historical data
    ax.plot(time_history, y_history, 'o-', color='#2d3748', linewidth=2,
           markersize=4, label='Historical', zorder=5)

    # Forecast bands (widest first for proper layering)
    sorted_levels = sorted(y_forecast_intervals.keys(), reverse=True)
    for level in sorted_levels:
        lower, upper = y_forecast_intervals[level]
        color = colors.get(level, '#90cdf4')
        ax.fill_between(time_forecast, lower, upper, alpha=0.4,
                       color=color, label=f'{int(level*100)}% CI', zorder=1)

    # Mean forecast
    ax.plot(time_forecast, y_forecast_mean, '-', color='#e53e3e',
           linewidth=2.5, label='Forecast Mean', zorder=4)

    # Forecast start line
    ax.axvline(time_history[-1], color='#718096', linestyle=':', linewidth=1.5)
    ax.annotate('Forecast Start', xy=(time_history[-1], ax.get_ylim()[1] * 0.95),
               xytext=(-5, 0), textcoords='offset points',
               ha='right', fontsize=9, style='italic')

    # Uncertainty growth annotation
    if 0.95 in y_forecast_intervals:
        lower95, upper95 = y_forecast_intervals[0.95]
        initial_width = upper95[0] - lower95[0]
        final_width = upper95[-1] - lower95[-1]
        growth = (final_width / initial_width - 1) * 100

        ax.annotate(f'95% CI width\ngrows {growth:.0f}%',
                   xy=(time_forecast[-1], (upper95[-1] + lower95[-1])/2),
                   xytext=(10, 0), textcoords='offset points',
                   fontsize=9, va='center',
                   arrowprops=dict(arrowstyle='->', color='#718096'))

    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    # Historical data (Olympics 2000-2024)
    time_history = np.array([2000, 2004, 2008, 2012, 2016, 2020, 2024])
    y_history = np.array([36, 38, 40, 42, 46, 38, 40])

    # Forecast (2028, 2032, 2036)
    time_forecast = np.array([2024, 2028, 2032, 2036])
    y_forecast_mean = np.array([40, 44, 46, 48])

    # Expanding uncertainty
    base_std = np.array([0, 3, 5, 8])
    y_forecast_intervals = {
        0.50: (y_forecast_mean - 0.67 * base_std, y_forecast_mean + 0.67 * base_std),
        0.80: (y_forecast_mean - 1.28 * base_std, y_forecast_mean + 1.28 * base_std),
        0.95: (y_forecast_mean - 1.96 * base_std, y_forecast_mean + 1.96 * base_std)
    }

    create_fan_chart(
        time_history=time_history,
        y_history=y_history,
        time_forecast=time_forecast,
        y_forecast_mean=y_forecast_mean,
        y_forecast_intervals=y_forecast_intervals,
        output_path="model_1_uncertainty_fan_chart.png",
        title="USA Medal Forecast: 2024-2036",
        xlabel="Olympic Year",
        ylabel="Total Medals"
    )
```

**Caption Template**:
"Figure X: Fan chart projects USA medal trajectory with expanding uncertainty. The 95% prediction interval widens from ±6 medals (2028) to ±16 medals (2036), representing 167% growth in uncertainty over the 12-year horizon. The mean forecast of 48 medals by 2036 requires favorable GDP and investment scenarios; the lower 95% bound (32 medals) represents pessimistic conditions."

---

## Template 6: Credible Interval Comparison

**Purpose**: Compare uncertainty estimates across models or scenarios.

**When to Use**:
- Model comparison
- Scenario analysis
- Sensitivity to assumptions

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_credible_interval_comparison(
    categories: list,
    estimates: dict,
    output_path: str = "uncertainty_ci_comparison.png",
    title: str = "Credible Interval Comparison",
    xlabel: str = "Value",
    show_overlap: bool = True
):
    """
    Create a credible interval comparison plot (forest plot style).

    Parameters:
    -----------
    categories : list
        Category labels (e.g., country names, model names)
    estimates : dict
        {model_name: {'mean': array, 'lower': array, 'upper': array}}
    output_path : str
        Path to save figure
    title : str
        Figure title
    xlabel : str
        X-axis label
    show_overlap : bool
        Whether to highlight overlapping intervals

    Returns:
    --------
    fig, ax : matplotlib figure and axis
    """

    n_categories = len(categories)
    n_models = len(estimates)

    fig, ax = plt.subplots(figsize=(12, max(6, n_categories * 0.4)))

    colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5', '#ed8936']
    y_positions = np.arange(n_categories)

    # Spacing for multiple models
    total_height = 0.7
    bar_height = total_height / n_models

    for i, (model_name, data) in enumerate(estimates.items()):
        offset = (i - n_models/2 + 0.5) * bar_height
        y_pos = y_positions + offset

        # Error bars
        xerr_lower = data['mean'] - data['lower']
        xerr_upper = data['upper'] - data['mean']

        ax.errorbar(data['mean'], y_pos, xerr=[xerr_lower, xerr_upper],
                   fmt='o', color=colors[i % len(colors)],
                   markersize=8, capsize=5, capthick=2,
                   linewidth=2, label=model_name)

        # Value annotations
        for j, (mean, lower, upper) in enumerate(zip(data['mean'], data['lower'], data['upper'])):
            ax.annotate(f'{mean:.1f} [{lower:.1f}, {upper:.1f}]',
                       xy=(upper + 1, y_pos[j]), fontsize=8, va='center')

    # Reference line at 0 or mean
    ax.axvline(0, color='#718096', linestyle=':', linewidth=1, alpha=0.5)

    # Identify non-overlapping intervals
    if show_overlap and n_models >= 2:
        model_names = list(estimates.keys())
        for j in range(n_categories):
            intervals = [(estimates[m]['lower'][j], estimates[m]['upper'][j]) for m in model_names]
            # Check if first and second model overlap
            if len(intervals) >= 2:
                overlap = not (intervals[0][1] < intervals[1][0] or intervals[1][1] < intervals[0][0])
                if not overlap:
                    ax.annotate('*', xy=(max(intervals[0][1], intervals[1][1]), y_positions[j]),
                               fontsize=16, color='#e53e3e', fontweight='bold', va='center')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(categories, fontsize=10)
    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, axis='x', alpha=0.3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    categories = ["USA", "China", "Russia", "UK", "Germany",
                  "Japan", "France", "Australia", "Italy", "Brazil"]

    estimates = {
        "Hurdle Model": {
            'mean': np.array([42, 45, 28, 32, 25, 22, 18, 20, 15, 8]),
            'lower': np.array([36, 38, 22, 26, 19, 17, 13, 15, 10, 4]),
            'upper': np.array([48, 52, 34, 38, 31, 27, 23, 25, 20, 12])
        },
        "Hierarchical Bayes": {
            'mean': np.array([44, 43, 30, 30, 27, 20, 20, 18, 16, 10]),
            'lower': np.array([39, 37, 25, 25, 22, 16, 16, 14, 12, 6]),
            'upper': np.array([49, 49, 35, 35, 32, 24, 24, 22, 20, 14])
        }
    }

    create_credible_interval_comparison(
        categories=categories,
        estimates=estimates,
        output_path="model_0_uncertainty_ci_comparison.png",
        title="2028 Medal Predictions: Model Comparison",
        xlabel="Predicted Total Medals"
    )
```

**Caption Template**:
"Figure X: Forest plot compares 95% credible intervals from two models across top 10 countries. The models agree on USA (overlapping 36-49 range) but diverge significantly for China and Russia (marked with *), where the Hierarchical model predicts 5-7 fewer medals. Interval widths are comparable, averaging ±8 medals, indicating similar uncertainty quantification despite mean differences."

---

## Naming Convention

Following the standardized format:

```
{model_number}_uncertainty_{type}.png
```

**Examples**:
- `model_1_uncertainty_mc.png`
- `model_2_uncertainty_ppc.png`
- `model_1_uncertainty_decomposition.png`
- `model_0_uncertainty_coverage.png`
- `model_1_uncertainty_fan_chart.png`
- `model_0_uncertainty_ci_comparison.png`

---

## Integration with Other Knowledge Base Files

- **Professional Styling**: See `professional_styling_guide.md` for color palettes
- **Rendering**: See `rendering_best_practices.md` for DPI and resolution
- **Sensitivity**: See `sensitivity_analysis_templates.md` for parameter uncertainty
- **Validation**: See `model_validation_figures.md` for convergence diagnostics
- **Captions**: Follow 4-element structure from `conceptual_figures_guide.md`

---

## Quality Checklist

Before submitting uncertainty figures:

- [ ] Intervals clearly labeled (50%, 80%, 95%, etc.)
- [ ] Legend explains all shaded regions
- [ ] Reference lines included (baseline, zero, perfect calibration)
- [ ] Coverage statistics calculated and annotated
- [ ] 300 DPI, minimum 2400px width
- [ ] Color scheme consistent with other figures
- [ ] Caption includes: what uncertainty represents, magnitude, implications

