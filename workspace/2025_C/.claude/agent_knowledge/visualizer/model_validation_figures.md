# Model Validation Visualization Templates

> **"Validation figures prove your model works. Without residual diagnostics, convergence plots, and calibration checks, judges will question every prediction you make."**

This guide provides copy-paste-ready Python templates for model validation visualizations essential for MCM papers.

---

## Overview: Validation Figure Types

| Figure Type | Use Case | When to Use |
|-------------|----------|-------------|
| Residual Diagnostic 4-Panel | Regression model validation | Every regression model |
| MCMC Trace/Convergence | Bayesian model validation | All MCMC-based models |
| Cross-Validation Performance | Model comparison | Holdout/k-fold validation |
| Calibration Plot | Probabilistic predictions | Any model with probabilities |
| Learning Curve | Model complexity tuning | Training vs validation gap |
| Prediction vs Observed | Point prediction accuracy | Final model validation |

---

## Template 1: Residual Diagnostic 4-Panel

**Purpose**: Comprehensive residual analysis in a single figure (Q-Q, residuals vs fitted, scale-location, leverage).

**When to Use**:
- After fitting ANY regression model
- Required for establishing model assumptions
- Essential for linear/GLM models

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import warnings

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_residual_diagnostics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    leverage: np.ndarray = None,
    output_path: str = "validation_residuals.png",
    model_name: str = "Model"
):
    """
    Create a 4-panel residual diagnostic plot.

    Parameters:
    -----------
    y_true : np.ndarray
        Actual values
    y_pred : np.ndarray
        Predicted values
    leverage : np.ndarray (optional)
        Leverage values for each observation (from hat matrix diagonal)
    output_path : str
        Path to save figure
    model_name : str
        Model name for title

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    residuals = y_true - y_pred
    standardized_residuals = (residuals - np.mean(residuals)) / np.std(residuals)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Color scheme
    point_color = '#4a90d9'
    line_color = '#e53e3e'
    highlight_color = '#ed8936'

    # ============ Panel 1: Residuals vs Fitted ============
    ax1 = axes[0, 0]
    ax1.scatter(y_pred, residuals, alpha=0.6, color=point_color, edgecolor='white', s=50)
    ax1.axhline(0, color=line_color, linestyle='--', linewidth=2)

    # Lowess smoothing line
    try:
        from statsmodels.nonparametric.smoothers_lowess import lowess
        smoothed = lowess(residuals, y_pred, frac=0.3)
        ax1.plot(smoothed[:, 0], smoothed[:, 1], color=highlight_color, linewidth=2, label='LOWESS')
        ax1.legend(loc='upper right')
    except:
        pass

    ax1.set_xlabel('Fitted Values', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Residuals', fontsize=11, fontweight='bold')
    ax1.set_title('Residuals vs Fitted', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # ============ Panel 2: Q-Q Plot ============
    ax2 = axes[0, 1]
    (osm, osr), (slope, intercept, r) = stats.probplot(standardized_residuals, dist="norm")
    ax2.scatter(osm, osr, alpha=0.6, color=point_color, edgecolor='white', s=50)
    ax2.plot(osm, slope * osm + intercept, color=line_color, linewidth=2, label=f'R² = {r**2:.3f}')

    ax2.set_xlabel('Theoretical Quantiles', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Sample Quantiles', fontsize=11, fontweight='bold')
    ax2.set_title('Normal Q-Q Plot', fontsize=12, fontweight='bold')
    ax2.legend(loc='lower right')
    ax2.grid(True, alpha=0.3)

    # ============ Panel 3: Scale-Location ============
    ax3 = axes[1, 0]
    sqrt_std_residuals = np.sqrt(np.abs(standardized_residuals))
    ax3.scatter(y_pred, sqrt_std_residuals, alpha=0.6, color=point_color, edgecolor='white', s=50)

    # Lowess smoothing
    try:
        smoothed = lowess(sqrt_std_residuals, y_pred, frac=0.3)
        ax3.plot(smoothed[:, 0], smoothed[:, 1], color=highlight_color, linewidth=2, label='LOWESS')
        ax3.legend(loc='upper right')
    except:
        pass

    ax3.set_xlabel('Fitted Values', fontsize=11, fontweight='bold')
    ax3.set_ylabel('√|Standardized Residuals|', fontsize=11, fontweight='bold')
    ax3.set_title('Scale-Location (Homoscedasticity)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)

    # ============ Panel 4: Residuals vs Leverage ============
    ax4 = axes[1, 1]

    if leverage is None:
        # Approximate leverage if not provided
        n = len(y_pred)
        leverage = np.ones(n) / n + (y_pred - np.mean(y_pred))**2 / np.sum((y_pred - np.mean(y_pred))**2)

    ax4.scatter(leverage, standardized_residuals, alpha=0.6, color=point_color, edgecolor='white', s=50)
    ax4.axhline(0, color='#718096', linestyle='--', linewidth=1)

    # Cook's distance contours
    n = len(y_pred)
    p = 2  # Approximate number of parameters
    for cook_d in [0.5, 1.0]:
        x_range = np.linspace(0.001, max(leverage) * 1.1, 100)
        y_pos = np.sqrt(cook_d * p * (1 - x_range) / x_range)
        y_neg = -y_pos
        ax4.plot(x_range, y_pos, color=line_color, linestyle=':', linewidth=1.5,
                label=f"Cook's D = {cook_d}" if cook_d == 0.5 else None)
        ax4.plot(x_range, y_neg, color=line_color, linestyle=':', linewidth=1.5)

    # Highlight high-leverage points
    high_leverage = leverage > 2 * p / n
    high_influence = np.abs(standardized_residuals) > 2
    influential = high_leverage & high_influence
    if np.any(influential):
        ax4.scatter(leverage[influential], standardized_residuals[influential],
                   s=150, facecolors='none', edgecolors=line_color, linewidth=2,
                   label=f'Influential ({np.sum(influential)})')

    ax4.set_xlabel('Leverage', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Standardized Residuals', fontsize=11, fontweight='bold')
    ax4.set_title('Residuals vs Leverage', fontsize=12, fontweight='bold')
    ax4.legend(loc='upper right', fontsize=9)
    ax4.grid(True, alpha=0.3)

    # Overall title
    fig.suptitle(f'{model_name}: Residual Diagnostics', fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)
    n = 200

    # Simulated data
    x = np.random.uniform(0, 10, n)
    y_true = 2 * x + 5 + np.random.normal(0, 2, n)
    y_pred = 2 * x + 5  # Perfect fit + noise

    create_residual_diagnostics(
        y_true=y_true,
        y_pred=y_pred,
        output_path="model_1_validation_residuals.png",
        model_name="Hurdle Model"
    )
```

**Caption Template**:
"Figure X: Residual diagnostics for the Hurdle model reveal well-behaved residuals. (Top-left) Residuals vs fitted shows random scatter around zero with no systematic pattern. (Top-right) Q-Q plot confirms approximate normality (R²=0.987). (Bottom-left) Scale-location plot indicates constant variance (homoscedasticity). (Bottom-right) No points exceed Cook's D=1.0, indicating absence of influential outliers."

---

## Template 2: MCMC Trace and Convergence Plots

**Purpose**: Visualize MCMC chain behavior and convergence diagnostics.

**When to Use**:
- All Bayesian models using MCMC
- After running NUTS, Metropolis-Hastings, or Gibbs sampling
- Essential for establishing posterior validity

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_mcmc_diagnostics(
    chains: dict,
    output_path: str = "validation_mcmc.png",
    model_name: str = "Bayesian Model",
    n_params: int = 4
):
    """
    Create MCMC convergence diagnostic plots.

    Parameters:
    -----------
    chains : dict
        {param_name: np.ndarray of shape (n_chains, n_samples)}
    output_path : str
        Path to save figure
    model_name : str
        Model name for title
    n_params : int
        Number of parameters to show (top n_params)

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    param_names = list(chains.keys())[:n_params]
    n_rows = len(param_names)

    fig, axes = plt.subplots(n_rows, 3, figsize=(14, 3 * n_rows))

    # Colors for different chains
    chain_colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5']

    for i, param in enumerate(param_names):
        samples = chains[param]  # Shape: (n_chains, n_samples)

        if samples.ndim == 1:
            samples = samples.reshape(1, -1)

        n_chains, n_samples = samples.shape

        # ============ Column 1: Trace Plot ============
        ax1 = axes[i, 0] if n_rows > 1 else axes[0]
        for chain_idx in range(n_chains):
            ax1.plot(samples[chain_idx], alpha=0.7,
                    color=chain_colors[chain_idx % len(chain_colors)],
                    linewidth=0.5, label=f'Chain {chain_idx+1}')

        ax1.set_xlabel('Iteration', fontsize=10)
        ax1.set_ylabel(param, fontsize=10, fontweight='bold')
        ax1.set_title('Trace Plot', fontsize=11, fontweight='bold')
        if i == 0:
            ax1.legend(loc='upper right', fontsize=8, ncol=2)
        ax1.grid(True, alpha=0.3)

        # ============ Column 2: Posterior Distribution ============
        ax2 = axes[i, 1] if n_rows > 1 else axes[1]
        all_samples = samples.flatten()
        ax2.hist(all_samples, bins=50, density=True, alpha=0.7,
                color='#4a90d9', edgecolor='white', linewidth=0.5)

        # KDE overlay
        kde_x = np.linspace(all_samples.min(), all_samples.max(), 200)
        kde = stats.gaussian_kde(all_samples)
        ax2.plot(kde_x, kde(kde_x), color='#e53e3e', linewidth=2, label='KDE')

        # Mean and 95% CI
        mean_val = np.mean(all_samples)
        ci_low, ci_high = np.percentile(all_samples, [2.5, 97.5])
        ax2.axvline(mean_val, color='#2d3748', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.3f}')
        ax2.axvspan(ci_low, ci_high, alpha=0.2, color='#38a169', label=f'95% CI: [{ci_low:.3f}, {ci_high:.3f}]')

        ax2.set_xlabel(param, fontsize=10)
        ax2.set_ylabel('Density', fontsize=10)
        ax2.set_title('Posterior Distribution', fontsize=11, fontweight='bold')
        ax2.legend(loc='upper right', fontsize=8)
        ax2.grid(True, alpha=0.3)

        # ============ Column 3: R-hat and ESS ============
        ax3 = axes[i, 2] if n_rows > 1 else axes[2]

        # Calculate R-hat (Gelman-Rubin diagnostic)
        if n_chains > 1:
            chain_means = np.mean(samples, axis=1)
            chain_vars = np.var(samples, axis=1, ddof=1)
            W = np.mean(chain_vars)  # Within-chain variance
            B = np.var(chain_means, ddof=1) * n_samples  # Between-chain variance
            var_hat = (1 - 1/n_samples) * W + (1/n_samples) * B
            r_hat = np.sqrt(var_hat / W) if W > 0 else 1.0
        else:
            r_hat = np.nan

        # Calculate ESS (simplified)
        def ess_simple(x):
            n = len(x)
            if n < 10:
                return n
            acf_vals = np.correlate(x - np.mean(x), x - np.mean(x), mode='full')
            acf_vals = acf_vals[n-1:] / acf_vals[n-1]
            # Sum until first negative autocorrelation
            cutoff = np.where(acf_vals < 0)[0]
            cutoff = cutoff[0] if len(cutoff) > 0 else len(acf_vals)
            tau = 1 + 2 * np.sum(acf_vals[1:cutoff])
            return n / tau

        ess = ess_simple(all_samples)

        # Display metrics as text
        ax3.axis('off')
        metrics_text = (
            f"Convergence Diagnostics\n"
            f"{'='*30}\n\n"
            f"R-hat: {r_hat:.4f}\n"
            f"{'✓ PASS' if r_hat < 1.1 else '✗ FAIL'} (threshold: < 1.1)\n\n"
            f"ESS: {ess:.0f}\n"
            f"{'✓ PASS' if ess > 400 else '⚠ LOW' if ess > 100 else '✗ FAIL'} (threshold: > 400)\n\n"
            f"ESS/sample: {ess/n_samples:.1%}\n\n"
            f"Mean: {mean_val:.4f}\n"
            f"Std: {np.std(all_samples):.4f}\n"
            f"95% CI: [{ci_low:.4f}, {ci_high:.4f}]"
        )

        # Color based on convergence
        text_color = '#276749' if (r_hat < 1.1 and ess > 400) else '#c05621' if ess > 100 else '#c53030'
        ax3.text(0.5, 0.5, metrics_text, transform=ax3.transAxes,
                fontsize=10, verticalalignment='center', horizontalalignment='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='#f7fafc', edgecolor=text_color, linewidth=2))

    # Overall title
    fig.suptitle(f'{model_name}: MCMC Convergence Diagnostics', fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    # Simulated MCMC chains (4 chains, 2000 samples each)
    n_chains, n_samples = 4, 2000

    chains = {
        'β₀ (Intercept)': np.random.normal(5.0, 0.3, (n_chains, n_samples)) + \
                          np.random.normal(0, 0.1, (n_chains, 1)),  # Add chain-specific offset
        'β₁ (GDP)': np.random.normal(0.15, 0.02, (n_chains, n_samples)),
        'β₂ (Population)': np.random.normal(0.08, 0.01, (n_chains, n_samples)),
        'σ (Error SD)': np.abs(np.random.normal(2.0, 0.2, (n_chains, n_samples)))
    }

    create_mcmc_diagnostics(
        chains=chains,
        output_path="model_2_validation_mcmc.png",
        model_name="Hierarchical Bayesian Model"
    )
```

**Caption Template**:
"Figure X: MCMC convergence diagnostics confirm reliable posterior estimation. All four parameters achieve R-hat < 1.1 (range: 1.001-1.003), indicating between-chain convergence. Effective sample sizes exceed 1,000 for all parameters (ESS/sample > 25%), ensuring stable credible interval estimation. Trace plots show well-mixed chains with no drift or stickiness."

---

## Template 3: Cross-Validation Performance Plot

**Purpose**: Show model performance across CV folds with comparison.

**When to Use**:
- K-fold or leave-one-out cross-validation
- Comparing multiple models
- Demonstrating generalization

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_cv_performance_plot(
    models: dict,
    output_path: str = "validation_cv.png",
    metric_name: str = "RMSE",
    title: str = "Cross-Validation Performance",
    lower_is_better: bool = True
):
    """
    Create cross-validation performance comparison plot.

    Parameters:
    -----------
    models : dict
        {model_name: list of fold scores}
    output_path : str
        Path to save figure
    metric_name : str
        Name of the metric (e.g., "RMSE", "R²", "MAE")
    title : str
        Figure title
    lower_is_better : bool
        True if lower metric is better (for coloring best model)

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    model_names = list(models.keys())
    n_models = len(model_names)
    n_folds = len(list(models.values())[0])

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Colors
    colors = ['#4a90d9', '#e53e3e', '#38a169', '#805ad5', '#ed8936']

    # ============ Left Panel: Box Plot ============
    ax1 = axes[0]

    box_data = [models[name] for name in model_names]
    bp = ax1.boxplot(box_data, patch_artist=True, labels=model_names)

    # Color boxes
    for i, (box, median) in enumerate(zip(bp['boxes'], bp['medians'])):
        box.set_facecolor(colors[i % len(colors)])
        box.set_alpha(0.6)
        median.set_color('#2d3748')
        median.set_linewidth(2)

    # Individual points
    for i, name in enumerate(model_names):
        x = np.random.normal(i + 1, 0.04, len(models[name]))
        ax1.scatter(x, models[name], alpha=0.5, color=colors[i % len(colors)],
                   edgecolor='white', s=30, zorder=3)

    # Mean markers
    for i, name in enumerate(model_names):
        mean_val = np.mean(models[name])
        ax1.scatter(i + 1, mean_val, marker='D', s=100, color='#2d3748',
                   edgecolor='white', linewidth=2, zorder=4)

    ax1.set_ylabel(metric_name, fontsize=12, fontweight='bold')
    ax1.set_title(f'{metric_name} Distribution by Model', fontsize=12, fontweight='bold')
    ax1.grid(True, axis='y', alpha=0.3)

    # Highlight best model
    mean_scores = {name: np.mean(scores) for name, scores in models.items()}
    if lower_is_better:
        best_model = min(mean_scores, key=mean_scores.get)
    else:
        best_model = max(mean_scores, key=mean_scores.get)

    best_idx = model_names.index(best_model)
    ax1.get_xticklabels()[best_idx].set_fontweight('bold')
    ax1.get_xticklabels()[best_idx].set_color('#276749')

    # ============ Right Panel: Fold-by-Fold ============
    ax2 = axes[1]

    x = np.arange(1, n_folds + 1)
    width = 0.8 / n_models

    for i, name in enumerate(model_names):
        offset = (i - n_models/2 + 0.5) * width
        bars = ax2.bar(x + offset, models[name], width, label=name,
                      color=colors[i % len(colors)], alpha=0.8, edgecolor='white')

    ax2.set_xlabel('Fold', fontsize=12, fontweight='bold')
    ax2.set_ylabel(metric_name, fontsize=12, fontweight='bold')
    ax2.set_title(f'{metric_name} by Cross-Validation Fold', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(True, axis='y', alpha=0.3)

    # Summary statistics text
    summary = "Model Summary:\n"
    for name in model_names:
        mean = np.mean(models[name])
        std = np.std(models[name])
        marker = " ★" if name == best_model else ""
        summary += f"  {name}: {mean:.3f} ± {std:.3f}{marker}\n"

    ax2.text(0.02, 0.98, summary, transform=ax2.transAxes, fontsize=9,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096', alpha=0.9))

    fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    models = {
        "Baseline Poisson": np.random.normal(8.5, 1.2, 10),
        "Hurdle Model": np.random.normal(5.2, 0.8, 10),
        "Hierarchical Bayes": np.random.normal(4.8, 0.6, 10),
        "Ensemble": np.random.normal(4.5, 0.5, 10)
    }

    create_cv_performance_plot(
        models=models,
        output_path="model_0_validation_cv.png",
        metric_name="RMSE (Medals)",
        title="10-Fold Cross-Validation: Model Comparison",
        lower_is_better=True
    )
```

**Caption Template**:
"Figure X: 10-fold cross-validation reveals consistent ensemble superiority (RMSE: 4.5 ± 0.5) over baseline Poisson (8.5 ± 1.2), representing a 47% error reduction. The ensemble shows minimal fold-to-fold variance (CV=11%), indicating robust generalization. Hierarchical Bayes performs comparably (4.8 ± 0.6) but with higher computational cost."

---

## Template 4: Calibration Plot (Reliability Diagram)

**Purpose**: Show whether predicted probabilities match observed frequencies.

**When to Use**:
- Any model producing probabilities
- Classification or probability predictions
- Essential for decision-making credibility

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_calibration_plot(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    n_bins: int = 10,
    output_path: str = "validation_calibration.png",
    title: str = "Calibration Plot",
    model_name: str = "Model"
):
    """
    Create a calibration/reliability diagram.

    Parameters:
    -----------
    y_true : np.ndarray
        Binary outcomes (0/1)
    y_prob : np.ndarray
        Predicted probabilities
    n_bins : int
        Number of calibration bins
    output_path : str
        Path to save figure
    title : str
        Figure title
    model_name : str
        Model name for legend

    Returns:
    --------
    fig, axes : matplotlib figure and axes
    """

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # ============ Left Panel: Calibration Curve ============
    ax1 = axes[0]

    # Bin the predictions
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    bin_means = []
    bin_true_fracs = []
    bin_counts = []

    for i in range(n_bins):
        mask = (y_prob >= bin_edges[i]) & (y_prob < bin_edges[i+1])
        if i == n_bins - 1:  # Include right edge for last bin
            mask = (y_prob >= bin_edges[i]) & (y_prob <= bin_edges[i+1])

        if np.sum(mask) > 0:
            bin_means.append(np.mean(y_prob[mask]))
            bin_true_fracs.append(np.mean(y_true[mask]))
            bin_counts.append(np.sum(mask))
        else:
            bin_means.append(bin_centers[i])
            bin_true_fracs.append(np.nan)
            bin_counts.append(0)

    bin_means = np.array(bin_means)
    bin_true_fracs = np.array(bin_true_fracs)
    bin_counts = np.array(bin_counts)

    # Perfect calibration line
    ax1.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Perfect Calibration')

    # Calibration curve
    valid = ~np.isnan(bin_true_fracs)
    ax1.plot(bin_means[valid], bin_true_fracs[valid], 'o-',
            color='#4a90d9', linewidth=2, markersize=8, label=model_name)

    # Confidence band (using binomial SE)
    for i in range(len(bin_means)):
        if bin_counts[i] > 0:
            se = np.sqrt(bin_true_fracs[i] * (1 - bin_true_fracs[i]) / bin_counts[i])
            ax1.errorbar(bin_means[i], bin_true_fracs[i], yerr=1.96*se,
                        color='#4a90d9', alpha=0.3, capsize=3)

    # Calculate calibration error
    valid_mask = bin_counts > 0
    ece = np.sum(bin_counts[valid_mask] * np.abs(bin_true_fracs[valid_mask] - bin_means[valid_mask])) / np.sum(bin_counts)
    mce = np.max(np.abs(bin_true_fracs[valid_mask] - bin_means[valid_mask]))

    ax1.text(0.05, 0.95, f'ECE = {ece:.3f}\nMCE = {mce:.3f}',
            transform=ax1.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax1.set_xlabel('Mean Predicted Probability', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Fraction of Positives', fontsize=11, fontweight='bold')
    ax1.set_title('Calibration Curve', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right', fontsize=10)
    ax1.set_xlim(-0.02, 1.02)
    ax1.set_ylim(-0.02, 1.02)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')

    # ============ Right Panel: Prediction Distribution ============
    ax2 = axes[1]

    ax2.hist(y_prob[y_true == 0], bins=20, alpha=0.6, color='#e53e3e',
            label='Actual: No Medal', density=True, edgecolor='white')
    ax2.hist(y_prob[y_true == 1], bins=20, alpha=0.6, color='#38a169',
            label='Actual: Medal', density=True, edgecolor='white')

    ax2.set_xlabel('Predicted Probability', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Density', fontsize=11, fontweight='bold')
    ax2.set_title('Prediction Distribution by Outcome', fontsize=12, fontweight='bold')
    ax2.legend(loc='upper center', fontsize=10)
    ax2.grid(True, alpha=0.3)

    fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, axes


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)
    n = 500

    # Simulated probabilities and outcomes
    y_prob = np.random.beta(2, 2, n)  # Predicted probabilities
    y_true = (np.random.random(n) < y_prob).astype(int)  # Well-calibrated outcomes

    create_calibration_plot(
        y_true=y_true,
        y_prob=y_prob,
        output_path="model_1_validation_calibration.png",
        title="Hurdle Model: Probability Calibration",
        model_name="Hurdle Model"
    )
```

**Caption Template**:
"Figure X: Calibration plot confirms well-calibrated probability estimates (ECE=0.023). Points closely follow the diagonal, indicating that when the model predicts 60% medal probability, approximately 60% of such countries actually win medals. The prediction distribution (right) shows good separation between medal-winners (green) and non-winners (red), with minimal overlap at intermediate probabilities."

---

## Template 5: Learning Curve

**Purpose**: Show training vs validation performance across training set sizes.

**When to Use**:
- Diagnosing overfitting vs underfitting
- Determining if more data would help
- Model complexity tuning

```python
import matplotlib.pyplot as plt
import numpy as np

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_learning_curve(
    train_sizes: np.ndarray,
    train_scores: np.ndarray,
    val_scores: np.ndarray,
    output_path: str = "validation_learning_curve.png",
    metric_name: str = "Score",
    title: str = "Learning Curve",
    higher_is_better: bool = True
):
    """
    Create a learning curve plot.

    Parameters:
    -----------
    train_sizes : np.ndarray
        Training set sizes
    train_scores : np.ndarray
        Shape (n_sizes, n_cv_folds) - training scores
    val_scores : np.ndarray
        Shape (n_sizes, n_cv_folds) - validation scores
    output_path : str
        Path to save figure
    metric_name : str
        Name of the metric
    title : str
        Figure title
    higher_is_better : bool
        True if higher metric is better

    Returns:
    --------
    fig, ax : matplotlib figure and axis
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)

    # Training curve
    ax.plot(train_sizes, train_mean, 'o-', color='#4a90d9', linewidth=2,
           markersize=8, label='Training Score')
    ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std,
                   alpha=0.2, color='#4a90d9')

    # Validation curve
    ax.plot(train_sizes, val_mean, 's-', color='#e53e3e', linewidth=2,
           markersize=8, label='Validation Score')
    ax.fill_between(train_sizes, val_mean - val_std, val_mean + val_std,
                   alpha=0.2, color='#e53e3e')

    # Diagnosis annotations
    gap = train_mean[-1] - val_mean[-1]
    if higher_is_better:
        if gap > 0.1:  # Large gap = overfitting
            diagnosis = "⚠ Overfitting: Large train-val gap"
            color = '#c05621'
        elif val_mean[-1] < 0.7:  # Low overall = underfitting
            diagnosis = "⚠ Underfitting: Low overall performance"
            color = '#c05621'
        else:
            diagnosis = "✓ Good fit: Converging curves"
            color = '#276749'
    else:  # Lower is better (like RMSE)
        gap = val_mean[-1] - train_mean[-1]
        if gap > 0.1:
            diagnosis = "⚠ Overfitting: Large train-val gap"
            color = '#c05621'
        else:
            diagnosis = "✓ Good fit: Converging curves"
            color = '#276749'

    ax.text(0.98, 0.02, diagnosis, transform=ax.transAxes, fontsize=11,
           ha='right', va='bottom', fontweight='bold', color=color,
           bbox=dict(boxstyle='round', facecolor='white', edgecolor=color))

    # Final metrics annotation
    ax.annotate(f'Final Gap: {abs(gap):.3f}',
               xy=(train_sizes[-1], (train_mean[-1] + val_mean[-1])/2),
               xytext=(train_sizes[-1] * 0.85, (train_mean[-1] + val_mean[-1])/2),
               fontsize=10, ha='right',
               arrowprops=dict(arrowstyle='->', color='#718096'))

    ax.set_xlabel('Training Set Size', fontsize=12, fontweight='bold')
    ax.set_ylabel(metric_name, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Set reasonable y limits
    all_scores = np.concatenate([train_mean, val_mean])
    ax.set_ylim(min(all_scores) * 0.9, max(all_scores) * 1.1)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)

    train_sizes = np.array([100, 200, 400, 800, 1600, 3200, 6400])
    n_folds = 5

    # Simulated scores (converging curves)
    train_scores = 0.95 - 0.15 / np.sqrt(train_sizes[:, None]) + np.random.normal(0, 0.02, (len(train_sizes), n_folds))
    val_scores = 0.90 - 0.25 / np.sqrt(train_sizes[:, None]) + np.random.normal(0, 0.03, (len(train_sizes), n_folds))

    create_learning_curve(
        train_sizes=train_sizes,
        train_scores=train_scores,
        val_scores=val_scores,
        output_path="model_1_validation_learning_curve.png",
        metric_name="R² Score",
        title="Learning Curve: Hierarchical Model",
        higher_is_better=True
    )
```

**Caption Template**:
"Figure X: Learning curve shows converging training and validation scores, indicating good model fit without overfitting. The final training-validation gap of 0.03 (R²: 0.93 vs 0.90) is within acceptable bounds. Validation score plateaus at N≈3,200, suggesting diminishing returns from additional data. The shaded bands represent ±1 standard deviation across 5-fold CV."

---

## Template 6: Prediction vs Observed Plot

**Purpose**: Direct comparison of predicted vs actual values.

**When to Use**:
- Final model validation
- Point prediction accuracy assessment
- Identifying systematic biases

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Try SciencePlots if available
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('seaborn-v0_8-whitegrid')

def create_pred_vs_obs_plot(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_pred_lower: np.ndarray = None,
    y_pred_upper: np.ndarray = None,
    labels: list = None,
    highlight_indices: list = None,
    output_path: str = "validation_pred_obs.png",
    title: str = "Predicted vs Observed",
    xlabel: str = "Observed",
    ylabel: str = "Predicted"
):
    """
    Create predicted vs observed scatter plot with optional credible intervals.

    Parameters:
    -----------
    y_true : np.ndarray
        Observed values
    y_pred : np.ndarray
        Predicted values (point estimates)
    y_pred_lower, y_pred_upper : np.ndarray (optional)
        Lower and upper bounds of prediction intervals
    labels : list (optional)
        Labels for each point (e.g., country names)
    highlight_indices : list (optional)
        Indices of points to highlight and label
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

    fig, ax = plt.subplots(figsize=(10, 10))

    # Perfect prediction line
    min_val = min(min(y_true), min(y_pred))
    max_val = max(max(y_true), max(y_pred))
    margin = (max_val - min_val) * 0.05
    ax.plot([min_val - margin, max_val + margin], [min_val - margin, max_val + margin],
           'k--', linewidth=2, label='Perfect Prediction', zorder=1)

    # Error bars if intervals provided
    if y_pred_lower is not None and y_pred_upper is not None:
        for i in range(len(y_true)):
            ax.plot([y_true[i], y_true[i]], [y_pred_lower[i], y_pred_upper[i]],
                   color='#90cdf4', linewidth=1, alpha=0.5, zorder=2)

    # Main scatter
    colors = plt.cm.viridis(np.abs(y_pred - y_true) / max(np.abs(y_pred - y_true)))
    scatter = ax.scatter(y_true, y_pred, c=np.abs(y_pred - y_true),
                        cmap='viridis_r', s=60, alpha=0.7, edgecolor='white',
                        linewidth=0.5, zorder=3)

    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label('Absolute Error', fontsize=10)

    # Highlight specific points
    if highlight_indices is not None and labels is not None:
        for idx in highlight_indices:
            ax.scatter(y_true[idx], y_pred[idx], s=150, facecolors='none',
                      edgecolors='#e53e3e', linewidth=2, zorder=4)
            ax.annotate(labels[idx], (y_true[idx], y_pred[idx]),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=9, fontweight='bold')

    # Regression line through points
    slope, intercept, r_value, p_value, std_err = stats.linregress(y_true, y_pred)
    fit_line = slope * np.array([min_val, max_val]) + intercept
    ax.plot([min_val, max_val], fit_line, color='#e53e3e', linewidth=2,
           linestyle=':', label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')

    # Calculate metrics
    rmse = np.sqrt(np.mean((y_pred - y_true)**2))
    mae = np.mean(np.abs(y_pred - y_true))
    r2 = r_value**2

    # Coverage if intervals provided
    if y_pred_lower is not None and y_pred_upper is not None:
        coverage = np.mean((y_true >= y_pred_lower) & (y_true <= y_pred_upper))
        metrics_text = f'R² = {r2:.3f}\nRMSE = {rmse:.2f}\nMAE = {mae:.2f}\n95% CI Coverage = {coverage:.1%}'
    else:
        metrics_text = f'R² = {r2:.3f}\nRMSE = {rmse:.2f}\nMAE = {mae:.2f}'

    ax.text(0.05, 0.95, metrics_text, transform=ax.transAxes, fontsize=11,
           verticalalignment='top', fontfamily='monospace',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#718096'))

    ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlim(min_val - margin, max_val + margin)
    ax.set_ylim(min_val - margin, max_val + margin)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    return fig, ax


# EXAMPLE USAGE
if __name__ == "__main__":
    np.random.seed(42)
    n = 50

    # Simulated data
    y_true = np.random.uniform(0, 100, n)
    y_pred = y_true + np.random.normal(0, 8, n)
    y_pred_lower = y_pred - 15
    y_pred_upper = y_pred + 15

    labels = [f"Country_{i}" for i in range(n)]
    highlight_indices = [np.argmax(np.abs(y_pred - y_true)),  # Largest error
                        np.argmax(y_true)]  # Highest value

    create_pred_vs_obs_plot(
        y_true=y_true,
        y_pred=y_pred,
        y_pred_lower=y_pred_lower,
        y_pred_upper=y_pred_upper,
        labels=labels,
        highlight_indices=highlight_indices,
        output_path="model_1_validation_pred_obs.png",
        title="2024 Paris Olympics: Predicted vs Observed Medals",
        xlabel="Observed Medals",
        ylabel="Predicted Medals"
    )
```

**Caption Template**:
"Figure X: Predicted vs observed medal counts show strong agreement (R²=0.89, RMSE=6.2 medals). Points cluster tightly around the perfect prediction line (dashed), with color intensity indicating prediction error. The 95% credible intervals achieve 93% coverage, slightly below nominal but within acceptable bounds. Two outliers are highlighted: Country_23 (largest underprediction) and Country_47 (highest medal count)."

---

## Naming Convention

Following the standardized format:

```
{model_number}_validation_{type}.png
```

**Examples**:
- `model_1_validation_residuals.png`
- `model_2_validation_mcmc.png`
- `model_0_validation_cv.png`
- `model_1_validation_calibration.png`
- `model_1_validation_learning_curve.png`
- `model_1_validation_pred_obs.png`

---

## Quality Checklist

Before submitting validation figures:

- [ ] All diagnostics pass thresholds (R-hat < 1.1, ESS > 400, etc.)
- [ ] Metrics clearly annotated on figure
- [ ] Reference lines included (perfect prediction, thresholds)
- [ ] Caption explains what PASS/FAIL means
- [ ] 300 DPI, minimum 2400px width
- [ ] Color scheme consistent with other figures
- [ ] Caption includes observation, implication, takeaway

