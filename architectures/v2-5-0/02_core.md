# MCM-Killer v2.5.0: 核心规则

> **本文档定义系统的基础规则和约定**
>
> **版本**: v2.5.0
> **最后更新**: 2026-01-07

---

## 一、系统概述

### 1.1 设计目标

MCM-Killer 是一个**多 Agent 协作系统**，用于完成数学建模竞赛（MCM/ICM）。

**核心特点**：
- 专业化分工：13 个专业 Agent 各司其职
- 强制验证：每个关键阶段有多人验证
- 完整性保证：禁止简化或跳过任何步骤
- 反偷懒设计：强制执行所有阶段

### 1.2 参与者

| 角色 | 数量 | 说明 |
|------|------|------|
| **Director** | 1 | 系统主 Agent，负责编排其他 Agent |
| **Specialist Agents** | 13 | 专业化执行者，各有专门职责 |

### 1.3 Agent 列表（规范名称）

| # | Agent 名称 | 职责 |
|---|-----------|------|
| 0 | director | 编排所有 Agent，管理 workflow |
| 1 | reader | 读取 PDF，提取需求 |
| 2 | researcher | 方法建议 |
| 3 | modeler | 设计数学模型 |
| 4 | feasibility_checker | 可行性检查 |
| 5 | data_engineer | 数据处理 |
| 6 | code_translator | 代码翻译 |
| 7 | model_trainer | 模型训练 |
| 8 | validator | 结果验证 |
| 9 | visualizer | 生成图表 |
| 10 | writer | 撰写论文 |
| 11 | summarizer | 创建摘要 |
| 12 | editor | 润色文档 |
| 13 | advisor | 质量评估 |

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
```

### 2.2 文件系统规则

**绝对禁止写入**：
- ❌ `output/` 以外的任何文件
- ❌ `reference_papers/`
- ❌ `latex_template/`
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
Level 3: 论文文档 (TEX/MD) — 必须与 Level 1 一致，冲突时以 Level 1 为准
```

**含义**：
- CSV 数据是事实的唯一来源
- 论文中引用的数据必须与 CSV 一致
- 验证时必须对比 CSV，不能仅看论文

---

## 四、版本管理契约

### 4.1 版本号规则

**所有输出文件必须带版本号**：`{name}_{i}.{ext}`（`{i}` 从 1 开始）

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| Markdown 文档 | `{name}_{i}.md` | `model_design_1.md` |
| Python 脚本 | `{name}_{i}.py` | `model_1.py` |
| 数据文件 | `{name}_{i}.pkl/csv` | `features_1.pkl` |
| 图表 | `figure_{name}_{i}.png` | `figure_trend_1.png` |
| Agent 汇报 | `{agent}_{i}.md` | `modeler_1.md` |

**例外（不带版本号）**：
- `problem_full.md` - 一次性生成
- `VERSION_MANIFEST.json` - 元数据文件
- `.venv/` - 虚拟环境目录

### 4.2 VERSION_MANIFEST.json

**位置**：`output/VERSION_MANIFEST.json`

**结构**：
```json
{
  "version": "2.5.0",
  "created_at": "2026-01-07 00:00:00",
  "last_updated": "2026-01-07 01:30:00",

  "files": {
    "model/model_design": {
      "current": 2,
      "history": [
        {"version": 1, "created_at": "...", "created_by": "modeler"},
        {"version": 2, "created_at": "...", "created_by": "modeler"}
      ]
    }
  },

  "agent_calls": {
    "reader": 2,
    "modeler": 2,
    "data_engineer": 1
  },

  "checkpoints": {
    "last_phase": 5,
    "last_checkpoint": "output/.checkpoint_phase5.json"
  }
}
```

### 4.3 Agent 操作规范

**写文件前**：
1. 读取 `VERSION_MANIFEST.json`
2. 查找该文件的当前版本号
3. 版本号 +1 作为新版本号

**写文件后**：
1. 更新 manifest 中的版本信息
2. 更新 `last_updated` 时间戳
3. 更新 `agent_calls` 计数

---

## 五、目录结构契约

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
│   │   ├── raw/                 # 原始数据
│   │   ├── processed/           # 清洗后数据
│   │   └── features_{i}.pkl/csv
│   ├── code/                    # 代码
│   │   ├── data_prep_{i}.py
│   │   ├── model_{i}.py
│   │   └── test_{i}.py
│   └── logs/                    # 运行日志
│
└── paper/                       # 论文相关
    ├── paper_{i}.md             # 论文源文件
    ├── figures/                 # 图表
    │   └── figure_{name}_{i}.png
    └── summary/                 # 摘要
        └── summary_1page.md
```

---

## 六、数据完整性标准

> **防止数据污染**：v2.4.0 实验显示 Python 对象被序列化为字符串写入 CSV。

### 6.1 标量原则

**CSV 中的每个单元格必须是**：
- `int` - 整数
- `float` - 浮点数
- `str` - 纯字符串（不含序列化对象）
- `bool` - 布尔值

**绝对禁止**：
- ❌ `"[1, 2, 3]"` - 序列化的列表
- ❌ `"{'a': 1}"` - 序列化的字典
- ❌ `"array([1, 2, 3])"` - NumPy 数组转字符串

### 6.2 强制自检

**Data Engineer 必须在代码中包含**：
```python
def check_data_quality(df):
    """检查数据完整性，防止污染"""
    # 检查序列化对象
    for col in df.select_dtypes(include=['object']):
        if df[col].astype(str).str.contains(r'^\[|^\{').any():
            raise ValueError(f"列 {col} 包含序列化的 Python 对象！")

    # 检查重复
    if df.duplicated().any():
        raise ValueError(f"数据包含 {df.duplicated().sum()} 重复行！")

    print("✅ 数据质量检查通过")
```

---

## 七、Token 管理机制（v2.5.0 新增）

### 7.1 Token 监控

**Director 职责**：
- 每个阶段结束后检查 Token 使用
- 当 Token 超过 80% 时发出警告
- 当 Token 超过 90% 时必须采取行动

### 7.2 行动策略

| Token 使用率 | 行动 |
|-------------|------|
| < 80% | 正常执行 |
| 80% - 90% | 发出警告，考虑压缩输出 |
| > 90% | **必须**：暂停并请求用户干预（轮换上下文或继续） |

**绝对禁止**：
- ❌ 擅自跳过阶段以节省 Token
- ❌ 生成"摘要版"报告以节省 Token
- ❌ 降低输出质量

### 7.3 检查点机制

**每个阶段结束时**：
1. 保存当前状态到 `output/.checkpoint_phase{i}.json`
2. 记录已完成的文件
3. 记录 manifest 状态

**检查点格式**：
```json
{
  "phase": 5,
  "completed_at": "2026-01-07 12:30:00",
  "outputs": [
    "output/implementation/data/results_1.csv"
  ],
  "manifest": "VERSION_MANIFEST.json 的快照"
}
```

---

## 八、用户决策优先原则

### 8.1 必须请求用户决策的场景

1. **Token 接近限制**（> 90%）
2. **遇到无法自行解决的问题**
3. **验证失败超过 3 次**
4. **需要在"质量"和"效率"之间权衡**

### 8.2 决策请求格式

```markdown
## 需要用户决策

**问题**：{描述问题}
**选项 A**：{选项 A 的描述和后果}
**选项 B**：{选项 B 的描述和后果}
**推荐**：{Director 的推荐和理由}

请用户选择 A 或 B，或提供其他指示。
```

---

## 九、与其他文档的关系

| 文档 | 内容 |
|------|------|
| `02_core.md`（本文档） | 核心规则和约定 |
| `03_workflow.md` | 执行流程（10 阶段） |
| `04_validation.md` | 验证机制 |
| `05_consultation.md` | 咨询机制 |
| `06_agents.md` | Agent 契约定义 |
| `07_anti_laziness.md` | 反偷懒机制 |

**阅读顺序**：本文档 → 03_workflow.md → 07_anti_laziness.md

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
