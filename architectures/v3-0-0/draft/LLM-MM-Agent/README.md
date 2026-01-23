# LLM-MM-Agent 文档结构总览

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/README.md`
> **最后更新**: 2026-01-24

本文档系列按照 **LLM-MM-Agent 项目的实际目录结构** 组织，提供完整的导航和详细说明。

---

## 系统定位

**LLM-MM-Agent** 与 **MCM-Killer** 是两个**独立的系统**，各自有不同的设计目标：

| 特性 | LLM-MM-Agent | MCM-Killer |
|------|--------------|------------|
| **定位** | 学术研究原型 (NeurIPS/ICML 2025) | 竞赛实战系统 |
| **目标** | 探索 LLM 解决数学建模问题的可行性 | 最大化竞赛成绩和完成质量 |
| **工作流** | 4 阶段流水线 | 18 阶段工作流 + 7 个验证门控 |
| **Agent 数量** | 5 个基础 Agent | 14 个专业 Agent |
| **复杂度** | 相对简单，适合学习和研究 | 高度复杂，严格质量控制 |
| **参考位置** | `clean version/LLM-MM-Agent/` | `MCM-Killer/` |

**重要**: LLM-MM-Agent 是独立的学术研究系统，与 MCM-Killer 没有从属或衍生关系。

---

## 完整目录树

```
clean version/LLM-MM-Agent/
│
├── 📄 项目根文件 (01_Project_Root.md)
│   ├── config.yaml
│   ├── requirements.txt
│   ├── README.md
│   ├── README_zh.md
│   ├── run.py
│   └── fix_templates.py
│
├── 📁 MMAgent/ (核心实现目录)
│   ├── main.py ⭐ (02_MMAgent_Main.md) ✅
│   │
│   ├── 📁 prompt/ ⭐⭐⭐⭐⭐ (03_MMAgent_Prompt.md) ✅
│   │   ├── template.py - 核心提示词模板（45+ 模板）
│   │   ├── journal_prompts.py
│   │   ├── chart_template_prompt.py
│   │   ├── variable_contract_prompt.py
│   │   ├── constants.py
│   │   └── decompose_prompt.json
│   │
│   ├── 📁 agent/ (04_MMAgent_Agent.md) ✅
│   │   ├── base_agent.py
│   │   ├── coordinator.py
│   │   ├── task_solving.py
│   │   ├── retrieve_method.py
│   │   ├── problem_analysis.py
│   │   ├── create_charts.py
│   │   ├── data_description.py
│   ├── debug_agent.py
│   │   └── problem_decompose.py
│   │
│   ├── 📁 core/ (05_MMAgent_Core.md) ✅
│   │   ├── abduction_engine.py
│   │   ├── red_team_critic.py
│   │   ├── research_strategist.py
│   │   ├── research_strategist_fsm.py
│   │   └── state_manager.py
│   │
│   ├── 📁 engine/ (06_MMAgent_Engine.md) ✅
│   │   ├── chart_renderer.py
│   │   ├── diagram_engine.py
│   │   ├── feature_engineer.py
│   │   ├── knowledge_retriever.py
│   │   ├── model_arena.py
│   │   ├── robustness_tester.py
│   │   ├── scientific_renderer.py
│   │   ├── sensitivity_analyzer.py
│   │   ├── sensitivity_engine.py
│   │   └── validation_suite.py
│   │
│   ├── 📁 llm/ (07_MMAgent_LLM.md) ✅
│   │   ├── llm.py - 统一 LLM 接口
│   │   └── __init__.py
│   │
│   ├── 📁 narrative/ (08_MMAgent_Narrative.md) ✅
│   │   ├── narrative_weaver.py
│   │   ├── academic_tools.py
│   │   ├── critique_generator.py
│   │   └── abstract_orchestrator.py
│   │
│   ├── 📁 execution/ (09_MMAgent_Execution.md) ✅
│   │   └── kernel_client.py
│   │
│   ├── 📁 reporting/ (10_MMAgent_Reporting.md) ✅
│   │
│   ├── 📁 schema/ (11_MMAgent_Schema.md) ✅
│   │
│   ├── 📁 data/ (12_MMAgent_Data.md) ✅
│   │   └── data_ingestor.py
│   │
│   ├── 📁 knowledge/ (13_MMAgent_Knowledge.md) ✅
│   │   ├── knowledge_base.py
│   │   ├── domain_knowledge.json
│   │   └── history_knowledge.json
│   │
│   ├── 📁 HMML/ (14_HMML.md) ✅
│   │   ├── HMML.md
│   │   └── HMML.json
│   │
│   ├── 📁 utils/ (15_Utilities.md) ✅
│   │   └── [40+ 工具模块]
│   │
│   ├── 📁 code_template/ (16_Code_Template.md) ✅
│   │   ├── main.py - main10.py
│   │
│   ├── 📁 prompts/ (提示词备用)
│   │
│   └── 📁 output/ (输出目录)
│
├── 📁 MMBench/ (17_MMBench.md) ✅
│   ├── problem/ - 111 题目 JSON
│   ├── dataset/ - 数据文件
│   └── evaluation/ - 评估框架
│
├── 📁 test workplace/ (18_Test_Infrastructure.md) ✅
│   ├── tests/ - 35+ 测试
│   ├── docs/ - 测试文档
│   └── ultrathink/ - 分析报告
│
├── 📁 assets/ (19_Assets.md) 🔴 缺失
├── 📁 doc/ (20_Doc.md) 🔴 缺失
├── 📁 figs/ (21_Figs.md) 🔴 缺失
└── 📁 scripts/ (22_Scripts.md) 🔴 缺失
```

---

## 文档导航

### 已完成的文档 (18/22)

| 编号 | 文档 | 状态 | 优先级 |
|------|------|------|--------|
| 00 | [README.md](README.md) | ✅ | - |
| 01 | [01_Project_Root.md](01_Project_Root.md) | ✅ | P3 |
| 02 | [02_MMAgent_Main.md](02_MMAgent_Main.md) | ✅ 新建 | 🔴 **P0** |
| 03 | [03_MMAgent_Prompt.md](03_MMAgent_Prompt.md) | ✅ 新建 | 🔴 **P0** |
| 04 | [04_MMAgent_Agent.md](04_MMAgent_Agent.md) | ✅ 重命名 | 🟡 P1 |
| 05 | [05_MMAgent_Core.md](05_MMAgent_Core.md) | ✅ 新建 | 🔴 **P0** |
| 06 | [06_MMAgent_Engine.md](06_MMAgent_Engine.md) | ✅ 新建 | 🔴 **P0** |
| 07 | [07_MMAgent_LLM.md](07_MMAgent_LLM.md) | ✅ 新建 | 🔴 **P0** |
| 08 | [08_MMAgent_Narrative.md](08_MMAgent_Narrative.md) | ✅ 新建 | 🟡 P1 |
| 09 | [09_MMAgent_Execution.md](09_MMAgent_Execution.md) | ✅ 新建 | 🟡 P1 |
| 10 | [10_MMAgent_Reporting.md](10_MMAgent_Reporting.md) | ✅ 新建 | 🟡 P1 |
| 11 | [11_MMAgent_Schema.md](11_MMAgent_Schema.md) | ✅ 新建 | 🟡 P1 |
| 12 | [12_MMAgent_Data.md](12_MMAgent_Data.md) | ✅ 新建 | 🟡 P1 |
| 13 | [13_MMAgent_Knowledge.md](13_MMAgent_Knowledge.md) | ✅ 新建 | 🟡 P1 |
| 14 | [14_HMML.md](14_HMML.md) | ✅ 重命名 | 🟡 P1 |
| 15 | [15_Utilities.md](15_Utilities.md) | ✅ 重命名 | 🟡 P1 |
| 16 | [16_Code_Template.md](16_Code_Template.md) | ✅ 新建 | 🟡 P1 |
| 17 | [17_MMBench.md](17_MMBench.md) | ✅ 重命名 | 🟡 P1 |
| 18 | [18_Test_Infrastructure.md](18_Test_Infrastructure.md) | ✅ 重命名 | 🟡 P1 |
| 19 | [19_Assets.md](19_Assets.md) | 🔴 缺失 | 🟢 P3 |
| 20 | [20_Doc.md](20_Doc.md) | 🔴 缺失 | 🟢 P3 |
| 21 | [21_Figs.md](21_Figs.md) | 🔴 缺失 | 🟢 P3 |
| 22 | [22_Scripts.md](22_Scripts.md) | 🔴 缺失 | 🟢 P3 |

---

## 完成进度

### ✅ 已完成 (18/22)

- ✅ **核心文档 (8个)**：README, Project_Root, Main, Prompt, Agent, Core, Engine, LLM, Utilities, HMML, MMBench, Test_Infrastructure
- ✅ **补充文档 (9个)**：Narrative, Execution, Reporting, Schema, Data, Knowledge, Code_Template, Agent (重命名)

### 🔴 待完成 (4/22)

- 🔴 **P3 优先级 (4个)**：Assets, Doc, Figs, Scripts - 这些是辅助文件，可以稍后补充

---

## 重要更新

### 新发现的核心模块

通过完整的 tree 分析，发现了之前遗漏的重要模块：

1. **MMAgent/prompt/** ⭐⭐⭐⭐⭐
   - 系统的"大脑"
   - 45+ 提示词模板
   - BASE_SYSTEM_PROMPT, CODING_SYSTEM_PROMPT
   - 这是之前最重要的遗漏！

2. **MMAgent/core/** ⭐⭐⭐⭐
   - 5 个核心组件
   - 溯源引擎、红队批评家、研究策略家

3. **MMAgent/engine/** ⭐⭐⭐⭐
   - 10 个专业引擎
   - 图表渲染、特征工程、知识检索等

4. **MMAgent/llm/** ⭐⭐⭐⭐
   - 统一 LLM 接口
   - 线程锁防止速率限制
   - Token 使用跟踪

5. **MMAgent/narrative/** ⭐⭐⭐
   - 叙述生成模块
   - 学术写作工具

---

## 下一步

LLM-MM-Agent 文档结构已完成，接下来需要创建 **MCM-Killer 的对应文档结构**。

---

**文档版本**: v2.0
**完成进度**: 18/22 (81.8%)
**最后更新**: 2026-01-24
