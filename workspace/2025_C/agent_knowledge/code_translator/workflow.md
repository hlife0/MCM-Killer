# Code Translation Workflow

**Agent**: code_translator
**Source**: Originally embedded in `.claude/agents/code_translator.md`
**Purpose**: Step-by-step workflow for translating math models to Python code

---

## Step 1: Read Model Design (AND Design Expectations Table)

```
Read: output/model_design.md
```

**Extract**: Objective functions, constraints, variables/parameters, algorithms/procedures, input/output specifications

---

## Step 2: Load Features

```python
import pickle
import pandas as pd

with open('output/implementation/data/features_1.pkl', 'rb') as f:
    features = pickle.load(f)
print(f"Features loaded: {features.shape}")
```

---

## Step 3: Implement Model Code

See `code_structure_template.md` for the standard code structure.

---

## Step 4: Create Test Suite

**Standard Test Structure (MANDATORY)**:

```python
#!/usr/bin/env python3
"""Test Suite for Model {i} - Tests: model_{i}.py"""

import pandas as pd
import numpy as np
import pickle
import sys
from model_{i} import load_features, prepare_data, train_model, predict

def test_load_features():
    """Test feature loading."""
    print("Testing load_features()...")
    features = load_features('output/implementation/data/features_1.pkl')
    assert features is not None, "Features is None"
    assert isinstance(features, pd.DataFrame), "Features is not DataFrame"
    assert len(features) > 0, "Features is empty"
    print("✅ test passed")

def test_prepare_data():
    """Test data preparation."""
    print("Testing prepare_data()...")
    features = load_features('output/implementation/data/features_1.pkl')
    X_train, X_test, y_train, y_test = prepare_data(features)
    assert X_train is not None and y_train is not None
    print("✅ test passed")

def test_train_model():
    """Test model training (quick test with subset)."""
    print("Testing train_model()...")
    features = load_features('output/implementation/data/features_1.pkl')
    X_train, X_test, y_train, y_test = prepare_data(features)
    X_subset = X_train.head(10)
    y_subset = y_train.head(10)
    model = train_model(X_subset, y_subset, test_mode=True)
    assert model is not None
    print("✅ test passed")

def test_predict():
    """Test predictions."""
    print("Testing predict()...")
    features = load_features('output/implementation/data/features_1.pkl')
    X_train, X_test, y_train, y_test = prepare_data(features)
    X_subset = X_train.head(10)
    y_subset = y_train.head(10)
    model = train_model(X_subset, y_subset, test_mode=True)
    predictions = predict(model, X_test.head(5))
    assert predictions is not None and len(predictions) == 5
    print("✅ test passed")

def run_all_tests():
    """Run all tests."""
    print("\n" + "="*50)
    print(f"Running Test Suite for Model {i}")
    print("="*50 + "\n")
    try:
        test_load_features()
        test_prepare_data()
        test_train_model()
        test_predict()
        print("\n" + "="*50)
        print("✅ ALL TESTS PASSED")
        print("="*50)
        return 0
    except (AssertionError, Exception) as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
```

---

## Step 5: Execute Tests (MANDATORY)

```bash
source output/venv/bin/activate
python output/implementation/code/test_{i}.py
```

**ALL TESTS MUST PASS before reporting completion.**

---

## Step 6: Save Files

- `output/implementation/code/model_{i}.py`
- `output/implementation/code/test_{i}.py`

---

## Iteration and Re-verification

### The Revision-Verification Cycle

**When you receive feedback**:
1. Read feedback carefully
2. Make revisions
3. Re-run tests
4. Request re-verification from @validator

```
Director, I have completed the revisions based on feedback from @validator.
Changes made:
- [List each code change]
- Re-ran tests: [all passed / specific results]

Please send to @validator for RE-VERIFICATION to confirm the issues are resolved.
```

**DO NOT**:
- ❌ Assume revisions are "good enough" without verification
- ❌ Mark task as complete without re-verification
- ❌ Skip re-running tests after changes
