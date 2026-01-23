# MCM-Killer: Architectures 架构历史

> Path: `MCM-Killer/architectures/`
> **重要程度**: ⭐⭐⭐ 系统设计演进记录

本目录记录 MCM-Killer 系统从 v2-3-0 到 v3-0-0 的完整架构演进历史。每个版本都包含详细的设计文档、工作流定义、Agent 规范、验证机制说明。是理解系统设计演变和核心概念的重要资源。

---

## 版本历史概览

| 版本 | 描述 | 状态 | 迁移重要性 |
|------|------|------|-----------|
| v2-3-0 | 早期版本 | 已归档 | ⭐ 了解初始概念 |
| v2-4-0 | 工作流设计引入 | 已归档 | ⭐⭐ 工作流概念起源 |
| v2-4-1 | Agent 规范化 | 已归档 | ⭐⭐ Agent 规范参考 |
| v2-4-2 | 迭代优化 | 已归档 | ⭐ |
| v2-5-0 | 完整 18 阶段工作流 | 稳定版 | ⭐⭐⭐ **主要参考版本** |
| v2-5-1 | 精简版 | 已归档 | ⭐⭐ |
| v2-5-7 | 当前稳定版 | **推荐使用** | ⭐⭐⭐ **当前标准** |
| v3-0-0 | 开发中 | 实验性 | ⭐⭐⭐ **最新方向** |

---

## v2-5-7 （当前稳定版）⭐⭐⭐

### 概览文件
- **`README.md`** - 版本总览，快速了解本版本的核心特性和改进
- **`SUMMARY.md`** - 版本摘要，简要说明本版本的关键内容
- **`CHANGELOG.md`** - 变更日志，记录本版本相对于前一版本的修改

### 核心文档 ⭐⭐⭐
- **`01_core_rules.md`** - 核心规则，定义系统的基本规则和约束条件
- **`02_workflow_phases.md`** - 工作流程阶段（18 阶段详解），每个阶段的目标、输入、输出、验证标准
- **`03_validation_gates.md`** - 验证门控（7 门控详解），每个门控的检查项、通过标准、失败处理
- **`04_data_authority.md`** - 数据权威层级，三层权威体系的详细说明和约束规则

### `agents/` 目录 ⭐⭐⭐
13 个 Agent 的详细规范文档，包含最新版本的 Agent 定义。每个 Agent 文档包括：
- 职责说明
- 输入输出
- 工作流程
- 与其他 Agent 的协作关系
- 验证标准

### `workflows/` 目录 ⭐⭐⭐
工作流定义，每个阶段都有独立的工作流文档：
- `phase_0_init.md` - Phase 0 初始化阶段
- `phase_05_validation.md` - Phase 0.5 验证门控
- `phase_1_research.md` - Phase 1 研究阶段
- `phase_15_validation.md` - Phase 1.5 验证门控
- `phase_2_design.md` - Phase 2 设计阶段
- ... （所有 18 阶段的工作流文档）

**迁移价值**：这是当前稳定版本的完整文档，是理解系统核心概念（18 阶段工作流、验证门控、数据权威、Agent 协作）的最佳参考。

---

## v3-0-0 （开发中）⭐⭐⭐

### 概览文件
- **`README.md`** - 版本总览
- **`00_ARCHITECTURE.md`** - 架构总文档，系统整体架构设计
- **`01_VERSION_HISTORY.md`** - 版本历史，记录从 v2-5-7 到 v3-0-0 的演进
- **`v3-0-0_new.md`** - 新特性说明，v3-0-0 相对于 v2-5-7 的新增功能
- **`V3-0-0_INITIALIZATION_COMPLETE.md`** - 初始化完成标记

### `draft/` 目录
草稿文档目录，存放开发中的文档：
- `README.md` - 草稿索引（本文档所在位置）
- `LLM-MM-Agent/` - LLM-MM-Agent 文件结构文档（7 个子文档）
- `MCM-Killer/` - MCM-Killer 文件结构文档（5 个子文档）

**迁移价值**：这是最新开发版本的架构文档，包含系统的最新设计思路和改进方向。

---

## v2-5-0 （重要版本）⭐⭐⭐

### 概览文件
- **`README.md`** - 版本总览
- **`SUMMARY.md`** - 版本摘要
- **`ARCHITECTURE_v2.5.0.md`** - 架构总文档
- **`CHANGELOG.md`** - 变更日志

### 核心文档 ⭐⭐⭐
- **`00_CHANGES.md`** - 主要变更说明
- **`01_README.md`** - README
- **`02_core.md`** - 核心规则
- **`03_workflow.md`** - 工作流程（18 阶段）
- **`04_validation.md`** - 验证机制（7 门控）
- **`05_consultation.md`** - 咨询机制
- **`06_agents.md`** - Agent 规范
- **`07_anti_laziness.md`** - 反懒惰机制

### `agents/` 目录
13 个 Agent 的详细定义，每个 Agent 都有独立的 Markdown 文档，包含职责、输入输出、工作流程、提示词模板。

**迁移价值**：v2-5-0 是引入完整 18 阶段工作流的重要版本，v2-5-7 在此基础上进行了优化。理解 v2-5-0 有助于理解系统设计的历史演变。

---

## v2-4-0 （工作流设计引入）⭐⭐

### 架构文件
- **`architecture.md`** - 系统架构设计，定义基本的模块划分和接口
- **`workflow_design.md`** - 工作流程设计，**引入阶段化工作流的概念**（重要）
- **`validation_design.md`** - 验证机制设计，定义质量检查方法
- **`consultation_design.md`** - 咨询机制设计，定义与 Advisor 的交互流程
- **`report_design.md`** - 报告设计，定义输出报告的格式和内容
- **`methodology.md`** - 方法学文档，记录方法论基础
- **`retrospective.md`** - 版本回顾总结

**迁移价值**：v2-4-0 首次引入了阶段化工作流和验证门控的概念，是理解这些核心概念起源的重要参考。

---

## v2-4-1 （Agent 规范化）⭐⭐

### 架构文件
- **`architecture.md`** - 系统架构（更新版）
- **`methodology.md`** - 方法学（更新版）
- **`retrospective.md`** - 版本回顾总结

### `agents_backup/` 目录
Agent 定义备份，包含 13 个 Agent 的完整定义文档：advisor, code_translator, data_engineer, editor, feasibility_checker, model_trainer, modeler, reader, researcher, summarizer, time_validator, validator, visualizer, writer。

**迁移价值**：v2-4-1 规范化了 Agent 的定义，提供了早期的 Agent 规范参考。

---

## 其他版本

### v2-3-0, v2-4-2, v2-5-1 ⭐
早期版本或精简版本，主要价值在于了解系统的演进历史。对于理解当前系统的核心概念贡献较小。

---

## 架构演进的关键里程碑

### 1. v2-4-0：阶段化工作流的诞生
- 引入阶段化工作流概念
- 引入验证门控机制
- 引入咨询机制（Advisor Agent）

### 2. v2-5-0：完整 18 阶段工作流
- 确定 18 个阶段（Phase 0-10）
- 确定 7 个验证门控（Phase 0.5, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5, 10）
- 确定 13 个 Agent 规范
- 引入数据权威层级概念

### 3. v2-5-7：当前稳定版
- 优化工作流细节
- 完善验证门控规则
- 强化数据权威层级
- 提供完整的工作流文档（workflows/ 目录）

### 4. v3-0-0：最新演进方向
- 引入 v3-0-0 新特性（详见 v3-0-0_new.md）
- 优化架构设计
- 完善文档结构（draft/ 目录）

---

## 迁移指南：如何使用这些文档

### 理解系统核心概念
1. **首选**：阅读 `v2-5-7/` 的核心文档（01_core_rules.md, 02_workflow_phases.md, 03_validation_gates.md, 04_data_authority.md）
2. **补充**：阅读 `v3-0-0/` 的最新架构文档（00_ARCHITECTURE.md）
3. **历史**：阅读 `v2-4-0/workflow_design.md` 了解工作流概念的起源

### 理解 Agent 协作
1. **首选**：阅读 `v2-5-7/agents/` 的各个 Agent 文档
2. **补充**：阅读 `v2-4-1/agents_backup/` 了解 Agent 规范的演进
3. **参考**：阅读本目录的 `03_Agents.md` 了解 Agent 协作流程

### 理解工作流细节
1. **首选**：阅读 `v2-5-7/workflows/` 的各阶段工作流文档
2. **补充**：阅读 `v2-5-0/03_workflow.md` 了解工作流的整体设计

---

**文档版本**: v1.0
