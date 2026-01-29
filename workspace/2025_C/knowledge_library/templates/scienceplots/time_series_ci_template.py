# -*- coding: utf-8 -*-
"""
Time Series with Confidence Intervals Template
Model Number: Any (1, 2, 3, etc.)
Output: output/figures/model_X_line_time_series_with_ci.png

Purpose: Show trends over time with uncertainty bounds
When to Use: Predictions over years (e.g., medal counts 1992-2024), training progress, forecasting
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Add tools to path
# NOTE: Adjust path based on where you run this script from
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(script_dir, '../../../tools')
sys.path.insert(0, tools_dir)
import mpl_config

# Apply research style (IEEE format with fallback)
scienceplots_available = mpl_config.apply_research_style(dpi=300, figsize=(10, 6))

# Load data (UPDATE THIS PATH)
# Expected CSV format: year,predictions,PI_2.5,PI_97.5 (or similar confidence interval columns)
# Example:
# year,predictions,PI_2.5,PI_97.5
# 1992,105,98,112
# 1994,108,100,116
# 1996,115,107,123
data_path = 'output/sample_time_series.csv'  # UPDATE THIS
data = pd.read_csv(data_path, encoding='utf-8')

# Create figure
fig, ax = plt.subplots()

# Plot main line (UPDATE COLUMN NAMES IF NEEDED)
x_col = 'year' if 'year' in data.columns else data.columns[0]
y_col = 'predictions' if 'predictions' in data.columns else data.columns[1]

ax.plot(data[x_col], data[y_col], 'o-', linewidth=2, markersize=6,
        label='Predictions', color=mpl_config.get_color_palette('colorblind')[0])

# Check for confidence intervals (UPDATE COLUMN NAMES IF NEEDED)
ci_cols = [col for col in data.columns if 'PI' in col or 'CI' in col or 'conf' in col.lower()]

if len(ci_cols) >= 2:
    # Found confidence interval columns
    ci_lower = ci_cols[0] if '2.5' in ci_cols[0] or 'lower' in ci_cols[0] else ci_cols[1]
    ci_upper = ci_cols[1] if '97.5' in ci_cols[1] or 'upper' in ci_cols[1] else ci_cols[0]

    ax.fill_between(data[x_col], data[ci_lower], data[ci_upper],
                    alpha=0.3, label='95% Confidence Interval',
                    color=mpl_config.get_color_palette('colorblind')[0])
    has_ci = True
else:
    has_ci = False
    print("[INFO] No confidence intervals found in data")

# Labels
ax.set_xlabel('Year', fontweight='bold')
ax.set_ylabel('Predicted Medal Count', fontweight='bold')
ax.set_title('Model 1: Medal Count Predictions Over Time', fontweight='bold')
ax.legend(loc='best')
ax.grid(True, alpha=0.3)

# Optional: Add vertical line for current year or event (UNCOMMENT IF NEEDED)
# ax.axvline(x=2024, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Current Year')

# Optional: Set x-axis limits (UNCOMMENT IF NEEDED)
# ax.set_xlim(1990, 2030)

# Optional: Set y-axis limits (UNCOMMENT IF NEEDED)
# ax.set_ylim(0, 150)

plt.tight_layout()

# Save with verification (UPDATE OUTPUT PATH)
output_path = 'output/figures/model_1_line_time_series_with_ci.png'
success, msg = mpl_config.save_figure(fig, output_path)

if success:
    print(f"[SUCCESS] {output_path}")
    if scienceplots_available:
        print("[INFO] Using SciencePlots style")
    else:
        print("[INFO] Using fallback style (seaborn-whitegrid)")
else:
    print(f"[ERROR] {msg}")

# Print figure info for verification
print("\n[FIGURE INFO]")
print(f"  Type: Time series with confidence intervals")
print(f"  X-axis: {x_col}")
print(f"  Y-axis: {y_col}")
print(f"  Confidence intervals: {'Yes' if has_ci else 'No'}")
print(f"  Data range: {data[x_col].min()} - {data[x_col].max()}")
print(f"  Output: {output_path}")
