---
common_pitfalls:
- Parameter Identifiability
complexity: Medium
domain: optimization
last_updated: '2026-01-27'
method_name: Restriction
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
- solving_techniques
version: '2.0'
---

# Restriction

> **Domain**: Optimization
> **Complexity**: Medium
> **Narrative Value**: Low

## Overview

<modeling_method>: In mathematical modeling, restriction refers to the conditions or constraints imposed on decision variables or model parameters to ensure that the solution of the model meets the requirements of the actual problem. <core_idea>: The core idea of restriction is to ensure the feasibility and validity of the solution in practical applications by imposing specific conditions on the model. <application>: Restrictions are widely used in the following types of mathematical modeling problems: Resource allocation problems: such as production planning, transportation scheduling, etc., restrictions are used to ensure the rational allocation of resources. Optimization problems: such as linear programming, integer programming, etc., restrictions are used to define the feasible solution space. Engineering design problems: such as structural optimization, parameter tuning, etc., restrictions are used to meet design specifications and safety standards.

HMML classes: Optimization Methods (Optimization Methods): / Solving Techniques:

## O-Prize Examples

- **2020 Problem A**: Used optimization methodology
- **2022 Problem B**: Used optimization methodology

## Common Pitfalls (Detailed)

### Pitfall 1: Parameter Identifiability

**Problem**: Correlated parameters may not converge or may compensate for each other

**Solution**: Use non-centered parameterization, strong priors, or reduce model complexity

## Narrative Strategy

**Value**: Low - Standard method - consider enhancing with sensitivity analysis

### Suggested Framing

> "We employ Restriction to capture [specific mechanism], 
> which enables us to [key insight] while accounting for [complexity/uncertainty]."
