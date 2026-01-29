#!/usr/bin/env python3
"""
Unit Test Template for Model Components
Protocol 17: Model Component Testing

This template shows the REQUIRED unit test structure for all model_{i}.py files.
Copy this template and customize for each model.
"""

import numpy as np
import pandas as pd


def generate_synthetic_test_data(n_rows=100, n_features=10):
    """
    Generate synthetic data for unit testing.

    Args:
        n_rows: Number of rows (default: 100 for quick testing)
        n_features: Number of features

    Returns:
        X, y: Feature matrix and target vector
    """
    np.random.seed(42)
    X = np.random.randn(n_rows, n_features)
    y = np.random.randn(n_rows)
    return X, y


def validate_dimensions(X, y, model_name, expected_features):
    """
    Validate input dimensions match expected shape.

    Args:
        X: Feature matrix
        y: Target vector
        model_name: Name of model (for error message)
        expected_features: Expected number of features

    Raises:
        ValueError: If dimensions don't match expected shape
    """
    n_samples, n_features = X.shape

    if n_features != expected_features:
        raise ValueError(
            f"{model_name} dimension error:\n"
            f"  Expected features: {expected_features}\n"
            f"  Actual features: {n_features}\n"
            f"  Shape: {X.shape}\n"
            f"  Check feature selection or data preprocessing!"
        )

    if n_samples != y.shape[0]:
        raise ValueError(
            f"{model_name} sample count mismatch:\n"
            f"  X samples: {n_samples}\n"
            f"  y samples: {y.shape[0]}\n"
            f"  Check data alignment!"
        )

    print(f"✓ {model_name} dimensions validated: {X.shape} → {y.shape}")


# ============================================================================
# MODEL-SPECIFIC IMPLEMENTATION GOES HERE
# ============================================================================

class ExampleModel:
    """Example model class - replace with your actual model."""

    def __init__(self, n_features=10):
        self.n_features = n_features
        self.params = None

    def fit(self, X, y):
        """Fit model to data."""
        validate_dimensions(X, y, "ExampleModel", self.n_features)
        # Your fitting logic here
        self.params = np.random.randn(self.n_features)
        return self

    def predict(self, X):
        """Make predictions."""
        if X.shape[1] != self.n_features:
            raise ValueError(f"Expected {self.n_features} features, got {X.shape[1]}")
        return X @ self.params


# ============================================================================
# UNIT TESTS (REQUIRED FOR PROTOCOL 17)
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Running Model Unit Tests (Protocol 17)")
    print("=" * 60)

    # Test 1: Dimension verification
    print("\n[Test 1] Dimension verification...")
    X, y = generate_synthetic_test_data(n_rows=100, n_features=10)
    assert X.shape == (100, 10), f"Expected (100, 10), got {X.shape}"
    print("✓ Test 1 passed: Dimension verification")

    # Test 2: Feature preprocessing
    print("\n[Test 2] Feature preprocessing...")
    # Add your preprocessing tests here
    X_processed = X  # Replace with actual preprocessing
    assert X_processed.shape == (100, 10), f"Expected (100, 10), got {X_processed.shape}"
    print("✓ Test 2 passed: Feature preprocessing")

    # Test 3: Model initialization
    print("\n[Test 3] Model initialization...")
    model = ExampleModel(n_features=10)
    assert model is not None, "Model initialization failed"
    print("✓ Test 3 passed: Model initialization")

    # Test 4: Forward pass
    print("\n[Test 4] Forward pass...")
    model.fit(X, y)
    predictions = model.predict(X)
    assert predictions.shape == (100,), f"Expected (100,), got {predictions.shape}"
    print("✓ Test 4 passed: Forward pass")

    # Test 5: Dimension validation function
    print("\n[Test 5] Dimension validation function...")
    validate_dimensions(X, y, "TestModel", 10)
    print("✓ Test 5 passed: Dimension validation function")

    print("\n" + "=" * 60)
    print("✅ ALL UNIT TESTS PASSED (Protocol 17)")
    print("=" * 60)
