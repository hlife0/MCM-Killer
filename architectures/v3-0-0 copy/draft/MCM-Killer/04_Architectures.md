# MCM-Killer: Architectures 架构历史

> Path: `MCM-Killer/architectures/`

---

## 版本历史概览

| 版本 | 描述 | 状态 |
|------|------|------|
| v2-3-0 | 早期版本 | 已归档 |
| v2-4-0 | 工作流设计引入 | 已归档 |
| v2-4-1 | Agent规范化 | 已归档 |
| v2-4-2 | 迭代优化 | 已归档 |
| v2-5-0 | 完整18阶段工作流 | 稳定版 |
| v2-5-1 | 精简版 | 已归档 |
| v2-5-7 | 当前稳定版 | **推荐使用** |
| v3-0-0 | 开发中 | 实验性 |

---

## v2-3-0

### `v2-3-0.md`
早期架构文档，记录系统的初始设计和基本概念。

---

## v2-4-0

### 架构文件
- **`architecture.md`** - 系统架构设计，定义基本的模块划分和接口
- **`workflow_design.md`** - 工作流程设计，引入阶段化工作流的概念
- **`validation_design.md`** - 验证机制设计，定义质量检查方法
- **`consultation_design.md`** - 咨询机制设计，定义与Advisor的交互流程
- **`report_design.md`** - 报告设计，定义输出报告的格式和内容
- **`methodology.md`** - 方法学文档，记录方法论基础
- **`retrospective.md`** - 版本回顾总结

---

## v2-4-1

### 架构文件
- **`architecture.md`** - 系统架构（更新版）
- **`methodology.md`** - 方法学（更新版）
- **`retrospective.md`** - 版本回顾总结

### `agents_backup/`
Agent定义备份，包含13个Agent的完整定义文档：advisor, code_translator, data_engineer, editor, feasibility_checker, model_trainer, modeler, reader, researcher, summarizer, validator, visualizer, writer。

---

## v2-4-2

### 架构文件
- **`architecture.md`** - 系统架构（简化版）
- **`methodology.md`** - 方法学（简化版）
- **`retrospective.md`** - 版本回顾总结

---

## v2-5-0 （重要版本）

### 概览文件
- **`README.md`** - 版本总览
- **`SUMMARY.md`** - 版本摘要
- **`ARCHITECTURE_v2.5.0.md`** - 架构总文档
- **`CHANGELOG.md`** - 变更日志

### 核心文档
- **`00_CHANGES.md`** - 主要变更说明
- **`01_README.md`** - README
- **`02_core.md`** - 核心规则
- **`03_workflow.md`** - 工作流程（18阶段）
- **`04_validation.md`** - 验证机制（7门控）
- **`05_consultation.md`** - 咨询机制
- **`06_agents.md`** - Agent规范
- **`07_anti_laziness.md`** - 反懒惰机制

### 架构详细文件
- **`architecture.md`** - 架构设计
- **`anti_lazy_mechanisms.md`** - 反懒惰机制详解
- **`directory_structure.md`** - 目录结构说明

### `agents/`
13个Agent的详细定义，每个Agent都有独立的Markdown文档，包含职责、输入输出、工作流程、提示词模板。

---

## v2-5-1 （精简版）

### 概览文件
- **`README.md`** - 版本总览
- **`SUMMARY.md`** - 版本摘要
- **`CHANGELOG.md`** - 变更日志

### 核心文档
- **`01_core_rules.md`** - 核心规则
- **`02_agents_contract.md`** - Agent契约

### 架构文件
- **`architecture.md`** - 架构设计
- **`methodology.md`** - 方法学
- **`retrospective.md`** - 版本回顾总结

### `agents/`
核心Agent（精简版），包含7个主要Agent：advisor, director, editor, model_trainer, summarizer, validator, writer。

### `agents_backup_v2.5.1/`
Agent备份，包含v2.5.0版本的完整Agent集合（13个）和当前版本的Agent定义。

---

## v2-5-7 （当前稳定版）

### 概览文件
- **`README.md`** - 版本总览
- **`SUMMARY.md`** - 版本摘要
- **`CHANGELOG.md`** - 变更日志

### 核心文档
- **`01_core_rules.md`** - 核心规则
- **`02_workflow_phases.md`** - 工作流程阶段（18阶段详解）
- **`03_validation_gates.md`** - 验证门控（7门控详解）
- **`04_data_authority.md`** - 数据权威层级

### `agents/`
13个Agent的详细规范文档，包含最新版本的Agent定义。

### `workflows/`
工作流定义，每个阶段都有独立的工作流文档：
- phase_0_init.md
- phase_05_validation.md
- phase_1_research.md
- phase_15_validation.md
- phase_2_design.md
- ... (所有18阶段)

---

## v3-0-0 （开发中）

### 概览文件
- **`README.md`** - 版本总览
- **`00_ARCHITECTURE.md`** - 架构总文档
- **`01_VERSION_HISTORY.md`** - 版本历史
- **`v3-0-0_new.md`** - 新特性说明
- **`V3-0-0_INITIALIZATION_COMPLETE.md`** - 初始化完成标记

### `draft/`
草稿文档目录，存放开发中的文档：
- `README.md` - 草稿索引
- `LLM-MM-Agent/` - LLM-MM-Agent文件结构文档
- `MCM-Killer/` - MCM-Killer文件结构文档

---

**文档版本**: v1.0
