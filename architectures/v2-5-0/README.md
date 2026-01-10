# MCM-Killer v2.5.0: Architecture Overview

> **反偷懒架构版本** - 解决AI跳过Phase的问题

---

## 版本目标

v2.5.0的核心目标是**消除AI偷懒行为**,确保:

1. **零跳过**: 不允许任何Phase被跳过
2. **轻量降级**: 资源不足时必须降级,不能skip
3. **路径自洽**: workspace包含完整架构副本
4. **强制检查**: 每个Phase结束必须验证完整性

---

## 关键改进

### 1. 架构部署方式

**v2.4.1 (错误)**:
```
MCM-Killer/
├── architectures/v2-4-1/architecture.md  ← AI无法访问
└── workspace/2025_C/.claude/agents/
```

**v2.5.0 (正确)**:
```
MCM-Killer/
├── architectures/v2-5-0/              # 模板和参考
└── workspace/2025_C/
    └── .claude/
        ├── architecture/              # ← 自包含架构副本
        │   └── architecture.md
        └── agents/                    # Agent定义
```

### 2. Model Trainer强制3-tier

**Tier 1 (完整模型)**:
- 标准参数设置
- 完整采样/迭代
- 预期时间: 4-8小时

**Tier 2 (轻量模型)**:
- 减少采样次数 (50%)
- 降低收敛标准
- 预期时间: 1-2小时

**Tier 3 (最小模型)**:
- 快速原型算法
- 最少必要迭代
- 预期时间: 10-30分钟

**规则**:
- ✅ 优先Tier 1
- ⚠️ 资源不足时Tier 2
- ❌ 紧急时Tier 3 (但必须有结果)
- 🚫 **禁止skip**

### 3. Phase完整性检查

**Director Agent每Phase结束时必须检查**:

```markdown
## Phase X 完整性检查

- [ ] 所有必需文件已生成?
- [ ] 文件非空且格式正确?
- [ ] 版本号已更新?
- [ ] Report已提交?
- [ ] Validation Gate已执行 (如果有)?
- [ ] 是否有步骤被跳过? (如有,记录原因)

如果任何一项为NO → 回滚并重新执行
```

---

## 目录结构规范

### 完整结构

```
MCM-Killer/
│
├── architectures/                      # 全局架构模板
│   ├── v2-4-1/
│   │   ├── architecture.md
│   │   ├── methodology.md
│   │   └── retrospective.md
│   └── v2-5-0/
│       ├── CHANGELOG.md               # 版本变更
│       ├── README.md                  # 本文件
│       ├── architecture.md            # 核心架构定义
│       ├── directory_structure.md     # 目录结构说明
│       └── anti_lazy_mechanisms.md    # 反偷懒机制
│
├── workspace/                         # 项目工作区
│   └── 2025_C/                        # 具体项目
│       ├── .claude/
│       │   ├── architecture/          # ← 项目专用架构副本
│       │   │   └── architecture.md    # 从architectures/v2-5-0/复制
│       │   │
│       │   ├── agents/                # Agent定义
│       │   │   ├── director.md        # 主控Agent
│       │   │   ├── reader.md
│       │   │   ├── researcher.md
│       │   │   ├── modeler.md
│       │   │   ├── data_engineer.md
│       │   │   ├── code_translator.md
│       │   │   ├── model_trainer.md   # ← 增强: 3-tier模型
│       │   │   ├── validator.md
│       │   │   ├── visualizer.md
│       │   │   ├── writer.md
│       │   │   ├── summarizer.md
│       │   │   ├── editor.md
│       │   │   ├── advisor.md
│       │   │   └── feasibility_checker.md
│       │   │
│       │   └── settings.local.json    # 项目配置
│       │
│       ├── output/                    # 所有输出
│       │   ├── VERSION_MANIFEST.json
│       │   ├── problem/
│       │   ├── docs/
│       │   ├── model/
│       │   ├── implementation/
│       │   └── paper/
│       │
│       └── CLAUDE.md                  # 项目入口文档
│
└── README.md                          # MCM-Killer总体说明
```

---

## 核心文件说明

### architecture.md

**位置**: `workspace/{project}/.claude/architecture/architecture.md`

**内容**:
- 系统核心规则
- Agent契约定义
- 目录结构契约
- 协作机制 (Consultation/Validation/Report)
- 执行流程

**引用方式**:
```markdown
> **权威参考**: `.claude/architecture/architecture.md`
```

### agents/*.md

**位置**: `workspace/{project}/.claude/agents/*.md`

**特点**:
- 每个 agent一份独立文件
- 引用本项目的 architecture.md (相对路径)
- 包含输入/输出/职责/验证参与

### CLAUDE.md

**位置**: `workspace/{project}/CLAUDE.md`

**作用**:
- 项目入口文档
- Director Agent的主prompt
- 引用架构和其他agents

---

## 关键规则

### Rule 1: 禁止跳过Phase

**错误** (v2.4.1):
```
Phase 5: Model Training | ⏭️ Skipped | 0%
```

**正确** (v2.5.0):
```
Phase 5: Model Training | ⚠️ Tier 3 (Light) | 100%
结果: results_1.csv (快速原型,可用但不精确)
```

### Rule 2: 路径必须可访问

**错误** (v2.4.1):
```markdown
> **权威参考**: `architectures/v2-4-1/architecture.md`
```
AI在workspace中无法访问父目录的architectures/

**正确** (v2.5.0):
```markdown
> **权威参考**: `.claude/architecture/architecture.md`
```
相对路径,AI可以访问

### Rule 3: Token不足必须降级

**错误** (v2.4.1):
```
考虑到Token限制,建议跳过完整训练,进入Phase 6
```

**正确** (v2.5.0):
```
Token接近限制,切换到Tier 2轻量模型:
- 迭代次数: 1000 → 500
- 链数: 4 → 2
- 必须产生results.csv
```

---

## 使用指南

### 创建新项目

1. **初始化workspace**:
```bash
mkdir -p workspace/2026_A/.claude/{architecture,agents}
```

2. **复制架构文件**:
```bash
cp architectures/v2-5-0/*.md workspace/2026_A/.claude/architecture/
```

3. **复制agents**:
```bash
cp -r architectures/v2-5-0/agents/* workspace/2026_A/.claude/agents/
```

4. **创建CLAUDE.md**:
```bash
cp architectures/v2-5-0/CLAUDE.template.md workspace/2026_A/CLAUDE.md
```

### 验证部署

检查清单:
- [ ] `.claude/architecture/architecture.md` 存在
- [ ] 所有agents存在 (13个.md文件)
- [ ] agents中的路径引用正确 (`.claude/architecture/`)
- [ ] CLAUDE.md引用路径正确
- [ ] architecture.md版本号为v2.5.0

---

## 版本对比

| 特性 | v2.4.1 | v2.5.0 |
|------|--------|--------|
| 架构路径 | architectures/ (不可达) | .claude/architecture/ (可达) |
| Model Trainer | 可skip | 3-tier强制 |
| Phase检查 | 无 | 每Phase强制检查 |
| Token处理 | 允许跳过 | 强制降级 |
| 完整性 | Completeness Mandate | Mandate + 执行机制 |

---

## 维护指南

### 更新架构

1. 修改 `architectures/v2-5-0/architecture.md`
2. 同步到所有workspace: `cp architectures/v2-5-0/*.md workspace/*/.claude/architecture/`
3. 更新版本号和CHANGELOG

### 更新Agent

1. 修改 `architectures/v2-5-0/agents/{agent}.md`
2. 同步到所有workspace
3. 验证路径引用正确

### 版本升级

1. 创建新目录: `architectures/v2-6-0/`
2. 复制并修改文件
3. 更新CHANGELOG
4. 迁移现有workspace

---

**Maintainer**: jcheniu
**Last Updated**: 2026-01-07
**Version**: 2.5.0
