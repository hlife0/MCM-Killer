# MCM-Killer v2.4.0 设计方法论

> **内部设计文档** — 给我们自己看的方法论思考，不是给 Agent 看的指令。

---

## 文档关系

| 文档 | 职责 |
|------|------|
| `retrospective.md` | 分析 v2.0-v2.3 的问题根源 |
| **`methodology.md`（本文档）** | 定义设计原则和方法论 |
| `architecture.md` | 定义具体架构和 Agent 契约 |

阅读顺序：retrospective → methodology → architecture

---

## 1. 问题背景

> 详细的问题分析见 `retrospective.md`。

**核心问题**：v2.0-v2.3 缺乏一个权威的、单一的架构定义，导致规则分散、冲突不断。

**v2.4 的目标**：建立规范层，让所有规则有唯一定义处。

---

## 2. 设计原则：我们需要什么样的系统？

### 原则 1: 单一真相源 (Single Source of Truth)

**每一类信息只定义在一个地方。**

- 历史问题分析 → 定义在 `retrospective.md`
- 设计原则和方法论 → 定义在 `methodology.md`（本文档）
- Agent 契约和具体架构 → 定义在 `architecture.md`

**Agent prompt 的职责不是"定义规则"，而是"实现契约"。**

这意味着：
- `CLAUDE.md` 不应该重复定义 Agent 的输入输出（应该引用 architecture.md）
- Agent prompt 不应该自己发明目录结构（应该引用 architecture.md）

### 原则 2: 明确的契约 (Clear Contracts)

**每个 Agent 是一个"黑盒"，有明确的接口。**

```
┌─────────────────────┐
│       Agent         │
│                     │
│  Input:  定义好的   │
│  Output: 定义好的   │
│  Trigger: 定义好的  │
│  Side Effects: 0    │
└─────────────────────┘
```

契约应该包含：
- **输入**: 这个 Agent 需要读取什么文件？格式是什么？
- **输出**: 这个 Agent 会产生什么文件？写到哪里？
- **触发条件**: 什么条件下这个 Agent 被调用？
- **前置依赖**: 调用前必须完成什么？
- **后置验证**: 调用后如何验证成功？

### 原则 3: 分层架构 (Layered Architecture)

**系统应该分为清晰的层次，每层有明确的职责。**

```
┌─────────────────────────────────────────┐
│  Layer 0: 规范层 (architectures/)       │  ← 我们设计的，定义规则
├─────────────────────────────────────────┤
│  Layer 1: 协调层 (CLAUDE.md / Director) │  ← 主 Agent，编排执行顺序
├─────────────────────────────────────────┤
│  Layer 2: 执行层 (Agent prompts)        │  ← 具体执行任务
├─────────────────────────────────────────┤
│  Layer 3: 数据层 (output/)              │  ← 产物存储
└─────────────────────────────────────────┘
```

**规则从上往下传递，不允许下层自己发明规则。**

### 原则 4: 可验证性 (Verifiability)

**所有规则都应该是可机器检查的。**

- 目录结构 → 可以用脚本验证
- 命名规范 → 可以用正则检查
- Agent prompt 格式 → 可以用模板验证

如果一个规则无法机器检查，那它就会在演进过程中被违反，然后我们又要打补丁。

### 原则 5: 演进机制 (Evolution Mechanism)

**修改规则有且只有一条路径：先改规范，再同步实现。**

```
1. 在 architecture.md 修改规则定义
2. 运行验证脚本，找出所有违反新规则的文件
3. 批量更新所有相关 prompts
4. 再次运行验证脚本，确保通过
```

**禁止**：直接修改某个 Agent prompt 来"修复"问题，而不更新 architecture.md。

---

## 3. 架构层次设计

### Layer 0: 规范层 (architectures/v2.4.0/)

这是"宪法"层，定义所有规则：

```
architectures/v2-4-0/
├── retrospective.md  # 问题反思：为什么之前版本出问题
├── methodology.md    # 本文档：设计原则和方法论
├── architecture.md   # 具体架构：Agent 契约、目录结构、命名规范
└── validators/       # （未来）验证脚本
    └── check_consistency.py
```

### Layer 1: 协调层 (CLAUDE.md)

`CLAUDE.md` 的职责是**编排**，不是**定义规则**。

它应该：
- 引用 architecture.md 中的规则（而不是复制粘贴）
- 定义 Agent 的执行顺序
- 处理异常情况（比如某个 Agent 失败时怎么办）

它不应该：
- 定义 Agent 的输入输出路径（这是 architecture.md 的事）
- 定义命名规范（这是 architecture.md 的事）
- 定义版本控制规则（这是 architecture.md 的事）

### Layer 2: 执行层 (Agent prompts)

每个 Agent prompt 的结构应该是：

```markdown
---
name: xxx
contract: architecture.md#4.x   # 引用架构文档中的契约定义
---

# Agent 特定的实现细节

## 你的职责
[从 architecture.md 复制，保持一致]

## 输入/输出
[从 architecture.md 复制，保持一致]

## 实现指南
[这里是 Agent 特定的内容，比如代码模板]
```

**关键点**：基础信息（职责、IO、路径）从 architecture.md 复制，Agent prompt 只包含实现细节。

### Layer 3: 数据层 (output/)

目录结构在 `architecture.md` 第三节中定义，所有 Agent 遵循同一份定义。

---

## 4. 信息流设计

### 4.1 控制流

**Director（主 Agent）是唯一的编排者，其他 Agent 之间不直接调用。**

```
Director → Agent A → Director → Agent B → Director → ...
               ↑           ↑           ↑
          验证结果     验证结果     验证结果
```

这样的好处：
- Director 可以控制执行顺序
- Director 可以处理失败
- Agent 之间解耦

### 4.2 数据流

**所有数据通过 `output/` 目录传递，Agent 之间不直接传参。**

```
Agent A → writes → output/data/xxx.csv
                        ↑
Agent B → reads ────────┘
```

这样的好处：
- 数据可追溯（有文件记录）
- 可以断点续跑
- 可以人工干预

### 4.3 版本流

**VERSION_MANIFEST.json 是唯一的版本状态记录。**

- Agent 写文件前：读 manifest，确定版本号
- Agent 写文件后：更新 manifest
- 其他 Agent 读文件：通过 manifest 找到最新版本

---

## 5. 演进策略

### 5.1 从 v2.3 到 v2.4 的迁移路径

1. **第一步：完善规范层**
   - ✅ 创建 `retrospective.md`：问题反思
   - ✅ 创建 `methodology.md`：方法论
   - ✅ 创建 `architecture.md`：Agent 契约
   - 📋 创建验证脚本

2. **第二步：重构 CLAUDE.md**
   - 删除重复定义的规则
   - 改为引用规范
   - 专注于编排逻辑

3. **第三步：重构 Agent prompts**
   - 统一格式
   - 删除与规范冲突的定义
   - 保留实现细节（代码模板等）

4. **第四步：验证**
   - 运行验证脚本
   - 确保所有文件符合规范

### 5.2 未来如何修改规则

**示例：想修改输出目录结构**

错误做法：
```
修改 data_engineer.md 中的路径
→ 发现 model_trainer.md 也要改
→ 发现 CLAUDE.md 也有提到
→ 漏改了 editor.md
→ 系统崩溃
```

正确做法：
```
1. 修改 architecture.md 第三节
2. 运行 check_consistency.py
3. 脚本告诉我们哪些文件需要更新
4. 批量更新
5. 再次验证
```

---

## 6. 成功标准

当我们完成 v2.4 后，应该能做到：

1. **新加一个 Agent**：在 `architecture.md` 第四节添加契约定义，然后创建 prompt
2. **修改目录结构**：修改 `architecture.md` 第三节，然后运行同步脚本
3. **检查系统健康**：运行验证脚本，0 errors = 系统健康
4. **理解系统**：看 `methodology.md` 和 `architecture.md` 就够了，不需要读 14 个文件

---

## 7. 下一步

基于这份方法论，下一步：

1. ✅ 设计规范层文档结构（已完成）
2. 📋 创建验证脚本
3. 📋 重构 CLAUDE.md（引用 architecture.md 而非重复定义）
4. 📋 重构 Agent prompts（引用 architecture.md 的契约）

**注意**：在验证脚本完成之前，不要修改任何 Agent prompt。

---

**文档版本**: v2.4.0-draft
**作者**: 我们
**日期**: 2026-01-03
