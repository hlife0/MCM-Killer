# v2.4.0 系统架构

> **权威架构定义** — 所有 Agent prompts 都应该从这份文档派生。

---

## 文档关系

| 文档 | 职责 |
|------|------|
| `retrospective.md` | 分析 v2.0-v2.3 的问题根源 |
| `methodology.md` | 定义设计原则和方法论 |
| **`architecture.md`（本文档）** | 定义具体架构和 Agent 契约 |

阅读顺序：retrospective → methodology → architecture

> ⚠️ **本文档是权威**。当 Agent prompt 与本文档冲突时，以本文档为准。

---

## 一、文档说明

这份文档是 v2.4.0 的**具体架构定义**，包含：

1. 系统的核心规则（唯一定义处）
2. 每个 Agent 的契约（输入/输出/触发/职责）
3. 目录结构契约
4. 命名规范
5. 验证方法

**使用方式**：创建或修改 Agent prompt 时，应该引用这份文档中的定义，而不是自己发明规则。

---

## 二、系统核心规则

### 2.1 参与者

| 角色 | 数量 | 说明 |
|------|------|------|
| Director | 1 | **系统主 Agent**，由 CLAUDE.md 配置，负责编排其他 Agent |
| Agent | 13 | 专业化执行者，各有专门职责 |

**Agent 列表**（规范名称）：
1. `reader`
2. `researcher`
3. `modeler`
4. `feasibility_checker`
5. `data_engineer`
6. `code_translator`
7. `model_trainer`
8. `validator`
9. `visualizer`
10. `writer`
11. `summarizer`
12. `editor`
13. `advisor`

> ⚠️ 在所有文档中必须使用上述规范名称，不得使用别名（如 `Coder`）。


### 2.2 数据权威等级

```
Level 1: 代码输出 (CSV/PKL) — 最高权威，其他文件必须与之一致
Level 2: Agent 报告 (MD)   — 必须反映 Level 1 的内容
Level 3: 论文文档 (TEX)    — 必须与 Level 1 一致，冲突时以 Level 1 为准
```

### 2.3 文件系统规则

**绝对禁止**：
- ❌ 修改 `output/` 以外的任何文件
- ❌ 写入 `reference_papers/`, `latex_template/`, `.claude/`
- ❌ 使用 `_final`, `_backup`, `_old` 等后缀

**版本控制**：
- ✅ 所有输出文件必须带版本号：`{name}_{i}.{ext}`（详见第三节）
- ✅ 每次写文件后更新 `VERSION_MANIFEST.json`

---

## 三、版本管理契约

### 3.1 核心原则

1. **所有输出文件必须带版本号**：`{name}_{i}.{ext}`（`{i}` 从 1 开始）
2. **VERSION_MANIFEST.json 是唯一的版本状态记录**
3. **禁止使用语义模糊的后缀**：`_final`, `_backup`, `_old`, `_new`

### 3.2 版本号规则

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| Markdown 文档 | `{name}_{i}.md` | `problem_requirements_1.md`, `model_design_2.md` |
| Python 脚本 | `{name}_{i}.py` | `model_1.py`, `data_prep_2.py` |
| 数据文件 | `{name}_{i}.pkl/csv` | `features_1.pkl`, `results_3.csv` |
| 图表 | `fig_{name}_{i}.png/pdf` | `fig_trend_1.png` |
| 论文 | `paper_{i}.tex/pdf` | `paper_1.tex` |
| Agent 汇报 | `{agent}_{i}.md` | `reader_1.md`, `modeler_2.md` |

**特殊情况**：
- `problem_full.md` - 不带版本号（一次性生成）
- `figure_index.md` - 不带版本号（持续更新）
- `.venv/` - 不带版本号（环境目录）

### 3.3 VERSION_MANIFEST.json

**位置**：`output/VERSION_MANIFEST.json`

**结构**：

```json
{
  "created_at": "2026-01-04 00:00:00",
  "last_updated": "2026-01-04 01:30:00",
  
  "files": {
    "problem/problem_requirements": {
      "current": 2,
      "history": [
        {"version": 1, "created_at": "2026-01-04 00:10:00", "created_by": "reader"},
        {"version": 2, "created_at": "2026-01-04 00:45:00", "created_by": "reader"}
      ]
    },
    "model/model_design": {
      "current": 1,
      "history": [
        {"version": 1, "created_at": "2026-01-04 00:30:00", "created_by": "modeler"}
      ]
    },
    "implementation/data/features": {
      "current": 3,
      "history": [...]
    }
  },
  
  "agent_calls": {
    "reader": 2,
    "researcher": 1,
    "modeler": 1,
    "data_engineer": 3
  }
}
```

### 3.4 Agent 操作规范

**写文件前**：
1. 读取 `VERSION_MANIFEST.json`
2. 查找该文件的当前版本号
3. 版本号 +1 作为新版本号

**写文件后**：
1. 更新 manifest 中该文件的 `current` 版本号
2. 在 `history` 数组中追加新版本记录
3. 更新 `last_updated` 时间戳
4. 更新 `agent_calls` 中该 Agent 的调用次数

**读文件时**：
1. 读取 `VERSION_MANIFEST.json`
2. 查找该文件的当前版本号
3. 读取 `{name}_{current}.{ext}`

**禁止**：
- ❌ 直接硬编码文件名（如 `features_1.pkl`）
- ❌ 覆盖已有版本文件
- ❌ 不更新 manifest 就写文件

### 3.5 版本回退

如果需要回退到旧版本：
1. 修改 manifest 中的 `current` 为目标版本号
2. **不要**删除任何版本文件
3. 在 `history` 中添加回退记录

---

## 四、目录结构契约

```
output/
├── VERSION_MANIFEST.json        # 版本控制元数据
│
├── problem/                     # 问题相关
│   ├── original/                # 原始题目文件（copy）
│   │   ├── {year}_MCM_Problem_{letter}.pdf
│   │   └── {year}_Problem_{letter}_Data/
│   ├── problem_full.md          # 完整题目 Markdown 版（Reader 从 PDF 转换）
│   └── problem_requirements_{i}.md  # Reader 的需求提取
│
├── docs/                        # 文档（协作相关）
│   ├── consultation/            # Agent 间咨询
│   │   └── {i}_{from}_{to}.md   # i = 全局咨询计数
│   ├── validation/              # 验证报告
│   │   └── {i}_{stage}_{agent}.md  # i = 全局验证计数
│   └── report/                  # Agent → Director 汇报
│       └── {agent_name}_{i}.md
│
├── model/                       # 模型设计
│   ├── research_notes_{i}.md    # 研究笔记
│   ├── model_design_{i}.md      # 数学模型设计
│   └── feasibility_{i}.md       # 可行性分析
│
├── implementation/              # 实现相关
│   ├── .venv/                   # Python 虚拟环境（所有 Agent 必须使用）
│   ├── data/                    # 数据文件
│   │   ├── raw/                 # 原始数据
│   │   ├── processed/           # 清洗后数据
│   │   ├── features_{i}.pkl     # 特征数据
│   │   └── results_{i}.csv      # 模型输出
│   ├── code/                    # 代码
│   │   ├── data_prep_{i}.py
│   │   ├── model_{i}.py
│   │   └── test_{i}.py
│   ├── logs/                    # 运行日志
│   │   └── training_{i}.log
│   └── analysis/                # Implementation Agent 的总结
│       └── {agent_name}_summary_{i}.md
│
└── paper/                       # 论文相关（所有 LaTeX 编译相关文件）
    ├── paper_{i}.tex            # 论文源文件
    ├── paper_{i}.pdf            # 论文 PDF
    ├── figures/                 # 图表
    │   ├── fig_{name}_{i}.png
    │   ├── fig_{name}_{i}.pdf
    │   └── figure_index.md
    └── summary/                 # 摘要
        ├── summary_sheet_{i}.tex
        └── summary_sheet_{i}.pdf
```

> **注意**：`{i}` 表示该文件的第几个版本/第几次调用，从 1 开始。

---

### 4.1 problem/ — 问题相关

#### 4.1.1 problem_full.md

**用途**：Reader 将 PDF 转换为 Markdown，供其他 Agent 直接读取（避免重复调用 docling）。

**注意**：
- 一次性生成，不带版本号
- 保持 PDF 原文内容，不做解读或修改

```markdown
# MCM {YEAR} Problem {LETTER}

{PDF 的完整 Markdown 转换内容}

## Background
{原文背景内容}

## Requirements
{原文需求内容}

## Data Description
{原文数据描述}

## Attachments
{附件列表}
```

#### 4.1.2 problem_requirements_{i}.md

**用途**：Reader 对问题的需求提取。

```markdown
# MCM {YEAR} Problem {LETTER}: 需求分析 v{i}

## 问题标题
{问题的完整标题，从 PDF 提取}

## 问题概述
{问题的核心背景和目标，用自己的话概括}

---

## 主要需求
1. [ ] {第一个主要需求 - 从 PDF 原文提取}
2. [ ] {第二个主要需求}
...

## 子需求
1.1 [ ] {主需求 1 的子需求}
1.2 [ ] {主需求 1 的子需求}
...

---

## 数据情况

| 文件名 | 描述 | 格式 | 大小 |
|--------|------|------|------|
| {filename} | {description} | {CSV/Excel/etc.} | {rows × cols} |

### 数据约束
- **允许使用**: {明确允许的数据来源}
- **禁止使用**: {明确禁止的数据来源}

---

## 格式要求

| 要求项 | 规定 |
|--------|------|
| 页数限制 | {页数} |
| 必须包含的章节 | {章节列表} |
| 特殊要求 | {任何特殊格式要求} |

---

## 不确定点
1. {不确定点 1}
2. {不确定点 2}

## 初步观察
{Reader 对问题的初步观察和直觉，不做方法预设，仅描述问题特征}
```

---

### 4.2 docs/ — 协作文档

docs 目录包含三类协作文档，其**文件契约**详见第五节：

| 子目录 | 用途 | 文件命名 | 详见 |
|--------|------|---------|------|
| `consultation/` | Agent 间咨询 | `{i}_{from}_{to}.md` | 5.2 节 |
| `validation/` | 验证报告 | `{i}_{stage}_{agent}.md` | 5.3 节 |
| `report/` | Agent 汇报 | `{agent}_{i}.md` | 5.4 节 |

> 文件格式定义统一在第五节协作契约中，此处不重复。

---

### 4.3 model/ — 模型设计

**路径**：`model/model_design_{i}.md`

**用途**：Modeler 的数学模型设计。

```markdown
# 模型设计 v{i}

## 问题建模
{问题的数学抽象}

## 变量定义
| 符号 | 含义 | 类型 | 范围 |
|------|------|------|------|
| {symbol} | {meaning} | {type} | {range} |

## 目标函数
$$
{objective}
$$

## 约束条件
1. $${constraint_1}$$
2. $${constraint_2}$$

## 求解策略
{算法或方法描述}

## 所需特征
| 特征名 | 来源 | 说明 |
|--------|------|------|
| {feature} | {source} | {desc} |

## 预期输出
{模型的输出形式和含义}
```

---

### 4.4 implementation/ — 实现相关

#### 4.4.1 .venv/

Python 虚拟环境。**所有 Agent 运行 Python 代码必须使用此环境**。

#### 4.4.2 data/

| 子目录/文件 | 说明 |
|------------|------|
| `raw/` | 原始数据，不修改 |
| `processed/` | 清洗后的数据 |
| `features_{i}.pkl` | 特征 DataFrame |
| `results_{i}.csv` | 模型输出结果 |

#### 4.4.3 code/

| 文件 | 说明 |
|------|------|
| `data_prep_{i}.py` | 数据预处理脚本 |
| `model_{i}.py` | 模型代码 |
| `test_{i}.py` | 测试脚本 |

#### 4.4.4 logs/

| 文件 | 说明 |
|------|------|
| `training_{i}.log` | 训练日志 |

#### 4.4.5 analysis/

| 文件 | 说明 |
|------|------|
| `{agent_name}_summary_{i}.md` | Implementation Agent 的总结 |

---

### 4.5 paper/ — 论文相关

#### 4.5.1 paper_{i}.tex / paper_{i}.pdf

论文源文件和编译后的 PDF。

#### 4.5.2 figures/

| 文件 | 说明 |
|------|------|
| `fig_{name}_{i}.png/pdf` | 图表文件 |
| `figure_index.md` | 图表索引 |

**figure_index.md 格式**：
```markdown
# 图表索引

| 图号 | 文件名 | 描述 | 用于论文章节 |
|------|--------|------|-------------|
| 1 | fig_xxx_1.png | {desc} | {section} |
| 2 | fig_yyy_1.png | {desc} | {section} |
```

#### 4.5.3 summary/

| 文件 | 说明 |
|------|------|
| `summary_sheet_{i}.tex` | 摘要源文件 |
| `summary_sheet_{i}.pdf` | 摘要 PDF |

---

## 五、协作契约

本节定义 Agent 间协作的三种机制的**契约**（接口与格式）。

> **注意**：本节只定义"是什么"，不定义"何时用"。具体的调用时机在执行流程中定义。

---

### 5.1 核心原则

1. **单线程执行**：同一时间只有一个 Agent 工作
2. **所有协作 Blocking**：发起协作后立即处理，无异步
3. **Director 中转**：Agent 间不直接通信，通过 Director 协调
4. **文件记录**：所有协作写入 `docs/` 目录

---

### 5.2 Consultation（咨询）

**定义**：Agent 在执行中向其他 Agent 请求信息。

**特点**：
- 双向：A → B → A
- Blocking：发起后立即处理

#### 发起方准则

> **鼓励发起咨询**：有任何不确定的问题都应该 consult，而不是自己猜测。

- ✅ 不确定就问
- ✅ 说明自己的理解，请对方确认或纠正
- ❌ 禁止在不确定时自行假设
- ❌ 禁止编造信息

#### 回复方准则

> **诚实回答**：只回答自己确切知道的，不知道就说不知道。

- ✅ 如实回答自己知道的内容
- ✅ 不知道/不确定时如实说明，建议对方 consult 其他 Agent
- ✅ Implementation 相关 Agent 可运行程序验证
- ✅ Reader 等可读取文件获取信息
- ❌ **禁止在被 consult 时申请 consult 第三方**（不能套娃）
- ❌ 禁止编造不知道的内容

#### 5.2.1 与 Director 的通信

**发起方**（简洁，不浪费 Director 上下文）：
```
Director，我需要咨询 @{agent}，文件：docs/consultation/{i}_{from}_{to}.md
```

**回复方**：
```
Director，已完成 @{agent} 的咨询回复，文件：docs/consultation/{i}_{from}_{to}.md
```

#### 5.2.2 文件契约

**路径**：`docs/consultation/{i}_{from}_{to}.md`

> `{i}` 是**全局咨询计数**（非 A→B 的计数），从 VERSION_MANIFEST 获取。

```markdown
# Consultation #{i}: {from} → {to}

| 字段 | 值 |
|------|------|
| 编号 | {i} |
| 发起方 | {from} |
| 接收方 | {to} |
| 时间 | {timestamp} |
| 状态 | PENDING / ANSWERED |

---

## 问题

{咨询内容，发起方填写}

---

## 回复

{回复内容，回复方填写}

## 不确定点

{回复方不确定的内容，建议发起方继续 consult 其他 Agent}
```

---

### 5.3 Validation（验证）

**定义**：对产出物进行多视角质量检查。

**特点**：
- **多人参与**：每个 Stage 由多个 Agent 从不同角度验证
- **独立判断**：每个验证者只能根据自己知识判断
- **禁止咨询**：Validation 期间不允许发起 Consultation
- **并行执行**：Director 可并行调用多个验证者

#### 5.3.1 验证者视角

| Agent | 验证视角 |
|-------|---------|
| reader | 题意符合性、Sanity check |
| researcher | 方法论可行性、文献支撑 |
| modeler | 模型设计一致性 |
| feasibility_checker | 技术/时间可行性 |
| advisor | 创新度、质量评估 |
| code_translator | 代码正确性 |
| validator | 结果合理性、是否造假 |

#### 5.3.2 验证结果

| 结果 | 含义 |
|------|------|
| ✅ **APPROVED** | 通过 |
| ⚠️ **CONDITIONAL** | 有条件通过 |
| ❌ **REJECTED** | 未通过，需修复 |

#### 5.3.3 与 Director 的通信

```
Director，已完成 {stage} 验证，判定：{结果}，报告：docs/validation/{i}_{stage}_{agent}.md
```

#### 5.3.4 文件契约

**路径**：`docs/validation/{i}_{stage}_{agent}.md`

> `{i}` 是**全局验证计数**，从 VERSION_MANIFEST 获取。

```markdown
# Validation #{i}: {stage} by {agent}

| 字段 | 值 |
|------|------|
| 编号 | {i} |
| 阶段 | {stage} |
| 验证者 | {agent} |
| 时间 | {timestamp} |
| 判定 | ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED |

---

## 验证视角

{该 Agent 从什么角度验证}

---

## 检查结果

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | {item} | ✅/⚠️/❌ | {note} |

---

## 问题列表（如有）

| # | 问题 | 严重程度 | 建议 |
|---|------|---------|------|
| 1 | {issue} | HIGH/MEDIUM/LOW | {suggestion} |

---

## 结论

{验证结论}
```

---

### 5.4 Report（汇报）

**定义**：Agent 完成调用后向 Director 汇报。

**特点**：
- 单向：Agent → Director
- 强制：每次调用后必须汇报
- 私密：仅 Director 可见

#### 5.4.1 汇报状态

| 状态 | 含义 |
|------|------|
| ✅ **SUCCESS** | 任务完成 |
| ⚠️ **PARTIAL** | 部分完成，有遗留 |
| ❌ **FAILED** | 任务失败 |

#### 5.4.2 文件记录

**路径**：`docs/report/{agent_name}_{i}.md`

```markdown
# 汇报: {agent_name} #{i}

| 字段 | 值 |
|------|------|
| Agent | {agent_name} |
| 调用序号 | {i} |
| 开始时间 | {timestamp} |
| 结束时间 | {timestamp} |
| 耗时 | {duration} |
| 状态 | ✅ SUCCESS / ⚠️ PARTIAL / ❌ FAILED |

---

## 任务摘要

{一句话描述}

---

## 执行内容

1. {做了什么}
2. {做了什么}

---

## 产出物

| 文件 | 路径 |
|------|------|
| {name} | {path} |

---

## 问题与风险

{遇到的问题、不确定性}

---

## 下一步建议

{建议 Director 接下来做什么}
```

---

### 5.5 问题上报

Agent 遇到无法继续的问题时，必须立即上报：

| 类型 | 格式 |
|------|------|
| 文件缺失 | "Director，文件 {path} 不存在，无法继续。" |
| 工具失败 | "Director，工具 {tool} 失败：{error}。" |
| 数据异常 | "Director，数据异常：{desc}。" |
| 需要确认 | "Director，我不确定是否应该 {action}，请确认。" |

**禁止**：
- ❌ 自行假设或编造
- ❌ 跳过问题继续
- ❌ 不上报就失败

---

## 六、Agent 契约定义

每个 Agent 的契约包含以下属性：

| 属性 | 说明 |
|------|------|
| 职责 | 核心任务 |
| 输入 | 需要读取的文件 |
| 输出 | 需要产生的文件 |
| 写入目录 | 允许写入的目录 |
| 参与的 Validation | 作为验证者参与哪些 Stage |

### 6.1 Agent 概览

| Agent | 职责 | 参与验证 |
|-------|------|---------|
| reader | 读取 PDF，提取需求 | MODEL, DATA, TRAINING, PAPER, SUMMARY, FINAL |
| researcher | 方法建议 | MODEL |
| modeler | 设计数学模型 | DATA, CODE, TRAINING |
| feasibility_checker | 可行性检查 | MODEL, CODE |
| data_engineer | 数据处理 | - |
| code_translator | 代码翻译 | CODE, TRAINING |
| model_trainer | 模型训练 | - |
| validator | 结果验证 | DATA, TRAINING, PAPER, SUMMARY, FINAL |
| visualizer | 生成图表 | - |
| writer | 撰写论文 | PAPER |
| summarizer | 创建摘要 | - |
| editor | 润色文档 | - |
| advisor | 质量评估 | MODEL, PAPER, FINAL |

### 6.2 输入输出契约

详细的 Agent 契约见 `.claude/agents/` 目录下的各 Agent prompt 文件。

> ⚠️ Agent prompt 必须与本文档保持一致。冲突时以本文档为准。

---

## 七、执行流程

详细流程见 `workflow_design.md`。

### 7.1 阶段概览

| Phase | 名称 | 主要 Agent | Validation Gate |
|-------|------|-----------|-----------------|
| 0 | Problem Understanding | reader, researcher | - |
| 1 | Model Design | modeler | ✅ MODEL |
| 2 | Feasibility Check | feasibility_checker | - |
| 3 | Data Processing | data_engineer | ✅ DATA |
| 4 | Code Translation | code_translator | ✅ CODE |
| 5 | Model Training | model_trainer | ✅ TRAINING |
| 6 | Visualization | visualizer | - |
| 7 | Paper Writing | writer | ✅ PAPER |
| 8 | Summary | summarizer | ✅ SUMMARY |
| 9 | Polish | editor | ✅ FINAL |
| 10 | Final Review | advisor | - |

### 7.2 返工机制

1. **返工不免验**：返工后必须以同样标准重新验证
2. **返工计数**：每个 Gate 最多返工 3 次
3. **回退机制**：严重问题需回退到更早阶段

---

## 八、如何使用本文档

### 8.1 创建/修改 Agent prompt

1. 查找本文档中的定义
2. 确保 prompt 与本文档一致
3. 不要在 prompt 中重复定义规则

### 8.2 解决冲突

- **本文档是权威**
- 发现冲突时，修改 prompt 使其符合本文档

### 8.3 相关文档

| 文档 | 内容 |
|------|------|
| `retrospective.md` | v2.0-v2.3 问题分析 |
| `methodology.md` | 设计原则 |
| `architecture.md` | 本文档，架构定义 |
| `workflow_design.md` | 详细执行流程 |
| `validation_design.md` | 验证机制详情 |
| `consultation_design.md` | 咨询机制详情 |
| `report_design.md` | 汇报机制详情 |

---

**文档版本**: v2.4.0  
**最后更新**: 2026-01-04
