# v2.4.2 系统架构

> **权威架构定义** — 所有 Agent prompts 都应该从这份文档派生。
> **版本**: v2.4.2
> **日期**: 2026-01-05

---

## 文档关系

| 文档 | 职责 |
|------|------|
| `retrospective.md` | 分析 v2.4.1 的问题根源 |
| `methodology.md` | 定义设计原则和方法论 |
| **`architecture.md`（本文档）** | 定义具体架构和 Agent 契约 |

阅读顺序：retrospective → methodology → architecture

> ⚠️ **本文档是权威**。当 Agent prompt 与本文档冲突时，以本文档为准。

---

## 版本历史

| 版本 | 日期 | 关键变更 |
|------|------|----------|
| v2.4.0 | 2026-01-02 | 验证门机制、多 Agent 协作 |
| v2.4.1 | 2026-01-04 | 完整性强制令、数据完整性标准 |
| **v2.4.2** | **2026-01-05** | **返工重新验证、资源利用原则、质量门槛提升** |

---

## 一、文档说明

这份文档是 v2.4.2 的**具体架构定义**，包含：

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

### 2.4 数据完整性标准 (v2.4.1 New)

鉴于 v2.4.0 实验中出现的严重数据污染，v2.4.1 引入严格的数据完整性标准：
- **标量原则**：CSV/Excel 输出必须仅包含标量值 (int, float, string, boolean)。**绝对禁止**存储序列化对象（List, Dict, Numpy Object）。
- **类型安全**：生成数据的代码必须包含 `check_data_quality()` 函数，输出前断言数据类型。
- **自我修正**：Data Engineer 必须在提交前运行自检，发现非标量列立即修复。

### 2.5 完整性强制令 (Completeness Mandate) (v2.4.1 New)

鉴于 v2.4.0 实验中出现的"简化"错误，v2.4.1 确立以下绝对规则：
- **禁止简化 (No Simplification)**：系统必须严格执行 10 个阶段的所有步骤。
- **禁止跳过 (No Skipping)**：即使代码通过测试，Validation Gate 也必须完整执行。
- **质量优先 (Quality > Efficiency)**：当 Token 接近限制时，**暂停并请求用户干预**（如轮换上下文），绝不允许为了省 Token 而降低输出质量、合并步骤或生成"摘要版"报告。

### 2.6 返工必须重新验证 (Rework Must Revalidate) (v2.4.2 New)

鉴于 v2.4.1 实验中出现的"返工后跳过验证"错误，v2.4.2 确立以下规则：

- **强制重新验证**：如果 Validation Gate 返回 REJECTED，返工完成后**必须**重新触发同一 Gate
- **不得跳过**：Director 没有任何理由可以跳过重新验证（包括时间紧迫、Token 不足）
- **循环次数**：每个 Gate 最多循环 3 次（REJECTED → 返工 → 重新验证），超过后暂停请求用户干预

> ⚠️ **这是 v2.4.2 的核心改进**。v2.4.1 实验失败的主要原因就是返工后跳过了重新验证。

### 2.7 资源利用原则 (Resource Utilization Principles) (v2.4.2 New)

Agent 应当积极利用项目提供的资源，而非仅凭自身知识工作。

#### 2.7.1 参考文献资源

**目录**：`./reference_papers/`

**适用 Agent**：
- `researcher`：**强烈鼓励**浏览参考论文，学习相关领域的方法论和最佳实践
- `modeler`：参考类似问题的建模方法
- `summarizer`：学习高质量 MCM 论文的摘要写法和结构
- `writer`：参考论文的写作风格和组织方式

**原则**：
- ✅ 主动阅读和引用参考文献
- ✅ 从中汲取方法论灵感
- ✅ 引用时注明来源
- ❌ 不得直接复制内容

#### 2.7.2 LaTeX 模板资源

**目录**：`./latex_template/`

**适用 Agent**：`writer`

**强制规则**：

1. **禁止自创 LaTeX 文档**：
   - 必须将 `./latex_template/` 中的模板**复制**到 `output/paper/`
   - 在复制的模板基础上展开工作
   - ❌ 禁止从零创建新的 `.tex` 文件
   - ❌ 禁止修改模板的格式结构（如字体、页边距、章节样式）

2. **必须保证编译通过**：
   - 每次修改后必须尝试编译
   - 如果编译失败，首先检查是否是内容错误（自行修复）
   - 如果是**环境问题**（如字体缺失、包缺失）：
     - **必须通过 Consultation 协议请求 `feasibility_checker` 处理**
     - ❌ 禁止自行安装包或修改系统环境
     - ❌ 禁止使用 "no-font" 简化或其他绕过方案
     - ❌ 禁止降级模板要求

3. **文档长度要求**：
   - **最低 23 页**（不含附录）
   - 低于 23 页视为**不合格**，必须扩充内容
   - 验证者应检查页数，不足时返回 REJECTED

**检查清单**（writer 完成后自检）：
- [ ] 模板是从 `latex_template/` 复制的，不是自创的
- [ ] 编译通过，无错误
- [ ] 页数 >= 23 页
- [ ] 格式与原模板一致

#### 2.7.3 网络搜索

**适用 Agent**：`researcher`

**鼓励行为**：
- ✅ 搜索相关学术论文和方法
- ✅ 查找类似问题的解决方案
- ✅ 了解领域最新进展
- ❌ 不得依赖不可靠来源

### 2.8 质量门槛原则 (Quality Gate Principles) (v2.4.2 New)

Agent 应提高质量标准，严格拒绝不合格的产出。

#### 2.8.1 Modeler 严格标准

`modeler` 在 CODE Validation Gate 中应该：
- **严格审查**代码是否真正实现了设计的模型
- **拒绝**"能运行但不符合设计"的代码
- **拒绝**简化了核心数学逻辑的实现
- 发现严重偏差时，明确返回 REJECTED 并说明原因

> 不要因为"代码能跑"就放过质量问题。

#### 2.8.2 Advisor 独立验证（局外人视角）

> **核心原则**：你是"局外人"而非"参与者"。你不是这个团队的一员，你是来审查这个团队的。

**心态要求**：

1. **所有其他 Agent 都不可信**：
   - 不要相信 Director 的摘要
   - 不要相信 Validator 的"通过"报告
   - 不要相信任何 Agent 声称的数字
   - **假设这个比赛队伍可能有很多离谱的东西**

2. **以质疑者身份审查**：
   - 对每一个数据，问"这个数字对吗？"
   - 对每一个结论，问"真的是这样吗？"
   - **不要被漂亮的报告唬住**——报告写得再好，数据可能完全是错的

3. **独立验证**：
   - **亲自读取**预测文件（`predictions_*.csv`），不依赖任何人的汇报
   - **亲自检查**论文中的数字是否与文件一致
   - **亲自上网搜索**验证预测是否符合现实
     - 例如：搜索"USA Olympics 2024 medal count"，对比预测是否合理
     - 例如：搜索"host country Olympic advantage"，验证主办国效应方向

4. **常识 Sanity Check**：
   - 主办国预测应该高于往年，不是低于
   - 强国预测应该在历史范围附近，不应该暴跌 80%+
   - 预测区间的上界不应该小于均值

5. **与参考论文对比**：
   - **必须阅读几篇 `reference_papers/`** 中的论文
   - 对比本项目的论文质量与参考论文
   - 问自己：这份论文能和参考论文放在一起吗？
   - 如果差距太大，不要乐观，该 REJECT 就 REJECT

6. **极其严苛的高标准**：
   - **不要对拿到的东西过于乐观**——假设里面藏着问题
   - **敢于要求返工**——发现问题就 REJECT，不要"差不多就行"
   - **高标准高要求**——平庸的作品不值得高分
   - 宁可被认为苛刻，也不要让垃圾通过

**如果发现问题**：
- 立即降低评分（问题越多评分越低）
- 明确列出每个发现的问题
- 不要"为团队着想"而放过问题
- **敢于返回 REJECTED** 并要求修复

> ⚠️ **记住**：你的工作是找问题，不是找理由通过。一个诚实的 D 比一个虚假的 A+ 更有价值。

#### 2.8.3 Sanity Check 思维

所有 Agent 在验证时应具备 Sanity Check 思维：
- **常识判断**：预测结果是否符合常识？（如：主办国应该比平时表现更好）
- **历史对比**：与历史数据对比是否合理？
- **逻辑一致**：不同文件之间的数据是否一致？

### 2.9 输出一致性原则 (Output Consistency Principles) (v2.4.2 New)

鉴于 v2.4.1 实验中出现的数据不一致问题，v2.4.2 提醒所有 Agent：

- **唯一标识**：国家、变量等应使用统一的标识格式（NOC 代码或全名，不可混用）
- **避免覆盖**：不同模型/任务的输出应使用不同的文件名
- **验证日志-文件一致**：训练完成后，应检查日志中的关键数字与保存的文件内容一致

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

### 4.0 完整工作目录结构 (v2.4.2 New)

工作目录包含 output/ 以及多个**只读资源目录**，Agent 应充分利用这些资源。

```
workspace/2025_C/                 # 工作目录根
│
├── CLAUDE.md                     # Director Agent 系统提示词
├── .claude/                      # Agent 提示词目录
│   └── agents/                   # 各 Agent 的系统提示词
│       ├── reader.md
│       ├── researcher.md
│       ├── modeler.md
│       └── ...
│
├── 2025_MCM_Problem_C.pdf        # [只读] 原始问题 PDF
├── 2025_Problem_C_Data/          # [只读] 原始数据目录
│   └── *.csv                     # 提供的数据文件
├── 2025_Problem_C_Data.zip       # [只读] 数据压缩包
│
├── reference_papers/             # [只读] 参考论文目录
│   └── *.pdf                     # O-Prize 及其他优秀论文
│                                 # ** researcher, modeler, summarizer, advisor 应阅读 **
│
├── latex_template/               # [只读] LaTeX 模板目录
│   ├── mcmthesis.cls             # 模板类文件
│   ├── mcmthesis.tex             # 模板主文件
│   └── figures/                  # 模板图片
│                                 # ** writer 必须复制此模板到 output/paper/ **
│
└── output/                       # [可写] Agent 输出目录（见下文详细结构）
```

**资源使用指南**：

| 资源目录 | 权限 | 适用 Agent | 用途 |
|---------|------|-----------|------|
| `2025_MCM_Problem_C.pdf` | 只读 | reader | 提取问题需求 |
| `2025_Problem_C_Data/` | 只读 | data_engineer | 原始数据处理 |
| `reference_papers/` | 只读 | researcher, modeler, summarizer, advisor | 学习方法论、摘要写法、质量标准 |
| `latex_template/` | 只读 | writer | **必须复制到 output/paper/ 使用** |
| `output/` | 可写 | 所有 Agent | 输出所有产出物 |

---

### 4.1 output/ 输出目录结构

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
└── paper/                       # 论文相关
    ├── (从 latex_template/ 复制的模板文件)
    ├── paper_{i}.tex            # 论文源文件
    ├── paper_{i}.pdf            # 论文 PDF（必须 >= 23 页）
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

### 4.2 problem/ — 问题相关

#### 4.2.1 problem_full.md

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

### 6.1 Agent 概览 (Updated v2.4.2)

| Agent | 职责 | 核心变更 (v2.4.2) | 参与验证 |
|-------|------|------------------|---------|
| reader | 读取 PDF，提取需求 | - | MODEL, DATA, ... |
| **researcher** | 方法建议 | **[NEW] 鼓励搜索网络、浏览 `reference_papers/`** | MODEL |
| **modeler** | 设计数学模型 | **[NEW] 在 CODE Gate 严格拒绝低质量实现** | DATA, CODE, ... |
| feasibility_checker | 可行性检查 | - | MODEL, CODE |
| **data_engineer** | 数据处理 | 强制 Schema 验证；禁止非标量输出 | - |
| code_translator | 代码翻译 | - | CODE, TRAINING |
| model_trainer | 模型训练 | - | - |
| **validator** | 结果验证 | 需执行自动化预检查；**Sanity Check 思维** | DATA, TRAINING, ... |
| visualizer | 生成图表 | - | - |
| **writer** | 撰写论文 | **[NEW] 必须使用 `latex_template/`** | PAPER |
| **summarizer** | 创建摘要 | **[NEW] 参考 `reference_papers/` 学习摘要写法** | - |
| editor | 润色文档 | - | - |
| **advisor** | 质量评估 | **[NEW] 必须独立验证数据文件** | MODEL, PAPER, FINAL |

> **Director** 的职责增加：**返工后必须重新触发验证门**；Token 告警机制。


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

### 7.3 完整性检查清单 (v2.4.1 New)

Director 在每个 Phase 结束时必须确认：
1. [ ] 是否生成了该 Phase 定义的所有文件？
2. [ ] 是否执行了完整的 Validation Gate（包括所有验证者）？
3. [ ] 是否有任何步骤被"简化"或"跳过"？（如有，视为严重违规，必须回滚）

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

> **注**：原 v2.4.0 的外部设计文档已整合为本文档的附录。

| 文档 | 内容 | 位置 |
|------|------|------|
| `retrospective.md` | v2.0-v2.3 问题分析 | 独立文件 |
| `methodology.md` | 设计原则 | 独立文件 |
| `architecture.md` | 本文档 | **核心 + 附录** |
| `workflow_design` | 详细执行流程 | **附录 A** |
| `validation_design` | 验证机制详情 | **附录 B** |
| `consultation_design` | 咨询机制详情 | **附录 C** |
| `report_design` | 汇报机制详情 | **附录 D** |

================================================================================
# 附录内容
================================================================================

以下附录包含了 v2.4.0 的所有详细设计文档，并集成了 v2.4.1 的增强与修正。
作为 Director 和 Agent 的终极参考。


---

**文档版本**: v2.4.0  
**最后更新**: 2026-01-04
# MCM-Killer v2.4.0 工作流程设计

> **基于 architecture.md 1-5 节设计的完整执行流程**

---

## 一、核心原则

### 1.1 验证原则

1. **多人多视角验证**：每个 Stage 由多个 Agent 从不同角度验证
2. **返工不免验**：返工后的产出必须以**同样高标准**重新验证
3. **不允许放过**：验证者对返工结果不得降低标准
4. **独立判断**：验证时不允许发起 Consultation

### 1.2 返工原则

1. **明确问题**：验证报告必须明确指出问题和修复建议
2. **责任到人**：Director 指派具体 Agent 负责修复
3. **版本递增**：返工产生新版本文件
4. **循环验证**：返工后必须重新进入验证流程

> ⚠️ **对所有验证者的提醒**：返工后的结果依然需要以同样的高标准进行审查，不允许因为是"返工版本"就降低要求或自动通过。

---

## 二、阶段定义

### Phase 0: Problem Understanding（问题理解）

```
Director
    │
    ├─→ reader
    │   ├── 读取 PDF（使用 docling）
    │   ├── 生成 problem_full.md
    │   └── 生成 problem_requirements_1.md
    │
    └─→ researcher
        └── 生成 research_notes_1.md（方法建议）
```

**无验证门**（信息收集阶段）

---

### Phase 1: Model Design（模型设计）

```
Director
    │
    └─→ modeler
        └── 生成 model/model_design_1.md
```

#### Validation Gate: MODEL

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| reader | 模型能否解决题目要求？假设是否合理？ |
| feasibility_checker | 设备和时间约束下能否实现？ |
| advisor | 模型创新度是否足够？是否太水？ |
| researcher | 方法是否有理论支撑？ |

**判定规则**：
- 全部 APPROVED → 进入 Phase 2
- 任一 REJECTED → 返工

**返工流程**：
```
Director 收集所有 REJECTED 报告
    │
    └─→ modeler
        ├── 阅读所有验证报告
        ├── 修复问题
        └── 生成 model/model_design_2.md
        
    └─→ 重新触发 Validation Gate: MODEL
        （同样的验证者，同样的标准）
```

---

### Phase 2: Feasibility Check（可行性检查）

```
Director
    │
    └─→ feasibility_checker
        └── 生成 model/feasibility_1.md
```

**判定规则**：
- APPROVED → 进入 Phase 3
- NEEDS_REVISION → 返回 modeler 修改模型设计
- REJECTED → 返回 modeler 重新设计

---

### Phase 3: Data Processing（数据处理）

```
Director
    │
    └─→ data_engineer
        ├── 清洗数据
        ├── 生成 implementation/data/features_1.pkl
        └── 生成 implementation/data/features_1.csv
```

#### Validation Gate: DATA

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| modeler | 特征是否与 model_design 一致？ |
| validator | 数据是否合理？有无异常？ |
| reader | 数据处理是否符合题目约束？ |

**返工流程**：
```
任一 REJECTED
    │
    └─→ data_engineer
        ├── 阅读验证报告
        ├── 修复问题
        └── 生成 implementation/data/features_2.pkl
        
    └─→ 重新触发 Validation Gate: DATA
        （同样标准，不因返工降低要求）
```

---

### Phase 4: Code Translation（代码翻译）

```
Director
    │
    └─→ code_translator
        ├── 将数学模型翻译为代码
        ├── 生成 implementation/code/model_1.py
        └── 生成 implementation/code/test_1.py
```

#### Validation Gate: CODE

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| modeler | 代码是否严格实现了数学模型？ |
| code_translator | 代码语法/逻辑是否正确？ |
| feasibility_checker | 代码能否在当前环境运行？ |

**返工流程**：同上，重新验证使用同样标准。

---

### Phase 5: Model Training（模型训练）

```
Director
    │
    └─→ model_trainer
        ├── 训练/求解模型
        ├── 生成 implementation/data/results_1.csv
        └── 生成 implementation/logs/training_1.log
```

#### Validation Gate: TRAINING

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| modeler | 训练过程是否严格遵循模型设计？ |
| code_translator | 训练代码是否正确执行？ |
| validator | 结果是否合理？是否造假？符合常识？ |
| reader | 结果是否符合题目假设？Sanity check |

**特别注意**：这是最容易出问题的阶段，验证者必须严格检查：
- 结果是否在合理范围内
- 是否有明显的造假迹象
- 是否与模型设计的预期一致

---

### Phase 6: Visualization（可视化）

```
Director
    │
    └─→ visualizer
        ├── 生成图表
        ├── 生成 paper/figures/fig_*.png
        └── 更新 paper/figures/figure_index.md
```

**无单独验证门**（与 PAPER 一起验证）

---

### Phase 7: Paper Writing（论文撰写）

```
Director
    │
    └─→ writer
        └── 生成 paper/paper_1.tex
```

#### Validation Gate: PAPER

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| reader | 论文是否回答了所有题目要求？ |
| validator | 论文数据是否与 CSV 一致？ |
| advisor | 论文质量是否足够？与 O-Prize 差距？ |
| writer | 表达是否清晰？逻辑是否通顺？ |

**返工流程**：
```
任一 REJECTED
    │
    ├── 如果是数据不一致 → 可能需要回退到 Phase 5
    ├── 如果是表达问题 → writer 修复
    └── 如果是内容不足 → 可能需要回退到更早阶段
```

---

### Phase 8: Summary（摘要）

```
Director
    │
    └─→ summarizer
        └── 生成 paper/summary/summary_sheet_1.tex
```

#### Validation Gate: SUMMARY

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| validator | 摘要数据是否与论文一致？ |
| reader | 摘要是否准确概括解决方案？ |

**硬性要求**：编译后必须恰好 1 页

---

### Phase 9: Polish（润色）

```
Director
    │
    └─→ editor
        ├── 润色 paper.tex
        └── 润色 summary_sheet.tex
```

#### Validation Gate: FINAL

**参与者**：

| Agent | 验证问题 |
|-------|---------|
| validator | 全局一致性：paper = summary = CSV？ |
| advisor | 整体质量评估 |
| reader | 是否完全满足题目要求？ |

**最终检查清单**：
- [ ] 论文数据与 CSV 完全一致
- [ ] 摘要数据与论文完全一致
- [ ] 所有图表清晰可读
- [ ] 页数符合要求
- [ ] 格式符合 MCM 规范

---

### Phase 10: Final Review（最终审核）

```
Director
    │
    └─→ advisor
        └── 生成最终审核报告
```

**如果 advisor 发现重大问题**：返回相应阶段修复

---

## 三、验证机制总结

### 3.1 验证门列表

| Gate | 位置 | 参与者数量 | 返工目标 |
|------|------|-----------|---------|
| MODEL | Phase 1 后 | 4 | modeler |
| DATA | Phase 3 后 | 3 | data_engineer |
| CODE | Phase 4 后 | 3 | code_translator |
| TRAINING | Phase 5 后 | 4 | model_trainer 或回退 |
| PAPER | Phase 7 后 | 4 | writer 或回退 |
| SUMMARY | Phase 8 后 | 2 | summarizer |
| FINAL | Phase 9 后 | 3 | editor 或回退 |

### 3.2 返工计数器

Director 应追踪每个 Gate 的返工次数：

```json
{
  "rework_counts": {
    "MODEL": 0,
    "DATA": 0,
    "CODE": 0,
    "TRAINING": 0,
    "PAPER": 0,
    "SUMMARY": 0,
    "FINAL": 0
  },
  "max_rework_per_gate": 3
}
```

**如果返工次数超过 3 次**：
1. Director 发起全体讨论
2. 考虑是否需要回退到更早阶段
3. 或重新评估整体方案

---

## 四、返工流程详解

### 4.1 标准返工流程

```
Validation Gate 返回 REJECTED
    │
    ▼
Director 收集所有验证报告
    │
    ▼
Director 分析问题，确定责任 Agent
    │
    ▼
Director 调用责任 Agent，传入：
    - 所有 REJECTED 的验证报告
    - 明确的修复要求
    │
    ▼
责任 Agent 修复，生成新版本文件
    │
    ▼
重新触发 Validation Gate
    │
    ▼
所有验证者以同样标准重新验证
    │
    ├── 全部 APPROVED → 进入下一阶段
    └── 仍有 REJECTED → 继续返工
```

### 4.2 返工时的验证者提醒

每个验证者在收到返工版本时，会收到以下提醒：

```
[REWORK VALIDATION]

这是第 {N} 次返工后的产出。

⚠️ 重要提醒：
1. 请以同样的高标准进行审查
2. 不要因为是返工版本就降低要求
3. 不要假设之前的问题已经修复
4. 必须重新完整检查所有检查项
5. 如果发现新问题，必须指出

返工不等于免检，请严格执行验证职责。
```

### 4.3 回退机制

有些问题需要回退到更早阶段：

| 在 Gate | 发现问题 | 回退到 |
|---------|---------|--------|
| CODE | 模型设计有缺陷 | Phase 1 (modeler) |
| TRAINING | 特征不正确 | Phase 3 (data_engineer) |
| PAPER | 结果不合理 | Phase 5 (model_trainer) |
| FINAL | 模型方法论问题 | Phase 1 (modeler) |

**回退后**：从回退点开始，所有后续阶段都需要重新执行。

---

## 五、流程图

```
┌─────────────────────────────────────────────────────────────────────┐
│                         MCM-Killer Workflow                          │
└─────────────────────────────────────────────────────────────────────┘

Phase 0: Problem Understanding
    │
    ▼
Phase 1: Model Design ──────────────┐
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: MODEL   │ ─REJECTED─→ │ (返工)
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 2: Feasibility Check ─────────┘
    │
    ▼
Phase 3: Data Processing ───────────┐
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: DATA    │ ─REJECTED─→ │
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 4: Code Translation ──────────┤
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: CODE    │ ─REJECTED─→ │
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 5: Model Training ────────────┤
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: TRAINING│ ─REJECTED─→ │
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 6: Visualization              │
    │                               │
    ▼                               │
Phase 7: Paper Writing ─────────────┤
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: PAPER   │ ─REJECTED─→ │
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 8: Summary ───────────────────┤
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: SUMMARY │ ─REJECTED─→ │
└─────────────────────┘             │
    │ APPROVED                      │
    ▼                               │
Phase 9: Polish ────────────────────┤
    │                               │
    ▼                               │
┌─────────────────────┐             │
│ Validation: FINAL   │ ─REJECTED─→ ┘
└─────────────────────┘
    │ APPROVED
    ▼
Phase 10: Final Review
    │
    ▼
  DONE ✓
```

---

## 六、关键强调

### 6.1 对 Director 的要求

1. 严格执行所有 Validation Gate
2. 不允许跳过任何验证步骤
3. 返工后必须重新完整验证
4. 追踪返工次数，防止无限循环

### 6.2 对验证者的要求

1. **返工不免验**：返工版本必须以同样标准审查
2. **不降低要求**：不因时间压力或疲劳而放水
3. **独立判断**：不受其他验证者影响
4. **完整检查**：不假设问题已修复，重新检查所有项

### 6.3 对被验证者的要求

1. 认真阅读验证报告
2. 逐项解决指出的问题
3. 在返工报告中说明如何修复每个问题
4. 不隐瞒或回避问题

---

## 七、总结

**核心理念**：宁可多次返工，不可放过问题。

**质量公式**：
```
最终质量 = Σ(每个阶段的质量) × 验证严格度
```

只有在每个 Validation Gate 都保持高标准，才能确保最终产出的质量。
# Validation 机制设计（多人参与版）

> **核心理念**：Validation 是多视角检验，不同 Agent 从各自专业角度验证同一产出物。

---

## 一、核心原则

1. **多人参与**：每个 Validation 阶段由多个 Agent 从不同角度验证
2. **独立判断**：每个参与者**只能根据自己的知识判断**，不允许发起 Consultation
3. **并行验证**：多个 Agent 的验证可以并行进行（由 Director 调度）
4. **汇总决策**：Director 汇总所有验证报告，综合判断是否通过

---

## 二、Validation vs Consultation

| 方面 | Validation | Consultation |
|------|-----------|--------------|
| 目的 | 质量检查 | 信息获取 |
| 方向 | 多对一（多人验证一个产出） | 一对一 |
| 能否发起咨询 | ❌ 禁止 | ✅ 允许 |
| 能否使用工具 | ✅ 可以（运行代码、读文件等） | ✅ 可以 |
| 输出 | 验证报告（APPROVED/REJECTED） | 回复 |

---

## 三、Validation 参与者角色

每个 Agent 在 Validation 时有特定的**验证视角**：

| Agent | 验证视角 | 典型检查内容 |
|-------|---------|-------------|
| **reader** | 题意符合性 | 是否符合题目要求？假设是否合理？Sanity check |
| **researcher** | 方法论可行性 | 过去论文是否有类似方法？联网搜索可行性 |
| **modeler** | 模型设计一致性 | 实现是否严格遵循模型设计？ |
| **feasibility_checker** | 技术可行性 | 当前设备是否能运行？库是否可用？ |
| **advisor** | 创新度/质量 | 是否"太水"？创新度是否足够？与 O-Prize 差距？ |
| **code_translator** | 代码正确性 | 代码是否正确实现了要求？ |
| **validator** | 结果合理性 | 是否造假？结果是否符合常识？ |
| **data_engineer** | 数据质量 | 数据是否准确？特征是否正确？ |
| **writer** | 表达清晰性 | 论述是否清晰？逻辑是否通顺？ |

---

## 四、Validation 阶段定义

### Stage 1: MODEL（模型设计后）

**被验证对象**：`model/model_design_{i}.md`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| reader | 模型是否能解决题目要求的问题？假设是否合理？ |
| feasibility_checker | 当前设备和时间约束下是否能实现？ |
| advisor | 模型是否有足够创新度？是否太简单/太水？ |
| researcher | 方法是否有理论支撑？过去是否有类似成功案例？ |

---

### Stage 2: DATA（数据处理后）

**被验证对象**：`implementation/data/features_{i}.pkl`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 特征是否与模型设计中的要求一致？ |
| validator | 数据是否合理？有没有明显异常？ |
| reader | 数据处理是否符合题目约束（如不能用外部数据）？ |

---

### Stage 3: CODE（代码完成后）

**被验证对象**：`implementation/code/model_{i}.py`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 代码是否严格实现了数学模型？ |
| code_translator | 代码语法、逻辑是否正确？ |
| feasibility_checker | 代码是否能在当前环境运行？ |

---

### Stage 4: TRAINING（训练完成后）

**被验证对象**：`implementation/data/results_{i}.csv`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 训练过程是否严格遵循模型设计？ |
| code_translator | 训练代码是否正确执行？ |
| validator | 结果是否合理？有没有造假？是否符合常识？ |
| reader | 结果是否符合题目假设？Sanity check |

---

### Stage 5: PAPER（论文完成后）

**被验证对象**：`paper/paper_{i}.tex`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| reader | 论文是否回答了所有题目要求？ |
| validator | 论文中的数据是否与 CSV 一致？ |
| advisor | 论文质量是否足够？与 O-Prize 论文差距？ |
| writer | 表达是否清晰？逻辑是否通顺？ |

---

### Stage 6: SUMMARY（摘要完成后）

**被验证对象**：`paper/summary/summary_sheet_{i}.tex`

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| validator | 摘要数据是否与论文一致？ |
| reader | 摘要是否准确概括了解决方案？ |

---

### Stage 7: FINAL（最终检查）

**被验证对象**：所有文件

**参与者及职责**：

| 参与者 | 验证问题 |
|--------|---------|
| validator | 全局一致性：paper = summary = CSV |
| advisor | 整体质量评估 |
| reader | 是否完全满足题目要求 |

---

## 五、Validation 流程

```
Director 触发某 Stage 的 Validation
    │
    ├── 并行调用多个 Agent
    │   ├── Agent A 验证 → 写入 docs/validation/{stage}_{agent}_1.md
    │   ├── Agent B 验证 → 写入 docs/validation/{stage}_{agent}_1.md
    │   └── Agent C 验证 → 写入 docs/validation/{stage}_{agent}_1.md
    │
    ▼
Director 汇总所有验证报告
    │
    ├── 全部 APPROVED → 进入下一阶段
    ├── 有 CONDITIONAL → 记录问题，继续（需关注）
    └── 有 REJECTED → 返回修复，重新验证
```

---

## 六、验证报告格式

**路径**：`docs/validation/{i}_{stage}_{agent}.md`

> 每个参与者独立写一份报告。

```markdown
# Validation: {stage} by {agent} #{i}

| 字段 | 值 |
|------|------|
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
| 2 | {item} | ✅/⚠️/❌ | {note} |

---

## 问题列表（如有）

| # | 问题 | 严重程度 | 建议 |
|---|------|---------|------|
| 1 | {issue} | HIGH/MEDIUM/LOW | {suggestion} |

---

## 结论

{该 Agent 的验证结论}
```

---

## 七、目录结构更新

```
docs/
└── validation/
    ├── 1_model_reader.md           # 全局第 1 次验证
    ├── 2_model_feasibility_checker.md
    ├── 3_model_advisor.md
    ├── 4_model_researcher.md
    ├── 5_data_modeler.md           # 全局第 5 次验证
    ├── 6_data_validator.md
    ├── ...
```

---

## 八、与 Director 的通信

**验证者**（简洁）：
```
Director，已完成 {stage} 阶段验证，判定：{APPROVED/CONDITIONAL/REJECTED}，报告：docs/validation/{i}_{stage}_{agent}.md
```

---

## 九、禁止事项

在 Validation 阶段：

- ❌ **禁止发起 Consultation**（独立判断）
- ❌ 禁止修改被验证的文件
- ❌ 禁止编造检查结果

---

## 十、总结

**新设计的核心**：
1. **多人多视角**：每个 Stage 有多个 Agent 从不同角度验证
2. **独立判断**：不允许 Consultation，避免相互影响
3. **并行验证**：Director 可以并行调用多个验证者
4. **汇总决策**：Director 综合所有报告决定是否通过
5. **清晰职责**：每个 Agent 有明确的验证视角
# Consultation 机制设计（简化版）

> **核心前提**：系统是单线程的，同一时间只有一个 Agent 工作。

---

## 一、Consultation 的本质

**Consultation = Agent 在执行过程中向其他 Agent 寻求信息**

特点：
1. **同步阻塞**：发起咨询后，Director 立即处理，获得回复后才继续
2. **立即响应**：不存在"待处理"状态
3. **有记录**：所有咨询记录到 `consultation/` 目录

---

## 二、咨询流程

```
Agent A 工作中
    │
    ├── 遇到需要其他 Agent 知识的问题
    │
    ▼
Agent A: "Director，我需要咨询 @{agent_name}：{问题}"
    │
    ▼
Director 暂停 Agent A
    │
    ▼
Director 调用 Agent B，传入咨询问题
    │
    ▼
Agent B 回复
    │
    ▼
Director 将回复写入 consultation/{from}_{to}_{i}.md
    │
    ▼
Director 将回复传达给 Agent A
    │
    ▼
Agent A 继续工作
```

**就这么简单。**

---

## 三、咨询类型

只按"目的"分类，不按紧急程度（因为全部都是 blocking）：

| 类型 | 场景 | 示例 |
|------|------|------|
| **知识咨询** | 请求专业知识 | "Researcher，有哪些时序预测方法？" |
| **确认咨询** | 确认理解是否正确 | "Modeler，我理解的特征 X 这样定义对吗？" |
| **问题反馈** | 发现产出有问题 | "Writer，论文中这个数据与 CSV 不一致" |

---

## 四、咨询场景表

| 发起方 | 典型咨询对象 | 典型场景 |
|--------|------------|---------|
| reader | advisor | 问题理解不确定 |
| researcher | reader | 确认问题某个细节 |
| modeler | researcher | 方法选择 |
| modeler | data_engineer | 数据是否支持某特征 |
| data_engineer | modeler | 特征定义不清楚 |
| code_translator | modeler | 数学公式不清楚 |
| model_trainer | code_translator | 代码问题 |
| validator | 任何 Agent | 发现问题时反馈 |
| writer | visualizer | 需要特定图表 |
| writer | modeler | 模型解释 |

> 注：不做硬性限制，任何 Agent 都可以咨询任何其他 Agent，由 Director 判断是否合理。

---

## 五、咨询请求格式

Agent 发起咨询时：

```
Director，我需要咨询 @{agent_name}：

**问题**：{具体问题}
**背景**：{为什么需要问这个}（可选）
**我的理解**：{自己的初步判断}（可选）
```

---

## 六、咨询回复格式

被咨询的 Agent 回复时：

```
FROM @{agent_name}:

**回答**：{直接回答问题}
**补充说明**：{额外需要注意的点}（可选）
```

---

## 七、文件记录

### 7.1 目录结构

```
consultation/
└── {from}_{to}_{i}.md    # 咨询记录，i 为序号
```

不需要 pending/active/resolved，因为咨询是同步的，写入时已经完成。

### 7.2 文件格式

```markdown
# 咨询记录: {from_agent} → {to_agent} #{i}

| 字段 | 值 |
|------|------|
| 发起方 | {from_agent} |
| 接收方 | {to_agent} |
| 时间 | {timestamp} |

---

## 问题

{咨询的问题}

## 背景

{为什么需要问这个}

---

## 回复

{回复内容}

---

## 结果

{问题是否解决，发起方如何使用这个信息}
```

---

## 八、与 Validation 的关系

**Validation 不是 Consultation**：
- Validation 是**强制性质量检查**，有固定的 Gate 位置
- Consultation 是**可选的信息交换**，随时可能发生

但 Validation 可能**触发** Consultation：
- Validator 发现问题 → REJECTED
- 如果问题需要讨论，Validator 可以发起 Consultation 请求相关 Agent 澄清

---

## 九、简化后的章节结构

```
五、协作契约
├── 5.1 协作原则（单线程、所有咨询 blocking）
├── 5.2 咨询机制
│   ├── 5.2.1 咨询流程
│   ├── 5.2.2 咨询场景表
│   └── 5.2.3 咨询记录格式
├── 5.3 验证机制（原有的 Gate 定义）
└── 5.4 汇报机制（Agent → Director）
```

---

## 十、总结

**简化要点**：
1. ❌ 不需要异步状态管理
2. ❌ 不需要紧急程度分类
3. ❌ 不需要 pending/active/resolved 目录
4. ❌ 不需要 index.json
5. ✅ 简单的同步流程：发起 → Director 处理 → 回复 → 继续
6. ✅ 简单的文件记录：`{from}_{to}_{i}.md`

---

**待确认**：
1. 这个简化版本是否合适？
2. 是否保留"咨询场景表"作为参考（非强制）？
3. Validation 是否继续放在同一节？
# Report 机制设计

> **核心前提**：Report 是 Agent 向 Director 的单向汇报，每次调用完成后强制执行。

---

## 一、Report 的本质

**Report = Agent 向 Director 的工作汇报**

特点：
1. **单向**：Agent → Director，不期待回复
2. **强制**：每次 Agent 调用完成后必须汇报
3. **私密**：仅 Director 可见，其他 Agent 不可见
4. **追踪调用历史**：记录每个 Agent 被调用了多少次，每次做了什么

---

## 二、Report 的目的

1. **进度追踪**：Director 知道每个 Agent 完成了什么
2. **问题发现**：Agent 主动上报遇到的问题
3. **决策支持**：Agent 提供下一步建议
4. **审计记录**：事后可以回顾整个工作流程

---

## 三、汇报时机

| 时机 | 是否必须 | 说明 |
|------|---------|------|
| Agent 调用完成（正常） | ✅ 必须 | 无论成功失败都要汇报 |
| Agent 调用完成（失败） | ✅ 必须 | 汇报失败原因 |
| Agent 调用中途遇到阻塞 | ✅ 必须 | 先汇报问题，再发起 Consultation |

---

## 四、汇报内容

### 4.1 必须包含

| 字段 | 说明 |
|------|------|
| Agent 名称 | 谁在汇报 |
| 调用序号 | 第几次被调用 |
| 开始时间 | 调用开始的时间戳 |
| 结束时间 | 调用结束的时间戳 |
| 耗时 | 本次调用花了多长时间 |
| 状态 | SUCCESS / FAILED / PARTIAL |
| 任务摘要 | 一句话描述做了什么 |

### 4.2 可选包含

| 字段 | 说明 |
|------|------|
| 执行内容详情 | 具体做了哪些步骤 |
| 产出物列表 | 创建/修改了哪些文件 |
| 问题与风险 | 遇到的问题、不确定性 |
| 下一步建议 | 建议 Director 接下来做什么 |

---

## 五、汇报格式

```markdown
# Agent 汇报: {agent_name} #{i}

## 基本信息

| 字段 | 值 |
|------|------|
| Agent | {agent_name} |
| 调用序号 | {i} |
| 开始时间 | {YYYY-MM-DD HH:MM:SS} |
| 结束时间 | {YYYY-MM-DD HH:MM:SS} |
| 耗时 | {HH:MM:SS 或 X 分钟} |
| 状态 | ✅ SUCCESS / ❌ FAILED / ⚠️ PARTIAL |

---

## 任务摘要

{一句话描述本次调用的主要任务}

---

## 执行内容

1. {做了什么}
2. {做了什么}
3. ...

---

## 产出物

| 文件 | 路径 | 说明 |
|------|------|------|
| {name} | {path} | {description} |

---

## 问题与风险

{遇到的问题、不确定性、需要 Director 注意的事项}

（如无问题，写"无"）

---

## 下一步建议

{建议 Director 接下来调用哪个 Agent，或需要什么决策}
```

---

## 六、状态说明

| 状态 | 含义 | 典型场景 |
|------|------|---------|
| ✅ **SUCCESS** | 任务完成，产出符合预期 | 正常情况 |
| ❌ **FAILED** | 任务失败，无法完成 | 文件不存在、工具错误、无法解决的问题 |
| ⚠️ **PARTIAL** | 部分完成，有遗留问题 | 主要任务完成，但有小问题待处理 |

---

## 七、目录结构

```
docs/
└── report/
    ├── reader_1.md
    ├── reader_2.md         # reader 被调用了 2 次
    ├── researcher_1.md
    ├── modeler_1.md
    ├── modeler_2.md        # modeler 被调用了 2 次
    ├── data_engineer_1.md
    └── ...
```

命名格式：`{agent_name}_{i}.md`，`{i}` 为该 Agent 的第几次调用。

---

## 八、与其他机制的关系

### 8.1 Report vs Consultation

| 方面 | Report | Consultation |
|------|--------|--------------|
| 方向 | Agent → Director | Agent ↔ Agent（通过 Director） |
| 目的 | 汇报进度 | 寻求信息 |
| 期待回复 | 否 | 是 |
| 时机 | 任务完成后 | 任务中遇到问题 |

### 8.2 Report vs Validation

| 方面 | Report | Validation |
|------|--------|------------|
| 执行者 | 每个 Agent 自己 | Validator Agent |
| 内容 | 自己做了什么 | 检查别人做的对不对 |
| 时机 | 每次调用后 | 特定 Gate 位置 |

---

## 九、问题上报

Agent 在汇报中可以上报问题，触发 Director 决策：

### 9.1 问题类型

| 类型 | 格式 | Director 动作 |
|------|------|--------------|
| 阻塞性问题 | "遇到阻塞：{description}" | 必须解决才能继续 |
| 建议性问题 | "建议：{description}" | 可以忽略或处理 |
| 风险提示 | "风险：{description}" | 记录，后续关注 |

### 9.2 示例

```markdown
## 问题与风险

**阻塞性问题**：
- 数据文件 raw/train.csv 不存在，无法继续数据处理

**建议**：
- 特征 X 的缺失值较多（30%），建议与 modeler 讨论是否需要

**风险**：
- 训练数据量较小（仅 500 条），模型可能过拟合
```

---

## 十、总结

**Report 的核心特点**：
1. **单向**：Agent → Director
2. **强制**：每次调用后必须汇报
3. **私密**：仅 Director 可见
4. **结构化**：固定格式，便于追踪
5. **可包含问题上报**：阻塞/建议/风险
