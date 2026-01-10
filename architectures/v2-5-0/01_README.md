# MCM-Killer v2.5.0 系统架构

> **版本**: v2.5.0
> **发布日期**: 2026-01-07
> **基于**: v2.4.1

---

## 快速开始

本目录包含 MCM-Killer v2.5.0 的架构定义。**这是模板目录**，实际使用时需要复制到 workspace 中。

### 部署到 workspace

```bash
# 复制架构到 workspace
cp -r architectures/v2-5-0/* workspace/2025_C/.claude/architecture/
cp -r architectures/v2-5-0/agents/* workspace/2025_C/.claude/agents/
```

---

## 文档结构

```
v2-5-0/
├── 00_CHANGES.md           # 变更说明
├── 01_README.md            # 本文件
├── 02_core.md              # 核心规则（系统、目录、版本）
├── 03_workflow.md          # 执行流程（10 阶段）
├── 04_validation.md        # 验证机制
├── 05_consultation.md      # 咨询机制
├── 06_agents.md            # Agent 契约定义
├── 07_anti_laziness.md     # 反偷懒机制（新增）
└── agents/                 # Agent 模板
    ├── director.md
    ├── reader.md
    ├── researcher.md
    └── ...
```

---

## v2.5.0 核心改进

### 1. 架构可访问性
- 架构定义嵌入 workspace 内
- AI 可以直接查阅架构文件
- 解决 v2.4.1 的权限问题

### 2. 反偷懒机制
- 强制执行所有阶段
- 轻量级训练选项
- Token 监控和检查点
- 用户决策优先

### 3. 模块化设计
- 架构拆分为多个文件
- 便于维护和查阅
- 清晰的职责分离

### 4. 快速训练模式
- Phase 5A: 快速验证（mandatory, ≤30min）
- Phase 5B: 完整训练（optional）
- 禁止完全跳过训练

---

## 阅读顺序

**第一次使用**：
1. 00_CHANGES.md - 了解 v2.5.0 改进
2. 02_core.md - 核心规则和概念
3. 03_workflow.md - 执行流程
4. 07_anti_laziness.md - 反偷懒机制

**查阅特定内容**：
- Agent 契约 → 06_agents.md
- 验证机制 → 04_validation.md
- 咨询机制 → 05_consultation.md

---

## 与 v2.4.1 的对比

| 方面 | v2.4.1 | v2.5.0 |
|------|--------|--------|
| 架构位置 | 根目录 architectures/ | workspace 内 .claude/architecture/ |
| 文件组织 | 单文件 architecture.md | 多文件模块化 |
| Phase 5 | 可跳过 | 强制至少完成快速验证 |
| Token 管理 | 仅警告 | 监控 + 检查点 + 用户决策 |
| 训练策略 | 单一完整训练 | 两阶段（快速 + 完整） |

---

## 版本兼容性

- **兼容 v2.4.1 的输出目录结构**
- **兼容 v2.4.1 的 workflow**
- **Agent 契约基本不变**
- **新增反偷懒约束**

---

## 维护指南

### 修改架构

1. 修改 `architectures/v2-5-0/` 下的文件
2. 更新版本号和日期
3. 同步更新 workspace 中的副本

### 添加新 Agent

1. 在 `agents/` 目录创建 `{agent}.md`
2. 在 `06_agents.md` 中注册契约
3. 更新 workflow 中的调用位置

---

## 问题反馈

发现问题请记录在：
- `workspace/{problem}/output/docs/issues/`

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
