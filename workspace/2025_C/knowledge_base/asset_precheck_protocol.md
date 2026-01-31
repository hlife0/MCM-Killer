# Phase 6.5: Asset Pre-Check Protocol (V2.0)

> **"Visualization Enhancement" Protocol**
> Before entering Phase 7 (Writing), ALL referenced image paths MUST be verified.
> Missing assets trigger @visualizer callback, NOT LaTeX compilation errors.

---

## Overview

The Asset Pre-Check ensures that all figures required for the paper exist and are valid before Phase 7 begins. This prevents LaTeX compilation failures due to missing or corrupt images.

---

## Asset Pre-Check Script

Save this script to `tools/asset_pre_check.py` and run before Phase 7:

```python
import os
import glob

def asset_pre_check(figures_dir="output/figures/", model_count=5):
    """
    Verify all expected figure files exist before Phase 7.

    Args:
        figures_dir: Path to figures directory
        model_count: Number of models (from model_design.md)

    Returns:
        (passed: bool, missing_files: list, issues: list)
    """
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


def run_pre_check():
    """Run the pre-check and print results."""
    passed, missing, issues = asset_pre_check()

    if not passed:
        print("=" * 60)
        print("⚠️ ASSET PRE-CHECK FAILED - DO NOT ENTER PHASE 7")
        print("=" * 60)
        if missing:
            print("\nMissing Files:")
            for m in missing:
                print(f"  ❌ {m}")
        if issues:
            print("\nFile Issues:")
            for i in issues:
                print(f"  ⚠️ {i}")
        print("\nACTION: Callback @visualizer to regenerate missing/corrupt figures")
        return False
    else:
        print("✅ Asset Pre-Check PASSED - Ready for Phase 7")
        return True


if __name__ == "__main__":
    import sys
    success = run_pre_check()
    sys.exit(0 if success else 1)
```

---

## Usage Examples

### Example 1: Basic Pre-Check

```bash
# From workspace root
python tools/asset_pre_check.py
```

**Output (Pass)**:
```
✅ Asset Pre-Check PASSED - Ready for Phase 7
```

**Output (Fail)**:
```
============================================================
⚠️ ASSET PRE-CHECK FAILED - DO NOT ENTER PHASE 7
============================================================

Missing Files:
  ❌ model_3_*.png (no figures for Model 3)
  ❌ model_5_*.png (no figures for Model 5)

File Issues:
  ⚠️ EMPTY: output/figures/model_2_scatter_residuals.png
  ⚠️ CORRUPT: output/figures/model_1_line_trend.png (invalid PNG header)

ACTION: Callback @visualizer to regenerate missing/corrupt figures
```

### Example 2: Director Workflow

```
@director: Before Phase 7, run asset pre-check.

1. Execute: python tools/asset_pre_check.py
2. If exit code != 0:
   - Call @visualizer: "Regenerate missing/corrupt figures: [list from output]"
   - Wait for @visualizer completion
   - Re-run: python tools/asset_pre_check.py
   - Loop until exit code == 0
3. If exit code == 0:
   - Proceed to Phase 7A
```

### Example 3: @visualizer Callback Format

When pre-check fails, Director sends this to @visualizer:

```
@visualizer: Asset pre-check failed. Please regenerate the following:

Missing Figures (no figures exist for these models):
- Model 3: Need at least one figure (e.g., model_3_scatter_*.png)
- Model 5: Need at least one figure (e.g., model_5_line_*.png)

Corrupt/Empty Figures (regenerate these specific files):
- output/figures/model_2_scatter_residuals.png (empty file)
- output/figures/model_1_line_trend.png (corrupt PNG header)

After regeneration, report back for re-check.
```

---

## Phase 6.5 Protocol Table

| Step | Action | On Failure |
|------|--------|------------|
| 1 | Run `python tools/asset_pre_check.py` | - |
| 2 | Check exit code | - |
| 3 | If exit code != 0 | Callback @visualizer with missing/corrupt list |
| 4 | Wait for @visualizer | - |
| 5 | Re-run pre-check | Loop until passed |
| 6 | Exit code == 0 | Enter Phase 7A |

---

## Integration with Chart Diversity

The Asset Pre-Check works together with Chart Diversity Enforcement:

1. **@visualizer** generates figures with diversity (Phase 6)
2. **@visualizer** produces Chart Diversity Report (Phase 6)
3. **Director** runs Asset Pre-Check (Phase 6.5)
4. If failed → **@visualizer** regenerates (Phase 6.5 loop)
5. If passed → **@writer** begins Phase 7A

---

## Verification Checklist

- [ ] `tools/asset_pre_check.py` exists and is executable
- [ ] Pre-check runs before every Phase 7 entry
- [ ] Missing figures trigger @visualizer callback (not Phase 7 failure)
- [ ] Corrupt figures are detected (empty files, invalid PNG headers)
- [ ] Loop continues until all figures pass
- [ ] No LaTeX compilation errors from missing figures

---

## Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| "No figures for Model X" | Model training didn't produce visualizable results | Check results_{i}.csv exists, then @visualizer |
| "Empty file" | Script crashed mid-save | @visualizer regenerate specific file |
| "Invalid PNG header" | File corruption during write | @visualizer regenerate specific file |
| "UNREADABLE" | Permission or path issue | Check file permissions, path validity |

---

## Notes

- The pre-check is **mandatory** before Phase 7
- The script expects figures to follow naming convention: `model_{i}_{type}_{description}.png`
- Adjust `model_count` parameter if fewer/more models are used
- The script exits with code 0 (pass) or 1 (fail) for automation
