# MCM-Killer: Workspace 工作目录

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/02_Workspace.md`
> **重要程度**: ⭐⭐⭐ 活跃工作空间
> **扩容影响**: **极高** - 18 阶段 → 72 阶段

本目录是 MCM-Killer 系统的活跃开发空间，包含当前竞赛（2025_C）的完整工作环境。所有 Agent 执行、数据存储、结果输出都在此目录进行。在"扩容一倍源代码再扩容一倍"的背景下（从 18 阶段扩容到 72 阶段，从 13 Agent 扩容到 52 Agent），workspace 的组织结构需要支持大规模的工作流管理和 Agent 协作。

**迁移价值**：workspace/2025_C/ 是系统运行的核心区域。在扩容时需要：1）重新组织目录结构以支持 72 阶段；2）建立 Agent 注册和管理机制；3）强化数据权威层级（从 3 层到 5 层）；4）建立版本管理系统（VERSION_MANIFEST.json 需要支持更多阶段和 Agent）。这是扩容实施的直接战场。

---

## 核心文件

### `CLAUDE.md` ⭐⭐⭐
**Claude Code 指导文档**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/CLAUDE.md`。MCM-Killer 系统的操作手册。定义 18 阶段工作流程（Phase 0 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5 → 5.5 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.5 → 10）、13+ 专业 Agent 职责（Reader, Researcher, Modeler, Feasibility Checker, Data Engineer, Code Translator, Model Trainer, Validator, Visualizer, Writer, Editor, Advisor, Time Validator, Summarizer）、7 个验证门控规则、三层数据权威层级（CSV Level 1 > Agent Reports Level 2 > Paper Level 3）。

**迁移价值**：这是系统使用的基础文档。在扩容到 72 阶段和 52 Agent 时，CLAUDE.md 需要全面重写。需要定义新的阶段序列（可能到 Phase 40+）、新的 Agent 职责和协作关系、扩展的验证门控（可能到 28+ 个）、更精细的数据权威层级（5 层）。这是扩容设计的核心文档。

### `.mcp.json` ⭐⭐
**MCP 配置文件**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.mcp.json`。定义模型上下文协议的参数和设置。

**迁移价值**：在扩容时需要支持更多的上下文窗口和更复杂的配置。

### `.claude/settings.local.json` ⭐⭐
**Claude Code 本地配置**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/settings.local.json`。

**迁移价值**：需要支持更多的 Agent 配置和设置。

---

## 问题文件

### `2025_MCM_Problem_C.pdf` ⭐⭐⭐
**2025 年 MCM 问题 C 的 PDF 文件**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/2025_MCM_Problem_C.pdf`。包含完整的问题陈述、背景信息、具体要求、数据描述。

**迁移价值**：不需要修改，但需要支持更多年份和类型的题目。

### `2025_Problem_C_Data.zip` ⭐⭐⭐
**问题 C 数据压缩包**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/2025_Problem_C_Data.zip`。

**迁移价值**：需要支持更大规模和更多类型的数据集。

---

## 数据文件 (`2025_Problem_C_Data/`)

### `summerOly_*.csv` ⭐⭐⭐
**奥运会数据文件**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/2025_Problem_C_Data/`。包含主办城市、运动员、奖牌统计、比赛项目等数据。

**迁移价值**：需要支持更多数据源和更复杂的数据结构。

### `data_dictionary.csv` ⭐⭐⭐
**数据字典**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/2025_Problem_C_Data/data_dictionary.csv`。

**迁移价值**：需要支持更复杂的数据字典结构（如 5 层权威层级）。

---

## Agent 定义 (`.claude/agents/`)

### 13+ 专业 Agent 定义 ⭐⭐⭐
**Agent 定义文件**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/.claude/agents/`。包含 advisor.md, code_translator.md, data_engineer.md, editor.md, feasibility_checker.md, model_trainer.md, modeler.md, reader.md, researcher.md, summarizer.md, time_validator.md, validator.md, visualizer.md, writer.md 等。

**迁移价值**：这是扩容的核心。当前是 13+ Agent，目标是 52+ Agent。需要：1）建立 Agent 模板和标准；2）定义 Agent 接口和协作协议；3）建立 Agent 工厂模式；4）支持动态 Agent 注册。这是扩容中技术难度第二大的部分（仅次于 HMML）。

---

## 输出目录 (`output/`)

### `VERSION_MANIFEST.json` ⭐⭐⭐
**版本清单**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/output/VERSION_MANIFEST.json`。单一数据来源（Single Source of Truth）。

**迁移价值**：在扩容到 72 阶段和 52 Agent 时，VERSION_MANIFEST.json 需要支持更复杂的版本信息。需要记录更多的阶段状态、更多的 Agent 签名、更复杂的依赖关系、更精细的校验和（支持增量更新）。

### `docs/` ⭐⭐⭐
**文档目录**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/output/docs/`。包含 consultations/, validations/, reports/。

**迁移价值**：需要支持更多的咨询记录、更多的验证报告、更多的阶段报告。需要建立文档自动生成和索引系统。

### `model/` ⭐⭐⭐
**模型设计目录**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/output/model/`。

**迁移价值**：需要支持更多的模型设计方案和更复杂的模型管理。

### `implementation/` ⭐⭐⭐
**实现目录**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/output/implementation/`。包含 code/, data/, logs/, models/, .venv/。

**迁移价值**：需要支持更多的代码文件、更大的数据集、更复杂的日志、更多的模型文件。

### `paper/` ⭐⭐⭐
**论文目录**，绝对路径：`D:/migration/MCM-Killer/workspace/2025_C/output/paper/`。包含 paper.tex, figures/, summary.md, paper.pdf。

**迁移价值**：需要支持更多章节的论文、更多的图表、更复杂的引用管理。

---

## Workspace 扩容计划

### 阶段 1：目录结构重组（1 周）
- 重组 output/ 目录以支持 72 阶段
- 建立 Agent 注册目录（.claude/agents/）
- 建立阶段模板目录（templates/phases/）

### 阶段 2：CLAUDE.md 重写（2 周）
- 定义新的 72 阶段工作流
- 定义新的 52+ Agent 规范
- 定义新的 28+ 验证门控

### 阶段 3：VERSION_MANIFEST 扩展（1 周）
- 支持更多的阶段和 Agent
- 支持更复杂的依赖关系
- 支持增量更新和版本控制

### 阶段 4：文档自动化（2 周）
- 建立咨询记录自动生成
- 建立验证报告自动生成
- 建立阶段报告自动生成

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
