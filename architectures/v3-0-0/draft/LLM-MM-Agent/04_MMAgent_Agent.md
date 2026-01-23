# LLM-MM-Agent: Agent 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/03_Agents.md`
> **重要程度**: ⭐⭐⭐⭐⭐ 智能代理协作核心
> **迁移价值**: **极高** - DAG 调度和任务协调是核心机制

本目录包含 LLM-MM-Agent 系统的所有 Agent 定义和实现。Agent 是系统的智能执行单元，每个 Agent 负责特定类型的任务（问题分析、方法检索、任务求解、图表生成等）。通过 Agent 之间的协作，系统实现了从问题输入到解决方案输出的完整自动化流程。所有 Agent 都继承自 base_agent.py 基类，确保系统的一致性和可扩展性。

**迁移价值**：Agent 模块包含了 LLM-MM-Agent 的两个核心设计：1）Agent 基类（base_agent.py）定义了 Agent 的标准接口和行为模式；2）DAG 任务调度器（coordinator.py）管理子任务之间的依赖关系和执行顺序。这两个设计是系统协同工作的基础。在迁移时，Agent 基类的思想（统一的接口、状态管理、错误处理）值得借鉴，DAG 调度机制更是处理复杂任务依赖的核心算法。task_solving.py 展示了如何编排完整的任务求解流程（分析→建模→编码→执行），这个流程模板可以应用到其他问题求解系统。

---

### `base_agent.py` ⭐⭐
**所有 Agent 的基类**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/base_agent.py`。定义 Agent 的通用接口和行为模式。提供核心功能包括：统一的 LLM 调用接口（与 llm.py 集成）、提示词管理系统（加载、填充、格式化）、输出解析器（提取结构化结果）、错误处理和重试机制（指数退避）。定义了 Agent 的标准生命周期（初始化→思考→行动→输出）、状态管理（记忆累积、上下文维护）、结果返回格式。

**迁移价值**：base_agent.py 的设计展示了如何定义一个可扩展的 Agent 基类。统一的接口、标准化的生命周期管理、完善的错误处理机制，这些设计模式使得系统可以轻松添加新的 Agent 而不会破坏现有代码。在迁移时，这种基类设计思想非常有价值，可以应用到任何需要管理多个智能体的系统。

---

### `coordinator.py` ⭐⭐⭐⭐⭐⭐
**DAG 任务调度器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/coordinator.py`。管理子任务之间的复杂依赖关系和执行顺序。核心功能包括：构建依赖图（DAG：有向无环图）、拓扑排序确定执行顺序、识别可并行执行的任务、检测循环依赖并报错、处理任务失败和重试。

**迁移价值**：coordinator.py 是 LLM-MM-Agent 中最核心的算法模块之一。它展示了如何使用图论算法（拓扑排序）来解决实际问题（任务调度）。这个模块的实现思想和算法可以直接应用到其他需要任务调度的场景。在迁移时，如果新的系统也面临复杂任务依赖的管理问题，coordinator.py 的实现是非常好的参考。

---

### `task_solving.py` ⭐⭐⭐⭐⭐⭐
**TaskSolver Agent**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/task_solving.py`。编排单个子任务的完整求解流程：分析→建模→编码→执行。管理子任务的四个阶段：问题理解（明确任务目标和输入输出）、数学建模（选择方法、定义变量、构建模型）、代码生成（编写求解代码）、结果验证（检查正确性和合理性）。

**迁移价值**：task_solving.py 展示了如何将一个复杂任务分解为多个阶段，然后按顺序执行每个阶段。这种分阶段的任务处理思想非常通用，可以应用到各种问题求解系统。SafePlaceholder 模式（防止模板格式化崩溃）也是一个实用的设计技巧。

---

### `retrieve_method.py` ⭐⭐⭐⭐⭐⭐
**方法检索器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/retrieve_method.py`。从 HMML 知识库中检索合适的数学建模方法。基于嵌入相似度匹配，支持问题感知检索（根据问题类型）和解决方案感知检索（根据已有方案）。

**迁移价值**：retrieve_method.py 展示了如何实现基于嵌入相似度的知识检索。这个设计思想在迁移时非常有价值，特别是当系统需要从大型知识库中智能检索相关内容时。嵌入相似度匹配比关键词匹配更智能，可以处理语义相似的查询。

---

### `problem_analysis.py` ⭐⭐⭐⭐⭐⭐
**问题分析 Agent**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/problem_analysis.py`。将复杂问题分解为可管理的子任务。采用 actor-critic 模式：Actor 生成初步分解，Critic 评估并反馈，Actor 迭代优化（默认 3 轮）。

**迁移价值**：problem_analysis.py 的 actor-critic 迭代优化模式是一个非常实用的设计，可以用于任何需要逐步改进结果的场景。这种"生成→评估→改进"的循环是提升质量的有效方法。

---

### `create_charts.py` ⭐⭐
**图表生成管道**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/create_charts.py`。将自然语言图表描述转换为可视化图像。

**迁移价值**：图表生成功能在迁移时可以由 Claude Code 处理，不需要特别关注。

---

### `data_description.py` ⭐⭐⭐⭐⭐⭐
**数据描述 Agent**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/data_description.py`。处理数据描述和预处理任务。

**迁移价值**：数据分析功能在迁移时可以由 Claude Code 处理。

---

### `debug_agent.py` ⭐⭐
**调试 Agent**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/debug_agent.py`。诊断管道问题、追踪错误来源。

**迁移价值**：调试功能在迁移时可以由开发工具处理。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
