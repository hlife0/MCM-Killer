---
common_pitfalls:
- Scale Mismatch
complexity: Medium
domain: optimization
last_updated: '2026-01-27'
method_name: Data Envelopment Analysis (DEA)
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
- evaluation_methods_evaluation_methods
- scoring_evaluation_scoring_evaluation
version: '2.0'
---

# Data Envelopment Analysis (DEA)

> **Domain**: Optimization
> **Complexity**: Medium
> **Narrative Value**: Low

## Overview

<modeling_method>: Data Envelopment Analysis (DEA) is a non-parametric method used to evaluate the relative efficiency of decision-making units (DMUs) with multiple inputs and outputs. It constructs an envelope surface (or efficiency frontier) to compare the relative efficiency of each DMU, determining which DMUs are efficient given the resources used and which are not. <core_idea>: The core idea of DEA is to construct an envelope surface using linear programming methods, surrounding the most efficient DMUs to form the efficiency frontier. The distance of other DMUs from the efficiency frontier reflects their relative efficiency. Specifically, DEA weights the inputs and outputs of each DMU to find an optimal combination of weights that maximizes the efficiency of each DMU. <application>: DEA is widely used in the following fields: Education: Evaluating the teaching efficiency of different schools, such as the relationship between student performance and teaching resources. Healthcare: Measuring the service efficiency of hospitals or clinics, such as the relationship between medical resources and patient satisfaction. Banking: Evaluating the operational efficiency of branches, such as the relationship between fund usage and profits. Manufacturing: Measuring the production efficiency of different production lines or factories, such as the relationship between output and resource consumption. Public services: Evaluating the service efficiency of government departments or public institutions, such as the relationship between administrative costs and service quality.

HMML classes: Evaluation Methods (Evaluation Methods): / Scoring Evaluation (Scoring Evaluation):

## O-Prize Examples

- **2020 Problem A**: Used optimization methodology
- **2022 Problem B**: Used optimization methodology

## Common Pitfalls (Detailed)

### Pitfall 1: Scale Mismatch

**Problem**: Input features with different magnitudes may cause numerical issues

**Solution**: Normalize all features to [0, 1] or standardize to zero mean, unit variance

## Narrative Strategy

**Value**: Low - Standard method - consider enhancing with sensitivity analysis

### Suggested Framing

> "We employ Data Envelopment Analysis (DEA) to capture [specific mechanism], 
> which enables us to [key insight] while accounting for [complexity/uncertainty]."
