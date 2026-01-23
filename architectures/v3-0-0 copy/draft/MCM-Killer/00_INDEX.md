# MCM-Killer 文件结构文档

> Path: `MCM-Killer/`

## 文档导航

| 文档 | 描述 |
|------|------|
| [01_Project_Root.md](01_Project_Root.md) | 项目根目录文件（README, .gitignore等） |
| [02_Workspace.md](02_Workspace.md) | Workspace工作目录（2025_C/） |
| [03_Agents.md](03_Agents.md) | Agent定义文件（.claude/agents/） |
| [04_Architectures.md](04_Architectures.md) | Architectures架构历史 |
| [05_LaTeX_Template.md](05_LaTeX_Template.md) | LaTeX论文模板 |

## 项目概览

MCM-Killer 是一个基于多智能体系统的数学建模竞赛优化系统。

### 核心特性
- **18阶段工作流**：从问题理解到提交准备的完整流程
- **13+专业Agent**：Reader, Researcher, Modeler, Validator, Writer等
- **7个验证门控**：确保每个阶段的质量
- **三层数据权威**：CSV > Agent Reports > Paper

### 目录结构概览

```
MCM-Killer/
├── architectures/           # 架构版本历史
│   ├── v2-5-7/             # 当前稳定版
│   └── v3-0-0/             # 开发中
├── workspace/2025_C/        # 活跃开发空间
│   ├── CLAUDE.md           # 工作流程
│   ├── .claude/agents/     # Agent定义
│   └── output/             # 输出
└── LaTeX__Template/        # 论文模板
```

---

**文档版本**: v1.0
**最后更新**: 2026-01-23
