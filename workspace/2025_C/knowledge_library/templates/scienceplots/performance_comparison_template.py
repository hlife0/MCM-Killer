# -*- coding: utf-8 -*-
"""
Performance Comparison Template
Model Number: Any (1, 2, 3, etc.)
Output: output/figures/model_X_bar_performance_comparison.png

Purpose: Compare multiple models or methods on the same metrics
When to Use: Comparing Model 1 vs Model 2 vs Model 3, or showing performance on different test cases
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Add tools to path
import os
import importlib.util

script_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(script_dir, '../../../tools')
sys.path.insert(0, tools_dir)

# Import mpl_config (handle numbered filename)
spec = importlib.util.spec_from_file_location("mpl_config", os.path.join(tools_dir, "9_mpl_config.py"))
mpl_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mpl_config)

# Apply research style (IEEE format with fallback)
scienceplots_available = mpl_config.apply_research_style(dpi=300, figsize=(10, 6))

# Load data (UPDATE THIS PATH)
# Expected CSV format: model,metric,value,error
# Example:
# model,metric,value,error
# Model_1,Accuracy,0.85,0.03
# Model_1,R_squared,0.78,0.05
# Model_2,Accuracy,0.82,0.04
# Model_2,R_squared,0.75,0.06
data_path = 'output/results_1.csv'  # UPDATE THIS - Path relative to workspace root
data = pd.read_csv(data_path, encoding='utf-8')

# Create figure
fig, ax = plt.subplots()

# Get unique models and metrics (UPDATE COLUMN NAMES IF NEEDED)
if 'model' in data.columns and 'metric' in data.columns:
    models = data['model'].unique()
    metrics = data['metric'].unique()

    # Set up grouped bar chart
    x = np.arange(len(metrics))
    width = 0.8 / len(models)

    # Get color palette
    colors = mpl_config.get_color_palette('colorblind')

    # Plot bars for each model
    for i, model in enumerate(models):
        model_data = data[data['model'] == model]
        values = model_data['value'].values
        errors = model_data['error'].values if 'error' in model_data.columns else None

        if errors is not None:
            ax.bar(x + i * width, values, width, label=model, yerr=errors,
                   capsize=5, color=colors[i % len(colors)])
        else:
            ax.bar(x + i * width, values, width, label=model,
                   color=colors[i % len(colors)])

    # Labels
    ax.set_xlabel('Performance Metric', fontweight='bold')
    ax.set_ylabel('Value', fontweight='bold')
    ax.set_title('Model Performance Comparison', fontweight='bold')
    ax.set_xticks(x + width * (len(models) - 1) / 2)
    ax.set_xticklabels(metrics, rotation=45, ha='right')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3, axis='y')

else:
    # Alternative: If data has different structure, adapt accordingly
    # Example: Simple bar chart with single metric
    categories = data.iloc[:, 0].values
    values = data.iloc[:, 1].values

    ax.bar(categories, values, color=mpl_config.get_color_palette('colorblind')[0])
    ax.set_xlabel('Category', fontweight='bold')
    ax.set_ylabel('Value', fontweight='bold')
    ax.set_title('Performance Comparison', fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()

# Save with verification (UPDATE OUTPUT PATH)
output_path = 'output/figures/model_1_bar_performance_comparison.png'
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
print(f"  Type: Grouped bar chart")
print(f"  Metrics shown: {', '.join(metrics) if 'metric' in data.columns else 'N/A'}")
print(f"  Models compared: {', '.join(models) if 'model' in data.columns else 'N/A'}")
print(f"  Output: {output_path}")
