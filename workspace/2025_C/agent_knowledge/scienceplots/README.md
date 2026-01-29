# SciencePlots Knowledge Base for MCM-Killer

## Overview

This knowledge base provides comprehensive guidance for using SciencePlots to create IEEE-quality publication figures in the MCM-Killer multi-agent system.

## Table of Contents

1. **[README.md](README.md)** (this file) - Index and quick reference
2. **[protocols.md](protocols.md)** - 10 visualization protocols for consistent figure quality
3. **[plot_type_guide.md](plot_type_guide.md)** - Decision tree for selecting appropriate plot types
4. **[mcm_templates.md](mcm_templates.md)** - MCM-specific template documentation

## Quick Start

### Step 1: Import Configuration Module

```python
import sys
sys.path.insert(0, '../../tools')
import mpl_config
```

### Step 2: Apply Research Style

```python
# Apply IEEE-style formatting with fallback
scienceplots_available = mpl_config.apply_research_style(dpi=300, figsize=(10, 6))
```

### Step 3: Create Figure

```python
import matplotlib.pyplot as plt
import pandas as pd

# Read data
data = pd.read_csv('output/results_1.csv')

# Create figure
fig, ax = plt.subplots()
ax.plot(data['year'], data['predictions'])
ax.set_xlabel('Year')
ax.set_ylabel('Predicted Value')
ax.set_title('Model 1: Predictions Over Time')
```

### Step 4: Save with Verification

```python
# Save with automatic quality verification
success, msg = mpl_config.save_figure(fig, 'output/figures/model_1_line_predictions.png')
if not success:
    print(f"Error: {msg}")
```

## Self-Healing Loop

For automated code generation with error fixing:

```python
from tools.scienceplots_controller import execute_visualization_code

code = """
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig('output/test.png')
"""

success, msg = execute_visualization_code(code, 'output/test.png', max_retries=3)
```

**Progressive Fix Strategy**:
- Attempt 1: Execute original code
- Attempt 2: Fix syntax, imports, remove `plt.show()`
- Attempt 3: Fix column names, dimensions, NaN handling
- Attempt 4: Fix directory creation, `tight_layout()`

## Style Configuration

### Primary Style (SciencePlots)
- **Style combination**: `['science', 'ieee', 'no-latex']`
- **Requirements**: `pip install scienceplots`
- **Font**: Computer Modern Roman (serif)
- **DPI**: 300 (publication quality)

### Fallback Style (Seaborn)
- **Style**: `seaborn-whitegrid`
- **No installation required** (included with matplotlib)
- **Font**: Arial/DejaVu Sans (sans-serif)
- **DPI**: 300 (maintained)

## Figure Naming Convention

**Format**: `{model_number}_{figure_type}_{description}.png`

**Examples**:
- `model_1_scatter_predictions_vs_actual.png`
- `model_1_histogram_residuals.png`
- `model_2_line_convergence_history.png`
- `model_3_heatmap_correlation_matrix.png`

**See**: [get_figure_naming_convention()](../../tools/9_mpl_config.py) for full documentation

## Integration with MCM-Killer

### Phase 6 (Visualization)
- **Input**: `results_*.csv` from Phase 5A/5B
- **Output**: `output/figures/*.png`
- **Uses**: `tools/9_mpl_config.py`

### Phase 6.5 (Visual Quality Gate)
- **Verification**: `mpl_config.verify_figure_quality()`
- **Corruption detection**: Existing mechanism preserved

### Visualizer Agent
- **Configuration**: `.claude/agents/visualizer.md`
- **Import requirement**: `tools/9_mpl_config.py`
- **Modes**: Mode A (data plots) + Mode B (Mermaid diagrams)

## Templates

### Available Templates (v3.1.0)
1. **Performance Comparison** ✓ - Grouped bar chart (`performance_comparison_template.py`)
2. **Time Series with CI** ✓ - Line chart with confidence bands (`time_series_ci_template.py`)

### Planned Templates (Future)
3. **Scatter Plot** - Predictions vs actual
4. **Histogram** - Residual distribution
5. **Heatmap** - Correlation matrix
6. **Multi-Panel** - Combined results display

**Location**: `knowledge_library/templates/scienceplots/`

## Protocols

See [protocols.md](protocols.md) for detailed visualization protocols:
1. Figure Initialization
2. Data Preparation
3. Plot Selection
4. Styling Guidelines
5. Labeling Standards
6. Legend Management
7. Color Usage
8. Error Representation
9. Multi-Panel Figures
10. Export and Verification

## Troubleshooting

### Issue: SciencePlots not installed
**Solution**: System automatically falls back to seaborn-whitegrid

### Issue: TeX dependency errors
**Solution**: Use `'no-latex'` style (mathtext renders LaTeX without TeX)

### Issue: Image corruption
**Solution**: `verify_figure_quality()` detects and reports issues

### Issue: Code execution failures
**Solution**: Use `execute_visualization_code()` with max_retries=3

## Best Practices

1. **ALWAYS** use UTF-8 encoding for file operations
2. **ALWAYS** verify figure quality after saving
3. **ALWAYS** follow naming convention
4. **NEVER** use `plt.show()` in automated scripts
5. **ALWAYS** include `tight_layout()` before saving
6. **PREFER** SciencePlots style, but accept fallback gracefully

## Additional Resources

- [SciencePlots Documentation](https://scienceplots.readthedocs.io/)
- [Matplotlib Style Reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
- [IEEE Graphics Guidelines](https://ieee-authorcenter.ieee.org/wp-content/uploads/IEEE-Graphics-Guidelines.pdf)

## Version History

- **v3.1.0** (2025-01-29): Initial integration with MCM-Killer
  - Core configuration module (tools/9_mpl_config.py)
  - Auto-fix controller (tools/scienceplots_controller.py)
  - Agent knowledge base (agent_knowledge/scienceplots/)
  - Integration with visualizer agent
