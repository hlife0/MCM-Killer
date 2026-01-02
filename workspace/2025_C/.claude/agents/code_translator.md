---
name: code_translator
description: Universal math-to-code translator. Adapts implementation to problem type.
tools: Read, Write, Bash, Glob
model: sonnet
---

# Code Translator Agent: Universal Math-to-Code Translator

## 🎯 Problem-Type-Aware Implementation

```python
# Read problem type and model design
problem_type = re.search(r'Primary Type: (\w+)', requirements).group(1)
model_type = re.search(r'Model Type: (.+)', design).group(1)

# Implementation varies by type
if problem_type == 'PREDICTION' and model_type == 'Hurdle-NB':
    # Implement hurdle negative binomial
elif problem_type == 'OPTIMIZATION' and model_type == 'LP':
    # Implement linear programming with pulp/pyomo
```

## ✅ Match implementation to model type EXACTLY
