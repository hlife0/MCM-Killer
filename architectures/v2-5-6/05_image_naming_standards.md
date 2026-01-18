# Image File Naming Standards (v2.5.6)

> **Purpose**: Standardize image file naming and fix verification commands
> **Status**: MANDATORY for all visualization workflows
> **Fixes Issue**: Image verification commands fail with wildcard errors

---

## Problem Summary

### v2.5.5 Issue

**Error Observed**:
```bash
Bash(ls -lh output/figures/*.png | wc -l && ls -lh output/figures/*..png && python3 -c "...")
⎿  Error: Exit code 2
     ls: cannot access 'output/figures/*..png': No such file or directory
```

**Root Cause**: Wildcard pattern `*..png` is incorrect

**Additional Issues**:
1. No standardized naming for images
2. Difficult to track which model created which figure
3. No consistency in figure types or descriptions

**Impact**:
- Image quality verification fails
- Cannot detect corrupted images
- Difficult to organize and reference figures

---

## v2.5.6 Solution

### Naming Convention (MANDATORY)

**Format**:
```
{model_number}_{figure_type}_{description}.png
```

**Components**:
- `{model_number}`: Model that created the figure (1, 2, 3, etc.)
- `{figure_type}`: Type of visualization (scatter, line, bar, histogram, heatmap, etc.)
- `{description}`: Brief description of what the figure shows
- `.png`: PNG extension

**Rules**:
- Use lowercase letters
- Use underscores to separate words in description
- Keep description under 50 characters
- No spaces or special characters

### Examples

**Model 1 Figures**:
```
model_1_scatter_predictions_vs_actual.png
model_1_histogram_residuals.png
model_1_line_predicted_medals_by_country.png
model_1_bar_feature_importance.png
model_1_heatmap_correlation_matrix.png
```

**Model 2 Figures**:
```
model_2_scatter_train_vs_test_error.png
model_2_line_convergence_history.png
model_2_bar_feature_importance.png
model_2_boxplot_medal_distribution.png
```

**Model 3 Figures**:
```
model_3_line_ensemble_predictions.png
model_3_histogram_prediction_intervals.png
model_3_scatter_model_comparison.png
model_3_violin_medal_distribution_by_year.png
```

### Figure Types (Standardized)

| Type | Usage | Example |
|------|-------|---------|
| `scatter` | Scatter plots | `model_1_scatter_predictions_vs_actual.png` |
| `line` | Line plots | `model_1_line_predicted_medals_by_country.png` |
| `bar` | Bar charts | `model_1_bar_feature_importance.png` |
| `histogram` | Histograms | `model_1_histogram_residuals.png` |
| `heatmap` | Heatmaps | `model_1_heatmap_correlation_matrix.png` |
| `boxplot` | Box plots | `model_2_boxplot_medal_distribution.png` |
| `violin` | Violin plots | `model_3_violin_medal_distribution_by_year.png` |
| `diagram` | Flowcharts/diagrams | `model_1_diagram_model_architecture.png` |
| `map` | Maps/geographic | `model_1_map_medals_by_country.png` |
| `table` | Tables | `model_1_table_model_summary.png` |

---

## Verification Commands (FIXED)

### Count Images

**v2.5.5 (BROKEN)**:
```bash
ls -lh output/figures/*..png  # WRONG: *..png
```

**v2.5.6 (FIXED)**:
```bash
# Count all PNG files
ls -1 output/figures/*.png | wc -l

# List all PNG files with details
ls -lh output/figures/*.png
```

### Verify Image Quality

**v2.5.5 (BROKEN)**:
```bash
ls -lh output/figures/*.png | wc -l && ls -lh output/figures/*..png && python3 -c "..."
# Error: *..pattern causes command to fail
```

**v2.5.6 (FIXED)**:
```bash
# Count images
ls -1 output/figures/*.png | wc -l

# Verify image quality (detect corruption)
python3 -c "
from PIL import Image
import os

corrupted = []
valid = []

for f in sorted(os.listdir('output/figures')):
    if f.endswith('.png'):
        filepath = os.path.join('output/figures', f)
        try:
            img = Image.open(filepath)
            img.verify()
            img = Image.open(filepath)  # Re-open for size
            print(f'{f}: {img.size[0]}x{img.size[1]} - OK')
            valid.append(f)
        except Exception as e:
            print(f'{f}: CORRUPTED - {e}')
            corrupted.append(f)

print(f'\\nSummary: {len(valid)} valid, {len(corrupted)} corrupted')
if corrupted:
    print(f'Corrupted files: {corrupted}')
    exit(1)
"
```

### Check Image Dimensions

**v2.5.6 (NEW)**:
```bash
# Check all images have reasonable dimensions
python3 -c "
from PIL import Image
import os

for f in sorted(os.listdir('output/figures')):
    if f.endswith('.png'):
        filepath = os.path.join('output/figures', f)
        img = Image.open(filepath)
        width, height = img.size

        # Check for unreasonable dimensions
        if width < 100 or height < 100:
            print(f'{f}: TOO SMALL ({width}x{height})')
        elif width > 10000 or height > 10000:
            print(f'{f}: TOO LARGE ({width}x{height})')
        elif width == 0 or height == 0:
            print(f'{f}: ZERO DIMENSION ({width}x{height})')
        else:
            print(f'{f}: {width}x{height} - OK')
"
```

### Check File Sizes

**v2.5.6 (NEW)**:
```bash
# Check all images have reasonable file sizes
python3 -c "
import os

for f in sorted(os.listdir('output/figures')):
    if f.endswith('.png'):
        filepath = os.path.join('output/figures', f)
        size_bytes = os.path.getsize(filepath)
        size_kb = size_bytes / 1024

        # Check for unreasonable sizes
        if size_bytes == 0:
            print(f'{f}: EMPTY FILE (0 bytes)')
        elif size_bytes < 1000:
            print(f'{f}: TOO SMALL ({size_kb:.1f} KB)')
        elif size_bytes > 10 * 1024 * 1024:  # 10 MB
            print(f'{f}: TOO LARGE ({size_kb/1024:.1f} MB)')
        else:
            print(f'{f}: {size_kb:.1f} KB - OK')
"
```

---

## @visualizer Agent Instructions

### When Creating Figures

**Step 1: Generate Figure**

```python
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(predictions, actual)
ax.set_xlabel('Predicted Medals')
ax.set_ylabel('Actual Medals')
ax.set_title('Model 1: Predictions vs Actual')

# Save with standardized naming
fig.savefig('output/figures/model_1_scatter_predictions_vs_actual.png',
           dpi=300, bbox_inches='tight')
plt.close(fig)
```

**Step 2: Verify Figure**

```python
from PIL import Image
import os

# Verify the saved file
filepath = 'output/figures/model_1_scatter_predictions_vs_actual.png'

# Check file exists
assert os.path.exists(filepath), f'File not found: {filepath}'

# Check file is not corrupted
img = Image.open(filepath)
img.verify()  # Raises exception if corrupted

# Check dimensions
width, height = img.size
assert width >= 800 and height >= 600, f'Image too small: {width}x{height}'

# Check file size
size_bytes = os.path.getsize(filepath)
assert size_bytes > 1000, f'File too small: {size_bytes} bytes'

print(f'✅ Figure saved and verified: {filepath}')
print(f'   Dimensions: {width}x{height}')
print(f'   File size: {size_bytes/1024:.1f} KB')
```

### Naming Guidelines

**DO**:
- ✅ Use `model_1_scatter_predictions_vs_actual.png`
- ✅ Use `model_2_line_convergence_history.png`
- ✅ Use `model_3_bar_feature_importance.png`
- ✅ Use descriptive but concise names
- ✅ Use underscores to separate words

**DON'T**:
- ❌ Use `figure1.png` (not descriptive)
- ❌ Use `model1fig.png` (no underscores)
- ❌ Use `predictions vs actual.png` (spaces)
- ❌ Use `Model_1_Scatter_Plot.png` (capital letters)
- ❌ Use `model_1_scatter_predictions_vs_actual_final_v2.png` (suffixes)

---

## @director Agent Instructions

### When Verifying Figures

**Step 1: Count Figures**

```bash
# Count all PNG files
count=$(ls -1 output/figures/*.png 2>/dev/null | wc -l)
echo "Total figures: $count"
```

**Expected**: At least 3-5 figures per model

**Step 2: Verify No Corruption**

```bash
# Run quality check
python3 -c "
from PIL import Image
import os

corrupted = []
for f in os.listdir('output/figures'):
    if f.endswith('.png'):
        try:
            img = Image.open(os.path.join('output/figures', f))
            img.verify()
        except Exception as e:
            corrupted.append(f)

if corrupted:
    print(f'❌ CORRUPTED: {corrupted}')
    exit(1)
else:
    print('✅ All figures valid')
"
```

**Step 3: Check Naming Compliance**

```bash
# Check all files follow naming convention
for f in output/figures/*.png; do
    basename=$(basename "$f" .png)

    # Check format: model_{number}_{type}_{description}.png
    if [[ ! $basename =~ ^model_[0-9]+_[a-z]+_[a-z_]+$ ]]; then
        echo "⚠️ NAMING VIOLATION: $f"
    fi
done
```

**Step 4: Verify Expected Figures Exist**

```bash
# For each model, check for expected figure types
expected_types=("scatter" "line" "bar" "histogram")

for model_num in 1 2 3; do
    for type in "${expected_types[@]}"; do
        pattern="output/figures/model_${model_num}_${type}_*.png"
        count=$(ls $pattern 2>/dev/null | wc -l)

        if [ $count -eq 0 ]; then
            echo "⚠️ MISSING: model_${model_num}_${type} figure"
        else
            echo "✅ FOUND: $count model_${model_num}_${type} figure(s)"
        fi
    done
done
```

---

## File Organization

### Directory Structure

```
output/
└── figures/
    ├── model_1/
    │   ├── model_1_scatter_predictions_vs_actual.png
    │   ├── model_1_histogram_residuals.png
    │   ├── model_1_line_predicted_medals_by_country.png
    │   └── model_1_bar_feature_importance.png
    ├── model_2/
    │   ├── model_2_scatter_train_vs_test_error.png
    │   ├── model_2_line_convergence_history.png
    │   └── model_2_bar_feature_importance.png
    └── model_3/
        ├── model_3_line_ensemble_predictions.png
        ├── model_3_histogram_prediction_intervals.png
        └── model_3_scatter_model_comparison.png
```

**Note**: All figures in flat `output/figures/` directory (no subdirectories), but prefix organizes by model.

### Model-Figure Mapping

**To find all figures for a specific model**:
```bash
ls -1 output/figures/model_1_*.png
```

**To find all figures of a specific type**:
```bash
ls -1 output/figures/*_scatter_*.png
ls -1 output/figures/*_histogram_*.png
ls -1 output/figures/*_bar_*.png
```

---

## Integration with Paper Writing

### @writer Includes Figures

**In LaTeX**:
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{output/figures/model_1_scatter_predictions_vs_actual.png}
\caption{Model 1: Predicted vs Actual Medal Counts}
\label{fig:model1_scatter}
\end{figure}
```

**Reference**:
```latex
As shown in Figure~\ref{fig:model1_scatter}, Model 1's predictions...
```

### Figure Tracking

**In VERSION_MANIFEST.json**:
```json
{
  "figures": {
    "model_1": [
      "model_1_scatter_predictions_vs_actual.png",
      "model_1_histogram_residuals.png",
      "model_1_line_predicted_medals_by_country.png",
      "model_1_bar_feature_importance.png"
    ],
    "model_2": [
      "model_2_scatter_train_vs_test_error.png",
      "model_2_line_convergence_history.png",
      "model_2_bar_feature_importance.png"
    ]
  }
}
```

---

## Quality Requirements

### Minimum Standards

**Resolution**:
- Minimum: 800×600 pixels
- Recommended: 1200×900 pixels
- DPI: 300 for publication quality

**File Size**:
- Minimum: 1 KB (not empty)
- Maximum: 10 MB (not excessively large)
- Recommended: 50-500 KB

**Content**:
- Clear labels (title, axes, legend if applicable)
- Readable font size (at least 10pt at final size)
- High contrast colors
- No distortion or artifacts

### Quality Check Command

```bash
# Comprehensive quality check
python3 -c "
from PIL import Image
import os

issues = []

for f in sorted(os.listdir('output/figures')):
    if f.endswith('.png'):
        filepath = os.path.join('output/figures', f)

        # Check file exists and not empty
        if not os.path.exists(filepath):
            issues.append(f'{f}: FILE NOT FOUND')
            continue

        size_bytes = os.path.getsize(filepath)
        if size_bytes == 0:
            issues.append(f'{f}: EMPTY FILE')
            continue

        # Check not corrupted
        try:
            img = Image.open(filepath)
            img.verify()
            img = Image.open(filepath)  # Re-open
        except Exception as e:
            issues.append(f'{f}: CORRUPTED - {e}')
            continue

        # Check dimensions
        width, height = img.size
        if width < 800 or height < 600:
            issues.append(f'{f}: TOO SMALL ({width}x{height})')

        # Check file size
        if size_bytes < 1000:
            issues.append(f'{f}: TOO SMALL ({size_bytes} bytes)')
        elif size_bytes > 10 * 1024 * 1024:
            issues.append(f'{f}: TOO LARGE ({size_bytes/1024/1024:.1f} MB)')

if issues:
    print('❌ QUALITY ISSUES FOUND:')
    for issue in issues:
        print(f'  - {issue}')
    exit(1)
else:
    print('✅ All figures meet quality standards')
"
```

---

## Troubleshooting

### Issue: Command Fails with "No such file or directory"

**Symptom**:
```bash
ls: cannot access 'output/figures/*..png': No such file or directory
```

**Cause**: Wrong wildcard pattern (`*..png` instead of `*.png`)

**Solution**: Use correct pattern
```bash
ls -1 output/figures/*.png  # CORRECT
```

### Issue: No Figures Found

**Symptom**: `ls: cannot access 'output/figures/*.png': No such file or directory`

**Cause**: `output/figures/` directory doesn't exist or no PNG files

**Solution**:
```bash
# Check if directory exists
ls -la output/figures/

# Create if doesn't exist
mkdir -p output/figures/

# Check if @visualizer completed
```

### Issue: Image Corrupted

**Symptom**: `PIL.UnidentifiedImageError: cannot identify image file`

**Cause**: Image file corrupted during save

**Solution**:
1. @visualizer regenerates the figure
2. Check disk space
3. Verify save code completed successfully

### Issue: Naming Convention Violation

**Symptom**: File name doesn't follow `model_{number}_{type}_{description}.png`

**Solution**:
1. @visualizer renames file to follow convention
2. OR @visualizer regenerates with correct name

---

## Verification Checklist

Before deploying v2.5.6, verify:

- [ ] Naming convention documented
- [ ] Verification commands fixed (use `*.png` not `*..png`)
- [ ] @visualizer updated with naming guidelines
- [ ] @director updated with verification commands
- [ ] @writer updated with figure inclusion examples
- [ ] Quality check script created
- [ ] Troubleshooting guide documented
- [ ] All agents updated with v2.5.6 changes

---

**Document Version**: v2.5.6
**Created**: 2026-01-18
**Status**: MANDATORY for all visualization workflows
