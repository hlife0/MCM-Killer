# MMAgent: 提示词系统

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/03_MMAgent_Prompt.md`
> **重要程度**: ⭐⭐⭐⭐⭐ 系统的"大脑"
> **迁移价值**: **极高** - 提示词设计模式可复用

本目录（`MMAgent/prompt/`）包含 LLM-MM-Agent 系统的所有提示词模板，是系统的"大脑"。提示词定义了 Agent 与 LLM 交互的所有方式，包括任务分析、数学建模、代码生成、图表生成、日记撰写等各个阶段的提示词。提示词系统采用模块化设计，通过 `system` 参数传递基础提示词，减少约 87% 的 token 使用量。核心提示词包括：BASE_SYSTEM_PROMPT（非编码任务基础提示）、CODING_SYSTEM_PROMPT（编码任务基础提示）、ONE_SHOT_CODING_EXAMPLE（代码示例）等。

**迁移价值**：提示词系统是 LLM-MM-Agent 的核心资产，其设计思想和方法值得借鉴。系统提示词、模块化提示词、示例驱动提示词等模式可以应用到任何基于 LLM 的自动化系统。特别是在数学建模、代码生成、数据分析等领域，这些提示词模板可以直接复用或稍作修改。

---

## 核心文件

### `template.py` ⭐⭐⭐⭐⭐⭐
**核心提示词模板**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/template.py`。包含 45+ 个提示词模板，覆盖系统的所有功能模块。

**核心提示词**：

1. **BASE_SYSTEM_PROMPT** - 非编码任务基础提示词
   - 原则：不重复其他 Agent 已完成的步骤
   - 依赖提供的输出/文件
   - 简洁、严谨、专业
   - 使用纯文本和 LaTeX 公式

2. **CODING_SYSTEM_PROMPT** - 编码任务基础提示词
   - 强制 UTF-8 输出
   - 强制 6 行导入语句（sys, io, pandas, numpy, matplotlib）
   - 数据加载规则（仅使用文件名，禁止路径）
   - 列名标准化（UPPERCASE）
   - 禁止硬编码路径
   - 超时限制（300s）

3. **ONE_SHOT_CODING_EXAMPLE** - 代码示例
   - 按示例结构编写代码
   - 准入输出函数
   - 保存中间结果

**任务阶段提示词**（45+ 模板）：
- PROBLEM_ANALYSIS_*：问题分析相关
- TASK_ANALYSIS_*：任务分析相关
- TASK_FORMULAS_*：公式推导相关
- TASK_MODELING_*：数学建模相关
- TASK_CODING_*：代码生成相关
- TASK_RESULT_*：结果解释相关
- TASK_ANSWER_*：答案生成相关
- CHART_*：图表生成相关

**迁移价值**：template.py 是系统的核心资产。BASE_SYSTEM_PROMPT 和 CODING_SYSTEM_PROMPT 定义了 Agent 的基本行为模式，可以复用到任何多 Agent 系统。强制导入、数据加载规则、路径规范等工程实践非常实用。

---

### `journal_prompts.py` ⭐⭐⭐⭐⭐
**日记提示词**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/journal_prompts.py`。

**核心提示词**：
- **SYSTEM_PROMPT**：日记生成系统提示词
- **STAGE_REFLECTION_ANALYSIS**：问题分析阶段复盘
- **STAGE_REFLECTION_MODELING**：数学建模阶段复盘
- **ERROR_DIAGNOSIS**：错误诊断提示词
- **ERROR_DIAGNOSIS_V2**：错误诊断 V2（结构化 JSON 输出）
- **RESULT_VALIDATION**：结果验证提示词

**功能**：这些提示词被 LatentReporter 使用，用于：
- 阶段性复盘（reflect_on_stage）
- 错误诊断（diagnose_failure）
- 结果总结（summarize_results）

**迁移价值**：后处理分析提示词可以用于任何需要生成研究报告、调试日志的系统。STAGE_REFLECTION 模式可以用于阶段性回顾，ERROR_DIAGNOSIS 模式可以用于错误分析。

---

### `chart_template_prompt.py` ⭐⭐⭐
**图表模板提示词**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/chart_template_prompt.py`。

包含图表生成的提示词模板，用于指导 LLM 生成各种类型的可视化图表（折线图、柱状图、散点图、热力图等）。

**迁移价值**：图表生成提示词可以复用到任何需要生成可视化代码的系统。

---

### `variable_contract_prompt.py` ⭐⭐⭐⭐
**变量契约提示词**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/variable_contract_prompt.py`。

定义建模阶段和编码阶段之间的变量契约，确保变量名、类型、来源的一致性。

**迁移价值**：变量契约模式可以用于任何多阶段系统，确保阶段间的数据一致性。

---

### `constants.py` ⭐⭐
**提示词常量**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/constants.py`。

定义提示词中使用的各种常量（如方法数量、任务数量、图表数量等）。

---

### `decompose_prompt.json` ⭐⭐
**分解提示词**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/prompt/decompose_prompt.json`。

JSON 格式的问题分解提示词。

---

## 提示词组织结构

```
MMAgent/prompt/
├── template.py              # 【核心】45+ 提示词模板 ⭐⭐⭐⭐⭐⭐
├── journal_prompts.py       # 日记提示词 ⭐⭐⭐⭐⭐
├── chart_template_prompt.py # 图表模板提示词 ⭐⭐⭐
├── variable_contract_prompt.py # 变量契约提示词 ⭐⭐⭐⭐
├── constants.py             # 提示词常量 ⭐⭐
├── decompose_prompt.json    # 分解提示词 ⭐⭐
└── __init__.py
```

---

## 关键设计模式

### 1. 模块化提示词（System Prompts）

**问题**：重复的内容导致 token 浪费
**解决方案**：提取公共部分作为 system prompt

```python
BASE_SYSTEM_PROMPT = """You are an expert Mathematical Modeling Assistant..."""
CODING_SYSTEM_PROMPT = """You are an expert Python Programmer..."""
```

**效果**：token 使用量减少约 87%

### 2. 示例驱动提示词（One-Shot Learning）

**问题**：LLM 生成代码不符合要求
**解决方案**：在提示词中包含正确示例

```python
ONE_SHOT_CODING_EXAMPLE = """
## REFERENCE EXAMPLE (Follow this structure):
```python
import sys
import io
import os
import pandas as pd
# ... 完整示例代码
```
"""
```

### 3. 强制约束提示词（Mandatory Constraints）

**问题**：LLM 忽略重要规则
**解决方案**：使用强烈标记和重复

```python
## MANDATORY CODE STRUCTURE (CRITICAL - DO NOT SKIP OR MODIFY)
## CRITICAL ENVIRONMENT RULES
## CRITICAL WARNING
```

### 4. 环境规则提示词（Environment Rules）

**数据加载规则**：
```python
## [CRITICAL] Data Loading:
- ALWAYS use `load_csv('filename.csv')` with ONLY the filename
- NEVER use paths like `dataset/` or `C:/` or `D:/`
- NEVER use os.path.join() with paths
```

**强制 UTF-8 输出**：
```python
# Force UTF-8 output immediately (mandatory - prevents encoding errors)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

### 5. 禁止列表提示词（Forbidden List）

**问题**：LLM 使用不安全的操作
**解决方案**：明确列出禁止项

```python
## FORBIDDEN
- NO `input()` calls.
- NO specialized libraries
- NO raw `print(df)` (too large)
- NO omitting the mandatory imports
```

---

## 与其他模块的集成

### 与 Agent 模块的集成

- `agent/task_solving.py` 使用 TASK_* 提示词
- `agent/create_charts.py` 使用 CHART_* 提示词
- `agent/problem_analysis.py` 使用 PROBLEM_ANALYSIS 提示词

### 与 Utils 模块的集成

- `utils/latent_reporter.py` 使用 journal_prompts.py
- `utils/computational_solving.py` 使用 TASK_CODING 提示词

### 与 LLM 接口的集成

- `llm/llm.py` 的 `generate()` 方法接受 system 参数
- System prompt + User prompt 组合使用

---

## 迁移建议

### 高优先级（强烈推荐迁移）

1. **BASE_SYSTEM_PROMPT 和 CODING_SYSTEM_PROMPT**
   - 适用于任何多 Agent 系统
   - 强制导入、数据加载规则、路径规范是通用工程实践

2. **强制 UTF-8 输出**
   - 解决跨平台编码问题
   - Windows 环境特别重要

3. **禁止硬编码路径**
   - 提高代码可移植性
   - 防止 Guard 违规

### 中优先级（根据需求迁移）

4. **STAGE_REFLECTION 提示词**
   - 适用于需要阶段性复盘的系统
   - 结合 LatentReporter 使用

5. **ERROR_DIAGNOSIS 提示词**
   - 适用于需要错误分析的系统
   - 结构化 JSON 输出便于解析

6. **图表生成提示词**
   - 侧重于可视化场景

### 低优先级（可选）

7. **变量契约提示词**
   - 仅在需要跨阶段变量一致性时使用

---

## 关键发现

1. **提示词是系统的"大脑"**：所有 Agent 行为由提示词定义
2. **模块化设计节省 87% token**：System prompt 可以被缓存
3. **示例驱动比指令驱动更有效**：One-shot learning 提高代码质量
4. **强制约束比建议更有效**：Mandatory/CRITICAL 标记显著提高遵守率
5. **环境规则必须明确**：数据加载、编码、路径等规则不能模糊

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**总模板数**: 45+ 个提示词模板
