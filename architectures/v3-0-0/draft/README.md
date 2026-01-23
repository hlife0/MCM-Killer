# 两大项目文件结构文档索引

> Path: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/`
> **重要程度**: ⭐⭐⭐ 文档导航总入口

本文档是 LLM-MM-Agent 和 MCM-Killer 两大项目的文件结构总索引，提供完整的文档导航和快速定位。通过本文档，用户可以快速找到所需的技术文档、理解项目结构、把握核心概念。

---

## 项目列表

| 项目 | 定位 | 文档目录 | 迁移重点 |
|------|------|----------|----------|
| **LLM-MM-Agent** | 学术研究原型 (NeurIPS/ICML 2025) | `draft/LLM-MM-Agent/` | HMML 知识库、4 阶段管道、DAG 调度 |
| **MCM-Killer** | 竞赛优化系统 | `draft/MCM-Killer/` | 18 阶段工作流、验证门控、数据权威、Agent 协作 |

---

## 快速导航

### LLM-MM-Agent 文档

| 文档 | 描述 | 重要程度 | 迁移价值 |
|------|------|----------|----------|
| [总索引](LLM-MM-Agent/00_INDEX.md) | 文档导航，提供完整的项目概览和文档索引 | ⭐⭐⭐ | 理解系统整体架构 |
| [项目根目录](LLM-MM-Agent/01_Project_Root.md) | config.yaml, requirements.txt, README 等 | ⭐⭐⭐ | 配置管理、依赖管理 |
| [MMAgent 核心](LLM-MM-Agent/02_MMAgent_Core.md) | main.py, core/, engine/, llm/ 等核心模块 | ⭐⭐⭐ | 4 阶段管道、LLM 接口 |
| [Agent 模块](LLM-MM-Agent/03_Agents.md) | coordinator, task_solving, 各个 Agent | ⭐⭐⭐ | DAG 任务调度、Agent 协作 |
| [工具集](LLM-MM-Agent/04_Utilities.md) | utils/ 下 40+ 工具模块 | ⭐⭐ | 辅助功能参考 |
| [HMML 知识库](LLM-MM-Agent/05_HMML.md) | HMML 数学建模知识库 | ⭐⭐⭐ | **核心知识源，98+ 建模模式** |
| [MMBench 数据集](LLM-MM-Agent/06_MMBench.md) | MMBench 数据集和评估系统 | ⭐⭐ | 测试与评估基础 |
| [测试基础设施](LLM-MM-Agent/07_Test_Infrastructure.md) | 35+ 测试文件和文档 | ⭐ | 质量保障参考 |

---

### MCM-Killer 文档

| 文档 | 描述 | 重要程度 | 迁移价值 |
|------|------|----------|----------|
| [总索引](MCM-Killer/00_INDEX.md) | 文档导航，提供完整的项目概览和文档索引 | ⭐⭐⭐ | 理解系统整体架构 |
| [项目根目录](MCM-Killer/01_Project_Root.md) | README, .gitignore, architectures, workspace 等 | ⭐⭐⭐ | 项目组织结构 |
| [Workspace 工作目录](MCM-Killer/02_Workspace.md) | workspace/2025_C/ 完整工作空间 | ⭐⭐⭐ | **18 阶段工作流、数据权威层级** |
| [Agent 定义](MCM-Killer/03_Agents.md) | 13+ 专业 Agent 的职责和协作流程 | ⭐⭐⭐ | **Agent 协作机制、验证门控** |
| [Architectures 架构历史](MCM-Killer/04_Architectures.md) | v2-3-0 到 v3-0-0 版本演进记录 | ⭐⭐⭐ | **系统设计演进、核心概念起源** |
| [LaTeX 模板](MCM-Killer/05_LaTeX_Template.md) | MCM/ICM 竞赛论文模板 | ⭐⭐⭐ | **论文输出标准、格式规范** |

---

## 迁移优先级指南

### 第一优先级：核心概念与机制 ⭐⭐⭐

这些是系统最核心的机制，必须在迁移中保留和实现：

1. **HMML 知识库**（LLM-MM-Agent/05_HMML.md）
   - 3 层层级结构（Domain → Subdomain → Method Node）
   - 98+ 数学建模模式
   - 嵌入相似度匹配检索

2. **18 阶段工作流**（MCM-Killer/02_Workspace.md）
   - Phase 0 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5 → 5.5 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.5 → 10
   - 每个阶段的目标、输入、输出、验证标准

3. **验证门控机制**（MCM-Killer/03_Agents.md, 04_Architectures.md）
   - 7 个验证门控（Phase 0.5, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5, 10）
   - Validator Agent 的检查标准
   - 通过/不通过判断机制

4. **数据权威层级**（MCM-Killer/02_Workspace.md）
   - Level 1（最高）：CSV/PKL 数据
   - Level 2：Agent Reports
   - Level 3（最低）：Paper
   - 约束规则：Paper 必须与 CSV 一致

5. **Agent 协作流程**（MCM-Killer/03_Agents.md）
   - 13+ 专业 Agent 的职责定义
   - Agent 之间的输入输出关系
   - 协作流程图

6. **LaTeX 论文模板**（MCM-Killer/05_LaTeX_Template.md）
   - mcmthesis.cls 文档类
   - 论文格式规范（页面、字体、行距、摘要页）
   - 图表、公式、引用规范

---

### 第二优先级：支撑机制 ⭐⭐

这些是重要的支撑机制，有助于理解系统：

1. **DAG 任务调度**（LLM-MM-Agent/03_Agents.md）
   - coordinator.py 的依赖图构建
   - 拓扑排序和并行执行

2. **4 阶段管道**（LLM-MM-Agent/02_MMAgent_Core.md）
   - Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting
   - 与 18 阶段工作流的对应关系

3. **版本历史**（MCM-Killer/04_Architectures.md）
   - v2-4-0：工作流概念起源
   - v2-5-7：当前稳定版
   - v3-0-0：最新方向

4. **MMBench 数据集**（LLM-MM-Agent/06_MMBench.md）
   - 25 年竞赛题目和数据
   - 标准化格式
   - 评估框架

---

### 第三优先级：实现细节 ⭐

这些是代码实现细节，Claude Code 可以自动处理，迁移时不需要特别关注：

1. **代码生成与错误处理**（LLM-MM-Agent/04_Utilities.md）
   - autofixer, syntax_fixer
   - Claude Code 自带代码生成能力

2. **安全验证**（LLM-MM-Agent/04_Utilities.md）
   - code_guards, import_guard
   - Claude Code 有自己的安全机制

3. **图表生成**（LLM-MM-Agent/02_MMAgent_Core.md）
   - chart_renderer, chart_templates
   - Claude Code 可以生成图表

4. **模型训练**（MCM-Killer/03_Agents.md）
   - model_trainer Agent
   - Claude Code 可以训练模型

---

## 文档说明

本文档采用模块化组织方式：
- **每个文件**都有详细的描述（50 字以上）
- **重要程度**用星级标注（⭐⭐⭐ 核心机制，⭐⭐ 支撑机制，⭐ 实现细节）
- **迁移价值**说明该内容在迁移到 Claude Code 时的重要性
- 按目录结构依次展开，方便定位
- 核心文件提供更详细说明和扩充描述
- 过大模块拆分为多个子文档

---

## 关键概念速查

### LLM-MM-Agent 核心创新
- **HMML**：第一个 3 层数学建模知识库
- **DAG 调度**：基于依赖关系的任务编排
- **Omni-Survival Kit**：确保 PDF 生成的死手开关
- **SafePlaceholder**：防止模板格式化崩溃

### MCM-Killer 核心创新
- **18 阶段工作流**：精细化阶段控制
- **7 个验证门控**：强制质量检查
- **三层数据权威**：防止数据不一致
- **13+ 专业 Agent**：细粒度职责分离

### 两系统对比

| 特性 | LLM-MM-Agent | MCM-Killer |
|------|-------------|-----------|
| 定位 | 学术研究原型 | 竞赛优化系统 |
| 工作流 | 4 阶段管道 | 18 阶段精细化流程 |
| Agent | 6 个通用 Agent | 13+ 专业 Agent |
| 验证 | Actor-Critic 迭代 | 7 个强制验证门控 |
| 数据权威 | 单一数据源 | 三层权威层级 |
| 论文输出 | Omni-Survival Kit | LaTeX 专用模板 |

---

**创建日期**: 2026-01-23
**最后更新**: 2026-01-24
**文档版本**: v2.0
**状态**: ✅ 已完成所有文档扩充
