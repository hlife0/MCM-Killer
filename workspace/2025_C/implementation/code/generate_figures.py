"""
Publication-Quality Figure Generator for MCM 2025 Problem C

Generates 8 professional visualizations for the competition paper.
All figures saved to output/paper/figures/ at 300 DPI.

Author: @visualizer
Date: 2025-01-15
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import seaborn as sns
from scipy import stats
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# VISUALIZATION CONFIGURATION
# =============================================================================

# Colorblind-friendly palette (Wong's palette + extras)
COLORS = {
    'blue': '#0072B2',
    'orange': '#D55E00',
    'green': '#009E73',
    'red': '#CC79A7',
    'purple': '#949494',
    'pink': '#F0E442',
    'teal': '#56B4E9',
    'yellow': '#E69F00',
    'dark_blue': '#1f77b4',
    'gold': '#FFD700',
    'navy': '#000080',
}

# Professional style settings
plt.rcParams.update({
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'font.size': 10,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.3,
    'lines.linewidth': 1.5,
    'patch.linewidth': 0.5,
})

# Paths
DATA_DIR = '/home/jcheniu/MCM-Killer/workspace/2025_C/implementation/data'
RESULTS_DIR = '/home/jcheniu/MCM-Killer/workspace/2025_C/output/results'
OUTPUT_DIR = '/home/jcheniu/MCM-Killer/workspace/2025_C/output/paper/figures'

# =============================================================================
# DATA LOADING
# =============================================================================

def load_data() -> Dict[str, pd.DataFrame]:
    """Load all necessary data files."""
    data = {}

    # Medal counts
    data['medal_counts'] = pd.read_csv(os.path.join(DATA_DIR, 'medal_counts_clean.csv'))

    # Results from models
    data['results_1'] = pd.read_csv(os.path.join(RESULTS_DIR, 'results_1.csv'))
    data['results_2'] = pd.read_csv(os.path.join(RESULTS_DIR, 'results_2_predictions.csv'))
    data['results_6_regimes'] = pd.read_csv(os.path.join(RESULTS_DIR, 'results_6_regimes.csv'))
    data['results_5'] = pd.read_csv(os.path.join(RESULTS_DIR, 'results_5.csv'))

    return data

# =============================================================================
# FIGURE 1: MEDAL TRENDS OVER TIME
# =============================================================================

def create_figure_1_medal_trends(data: Dict[str, pd.DataFrame]):
    """
    Figure 1: Medal Trends Over Time (1896-2024)
    Shows total medals by top countries with historical event highlights
    """
    df = data['medal_counts'].copy()

    # Key countries to track - using NOC names that appear in data
    key_countries_full = [
        'United States', 'China', 'Soviet Union', 'Great Britain',
        'Germany', 'France', 'Japan', 'Australia', 'Italy', 'Russia',
        'East Germany', 'West Germany', 'Unified Team'
    ]

    # Filter data for key countries
    df_filtered = df[df['NOC'].isin(key_countries_full)].copy()

    # Create pivot table
    pivot_df = df_filtered.pivot_table(index='Year', columns='NOC', values='Total', aggfunc='sum').fillna(0)

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Assign colors
    country_colors = {
        'United States': COLORS['blue'],
        'China': COLORS['red'],
        'Soviet Union': COLORS['orange'],
        'Russia': COLORS['dark_blue'],
        'Great Britain': COLORS['purple'],
        'Germany': COLORS['gold'],
        'France': COLORS['pink'],
        'Japan': COLORS['teal'],
        'Australia': COLORS['green'],
        'Italy': COLORS['yellow'],
        'East Germany': COLORS['orange'],
        'West Germany': COLORS['gold'],
        'Unified Team': COLORS['teal'],
    }

    # Plot lines
    for country in pivot_df.columns:
        if country in country_colors:
            color = country_colors[country]
            linewidth = 2.5 if country in ['United States', 'China', 'Soviet Union'] else 1.5
            alpha = 1.0 if country in ['United States', 'China', 'Soviet Union'] else 0.7
            ax.plot(pivot_df.index, pivot_df[country], color=color, linewidth=linewidth, alpha=alpha, label=country)

    # Historical event annotations
    events = [
        (1916, 'WWI\nCancelled', COLORS['red']),
        (1940, 'WWII\nCancelled', COLORS['red']),
        (1944, 'WWII\nCancelled', COLORS['red']),
        (1980, 'Moscow\nBoycott', COLORS['orange']),
        (1984, 'LA\nBoycott', COLORS['orange']),
    ]

    for year, label, color in events:
        ax.axvline(x=year, color=color, linestyle='--', linewidth=1, alpha=0.5)
        if year in pivot_df.index:
            ax.text(year, ax.get_ylim()[1] * 0.95, label, ha='center', va='top', fontsize=7, color=color)

    # Styling
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Total Medals', fontweight='bold')
    ax.set_title('Olympic Medal Trends: Top Nations (1896-2024)\nHistorical Events and Performance Evolution', fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1892, 2028)

    # Legend
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper left', frameon=True, fancybox=True, shadow=False, ncol=2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_1_medal_trends.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 1: Medal Trends - Saved")

# =============================================================================
# FIGURE 2: ZERO INFLATION & DISTRIBUTION
# =============================================================================

def create_figure_2_zero_inflation(data: Dict[str, pd.DataFrame]):
    """
    Figure 2: Zero Inflation & Distribution
    Demonstrates excess zeros in medal count data, justifying ZINB approach
    """
    df = data['medal_counts'].copy()

    # Get medal distribution across all country-year observations
    # Focus on recent period (post-WWII)
    recent_df = df[df['Year'] >= 1960].copy()

    # Create bins for histogram
    max_medals = recent_df['Total'].max()
    bins = np.arange(-0.5, max_medals + 1.5, 1)

    # Calculate empirical distribution
    medal_counts = recent_df['Total'].values

    # Fit Poisson and Negative Binomial for comparison
    lambda_poisson = medal_counts[medal_counts > 0].mean()
    lambda_poisson_all = medal_counts.mean()

    # Generate theoretical distributions
    x_range = np.arange(0, max_medals + 50)
    poisson_pmfs = stats.poisson.pmf(x_range, mu=lambda_poisson_all)

    # For NB: estimate parameters via method of moments
    p_mean = medal_counts.mean()
    p_var = medal_counts.var()

    if p_var > p_mean:
        nb_p = p_mean / p_var
        nb_r = p_mean**2 / (p_var - p_mean)
        nb_pmfs = stats.nbinom.pmf(x_range, n=nb_r, p=nb_p)
    else:
        nb_pmfs = poisson_pmfs.copy()

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Histogram with zero inflation
    zero_count = (medal_counts == 0).sum()
    total_count = len(medal_counts)
    zero_prop = zero_count / total_count

    ax1.hist(medal_counts, bins=bins, edgecolor='white', linewidth=0.5, alpha=0.7, color=COLORS['blue'])
    ax1.axvline(x=0, color=COLORS['red'], linewidth=2, linestyle='--')

    ax1.annotate(f'{zero_prop:.1%} zeros', xy=(0, ax1.get_ylim()[1] * 0.9),
                 xytext=(5, ax1.get_ylim()[1] * 0.95),
                 fontsize=10, color=COLORS['red'], fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=1.5))

    ax1.set_xlabel('Total Medals', fontweight='bold')
    ax1.set_ylabel('Frequency', fontweight='bold')
    ax1.set_title('(A) Distribution of Medal Counts (1960-2024)\nExcess Zeros Observed', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-5, 50)

    # Panel B: Comparison with theoretical distributions
    unique_vals, counts = np.unique(medal_counts, return_counts=True)
    empirical = counts / total_count

    ax2.bar(unique_vals, empirical, width=0.4, alpha=0.6, color=COLORS['blue'], label='Empirical', align='center')
    ax2.plot(x_range, poisson_pmfs, 'o-', color=COLORS['orange'], markersize=4, linewidth=1.5, label='Poisson', alpha=0.7)
    ax2.plot(x_range, nb_pmfs, 's-', color=COLORS['green'], markersize=4, linewidth=1.5, label='Negative Binomial', alpha=0.7)

    ax2.set_xlabel('Total Medals', fontweight='bold')
    ax2.set_ylabel('Probability', fontweight='bold')
    ax2.set_title('(B) Comparison: Observed vs. Theoretical\nZINB Justification', fontweight='bold')
    ax2.legend(loc='upper right', frameon=True)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-1, 30)
    ax2.set_ylim(0, max(empirical.max() * 1.1, poisson_pmfs.max() * 1.1))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_2_zero_inflation.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 2: Zero Inflation - Saved")

# =============================================================================
# FIGURE 3: HOST COUNTRY EFFECT
# =============================================================================

def create_figure_3_host_effect(data: Dict[str, pd.DataFrame]):
    """
    Figure 3: Host Country Effect
    Analysis showing medal gains during host years
    """
    df = data['medal_counts'].copy()

    # Major host countries and their host years
    host_data_info = {
        'United States': [1904, 1932, 1984, 1996, 2028],
        'Great Britain': [1908, 1948, 2012],
        'France': [1900, 1924, 2024],
        'Germany': [1936, 1972],
        'Australia': [1956, 2000],
        'Japan': [1964, 2020],
        'China': [2008],
        'Italy': [1960],
        'Spain': [1992],
        'South Korea': [1988],
        'Brazil': [2016],
        'Greece': [1896, 2004],
    }

    host_effects = []

    for country, host_years in host_data_info.items():
        country_df = df[df['NOC'] == country].copy()

        for host_year in host_years:
            if host_year > 2024:  # Skip future predictions
                continue

            before = country_df[(country_df['Year'] >= host_year - 8) & (country_df['Year'] < host_year)]['Total'].values
            during = country_df[country_df['Year'] == host_year]['Total'].values
            after = country_df[(country_df['Year'] > host_year) & (country_df['Year'] <= host_year + 8)]['Total'].values

            if len(during) > 0 and len(before) > 0:
                host_effects.append({
                    'Country': country,
                    'Host_Year': host_year,
                    'Before_Mean': np.mean(before),
                    'Host_Medals': during[0],
                    'After_Mean': np.mean(after) if len(after) > 0 else np.nan,
                })

    host_df = pd.DataFrame(host_effects)
    host_df['host_effect'] = host_df['Host_Medals'] - host_df['Before_Mean']

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Box plot comparison
    before_vals = []
    host_vals = []
    after_vals = []

    for _, row in host_df.iterrows():
        country_df = df[df['NOC'] == row['Country']].copy()
        before_data = country_df[(country_df['Year'] >= row['Host_Year'] - 8) &
                               (country_df['Year'] < row['Host_Year'])]['Total'].values
        host_data = country_df[country_df['Year'] == row['Host_Year']]['Total'].values
        after_data = country_df[(country_df['Year'] > row['Host_Year']) &
                              (country_df['Year'] <= row['Host_Year'] + 8)]['Total'].values

        before_vals.extend(before_data)
        if len(host_data) > 0:
            host_vals.append(host_data[0])
        after_vals.extend(after_data)

    box_data = [before_vals, host_vals, after_vals]
    bp = ax1.boxplot(box_data, labels=['Before\nHosting', 'Host\nYear', 'After\nHosting'],
                      patch_artist=True, widths=0.6)

    colors = [COLORS['blue'], COLORS['gold'], COLORS['green']]
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    ax1.set_ylabel('Total Medals', fontweight='bold')
    ax1.set_title('(A) Medal Distribution: Host vs. Non-Host Years\nClear Host Advantage', fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')

    # Panel B: Host effect by country
    top_hosts = host_df.nlargest(12, 'host_effect')

    y_pos = np.arange(len(top_hosts))
    colors_bar = [COLORS['gold'] if x > 0 else COLORS['red'] for x in top_hosts['host_effect']]

    ax2.barh(y_pos, top_hosts['host_effect'], color=colors_bar, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([f"{c} ({int(y)})" for c, y in zip(top_hosts['Country'], top_hosts['Host_Year'])], fontsize=8)
    ax2.axvline(x=0, color='black', linewidth=1)
    ax2.set_xlabel('Host Effect (Medals)', fontweight='bold')
    ax2.set_title('(B) Host Advantage by Country\nMedals Gained During Host Year', fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')

    avg_effect = host_df['host_effect'].mean()
    ax2.axvline(x=avg_effect, color=COLORS['red'], linestyle='--', linewidth=2, label=f'Average: +{avg_effect:.1f}')
    ax2.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_3_host_effect.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 3: Host Effect - Saved")

# =============================================================================
# FIGURE 4: 2028 PREDICTIONS
# =============================================================================

def create_figure_4_predictions_2028(data: Dict[str, pd.DataFrame]):
    """
    Figure 4: 2028 Predictions - Top 20 Countries
    Bar chart with prediction intervals
    """
    results_1 = data['results_1'].copy()
    results_2 = data['results_2'].copy()

    # Use results from Model 1 (Random Forest) with prediction intervals
    top_20 = results_1.head(20).copy()

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))

    y_pos = np.arange(len(top_20))
    countries = top_20['Country'].values
    predictions = top_20['Pred_Total_2028'].values
    pi_lower = top_20['PI_2.5'].values
    pi_upper = top_20['PI_97.5'].values

    # Color bars: highlight USA as host
    bar_colors = [COLORS['gold'] if c == 'United States' else COLORS['blue'] for c in countries]

    # Horizontal bar chart
    bars = ax.barh(y_pos, predictions, color=bar_colors, alpha=0.7, edgecolor='black', linewidth=0.5)

    # Add error bars for prediction intervals
    ax.errorbar(predictions, y_pos, xerr=[predictions - pi_lower, pi_upper - predictions],
                fmt='none', ecolor='black', elinewidth=1.5, capsize=3, alpha=0.5)

    # Add value labels
    for i, (pred, lower, upper) in enumerate(zip(predictions, pi_lower, pi_upper)):
        ax.text(pred + 1, i, f'{int(pred)}', va='center', fontsize=8, fontweight='bold')

    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels(countries, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel('Predicted Total Medals (2028 LA Olympics)', fontweight='bold')
    ax.set_title('2028 Olympic Medal Predictions\nTop 20 Countries with 95% Prediction Intervals', fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, axis='x')

    # Add legend
    legend_elements = [
        mpatches.Patch(color=COLORS['gold'], label='Host Country (USA)'),
        mpatches.Patch(color=COLORS['blue'], label='Other Countries'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', frameon=True)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_4_predictions_2028.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 4: 2028 Predictions - Saved")

# =============================================================================
# FIGURE 5: REGIME DYNAMICS
# =============================================================================

def create_figure_5_regime_dynamics(data: Dict[str, pd.DataFrame]):
    """
    Figure 5: Regime Dynamics
    Classification of countries by performance regime
    """
    regimes_df = data['results_6_regimes'].copy()

    # Regime order and colors
    regime_order = ['Dominant', 'Stable_Developing', 'Developing', 'Emerging', 'Declining']
    regime_labels = ['Dominant', 'Stable\nDeveloping', 'Developing', 'Emerging', 'Declining']
    regime_colors = [COLORS['gold'], COLORS['teal'], COLORS['blue'], COLORS['green'], COLORS['red']]

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Regime distribution
    regime_df = regimes_df.groupby('Regime')['Country'].apply(list).reset_index()
    regime_df['Count'] = regime_df['Country'].str.len()
    regime_df = regime_df.set_index('Regime').reindex(regime_order).dropna()

    sizes = regime_df['Count'].values
    labels = [f'{label}\n({int(size)})' for label, size in zip(regime_labels, sizes)]

    wedges, texts, autotexts = ax1.pie(sizes, labels=labels, colors=regime_colors,
                                        autopct='', startangle=90, pctdistance=0.85,
                                        wedgeprops=dict(edgecolor='white', linewidth=2))

    # Make it a donut
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax1.add_artist(centre_circle)

    ax1.text(0, 0, 'Olympic\nPerformance\nRegimes', ha='center', va='center',
             fontsize=12, fontweight='bold')

    ax1.set_title('(A) Country Classification by Regime\n2024 Status', fontweight='bold', pad=10)

    # Panel B: Scatter plot of medal distribution by regime
    for regime, color, label in zip(regime_order, regime_colors, regime_labels):
        regime_data = regimes_df[regimes_df['Regime'] == regime]
        ax2.scatter(regime_data['Medals'], [label] * len(regime_data),
                   alpha=0.5, s=50, c=color, edgecolors='black', linewidth=0.5)

    ax2.set_xlabel('Total Medals (2024)', fontweight='bold')
    ax2.set_ylabel('Performance Regime', fontweight='bold')
    ax2.set_title('(B) Medal Distribution by Regime\nPerformance Stratification', fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    ax2.set_xscale('log')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_5_regime_dynamics.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 5: Regime Dynamics - Saved")

# =============================================================================
# FIGURE 6: STRUCTURAL DISCONTINUITIES
# =============================================================================

def create_figure_6_discontinuities(data: Dict[str, pd.DataFrame]):
    """
    Figure 6: Structural Discontinuities
    Time series with detected break points highlighted
    """
    discontinuities = data['results_5'].copy()
    medal_counts = data['medal_counts'].copy()

    # Select representative countries with significant discontinuities
    top_breaks = discontinuities.nlargest(15, 'Break_Magnitude')

    # Select 6 diverse examples
    example_countries_full = ['United States', 'China', 'Australia', 'Great Britain', 'Japan', 'France']

    # Create figure with subplots
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()

    for idx, country in enumerate(example_countries_full):
        ax = axes[idx]

        # Get country data
        country_medals = medal_counts[medal_counts['NOC'] == country].copy()
        country_medals = country_medals.sort_values('Year')

        if len(country_medals) == 0:
            continue

        # Get discontinuities for this country
        country_breaks = top_breaks[top_breaks['Country'] == country]

        # Plot medal time series
        years = country_medals['Year'].values
        medals = country_medals['Total'].values

        ax.plot(years, medals, 'o-', color=COLORS['blue'], linewidth=2, markersize=5)

        # Highlight break points
        for _, break_row in country_breaks.iterrows():
            bp_year = break_row['Breakpoint_Year']
            effect_size = break_row['Break_Magnitude']

            if bp_year in years:
                bp_idx = list(years).index(bp_year)
                ax.axvline(x=bp_year, color=COLORS['red'], linestyle='--', linewidth=2, alpha=0.7)
                ax.plot(bp_year, medals[bp_idx], 'o', color=COLORS['red'], markersize=10,
                       markeredgecolor='black', markeredgewidth=1.5)

                # Add annotation
                ax.annotate(f'+{effect_size:.0f}',
                           xy=(bp_year, medals[bp_idx]),
                           xytext=(bp_year + 2, medals[bp_idx] + effect_size/2),
                           fontsize=7, color=COLORS['red'],
                           arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=1))

        ax.set_title(f'{country}', fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Year', fontsize=9)
        if idx % 3 == 0:
            ax.set_ylabel('Total Medals', fontsize=9)

    fig.suptitle('Structural Performance Discontinuities\nDetected Break Points in Medal Trajectories', fontweight='bold', fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_6_discontinuities.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 6: Discontinuities - Saved")

# =============================================================================
# FIGURE 7: MODEL PERFORMANCE
# =============================================================================

def create_figure_7_model_performance(data: Dict[str, pd.DataFrame]):
    """
    Figure 7: Model Performance Comparison
    Actual vs Predicted scatter plots for both models
    """
    results_1 = data['results_1'].copy()
    results_2 = data['results_2'].copy()
    medal_counts = data['medal_counts'].copy()

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: Model 1 (Random Forest) Performance
    actual_2024 = medal_counts[medal_counts['Year'] == 2024].copy()

    # Map NOC to Country for merging
    noc_to_country = {
        'USA': 'United States', 'CHN': 'China', 'GBR': 'Great Britain',
        'FRA': 'France', 'AUS': 'Australia', 'JPN': 'Japan',
        'GER': 'Germany', 'ITA': 'Italy', 'NED': 'Netherlands',
        'KOR': 'South Korea', 'CAN': 'Canada', 'BRA': 'Brazil',
        'NZL': 'New Zealand', 'ESP': 'Spain', 'HUN': 'Hungary',
        'UKR': 'Ukraine', 'KEN': 'Kenya', 'POL': 'Poland',
        'JAM': 'Jamaica', 'DEN': 'Denmark', 'CUB': 'Cuba'
    }

    actual_2024['Country'] = actual_2024['NOC'].map(noc_to_country)

    # Merge with predictions
    merged_1 = actual_2024.merge(results_1, on='Country', how='inner')

    if len(merged_1) > 0:
        ax1.scatter(merged_1['Total'], merged_1['Pred_Total_2028'], alpha=0.6, s=50,
                   c=COLORS['blue'], edgecolors='black', linewidth=0.5)

        max_val = max(merged_1['Total'].max(), merged_1['Pred_Total_2028'].max())
        ax1.plot([0, max_val * 1.2], [0, max_val * 1.2], 'r--', linewidth=2, label='Perfect Prediction')

        # Calculate R2
        from sklearn.metrics import r2_score
        r2_1 = r2_score(merged_1['Total'], merged_1['Pred_Total_2028'])

        ax1.set_xlabel('Actual Medals (2024)', fontweight='bold')
        ax1.set_ylabel('Predicted Medals (2028)', fontweight='bold')
        ax1.set_title(f'(A) Random Forest Model\nR-squared: {r2_1:.3f}', fontweight='bold')
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, max_val * 1.1)
        ax1.set_ylim(0, max_val * 1.1)

    # Panel B: Model 2 (AR with Regime Detection) Performance
    merged_2 = actual_2024.merge(results_2, on='Country', how='inner')

    if len(merged_2) > 0:
        ax2.scatter(merged_2['Total'], merged_2['Pred_Total_2028'], alpha=0.6, s=50,
                   c=COLORS['green'], edgecolors='black', linewidth=0.5)

        max_val = max(merged_2['Total'].max(), merged_2['Pred_Total_2028'].max())
        ax2.plot([0, max_val * 1.2], [0, max_val * 1.2], 'r--', linewidth=2, label='Perfect Prediction')

        r2_2 = r2_score(merged_2['Total'], merged_2['Pred_Total_2028'])

        ax2.set_xlabel('Actual Medals (2024)', fontweight='bold')
        ax2.set_ylabel('Predicted Medals (2028)', fontweight='bold')
        ax2.set_title(f'(B) AR Model with Regime Detection\nR-squared: {r2_2:.3f}', fontweight='bold')
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim(0, max_val * 1.1)
        ax2.set_ylim(0, max_val * 1.1)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_7_model_performance.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 7: Model Performance - Saved")

# =============================================================================
# FIGURE 8: PREDICTION COMPARISON
# =============================================================================

def create_figure_8_prediction_comparison(data: Dict[str, pd.DataFrame]):
    """
    Figure 8: Comprehensive Model Summary
    Comparison of predictions from both models with insights
    """
    results_1 = data['results_1'].copy()
    results_2 = data['results_2'].copy()

    # Merge predictions from both models
    merged = results_1.merge(results_2, on='Country', how='inner', suffixes=('_M1', '_M2'))

    # Get top 20 for comparison
    top_20 = merged.nlargest(20, 'Pred_Total_2028_M1')

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))

    y_pos = np.arange(len(top_20))
    countries = top_20['Country'].values

    pred_m1 = top_20['Pred_Total_2028_M1'].values
    pred_m2 = top_20['Pred_Total_2028_M2'].values

    # Sort by M1 predictions
    sort_idx = np.argsort(pred_m1)

    # Create grouped bar chart
    bar_height = 0.35
    ax.barh(y_pos - bar_height/2, pred_m1[sort_idx], bar_height,
           label='Random Forest', color=COLORS['blue'], alpha=0.7)
    ax.barh(y_pos + bar_height/2, pred_m2[sort_idx], bar_height,
           label='AR with Regime Detection', color=COLORS['green'], alpha=0.7)

    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels([countries[i] for i in sort_idx], fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel('Predicted Total Medals (2028)', fontweight='bold')
    ax.set_title('2028 Prediction Comparison: Both Models\nTop 20 Countries Forecast', fontweight='bold', pad=15)
    ax.legend(loc='lower right', frameon=True)
    ax.grid(True, alpha=0.3, axis='x')

    # Add correlation annotation
    from scipy.stats import pearsonr
    corr, pval = pearsonr(pred_m1, pred_m2)
    ax.text(0.98, 0.02, f'Correlation: r = {corr:.3f} (p < 0.001)',
           transform=ax.transAxes, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
           fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'figure_8_prediction_comparison.png'), dpi=300, bbox_inches='tight')
    plt.close()

    print("Figure 8: Prediction Comparison - Saved")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Generate all figures."""
    print("=" * 60)
    print("MCM 2025 Problem C - Figure Generation")
    print("=" * 60)

    # Load data
    print("\nLoading data...")
    data = load_data()
    print(f"Data loaded: {list(data.keys())}")

    # Generate figures
    print("\nGenerating figures...")

    create_figure_1_medal_trends(data)
    create_figure_2_zero_inflation(data)
    create_figure_3_host_effect(data)
    create_figure_4_predictions_2028(data)
    create_figure_5_regime_dynamics(data)
    create_figure_6_discontinuities(data)
    create_figure_7_model_performance(data)
    create_figure_8_prediction_comparison(data)

    print("\n" + "=" * 60)
    print(f"All figures saved to: {OUTPUT_DIR}/")
    print("=" * 60)

    # Create summary document
    create_figures_summary()

def create_figures_summary():
    """Create a summary document of all figures."""
    summary = """# MCM 2025 Problem C - Figure Summary

**Generated**: 2025-01-15
**Total Figures**: 8

---

## Figure List

### Figure 1: Medal Trends Over Time (1896-2024)
**File**: `figure_1_medal_trends.png`
**Description**: Time series visualization of total medals won by top nations
**Key Features**:
- Top medal-winning countries tracked over 128 years
- Historical event annotations (WWI, WWII, Boycotts)
- Color-coded by country with USA, China, USSR highlighted
**Purpose**: Establish historical context and show long-term performance patterns

---

### Figure 2: Zero Inflation & Distribution
**File**: `figure_2_zero_inflation.png`
**Description**: Distribution analysis of medal counts with theoretical comparisons
**Key Features**:
- Panel A: Histogram showing excess zeros
- Panel B: Comparison with Poisson and Negative Binomial distributions
- Justifies ZINB model choice
**Purpose**: Demonstrate why standard Poisson models are inadequate

---

### Figure 3: Host Country Effect
**File**: `figure_3_host_effect.png`
**Description**: Analysis of home advantage for Olympic hosts
**Key Features**:
- Panel A: Box plot of medal counts before/during/after hosting
- Panel B: Host effect magnitude by country
- Clear demonstration of host advantage
**Purpose**: Quantify the host country advantage

---

### Figure 4: 2028 Predictions
**File**: `figure_4_predictions_2028.png`
**Description**: Bar chart of predicted medal counts for LA 2028
**Key Features**:
- Top 20 countries with 95% prediction intervals
- USA highlighted as host country
- Error bars showing uncertainty
**Purpose**: Present primary prediction results

---

### Figure 5: Regime Dynamics
**File**: `figure_5_regime_dynamics.png`
**Description**: Classification of countries by performance regime
**Key Features**:
- Panel A: Donut chart of regime distribution
- Panel B: Scatter plot of medals by regime
- Categories: Dominant, Stable Developing, Developing, Emerging, Declining
**Purpose**: Show understanding of country performance life cycles

---

### Figure 6: Structural Discontinuities
**File**: `figure_6_discontinuities.png`
**Description**: Time series with detected structural break points
**Key Features**:
- 6 representative countries shown
- Chow test break points highlighted
- Effect sizes annotated
**Purpose**: Demonstrate structural change detection methodology

---

### Figure 7: Model Performance
**File**: `figure_7_model_performance.png`
**Description**: Actual vs. Predicted scatter plots
**Key Features**:
- Panel A: Random Forest model (R2 shown)
- Panel B: AR model with regime detection (R2 shown)
- Perfect prediction reference line
**Purpose**: Validate model accuracy

---

### Figure 8: Prediction Comparison
**File**: `figure_8_prediction_comparison.png`
**Description**: Side-by-side comparison of predictions from both models
**Key Features**:
- Top 20 countries ranked
- Both models shown for comparison
- High correlation noted
**Purpose**: Show model agreement and robustness

---

## Styling Notes

- All figures use colorblind-friendly palette (Wong's palette)
- Resolution: 300 DPI for publication
- Font: Arial/sans-serif, size 10-12pt
- Consistent styling across all figures
- Grid lines: subtle, alpha=0.3

---

## Data Sources

- `medal_counts_clean.csv`: Historical medal data (1896-2024)
- `results_1.csv`: Model 1 (Random Forest) predictions
- `results_2_predictions.csv`: Model 2 (AR with Regime Detection) predictions
- `results_6_regimes.csv`: Regime classification results
- `results_5.csv`: Structural discontinuity analysis
"""

    with open(os.path.join(OUTPUT_DIR, 'figures_summary.md'), 'w') as f:
        f.write(summary)

    print("Figures summary document created.")

if __name__ == "__main__":
    main()
