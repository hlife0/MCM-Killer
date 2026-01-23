# VALUABLE - 核心资产精选

> **绝对路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/README.md`
> **创建时间**: 2026-01-24
> **来源**: LLM-MM-Agent 项目中标注为 4、5、6 星的核心模块

本目录精选了 LLM-MM-Agent 项目中最重要的核心资产，按星级排序，附带详细的架构分析和迁移说明。

---

## 星级说明

| 星级 | 含义 | 数量 | 用途 |
|------|------|------|------|
| ⭐⭐⭐⭐⭐⭐ | **核心创新** | 29 项 | 系统的独特创新，不可替代的核心组件 |
| ⭐⭐⭐⭐⭐ | **关键资产** | 16 项 | 系统的关键模块，高度复用价值 |
| ⭐⭐⭐⭐ | **重要组件** | 16 项 | 系统的重要组件，值得参考借鉴 |

---

## 快速导航

### 📁 6-STARS/ (29 项)

**提示词系统** (1 项)
- `03_MMAgent_Prompt.md.template_py` - **45+ 提示词模板**，系统的"大脑"

**Agent 协作核心** (6 项)
- `04_MMAgent_Agent.md.coordinator_py` - **DAG 调度器**，拓扑排序任务调度
- `04_MMAgent_Agent.md.task_solving_py` - **SafePlaceholder 模式**，分阶段任务处理
- `04_MMAgent_Agent.md.retrieve_method_py` - **嵌入相似度检索**，智能知识检索
- `04_MMAgent_Agent.md.problem_analysis_py` - **Actor-Critic 迭代**，动态优化
- `04_MMAgent_Agent.md.data_description_py` - **数据分析引擎**

**核心分析引擎** (4 项)
- `05_MMAgent_Core.md.abduction_engine_py` - **溯因推理引擎**，诊断分析
- `05_MMAgent_Core.md.red_team_critic_py` - **红队批评家**，质量评估
- `05_MMAgent_Core.md.research_strategist_py` - **研究策略家**，动态规划
- `05_MMAgent_Core.md.research_strategist_fsm_py` - **FSM 状态机**，流程控制

**专业引擎** (2 项)
- `06_MMAgent_Engine.md.feature_engineer_py` - **特征工程引擎**
- `06_MMAgent_Engine.md.knowledge_retriever_py` - **知识检索引擎**

**叙述生成** (4 项)
- `08_MMAgent_Narrative.md.narrative_weaver_py` - **叙述编织器**
- `08_MMAgent_Narrative.md.academic_tools_py` - **学术写作工具**
- `08_MMAgent_Narrative.md.critique_generator_py` - **批评生成器**
- `08_MMAgent_Narrative.md.abstract_orchestrator_py` - **摘要编排器**

**知识库** (3 项)
- `13_MMAgent_Knowledge.md.knowledge_base_py` - **知识库基类**
- `13_MMAgent_Knowledge.md.domain_knowledge_json` - **领域知识**
- `13_MMAgent_Knowledge.md.history_knowledge_json` - **历史知识**

**HMML 核心** (2 项)
- `14_HMML.md.HMML_md` - **98+ 数学建模模式** (3层层级)
- `14_HMML.md.HMML_json` - **HMML JSON 数据源**

**工具集** (7 项)
- `15_Utilities.md.mathematical_modeling_py` - **数学建模流程** + Context Pruning
- `15_Utilities.md.computational_solving_py` - **计算求解引擎** + Schema Registry
- `15_Utilities.md.problem_analysis_py` - **动态问题分析** + 假设生成
- `15_Utilities.md.data_manager_py` - **单一数据源模式** + 数据快照
- `15_Utilities.md.autofixer_py` - **自愈机制**，错误恢复基础设施
- `15_Utilities.md.embedding_py` - **嵌入相似度**，向量检索
- `15_Utilities.md.auto_evaluation_py` - **自动评估框架**

**评估框架** (1 项)
- `17_MMBench.md.evaluation_dir` - **独立评估框架**

---

### 📁 5-STARS/ (16 项)

**核心模块**
- `02_MMAgent_Main.md` - **系统入口**，4 阶段管道 + Checkpoint + Omni-Survival Kit
- `03_MMAgent_Prompt.md` - **提示词系统**，模块化提示词架构
- `03_MMAgent_Prompt.md.journal_prompts_py` - **后处理分析提示词**
- `03_MMAgent_Prompt.md.variable_contract_prompt_py` - **变量契约提示词**
- `04_MMAgent_Agent.md` - **Agent 协作系统**
- `15_Utilities.md.execution_tracker_py` - **事件追踪器**，Truth Mode 日志
- `15_Utilities.md.latent_reporter_py` - **后处理分析**，法医式尸检

**知识管理**
- `14_HMML.md` - **HMML 知识库**，核心创新
- `13_MMAgent_Knowledge.md` - **知识管理模块**

**数据处理**
- `15_Utilities.md.syntax_fixer_py` - **语法修复器**
- `15_Utilities.md.json_utils_py` - **鲁棒 LLM 输出解析**
- `15_Utilities.md.data_manager_py` - **数据管理架构**
- `15_Utilities.md.column_normalization_py` - **列名规范化**

**系统架构**
- `00_INDEX.md` - **MMAgent/ 核心目录**
- `00_INDEX.md` - **HMML/ 知识库**
- `10_MMAgent_Reporting.md` - **报告生成框架**

---

### 📁 4-STARS/ (16 项)

**引擎组件**
- `05_MMAgent_Core.md` - **核心组件集合**
- `06_MMAgent_Engine.md` - **10 个专业引擎**
- `07_MMAgent_LLM.md` - **统一 LLM 接口**，线程锁防 Error 429
- `08_MMAgent_Narrative.md` - **叙述生成模块**
- `10_MMAgent_Reporting.md` - **报告生成**

**工具模块**
- `15_Utilities.md` - **40+ 工具集合**
- `11_MMAgent_Schema.md` - **Schema 管理**
- `15_Utilities.md.code_guards_py` - **代码守卫**
- `15_Utilities.md.rate_limiter_py` - **速率限制器**
- `15_Utilities.md.schema_registry_py` - **Schema 注册表**
- `15_Utilities.md.variable_contract_py` - **变量契约系统**

**基础设施**
- `00_INDEX.md` - **系统架构导航**
- `00_INDEX.md` - **MMBench/ 数据集**
- `00_INDEX.md` - **evaluation/ 评估目录**
- `00_INDEX.md` - **utils/ 工具集**

---

## 迁移优先级

### 🔴 P0 - 必须迁移 (6 星)

这些是系统的核心创新，不可替代：

1. **HMML 知识库** (14_HMML.md) - 首个 3 层级数学建模知识库
2. **DAG 调度器** (coordinator.py) - 拓扑排序任务调度
3. **提示词模板** (template.py) - 45+ 模块化提示词
4. **SafePlaceholder 模式** (task_solving.py) - 防崩溃设计
5. **Context Pruning 策略** (mathematical_modeling.py) - 智能依赖上下文管理
6. **Schema Registry** (data_manager.py) - 单一数据源模式
7. **嵌入相似度检索** (retrieve_method.py, embedding.py) - 智能知识检索
8. **自愈机制** (autofixer.py) - 错误恢复基础设施

### 🟡 P1 - 强烈推荐 (5 星)

高度复用价值的关键模块：

1. **Actor-Critic 迭代** (problem_analysis.py) - 动态优化模式
2. **Checkpoint 机制** (main.py) - Auto-resume 检查点
3. **Omni-Survival Kit** (main.py) - 死手开关
4. **Truth Mode 日志** (execution_tracker.py) - 完整事件追踪
5. **法医式尸检** (latent_reporter.py) - 后处理分析
6. **变量契约系统** (variable_contract.py) - 多阶段数据一致性
7. **语法修复器** (syntax_fixer.py) - LLM 代码修复

### 🟢 P2 - 可选迁移 (4 星)

值得参考的重要组件：

1. **统一 LLM 接口** (llm.py) - 多模型支持
2. **10 个专业引擎** (engine/) - 特定功能引擎
3. **Schema 管理** (schema_*.py) - 数据模式管理
4. **速率限制器** (rate_limiter.py) - API 并发控制

---

## 统计信息

| 类别 | 6 星 | 5 星 | 4 星 | 合计 |
|------|------|------|------|------|
| 提示词系统 | 1 | 2 | 0 | 3 |
| Agent 系统 | 6 | 1 | 0 | 7 |
| 核心引擎 | 4 | 0 | 2 | 6 |
| 叙述生成 | 4 | 0 | 1 | 5 |
| 知识库 | 5 | 1 | 0 | 6 |
| HMML | 2 | 1 | 0 | 3 |
| 工具集 | 7 | 4 | 7 | 18 |
| 评估 | 1 | 0 | 1 | 2 |
| 其他 | 0 | 7 | 5 | 12 |
| **合计** | **29** | **16** | **16** | **61** |

---

**文档版本**: v1.0
**创建时间**: 2026-01-24
**数据来源**: LLM-MM-Agent 项目完整文档分析
