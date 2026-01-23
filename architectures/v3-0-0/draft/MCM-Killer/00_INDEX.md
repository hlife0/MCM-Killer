# MCM-Killer 文件结构文档

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/00_INDEX.md`
> **重要程度**: ⭐⭐⭐ 竞赛优化系统
> **扩容影响**: **极高** - Agent/阶段需扩展 4 倍

MCM-Killer 是基于多智能体系统的数学建模竞赛优化系统，相比 LLM-MM-Agent 学术原型，MCM-Killer 针对竞赛场景进行了深度优化，包含更严格的工作流控制、更多的质量验证门控和更专业的 Agent 协作机制。在"扩容一倍源代码再扩容一倍"的背景下（从 18 阶段扩容到 72 阶段，从 13 Agent 扩容到 52 Agent），MCM-Killer 的可扩展架构设计成为关键挑战。

**迁移价值**：MCM-Killer 的核心价值在于其工作流机制和 Agent 协作模式。在扩容到 52 Agent 和 72 阶段时，需要：1）重新设计工作流引擎（支持动态阶段注册）；2）建立 Agent 标准化规范（模板化生成）；3）扩展验证门控机制（从 7 个到 28+ 个）；4）强化数据权威层级（从 3 层到 5 层）。这是迁移的重点区域。

---

## 文档导航

| 文档 | 绝对路径 | 描述 | 重要程度 | 扩容影响 |
|------|----------|------|----------|----------|
| [01_Project_Root.md](01_Project_Root.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/01_Project_Root.md` | 项目根目录文件（README, .gitignore, architectures, workspace, LaTeX 模板） | ⭐⭐⭐ | 中 - 目录结构需扩展 |
| [02_Workspace.md](02_Workspace.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/02_Workspace.md` | Workspace 工作目录（2025_C/），包含当前竞赛的完整工作空间 | ⭐⭐⭐ | **极高** - 18 阶段 → 72 阶段 |
| [03_Agents.md](03_Agents.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/03_Agents.md` | Agent 定义文件（.claude/agents/），13+ 专业 Agent 的职责和协作流程 | ⭐⭐⭐ | **极高** - 13 Agent → 52 Agent |
| [04_Architectures.md](04_Architectures.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/04_Architectures.md` | Architectures 架构历史，v2-3-0 到 v3-0-0 的版本演进记录 | ⭐⭐⭐ | **极高** - 架构需支持扩展 |
| [05_LaTeX_Template.md](05_LaTeX_Template.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/05_LaTeX_Template.md` | LaTeX 论文模板，MCM/ICM 竞赛专用的论文格式和样式 | ⭐⭐⭐ | 中 - 模板需支持更多章节 |

---

## 项目概览

MCM-Killer 是一个高度工程化的数学建模竞赛解决系统，核心特点：
- **18 阶段工作流**：从问题理解（Phase 0）到提交准备（Phase 10）的完整流程（**扩容目标**：72 阶段）
- **13+ 专业 Agent**：Reader, Researcher, Modeler, Validator, Writer, Editor, Advisor 等（**扩容目标**：52 Agent）
- **7 个验证门控**：Phase 0.5, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5, 10（**扩容目标**：28+ 验证门控）
- **三层数据权威**：CSV（Level 1 最高）> Agent Reports（Level 2）> Paper（Level 3 最低）（**扩容目标**：5 层权威）

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
