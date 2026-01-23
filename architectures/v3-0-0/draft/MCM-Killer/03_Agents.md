# MCM-Killer: Agent 定义

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/03_Agents.md`
> **重要程度**: ⭐⭐⭐ 智能代理协作核心
> **扩容影响**: **极高** - 13 Agent → 52 Agent

本目录包含 MCM-Killer 系统的 13+ 专业 Agent 定义文档。每个 Agent 都有明确的职责、输入输出、工作流程和协作关系。这些 Agent 通过精心设计的协作流程，共同完成 18 阶段工作流。在"扩容一倍源代码再扩容一倍"的背景下（从 13 Agent 扩容到 52 Agent），Agent 的标准化、模块化、可组合性成为关键设计挑战。

**迁移价值**：Agent 协作机制是扩容的核心。从 13 Agent 扩容到 52 Agent 需要：1）建立 Agent 模板和标准接口；2）定义 Agent 协作协议（输入输出格式、通信机制）；3）建立 Agent 工厂模式（动态创建和注册 Agent）；4）建立 Agent 组合机制（支持多个 Agent 协作完成复杂任务）。这是扩容中技术难度第二大的部分，仅次于 HMML 扩展。

---

### `advisor.md` ⭐⭐⭐
**顾问 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/advisor.md`。提供战略建议和方向指导。在关键决策点（如方法选择、模型设计、论文结构、验证门控）提供专业建议，基于领域知识和历史经验帮助团队做出最佳决策。

**迁移价值**：在扩容到 52 Agent 时，Advisor 的角色更加重要。需要支持更复杂的决策树、更多的知识库（支持 400+ 方法的 HMML）、更智能的建议算法。可能需要拆分为多个专门 Advisor（如 ModelAdvisor, WorkflowAdvisor, ValidationAdvisor）。

### `reader.md` ⭐⭐⭐
**阅读 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/reader.md`。负责问题理解和数据读取。

**迁移价值**：在扩容时需要支持更多类型的数据输入（如图像、视频、音频）、更复杂的数据格式（如大规模图数据库）、更智能的问题理解（支持多语言、跨领域）。

### `researcher.md` ⭐⭐⭐
**研究 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/researcher.md`。负责文献调研和方法研究。

**迁移价值**：在扩容时需要支持更大的文献库（从 50+ 篇到 500+ 篇）、更智能的文献检索（支持语义搜索）、更自动化的综述生成。

### `modeler.md` ⭐⭐⭐
**建模 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/modeler.md`。负责数学模型的构建与设计。

**迁移价值**：在扩容时需要支持更多的建模方法（从 98+ 到 400+）、更复杂的模型组合、更自动化的模型选择算法。

### `validator.md` ⭐⭐⭐
**验证 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/validator.md`。负责结果验证和质量检查。

**迁移价值**：在扩容时需要支持更多的验证维度（从 3 个到 10+ 个）、更自动化的验证规则生成、更智能的异常检测。

### `writer.md` ⭐⭐⭐
**写作 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/writer.md`。负责论文撰写和报告生成。

**迁移价值**：在扩容时需要支持更多章节的论文（从 6 章到 20+ 章）、更复杂的引用管理、更自动化的图表生成。

### `editor.md` ⭐⭐⭐
**编辑 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/editor.md`。负责论文的语言优化和格式修正。

**迁移价值**：在扩容时需要支持更多的语言风格（学术、技术、科普）、更复杂的格式规范、更智能的语法和拼写检查。

### `feasibility_checker.md` ⭐⭐⭐
**可行性检查 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/feasibility_checker.md`。评估方案的可行性。

**迁移价值**：在扩容时需要支持更多的评估维度（技术、资源、时间、风险）、更智能的风险预测、更自动化的缓解策略生成。

### `time_validator.md` ⭐⭐⭐
**时间验证 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/time_validator.md`。控制进度和时间管理。

**迁移价值**：在扩容时需要支持更复杂的进度管理（72 个阶段）、更智能的时间预测、更自动化的进度调整。

### `data_engineer.md` ⭐⭐
**数据工程师 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/data_engineer.md`。

**迁移价值**：重要程度较低，Claude Code 可以处理大部分数据处理任务。

### `code_translator.md` ⭐⭐
**代码翻译 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/code_translator.md`。

**迁移价值**：重要程度较低，Claude Code 自带强大的代码生成能力。

### `model_trainer.md` ⭐⭐
**模型训练 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/model_trainer.md`。

**迁移价值**：重要程度较低，Claude Code 可以直接训练模型。

### `visualizer.md` ⭐⭐
**可视化 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/visualizer.md`。

**迁移价值**：重要程度较低，Claude Code 可以生成图表。

### `summarizer.md` ⭐⭐
**总结 Agent**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/summarizer.md`。

**迁移价值**：在扩容时需要支持更长的文档总结、更智能的关键信息提取。

---

## Agent 协作流程

```
Phase 0: Reader → Researcher → [Validator 0.5]
                                    ↓
Phase 1: Researcher → Modeler → [Validator 1.5] → Feasibility Checker → [Validator 2]
                                                          ↓
Phase 3: Data Engineer → Code Translator → Model Trainer → [Validator 4.5]
                                                          ↓
Phase 5-6: Validator → Visualizer → [Validator 6.5]
                                                          ↓
Phase 7-8: Writer → Editor → [Validator 9]
                                    ↑
Advisor (贯穿全过程，在关键决策点提供建议)
Time Validator (进度监控，在所有阶段检查时间)
Summarizer (关键节点总结，生成阶段摘要)
```

**迁移价值**：在扩容到 52 Agent 和 72 阶段时，这个协作流程会变得更加复杂。需要支持更多的 Agent 类型、更复杂的依赖关系、更动态的流程调整。

---

## Agent 扩容计划

### 阶段 1：Agent 标准化（2 周）
- 建立 Agent 模板（标准接口、输入输出格式）
- 定义 Agent 协作协议（通信机制、数据格式）
- 建立 Agent 注册中心

### 阶段 2：第一次扩容（3-4 周）
- 从 13 Agent 扩展到 26 Agent（新增 13 个）
- 添加新的专业 Agent（如图像处理 Agent、NLP Agent）
- 建立Agent 组合机制

### 阶段 3：Agent 工厂（2-3 周）
- 建立 Agent 工厂模式
- 支持动态 Agent 创建和注册
- 建立 Agent 配置系统

### 阶段 4：第二次扩容（4-6 周）
- 从 26 Agent 扩展到 52 Agent（新增 26 个）
- 添加更多专业 Agent
- 完善 Agent 生态系统

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
