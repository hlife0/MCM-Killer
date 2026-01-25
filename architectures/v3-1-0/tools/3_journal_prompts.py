# ===============================================================================
# MCM-Killer v3.1.0 Journal Prompts (Functional Component)
# ===============================================================================
# Source: D:\migration\clean version\LLM-MM-Agent\MMAgent\prompt\journal_prompts.py
# Integration: P1 (Strongly Recommended) - Metacognitive reflection prompts
# Purpose: Research journal generation for @metacognition_agent
#
# These prompts enable the cognitive narrative (认知叙事) framework by
# extracting insights from execution traces and transforming them into
# MCM/ICM-style research journal entries.
# ===============================================================================

"""
MCM-Killer Journal Prompts Module

This module contains specialized prompts for generating Research Journal entries
at different stages of the mathematical modeling process.

Each prompt is designed to extract specific insights from the execution trace
and format them as MCM/ICM-style research journal entries.

Integration Point: @metacognition_agent (Phase 5.8 - Insight Extraction)

Author: MM-Agent Team (Integrated for MCM-Killer)
Date: 2026-01-25
"""

# =============================================================================
# SYSTEM PROMPT (Research Journal Mode)
# =============================================================================

JOURNAL_SYSTEM_PROMPT = """你不是一个日志记录员。你是一名参加 MCM/ICM 数学建模竞赛的首席研究员。
你的任务是基于 Agent 的执行流，维护一份高质量的《科研日记》(Research Journal)。
你的语言风格应该是学术的、客观的、反思性的 (Reflective)。
你需要从繁杂的执行日志中提取出模型假设、算法逻辑、遇到的困难以及解决方案。
忽略底层的 I/O 操作细节，专注于思维过程 (Chain of Thought)。
请使用 Markdown 格式，公式使用 LaTeX 格式 (例如 $x_i$)."""

JOURNAL_SYSTEM_PROMPT_EN = """You are not a log recorder. You are the Chief Researcher in an MCM/ICM mathematical modeling competition.
Your task is to maintain a high-quality Research Journal based on the Agent's execution flow.
Your language style should be academic, objective, and reflective.
You need to extract model assumptions, algorithm logic, difficulties encountered, and solutions from the complex execution logs.
Ignore low-level I/O operation details and focus on the thought process (Chain of Thought).
Please use Markdown format, and use LaTeX format for formulas (e.g., $x_i$)."""


# =============================================================================
# STAGE REFLECTION PROMPTS
# =============================================================================

STAGE_REFLECTION_ANALYSIS = """请根据以下 Agent 的思考过程（JSONL 片段），撰写一段"问题重述与分析"章节：

**要求**：
1. **变量定义**: 我们如何定义了问题的核心变量？哪些被忽略了？为什么？（体现假设的合理性）
2. **任务拆解**: 我们将问题拆解成了哪几个子任务？逻辑链条是什么？
3. **数据理解**: 我们从数据中观察到了什么关键特征？

**风格指南**：
- 使用第一人称（"我们"，"本研究"）
- 重点突出建模思路，而非技术细节
- 适当引用数据特征支持假设

输入事件流:
{events}

**请生成 Markdown 格式的章节内容**：
"""

STAGE_REFLECTION_ANALYSIS_EN = """Based on the following Agent's thought process (JSONL fragment), write a "Problem Restatement and Analysis" section:

**Requirements**:
1. **Variable Definition**: How did we define the core variables? Which were ignored? Why? (Demonstrate the reasonableness of assumptions)
2. **Task Decomposition**: What subtasks did we break the problem into? What is the logical chain?
3. **Data Understanding**: What key features did we observe from the data?

**Style Guide**:
- Use first person ("we", "this study")
- Emphasize modeling approach, not technical details
- Appropriately cite data features to support assumptions

Input event stream:
{events}

**Please generate Markdown format section content**:
"""

STAGE_REFLECTION_MODELING = """Agent 刚刚完成/尝试了数学模型的构建。请根据记录撰写"建模过程"章节：

**要求**：
1. **模型选择依据**: 为什么选择这些模型/算法？它是基于数据的什么特征？
2. **适用性讨论**: 该模型在当前场景下的优缺点是什么？
3. **尝试与迭代**: 如果 Agent 尝试了多个模型，请对比它们的效果。
4. **数学表达**: 使用 LaTeX 公式表达核心思想（如果适用）。

**风格指南**：
- 突出建模思想而非代码实现
- 用数学语言描述模型（如 $f(x) = \\sum_{{i=1}}^{{n}} w_i x_i$）
- 讨论模型的局限性

输入事件流:
{events}

**请生成 Markdown 格式的章节内容**：
"""

STAGE_REFLECTION_MODELING_EN = """Agent just completed/attempted mathematical model construction. Write the "Modeling Process" section based on the record:

**Requirements**:
1. **Model Selection Basis**: Why were these models/algorithms chosen? What data features is it based on?
2. **Applicability Discussion**: What are the pros and cons of this model in the current scenario?
3. **Attempts and Iterations**: If Agent tried multiple models, compare their effects.
4. **Mathematical Expression**: Use LaTeX formulas to express core ideas (if applicable).

**Style Guide**:
- Emphasize modeling thinking rather than code implementation
- Describe models in mathematical language (e.g., $f(x) = \\sum_{{i=1}}^{{n}} w_i x_i$)
- Discuss model limitations

Input event stream:
{events}

**Please generate Markdown format section content**:
"""


# =============================================================================
# ERROR DIAGNOSIS PROMPTS (For DEFCON 1 situations)
# =============================================================================

ERROR_DIAGNOSIS = """AGENT 任务已崩溃。你现在是"事故调查委员会"的成员。
你需要分析提供的【底层堆栈信息 (Raw Traceback)】，如实撰写尸检报告。

**【CRITICAL REQUIREMENTS - 必须遵守】**:
1. 如果包含 Raw Traceback，**必须优先依据 Traceback 进行分析**
2. 不要编造错误原因，说"不知道"比编造要好
3. 使用具体的文件路径和行号定位错误
4. 用 Markdown 格式，关键信息用粗体标出
5. **必须声明可信度等级**

输入信息:
{events}

**请按以下结构生成尸检报告**：

### 1. 致命原因 (Root Cause)

- ❌ **错误示范**：说"代码出错了"或"执行失败"
- ✅ **正确示范**：
  - "在调用 `pandas.read_csv()` 时找不到文件 'data.csv' (FileNotFoundError)"
  - "在计算矩阵逆时遇到了奇异矩阵 (LinAlgError: Singular matrix)"
  - "在尝试访问列表索引 100 时越界 (IndexError: list index out of range)"
  - "在访问字典键 'YEAR' 时不存在 (KeyError: 'YEAR')"

**要求**：明确指出是哪种Python异常，在什么操作时发生的。

### 2. 定位 (Location)

从 Traceback 中提取：
- **错误类型**: (例如：KeyError, ValueError, TypeError)
- **发生位置**: `文件路径:行号`
- **调用链**: Traceback 中关键的函数调用序列

**示例格式**：
```markdown
- **错误类型**: KeyError
- **发生位置**: `MMAgent/agent/task_solving.py:1234`
- **调用链**: `coding()` → `extract_code_structure()` → `df[column_name]`
```

### 3. 修复建议 (Fix Strategy)

基于具体的报错，提供可执行的修改建议：
- 数据问题：检查数据格式、列名、空值处理
- 代码逻辑问题：修改算法、增加验证、调整参数
- 环境配置问题：安装依赖、修改路径、调整权限

### 4. 可信度评估 (Confidence Level)

**必须包含以下声明之一**：
- **🟢 高可信度** - 分析基于完整的Python traceback
- **🟡 中等可信度** - 分析基于部分traceback或详细错误信息
- **🔴 低可信度** - 仅基于摘要信息，可能不准确

**请生成 Markdown 格式的尸检报告**：
"""

ERROR_DIAGNOSIS_EN = """AGENT task has crashed. You are now a member of the "Accident Investigation Committee".
You need to analyze the provided [Raw Traceback] and write an autopsy report truthfully.

**[CRITICAL REQUIREMENTS - MUST FOLLOW]**:
1. If Raw Traceback is included, **MUST prioritize analysis based on Traceback**
2. Don't fabricate error causes - saying "don't know" is better than making things up
3. Use specific file paths and line numbers to locate errors
4. Use Markdown format, bold key information
5. **MUST declare confidence level**

Input information:
{events}

**Please generate autopsy report following this structure**:

### 1. Root Cause

- ❌ **Wrong example**: Saying "code failed" or "execution failed"
- ✅ **Correct example**:
  - "FileNotFoundError when calling `pandas.read_csv()` - file 'data.csv' not found"
  - "LinAlgError: Singular matrix when computing matrix inverse"
  - "IndexError: list index out of range when accessing index 100"
  - "KeyError: 'YEAR' when accessing dictionary key"

**Requirement**: Clearly specify which Python exception, during what operation.

### 2. Location

Extract from Traceback:
- **Error Type**: (e.g., KeyError, ValueError, TypeError)
- **Location**: `file_path:line_number`
- **Call Chain**: Key function call sequence in Traceback

### 3. Fix Strategy

Based on specific error, provide executable modification suggestions.

### 4. Confidence Level

**Must include one of**:
- **🟢 High Confidence** - Analysis based on complete Python traceback
- **🟡 Medium Confidence** - Analysis based on partial traceback or detailed error info
- **🔴 Low Confidence** - Based only on summary info, may be inaccurate

**Please generate Markdown format autopsy report**:
"""


# =============================================================================
# RESULT VALIDATION PROMPT
# =============================================================================

RESULT_VALIDATION = """我们得到了一组计算结果。请进行"结果分析与灵敏度讨论"：

**要求**：
1. **合理性检查**: 数值是否在物理/逻辑上合理？（比如概率不能大于1，人口不能为负）。
2. **趋势解读**: 请描述生成的图表 (Charts) 展示了什么趋势？引用具体的图片文件名。
3. **自我批判 (Critical Thinking)**: 当前结果可能受限于哪些假设？如果时间允许，我们在哪些方面可以改进？
4. **结论**: 给出建模任务的明确结论。

**风格指南**：
- 客观评估结果，不夸大
- 承认模型的局限性
- 提出可能的改进方向

结果数据:
{solution}

**请生成 Markdown 格式的章节内容**：
"""

RESULT_VALIDATION_EN = """We have obtained a set of calculation results. Please conduct "Result Analysis and Sensitivity Discussion":

**Requirements**:
1. **Reasonableness Check**: Are the values physically/logically reasonable? (e.g., probability cannot exceed 1, population cannot be negative)
2. **Trend Interpretation**: Describe what trends the generated charts show. Reference specific image filenames.
3. **Critical Thinking**: What assumptions may limit the current results? Given more time, where could we improve?
4. **Conclusion**: Provide clear conclusions for the modeling task.

**Style Guide**:
- Objectively evaluate results without exaggeration
- Acknowledge model limitations
- Propose possible improvement directions

Result data:
{solution}

**Please generate Markdown format section content**:
"""


# =============================================================================
# NARRATIVE ARC EXTRACTION (MCM-Killer Specific)
# =============================================================================

NARRATIVE_ARC_EXTRACTION = """你是 @metacognition_agent，负责从训练日志中提取叙事弧线。

**输入**：
- 开发日记 (dev_diary.md)
- 训练日志摘要 (training_summary.json)
- 模型设计文档

**任务**：按照 Hero's Journey 模板提取叙事弧线：

## 1. The Call (初始状态)
- 初始方法是什么？
- 为什么选择这个方法？

## 2. The Ordeal (遇到的困难)
- 遇到了什么技术障碍？
- 具体的错误指标是什么？(R-hat, RMSE, 收敛问题等)

## 3. The Revelation (洞察)
- 这个困难揭示了什么问题本质？
- 技术指标 → 物理/领域意义的映射

## 4. The Resolution (解决方案)
- 如何改进了方法？
- 新方法的数学表达

## 5. The Treasure (最终成果)
- 改进后的指标是什么？
- 对政策/决策的启示

**输入日志**:
{logs}

**请按以上结构输出 narrative_arc.md**：
"""

NARRATIVE_ARC_EXTRACTION_EN = """You are @metacognition_agent, responsible for extracting narrative arcs from training logs.

**Input**:
- Development diary (dev_diary.md)
- Training log summary (training_summary.json)
- Model design documents

**Task**: Extract narrative arc following Hero's Journey template:

## 1. The Call (Initial State)
- What was the initial method?
- Why was this method chosen?

## 2. The Ordeal (Difficulties Encountered)
- What technical obstacles were encountered?
- What were the specific error metrics? (R-hat, RMSE, convergence issues, etc.)

## 3. The Revelation (Insight)
- What problem essence did this difficulty reveal?
- Technical metric → Physical/domain meaning mapping

## 4. The Resolution (Solution)
- How was the method improved?
- Mathematical expression of new method

## 5. The Treasure (Final Achievement)
- What are the improved metrics?
- Implications for policy/decision-making

**Input logs**:
{logs}

**Please output narrative_arc.md following the above structure**:
"""


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def format_stage_prompt(stage_name: str, events_json: str, lang: str = "en") -> str:
    """
    根据阶段名称返回对应的 prompt 模板。

    Args:
        stage_name: 阶段名称 (problem_analysis, mathematical_modeling, etc.)
        events_json: JSON 格式的事件流
        lang: Language preference ("en" or "cn")

    Returns:
        str: 格式化后的 prompt
    """
    if lang == "cn":
        stage_prompts = {
            "problem_analysis": STAGE_REFLECTION_ANALYSIS,
            "mathematical_modeling": STAGE_REFLECTION_MODELING,
            "error_diagnosis": ERROR_DIAGNOSIS,
            "result_validation": RESULT_VALIDATION,
            "narrative_arc": NARRATIVE_ARC_EXTRACTION,
        }
    else:
        stage_prompts = {
            "problem_analysis": STAGE_REFLECTION_ANALYSIS_EN,
            "mathematical_modeling": STAGE_REFLECTION_MODELING_EN,
            "error_diagnosis": ERROR_DIAGNOSIS_EN,
            "result_validation": RESULT_VALIDATION_EN,
            "narrative_arc": NARRATIVE_ARC_EXTRACTION_EN,
        }

    if stage_name in stage_prompts:
        return stage_prompts[stage_name].format(events=events_json)
    else:
        raise ValueError(f"Unknown stage: {stage_name}. Available: {list(stage_prompts.keys())}")


def get_system_prompt(lang: str = "en") -> str:
    """返回系统提示词 / Return system prompt"""
    return JOURNAL_SYSTEM_PROMPT if lang == "cn" else JOURNAL_SYSTEM_PROMPT_EN


def get_all_stage_names() -> list:
    """Return list of all available stage names."""
    return [
        "problem_analysis",
        "mathematical_modeling",
        "error_diagnosis",
        "result_validation",
        "narrative_arc",
    ]


# =============================================================================
# VERSION INFO
# =============================================================================

__version__ = "1.0.0"
__source__ = "D:\\migration\\clean version\\LLM-MM-Agent\\MMAgent\\prompt\\journal_prompts.py"
__integration_date__ = "2026-01-25"
