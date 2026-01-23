# Part VI: File Mapping (Revised)

> **Directory Manifest，不是 Python 实现**
> **Core Principle**: 目录规范，不写路径检查代码
> **Philosophy**: 告诉 Claude 目录结构，不强制执行
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
Python 文件管理系统：

class FileManager:
    def check_path(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError
        if not self.validate_schema(path):
            raise SchemaError
        ...

class ContextManager:
    def sliding_window(self, context):
        if token_count > MAX_TOKENS:
            return prune_context(context)
        ...
```

**问题**：
- 重复造轮子
- Claude Code 原生就有这些能力
- 维护成本高

### 新范式（正确）

```
Directory Manifest：

User: "保持这个目录结构：
- docs/ 知识库
- reference/ 参考论文
- global_memory/ 历史经验
- artifacts/ 所有中间产物（文件名带时间戳）
- tools/ 工具脚本"

Claude Code 自动遵守
```

**优势**：
- 简单直接
- Claude Code 遵守自然语言指令
- 无需维护代码

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | Claude Code 替代方案 |
|------|--------|------|---------------------|
| **FileManager 类** | Python 文件操作 | 重复 | Read/Write 工具 |
| **ContextManager 类** | Token 计数、滑动窗口 | 不必要 | /compact 命令 |
| **SchemaValidator** | JSON schema 验证 | 过度 | Claude Code 智能推断 |
| **PathChecker** | 路径验证 | 不需要 | Claude Code 自动处理 |
| **DependencyResolver** | DAG 依赖解析 | 过度 | 自然语言告诉 Claude |
| **JSON 控制流** | tasks.json 驱动执行 | 不自然 | Prompt 指令 |

---

## 第二部分：Directory Manifest（最终版）

### 完整目录结构

```
workspace/
│
├── docs/                           # 知识库（主动注入）
│   ├── math_models_cheatsheet.md   # 数学模型速查表
│   ├── anti_patterns.md            # 反模式
│   ├── mcm_o_prize_style_guide.md  # O-Prize 风格指南
│   ├── optimization_strategies.md  # 优化策略
│   └── coding_best_practices.md    # 编码最佳实践
│
├── global_memory/                  # Session 间记忆
│   └── lessons_learned.md          # 经验教训
│
├── reference/                      # 参考论文（One-Shot 学习）
│   └── best_paper_example/
│       ├── README.md
│       ├── 2023_C_OPrize.pdf
│       ├── 2023_C_OPrize.tex
│       ├── figures/
│       ├── code/
│       └── style_extraction/
│
├── tools/                          # 工具脚本（6 个）
│   ├── arena.py                    # 模型对比
│   ├── validate_statistics.py      # 统计检验
│   ├── validate_sensitivity.py     # 灵敏度分析
│   ├── journal_helper.py           # 研究日记
│   ├── latex_builder.py            # LaTeX 编译
│   └── chart_generator.py          # 图表生成
│
├── artifacts/                      # **所有中间产物**
│   ├── code/                      # 生成的代码（时间戳文件名）
│   ├── figures/                   # 图表（时间戳文件名）
│   ├── models/                    # 模型对象（时间戳文件名）
│   ├── data/                      # 处理后的数据（时间戳文件名）
│   ├── results/                   # 结果 JSON/CSV（时间戳文件名）
│   ├── validation/                # 验证报告（时间戳文件名）
│   └── paper/                     # LaTeX 和 PDF（时间戳文件名）
│
├── data/                           # 只读数据
│   └── 2025_Problem_C/
│       ├── 2025_Problem_C.pdf
│       └── summerOly_medal_counts.csv
│
└── current_status.md               # 任务状态（由 Claude 维护）
```

**总计**：~15 个文件 + 工具脚本 + artifacts/

---

## 第三部分：关键规范

### 1. docs/ 知识库

**用途**：存储所有领域知识

**规范**：
- ✅ 所有文档都是 Markdown
- ✅ Session 启动时主动读取
- ✅ Claude Code 内化为上下文
- ❌ 不用 Python 查询

**文件列表**：
```
docs/
├── math_models_cheatsheet.md       # ~2000 行，98+ 方法
├── anti_patterns.md                # ~500 行，常见错误
├── mcm_o_prize_style_guide.md      # ~1000 行，写作标准
├── optimization_strategies.md      # ~500 行，优化方法
└── coding_best_practices.md        # ~500 行，编码规范
```

### 2. global_memory/ 历史记忆

**用途**：Session 间记忆，避免重复错误

**规范**：
- ✅ 使用追加模式（Append）
- ✅ 每次任务结束后复盘
- ✅ 下次 Session 启动时读取
- ❌ 不删除或修改历史条目

**文件格式**：
```markdown
# Lessons Learned

## [2026-01-23] - 任务名
### 错误
[具体描述]

### 根因
[深入分析]

### 解决
[代码级别]

### 预防
**Claude Code，今后...**
```

### 3. reference/ 参考论文

**用途**：One-Shot 学习完整 O-Prize 论文

**规范**：
- ✅ 选择 1 篇最佳论文
- ✅ 包含 PDF + LaTeX 源码
- ✅ 手动提取风格要素
- ❌ 不自动分析多篇论文

**目录结构**：
```
reference/best_paper_example/
├── README.md                       # 论文说明
├── 2023_C_OPrize.pdf               # 完整 PDF
├── 2023_C_OPrize.tex               # LaTeX 源码
├── figures/                        # 所有图表（提取）
├── code/                           # 代码片段（提取）
└── style_extraction/               # 风格要素（手动提取）
    ├── structure.md                # 论文结构
    ├── color_palette.md            # 配色方案
    └── latex_packages.md           # LaTeX 宏包
```

### 4. tools/ 工具脚本

**用途**：可重用的 Python 工具

**规范**：
- ✅ 所有工具接受命令行参数
- ✅ 输出 JSON 格式（便于 Claude Code 读取）
- ✅ 有清晰的 --help 说明
- ❌ 不用 Python 包装器调用

**文件列表**：
```
tools/
├── arena.py                        # 模型对比
├── validate_statistics.py          # 统计检验
├── validate_sensitivity.py         # 灵敏度分析
├── journal_helper.py               # 研究日记
├── latex_builder.py                # LaTeX 编译
└── chart_generator.py              # 图表生成
```

**工具调用示例**：
```bash
# ❌ 错误：Python 包装器
subprocess.run(["python", "tools/arena.py", "--model", "ZINB"])

# ✅ 正确：自然语言指令
"使用 tools/arena.py 训练 ZINB 模型"
# Claude Code 自动转换为：
python tools/arena.py --model ZINB --input features.csv --output results.json
```

### 5. artifacts/ 中间产物

**用途**：所有生成的文件

**关键规范**：**文件名必须带时间戳**

**原因**：防止覆盖，保留历史版本

**正确示例**：
```
artifacts/figures/20260123_medal_counts.png
artifacts/models/20260123_zinb_model.pkl
artifacts/results/20260123_predictions.csv
artifacts/validation/20260123_statistical_tests.json
```

**错误示例**：
```
artifacts/figures/medal_counts.png          # ❌ 会被覆盖
artifacts/models/zinb_model.pkl             # ❌ 会被覆盖
```

**目录结构**：
```
artifacts/
├── code/                           # 生成的代码
│   └── 20260123_data_processing.py
├── figures/                        # 图表（PNG，300 DPI）
│   ├── 20260123_fig1_flowchart.png
│   ├── 20260123_fig2_data.png
│   └── 20260123_fig3_sensitivity.png
├── models/                         # 模型对象（PKL）
│   └── 20260123_zinb_model.pkl
├── data/                           # 处理后的数据（CSV）
│   ├── 20260123_features.csv
│   └── 20260123_clean_data.csv
├── results/                        # 结果（JSON/CSV）
│   ├── 20260123_predictions.csv
│   └── 20260123_arena_results.json
├── validation/                     # 验证报告（JSON）
│   ├── 20260123_statistical_tests.json
│   └── 20260123_sensitivity_report.json
└── paper/                          # LaTeX 和 PDF
    ├── 20260123_paper.tex
    ├── 20260123_paper.pdf
    └── references.bib
```

### 6. data/ 只读数据

**用途**：原始数据（只读）

**规范**：
- ✅ 只读，不修改
- ✅ 处理后的数据存 artifacts/data/
- ❌ 不在 data/ 目录下生成新文件

```
data/
└── 2025_Problem_C/
    ├── 2025_Problem_C.pdf
    └── summerOly_medal_counts.csv
```

### 7. current_status.md 任务状态

**用途**：跟踪任务进度

**维护者**：Claude Code

**格式**：
```markdown
# 当前任务状态

## 任务信息
- **问题**: 2025_C (Olympic medal prediction)
- **开始时间**: 2026-01-23 14:00
- **当前阶段**: Phase 3: 批评家模式（验证）

## 已完成
- [x] Phase 1: 科学家模式（问题分析）
- [x] Phase 2: 工程师模式（数据处理）
- [x] Phase 2: 工程师模式（模型训练）
- [ ] Phase 3: 批评家模式（验证）← 当前
- [ ] Phase 4: 作家模式（撰写论文）

## 当前状态
- **验证进度**: 2/3 检验通过
- **通过**: Shapiro-Wilk, Durbin-Watson
- **待检查**: Breusch-Pagan

## 遇到的问题
- [已解决] 日期格式问题（使用 pd.to_datetime(errors='coerce')）
- [已解决] BOM 字符问题（使用 encoding='utf-8-sig'）

## 下一步
- 运行 Breusch-Pagan 检验
- 如果通过，进入 Phase 4
- 如果不通过，参考 docs/optimization_strategies.md
```

---

## 第四部分：使用协议

### Session 启动（告诉 Claude 目录结构）

```markdown
# Session 启动指令

Claude Code，请执行以下初始化：

## 目录结构

我们的项目使用以下目录结构：

```
workspace/
├── docs/                    # 知识库（请阅读所有文档）
├── global_memory/           # 历史经验（请阅读）
├── reference/               # 参考论文（请学习）
├── tools/                   # 工具脚本（6 个）
├── artifacts/               # **所有中间产物必须存这里**
├── data/                   # 只读数据（不修改）
└── current_status.md        # 任务状态（你维护）
```

## 关键规范

1. **artifacts/ 规范**：
   - 所有中间产物存 artifacts/
   - **文件名必须带时间戳**（防止覆盖）
   - 示例：`20260123_predictions.csv`

2. **data/ 规范**：
   - 只读，不修改
   - 处理后的数据存 artifacts/data/

3. **current_status.md 规范**：
   - 由你维护
   - 每完成一个阶段，更新状态
   - 记录遇到的问题和解决方案

## 初始化任务

1. **读取知识库**：
   ```
   Read: docs/*.md
   ```

2. **读取历史经验**：
   ```
   Read: global_memory/lessons_learned.md
   ```

3. **学习参考论文**：
   ```
   Read: reference/best_paper_example/README.md
   ```

4. **确认理解**：
   - 你记住了哪些目录规范？
   - 你会在哪里存储中间产物？
   - 你会使用什么文件名格式？

确认后，开始执行任务。
```

### 任务执行中的指令

```markdown
# 任务执行指令

Claude Code，现在开始执行 2025_C 任务：

## Phase 1: 科学家模式

**指令**：
"分析问题并设计模型：
1. 读取 data/2025_Problem_C/2025_Problem_C.pdf
2. 参考 docs/math_models_cheatsheet.md
3. 选择 2-3 个候选模型
4. 输出到：current_status.md"

**注意**：
- 所有读取操作使用 data/ 下的原始数据
- 不要修改 data/ 下的文件

---

## Phase 2: 工程师模式

**指令**：
"实现模型：
1. 加载数据：data/2025_Problem_C/summerOly_medal_counts.csv
2. 处理数据（使用 BOM-safe 加载）
3. 保存特征到：artifacts/data/20260123_features.csv
4. 训练模型，保存到：artifacts/models/20260123_zinb_model.pkl
5. 保存预测到：artifacts/results/20260123_predictions.csv

**关键**：
- 所有输出必须存 artifacts/
- 文件名必须带时间戳
- 更新 current_status.md"

---

## Phase 3: 批评家模式

**指令**：
"验证模型：
1. 使用 tools/validate_statistics.py
2. 保存报告到：artifacts/validation/20260123_statistical_tests.json
3. 如果通过，继续
4. 如果不通过，参考 docs/optimization_strategies.md
5. 更新 current_status.md"

---

## Phase 4: 作家模式

**指令**：
"撰写论文：
1. 参考 reference/best_paper_example/ 的风格
2. 生成图表到：artifacts/figures/20260123_*.png
3. 撰写 LaTeX 到：artifacts/paper/20260123_paper.tex
4. 编译 PDF 到：artifacts/paper/20260123_paper.pdf
5. 更新 current_status.md"
```

---

## 第五部分：与原计划的对比

### 文件管理对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **文件操作** | FileManager, ContextManager 类 | Claude Code 原生工具 |
| **路径检查** | Python 代码验证 | 自然语言告诉 Claude |
| **依赖解析** | Python DAG | 自然语言告诉 Claude |
| **上下文管理** | Token 计数、滑动窗口 | /compact 命令 |
| **Schema 验证** | JSON schema 检查 | Claude Code 智能推断 |
| **输出规范** | 复杂的命名规则 | 时间戳文件名 |
| **状态跟踪** | task_status.json | current_status.md |

### 核心改变

1. **从"代码管理"到"规范管理"**
   - 不写 Python 代码管理文件
   - 用自然语言告诉 Claude 规范

2. **从"强制执行"到"信任遵守"**
   - 不强制路径检查
   - 信任 Claude Code 遵守指令

3. **从"复杂"到"简单"**
   - 时间戳文件名即可
   - 不需要复杂的命名系统

---

## 快速开始

### 初始化目录

```bash
# 1. 创建目录结构
mkdir -p docs global_memory reference/best_paper_example/{figures,code,style_extraction}
mkdir -p tools artifacts/{code,figures,models,data,results,validation,paper} data/2025_Problem_C

# 2. 初始化文件
echo "# Current Status\n\n" > current_status.md
echo "# Lessons Learned\n\n" > global_memory/lessons_learned.md

# 3. 复制工具脚本
cp path/to/tools/*.py tools/

# 4. 准备数据
cp path/to/2025_Problem_C.pdf data/2025_Problem_C/
cp path/to/summerOly_medal_counts.csv data/2025_Problem_C/

# 5. 准备参考论文
cp path/to/2023_C_OPrize.pdf reference/best_paper_example/
cp path/to/2023_C_OPrize.tex reference/best_paper_example/

# 6. 完成
echo "目录结构已创建，共 8 个目录"
ls -R
```

---

**版本**: Revised
**核心理念**: Directory Manifest，不写 Python 管理
**关键**: 告诉 Claude 规范，时间戳文件名，简单目录结构

---

**END OF 06_FILE_MAPPING_REVISED.md**
