# ===============================================================================
# MCM-Killer v3.1.0 Journal Prompts (Functional Component)
# ===============================================================================
# Source: D:\migration\clean version\LLM-MM-Agent\MMAgent\prompt\journal_prompts.py
# Integration: P1 (Strongly Recommended) - Metacognitive reflection prompts
# Purpose: Research journal generation for @metacognition_agent
#
# These prompts enable the cognitive narrative framework by
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

JOURNAL_SYSTEM_PROMPT = """You are not a log recorder. You are the Chief Researcher in an MCM/ICM mathematical modeling competition.
Your task is to maintain a high-quality Research Journal based on the Agent's execution flow.
Your language style should be academic, objective, and reflective.
You need to extract model assumptions, algorithm logic, difficulties encountered, and solutions from the complex execution logs.
Ignore low-level I/O operation details and focus on the thought process (Chain of Thought).
Please use Markdown format, and use LaTeX format for formulas (e.g., $x_i$)."""

JOURNAL_SYSTEM_PROMPT_EN = JOURNAL_SYSTEM_PROMPT


# =============================================================================
# STAGE REFLECTION PROMPTS
# =============================================================================

STAGE_REFLECTION_ANALYSIS = """Based on the following Agent's thought process (JSONL fragment), write a "Problem Restatement and Analysis" section:

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

STAGE_REFLECTION_ANALYSIS_EN = STAGE_REFLECTION_ANALYSIS

STAGE_REFLECTION_MODELING = """Agent just completed/attempted mathematical model construction. Write the "Modeling Process" section based on the record:

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

STAGE_REFLECTION_MODELING_EN = STAGE_REFLECTION_MODELING


# =============================================================================
# ERROR DIAGNOSIS PROMPTS (For DEFCON 1 situations)
# =============================================================================

ERROR_DIAGNOSIS = """AGENT task has crashed. You are now a member of the "Accident Investigation Committee".
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

ERROR_DIAGNOSIS_EN = ERROR_DIAGNOSIS


# =============================================================================
# RESULT VALIDATION PROMPT
# =============================================================================

RESULT_VALIDATION = """We have obtained a set of calculation results. Please conduct "Result Analysis and Sensitivity Discussion":

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

RESULT_VALIDATION_EN = RESULT_VALIDATION


# =============================================================================
# NARRATIVE ARC EXTRACTION (MCM-Killer Specific)
# =============================================================================

NARRATIVE_ARC_EXTRACTION = """You are @metacognition_agent, responsible for extracting narrative arcs from training logs.

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

NARRATIVE_ARC_EXTRACTION_EN = NARRATIVE_ARC_EXTRACTION


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def format_stage_prompt(stage_name: str, events_json: str, lang: str = "en") -> str:
    """
    Return the corresponding prompt template based on stage name.

    Args:
        stage_name: Stage name (problem_analysis, mathematical_modeling, etc.)
        events_json: JSON format event stream
        lang: Language preference ("en" or "cn")

    Returns:
        str: Formatted prompt
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
    """Return system prompt"""
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
