# 6-STARS: 提示词系统

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/6-STARS/00_PROMPT_SYSTEM.md`
> **星级**: ⭐⭐⭐⭐⭐⭐
> **来源文档**: `03_MMAgent_Prompt.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/template.py`

---

## 核心资产: template.py

### 为什么是 6 星？

`template.py` 是 LLM-MM-Agent 系统的**大脑**，定义了所有 Agent 的行为模式。它不仅是一组提示词，更是一套**模块化的提示词架构**，实现了：

1. **Token 节省**: ~87% Token 节省通过模块化系统提示词
2. **行为契约**: 明确定义 Agent 的职责边界
3. **防重复执行**: BASE_SYSTEM_PROMPT 的第 1 条原则就是"不要重复其他 Agent 已完成的工作"
4. **代码生成规范**: CODING_SYSTEM_PROMPT 强制 6 行导入 + UTF-8 输出
5. **数据加载规则**: 必须从 `../data/` 加载，禁止硬编码路径

### 核心提示词模板

#### 1. BASE_SYSTEM_PROMPT ⭐⭐⭐⭐⭐⭐

```python
BASE_SYSTEM_PROMPT = """You are an expert Mathematical Modeling Assistant...
PRINCIPLES:
1. Do NOT repeat steps already completed by other agents.
2. Rely on provided outputs/files from previous tasks.
3. Be concise, rigorous, and professional.

YOUR TASK:
{task}

CONTEXT FROM PREVIOUS TASKS:
{context}

INSTRUCTIONS:
{instructions}

OUTPUT REQUIREMENTS:
- Provide clear, step-by-step reasoning
- Include mathematical formulations where appropriate
- Cite methods from the provided knowledge base (HMML)
- Save results to the specified output directory
"""
```

**关键设计**:
- **防止重复工作**: Principle 1 明确禁止重复其他 Agent 的工作
- **依赖前序输出**: Principle 2 强制依赖前序任务的输出/文件
- **模块化占位符**: `{task}`, `{context}`, `{instructions}` 支持动态注入

#### 2. CODING_SYSTEM_PROMPT ⭐⭐⭐⭐⭐⭐

```python
CODING_SYSTEM_PROMPT = """You are an expert Python Programmer...
## MANDATORY CODE STRUCTURE (CRITICAL - DO NOT SKIP OR MODIFY)
Your generated code MUST start with EXACTLY these 6 lines:
```python
import sys
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Force UTF-8 output immediately (mandatory)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

## DATA LOADING RULES (CRITICAL)
1. ALWAYS load data from `../data/` directory
2. Use the EXACT column names from the data description
3. NEVER hardcode file paths

## OUTPUT REQUIREMENTS
1. Save ALL results to `../output/`
2. Use descriptive filenames (e.g., `task1_results.csv`)
3. Generate at least 1 visualization
4. Include console output for verification
"""
```

**关键设计**:
- **强制 6 行导入**: 防止缺少依赖，确保代码可执行
- **强制 UTF-8 输出**: 防止中文乱码
- **数据加载规则**: 防止硬编码路径导致 Guard 违规
- **输出规范**: 确保结果可追踪

#### 3. TASK_SPECIFIC_PROMPTS ⭐⭐⭐⭐⭐

针对不同阶段的 40+ 专用提示词模板：

```python
# Stage 1: Problem Analysis
PROBLEM_ANALYSIS_PROMPT = """
Analyze the mathematical modeling problem...
"""

# Stage 2: Method Selection
METHOD_SELECTION_PROMPT = """
Select appropriate methods from HMML...
"""

# Stage 3: Computational Solving
COMPUTATIONAL_SOLVING_PROMPT = """
Generate Python code to solve the problem...
"""

# Stage 4: Solution Reporting
SOLUTION_REPORTING_PROMPT = """
Generate a comprehensive report...
"""
```

**模块化优势**:
- **单一职责**: 每个提示词专注于一个阶段
- **可复用**: 相同阶段可以复用相同提示词
- **可测试**: 独立测试每个提示词的效果

### Token 节省策略

**传统方式** (每次生成完整提示词):
```
System Prompt (2000 tokens) + Task (500 tokens) = 2500 tokens
```

**模块化方式** (复用系统提示词):
```
Base System Prompt (500 tokens) + Task (500 tokens) = 1000 tokens
Token 节省: (2500 - 1000) / 2500 = 60%
加上模块化的其他提示词，总节省约 87%
```

### 迁移价值

#### ✅ 高度可复用

1. **多 Agent 系统**: 可以直接应用到任何多 Agent 系统
2. **数学建模领域**: 提示词模板针对数学建模优化
3. **代码生成场景**: CODING_SYSTEM_PROMPT 可用于任何代码生成任务
4. **阶段式工作流**: TASK_SPECIFIC_PROMPTS 适配 4 阶段管道

#### 🎯 设计模式可借鉴

1. **模块化系统提示词**: 分离基础行为和任务指令
2. **占位符注入**: 使用 `{variable}` 动态注入上下文
3. **原则前置**: 在系统提示词开头明确列出原则
4. **强约束**: 使用 MANDATORY, CRITICAL 等词汇强调约束

#### ⚠️ 需要适配

1. **域名特定**: 需要适配到新的应用领域
2. **阶段调整**: 如果工作流不是 4 阶段，需要调整提示词
3. **语言偏好**: 如果需要中文输出，需要调整提示词

### 扩展到 400+ 方法和 8+ 阶段

#### 1. 提示词模板扩容

**当前**: 45+ 模板支持 4 阶段管道
**目标**: 100+ 模板支持 8+ 阶段管道

**策略**:
- 为新增 4 个阶段创建专用提示词
- 扩展 HMML 方法检索提示词（支持 5 层层级）
- 增加中间验证阶段的提示词

#### 2. 上下文管理优化

**当前**: Context Pruning 防止上下文溢出
**目标**: 更智能的上下文压缩

**策略**:
- 实现上下文重要性评分
- 动态裁剪低重要性上下文
- 使用向量压缩长上下文

#### 3. 提示词版本管理

**当前**: 单一 template.py 文件
**目标**: 提示词版本化和 A/B 测试

**策略**:
- 将提示词存储为 JSON 文件
- 支持提示词版本控制
- 实现提示词 A/B 测试框架

### 核心创新点

1. **防止重复工作**: BASE_SYSTEM_PROMPT Principle 1
2. **强制代码规范**: CODING_SYSTEM_PROMPT 6 行导入
3. **模块化架构**: 45+ 模板可独立维护
4. **Token 高效**: ~87% Token 节省
5. **强约束设计**: MANDATORY, CRITICAL 等强调词

---

## 迁移清单

### 必须迁移 (P0)

- [ ] `BASE_SYSTEM_PROMPT` - 多 Agent 系统基础
- [ ] `CODING_SYSTEM_PROMPT` - 代码生成规范
- [ ] `SafePlaceholder` 模式 - 防止模板格式化崩溃

### 强烈推荐 (P1)

- [ ] `TASK_SPECIFIC_PROMPTS` - 阶段专用提示词
- [ ] `journal_prompts.py` - 后处理分析提示词
- [ ] `variable_contract_prompt.py` - 变量契约提示词

### 可选迁移 (P2)

- [ ] `chart_template_prompt.py` - 图表生成提示词
- [ ] `constants.py` - 提示词常量
- [ ] `decompose_prompt.json` - 分解提示词

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
