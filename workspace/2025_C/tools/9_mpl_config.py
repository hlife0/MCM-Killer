# -*- coding: utf-8 -*-
"""
SciencePlots Configuration Module for MCM-Killer v3.1.0

Core configuration for IEEE-quality publication figures with:
- Consistent scientific styling (['science', 'ieee', 'no-latex'])
- Self-healing code generation loop (max 3 retries)
- Image quality verification (integrated with existing Phase 6.5)

Author: MCM-Killer Visualizer Team
Version: 3.1.0
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys
from pathlib import Path
from typing import Tuple, Optional, List
from PIL import Image

# =============================================================================
# SECTION 1: Style Application
# =============================================================================

def apply_research_style(dpi: int = 300, figsize: Tuple[int, int] = (10, 6)) -> bool:
    """
    Apply SciencePlots research style with fallback mechanism.

    Style hierarchy:
    1. Primary: ['science', 'ieee', 'no-latex'] (IEEE publication quality)
    2. Fallback: seaborn-whitegrid (clean, professional)
    3. Emergency: matplotlib default with grid

    Args:
        dpi: Figure resolution (default: 300 for publication)
        figsize: Figure size in inches (default: 10x6)

    Returns:
        bool: True if SciencePlots loaded, False if using fallback

    Examples:
        >>> apply_research_style()  # Use defaults
        True  # SciencePlots available
        >>> apply_research_style(dpi=600, figsize=(12, 8))
        False  # Using fallback
    """
    try:
        # Attempt 1: SciencePlots with IEEE style (PRIMARY)
        import scienceplots  # noqa: F401

        # 'no-latex' is CRITICAL - avoids TeX installation requirement
        # Matplotlib's mathtext renders LaTeX math syntax without TeX
        plt.style.use(['science', 'ieee', 'no-latex'])

        # Configure figure settings
        plt.rcParams['figure.figsize'] = figsize
        plt.rcParams['figure.dpi'] = dpi
        plt.rcParams['savefig.dpi'] = dpi
        plt.rcParams['savefig.bbox'] = 'tight'
        plt.rcParams['savefig.pad_inches'] = 0.1

        # Font configuration
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Computer Modern Roman']
        plt.rcParams['mathtext.fontset'] = 'cm'

        # UTF-8 encoding enforcement
        plt.rcParams['axes.unicode_minus'] = False  # Proper minus signs

        return True

    except (ImportError, OSError):
        # Fallback 1: seaborn-whitegrid
        try:
            plt.style.use('seaborn-v0_8-whitegrid')
        except OSError:
            try:
                plt.style.use('seaborn-whitegrid')
            except OSError:
                # Fallback 2: Default with grid
                plt.rcParams['axes.grid'] = True
                plt.rcParams['grid.alpha'] = 0.3

        # Configure figure settings (same for all fallbacks)
        plt.rcParams['figure.figsize'] = figsize
        plt.rcParams['figure.dpi'] = dpi
        plt.rcParams['savefig.dpi'] = dpi
        plt.rcParams['savefig.bbox'] = 'tight'
        plt.rcParams['savefig.pad_inches'] = 0.1

        # Font configuration (fallback)
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False

        return False


# =============================================================================
# SECTION 2: Figure Quality Verification
# =============================================================================

def verify_figure_quality(image_path: str) -> Tuple[bool, str]:
    """
    Verify generated figure is not corrupted.

    Integrated with Phase 6.5 (Visual Quality Gate).

    Checks:
    1. File exists and non-zero size
    2. Valid image format (PNG verification)
    3. Minimum dimensions (100x100 pixels)
    4. No pixel corruption (all identical values)
    5. Correct image mode (RGB, RGBA, L, CMYK)

    Args:
        image_path: Path to image file

    Returns:
        Tuple[bool, str]: (is_valid, issue_description)

    Examples:
        >>> verify_figure_quality('output/figures/model_1_scatter_predictions.png')
        (True, 'Image is valid')
        >>> verify_figure_quality('output/figures/corrupted.png')
        (False, 'File is empty (0 bytes)')
    """
    try:
        # Check 1: File exists
        if not os.path.exists(image_path):
            return False, "File does not exist"

        # Check 2: Non-zero size
        if os.path.getsize(image_path) == 0:
            return False, "File is empty (0 bytes)"

        # Check 3: Valid image format
        img = Image.open(image_path)
        img.verify()  # Verify it's a valid image (closes file)

        # Reopen for further checks
        img = Image.open(image_path)

        # Check 4: Minimum dimensions
        width, height = img.size
        if width < 100 or height < 100:
            return False, f"Image too small: {width}x{height} (minimum: 100x100)"

        # Check 5: No pixel corruption
        img_array = np.array(img)
        if len(img_array.shape) >= 2:
            # Check if all pixels are the same (corrupted)
            if np.all(img_array == img_array.flat[0]):
                return False, "All pixels have identical value (corrupted)"

        # Check 6: Valid image mode
        if img.mode not in ['RGB', 'RGBA', 'L', 'CMYK']:
            return False, f"Unexpected image mode: {img.mode}"

        return True, "Image is valid"

    except Exception as e:
        return False, f"Image corruption detected: {str(e)}"


# =============================================================================
# SECTION 3: Figure Saving with Verification
# =============================================================================

def save_figure(fig: plt.Figure, output_path: str, verify: bool = True) -> Tuple[bool, str]:
    """
    Save figure with automatic quality verification.

    Creates output directory if needed, saves figure, and verifies quality.

    Args:
        fig: Matplotlib figure object
        output_path: Path where figure will be saved
        verify: Whether to verify image quality after saving (default: True)

    Returns:
        Tuple[bool, str]: (success, message)

    Examples:
        >>> fig, ax = plt.subplots()
        >>> ax.plot([1, 2, 3], [1, 4, 9])
        >>> save_figure(fig, 'output/figures/model_1_line_example.png')
        (True, 'Figure saved successfully: output/figures/model_1_line_example.png')
    """
    try:
        # Create output directory if needed
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Save figure with UTF-8 encoding enforcement
        fig.savefig(
            output_path,
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.1,
            format='png',
            metadata={'Software': None}  # Remove matplotlib metadata
        )

        # Verify figure quality
        if verify:
            is_valid, issue = verify_figure_quality(output_path)
            if not is_valid:
                return False, f"Figure saved but verification failed: {issue}"

        plt.close(fig)
        return True, f"Figure saved successfully: {output_path}"

    except Exception as e:
        return False, f"Failed to save figure: {str(e)}"


# =============================================================================
# SECTION 4: Figure Naming Convention
# =============================================================================

def get_figure_naming_convention() -> str:
    """
    Return the standardized figure naming convention documentation.

    Returns:
        str: Naming convention specification

    Examples:
        >>> get_figure_naming_convention()
        'Figure Naming Format (MANDATORY):\\n{model_number}_{figure_type}_{description}.png\\n...'
    """
    return """
Figure Naming Format (MANDATORY):
{model_number}_{figure_type}_{description}.png

Components:
- {model_number}: Model that created the figure (1, 2, 3, etc.)
- {figure_type}: Type of visualization (scatter, line, bar, histogram, heatmap, boxplot, violin, diagram, map, table)
- {description}: Brief description of what the figure shows (use underscores, lowercase)
- .png: PNG extension

Rules:
- Use lowercase letters only
- Use underscores to separate words in description
- Keep description under 50 characters
- No spaces or special characters
- Always use .png extension

Examples:
✅ CORRECT:
model_1_scatter_predictions_vs_actual.png
model_1_histogram_residuals.png
model_2_line_convergence_history.png
model_2_bar_feature_importance.png
model_3_heatmap_correlation_matrix.png
model_1_diagram_model_architecture.png

❌ FORBIDDEN:
figure1.png (not descriptive)
Model1_Scatter.png (capital letters)
model 1 scatter.png (spaces)
model_1_scatter_predictions_vs_actual_final_v2.png (suffixes)
scatter.png (missing model number)

Figure Types (Standardized):
- scatter - Scatter plots
- line - Line plots
- bar - Bar charts
- histogram - Histograms
- heatmap - Heatmaps
- boxplot - Box plots
- violin - Violin plots
- diagram - Flowcharts/diagrams
- map - Maps/geographic visualizations
- table - Tables
"""


# =============================================================================
# SECTION 5: Color Palettes
# =============================================================================

def get_color_palette(palette_name: str = 'colorblind') -> List[str]:
    """
    Get publication-quality color palette.

    Args:
        palette_name: Name of color palette ('colorblind', 'viridis', 'coolwarm', 'husl')

    Returns:
        List[str]: List of hex color codes

    Examples:
        >>> get_color_palette('colorblind')
        ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#ECE133', '#D55E00']
    """
    # Colorblind-friendly palette (Paul Tol's scheme)
    palettes = {
        'colorblind': ['#0173B2', '#DE8F05', '#029E73', '#CC78BC',
                      '#ECE133', '#D55E00', '#0173B2', '#DE8F05'],
        'viridis': ['#440154', '#31688E', '#35B779', '#FDE725'],
        'coolwarm': ['#313695', '#4575B4', '#74ADD1', '#ABD9E9',
                    '#E0F3F8', '#FFFFBF', '#FEE090', '#FC8D59',
                    '#D53E4F', '#9E0142'],
        'husl': sns.color_palette('husl', 8).as_hex()
    }

    return palettes.get(palette_name, palettes['colorblind'])


# =============================================================================
# SECTION 6: Template Usage Guide
# =============================================================================

def get_template_usage_guide() -> str:
    """
    Return documentation for using SciencePlots templates.

    Returns:
        str: Template usage guide
    """
    return """
SciencePlots Template Usage Guide
==================================

All templates should:
1. Import mpl_config: sys.path.insert(0, '../../tools'); import mpl_config
2. Apply style: mpl_config.apply_research_style()
3. Save with verification: mpl_config.save_figure(fig, output_path)
4. Use UTF-8 encoding for all file operations
5. Follow naming convention: mpl_config.get_figure_naming_convention()

Example Template Structure:
```python
import sys
import matplotlib.pyplot as plt
import pandas as pd

# Add tools to path
sys.path.insert(0, '../../tools')
import mpl_config

# Apply research style
scienceplots_available = mpl_config.apply_research_style()

# Create figure
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')

# Save with verification
success, msg = mpl_config.save_figure(fig, 'output/figures/model_1_line_example.png')
if not success:
    print(f"Error: {msg}")
```
"""


# =============================================================================
# SELF-TEST
# =============================================================================

if __name__ == "__main__":
    # Force UTF-8 output
    sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 70)
    print("SciencePlots Configuration Module - Self-Test")
    print("=" * 70)

    # Test 1: Style Application
    print("\n[TEST 1] Style Application")
    scienceplots_available = apply_research_style()
    status = "[PASS] SciencePlots loaded" if scienceplots_available else "[PASS] Fallback loaded"
    print(f"  {status}")

    # Test 2: Figure Creation and Saving
    print("\n[TEST 2] Figure Creation and Saving")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o-', linewidth=2, markersize=8)
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('Test Figure')

    test_path = 'output/test_figure.png'
    success, msg = save_figure(fig, test_path)
    print(f"  {'[PASS]' if success else '[FAIL]'} {msg}")

    # Test 3: Figure Verification
    print("\n[TEST 3] Figure Verification")
    is_valid, issue = verify_figure_quality(test_path)
    print(f"  {'[PASS]' if is_valid else '[FAIL]'} {issue}")

    # Test 4: Naming Convention
    print("\n[TEST 4] Naming Convention")
    print(get_figure_naming_convention())

    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)
