# MCM-Killer v2.5.0 变更说明

> **版本日期**: 2026-01-07
> **基于版本**: v2.4.1

---

## 一、核心问题识别

### 1.1 架构定位误解（Critical）

**原错误理解**：
- 认为 workspace 中的 AI 需要访问 `architectures/` 目录
- 将架构嵌入到 workspace 内部

**正确理解**：
- `architectures/` 在根目录，用于**前期协调**
- 在工作中，Agent 只参考 `workspace/.claude/agents/*.md`
- Agent 文件应当**自包含**，不引用外部架构

**关键区别**：
| 位置 | 用途 | 工作时是否访问 |
|------|------|---------------|
| `architectures/v2-5-0/` | 前期协调，设计参考 | ❌ 不访问 |
| `workspace/.claude/agents/v2-5-0/` | Agent 工作指南 | ✅ 只访问这里 |

### 1.2 AI 偷懒问题（High）

**问题表现**（从 v2.4.1 输出）：
- Phase 5 完全跳过（0% 完成）
- 理由："context 已使用较大"、"模型训练需要 8-10 小时"
- AI 自主决定跳过，未请求用户干预

**影响**：完整性强制令失效

### 1.3 结构组织问题（Medium）

**问题**：
- `architectures/` 在根目录，`workspace/` 并列
- Agent prompts 在 `workspace/{year}_problem/.claude/agents/`
- 层次不清晰

### 1.4 缺少轻量级训练要求（High）

**问题**：
- 模型训练默认使用完整 HMC 采样（4-6 小时）
- 没有快速验证选项
- 导致 AI 在 Token 限制时选择跳过

---

## 二、v2.5.0 解决方案

### 2.1 架构分层化（Architecture Layering）

**方案**：
```
MCM-Killer/
├── architectures/                  # 架构定义（前期协调，设计参考）
│   ├── v2-4-1/
│   └── v2-5-0/                     # 本版本
│       ├── 00_CHANGES.md           # 变更说明
│       ├── 01_README.md            # 导航
│       ├── 02_core.md              # 核心规则
│       ├── 03_workflow.md          # 执行流程
│       ├── 04_validation.md        # 验证机制
│       ├── 05_consultation.md      # 咨询机制
│       ├── 06_agents.md            # Agent 契约
│       ├── 07_anti_laziness.md     # 反偷懒
│       └── agents/                 # Agent 模板
│           ├── director.md
│           └── model_trainer.md
│
└── workspace/                      # 实际工作区
    └── {year}_problem/
        └── .claude/
            └── agents/
                └── v2-5-0/         # Agent 工作指南（自包含）
                    ├── director.md       # 完整、自包含
                    ├── model_trainer.md  # 完整、自包含
                    └── {agent}.md        # 完整、自包含
```

**关键原则**：
- `architectures/` = 设计协调文档（开发时参考）
- `workspace/.claude/agents/` = 工作执行指南（运行时使用）
- Agent 文件必须**自包含**，不引用架构
- 工作时 AI 只读取 `agents/*.md`，不访问 `architectures/`

### 2.2 反偷懒机制（Anti-Laziness）

**2.2.1 强制执行规则**

```markdown
## 完整性强制令 v2.5.0

1. **禁止跳过（No Skipping）**
   - 每个阶段必须执行
   - 遇到资源限制时自动降级
   - 禁止 AI 自主决定跳过

2. **自动降级（Automatic Degradation）**
   - Phase 5 根据预计时间自动选择 Tier
   - 6 小时阈值：≤6h 标准，>6h 自动降级
   - 4 级降级策略（Tier 1-4）
   - 任何 Tier 都必须产生有效输出

3. **无需人工干预（No Human Intervention）**
   - AI 自动做出所有决策
   - 不请求用户指示
   - 确保流畅执行到结束

4. **检查点机制（Checkpoint）**
   - 每个阶段结束保存状态
   - Token 接近限制时自动切换到轻量模式
```

**2.2.2 Phase 5 改进（6小时阈值）**

```markdown
## Phase 5: 模型训练（自动降级）

### 6小时阈值策略

**时间预估**：
- 评估训练时间（数据量 × 复杂度）

**自动决策**：
- ≤ 6 小时 → Tier 1（标准，100% 数据）
- > 6 小时 → Tier 2（轻量，50% 数据）
- > 12 小时 → Tier 3（最小，20% 数据）
- > 24 小时 → Tier 4（原型，10% 数据/MAP）

### 绝对禁止
- ❌ 完全跳过 Phase 5
- ❌ 理由"时间不足"就跳过
- ❌ 请求用户决策
- ✅ 必须至少 Tier 4
- ✅ 必须产生有效输出
```

### 2.3 目录结构（正确理解）

**最终结构**：
```
MCM-Killer/
├── architectures/                  # 架构定义（前期协调）
│   ├── v2-4-1/
│   └── v2-5-0/                     # 本版本
│       ├── 00_CHANGES.md           # 变更说明
│       ├── 01_README.md
│       ├── 02_core.md              # 核心规则
│       ├── 03_workflow.md
│       ├── 04_validation.md
│       ├── 05_consultation.md
│       ├── 06_agents.md
│       ├── 07_anti_laziness.md
│       └── agents/                 # Agent 模板（源）
│           ├── director.md
│           └── model_trainer.md
│
└── workspace/                      # 实际工作区
    └── 2025_C/
        └── .claude/
            └── agents/
                └── v2-5-0/         # Agent 工作指南（自包含）
                    ├── director.md       # 从 architectures 复制并修改
                    ├── model_trainer.md  # 从 architectures 复制并修改
                    └── {agent}.md        # 自包含，不引用架构
```

**关键点**：
- `architectures/v2-5-0/agents/` = Agent 模板源文件
- `workspace/.claude/agents/v2-5-0/` = Agent 工作文件（自包含）
- 工作时 AI 只读取 workspace 中的 agents/*.md

### 2.4 Agent 文件改进

**Director Agent（自包含）**：
- 完整的工作流程说明（内嵌）
- 10 阶段 workflow（内嵌）
- 4 级自动降级策略（内嵌）
- Phase 完整性检查（内嵌）
- **不引用任何架构文件**

**Model Trainer Agent（自包含）**：
- 6 小时阈值自动决策（内嵌）
- 4 级 Tier 降级策略（内嵌）
- 时间预估方法（内嵌）
- 训练流程示例（内嵌）
- **不引用任何架构文件**

**所有 Agent 文件原则**：
- 自包含（Self-contained）
- 工作时无需访问架构
- 所有必要信息内嵌在文件中

---

## 三、详细变更列表

### 3.1 架构文件变更

| 文件 | 状态 | 说明 |
|------|------|------|
| `00_core.md` | 新增 | 核心规则（从 architecture.md 提取） |
| `01_workflow.md` | 新增 | 执行流程（从 workflow_design 提取） |
| `02_validation.md` | 新增 | 验证机制（从 validation_design 提取） |
| `03_consultation.md` | 新增 | 咨询机制（从 consultation_design 提取） |
| `04_agents.md` | 新增 | Agent 契约（从 architecture.md 提取） |
| `05_anti_laziness.md` | 新增 | 反偷懒机制 |

### 3.2 Agent 文件变更

| Agent | 变更 |
|-------|------|
| director.md | 重写：添加 Token 监控、检查点、用户决策 |
| model_trainer.md | 增强：添加快速训练模式 |
| 所有 Agent | 更新架构引用路径 |

### 3.3 部署流程

**从 architectures 复制到 workspace**：
```bash
# 1. 创建 agents 目录
mkdir -p workspace/2025_C/.claude/agents/v2-5-0/

# 2. 复制 Agent 文件（从 architectures）
cp architectures/v2-5-0/agents/*.md workspace/2025_C/.claude/agents/v2-5-0/

# 3. 验证 Agent 文件是自包含的
# 确保不包含任何架构引用路径
```

**CLAUDE.md 内容（可选）**：
```markdown
# MCM-Killer v2.5.0

当前版本使用 v2.5.0 架构。
Agent 文件位置：`.claude/agents/v2-5-0/`
```

---

## 四、兼容性

### 4.1 向后兼容

- v2.5.0 完全兼容 v2.4.1 的输出目录结构
- v2.5.0 的 workflow 与 v2.4.1 保持一致
- Agent 契约基本不变

### 4.2 迁移指南

从 v2.4.1 迁移到 v2.5.0：
1. 创建 `architectures/v2-5-0/` 目录结构（模块化架构文档）
2. 创建 `workspace/{problem}/.claude/agents/v2-5-0/` 目录
3. 将 Agent 文件从 architectures 复制到 workspace
4. 确保 Agent 文件自包含（删除所有架构引用）
5. 更新 Agent 文件内容：
   - director.md：添加 4 级自动降级
   - model_trainer.md：添加 6 小时阈值
   - 其他 Agent：确保自包含

---

## 五、测试计划

### 5.1 单元测试
- [ ] Token 监控机制
- [ ] 检查点保存/恢复
- [ ] 快速训练模式

### 5.2 集成测试
- [ ] 完整 workflow 执行
- [ ] 验证 gate 触发
- [ ] 咨询机制

### 5.3 反偷懒测试
- [ ] 模拟长时间训练（>6 小时）场景
- [ ] 验证 AI 自动降级到 Tier 2/3/4
- [ ] 验证 AI 不跳过 Phase 5
- [ ] 验证 AI 不请求用户决策
- [ ] 验证任何 Tier 都产生有效输出

---

**版本**: v2.5.0
**创建日期**: 2026-01-07
**作者**: jcheniu
