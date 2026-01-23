# orientation2 Implementation Checklist

> **Version**: 3.0-Final
> **Date**: 2026-01-23
> **Estimated Time**: 10 minutes setup + 30 minutes knowledge preparation

---

## Phase 1: Directory Setup (2 minutes)

### Step 1.1: Create Base Directory Structure

```bash
# Navigate to workspace
cd "D:/migration/MCM-Killer/workspace/2025_C"

# Create required directories
mkdir -p docs
mkdir -p global_memory
mkdir -p artifacts/{code,figures,models,data,results,validation,paper}
mkdir -p reference/best_paper_example/{figures,code,style_extraction}
```

**Verification**:
```bash
ls -la docs/ global_memory/ artifacts/ reference/
```

**Expected Output**: All directories exist

---

## Phase 2: Knowledge Base Preparation (20 minutes)

### Step 2.1: Create `docs/math_models_cheatsheet.md`

**Source**: Extract from HMML (located at `D:/migration/clean version/LLM-MM-Agent/MMAgent/HMML/HMML.md` or orientation2/reference/HMML.md)

**Task**: Create a condensed cheatsheet with:
- Top 20 most useful methods for MCM problems
- For each method: brief description, when to use, key formulas
- Format: Markdown table for easy reference

**Template**:
```markdown
# Mathematical Methods Cheatsheet

## Optimization
| Method | When to Use | Key Formulas | Notes |
|--------|-------------|--------------|-------|
| Linear Programming | Resource allocation problems | Maximize cᵀx subject to Ax ≤ b | Use pulp or scipy.optimize |

## Machine Learning
| Method | When to Use | Key Parameters | Notes |
|--------|-------------|----------------|-------|
| Random Forest | Prediction with tabular data | n_estimators, max_depth | sklearn.ensemble |
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/docs/math_models_cheatsheet.md" && echo "EXISTS" || echo "MISSING"
```

### Step 2.2: Create `docs/anti_patterns.md`

**Source**: Based on common mistakes (document in 00_MAIN.md section "坚决舍弃的模块")

**Template**:
```markdown
# Anti-Patterns: What NOT to Do

## Code Anti-Patterns
- ❌ Don't write file managers - trust Claude Code
- ❌ Don't implement retry loops - let LLM handle errors naturally
- ❌ Don't create JSON validation schemas - use natural language
- ❌ Don't build DAG schedulers - use prompt dependencies

## Data Anti-Patterns
- ❌ Don't hardcode relative paths - use absolute paths
- ❌ Don't overwrite files - use timestamps: `artifact_YYYYMMDD_HHMMSS.py`
- ❌ Don't mix code and data - keep in separate artifacts/ subdirs

## Process Anti-Patterns
- ❌ Don't skip validation gates - each phase must pass before next
- ❌ Don't ignore paper requirements - all bullets are mandatory
- ❌ Don't optimize prematurely - simplest working solution first
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/docs/anti_patterns.md" && echo "EXISTS" || echo "MISSING"
```

### Step 2.3: Create `docs/mcm_o_prize_style_guide.md`

**Source**: Extract from selected best paper (Phase 3)

**Template**:
```markdown
# MCM O-Prize Style Guide

## Paper Structure
1. Summary (1 page)
2. Problem Restatement (1 page)
3. Assumptions and Justifications
4. Variable Definitions
5. Model Development
   - Model 1: [Name]
   - Model 2: [Name]
6. Model Testing and Analysis
7. Results and Discussion
8. Strengths and Weaknesses
9. Memo to Team Leader

## Writing Guidelines
- Active voice: "We developed" not "It was developed"
- Present tense for model description: "The model uses..."
- Past tense for experiments: "We tested..."
- Specific numbers: "R² = 0.94" not "high R²"

## Visual Guidelines
- Color scheme: [extract from best paper]
- Figure fonts: [specify]
- Table style: [specify]
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/docs/mcm_o_prize_style_guide.md" && echo "EXISTS" || echo "MISSING"
```

### Step 2.4: Create `docs/optimization_strategies.md`

**Source**: Based on HMML optimization domain

**Template**:
```markdown
# Optimization Strategies

## Problem → Optimization Method Mapping

| Problem Type | Recommended Method | Python Package |
|--------------|-------------------|----------------|
| Linear objective + linear constraints | Linear Programming | scipy.optimize.linprog |
| Integer variables | Integer Programming | pulp |
| Non-linear objective | Non-linear Programming | scipy.optimize.minimize |
| Multi-objective | Pareto Optimization | pymoo |
| Combinatorial | Genetic Algorithms | deap |

## Common MCM Optimization Patterns

1. **Resource Allocation**: Linear Programming
2. **Routing/Scheduling**: Integer Programming or TSP variants
3. **Forecasting**: Time Series (ARIMA/SARIMA)
4. **Classification**: Machine Learning (Random Forest, XGBoost)
5. **Clustering**: K-means, DBSCAN
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/docs/optimization_strategies.md" && echo "EXISTS" || echo "MISSING"
```

### Step 2.5: Create `docs/coding_best_practices.md`

**Source**: Based on LLM-MM-Agent code patterns and MCM-Killer standards

**Template**:
```markdown
# Coding Best Practices for MCM

## File Organization

### Generated Code Structure
```
artifacts/code/model_name_YYYYMMDD_HHMMSS.py
├── Imports (standard library first, then third-party)
├── Configuration (constants at top)
├── Data Loading (use absolute paths)
├── Data Preprocessing
├── Model Definition/Training
├── Evaluation
└── Output Saving (CSV, PKL, figures)
```

## Absolute Path Pattern

```python
import os

# ALWAYS use absolute paths for data
DATA_DIR = r"D:/migration/MCM-Killer/workspace/2025_C/2025_Problem_C_Data"
output_file = os.path.join(DATA_DIR, "filename.csv")

# NEVER use relative paths for data
# WRONG: pd.read_csv("data.csv")
```

## Output Format

```python
# Save results
results_df.to_csv(
    "artifacts/results/model1_results_20260123_143000.csv",
    index=False
)

# Save model
import pickle
with open("artifacts/models/model1_20260123_143000.pkl", "wb") as f:
    pickle.dump(model, f)

# Save figure
plt.savefig("artifacts/figures/plot1_20260123_143000.png", dpi=300)
```

## Error Handling

```python
try:
    result = risky_operation()
except Exception as e:
    print(f"Error: {e}")
    # Fallback or alternative approach
    result = fallback_method()
```

## Timeout Protection

```python
import signal
from contextlib import contextmanager

@contextmanager
def timeout(seconds):
    """Timeout context manager"""
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Operation timed out after {seconds} seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

# Usage
with timeout(300):  # 5 minutes
    long_running_operation()
```
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/docs/coding_best_practices.md" && echo "EXISTS" || echo "MISSING"
```

---

## Phase 3: One-Shot Learning Setup (5 minutes)

### Step 3.1: Select Best Paper

**Action**: Choose ONE complete O-Prize paper from `reference_papers/`

**How to Identify**:
1. Look for papers with high control numbers (likely recent)
2. Check if LaTeX source is available
3. Prefer papers with:
   - Clear structure (IMRaD)
   - Excellent visualizations
   - Complete code availability

**Example Command**:
```bash
# List papers with sizes
ls -lh "D:/migration/MCM-Killer/workspace/2025_C/reference_papers/" | sort -k5 -hr
```

### Step 3.2: Create Best Paper Directory

```bash
# Assuming 2318982.pdf is selected (example - replace with actual choice)
PAPER_ID="2318982"

mkdir -p "D:/migration/MCM-Killer/workspace/2025_C/reference/best_paper_example/figures"
mkdir -p "D:/migration/MCM-Killer/workspace/2025_C/reference/best_paper_example/code"
mkdir -p "D:/migration/MCM-Killer/workspace/2025_C/reference/best_paper_example/style_extraction"

# Copy paper
cp "D:/migration/MCM-Killer/workspace/2025_C/reference_papers/${PAPER_ID}.pdf" \
   "D:/migration/MCM-Killer/workspace/2025_C/reference/best_paper_example/"
```

### Step 3.3: Extract Style Elements

**Create `reference/best_paper_example/style_extraction/structure.md`**:
```markdown
# Paper Structure Analysis

## Sections (with page counts)
- Summary: 1 page
- Problem Restatement: 1 page
- ...

## Key Patterns
- How equations are formatted
- How figures are referenced
- How tables are structured
```

**Create `reference/best_paper_example/style_extraction/visuals.md`**:
```markdown
# Visual Style Guide

## Color Scheme
- Primary color: #XXXXXX
- Secondary color: #XXXXXX
- Accent color: #XXXXXX

## Figure Style
- Font: Times New Roman, 12pt
- Grid: Yes/No
- Legends: Position and format

## Table Style
- Borders: Which lines
- Header format
- Data alignment
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/reference/best_paper_example/style_extraction/structure.md" && echo "EXISTS" || echo "MISSING"
```

---

## Phase 4: Global Memory Initialization (3 minutes)

### Step 4.1: Create `global_memory/lessons_learned.md`

```bash
cat > "D:/migration/MCM-Killer/workspace/2025_C/global_memory/lessons_learned.md" << 'EOF'
# Lessons Learned - MCM Competition

## [Date] - [Session/Task Name]

### Error
[Describe what went wrong]

### Root Cause
[Analyze why it happened]

### Solution
[Code-level fix]

### Prevention
**Claude Code，今后...** [Specific instruction for future]
EOF
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/global_memory/lessons_learned.md" && echo "EXISTS" || echo "MISSING"
```

### Step 4.2: Create Bootstrap Instructions

```bash
cat > "D:/migration/MCM-Killer/workspace/2025_C/global_memory/BOOTSTRAP.md" << 'EOF'
# Session Bootstrap Instructions

## When Starting Claude Code Session

Execute this first:

```
Claude Code，请按以下顺序启动：

1. 阅读 docs/ 目录下的所有知识库文件（5个MD）
2. 阅读 reference/best_paper_example/ 中的最佳论文示例
3. 阅读 global_memory/lessons_learned.md（如果有）
4. 确认理解当前任务：[2025_MCM_Problem_C.pdf]
5. 准备进入 4 元认知模式循环
```

## Session Start Checklist

- [ ] Read all 5 knowledge base files in docs/
- [ ] Read best paper example
- [ ] Review lessons learned
- [ ] Read current problem statement
- [ ] Confirm ready to begin

## Mode Switching Commands

### Switch to Scientist Mode
```
Claude Code，切换到科学家模式，分析问题并提出假设。
```

### Switch to Engineer Mode
```
Claude Code，切换到工程师模式，实现代码。
```

### Switch to Critic Mode
```
Claude Code，切换到批评家模式，审查质量。
```

### Switch to Writer Mode
```
Claude Code，切换到作家模式，撰写论文。
```

## Session End Debrief

When session ends:

1. **Review Execution**: What went well? What failed?
2. **Extract Lessons**: Add 3-5 entries to lessons_learned.md
3. **Code-Level Fixes**: Be specific with "Claude Code，今后..."
4. **Next Session Prep**: What should be done differently next time?
EOF
```

**Verification**:
```bash
test -f "D:/migration/MCM-Killer/workspace/2025_C/global_memory/BOOTSTRAP.md" && echo "EXISTS" || echo "MISSING"
```

---

## Phase 5: Final Verification (2 minutes)

### Step 5.1: Run Complete Check

```bash
# Navigate to workspace
cd "D:/migration/MCM-Killer/workspace/2025_C"

# Check all required files and directories
echo "=== Directory Structure Check ==="
for dir in docs global_memory artifacts reference; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/"
    else
        echo "❌ $dir/ MISSING"
    fi
done

echo ""
echo "=== Knowledge Base Files Check ==="
for file in docs/math_models_cheatsheet.md \
            docs/anti_patterns.md \
            docs/mcm_o_prize_style_guide.md \
            docs/optimization_strategies.md \
            docs/coding_best_practices.md; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file MISSING"
    fi
done

echo ""
echo "=== Global Memory Files Check ==="
for file in global_memory/lessons_learned.md \
            global_memory/BOOTSTRAP.md; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file MISSING"
    fi
done

echo ""
echo "=== Artifacts Subdirectories Check ==="
for subdir in code figures models data results validation paper; do
    if [ -d "artifacts/$subdir" ]; then
        echo "✅ artifacts/$subdir/"
    else
        echo "❌ artifacts/$subdir/ MISSING"
    fi
done

echo ""
echo "=== Reference Structure Check ==="
if [ -d "reference/best_paper_example" ]; then
    echo "✅ reference/best_paper_example/"
    # Check for style extraction files
    if [ -f "reference/best_paper_example/style_extraction/structure.md" ]; then
        echo "  ✅ style_extraction/structure.md"
    else
        echo "  ⚠️  style_extraction/structure.md not created yet"
    fi
else
    echo "❌ reference/best_paper_example/ MISSING"
fi
```

### Step 5.2: Test Bootstrap Instructions

**Start a new Claude Code session** and run:

```
Claude Code，请阅读 global_memory/BOOTSTRAP.md 并执行启动流程。
```

**Expected Behavior**:
1. Claude reads all 5 knowledge base files
2. Claude reads best paper example
3. Claude reviews lessons_learned.md
4. Claude confirms understanding of current problem
5. Claude confirms ready for 4-mode cycle

---

## Complete Checklist Summary

### Phase 1: Directory Setup (2 min)
- [ ] Create base directories (docs, global_memory, artifacts, reference)

### Phase 2: Knowledge Base (20 min)
- [ ] Create docs/math_models_cheatsheet.md
- [ ] Create docs/anti_patterns.md
- [ ] Create docs/mcm_o_prize_style_guide.md
- [ ] Create docs/optimization_strategies.md
- [ ] Create docs/coding_best_practices.md

### Phase 3: One-Shot Learning (5 min)
- [ ] Select ONE best paper from reference_papers/
- [ ] Create best_paper_example/ directory
- [ ] Extract style elements (structure.md, visuals.md)

### Phase 4: Global Memory (3 min)
- [ ] Create global_memory/lessons_learned.md
- [ ] Create global_memory/BOOTSTRAP.md

### Phase 5: Verification (2 min)
- [ ] Run complete check script
- [ ] Test bootstrap instructions with Claude Code

---

## Post-Setup: First Session Execution

### Session Workflow

1. **Start Claude Code** in `D:/migration/MCM-Killer/workspace/2025_C/`
2. **Run Bootstrap**: "Claude Code，请阅读 global_memory/BOOTSTRAP.md 并执行启动流程。"
3. **Begin Problem Solving**:
   - Scientist Mode: Analyze problem, propose hypothesis
   - Engineer Mode: Implement code solution
   - Critic Mode: Review quality, validate results
   - Writer Mode: Draft paper sections
4. **Iterate** until all requirements met
5. **Session Debrief**: Add lessons learned

---

## Troubleshooting

### Issue: "Claude doesn't read all files"

**Solution**: Explicitly instruct:
```
Claude Code，请依次读取以下文件并确认：
1. docs/math_models_cheatsheet.md
2. docs/anti_patterns.md
3. docs/mcm_o_prize_style_guide.md
4. docs/optimization_strategies.md
5. docs/coding_best_practices.md

每个文件读完后，请用一句话总结核心内容。
```

### Issue: "Artifacts get overwritten"

**Solution**: Add to anti_patterns.md:
```markdown
## File Naming Convention
ALWAYS use timestamps: `artifact_YYYYMMDD_HHMMSS.ext`

Example:
- ✅ model1_20260123_143000.py
- ❌ model1.py (will be overwritten)
```

### Issue: "Mode switching doesn't work"

**Solution**: Use explicit commands:
```
Claude Code，现在切换到[科学家/工程师/批评家/作家]模式。
当前任务：[具体描述]
请使用对应的思维模式工作。
```

---

## Success Criteria

Setup is complete when:
- ✅ All directories exist
- ✅ All 5 knowledge base files created
- ✅ Best paper selected and analyzed
- ✅ Bootstrap instructions work
- ✅ Claude Code successfully completes first task in Scientist mode

---

**END OF CHECKLIST**

**Next Steps**: Execute setup, then start with Phase 0 (Problem Understanding) from the workflow.
