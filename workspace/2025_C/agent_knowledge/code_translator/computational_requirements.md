# Computational Requirements Enforcement

> **Purpose**: This knowledge file documents the mandatory computational intensity requirements for model implementations. Code translators MUST implement computationally intensive methods (2-6 hours training) to meet MCM competition standards.
>
> **Source**: Extracted from code_translator.md lines 1205-1353
>
> **Critical**: Lightweight methods (Ridge, Lasso, basic sklearn) that train in seconds/minutes are FORBIDDEN. Only approved patterns that require 2-6 hours are acceptable.

---

## 🆔 Computational Requirements Enforcement (MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] You MUST implement computationally intensive methods (2-6 hours training).**

### Pre-Implementation Check

Verify **Computational Requirements** in `model_design.md`: **Required Training Time**: 2-6 hours per model

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

#### Pattern C: Large-Scale Ensemble Methods

```python
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train, **kwargs):
    """Train large-scale ensemble. Expected: 2-3 hours"""
    param_grid = {
        'n_estimators': [500, 1000, 2000],
        'max_depth': [10, 20, 30, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'learning_rate': [0.01, 0.05, 0.1]
    }

    model = GradientBoostingRegressor(random_state=42, warm_start=True)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    # Bootstrap ensemble
    n_bootstrap = 1000
    bootstrap_models = []
    for i in range(n_bootstrap):
        from sklearn.utils import resample
        X_boot, y_boot = resample(X_train, y_train, random_state=i)
        model = GradientBoostingRegressor(**grid_search.best_params_)
        model.fit(X_boot, y_boot)
        bootstrap_models.append(model)
    return {'best_model': grid_search.best_estimator_, 'bootstrap_models': bootstrap_models}
```

**Expected**: 2-3 hours (grid search + 1000 bootstrap models)

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
