# Standard Python Code Structure

**Agent**: code_translator
**Source**: Originally embedded in `.claude/agents/code_translator.md`
**Purpose**: Standard template for model implementation code

---

## Standard Code Structure (MANDATORY)

```python
#!/usr/bin/env python3
"""
Model {i} Implementation
Based on: output/model_design.md
Translated by: @code_translator
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional
import pickle

# Model-specific imports (add sklearn, scipy, statsmodels as needed)

def load_features(path: str) -> pd.DataFrame:
    """Load feature data from pickle file."""
    with open(path, 'rb') as f:
        features = pickle.load(f)
    print(f"Loaded features: {features.shape}")
    return features

def prepare_data(features: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Prepare data for model training."""
    # Implement per model_design.md: Train/test split, Feature scaling, Missing value imputation
    pass

def train_model(X_train: pd.DataFrame, y_train: pd.DataFrame, **kwargs) -> Dict:
    """Train the model."""
    # Implement training algorithm from model_design.md
    pass

def predict(model: Dict, X: pd.DataFrame) -> np.ndarray:
    """Make predictions using trained model."""
    # Implement prediction logic
    pass

def save_model(model: Dict, path: str):
    """Save trained model to file."""
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {path}")

def main():
    """Main execution function."""
    print("="*50)
    print(f"Model {i} Implementation")
    print("="*50)

    features = load_features('output/implementation/data/features_1.pkl')
    X_train, X_test, y_train, y_test = prepare_data(features)
    model = train_model(X_train, y_train, **hyperparameters)
    save_model(model, 'output/implementation/models/model_1.pkl')
    print("✅ Model implementation complete")

if __name__ == "__main__":
    main()
```

---

## UTF-8 Enforcement (CRITICAL)

> **"ALWAYS use UTF-8 encoding when writing files."**

**MANDATORY Rules for ALL Python Code**:
1. **ALWAYS specify `encoding='utf-8'`** in Python file operations
2. **NEVER use default system encoding** (platform-dependent)
3. **For code files**: Add `# -*- coding: utf-8 -*-` at top
4. **For data files**: Use `encoding='utf-8'` in `read_csv()`, `to_csv()`
5. **For print statements**: Use `sys.stdout.reconfigure(encoding='utf-8')` if needed

**Example**:
```python
import sys
import io

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Read/write with UTF-8
df = pd.read_csv('data.csv', encoding='utf-8')
df.to_csv('output.csv', index=False, encoding='utf-8')

# Write text files
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
```

**Why This Matters**: Special characters, mathematical symbols, and non-English text will corrupt without UTF-8.

---

## Code Quality Standards

### Mandatory Requirements

✅ **Code MUST**:
- Follow PEP 8
- Include docstrings
- Handle missing data
- Use random seeds
- Include error handling
- Be executable without manual intervention

❌ **Code MUST NOT**:
- Use hardcoded values
- Have infinite loops
- Ignore exceptions silently
- Assume data exists without checking
- Use print statements for debugging in production

### Reproducibility

```python
# ALWAYS set random seeds
np.random.seed(42)
if hasattr(torch, 'manual_seed'):
    torch.manual_seed(42)
```

---

## Numerical Stability Engineering

**Anti-Explosion Protocols**:
- **Log-Space**: Do probability calculations in log-space (`logsumexp`)
- **Clipping**: Clip gradients and values to safe ranges (`np.clip(x, 1e-9, 1-1e-9)`)
- **Scaling**: Standardize inputs (handled by @data_engineer, but check it)

**Example**:
```python
# ❌ Risky
likelihood = np.prod(probs)

# ✅ Stable
log_likelihood = np.sum(np.log(probs + 1e-10))
```

---

## Computational Requirements

**Verify** `Computational Requirements` in `model_design.md`:
- **Required Training Time**: 2-6 hours per model

### ✅ Approved Implementation Patterns

#### Pattern A: Bayesian Hierarchical Models (RECOMMENDED)

```python
import pymc as pm

def train_model(X_train, y_train, **kwargs):
    """Train Bayesian Hierarchical Model. Expected: 3-5 hours"""
    with pm.Model() as hierarchical_model:
        # Hyperpriors
        mu_alpha = pm.Normal('mu_alpha', mu=0, sigma=10)
        sigma_alpha = pm.HalfCauchy('sigma_alpha', beta=2)
        alpha = pm.Normal('alpha', mu=mu_alpha, sigma=sigma_alpha, shape=n_countries)
        beta = pm.Normal('beta', mu=0, sigma=10, shape=n_features)
        sigma = pm.HalfCauchy('sigma', beta=2)
        mu = alpha[country_idx] + pm.math.dot(X_train, beta)
        pm.Normal('y', mu=mu, sigma=sigma, observed=y_train)

        # MCMC sampling (COMPUTATIONALLY INTENSIVE)
        trace = pm.sample(draws=2000, tune=1000, chains=4, cores=4, target_accept=0.95)
    return {'model': hierarchical_model, 'trace': trace}
```

**Expected**: 3-5 hours (2000 samples × 4 chains with NUTS)

#### Pattern B: Deep Neural Networks

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

class DeepModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(256, 128), nn.BatchNorm1d(128), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(128, 64), nn.BatchNorm1d(64), nn.ReLU(), nn.Dropout(0.2),
            nn.Linear(64, 1)
        )
    def forward(self, x):
        return self.network(x)

def train_model(X_train, y_train, **kwargs):
    """Train deep neural network. Expected: 2-4 hours"""
    X_tensor = torch.FloatTensor(X_train.values)
    y_tensor = torch.FloatTensor(y_train.values)
    dataset = TensorDataset(X_tensor, y_tensor)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = DeepModel(input_dim=X_train.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    n_epochs = 5000  # 5000+ epochs
    for epoch in range(n_epochs):
        model.train()
        for X_batch, y_batch in dataloader:
            optimizer.zero_grad()
            predictions = model(X_batch).squeeze()
            loss = criterion(predictions, y_batch)
            loss.backward()
            optimizer.step()
    return {'model': model}
```

**Expected**: 2-4 hours (5000+ epochs with backpropagation)

### ❌ FORBIDDEN Implementation Patterns

**DO NOT implement lightweight methods**:
```python
# ❌ FORBIDDEN: Ridge/Lasso (trains in seconds)
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)  # < 1 minute

# ❌ FORBIDDEN: Basic sklearn defaults
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()  # Default parameters
model.fit(X_train, y_train)  # < 5 minutes

# ❌ FORBIDDEN: Simple analytical solutions
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)  # < 10 seconds
```

### Implementation Verification

Before reporting completion:
```python
import time

def train_model(X_train, y_train, **kwargs):
    start_time = time.time()
    # ... implementation ...
    elapsed_time = time.time() - start_time
    print(f"Training completed in {elapsed_time/3600:.2f} hours")

    if elapsed_time < 3600:  # Less than 1 hour
        raise ValueError(f"Training time ({elapsed_time/60:.1f} min) is below 2-6 hour minimum. Use more intensive method.")
    return model
```
