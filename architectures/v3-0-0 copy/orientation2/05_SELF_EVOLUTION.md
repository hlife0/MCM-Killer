# Part V: Self-Evolution System (Revised)

> **Session 间记忆，不是自动进化**
> **Core Principle**: 复盘 + 人工审核，不是自动分析
> **Philosophy**: 从错误中学习，不是自动优化
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
自动进化系统：

Python 脚本分析 MMBench 报告 → 识别弱点 → 自动更新 Agent Prompts
- auto_evolution.py 扫描 benchmarks/run_*.json
- 找到 recurring issues
- 自动修改 .claude/agents/*.md
- 自动测试新 Prompts
```

**问题**：
- 过于自动化，容易出错
- 缺乏人工审核
- 可能引入新错误

### 新范式（正确）

```
Session 间记忆 + 人工审核：

Session 结束 → Claude Code 复盘 → 提炼经验教训 → 追加到 lessons_learned.md
↓
User 审核 → 确认无误 → 下次 Session 自动读取
↓
Claude Code 严格避免重复历史错误
```

**优势**：
- 人工审核，质量保证
- 具体到代码级别
- 简单有效

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | 替代方案 |
|------|--------|------|----------|
| **自动分析脚本** | auto_evolution.py | 过度自动化 | 人工复盘 |
| **MMBench 评估** | 111 问题自动测试 | 太重了 | Session 内验证 |
| **自动 Prompt 更新** | 修改 .claude/agents/*.md | 容易出错 | 人工更新 |
| **评分系统** | 复杂的评分 JSON | 不必要 | 人工判断 |
| **进化日志** | evolution_log.md | 太复杂 | lessons_learned.md |

---

## 第二部分：Session 间记忆系统

### global_memory/lessons_learned.md

```markdown
# 经验教训 (Lessons Learned)

> **Session 间记忆，避免重复错误**

---

## [2026-01-23] - 2025_Problem_C 数据处理

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

## [2026-01-22] - 模型训练失败

### 错误
ZINB 模型在 50 个国家的小数据集上训练失败（收敛警告）。

### 根因
样本量不足（n=50），但 ZINB 参数过多导致过拟合和收敛困难。

### 解决方案
改用简单 Poisson 回归 + L2 正则化。

### 预防措施
**Claude Code，今后选择模型时**：
- 如果 n < 100，优先选择简单模型（线性/逻辑回归）
- 参考 `docs/math_models_cheatsheet.md` 中的"适用场景"
- 如果必须用复杂模型，必须加强正则化
- 参考 `docs/anti_patterns.md` 避免过拟合

---

## [2026-01-20] - BOM 字符错误

### 错误
读取 CSV 文件时，列名包含 BOM 字符（`\ufeff`），导致后续代码找不到列。

### 根因
使用 `pd.read_csv(file)` 而未指定编码，导致 BOM 字符未去除。

### 解决方案
```python
# 修改前
df = pd.read_csv('summerOly_medal_counts.csv')

# 修改后
df = pd.read_csv('summerOly_medal_counts.csv', encoding='utf-8-sig')
# 或
import codecs
with codecs.open('summerOly_medal_counts.csv', 'r', 'utf-8-sig') as f:
    df = pd.read_csv(f)
```

### 预防措施
**Claude Code，今后读取任何 CSV 文件时**：
- 必须使用 `encoding='utf-8-sig'` 或 `codecs.open()`
- 读取后检查列名是否有 BOM 字符
- 如果有，使用 `.str.replace('\ufeff', '')` 去除

---

## [2026-01-18] - 缺失值处理错误

### 错误
使用均值填充缺失值，导致数据分布偏差。

### 根因
没有考虑数据的分布特征，直接使用 `df.fillna(df.mean())`。

### 解决方案
```python
# 对于计数数据，使用中位数或 0
df['medal_count'].fillna(0, inplace=True)

# 对于连续数据，使用 MICE 多重插补
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
df[['feature1', 'feature2']] = imputer.fit_transform(df[['feature1', 'feature2']])
```

### 预防措施
**Claude Code，今后处理缺失值时**：
- 参考 `docs/anti_patterns.md` 中的缺失值处理
- 根据数据类型选择合适的填充方法
- 填充后检查数据分布是否合理
```

### 格式规范

每个条目必须包含 4 部分：

1. **错误**：具体描述发生了什么
2. **根因**：为什么发生（深入分析）
3. **解决**：如何修复的（代码级别）
4. **预防**：下次如何避免（给 Claude Code 的指令）

---

## 第三部分：复盘协议

### Session 启动（读取历史经验）

```markdown
# Session 启动指令

Claude Code，请执行以下初始化：

1. **读取历史经验**：
   ```
   Read: global_memory/lessons_learned.md
   ```

2. **确认理解**：
   - 你记住了哪些历史错误？
   - 你会在本次任务中如何避免这些错误？

3. **承诺**：
   - 我会在本次任务中严格避免重复这些错误
   - 如果遇到类似情况，我会自动应用已知的解决方案

确认后，开始执行任务。
```

### Session 结束（复盘）

```markdown
# Session 结束指令

Claude Code，任务完成，请执行复盘：

## 第一步：总结关键错误

**回顾整个任务，识别所有 Critical Errors**：

1. **数据处理错误**：
   - 发生了什么？
   - 什么时候发生的？
   - 如何发现的？

2. **模型训练错误**：
   - 模型是否收敛？
   - 统计检验是否通过？
   - 是否过拟合？

3. **代码错误**：
   - 是否有 Bug？
   - 是否有警告？
   - 如何修复的？

4. **验证失败**：
   - 哪些验证未通过？
   - 为什么？
   - 如何修正的？

## 第二步：提炼经验教训

**对于每个关键错误，提炼成经验教训**：

格式：
```markdown
## [日期] - [任务名]

### 错误
[具体描述]

### 根因
[深入分析]

### 解决方案
[代码级别]

### 预防措施
**Claude Code，今后...**：
```

## 第三步：追加记忆

**将提炼的经验教训追加到 global_memory/lessons_learned.md**：

```
Append: global_memory/lessons_learned.md
```

**确保**：
- 格式与现有条目一致
- 包含所有 4 个部分（错误、根因、解决、预防）
- 预防措施具体到代码级别
- 给 Claude Code 的指令明确可执行

## 第四步：验证记忆

**自我检查**：

- [ ] 所有关键错误都已记录？
- [ ] 根因分析足够深入？
- [ ] 解决方案具体到代码？
- [ ] 预防措施可执行？
- [ ] 格式与现有条目一致？

确认后，保存文件。
```

---

## 第四部分：人工审核

### 审核协议

```markdown
# 人工审核协议

**User: 审核 Claude Code 生成的复盘内容**

## 审核清单

1. **准确性**：
   - [ ] 错误描述准确？
   - [ ] 根因分析正确？
   - [ ] 解决方案有效？

2. **完整性**：
   - [ ] 所有关键错误都记录了？
   - [ ] 没有遗漏重要信息？

3. **可执行性**：
   - [ ] 预防措施具体？
   - [ ] 代码可复制粘贴？
   - [ ] Claude Code 能理解？

4. **格式规范**：
   - [ ] 包含所有 4 个部分？
   - [ ] 格式与现有条目一致？

## 如果需要修改

**指令**：
"Claude Code，请修改第 X 条经验教训：
- 根因应该是：[正确的根因]
- 解决方案应该是：[代码]
- 预防措施应该更具体：[具体指令]"

**修改后重新审核**。

## 如果审核通过

**指令**：
"批准。保存到 global_memory/lessons_learned.md"

**Claude Code 执行**：
```bash
Append: global_memory/lessons_learned.md
```
```

---

## 第五部分：使用协议

### 完整流程（从 Session 开始到结束）

```markdown
# 完整 Session 流程

## Phase 1: Session 启动

**User**:
"Claude Code，请：

1. **读取知识库**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: docs/mcm_o_prize_style_guide.md

2. **读取历史经验**：
   - Read: global_memory/lessons_learned.md

3. **确认理解**：
   - 你记住了哪些反模式？
   - 你记住了哪些历史错误？
   - 你会在本次任务中如何避免？

确认后开始。"

**Claude Code**:
→ 读取所有文档
→ 内化为上下文
→ 确认理解
→ 准备执行任务

---

## Phase 2: 执行任务

**User**:
"开始执行 2025_C 任务。"

**Claude Code**:
→ 科学家模式：分析问题
→ 工程师模式：实现代码
  - **自动检查**：global_memory/lessons_learned.md
  - **自动应用**：已知的解决方案
→ 批评家模式：验证结果
→ 作家模式：撰写论文

**如果在执行过程中遇到历史错误**：
→ Claude Code 自动应用已知解决方案
→ 不需要人工干预

---

## Phase 3: Session 结束

**User**:
"任务完成，请复盘。"

**Claude Code**:
→ 第一步：总结关键错误
→ 第二步：提炼经验教训
→ 第三步：追加到 global_memory/lessons_learned.md
→ 第四步：自我检查

**输出**：
```markdown
## 复盘结果

### 关键错误

1. **错误 1**：[描述]
   - 根因：[分析]
   - 解决：[代码]
   - 预防：[指令]

2. **错误 2**：[描述]
   - ...

### 追加记忆

已追加到 global_memory/lessons_learned.md：
- [ ] 错误 1
- [ ] 错误 2

请审核。
```

---

## Phase 4: 人工审核

**User**:
"审核通过。保存。"

**Claude Code**:
→ 保存到 global_memory/lessons_learned.md
→ 确认保存成功

**下次 Session 启动时**：
→ Claude Code 自动读取新追加的经验教训
→ 严格避免重复错误
```

---

## 第六部分：与原计划的对比

### 进化系统对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **进化方式** | 自动分析 MMBench → 更新 Prompts | Session 复盘 → 追加记忆 |
| **分析工具** | auto_evolution.py | 人工复盘 |
| **评估系统** | MMBench 111 问题 | Session 内验证 |
| **更新方式** | 自动修改 .claude/agents/*.md | 人工审核后追加 lessons_learned.md |
| **输出** | evolution_log.md（复杂） | lessons_learned.md（简单） |
| **人工介入** | 最少 | 必需 |

### 核心改变

1. **从"自动进化"到"人工审核"**
   - 不自动更新 Prompts
   - 人工审核后追加记忆

2. **从"MMBench 测试"到"Session 内验证"**
   - 不用 111 问题测试
   - Session 内验证即可

3. **从"复杂日志"到"简单记忆"**
   - 不维护 evolution_log.md
   - 简单的 lessons_learned.md

---

## 第七部分：快速开始

### 初始化

```bash
# 1. 创建目录
mkdir -p global_memory

# 2. 初始化文件
echo "# Lessons Learned\n\n" > global_memory/lessons_learned.md

# 3. 添加第一个条目（示例）
cat >> global_memory/lessons_learned.md << 'EOF'
## [2026-01-23] - 示例条目

### 错误
这是一个示例条目，展示 lessons_learned.md 的格式。

### 根因
新系统初始化时需要一个示例。

### 解决方案
创建此示例条目。

### 预防措施
**Claude Code，今后**：
- 严格遵循此格式
- 包含所有 4 个部分
- 预防措施必须具体可执行
EOF
```

### 使用

```markdown
# Session 启动

Claude Code，请：

1. **读取历史经验**：
   ```
   Read: global_memory/lessons_learned.md
   ```

2. **确认理解**：
   - 你记住了哪些历史错误？
   - 你会在本次任务中如何避免？

3. **开始任务**：
   - "开始执行 2025_C 任务"

---

# Session 结束

Claude Code，任务完成，请复盘：

1. 总结关键错误
2. 提炼经验教训
3. 追加到 global_memory/lessons_learned.md
4. 格式：[日期] - [任务名] / 错误 / 根因 / 解决 / 预防
```

---

**版本**: Revised
**核心理念**: Session 间记忆，人工审核
**关键**: 复盘协议，lessons_learned.md，人工审核

---

**END OF 05_SELF_EVOLUTION_REVISED.md**
