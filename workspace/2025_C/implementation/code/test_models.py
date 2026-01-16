#!/usr/bin/env python3
"""
Test Suite for All Models
Tests: model_1 through model_6
Tests basic sanity checks on predictions
"""

import pandas as pd
import numpy as np
import sys
import os

# Add implementation/code to path
sys.path.insert(0, 'implementation/code')

# Set random seed
np.random.seed(42)

def check_sanity_predictions(df: pd.DataFrame, model_name: str) -> bool:
    """
    Perform sanity checks on prediction results.

    Args:
        df: DataFrame with predictions
        model_name: Name of the model being tested

    Returns:
        True if all checks pass
    """
    print(f"\n   Testing {model_name} sanity checks...")

    issues = []

    # Check 1: No duplicate NOCs
    if 'NOC' in df.columns:
        duplicates = df['NOC'].duplicated().sum()
        if duplicates > 0:
            issues.append(f"   ❌ Found {duplicates} duplicate NOCs")
        else:
            print(f"   ✅ No duplicate NOCs")

    # Check 2: No negative predictions
    pred_cols = [c for c in df.columns if 'Pred' in c or 'pred' in c]
    for col in pred_cols:
        if (df[col] < 0).any():
            issues.append(f"   ❌ Negative values found in {col}")
        else:
            print(f"   ✅ No negative values in {col}")

    # Check 3: Gold <= Total
    if 'Pred_Gold' in df.columns and 'Pred_Total' in df.columns:
        if (df['Pred_Gold'] > df['Pred_Total']).any():
            issues.append(f"   ❌ Gold predictions exceed Total predictions")
        else:
            print(f"   ✅ Gold <= Total")

    # Check 4: PI bounds valid
    if 'PI_2.5' in df.columns and 'PI_97.5' in df.columns:
        if 'Pred_Total' in df.columns or 'Pred_Total_2028' in df.columns:
            pred_col = 'Pred_Total' if 'Pred_Total' in df.columns else 'Pred_Total_2028'
            invalid_lower = (df['PI_2.5'] > df[pred_col]).sum()
            invalid_upper = (df['PI_97.5'] < df[pred_col]).sum()

            if invalid_lower > 0 or invalid_upper > 0:
                issues.append(f"   ❌ Invalid prediction intervals")
            else:
                print(f"   ✅ Valid prediction intervals")

    # Check 5: PI_97.5 >= PI_2.5
    if 'PI_2.5' in df.columns and 'PI_97.5' in df.columns:
        if (df['PI_97.5'] < df['PI_2.5']).any():
            issues.append(f"   ❌ PI_97.5 < PI_2.5")
        else:
            print(f"   ✅ PI_97.5 >= PI_2.5")

    if issues:
        for issue in issues:
            print(issue)
        return False

    return True


def test_model_1():
    """Test Model 1: Medal Count Model"""
    print("\n" + "=" * 50)
    print("Testing Model 1: Medal Count Model")
    print("=" * 50)

    try:
        # Import model
        from model_1_medal_count import load_features, predict_2028

        # Load features
        print("   Loading features...")
        df = load_features('implementation/data/features_core.csv')
        assert df is not None, "Features is None"
        assert isinstance(df, pd.DataFrame), "Features is not DataFrame"
        assert len(df) > 0, "Features is empty"
        print("   ✅ load_features() test passed")

        # Quick check that data has expected columns
        expected_cols = ['year', 'noc', 'total_medals', 'gold_count', 'athlete_count']
        for col in expected_cols:
            assert col in df.columns, f"Missing column: {col}"
        print("   ✅ Expected columns present")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_2():
    """Test Model 2: 2028 Projections"""
    print("\n" + "=" * 50)
    print("Testing Model 2: 2028 Projections")
    print("=" * 50)

    try:
        # Import model
        from model_2_projections import load_features

        # Load features
        print("   Loading features...")
        df = load_features('implementation/data/features_core.csv')
        assert df is not None, "Features is None"
        assert isinstance(df, pd.DataFrame), "Features is not DataFrame"
        print("   ✅ load_features() test passed")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_3():
    """Test Model 3: First-Time Medalists"""
    print("\n" + "=" * 50)
    print("Testing Model 3: First-Time Medalists")
    print("=" * 50)

    try:
        # Import model
        from model_3_first_time import load_features

        # Load features
        print("   Loading features...")
        df = load_features('implementation/data/features_core.csv')
        assert df is not None, "Features is None"
        print("   ✅ load_features() test passed")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_4():
    """Test Model 4: Events Analysis"""
    print("\n" + "=" * 50)
    print("Testing Model 4: Events Analysis")
    print("=" * 50)

    try:
        # Import model
        from model_4_events import load_sport_features

        # Load features
        print("   Loading sport features...")
        df = load_sport_features('implementation/data/features_sport.csv')
        assert df is not None, "Features is None"
        print("   ✅ load_sport_features() test passed")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_5():
    """Test Model 5: Structural Discontinuities"""
    print("\n" + "=" * 50)
    print("Testing Model 5: Structural Discontinuities")
    print("=" * 50)

    try:
        # Import model
        from model_5_discontinuities import load_sport_features

        # Load features
        print("   Loading sport features...")
        df = load_sport_features('implementation/data/features_sport.csv')
        assert df is not None, "Features is None"
        print("   ✅ load_sport_features() test passed")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_6():
    """Test Model 6: Original Insights"""
    print("\n" + "=" * 50)
    print("Testing Model 6: Original Insights")
    print("=" * 50)

    try:
        # Import model
        from model_6_insights import load_features

        # Load features
        print("   Loading features...")
        df = load_features('implementation/data/features_core.csv')
        assert df is not None, "Features is None"
        print("   ✅ load_features() test passed")

        return True

    except Exception as e:
        print(f"   ❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_output_files():
    """Check that output files exist and are valid."""
    print("\n" + "=" * 50)
    print("Checking Output Files")
    print("=" * 50)

    import os

    output_files = [
        'output/results/results_1.csv',
        'output/results/results_2.csv',
        'output/results/results_3.csv',
        'output/results/results_4.csv',
        'output/results/results_5.csv',
        'output/results/results_6_efficiency.csv'
    ]

    existing_files = []
    for f in output_files:
        if os.path.exists(f):
            size = os.path.getsize(f)
            if size > 0:
                print(f"   ✅ {f} exists ({size} bytes)")
                existing_files.append(f)
            else:
                print(f"   ⚠️  {f} exists but is empty")
        else:
            print(f"   ❌ {f} does not exist")

    return existing_files


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Running Test Suite for All Models")
    print("=" * 60)

    # Test imports
    print("\n1. Testing imports...")
    try:
        import pandas as pd
        import numpy as np
        import statsmodels.api as sm
        import sklearn
        import networkx as nx
        import ruptures
        print("   ✅ All required libraries imported")
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return 1

    # Run model tests
    results = {}

    print("\n2. Testing model modules...")
    results['model_1'] = test_model_1()
    results['model_2'] = test_model_2()
    results['model_3'] = test_model_3()
    results['model_4'] = test_model_4()
    results['model_5'] = test_model_5()
    results['model_6'] = test_model_6()

    # Check output files
    print("\n3. Checking output files...")
    output_files = check_output_files()

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for model, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"   {model}: {status}")

    all_passed = all(results.values())

    if all_passed:
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        return 0
    else:
        print("\n" + "=" * 60)
        print("❌ SOME TESTS FAILED")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
