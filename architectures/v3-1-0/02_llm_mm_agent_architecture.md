# LLM-MM-Agent Architecture

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete architecture for LLM-MM-Agent (Reference/Stable System)

---

## System Overview

**LLM-MM-Agent** is a research prototype published at top ML conferences (NeurIPS 2025, ICML 2025) that demonstrates LLMs as autonomous agents for solving MCM/ICM problems.

**Location**: `clean version/LLM-MM-Agent/`

**Key Characteristics**:
- **Single-Agent Architecture**: One LLM agent with actor-critic refinement
- **4-Stage Pipeline**: Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting
- **HMML Knowledge Base**: 98+ modeling schemas organized hierarchically
- **DAG-Based Scheduling**: Dependency-aware task execution
- **Academic Baseline**: Reference implementation for research

**Paper**: "MM-Agent: LLMs as Agents for Real-world Mathematical Modeling Problems"
**arXiv**: https://arxiv.org/abs/2505.14148

---

## 4-Stage Pipeline

### Stage 1: Problem Analysis

**Purpose**: Decompose the problem into manageable subtasks

**Process**:
1. Read problem PDF
2. Extract requirements
3. Identify key components
4. Decompose into subtasks (max: 5 by default)
5. Actor-critic refinement (3 rounds by default)

**Output**: `Memory/subtasks.json`

**Configuration**: `problem_analysis_round: 3` (in config.yaml)

**Example**:
```json
{
  "subtask_1": "Build a predictive model for gold price forecasting",
  "subtask_2": "Analyze feature importance and economic indicators",
  "subtask_3": "Evaluate model performance and uncertainty quantification"
}
```

---

### Stage 2: Mathematical Modeling

**Purpose**: Retrieve appropriate mathematical methods and formulate models

**Process**:
1. Retrieve methods from HMML (top 6 by default)
2. Select methods for each subtask
3. Formulate mathematical models
4. Actor-critic refinement (3 rounds by default)

**Output**: `Memory/methods.json`

**Configuration**:
- `top_method_num: 6` (number of methods to retrieve)
- `problem_modeling_round: 3` (actor-critic rounds)

**HMML Retrieval**:
```
Query: "time series forecasting"
↓
Embedding-based similarity search
↓
Top 6 methods:
1. ARIMA (Auto-Regressive Integrated Moving Average)
2. LSTM (Long Short-Term Memory)
3. Prophet (Facebook's forecasting tool)
4. Bayesian Structural Time Series
5. Transformer-based models
6. Gaussian Process Regression
```

---

### Stage 3: Computational Solving

**Purpose**: Generate and execute Python code to solve the problem

**Process**:
1. Generate Python code for each subtask
2. Execute code with timeout (300 seconds default)
3. Debug and retry on failure
4. Save results (CSV, charts)

**Output**:
- `Workspace/code/main*.py`
- `Workspace/json/results*.json`
- `Workspace/charts/*.png`

**Configuration**:
- `code_execution_timeout: 300` (seconds)
- `task_formulas_round: 5` (formula derivation iterations)

**SafePlaceholder Pattern**:
```python
class SafePlaceholder:
    """Prevents template formatting crashes when variables missing"""
    def __getattr__(self, name):
        return self
    def __format__(self, format_spec):
        return str(self)
```

---

### Stage 4: Solution Reporting

**Purpose**: Generate comprehensive reports in multiple formats

**Process**:
1. Generate JSON report
2. Generate Markdown report
3. Generate LaTeX report
4. Compile LaTeX to PDF

**Output**:
- `Workspace/json/report.json`
- `Workspace/markdown/report.md`
- `Workspace/latex/report.tex`
- `Report/paper.pdf` (final PDF)

**Omni-Survival Kit** (Dead Man's Switch):
- Guarantees PDF generation even if some stages fail
- Fallback mechanisms for missing data
- Template-based report generation

**Latent Reporter** (Post-Processing):
- Research journal generation
- Forensic analysis of execution
- "Truth Mode" logging for debugging

---

## HMML (Hierarchical Mathematical Modeling Library)

### Structure

```
HMML/
├── Domains (Level 1)
│   ├── Optimization
│   ├── Differential Equations
│   ├── Statistics
│   ├── Machine Learning
│   └── Graph Theory
│
├── Subdomains (Level 2)
│   ├── Optimization → Linear Programming
│   ├── Optimization → Integer Programming
│   ├── Differential Equations → ODEs
│   ├── Differential Equations → PDEs
│   └── Statistics → Bayesian Inference
│
└── Method Nodes (Level 3)
    ├── Linear Programming → Simplex Method
    ├── Linear Programming → Interior Point Methods
    ├── ODEs → Runge-Kutta Methods
    ├── ODEs → Euler's Method
    └── Bayesian Inference → MCMC Sampling
```

### Example HMML Entry

```markdown
## Method: Bayesian Hierarchical Model

**Domain**: Statistics
**Subdomain**: Bayesian Inference
**Method Node**: Hierarchical Models

**Description**:
A Bayesian hierarchical model specifies a joint probability distribution over parameters and data, allowing partial pooling of information across groups.

**Key Components**:
- Prior distribution
- Likelihood function
- Hyperpriors
- Posterior inference

**Common Algorithms**:
- MCMC Sampling (NUTS, HMC)
- Variational Inference
- Laplace Approximation

**Use Cases**:
- Multi-level data (students within schools)
- Small sample sizes per group
- Partial pooling (between complete pooling and no pooling)

**Computational Complexity**:
- NUTS: O(n × d × iter) where n=samples, d=dimensions, iter=iterations
- Typical runtime: 10-20 hours for 5000 samples, 20 dimensions, 10000 iterations

**Python Libraries**:
- PyMC3 / PyMC4
- Stan (pystan)
- TensorFlow Probability
```

### Retrieval Mechanism

1. **Embedding-Based**: Query and method nodes embedded in vector space
2. **Similarity Search**: Cosine similarity to find top-K matches
3. **Contextual**: Problem description matched to method descriptions

**Configuration**: `top_method_num: 6` (retrieve top 6 methods)

---

## DAG-Based Task Scheduling

### Coordinator Pattern

The `coordinator.py` builds a dependency graph:

```python
# Example DAG for 3 subtasks
subtask_1 → subtask_2 → subtask_3
     ↓           ↓           ↓
  code_1      code_2      code_3
     ↓           ↓           ↓
  result_1 → result_2 → result_3
```

### Key Features

1. **Dependency Resolution**: Automatically resolves task dependencies
2. **Cycle Detection**: Prevents circular dependencies with retry attempts
3. **Type Normalization**: String type enforcement prevents KeyError
4. **Checkpointing**: Resume from failures without restarting

### Memory Management

```
memory: {
  "subtask_1": {...},
  "subtask_2": {...},
  "subtask_3": {...}
}

code_memory: {
  "subtask_1": "main1.py",
  "subtask_2": "main2.py",
  "subtask_3": "main3.py"
}
```

---

## Context Pruning Strategy ("远近亲疏")

### Problem

As subtasks grow, context from all dependencies becomes too large.

### Solution: Intelligent Pruning

**Immediate Predecessor (task_id - 1)**:
- Full context with character limits
- Most recent and relevant

**Earlier Dependencies**:
- Minimal context (results only)
- File outputs preserved

**Example**:
```
Task 3 executing:
- Task 2 (immediate predecessor): Full context (10K chars max)
- Task 1 (earlier dependency): Results only + file paths
```

**Benefits**:
- Reduces token usage
- Focuses on most relevant context
- Maintains reproducibility (files preserved)

---

## Actor-Critic Pattern

### Throughout Pipeline

**Actor**: Generates initial output
**Critic**: Reviews and provides critique
**Actor**: Improves based on critique

**Repeat** N times (default: 3)

### Application Points

1. **Problem Analysis** (`problem_analysis_round: 3`)
   - Actor: Decompose problem
   - Critic: Review decomposition quality
   - Actor: Refine subtasks

2. **Mathematical Modeling** (`problem_modeling_round: 3`)
   - Actor: Select methods, formulate models
   - Critic: Review mathematical soundness
   - Actor: Refine formulations

3. **Formula Derivation** (`task_formulas_round: 5`)
   - Actor: Derive equations
   - Critic: Check mathematical correctness
   - Actor: Correct and refine

---

## Output Structure

### Three-Tier Structure

```
output/MM-Agent/{task}_{timestamp}/
│
├── Report/                    # Final outputs
│   ├── paper.pdf             # Compiled LaTeX PDF
│   └── figures/              # Figures for paper
│
├── Workspace/                # Working files
│   ├── json/                 # Results (JSON)
│   │   ├── results_1.json
│   │   └── ...
│   ├── markdown/             # Reports (Markdown)
│   │   └── report.md
│   ├── latex/                # LaTeX source
│   │   ├── report.tex
│   │   └── figures/
│   ├── code/                 # Generated Python code
│   │   ├── main1.py
│   │   └── ...
│   └── charts/               # Generated figures
│       ├── figure_1.png
│       └── ...
│
└── Memory/                   # Execution data
    ├── logs/                 # Execution logs
    │   ├── execution_tracker_readable.txt
    │   └── execution_tracker.json
    ├── checkpoints/          # Resume capability
    │   └── checkpoint.json
    ├── usage/                # Token usage
    │   └── usage.json
    └── evaluation/           # Self-evaluation
        └── evaluation.json
```

### Quick Check

**After each run**, check: `Memory/logs/brief_summary.txt`

Contains:
- Subtasks completed
- Methods used
- Code execution status
- Final outputs
- Any errors or warnings

---

## Unique Innovations

### 1. HMML (Hierarchical Mathematical Modeling Library)

**First** 3-level knowledge base for mathematical modeling with 98+ schemas.

**Impact**:
- Systematic method retrieval
- Embedding-based matching
- Covers optimization, differential equations, statistics, ML, graph theory

### 2. Context Pruning Strategy

**Intelligent** dependency context management ("远近亲疏" - near and far, close and distant).

**Impact**:
- Reduces token usage by 60-80%
- Maintains focus on relevant context
- Preserves reproducibility

### 3. Omni-Survival Kit

**Dead Man's Switch** system guaranteeing PDF generation.

**Impact**:
- Never produces incomplete output
- Fallback mechanisms
- Template-based generation

### 4. Auto-Resume Checkpointing

**Transparent** pipeline state persistence.

**Impact**:
- Resume from failures
- No wasted computation
- Fault tolerance

### 5. Type-Normalized DAG

**Robust** task scheduling with string type enforcement.

**Impact**:
- Prevents KeyError from type mismatches
- Cycle detection with retry
- Dependency resolution

### 6. Truth Mode Logging

**Complete** event tracebacks for forensic analysis.

**Impact**:
- Debug failed runs
- Understand LLM decisions
- Reproduce results

### 7. Latent Reporter

**Post-processing** research journal generation.

**Impact**:
- Documents the problem-solving process
- Useful for analysis and publication

### 8. SafePlaceholder Pattern

**Prevents** template formatting crashes when variables missing.

**Impact**:
- No crashes from missing data
- Graceful degradation
- Robust string formatting

---

## Configuration (config.yaml)

### Key Parameters

```yaml
# HMML Settings
top_method_num: 6              # Number of methods to retrieve

# Actor-Critic Rounds
problem_analysis_round: 3      # Problem analysis refinement
problem_modeling_round: 3      # Mathematical modeling refinement
task_formulas_round: 5         # Formula derivation refinement

# Task Limits
num_tasks: 5                   # Maximum subtasks to process
num_charts: 5                  # Charts per task

# Execution Settings
code_execution_timeout: 300    # Code execution timeout (seconds)

# Paths
paths:
  root_data: "MMBench"         # Data directory
  output_root: "MMAgent/output" # Output directory
```

---

## Usage

### Basic Usage

```bash
cd "clean version/LLM-MM-Agent"
python MMAgent/main.py \
    --key "your_api_key" \
    --task "2024_C" \
    --model_name "gpt-4o"
```

### Supported Models

- `gpt-4o` (OpenAI)
- `deepseek-chat` (DeepSeek)
- `glm-4-flash` (Zhipu AI - faster)
- `glm-4-plus` (Zhipu AI - more capable)
- `qwen2.5-72b-instruct` (Alibaba)

### Environment Setup

```bash
# Create conda environment
conda create --name math_modeling python=3.10
conda activate math_modeling

# Install dependencies
pip install -r requirements.txt
```

---

## Comparison with MCM-Killer

| Aspect | LLM-MM-Agent | MCM-Killer |
|--------|--------------|------------|
| **Agents** | Single (actor-critic) | 14 specialized |
| **Stages** | 4 stages | 10 phases |
| **Validation** | Actor-critic iterations | 7 validation gates |
| **Knowledge Base** | HMML (98+ schemas) | Agent expertise |
| **Workflow** | Sequential | Parallel (Phase 5) |
| **Protocols** | Basic | 12 critical protocols |
| **Use Case** | Research, reference | Competition |

---

## When to Use LLM-MM-Agent

Use LLM-MM-Agent when you want to:
- Study the reference implementation from NeurIPS/ICML papers
- Understand the 4-stage pipeline architecture
- Retrieve modeling methods via HMML
- Run autonomous problem solving with minimal configuration
- Test different LLM models (gpt-4o, deepseek, glm-4, qwen)
- Use command-line interface (not interactive)
- Leverage checkpointing and auto-resume
- Generate baseline results for comparison
- Research and experimentation in academic setting

---

## References

**Paper**: "MM-Agent: LLMs as Agents for Real-world Mathematical Modeling Problems"
**Authors**: NeurIPS 2025 / ICML 2025
**arXiv**: https://arxiv.org/abs/2505.14148
**Demo**: https://huggingface.co/spaces/MathematicalModelingAgent/MathematicalModelingAgent

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `03_mcm_killer_architecture.md` for MCM-Killer architecture
