# MCM-Killer v2.5.1: 核心规则

> **本文档定义系统的基础规则和约定**
>
> **版本**: v2.5.1
> **最后更新**: 2026-01-11

---

## 一、系统概述

### 1.1 设计目标

MCM-Killer 是一个**多 Agent 协作系统**，用于完成数学建模竞赛（MCM/ICM）。

**核心特点**：
- 专业化分工：13 个专业 Agent 各司其职
- 强制验证：每个关键阶段有多人验证
- 完整性保证：禁止简化或跳过任何步骤
- **LaTeX强制编译**：必须生成可编译的PDF（v2.5.1新增）

### 1.2 参与者

| 角色 | 数量 | 说明 |
|------|------|------|
| **Director** | 1 | 系统主 Agent，负责编排其他 Agent |
| **Specialist Agents** | 13 | 专业化执行者，各有专门职责 |

### 1.3 Agent 列表（规范名称）

| # | Agent 名称 | 职责 | LaTeX相关 |
|---|-----------|------|-----------|
| 0 | director | 编排所有 Agent，管理 workflow | - |
| 1 | reader | 读取 PDF，提取需求 | - |
| 2 | researcher | 方法建议 | - |
| 3 | modeler | 设计数学模型 | - |
| 4 | feasibility_checker | 可行性检查 | LaTeX环境问题处理 |
| 5 | data_engineer | 数据处理 | - |
| 6 | code_translator | 代码翻译 | - |
| 7 | model_trainer | 模型训练 | - |
| 8 | validator | 结果验证 | - |
| 9 | visualizer | 生成图表 | - |
| 10 | writer | 撰写论文 | ✅ **生成.tex/.pdf** |
| 11 | summarizer | 创建摘要 | ✅ **生成summary_sheet.tex** |
| 12 | editor | 润色文档 | ✅ **处理.tex并重新编译** |
| 13 | advisor | 质量评估 | - |

> **重要**：所有文档必须使用上述规范名称，不得使用别名。

---

## 二、绝对禁止规则

### 2.1 Director 禁止行为

```markdown
## Director 绝对禁止

- ❌ **NEVER 自己写代码** → 调用 @code_translator 或 @model_trainer
- ❌ **NEVER 自己设计模型** → 调用 @modeler
- ❌ **NEVER 自己写论文** → 调用 @writer
- ❌ **NEVER 自己画图** → 调用 @visualizer
- ❌ **NEVER 自己做验证** → 调用对应的验证者
- ❌ **NEVER 擅自跳过任何阶段** → 必须执行或请求用户决策
- ❌ **NEVER 降低质量要求以节省 Token** → 必须请求用户干预
- ❌ **NEVER 接受无PDF的论文** → Writer必须生成.tex和.pdf
```

### 2.2 Writer 禁止行为 (v2.5.1新增)

```markdown
## Writer 绝对禁止

- ❌ **NEVER 只生成.md文件** → 必须生成.tex和.pdf
- ❌ **NEVER 跳过LaTeX编译** → 编译失败必须通过Consultation解决
- ❌ **NEVER 从零创建.tex** → 必须使用latex_template/模板
- ❌ **NEVER 修改latex_template/** → 模板是只读的
- ❌ **NEVER 忽略编译错误** → 必须解决所有ERROR
- ❌ **NEVER 生成PDF页数不足** → 必须≥20页
```

### 2.3 Editor 禁止行为 (v2.5.1新增)

```markdown
## Editor 绝对禁止

- ❌ **NEVER 只处理.md文件** → 必须处理.tex并重新编译
- ❌ **NEVER 跳过编译验证** → 修改后必须重新生成PDF
- ❌ **NEVER 改变论文核心内容** → 只润色语言和格式
```

### 2.4 文件系统规则

**绝对禁止写入**：
- ❌ `output/` 以外的任何文件
- ❌ `reference_papers/`
- ❌ `latex_template/` (模板只读)
- ❌ `.claude/` 下的定义文件
- ❌ 使用 `_final`, `_backup`, `_old` 等后缀

**允许写入**：
- ✅ `output/` 下的所有子目录
- ✅ 必须带版本号：`{name}_{i}.{ext}`

---

## 三、数据权威等级

```
Level 1: 代码输出 (CSV/PKL) — 最高权威，其他文件必须与之一致
Level 2: Agent 报告 (MD)   — 必须反映 Level 1 的内容
Level 3: LaTeX文档 (TEX)   — 必须与 Level 1 一致，冲突时以 Level 1 为准
Level 4: PDF文档 (PDF)     — LaTeX编译的产物
Level 5: Markdown备份 (MD) — 可选的易读版本
```

**含义**：
- CSV 数据是事实的唯一来源
- LaTeX论文中引用的数据必须与 CSV 一致
- PDF是LaTeX的编译产物，必须验证可编译
- Markdown是可选备份，不能替代LaTeX

---

## 四、LaTeX强制要求 (v2.5.1核心)

### 4.1 LaTeX模板

**位置**：`workspace/{year}_{letter}/latex_template/`

**内容**：
```
latex_template/
├── mcmthesis.cls            # MCM论文类文件
├── mcmthesis-demo.tex       # 示例论文
└── figures/                 # 示例图表
    ├── example-image-a.pdf
    ├── example-image-b.pdf
    └── example-image-c.pdf
```

**规则**：
- ✅ Writer可以读取
- ❌ Writer禁止修改
- ✅ Writer必须复制到output/paper/使用

### 4.2 Writer输出要求

**强制输出**：
```
output/paper/
├── paper_{i}.tex            # LaTeX源文件（必须）
├── paper_{i}.pdf            # 编译后的PDF（必须）
├── paper_{i}.md             # Markdown备份（可选）
└── compile_{i}.log          # 编译日志（必须）
```

**编译要求**：
- ✅ 使用 `xelatex` 编译
- ✅ PDF必须可读且无损坏
- ✅ PDF页数必须 ≥ 20页
- ✅ 编译日志中无ERROR级别错误

### 4.3 编译错误处理

**遇到错误时的正确流程**：

```
Writer尝试编译
    ↓
编译失败？
    ├─ 是 → 停止工作
    │      ↓
    │   通过Consultation请求feasibility_checker
    │      ↓
    │   feasibility_checker安装缺失包/修复环境
    │      ↓
    │   Writer重新编译
    │
    └─ 否 → 验证PDF质量
             ↓
          提交Report
```

**禁止行为**：
- ❌ 跳过编译只输出.md
- ❌ 使用简化方案绕过错误
- ❌ 自行修改系统环境
- ❌ 降低PDF质量要求

### 4.4 Editor输出要求

**输入**：
- `paper/paper_{i}.tex`
- `paper/summary/summary_sheet_{i}.tex`

**输出**：
- `paper/paper_{i+1}.tex` (润色后的LaTeX)
- `paper/paper_{i+1}.pdf` (重新编译的PDF)
- `paper/summary/summary_sheet_{i+1}.tex`
- `paper/summary/summary_sheet_{i+1}.pdf`

**验证要求**：
- ✅ 修改后的.tex必须重新编译
- ✅ PDF必须可读
- ✅ 编译日志无ERROR

---

## 五、版本管理契约

### 5.1 版本号规则

**所有输出文件必须带版本号**：`{name}_{i}.{ext}`（`{i}` 从 1 开始）

| 文件类型 | 命名格式 | 示例 | LaTeX相关 |
|---------|---------|------|-----------|
| Markdown 文档 | `{name}_{i}.md` | `model_design_1.md` | - |
| LaTeX 文档 | `{name}_{i}.tex` | `paper_1.tex` | ✅ **v2.5.1新增** |
| PDF 文档 | `{name}_{i}.pdf` | `paper_1.pdf` | ✅ **v2.5.1新增** |
| 编译日志 | `compile_{i}.log` | `compile_1.log` | ✅ **v2.5.1新增** |
| Python 脚本 | `{name}_{i}.py` | `model_1.py` | - |
| 数据文件 | `{name}_{i}.pkl/csv` | `features_1.pkl` | - |
| 图表 | `figure_{name}_{i}.png` | `figure_trend_1.png` | - |
| Agent 汇报 | `{agent}_{i}.md` | `writer_1.md` | - |

**例外（不带版本号）**：
- `problem_full.md` - 一次性生成
- `VERSION_MANIFEST.json` - 元数据文件
- `.venv/` - 虚拟环境目录

### 5.2 VERSION_MANIFEST.json

**位置**：`output/VERSION_MANIFEST.json`

**结构**：
```json
{
  "version": "2.5.1",
  "created_at": "2026-01-11 00:00:00",
  "last_updated": "2026-01-11 01:30:00",

  "files": {
    "model/model_design": {
      "current": 2,
      "history": [
        {"version": 1, "created_at": "...", "created_by": "modeler"},
        {"version": 2, "created_at": "...", "created_by": "modeler"}
      ]
    },
    "paper/paper": {
      "current": 1,
      "history": [
        {"version": 1, "created_at": "...", "created_by": "writer", "compiled": true}
      ]
    }
  },

  "agent_calls": {
    "writer": 1
  },

  "latex_compilation": {
    "total_attempts": 1,
    "successful": 1,
    "failed": 0
  }
}
```

**v2.5.1新增字段**：
- `files[].compiled`: LaTeX是否成功编译
- `latex_compilation`: LaTeX编译统计

---

## 六、目录结构契约

### 6.1 完整结构

```
output/
├── VERSION_MANIFEST.json        # 版本控制元数据
│
├── problem/                     # 问题相关
│   ├── original/                # 原始题目文件（只读）
│   ├── problem_full.md          # 完整题目 Markdown 版
│   └── problem_requirements_{i}.md
│
├── docs/                        # 协作文档
│   ├── consultation/            # Agent 间咨询
│   │   └── {i}_{from}_{to}.md
│   ├── validation/              # 验证报告
│   │   └── {i}_{stage}_{agent}.md
│   └── report/                  # Agent → Director 汇报
│       └── {agent}_{i}.md
│
├── model/                       # 模型设计
│   ├── research_notes_{i}.md
│   ├── model_design_{i}.md
│   └── feasibility_{i}.md
│
├── implementation/              # 实现相关
│   ├── .venv/                   # Python 虚拟环境
│   ├── data/                    # 数据文件
│   │   ├── features_{i}.pkl/csv
│   │   └── results_{i}.csv
│   ├── code/                    # 代码
│   │   ├── data_prep_{i}.py
│   │   ├── model_{i}.py
│   │   └── test_{i}.py
│   └── logs/                    # 运行日志
│
└── paper/                       # 论文（v2.5.1重大更新）
    ├── paper_{i}.tex            # LaTeX源文件（强制）
    ├── paper_{i}.pdf            # 编译后的PDF（强制）
    ├── paper_{i}.md             # Markdown备份（可选）
    ├── compile_{i}.log          # 编译日志（强制）
    ├── figures/                 # 论文图表
    │   ├── figure_{name}_{i}.png
    │   └── figure_index.md
    └── summary/                 # 摘要
        ├── summary_sheet_{i}.tex    # LaTeX摘要表（强制）
        ├── summary_sheet_{i}.pdf    # 编译后的摘要（强制）
        └── summary_1page.md         # Markdown摘要（可选）
```

### 6.2 LaTeX相关文件契约

**Writer产出物**（Phase 7）：
```
output/paper/
├── paper_1.tex          # 必须存在，非空，可编译
├── paper_1.pdf          # 必须存在，可读，≥20页
├── compile_1.log        # 必须存在，记录编译过程
└── paper_1.md           # 可选
```

**Summarizer产出物**（Phase 8）：
```
output/paper/summary/
├── summary_sheet_1.tex  # 必须存在
└── summary_1.md         # 可选
```

**Editor产出物**（Phase 9）：
```
output/paper/
├── paper_2.tex          # 必须存在，润色后重新编译
├── paper_2.pdf          # 必须存在，编译验证通过
├── compile_2.log        # 必须存在
└── summary/
    ├── summary_sheet_2.tex   # 必须存在
    ├── summary_sheet_2.pdf   # 必须存在，v2.5.1新增
    └── summary_1page.md
```

---

## 七、验证Gate新增检查项 (v2.5.1)

### 7.1 PAPER Gate

**验证者**：reader, validator, advisor, writer

**v2.5.1新增检查项**：
- [ ] `paper_{i}.tex` 文件存在且非空
- [ ] `paper_{i}.pdf` 文件存在且可读
- [ ] PDF页数 ≥ 20页
- [ ] `compile_{i}.log` 无ERROR级别错误
- [ ] PDF内容与题目要求一致
- [ ] PDF无乱码或格式错误

**REJECTED条件**：
- 缺少 `.tex` 或 `.pdf` 文件
- PDF无法打开或损坏
- PDF内容为空或乱码
- 编译日志有未解决的ERROR
- PDF页数 < 20页且无合理说明

### 7.2 SUMMARY Gate

**v2.5.1新增检查项**：
- [ ] `summary_sheet_{i}.tex` 存在
- [ ] 摘要内容完整

### 7.3 FINAL Gate

**v2.5.1新增检查项**：
- [ ] 最终 `paper.pdf` 存在且可读
- [ ] 最终 `summary_sheet.pdf` 存在且可读
- [ ] 所有PDF文件大小合理（>10KB）
- [ ] 所有PDF可正常打开

---

## 八、质量保证 (v2.5.1强化)

### 8.1 LaTeX质量标准

**最低要求**：
- ✅ 使用xelatex编译通过
- ✅ 无ERROR级别编译错误
- ✅ PDF文件可正常打开
- ✅ PDF页数 ≥ 20页
- ✅ 包含所有必需章节

**推荐标准**：
- ⭐ PDF页数 20-30页
- ⭐ 包含3-5个图表
- ⭐ 无WARNING级别警告
- ⭐ 代码格式规范

### 8.2 编译日志要求

**必须包含**：
- xelatex完整命令
- 编译时间戳
- 所有输出（包括warnings）
- 最终编译状态（SUCCESS/FAILED）
- 失败时的错误详情

**示例**：
```
=== LaTeX Compilation Log ===
Date: 2026-01-11 12:00:00
Command: xelatex -interaction=nonstopmode paper_1.tex
Working Directory: /path/to/output/paper

=== Output ===
...
=== Final Status ===
SUCCESS: paper_1.pdf generated (23 pages)
```

---

**版本**: v2.5.1
**最后更新**: 2026-01-11
**主要变更**: 强制LaTeX编译，修复只生成Markdown的问题
