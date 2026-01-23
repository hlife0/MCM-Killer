# LLM-MM-Agent 文件结构文档

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/00_INDEX.md`
> **重要程度**: ⭐⭐⭐ 核心导航文档
> **扩容影响**: 高 - 文档结构需支持扩展

本文档是 LLM-MM-Agent 项目的总索引，为开发者和研究人员提供完整的文件结构导航。LLM-MM-Agent 是一个发表于 NeurIPS 2025 和 ICML 2025 的学术研究原型系统，专注于使用大语言模型解决数学建模竞赛问题。在"扩容一倍源代码再扩容一倍"的背景下（从 98+ 方法扩展到 400+ 方法，从 4 阶段扩展到 8+ 阶段），本文档提供了可扩展的文档组织架构，支持大规模系统的文档管理。通过本文档，用户可以快速定位和理解项目中各个模块的功能、位置和相互关系，是进入项目代码库的首要入口点。

**迁移价值**：本文档定义了 LLM-MM-Agent 的核心架构导航，在扩容到 400+ 方法和 8+ 阶段时，需要保持文档结构的可扩展性。重点关注 HMML 知识库的扩展架构（从 3 层到 5 层层级）和 DAG 调度的性能优化（支持数百个子任务）。文档结构采用模块化组织，便于动态增减内容。

---

## 完整目录树

### LLM-MM-Agent (clean version/LLM-MM-Agent/)

```
clean version/LLM-MM-Agent/
├── config.yaml                    # 主配置文件
├── requirements.txt               # Python 依赖
├── README.md                      # 项目说明（英文）
├── README_zh.md                   # 项目说明（中文）
├── run.py                         # 运行脚本
├── fix_templates.py               # 模板修复脚本
├── LICENSE                        # 许可证
├── __init__.py                    # 包初始化
│
├── assets/                        # 资源文件
│   ├── logo.png
│   ├── demo.mp4
│   ├── wechat_group.jpg
│   └── step*.png                  # 步骤截图
│
├── doc/                           # 文档
│   └── User_Guide.md
│
├── figs/                          # 图片
│   ├── Overview.png/pdf
│   └── difference.png/pdf
│
├── MMAgent/                       # 核心实现目录 ⭐⭐⭐⭐⭐
│   ├── main.py                    # 【入口】主程序
│   │
│   ├── agent/                     # Agent 模块 ⭐⭐⭐⭐⭐
│   │   ├── base_agent.py          # 所有 Agent 的基类
│   │   ├── coordinator.py         # DAG 任务调度器
│   │   ├── task_solving.py        # TaskSolver Agent
│   │   ├── retrieve_method.py     # 方法检索器
│   │   ├── problem_analysis.py    # 问题分析 Agent
│   │   ├── create_charts.py       # 图表生成管道
│   │   ├── data_description.py    # 数据描述 Agent
│   │   ├── debug_agent.py         # 调试 Agent
│   │   └── problem_decompose.py   # 问题分解
│   │
│   ├── core/                      # 核心组件 ⭐⭐⭐⭐
│   │   ├── abduction_engine.py    # 溯因引擎
│   │   ├── red_team_critic.py     # 红队批评家
│   │   ├── research_strategist.py # 研究策略家
│   │   ├── research_strategist_fsm.py  # 研究策略 FSM
│   │   └── state_manager.py       # 状态管理器
│   │
│   ├── engine/                    # 引擎组件 ⭐⭐⭐⭐
│   │   ├── chart_renderer.py      # 图表渲染引擎
│   │   ├── diagram_engine.py      # 图表引擎
│   │   ├── feature_engineer.py    # 特征工程
│   │   ├── knowledge_retriever.py # 知识检索器
│   │   ├── model_arena.py         # 模型竞技场
│   │   ├── robustness_tester.py   # 鲁棒性测试器
│   │   ├── scientific_renderer.py # 科学渲染器
│   │   ├── sensitivity_analyzer.py # 敏感度分析器
│   │   ├── sensitivity_engine.py  # 敏感度引擎
│   │   └── validation_suite.py    # 验证套件
│   │
│   ├── execution/                 # 执行模块 ⭐⭐⭐
│   │   └── kernel_client.py       # 内核客户端
│   │
│   ├── prompt/                    # 【重要】提示词系统 ⭐⭐⭐⭐⭐
│   │   ├── template.py            # 核心提示词模板（45+ 模板）
│   │   ├── journal_prompts.py     # 日记提示词
│   │   ├── chart_template_prompt.py  # 图表模板提示词
│   │   ├── variable_contract_prompt.py  # 变量契约提示词
│   │   ├── constants.py           # 提示词常量
│   │   ├── decompose_prompt.json  # 分解提示词
│   │   └── __init__.py
│   │
│   ├── prompts/                   # 提示词目录（备用）
│   │
│   ├── narrative/                 # 叙述生成 ⭐⭐⭐
│   │   ├── narrative_weaver.py    # 叙述编织器
│   │   ├── academic_tools.py      # 学术工具
│   │   ├── critique_generator.py  # 批评生成器
│   │   └── abstract_orchestrator.py # 摘要协调器
│   │
│   ├── reporting/                 # 报告生成 ⭐⭐⭐
│   │
│   ├── schema/                    # 模式管理 ⭐⭐⭐
│   │
│   ├── data/                      # 数据模块
│   │   └── data_ingestor.py       # 数据摄取器
│   │
│   ├── knowledge/                 # 知识库
│   │   ├── knowledge_base.py      # 知识库基类
│   │   ├── domain_knowledge.json  # 领域知识
│   │   └── history_knowledge.json # 历史知识
│   │
│   ├── HMML/                      # 【核心】HMML 数学建模知识库 ⭐⭐⭐⭐⭐
│   │   ├── HMML.md                # HMML Markdown 文档
│   │   └── HMML.json              # HMML JSON 数据
│   │
│   ├── llm/                       # LLM 接口 ⭐⭐⭐⭐
│   │   ├── llm.py                 # 统一 LLM 接口
│   │   └── __init__.py
│   │
│   ├── utils/                     # 工具集 ⭐⭐⭐⭐
│   │   ├── mathematical_modeling.py  # 数学建模管道
│   │   ├── computational_solving.py  # 计算求解管道
│   │   ├── solution_reporting.py     # 解决方案报告（Omni-Survival Kit）
│   │   ├── execution_tracker.py       # 事件跟踪（Truth Mode）
│   │   ├── latent_reporter.py        # 潜伏报告器
│   │   ├── data_manager.py            # 数据管理器（CRITICAL FIX #5）
│   │   ├── autofixer.py               # 自愈执行器
│   │   ├── ast_validator.py          # AST 验证器
│   │   ├── embedding.py              # 嵌入相似度检索
│   │   ├── code_guards.py            # P0 工程守卫
│   │   ├── import_guard.py           # 导入守卫
│   │   ├── rate_limiter.py           # 速率限制器
│   │   ├── schema_registry.py        # Schema 注册表
│   │   ├── syntax_fixer.py           # 语法修复器
│   │   ├── path_autofix.py           # 路径自动修复
│   │   ├── data_normalization.py     # 数据规范化
│   │   ├── column_normalization.py  # 列名规范化
│   │   ├── safe_merge.py             # 安全数据合并
│   │   ├── auto_evaluation.py        # 自动质量评估
│   │   ├── json_utils.py             # JSON 工具
│   │   ├── utils.py                  # 通用工具
│   │   ├── logging_config.py         # 日志配置
│   │   ├── failure_handler.py        # 故障处理器
│   │   ├── execution_fsm.py          # 执行 FSM
│   │   ├── fix_pattern_library.py    # 修复模式库
│   │   ├── env_guard.py              # 环境守卫
│   │   ├── data_preprocessing.py     # 数据预处理
│   │   ├── schema_manager.py         # Schema 管理器
│   │   ├── schema_normalization.py  # Schema 规范化
│   │   ├── data_models.py            # 数据模型
│   │   ├── variable_contract.py      # 变量契约
│   │   ├── medal_allocation.py       # 奖牌分配
│   │   ├── chart_config.py           # 图表配置
│   │   ├── chart_templates.py        # 图表模板
│   │   ├── minimal_chart_renderer.py # 最小图表渲染器
│   │   ├── code_guards_enhanced.py   # 增强守卫
│   │   ├── canonical_whitelist.py    # 规范白名单（DEPRECATED）
│   │   ├── convert_format.py         # 格式转换
│   │   ├── problem_analysis.py       # 问题分析
│   │   └── [40+ 其他工具模块]
│   │
│   ├── code_template/             # 代码模板 ⭐⭐⭐
│   │   ├── main.py                # 任务 0 主模板
│   │   ├── main1.py - main10.py   # 任务 1-10 模板
│   │
│   └── output/                    # 输出目录
│       └── MM-Agent/              # 三层输出结构
│           ├── {task}_{timestamp}/
│           │   ├── Report/         # 报告层（PDF、Research Journal）
│           │   ├── Workspace/      # 工作层（code/, json/, charts/, latex/, markdown/）
│           │   └── Memory/         # 记忆层（logs/, checkpoints/, usage/, evaluation/）
│
├── MMBench/                       # 【数据集】MMBench 数据集 ⭐⭐⭐⭐
│   ├── README.md                   # 数据集说明
│   ├── problem/                   # 问题目录（111 题 JSON）
│   │   ├── 2000_A.json - 2025_C.json
│   │   └── [历年 MCM/ICM 问题]
│   ├── dataset/                   # 数据集目录
│   │   ├── 2000_C/ - 2025_C/     # 各年数据文件
│   │   └── [CSV, XLS 等数据]
│   └── evaluation/                # 评估目录 ⭐⭐⭐⭐⭐
│       ├── model.py               # 评估模型
│       ├── prompts.py             # 评估提示词
│       ├── run_evaluation.py      # 单次评估
│       └── run_evaluation_batch.py # 批量评估
│
├── test workplace/                # 【测试】测试基础设施 ⭐⭐⭐
│   ├── README.md                  # 测试说明
│   ├── tests/                    # 测试文件（35+ 测试）
│   │   ├── 01_error_logging_test.py
│   │   ├── 02_evaluation_always_runs.py
│   │   ├── 03_llm_code_correction_robustness.py
│   │   ├── 04_chart_generation_end_to_end.py
│   │   ├── 20_checkpoint_resume.py
│   │   ├── 30_method_recursion.py
│   │   ├── 31_chart_verification.py
│   │   ├── 33_dag_dependency.py
│   │   └── [35+ 测试文件]
│   ├── docs/                     # 测试文档
│   │   └── [每个测试的详细说明]
│   └── ultrathink/              # 深度分析报告
│       └── [bug 修复会话记录]
│
└── scripts/                      # 脚本目录
```

---

### MCM-Killer (MCM-Killer/)

```
MCM-Killer/
├── README.md                      # 项目说明
├── CLAUDE.md                      # 项目指导（主文档）
│
├── architectures/                 # 架构版本管理 ⭐⭐⭐⭐⭐
│   ├── v2-3-0.md                 # v2.3.0 架构
│   ├── v2-4-0/                   # v2.4.0 架构
│   │   ├── architecture.md
│   │   ├── workflow_design.md
│   │   ├── validation_design.md
│   │   └── ...
│   ├── v2-4-1/                   # v2.4.1 架构
│   ├── v2-4-2/                   # v2.4.2 架构
│   ├── v2-5-0/                   # v2.5.0 架构（关键版本）
│   │   ├── 00_CHANGES.md
│   │   ├── 01_README.md
│   │   ├── 02_core.md
│   │   ├── 03_workflow.md
│   │   ├── agents/               # 13+ Agent 规范
│   │   │   ├── reader.md
│   │   │   ├── researcher.md
│   │   │   ├── modeler.md
│   │   │   ├── code_translator.md
│   │   │   ├── model_trainer.md
│   │   │   ├── validator.md
│   │   │   ├── visualizer.md
│   │   │   ├── writer.md
│   │   │   ├── summarizer.md
│   │   │   ├── editor.md
│   │   │   ├── advisor.md
│   │   │   ├── director.md
│   │   │   └── feasibility_checker.md
│   │   └── ...
│   ├── v2-5-1/ - v2-5-7/         # v2.5.x 系列迭代版本
│   ├── v2-6-0/                   # v2.6.0 架构
│   └── v3-0-0/                   # v3.0.0 架构（当前）
│       ├── 00_ARCHITECTURE.md
│       ├── 01_SYSTEM_COMPARISON.md
│       ├── 02_LLM_MM_AGENT_ARCHITECTURE.md
│       ├── 03_MCM_KILLER_ARCHITECTURE.md
│       ├── draft/                # 草稿文档
│       │   ├── LLM-MM-Agent/     # LLM-MM-Agent 详细文档
│       │   │   ├── 00_INDEX.md
│       │   │   ├── 01_Project_Root.md
│       │   │   ├── 02_MMAgent_Core.md
│       │   │   ├── 03_Agents.md
│       │   │   ├── 04_Utilities.md
│       │   │   ├── 05_HMML.md
│       │   │   ├── 06_MMBench.md
│       │   │   └── 07_Test_Infrastructure.md
│       │   └── MCM-Killer/       # MCM-Killer 详细文档
│       └── ...
│
├── workspace/                     # 【工作区】竞赛工作空间
│   └── 2025_C/                   # 2025 C 题工作区
│       ├── CLAUDE.md             # 工作区指导
│       ├── problem/              # 题目文件
│       ├── docs/                 # 文档
│       ├── model/                # 模型设计
│       ├── implementation/       # 实现代码
│       │   ├── .venv/            # 虚拟环境
│       │   └── [code, data, logs]
│       └── paper/                # 论文输出
│
├── experiments/                  # 实验记录
│   ├── trail-0102/
│   ├── trail-Istanbul/
│   └── [实验复盘点]
│
├── problems and results/         # 历年题目和结果
│   ├── 2020/ - 2025/           # 2020-2025 年
│   └── [PDF 题目和结果文件]
│
├── student paper/                # 学生论文
│   ├── 2020/ - 2024/
│   └── [历年优秀论文 PDF]
│
└── LaTeX__Template_for_MCM_ICM/  # LaTeX 模板
    ├── mcmthesis.cls            # 文档类
    ├── mcmthesis-demo.tex       # 示例
    ├── code/                    # 代码示例
    └── figures/                 # 图片资源
```

---

## 文档导航

### LLM-MM-Agent 文档系列

| 文档 | 绝对路径 | 描述 | 重要程度 |
|------|----------|------|----------|
| [本文档](00_INDEX.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/00_INDEX.md` | **总索引**：完整目录树和导航 | ⭐⭐⭐ |
| [01_Project_Root.md](01_Project_Root.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/01_Project_Root.md` | 项目根目录文件（config.yaml, README, requirements.txt, run.py） | ⭐⭐ |
| [02_MMAgent_Core.md](02_MMAgent_Core.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/02_MMAgent_Core.md` | **MMAgent 核心模块**：main.py, prompt/, core/, engine/, narrative/, reporting/, schema/ 等 | ⭐⭐⭐⭐⭐ |
| [03_Agents.md](03_Agents.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/03_Agents.md` | **Agent 模块**：所有 Agent 的职责、输入输出、工作流程 | ⭐⭐⭐⭐⭐ |
| [04_Utilities.md](04_Utilities.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/04_Utilities.md` | **工具集**：utils/ 下 40+ 工具模块完整文档 | ⭐⭐⭐⭐ |
| [05_HMML.md](05_HMML.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/05_HMML.md` | **HMML 知识库**：98+ 数学建模模式的层级化知识 | ⭐⭐⭐⭐⭐ |
| [06_MMBench.md](06_MMBench.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/06_MMBench.md` | **MMBench 数据集**：历年竞赛题目、数据文件、评估框架 | ⭐⭐⭐⭐ |
| [07_Test_Infrastructure.md](07_Test_Infrastructure.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/07_Test_Infrastructure.md` | **测试基础设施**：35+ 自动化测试和文档 | ⭐⭐ |

### 关键发现

#### 之前遗漏的重要目录

1. **MMAgent/prompt/** ⭐⭐⭐⭐⭐
   - `template.py`：核心提示词模板（45+ 模板）
   - `journal_prompts.py`：日记生成提示词
   - `chart_template_prompt.py`：图表模板提示词
   - `variable_contract_prompt.py`：变量契约提示词
   - 这是系统的"大脑"，定义了所有 LLM 交互的提示词

2. **MMAgent/core/** ⭐⭐⭐⭐
   - `abduction_engine.py`：溯源引擎
   - `red_team_critic.py`：红队批评家
   - `research_strategist.py`：研究策略家
   - `research_strategist_fsm.py`：研究策略 FSM
   - `state_manager.py`：状态管理器

3. **MMAgent/engine/** ⭐⭐⭐⭐
   - `chart_renderer.py`：图表渲染引擎
   - `diagram_engine.py`：图引擎
   - `feature_engineer.py`：特征工程
   - `knowledge_retriever.py`：知识检索器
   - `model_arena.py`：模型竞技场
   - `robustness_tester.py`：鲁棒性测试器
   - `scientific_renderer.py`：科学渲染器
   - `sensitivity_analyzer.py`：敏感度分析器
   - `sensitivity_engine.py`：敏感度引擎
   - `validation_suite.py`：验证套件

4. **MMAgent/execution/** ⭐⭐⭐
   - `kernel_client.py`：内核客户端

5. **MMAgent/narrative/** ⭐⭐⭐
   - `narrative_weaver.py`：叙述编织器
   - `academic_tools.py`：学术工具
   - `critique_generator.py`：批评生成器
   - `abstract_orchestrator.py`：摘要协调器

6. **MMAgent/reporting/** ⭐⭐⭐
   - 报告生成模块

7. **MMAgent/schema/** ⭐⭐⭐
   - Schema 管理

---

## 核心特性

### 4 阶段管道

1. **Problem Analysis** → 问题分解和子任务生成
2. **Mathematical Modeling** → HMML 方法检索和模型构建
3. **Computational Solving** → 代码生成和执行
4. **Solution Reporting** → 报告生成（JSON/Markdown/LaTeX）

### HMML 知识库

- **3 层层级**：Domain → Subdomain → Method Node
- **98+ 建模模式**：涵盖所有主要数学建模方法
- **嵌入相似度检索**：智能方法匹配
- **扩容目标**：5 层层级，400+ 模式

### DAG 任务调度

- 基于依赖关系的子任务编排
- 拓扑排序确定执行顺序
- 循环依赖检测
- **扩容目标**：支持数百个子任务

### 自动恢复

- 检查点机制（Stage 1 + 每个任务后自动保存）
- 透明恢复（重启自动继续）

### Omni-Survival Kit

- 死手开关系统（atexit + finally 双重触发）
- 确保即使系统崩溃也能生成 PDF

---

**文档版本**: v2.0 (完整版)
**最后更新**: 2026-01-24
**总文件数**: LLM-MM-Agent (200+ 文件), MCM-Killer (1000+ 文件)
