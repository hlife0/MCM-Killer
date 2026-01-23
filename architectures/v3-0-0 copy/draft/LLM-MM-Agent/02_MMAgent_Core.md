# LLM-MM-Agent: MMAgent 核心模块

> Path: `clean version/LLM-MM-Agent/MMAgent/`

---

## 主入口

### `main.py`
主程序入口，负责命令行参数解析（--key, --task, --model_name等）、API密钥管理、输出目录初始化、阶段编排（4阶段管道的协调）、检查点与恢复逻辑（自动保存和恢复管道状态）。是整个系统的指挥中心，处理所有高层逻辑。

---

## Core 组件 (`core/`)

### `__init__.py`
包初始化文件。

### `abduction_engine.py`
溯因推理引擎，实现从观察到假设的逆向推理过程。用于生成可能解释、评估假设合理性、选择最佳解释。

### `red_team_critic.py`
红队批评家，模拟对抗性攻击来测试系统鲁棒性。通过寻找弱点、生成反例、压力测试来提升系统质量。

### `research_strategist.py`
研究策略规划器，制定研究计划和方法选择策略。分析问题特点、推荐合适方法、规划研究路径。

### `research_strategist_fsm.py`
研究策略状态机，用有限状态机实现研究策略的动态调整和转换。根据当前状态和反馈决定下一步行动。

### `state_manager.py`
状态管理系统，管理Agent的内部状态、状态转换规则、状态持久化。确保状态一致性和可恢复性。

---

## Data 处理 (`data/`)

### `__init__.py`
包初始化文件。

### `data_ingestor.py`
数据摄取管道，负责数据加载、格式转换、清洗、验证。处理各种数据格式（CSV, Excel, JSON），进行基本的数据质量检查。

---

## Engine 组件 (`engine/`)

### `__init__.py`
包初始化文件。

### `chart_renderer.py`
图表渲染引擎，将数据转换为可视化图表。支持matplotlib、seaborn、plotly等库，处理图表样式、布局、保存。

### `diagram_engine.py`
图表生成引擎，创建流程图、架构图、系统图等。用于生成技术图表和模型结构图。

### `feature_engineer.py`
特征工程工具，提供特征提取、特征选择、特征变换、特征组合等功能。支持常见的特征工程技术。

### `knowledge_retriever.py`
知识检索系统，从知识库中检索相关信息、方法、案例。基于相似度匹配和关键词检索。

### `model_arena.py`
模型竞技场，对比不同模型/方法的性能。进行基准测试、性能评估、优劣分析。

### `robustness_tester.py`
鲁棒性测试框架，测试模型或系统在各种条件下的稳定性。包括噪声测试、边界测试、敏感性测试。

### `scientific_renderer.py`
科学可视化渲染器，生成符合学术出版标准的图表。遵循学术规范，处理高质量图形输出。

### `sensitivity_analyzer.py`
敏感度分析引擎，分析参数变化对结果的影响程度。识别关键参数、量化敏感性、生成敏感度报告。

### `sensitivity_engine.py`
敏感度分析实现，执行具体的敏感度计算。提供单因素、多因素敏感度分析方法。

### `validation_suite.py`
综合验证套件，集成多种验证方法。包括交叉验证、统计检验、专家验证等。

---

## Execution 环境 (`execution/`)

### `__init__.py`
包初始化文件。

### `kernel_client.py`
内核客户端，代码执行环境的客户端接口。与Jupyter内核或Python进程通信，执行生成的代码并返回结果。

---

## Knowledge 知识库 (`knowledge/`)

### `__init__.py`
包初始化文件。

### `domain_knowledge.json`
领域知识库，存储特定领域的专业知识、经验规则、最佳实践。按领域组织结构化知识。

### `history_knowledge.json`
历史知识库，存储历史问题和解决方案的模式、成功案例、常见陷阱。用于类比推理和经验借鉴。

### `knowledge_base.py`
知识库管理系统，提供知识的存储、检索、更新、验证功能。统一管理多个知识源。

---

## LLM 接口 (`llm/`)

### `__init__.py`
包初始化文件。

### `llm.py`
统一LLM接口，支持OpenAI、DeepSeek、GLM、Qwen等多种模型。提供统一的调用接口、错误处理、重试机制、线程锁防止API限流。是多模型兼容的核心适配层。

---

## Narrative 生成 (`narrative/`)

### `__init__.py`
包初始化文件。

### `abstract_orchestrator.py`
抽象叙述编排器，组织高层次叙述结构和逻辑流。确保叙述的连贯性和逻辑性。

### `academic_tools.py`
学术写作工具，提供学术规范、引用格式、写作风格指南。生成符合学术标准的文本。

### `critique_generator.py`
批评生成器，对生成内容进行批判性评估。识别问题、提出改进建议、评估质量。

### `narrative_weaver.py`
叙述编织器，将各部分内容整合成连贯的叙述。连接段落、过渡句子、统一风格。

---

## Output 输出 (`output/`)

### 目录结构
```
output/
└── MM-Agent/
    └── {task}_{timestamp}/
        ├── Report/              # 最终PDF报告
        ├── Workspace/           # 工作过程文件
        │   ├── charts/          # 可视化图表
        │   ├── code/            # 生成的Python代码
        │   ├── json/            # 结构化JSON数据
        │   ├── latex/           # LaTeX源文件
        │   └── markdown/        # Markdown报告
        └── Memory/              # 系统记忆和诊断
            ├── checkpoints/     # 管道状态检查点
            ├── evaluation/      # 质量评估报告
            ├── logs/            # 执行日志
            └── usage/           # API使用统计
```

输出目录采用三层结构组织：Report层存放最终交付物，Workspace层记录工作过程，Memory层保存系统诊断信息。支持自动恢复和事后分析。

---

## Prompt 模板 (`prompt/`)

### `__init__.py`
包初始化文件。

### `chart_template_prompt.py`
图表生成提示词模板，定义如何描述图表需求。包含图表类型、数据映射、样式要求的提示模板。

### `constants.py`
提示词常量和共享变量，定义常用的提示词片段、变量名、格式规范。确保提示词的一致性。

### `decompose_prompt.json`
问题分解提示词JSON格式，定义如何将复杂问题分解为子任务。包含分解规则、子任务描述模板。

### `journal_prompts.py`
研究日志生成提示词，定义如何生成研究过程的日志记录。包含日志结构、内容要求、风格指南。

### `template.py`
集中式提示词模板管理系统，统一管理所有提示词模板。提供模板加载、变量替换、格式化功能。

---

## Prompt 集合 (`prompts/`)

### `abstract_prompts.py`
抽象推理提示词，用于生成抽象层面的分析和推理。

### `arena_prompts.py`
模型对比竞技场提示词，用于模型间的对比评估和优劣分析。

### `decoupled_prompts.py`
解耦阶段提示词，将复杂任务分解为独立阶段的提示词。

### `strategist_prompts.py`
研究策略提示词，用于制定研究计划和策略选择。

---

## Reporting 系统 (`reporting/`)

### `__init__.py`
包初始化文件。

### `latex_compiler.py`
LaTeX编译引擎，将.tex文件编译为PDF。处理编译错误、依赖管理、多次编译。

### `multi_format_publisher.py`
多格式输出发布器，同时生成JSON、Markdown、LaTeX、PDF等多种格式。确保内容一致性。

### `report_manifest.py`
报告清单和元数据管理，记录报告的结构、文件清单、版本信息。用于报告管理和追踪。

---

## Schema 定义 (`schema/`)

### `chart_schema.py`
图表数据模式定义，规定图表数据的结构和格式。定义数据字段、类型约束、验证规则。

### `scientific_chart_schema.py`
科学图表规范，定义符合学术标准的图表格式。包含尺寸、分辨率、字体、颜色等规范。

---

## Code 模板 (`code_template/`)

### `main.py`
解决方案的基础代码模板，提供标准的问题求解代码框架。包含导入、数据加载、模型定义、结果输出等基本结构。

### `main1.py` ~ `main10.py`
编号的模板文件，提供不同的解决方案方法或代码模式。支持多种建模方法的基本框架。

---

**文档版本**: v1.0
