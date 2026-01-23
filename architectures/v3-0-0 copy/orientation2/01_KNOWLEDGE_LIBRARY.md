# Part I: Knowledge Library Architecture (Revised)

> **AI Native Knowledge Injection, Not Retrieval**
> **Core Principle**: 主动注入 (Active Injection) > 被动检索 (Passive Query)
> **Source**: MM-Agent HMML + Enhanced with Anti-Patterns
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
知识库 = 向量数据库 + 嵌入检索

User: "我需要预测模型"
  ↓
Python: Query vector DB → Return top-k
  ↓
Agent: Read results → Apply
```

### 新范式（正确）

```
知识库 = Markdown 文件 + 主动注入

Session 启动:
User: "请阅读 docs/*.md 作为你的领域知识背景"
  ↓
Claude Code: 读取所有知识文档 → 内化为上下文
  ↓
User: "现在开始解决问题"
  ↓
Claude Code: 自动应用已读取的知识
```

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | 替代方案 |
|------|--------|------|----------|
| **向量数据库** | Embedding + Similarity Search | Claude 更聪明 | 主动读取 MD 文件 |
| **嵌入检索** | Query → Top-K Results | 不必要复杂 | 直接告诉 Claude 读哪些文件 |
| **知识索引** | JSON catalog | MD 文件名即索引 | Glob 工具: `docs/**/*.md` |
| **动态查询** | Python query logic | 自然语言更直接 | "Read X, Y, Z files" |

---

## 第二部分：知识库结构（极简）

### Directory Manifest

```
docs/                         # 所有知识库（扁平结构，不嵌套）
├── math_models_cheatsheet.md
├── anti_patterns.md
├── mcm_o_prize_style_guide.md
├── optimization_strategies.md
└── coding_best_practices.md

reference/                    # 参考论文（完整范例）
└── best_paper_example/
    ├── 2023_C_OPrize.pdf
    ├── 2023_C_OPrize.tex
    ├── figures/
    └── README.md

global_memory/                # Session 间记忆
└── lessons_learned.md
```

**关键规范**：
- ✅ **要**在 Session 启动时告诉 Claude："请阅读 docs/ 下的所有文档"
- ❌ **不要**写 Python 代码去"查询"知识库
- ✅ **要**信任 Claude Code 会记住已读取的内容
- ❌ **不要**用向量数据库或嵌入检索

---

## 第三部分：核心资产（Must Keep）

### 1. 数学模型速查表 (math_models_cheatsheet.md)

**来源**：MM-Agent HMML (162KB) → 简化为 MD

**新增内容**：
```markdown
# 数学模型速查表

## 如何使用本文档

Claude Code，当你接到问题时：
1. 阅读本文档
2. 根据问题类型匹配模型
3. 选择 2-3 个候选模型
4. 对比优缺点

---

## 预测模型 (Prediction Models)

### ZINB (Zero-Inflated Negative Binomial)
**适用场景**：
- 数据特征：计数数据 + 过多零值 (zero inflation > 30%)
- 样本量：n > 50
- O-Prize 先例：2023 Problem C (medal prediction)

**数学公式**：
$$
P(Y=y) = \begin{cases}
\pi + (1-\pi) \times f_{NB}(0) & \text{if } y=0 \\
(1-\pi) \times f_{NB}(y) & \text{if } y>0
\end{cases}
$$

**Python 实现**：
- 库：`statsmodels` (ZeroInflatedNegativeBinomialP)
- 参数：`exog_infl` (zero-inflation component)

**验证要求**：
- [ ] VIF < 5 (no multicollinearity)
- [ ] Overdispersion test (p < 0.05)
- [ ] Vuong test (vs Poisson)

**常见错误**：
❌ 对小样本 (n<30) 使用 ZINB → 过拟合
✅ 使用简单模型 + 强正则化

---

### ARIMA (AutoRegressive Integrated Moving Average)
**适用场景**：
- 数据特征：时间序列，趋势性
- 样本量：n > 40
- O-Prize 先例：2019 Problem A

[... 其他 96 个方法 ...]
```

### 2. 反模式 (anti_patterns.md) - **NEW**

**来源**：基于 MM-Agent 的常见错误 + O-Prize 评审标准

```markdown
# MCM 竞赛反模式

> **比"做什么"更重要的是"不做什么"**

## 数据分析反模式

❌ **错误**: 对小样本数据（n<50）使用深度神经网络
- **原因**: 过拟合，无法泛化
- **替代**: 使用简单模型（逻辑回归、决策树）+ 强正则化
- **参考**: 2019 Problem B M-Prize 论文

❌ **错误**: 直接用均值填充缺失值
- **原因**: 引入偏差，破坏数据分布
- **替代**: MICE 多重插补 或 KNN
- **参考**: 统计学最佳实践

❌ **错误**: 忽略时间序列的平稳性检验
- **原因**: 虚假回归，模型无效
- **替代**: ADF 检验，差分处理
- **参考**: 计量经济学标准流程

## 模型选择反模式

❌ **错误**: "随机森林最准确，就用它"
- **原因**: 缺乏理论依据，评委质疑
- **替代**: 必须对比 2-3 个模型，说明选择理由
- **参考**: 所有 O-Prize 论文都有模型对比表

❌ **错误**: 只报告最好的结果
- **原因**: 隐瞒失败实验，学术不端
- **替代**: 报告所有尝试的模型，包括失败的
- **参考**: O-Prize 诚信标准

## 写作反模式

❌ **错误**: "图1显示了X与Y的关系"
- **原因**: 没有洞察，只是描述
- **替代**: "图1显示...这表明...（Implication）"
- **参考**: O-Prize 观察洞察模式

❌ **错误**: 没有灵敏度分析
- **原因**: 模型鲁棒性未知，无法信任
- **替代**: 必须包含龙卷风图或参数扰动分析
- **参考**: O-Prize 100% 都有灵敏度分析
```

### 3. O-Prize 风格指南 (mcm_o_prize_style_guide.md)

**来源**：从 44 篇 O-Prize 论文中提取的模式

```markdown
# O-Prize 风格指南

## 摘要标准

### 长度
- 目标：250 词
- 范围：200-300 词

### 必需组件
1. **问题背景** (1 句话)
2. **方法** (2-3 句话) - 必须具体命名技术
3. **结果** (2-3 句话) - 必须包含数字
4. **结论** (1 句话)

❌ **错误**: "Our model achieves good results."
✅ **正确**: "Our model achieves RMSE of 4.2 medals (95% CI: [3.1, 5.3])."

## 图表标准

### 必需图表
- **方法流程图**: 必需 (68% 的 O-Prize 论文)
- **数据可视化**: 折线图、散点图
- **验证**: 残差图、QQ 图
- **灵敏度**: 龙卷风图 (92% 的 O-Prize 论文)

### 标题风格
格式: [描述] + [洞察] + [统计]

❌ **错误**: "Figure 1: Medal counts over time"

✅ **正确**: "Figure 1: Historical medal counts (1896-2024) showing exponential growth phase post-1980, with anomalies during boycott years. Shaded region represents 95% CI from ZINB model."

## 统计检验标准

### 必需检验（按问题类型）

**预测/回归**:
- Shapiro-Wilk (正态性)
- Durbin-Watson (自相关)
- Breusch-Pagan (同方差性)

**时间序列**:
- ADF 检验 (平稳性)
- Ljung-Box (残差自相关)

### 报告格式
❌ **错误**: "The model passed all statistical tests."

✅ **正确**: "Residual analysis reveals satisfied assumptions (Table 4). Shapiro-Wilk test fails to reject normality (W=0.98, p=0.23). Durbin-Watson statistic (DW=1.87) suggests no significant autocorrelation. Breusch-Pagan test (p=0.36) confirms homoscedasticity."
```

### 4. Session 间记忆 (global_memory/lessons_learned.md) - **NEW**

```markdown
# 经验教训 (Lessons Learned)

> **Session 间记忆，避免重复错误**

---

## [2026-01-20] - 2025_Problem_C

### 错误
在处理日期格式时，使用了 `pd.to_datetime()` 而未指定 `errors='coerce'`，导致遇到无效日期时整个流程崩溃。

### 根因
奥运数据中存在异常日期格式（如 "1896-04-01 to 1896-04-15"），默认的 `errors='raise'` 模式会抛出异常。

### 解决方案
```python
# 修改前
df['date'] = pd.to_datetime(df['date'])

# 修改后
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

### 预防措施
**Claude Code，今后处理任何日期数据时**：
- 必须使用 `pd.to_datetime(..., errors='coerce')`
- 处理后检查 `df['date'].isna().sum()`
- 记录异常日期的数量和原因

---

## [2026-01-18] - Model Training

### 错误
ZINB 模型在 50 个国家的小数据集上训练失败（收敛问题）。

### 根因
样本量不足（n=50），但 ZINB 参数过多导致过拟合。

### 解决方案
改用简单 Poisson 回归 + L2 正则化。

### 预防措施
**Claude Code，今后选择模型时**：
- 如果 n < 100，优先选择简单模型（线性/逻辑回归）
- 参考 `docs/math_models_cheatsheet.md` 中的"适用场景"
- 如果必须用复杂模型，必须加强正则化
```

---

## 第四部分：One-Shot 学习（完整范例）

### 参考论文目录结构

```
reference/best_paper_example/
├── 2023_C_OPrize.pdf           # 完整 PDF
├── 2023_C_OPrize.tex           # LaTeX 源码
├── figures/                    # 所有图表（提取）
│   ├── fig1_flowchart.png
│   ├── fig2_data.png
│   └── fig3_sensitivity.png
├── code/                       # 代码片段（提取）
│   ├── zinb_model.py
│   └── sensitivity_analysis.py
└── README.md
```

### One-Shot 学习指令

```markdown
# 参考论文学习指令

**Claude Code，请执行以下学习**：

1. **阅读完整论文** (`reference/best_paper_example/2023_C_OPrize.pdf`)
   - 注意论文结构（IMRaD）
   - 注意图表类型和数量
   - 注意数学公式的写法

2. **阅读 LaTeX 源码** (`2023_C_OPrize.tex`)
   - 学习 LaTeX 宏包使用
   - 学习图表排版
   - 学习公式编号和引用

3. **复制风格特征**：
   - 目录结构（目录、章节编号）
   - 图表配色（提取 RGB 值）
   - TikZ 绘图代码（如果有）
   - 参考文献格式

4. **应用到当前问题**：
   我要与之 **1:1 的专业度**。
```

---

## 第五部分：使用协议

### Session 启动（Bootstrap）

```markdown
# 初始化指令

Claude Code，请执行以下初始化：

1. **读取知识库**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: docs/mcm_o_prize_style_guide.md
   - Read: docs/optimization_strategies.md

2. **确认理解**：
   - 回答：你理解了哪些反模式？
   - 回答：你记住了哪些必需的统计检验？

3. **读取历史经验**：
   - Read: global_memory/lessons_learned.md
   - 确认：本次任务中严格避免重复历史错误

4. **准备参考论文**：
   - Read: reference/best_paper_example/README.md
   - 目标：学习 O-Prize 论文的完整风格

确认后，开始执行任务。
```

### 知识应用（自动）

```markdown
# 任务执行指令

Claude Code，现在开始解决问题：

**要求**：
1. 应用已读取的知识（无需再读取）
2. 避免反模式中的错误
3. 遵循 O-Prize 风格标准
4. 如果遇到历史错误，自动修正

**执行**：
[你的问题描述]
```

### Session 结束（复盘）

```markdown
# 复盘指令

Claude Code，任务完成，请执行复盘：

1. **总结关键错误**：
   - 本次任务中出现了哪些 Critical Errors？
   - 根因是什么？

2. **提炼经验教训**：
   - 格式：错误 → 根因 → 解决 → 预防
   - 具体到代码级别

3. **追加记忆**：
   - Append: global_memory/lessons_learned.md
   - 格式参见现有条目

4. **验证记忆**：
   - 下次 session 启动时会自动读取
   - 确保不会重复错误
```

---

## 第六部分：与原计划的对比

### 知识库对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **存储格式** | 300+ 分散 MD 文件 | 5 个核心 MD 文件 |
| **检索方式** | 向量数据库查询 | Session 启动时主动读取 |
| **HMML** | 98 个独立文件 | 1 个速查表 |
| **新增** | - | 反模式（anti_patterns.md） |
| **新增** | - | Session 间记忆（lessons_learned.md） |
| **参考论文** | 提取模式 | 完整范例（One-Shot 学习） |
| **Python 代码** | 索引、查询脚本 | 无 |

### 核心改变

1. **从"检索"到"记忆"**
   - 不查询向量数据库
   - Session 启动时读取，Claude Code 内化为上下文

2. **从"分散"到"集中"**
   - 300+ 文件 → 5 个核心文件
   - 易于维护，易于理解

3. **从"自动"到"人工审核"**
   - 不自动分析报告
   - 复盘指令 + 人工审核后追加记忆

---

## 快速开始

### 10 分钟设置

```bash
# 1. 创建目录
mkdir -p docs reference/best_paper_example global_memory

# 2. 准备知识库（从 MM-Agent 提取）
# - 将 HMML 转为 docs/math_models_cheatsheet.md
# - 创建 docs/anti_patterns.md（参见本文档）

# 3. 准备参考论文
# - 复制一篇 O-Prize 论文到 reference/best_paper_example/

# 4. 初始化全局记忆
echo "# Lessons Learned\n\n" > global_memory/lessons_learned.md

# 5. 启动 Claude Code
cd workspace
claude
```

### 第一次交互

```markdown
Claude Code，请：

1. 阅读 docs/ 下的所有文档
2. 确认理解了：
   - MCM 竞赛的基本规则
   - 常见的反模式（Anti-Patterns）
   - O-Prize 论文的标准风格
3. 为 2025_C 问题创建 execution_plan.md
```

---

**版本**: Revised
**核心理念**: 主动注入，被动检索
**关键**: 不写 Python 查询代码，写 Markdown 知识文件；Session 启动时读取，Claude Code 自动记忆

---

**END OF 01_KNOWLEDGE_LIBRARY_REVISED.md**
