# Model 6: Flagship Implementation Requirements

> **Purpose**: This file contains implementation specifications for the flagship Model 6 (Mechanism Design) including required functions, data structures, and output schemas.

## Overview

Model 6 requires specialized implementation components to support mechanism design optimization, KKT verification, and counterfactual backtesting.

---

## Required Implementation Components

### 1. MechanismParams Dataclass

```python
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
import numpy as np
import pandas as pd

@dataclass
class MechanismParams:
    """Control variables for mechanism design.

    Attributes:
        theta1: Judge score weight [0.1, 0.9]
        theta2: Vote aggregation method {0=plurality, 1=Borda, 2=approval}
        theta3: Temporal discount factor [0.5, 1.0]
        theta4: Save threshold [0, 0.2]
        theta5: Tiebreaker rule {0=fan, 1=judge, 2=random}
    """
    theta1: float  # Judge score weight [0.1, 0.9]
    theta2: int    # Vote aggregation method {0=plurality, 1=Borda, 2=approval}
    theta3: float  # Temporal discount factor [0.5, 1.0]
    theta4: float  # Save threshold [0, 0.2]
    theta5: int    # Tiebreaker rule {0=fan, 1=judge, 2=random}

    @classmethod
    def status_quo(cls) -> 'MechanismParams':
        """Default/current mechanism parameters."""
        return cls(0.5, 0, 1.0, 0.15, 0)

    @classmethod
    def optimal(cls) -> 'MechanismParams':
        """Optimal mechanism parameters from optimization."""
        return cls(0.35, 1, 0.85, 0.08, 1)

    def to_array(self) -> np.ndarray:
        """Convert to numpy array for optimization."""
        return np.array([self.theta1, self.theta2, self.theta3, self.theta4, self.theta5])

    @classmethod
    def from_array(cls, arr: np.ndarray) -> 'MechanismParams':
        """Create from numpy array."""
        return cls(
            theta1=float(arr[0]),
            theta2=int(round(arr[1])),
            theta3=float(arr[2]),
            theta4=float(arr[3]),
            theta5=int(round(arr[4]))
        )
```

---

### 2. StakeholderWeights Dataclass

```python
@dataclass
class StakeholderWeights:
    """Weights for different stakeholder utilities in welfare function."""
    omega_fan: float = 0.4
    omega_judge: float = 0.3
    omega_producer: float = 0.3

    def __post_init__(self):
        total = self.omega_fan + self.omega_judge + self.omega_producer
        assert abs(total - 1.0) < 1e-6, f"Weights must sum to 1, got {total}"
```

---

### 3. SeasonResult Dataclass

```python
@dataclass
class SeasonResult:
    """Results from applying mechanism to a single season."""
    season_id: int
    eliminations: List[str]  # Ordered list of eliminated contestants
    fairness_score: float    # Skill-outcome correlation
    engagement_score: float  # Fan utility metric
    producer_score: float    # Simplicity/predictability metric
```

---

### 4. Welfare Computation Function

```python
def compute_welfare(params: MechanismParams,
                   results: List[SeasonResult],
                   weights: StakeholderWeights = None) -> float:
    """
    Compute social welfare W(θ) = ω_F·E[U_fan] + ω_J·E[U_judge] + ω_P·E[U_prod]

    Parameters:
        params: Mechanism control variables
        results: Backtesting results from all seasons
        weights: Stakeholder weights (default: [0.4, 0.3, 0.3])

    Returns:
        Social welfare value (higher is better)

    Example:
        >>> params = MechanismParams.optimal()
        >>> results = backtest_mechanism(season_data, params)
        >>> welfare = compute_welfare(params, results)
        >>> print(f"Welfare: {welfare:.4f}")
    """
    if weights is None:
        weights = StakeholderWeights()

    n = len(results)
    if n == 0:
        return 0.0

    # Average utilities across seasons
    avg_fan = sum(r.engagement_score for r in results) / n
    avg_judge = sum(r.fairness_score for r in results) / n  # Proxy for judge influence
    avg_producer = sum(r.producer_score for r in results) / n

    welfare = (weights.omega_fan * avg_fan +
               weights.omega_judge * avg_judge +
               weights.omega_producer * avg_producer)

    return welfare
```

---

### 5. KKT Verification Function

```python
def verify_kkt_conditions(params: MechanismParams,
                          gradient: np.ndarray,
                          hessian: np.ndarray,
                          tol: float = 1e-2) -> Dict[str, Any]:
    """
    Verify Karush-Kuhn-Tucker conditions at optimal point.

    Parameters:
        params: Mechanism parameters to verify
        gradient: Gradient of welfare function at params
        hessian: Hessian matrix of welfare function at params
        tol: Tolerance for numerical checks (default: 0.01)

    Returns:
        Dictionary with verification results:
        {
            'stationarity': bool,      # ||∇W|| < tol
            'gradient_norm': float,
            'primal_feasibility': bool,
            'second_order': bool,      # Hessian NSD
            'hessian_eigenvalues': List[float],
            'kkt_satisfied': bool      # All conditions met
        }

    Example:
        >>> params = MechanismParams.optimal()
        >>> grad = compute_gradient(params)
        >>> hess = compute_hessian(params)
        >>> kkt = verify_kkt_conditions(params, grad, hess)
        >>> print(f"KKT satisfied: {kkt['kkt_satisfied']}")
    """
    # Stationarity: ||∇W(θ*)|| < tol
    gradient_norm = np.linalg.norm(gradient)
    stationarity = gradient_norm < tol

    # Primal feasibility: θ in Θ (bounds check)
    primal_feasibility = (
        0.1 <= params.theta1 <= 0.9 and
        params.theta2 in [0, 1, 2] and
        0.5 <= params.theta3 <= 1.0 and
        0.0 <= params.theta4 <= 0.2 and
        params.theta5 in [0, 1, 2]
    )

    # Second-order: Hessian is negative semi-definite
    eigenvalues = np.linalg.eigvalsh(hessian)
    second_order = all(ev <= tol for ev in eigenvalues)

    kkt_satisfied = stationarity and primal_feasibility and second_order

    return {
        'stationarity': stationarity,
        'gradient_norm': float(gradient_norm),
        'primal_feasibility': primal_feasibility,
        'second_order': second_order,
        'hessian_eigenvalues': eigenvalues.tolist(),
        'kkt_satisfied': kkt_satisfied
    }
```

---

### 6. Backtesting Function

```python
def backtest_mechanism(season_data: List[Tuple],
                       params: MechanismParams) -> List[SeasonResult]:
    """
    Apply mechanism to historical data and compute counterfactuals.

    Parameters:
        season_data: List of (judge_scores, vote_shares, contestant_names) per season
                    - judge_scores: DataFrame with columns [contestant, episode, score]
                    - vote_shares: DataFrame with columns [contestant, episode, share]
                    - contestant_names: List of contestant names
        params: Mechanism parameters to test

    Returns:
        List of SeasonResult with eliminations, fairness, engagement per season

    Example:
        >>> season_data = load_historical_data()
        >>> sq_results = backtest_mechanism(season_data, MechanismParams.status_quo())
        >>> opt_results = backtest_mechanism(season_data, MechanismParams.optimal())
    """
    results = []

    for season_id, (judges, votes, names) in enumerate(season_data):
        # Normalize judge scores
        j_norm = (judges - judges.min()) / (judges.max() - judges.min() + 1e-10)

        # Compute cumulative votes with temporal discounting
        v_cum = compute_cumulative_votes(votes, params.theta3)

        # Combine scores
        combined = params.theta1 * j_norm + (1 - params.theta1) * v_cum

        # Determine eliminations
        eliminations = determine_eliminations(combined, params.theta4, params.theta5)

        # Compute metrics
        fairness = compute_skill_correlation(eliminations, names)
        engagement = compute_engagement_score(votes, eliminations)
        producer = compute_producer_score(eliminations)

        results.append(SeasonResult(
            season_id=season_id,
            eliminations=eliminations,
            fairness_score=fairness,
            engagement_score=engagement,
            producer_score=producer
        ))

    return results
```

---

### 7. Statistical Tests Function

```python
def run_statistical_tests(sq_results: List[SeasonResult],
                          opt_results: List[SeasonResult]) -> Dict[str, Dict]:
    """
    Run statistical tests comparing status quo vs proposed mechanism.

    Parameters:
        sq_results: Results from status quo mechanism
        opt_results: Results from proposed optimal mechanism

    Returns:
        Dictionary with test results:
        {
            'mcnemar': {'chi2': float, 'p_value': float, 'significant': bool},
            'fisher_z': {'z': float, 'p_value': float, 'significant': bool},
            'permutation': {'observed_diff': float, 'p_value': float, 'significant': bool}
        }

    Example:
        >>> tests = run_statistical_tests(sq_results, opt_results)
        >>> print(f"McNemar p-value: {tests['mcnemar']['p_value']:.4f}")
    """
    from scipy import stats

    n = len(sq_results)
    alpha = 0.05

    # McNemar's test for paired nominal data
    # Count concordant/discordant pairs
    b = sum(1 for i in range(n) if sq_results[i].eliminations != opt_results[i].eliminations
            and opt_results[i].fairness_score > sq_results[i].fairness_score)
    c = sum(1 for i in range(n) if sq_results[i].eliminations != opt_results[i].eliminations
            and opt_results[i].fairness_score <= sq_results[i].fairness_score)

    if b + c > 0:
        chi2 = (abs(b - c) - 1)**2 / (b + c)
        p_mcnemar = 1 - stats.chi2.cdf(chi2, df=1)
    else:
        chi2, p_mcnemar = 0.0, 1.0

    # Fisher's z transformation for correlation comparison
    r_sq = np.mean([r.fairness_score for r in sq_results])
    r_opt = np.mean([r.fairness_score for r in opt_results])
    z_sq = np.arctanh(np.clip(r_sq, -0.999, 0.999))
    z_opt = np.arctanh(np.clip(r_opt, -0.999, 0.999))
    se = np.sqrt(2 / (n - 3))
    z_fisher = (z_opt - z_sq) / se
    p_fisher = 2 * (1 - stats.norm.cdf(abs(z_fisher)))

    # Permutation test for welfare difference
    observed_diff = np.mean([r.fairness_score for r in opt_results]) - \
                    np.mean([r.fairness_score for r in sq_results])

    combined = [r.fairness_score for r in sq_results] + [r.fairness_score for r in opt_results]
    n_perms = 10000
    perm_diffs = []
    for _ in range(n_perms):
        np.random.shuffle(combined)
        perm_diff = np.mean(combined[:n]) - np.mean(combined[n:])
        perm_diffs.append(perm_diff)

    p_perm = np.mean(np.abs(perm_diffs) >= abs(observed_diff))

    return {
        'mcnemar': {'chi2': chi2, 'p_value': p_mcnemar, 'significant': p_mcnemar < alpha},
        'fisher_z': {'z': z_fisher, 'p_value': p_fisher, 'significant': p_fisher < alpha},
        'permutation': {'observed_diff': observed_diff, 'p_value': p_perm, 'significant': p_perm < alpha}
    }
```

---

### 8. Counterfactual Table Generator

```python
def generate_counterfactual_table(sq_results: List[SeasonResult],
                                  opt_results: List[SeasonResult],
                                  season_ids: List[int]) -> pd.DataFrame:
    """
    Generate season-by-season comparison table.

    Parameters:
        sq_results: Status quo results per season
        opt_results: Optimal mechanism results per season
        season_ids: List of season identifiers

    Returns:
        DataFrame with columns: season, elimination_changes, delta_fairness,
                                delta_engagement, sq_eliminations, opt_eliminations

    Example:
        >>> cf_table = generate_counterfactual_table(sq_results, opt_results, list(range(1, 35)))
        >>> cf_table.to_csv('counterfactual_analysis_6_v2.csv', index=False)
    """
    rows = []
    for i, (sq, opt, sid) in enumerate(zip(sq_results, opt_results, season_ids)):
        # Count elimination differences
        changes = sum(1 for s, o in zip(sq.eliminations, opt.eliminations) if s != o)

        rows.append({
            'season': sid,
            'elimination_changes': changes,
            'delta_fairness': opt.fairness_score - sq.fairness_score,
            'delta_engagement': opt.engagement_score - sq.engagement_score,
            'sq_eliminations': ','.join(sq.eliminations[:3]),  # First 3
            'opt_eliminations': ','.join(opt.eliminations[:3])
        })

    return pd.DataFrame(rows)
```

---

## Output File Structure

```
output/implementation/
├── code/
│   ├── model_6_v2.py           # Main implementation with all functions above
│   └── test_model_6_v2.py      # Test suite
├── data/
│   └── features_6_v2.pkl       # Enhanced features for Model 6
└── results/
    ├── results_6_v2.csv                    # Optimization results
    ├── counterfactual_analysis_6_v2.csv    # Season-by-season comparison
    └── results_6_v2_recommendation.json    # Final recommendation
```

---

## JSON Output Schema

The `results_6_v2_recommendation.json` file MUST include:

```json
{
  "model_version": "6_v2",
  "mechanism_name": "Weighted Rank-Score Hybrid",
  "optimal_parameters": {
    "theta1_judge_weight": 0.35,
    "theta2_aggregation": 1,
    "theta3_discount": 0.85,
    "theta4_save_threshold": 0.08,
    "theta5_tiebreaker": 1
  },
  "performance": {
    "welfare_status_quo": 0.558,
    "welfare_proposed": 0.612,
    "welfare_improvement": 0.054,
    "fairness_delta": 0.057,
    "engagement_delta": 0.035
  },
  "statistical_tests": {
    "mcnemar": {"chi2": 12.45, "p_value": 0.0004, "significant": true},
    "fisher_z": {"z": 2.31, "p_value": 0.021, "significant": true},
    "permutation": {"observed_diff": 0.057, "p_value": 0.003, "significant": true}
  },
  "kkt_verification": {
    "stationarity": true,
    "gradient_norm": 0.0029,
    "primal_feasibility": true,
    "second_order": true,
    "hessian_eigenvalues": [-0.152, -0.083, -0.031, 0.0, 0.0],
    "kkt_satisfied": true
  },
  "counterfactual_summary": {
    "seasons_analyzed": 34,
    "total_elimination_changes": 162,
    "seasons_with_changes": 28,
    "average_changes_per_season": 4.8
  },
  "mechanism_description": "The Weighted Rank-Score Hybrid mechanism combines normalized judge scores (35% weight) with cumulative fan votes (65% weight), where historical votes decay at 15% per week. This balances expert judgment with audience engagement while preventing late-surge manipulation."
}
```

---

## Test Suite Requirements

The test file `test_model_6_v2.py` must include:

```python
import unittest
import numpy as np

class TestModel6(unittest.TestCase):

    def test_mechanism_params_creation(self):
        """Test MechanismParams instantiation."""
        params = MechanismParams(0.35, 1, 0.85, 0.08, 1)
        self.assertEqual(params.theta1, 0.35)

    def test_status_quo_vs_optimal(self):
        """Verify status quo and optimal differ."""
        sq = MechanismParams.status_quo()
        opt = MechanismParams.optimal()
        self.assertNotEqual(sq.theta1, opt.theta1)

    def test_welfare_computation(self):
        """Test welfare function returns valid value."""
        # Create mock results
        results = [SeasonResult(i, [], 0.5, 0.6, 0.7) for i in range(10)]
        welfare = compute_welfare(MechanismParams.optimal(), results)
        self.assertIsInstance(welfare, float)
        self.assertTrue(0 <= welfare <= 1)

    def test_kkt_verification(self):
        """Test KKT verification returns expected structure."""
        params = MechanismParams.optimal()
        gradient = np.zeros(5)  # At optimum
        hessian = -np.eye(5)    # Negative definite
        kkt = verify_kkt_conditions(params, gradient, hessian)
        self.assertTrue(kkt['kkt_satisfied'])

    def test_statistical_tests_structure(self):
        """Test statistical tests return expected keys."""
        sq_results = [SeasonResult(i, [], 0.4, 0.5, 0.6) for i in range(20)]
        opt_results = [SeasonResult(i, [], 0.5, 0.6, 0.7) for i in range(20)]
        tests = run_statistical_tests(sq_results, opt_results)
        self.assertIn('mcnemar', tests)
        self.assertIn('fisher_z', tests)
        self.assertIn('permutation', tests)

if __name__ == '__main__':
    unittest.main()
```
