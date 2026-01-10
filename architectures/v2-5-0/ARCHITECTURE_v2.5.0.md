# MCM-Killer v2.5.0 Architecture

> **创建日期**: 2026-01-10
> **版本**: v2.5.0
> **作者**: jcheniu

---

## 概述

v2.5.0 是对 MCM-Killer 框架的重要架构更新，主要修复了 Agent 目录结构问题，并改进了整体系统设计。

## 关键修复

### 1. Agent 目录结构修复 (Critical)

**问题**: v2.5.0 之前的版本将 Agent 文件放在子目录中（如 `agents/v2-4-1/` 和 `agents/v2-5-0/`），这导致 Claude Code 无法正确调用 Agent。

**解决方案**: 将所有 Agent 文件扁平化到 `agents/` 目录下。

```
修复前:
workspace/2025_C/.claude/agents/
├── v2-4-1/
│   ├── advisor.md
│   ├── code_translator.md
│   └── ...
└── v2-5-0/
    ├── director.md
    ├── model_trainer.md
    └── ...

修复后:
workspace/2025_C/.claude/agents/
├── advisor.md
├── code_translator.md
├── director.md
├── model_trainer.md
└── ...
```

### 2. 版本命名规范

**问题**: 版本后缀混乱（v2-4-1、v2-5-0 使用连字符），与其他文件版本号不一致。

**解决方案**: 统一使用点号分隔版本号（v2.4.1、v2.5.0）。

### 3. 备份和迁移

- v2.4.1 Agent 文件已备份到 `/home/jcheniu/MCM-Killer/architectures/v2-4-1/agents_backup/`
- v2.5.0 Agent 文件已扁平化到 `/home/jcheniu/MCM-Killer/workspace/2025_C/.claude/agents/`

---

## 文件结构

```
MCM-Killer/
├── architectures/              # 架构文档库（开发时参考）
│   ├── v2-3-0.md              # 旧版本文档
│   ├── v2-4-0/                # v2.4.0 模块化架构
│   ├── v2-4-1/                # v2.4.1 架构和备份
│   │   ├── architecture.md    # v2.4.1 完整架构
│   │   ├── methodology.md
│   │   ├── retrospective.md
│   │   └── agents_backup/     # v2.4.1 agents 备份
│   └── v2-5-0/                # v2.5.0 改进架构（本目录）
│       ├── ARCHITECTURE_v2.5.0.md  # 本文件
│       └── (待添加其他文档)
│
└── workspace/
    └── 2025_C/
        └── .claude/
            ├── agents/        # Agent 文件（扁平化，运行时使用）
            │   ├── director.md
            │   ├── model_trainer.md
            │   └── ...
            └── CLAUDE.md      # 主配置文件
```

---

## 与 v2.4.1 的主要变化

| 方面 | v2.4.1 | v2.5.0 |
|------|--------|--------|
| Agent 目录结构 | `agents/v2-4-1/` 子目录 | `agents/` 扁平化 |
| 版本命名 | v2-4-1 | v2.5.0 |
| 架构文档位置 | `architectures/v2-4-1/architecture.md` | `architectures/v2-5-0/` |
| Agent 调用方式 | 无法正常调用 | 正常调用 |

---

## 部署说明

### 新项目部署

1. 复制 Agent 文件到 workspace:
   ```bash
   cp -r /home/jcheniu/MCM-Killer/architectures/v2-5-0/agents/* \
         /path/to/workspace/.claude/agents/
   ```

2. 复制并更新 CLAUDE.md

3. 验证 Agent 可以正常调用

### 现有项目迁移

1. 备份现有 agents 目录
2. 删除子目录结构
3. 将 Agent 文件扁平化到 agents 根目录
4. 更新 CLAUDE.md 中的路径引用

---

## 已知问题和限制

1. **架构文档访问**: workspace 中的 AI 无法访问父目录的 architectures 文件，需要将关键信息嵌入 CLAUDE.md 或 Agent 文件中

2. **版本管理**: 需要手动同步 architectures 和 workspace 中的版本

3. **备份策略**: 旧版本 agents 仅保留在 architectures 目录，不自动清理

---

## 未来改进方向

1. **自动化部署脚本**: 创建脚本自动同步 architectures 到 workspace

2. **版本管理工具**: 开发工具管理不同版本的架构和 agents

3. **文档生成**: 从架构文档自动生成 CLAUDE.md

4. **测试验证**: 添加自动化测试验证 Agent 可调用性

---

## 参考文档

- v2.3.0: `/home/jcheniu/MCM-Killer/architectures/v2-3-0.md`
- v2.4.1: `/home/jcheniu/MCM-Killer/architectures/v2-4-1/architecture.md`
- workspace: `/home/jcheniu/MCM-Killer/workspace/2025_C/CLAUDE.md`

---

**创建日期**: 2026-01-10
**最后更新**: 2026-01-10
**版本**: v2.5.0
