---
common_pitfalls:
- Local Optima
complexity: Medium
domain: network_science
last_updated: '2026-01-27'
method_name: Local Search
narrative_reason: Standard method - consider enhancing with sensitivity analysis
narrative_value: Low
oprize_examples:
- 2019 Problem D
- 2022 Problem E
sub_domain: pathfinding
tags:
- network_science
- pathfinding
- medium
- optimization_methods_optimization_methods
- deterministic_algorithms_deterministic_algorithms
version: '2.0'
---

# Local Search

> **Domain**: Network Science
> **Complexity**: Medium
> **Narrative Value**: Low

## Overview

<modeling_method>: Local Search is a heuristic algorithm widely used for solving optimization problems. It starts from an initial solution and iteratively searches its neighborhood until a better solution is found or a stopping condition is met. <core_idea>: The core idea of Local Search is to start from a candidate solution and continuously search its neighborhood until no better solution is found. <application>: Local Search is widely used in the following types of mathematical modeling problems: Minimum Vertex Cover Problem: Finding the smallest set of vertices that cover all edges in a graph. Traveling Salesman Problem: Finding the shortest possible route that visits each vertex exactly once and returns to the starting point. Boolean Satisfiability Problem: Finding a variable assignment that satisfies a set of clauses.

HMML classes: Optimization Methods (Optimization Methods): / Deterministic Algorithms (Deterministic Algorithms):

## O-Prize Examples

- **2019 Problem D**: Used network methodology
- **2022 Problem E**: Used network methodology

## Common Pitfalls (Detailed)

### Pitfall 1: Local Optima

**Problem**: Optimization may converge to suboptimal solutions

**Solution**: Use multiple random restarts, global optimization, or simulated annealing

## Narrative Strategy

**Value**: Low - Standard method - consider enhancing with sensitivity analysis

### Suggested Framing

> "We employ Local Search to capture [specific mechanism], 
> which enables us to [key insight] while accounting for [complexity/uncertainty]."
