---
common_pitfalls:
- Parameter Identifiability
- Scale Mismatch
- Local Optima
complexity: Medium
domain: optimization
last_updated: '2026-01-27'
method_name: Tabu Search (Tabu Search, TS)
narrative_reason: Standard method - consider enhancing with sensitivity analysis
narrative_value: Low
oprize_examples:
- 2020 Problem A
- 2022 Problem B
sub_domain: optimization
tags:
- optimization
- optimization
- medium
- optimization_methods_optimization_methods
- heuristic_algorithm_heuristic_algorithms
version: '2.0'
---

# Tabu Search (Tabu Search, TS)

> **Domain**: Optimization
> **Complexity**: Medium
> **Narrative Value**: Low

## Overview

<modeling_method>: Tabu Search (TS) is a global neighborhood search algorithm designed to avoid local optima by introducing a memory mechanism, thereby more effectively finding the global optimum. <core_idea>: The core idea of Tabu Search is to use a tabu list to record visited solutions or moves, preventing the search process from revisiting the same solutions or falling into cycles. By setting tabu criteria, it allows accepting worse solutions under certain conditions to escape local optima and explore a broader solution space. <application>: Tabu Search is widely used in the following types of mathematical modeling problems: Combinatorial optimization problems: such as the Traveling Salesman Problem (TSP), knapsack problem, and scheduling problems. Function optimization problems: In high-dimensional complex function optimization, Tabu Search can effectively avoid local optima. Engineering design problems: such as structural optimization and parameter tuning, where Tabu Search can be used to find optimal design solutions. Hyperparameter optimization in machine learning: In model training, Tabu Search can be used to optimize hyperparameter configurations.

HMML classes: Optimization Methods (Optimization Methods): / Heuristic Algorithm (Heuristic Algorithms):

## O-Prize Examples

- **2020 Problem A**: Used optimization methodology
- **2022 Problem B**: Used optimization methodology

## Common Pitfalls (Detailed)

### Pitfall 1: Parameter Identifiability

**Problem**: Correlated parameters may not converge or may compensate for each other

**Solution**: Use non-centered parameterization, strong priors, or reduce model complexity

### Pitfall 2: Scale Mismatch

**Problem**: Input features with different magnitudes may cause numerical issues

**Solution**: Normalize all features to [0, 1] or standardize to zero mean, unit variance

### Pitfall 3: Local Optima

**Problem**: Optimization may converge to suboptimal solutions

**Solution**: Use multiple random restarts, global optimization, or simulated annealing

## Narrative Strategy

**Value**: Low - Standard method - consider enhancing with sensitivity analysis

### Suggested Framing

> "We employ Tabu Search (Tabu Search, TS) to capture [specific mechanism], 
> which enables us to [key insight] while accounting for [complexity/uncertainty]."
