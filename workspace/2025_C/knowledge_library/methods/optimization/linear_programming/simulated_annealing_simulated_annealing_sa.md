---
common_pitfalls:
- Parameter Identifiability
- Scale Mismatch
- Local Optima
complexity: Medium
domain: optimization
last_updated: '2026-01-27'
method_name: Simulated Annealing (Simulated Annealing, SA)
narrative_reason: Standard method - consider enhancing with sensitivity analysis
narrative_value: Low
oprize_examples:
- 2020 Problem A
- 2022 Problem B
sub_domain: linear_programming
tags:
- optimization
- linear_programming
- medium
- optimization_methods_optimization_methods
- heuristic_algorithm_heuristic_algorithms
version: '2.0'
---

# Simulated Annealing (Simulated Annealing, SA)

> **Domain**: Optimization
> **Complexity**: Medium
> **Narrative Value**: Low

## Overview

<modeling_method>: Simulated Annealing (SA) is a probabilistic global optimization algorithm derived from the annealing process in physics. The basic idea is to start from a high-temperature state and gradually lower the temperature, simulating the process of particles transitioning from disorder to order to find the global optimum. <core_idea>: Simulated Annealing algorithm simulates the process of particles moving randomly at high temperatures and gradually stabilizing as the temperature decreases. During this process, the algorithm allows accepting worse solutions with a certain probability to escape local optima and eventually converge to the global optimum. <application>: Simulated Annealing algorithm is widely used in the following types of mathematical modeling problems: Combinatorial optimization problems: such as the Traveling Salesman Problem (TSP), knapsack problem, etc. Function optimization problems: In high-dimensional complex function optimization, Simulated Annealing can effectively avoid local optima. Hyperparameter optimization in machine learning: In model training, Simulated Annealing can be used to optimize hyperparameter configurations. Engineering design problems: such as structural optimization and parameter tuning, where Simulated Annealing can be used to find optimal design solutions.

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

> "We employ Simulated Annealing (Simulated Annealing, SA) to capture [specific mechanism], 
> which enables us to [key insight] while accounting for [complexity/uncertainty]."
