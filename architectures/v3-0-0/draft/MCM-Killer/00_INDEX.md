# MCM-Killer 文件结构文档

> Path: `MCM-Killer/`
> **重要程度**: ⭐⭐⭐ 竞赛优化系统

MCM-Killer 是基于多智能体系统的数学建模竞赛优化系统，相比 LLM-MM-Agent 学术原型，MCM-Killer 针对竞赛场景进行了深度优化，包含更严格的工作流控制、更多的质量验证门控和更专业的 Agent 协作机制。

---

## 文档导航

| 文档 | 描述 | 重要程度 |
|------|------|----------|
| [01_Project_Root.md](01_Project_Root.md) | 项目根目录文件（README, .gitignore, architectures, workspace, LaTeX 模板） | ⭐⭐⭐ |
| [02_Workspace.md](02_Workspace.md) | Workspace 工作目录（2025_C/），包含当前竞赛的完整工作空间 | ⭐⭐⭐ |
| [03_Agents.md](03_Agents.md) | Agent 定义文件（.claude/agents/），13+ 专业 Agent 的职责和协作流程 | ⭐⭐⭐ |
| [04_Architectures.md](04_Architectures.md) | Architectures 架构历史，v2-3-0 到 v3-0-0 的版本演进记录 | ⭐⭐ |
| [05_LaTeX_Template.md](05_LaTeX_Template.md) | LaTeX 论文模板，MCM/ICM 竞赛专用的论文格式和样式 | ⭐⭐⭐ |

---

## 项目概览

MCM-Killer 是一个高度工程化的数学建模竞赛解决系统，核心特点：

### 核心特性
- **18 阶段工作流**：从问题理解（Phase 0）到提交准备（Phase 10）的完整流程
- **13+ 专业 Agent**：Reader, Researcher, Modeler, Validator, Writer, Editor, Advisor 等，各司其职
- **7 个验证门控**：Phase 0.5, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5, 10 等关键节点的质量检查
- **三层数据权威**：CSV（Level 1 最高）> Agent Reports（Level 2）> Paper（Level 3 最低）

### 与 LLM-MM-Agent 的区别

| 特性 | LLM-MM-Agent | MCM-Killer |
|------|-------------|-----------|
| 定位 | 学术研究原型 | 竞赛优化系统 |
| 工作流 | 4 阶段管道 | 18 阶段精细化流程 |
| Agent | 6 个通用 Agent | 13+ 专业 Agent |
| 验证机制 | Actor-Critic 迭代 | 7 个强制验证门控 |
| 数据权威 | 单一数据源 | 三层权威层级 |
| 文档生成 | Omni-Survival Kit | 多层验证 + LaTeX 模板 |

---

## 目录结构概览

```
MCM-Killer/
├── architectures/           # 架构版本历史
│   ├── v2-5-7/             # 当前稳定版（推荐）
│   └── v3-0-0/             # 开发中版本
├── workspace/2025_C/        # 活跃开发空间
│   ├── CLAUDE.md           # 18 阶段工作流手册
│   ├── .claude/agents/     # Agent 定义
│   ├── output/             # 输出目录
│   └── 2025_Problem_C_Data/ # 数据文件
└── LaTeX__Template_for_MCM_ICM/  # 论文模板
```

---

## 关键文件说明

### `workspace/2025_C/CLAUDE.md` ⭐⭐⭐
MCM-Killer 系统的操作手册，定义了完整的 18 阶段工作流程、13+ Agent 的职责、7 个验证门控的规则、三层数据权威层级。是使用 MCM-Killer 系统的核心指南。

### `workspace/2025_C/.claude/agents/*.md` ⭐⭐⭐
13+ 个 Agent 的详细定义文档，每个 Agent 都有明确的职责、输入输出、工作流程。是理解系统协作机制的关键。

### `architectures/v2-5-7/` ⭐⭐⭐
当前稳定版本的架构文档，包含核心规则、工作流阶段详解、验证门控详解、数据权威层级等完整文档。是理解系统设计的最佳参考。

---

**文档版本**: v1.0
**最后更新**: 2026-01-23
