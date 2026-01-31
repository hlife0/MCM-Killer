#!/usr/bin/env python3
"""
Asset Pre-Check Tool (V2.0)
Verifies all expected figure files exist before Phase 7.

Usage:
    python tools/asset_pre_check.py
    python tools/asset_pre_check.py --figures-dir output/figures/ --model-count 5

Purpose:
    Prevents LaTeX compilation failures due to missing or corrupt images.
    Part of the "Visualization Enhancement" Protocol (V2.0).

Exit Codes:
    0 = All checks passed, ready for Phase 7
    1 = Checks failed, need @visualizer callback
"""

import os
import glob
import argparse
import sys


def asset_pre_check(figures_dir="output/figures/", model_count=5):
    """
    Verify all expected figure files exist before Phase 7.

    Args:
        figures_dir: Path to figures directory
        model_count: Number of models (from model_design.md)

    Returns:
        (passed: bool, missing_files: list, issues: list)
    """
    # Ensure figures_dir exists
    if not os.path.exists(figures_dir):
        return False, [f"Figures directory does not exist: {figures_dir}"], []

    # Get all existing figures
    existing_figures = set(glob.glob(f"{figures_dir}*.png"))
    existing_names = {os.path.basename(f) for f in existing_figures}

    missing = []
    issues = []

    # Verify file integrity
    for fig_path in existing_figures:
        # Check file size
        if os.path.getsize(fig_path) == 0:
            issues.append(f"EMPTY: {fig_path}")
            continue

        # Check file is readable and valid PNG
        try:
            with open(fig_path, 'rb') as f:
                header = f.read(8)
                # PNG signature check
                if not header.startswith(b'\x89PNG'):
                    issues.append(f"CORRUPT: {fig_path} (invalid PNG header)")
        except Exception as e:
            issues.append(f"UNREADABLE: {fig_path} ({e})")

    # Check minimum expected figures per model
    for i in range(1, model_count + 1):
        has_any = any(f"model_{i}_" in name for name in existing_names)
        if not has_any:
            missing.append(f"model_{i}_*.png (no figures for Model {i})")

    passed = len(missing) == 0 and len(issues) == 0
    return passed, missing, issues


def run_pre_check(figures_dir="output/figures/", model_count=5):
    """Run the pre-check and print results."""
    passed, missing, issues = asset_pre_check(figures_dir, model_count)

    if not passed:
        print("=" * 60)
        print("ASSET PRE-CHECK FAILED - DO NOT ENTER PHASE 7")
        print("=" * 60)
        if missing:
            print("\nMissing Files:")
            for m in missing:
                print(f"  [X] {m}")
        if issues:
            print("\nFile Issues:")
            for i in issues:
                print(f"  [!] {i}")
        print("\nACTION: Callback @visualizer to regenerate missing/corrupt figures")
        return False
    else:
        print("[OK] Asset Pre-Check PASSED - Ready for Phase 7")
        print(f"     Total figures found: {len(glob.glob(f'{figures_dir}*.png'))}")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Asset Pre-Check Tool for Phase 6.5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--figures-dir",
        default="output/figures/",
        help="Path to figures directory (default: output/figures/)"
    )
    parser.add_argument(
        "--model-count",
        type=int,
        default=5,
        help="Number of models to check figures for (default: 5)"
    )

    args = parser.parse_args()
    success = run_pre_check(args.figures_dir, args.model_count)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
