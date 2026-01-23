# MCM-Killer: 项目根目录

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/01_Project_Root.md`
> **重要程度**: ⭐⭐⭐ 项目组织中心
> **扩容影响**: 中 - 目录结构需扩展

MCM-Killer 项目根目录包含系统的顶层组织结构，包括版本控制、架构文档、工作空间、LaTeX 模板等核心组成部分。作为项目的顶层目录，它定义了系统的整体组织方式和模块划分。在"扩容一倍源代码再扩容一倍"的背景下，项目根目录的组织结构需要支持更多的子目录（如新增的 workspace 目录）、更复杂的版本管理（支持更多版本分支）、更完善的文档结构（支持更多架构版本）。

**迁移价值**：项目根目录的组织结构需要在扩容时进行调整。当前有 architectures/ 和 workspace/ 两个主要目录，在扩容时可能需要添加新的目录（如 templates/ 用于 Agent 和阶段模板，tools/ 用于自动化工具）。版本管理需要支持更多的分支和标签。README.md 需要更新以反映扩容后的系统架构和使用方法。

---

### `README.md` ⭐⭐⭐
**项目主文档**，绝对路径：`D:/migration/MCM-Killer/README.md`。介绍 MCM-Killer 系统的完整架构、核心功能、使用方法。包含系统概述（18 阶段工作流、13+ Agent）、快速开始指南、核心规则说明、数据权威层级、与 LLM-MM-Agent 的区别对比。

**迁移价值**：在扩容后需要大幅更新 README。当前描述的是 18 阶段和 13 Agent，扩容后需要更新为 72 阶段和 52 Agent 的系统架构。需要添加新的配置说明、新的使用指南、新的架构图。README 是用户理解系统的第一入口，必须准确反映扩容后的系统状态。

### `.gitignore` ⭐⭐
**Git 忽略文件配置**，绝对路径：`D:/migration/MCM-Killer/.gitignore`。指定不需要版本控制的文件和目录。

**迁移价值**：在扩容时需要添加新的忽略规则（如 templates/, tools/, cache/ 等新目录）。

### `architectures/` ⭐⭐⭐
**架构版本历史目录**，绝对路径：`D:/migration/MCM-Killer/architectures/`。记录系统架构的演进历史。

**迁移价值**：这是理解系统设计演进的 key。在扩容时需要添加新的架构版本（如 v3-0-0 是扩容设计的起点）。需要记录扩容过程中的设计决策、架构变更、版本对比。

### `workspace/` ⭐⭐⭐
**工作空间目录**，绝对路径：`D:/migration/MCM-Killer/workspace/`。包含各个竞赛年份的工作目录。

**迁移价值**：在扩容时需要支持更多的 workspace（如 2025_C/, 2026_A/, 2026_B/ 等）。每个 workspace 需要支持更多的阶段和更多的 Agent。

### `LaTeX__Template_for_MCM_ICM/` ⭐⭐⭐
**MCM/ICM 论文 LaTeX 模板目录**，绝对路径：`D:/migration/MCM-Killer/LaTeX__Template_for_MCM_ICM/`。

**迁移价值**：在扩容时需要支持更多的论文章节（从 6 章到 20+ 章）、更复杂的引用管理、更自动化的图表生成。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
