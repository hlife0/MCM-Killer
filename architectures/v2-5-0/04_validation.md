# MCM-Killer v2.5.0: 验证机制

> **定义多 Agent 协作验证的规则和流程**
>
> **版本**: v2.5.0
> **最后更新**: 2026-01-07

---

## 一、核心原则

### 1.1 验证的特点

- **多人参与**：每个 Validation Gate 由多个 Agent 从不同角度验证
- **独立判断**：每个验证者只能根据自己的知识判断，**不允许发起 Consultation**
- **并行执行**：Director 可并行调用多个验证者
- **同样标准**：返工后的验证必须保持同样高标准（**返工不免验**）

### 1.2 验证 vs Consultation

| 方面 | Validation | Consultation |
|------|-----------|--------------|
| 目的 | 质量检查 | 信息获取 |
| 方向 | 多对一（多人验证一个产出） | 一对一 |
| 能否发起咨询 | ❌ 禁止 | ✅ 允许 |
| 能否使用工具 | ✅ 可以 | ✅ 可以 |
| 输出 | 验证报告（APPROVED/REJECTED） | 回复 |

---

## 二、验证参与者角色

每个 Agent 在 Validation 时有特定的**验证视角**：

| Agent | 验证视角 | 典型检查内容 |
|-------|---------|-------------|
| **reader** | 题意符合性 | 是否符合题目要求？假设是否合理？Sanity check |
| **researcher** | 方法论可行性 | 过去论文是否有类似方法？ |
| **modeler** | 模型设计一致性 | 实现是否严格遵循模型设计？ |
| **feasibility_checker** | 技术可行性 | 当前设备是否能运行？ |
| **advisor** | 创新度/质量 | 是否"太水"？创新度是否足够？ |
| **code_translator** | 代码正确性 | 代码是否正确实现了要求？ |
| **validator** | 结果合理性 | 是否造假？结果是否符合常识？ |
| **data_engineer** | 数据质量 | 数据是否准确？特征是否正确？ |
| **writer** | 表达清晰性 | 论述是否清晰？逻辑是否通顺？ |

---

## 三、验证阶段定义

### Gate MODEL（模型设计后）

**被验证对象**：`model/model_design_{i}.md`

**参与者**（4 人）：

| 参与者 | 验证问题 |
|--------|---------|
| reader | 模型是否能解决题目要求的问题？假设是否合理？ |
| feasibility_checker | 当前设备和时间约束下是否能实现？ |
| advisor | 模型是否有足够创新度？是否太简单/太水？ |
| researcher | 方法是否有理论支撑？过去是否有类似成功案例？ |

---

### Gate DATA（数据处理后）

**被验证对象**：`implementation/data/features_{i}.pkl` 和 `.csv`

**参与者**（3 人）：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 特征是否与模型设计中的要求一致？ |
| validator | 数据是否合理？有没有明显异常？是否通过数据质量检查？ |
| reader | 数据处理是否符合题目约束（如不能用外部数据）？ |

---

### Gate CODE（代码完成后）

**被验证对象**：`implementation/code/model_{i}.py`

**参与者**（3 人）：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 代码是否严格实现了数学模型？ |
| code_translator | 代码语法、逻辑是否正确？ |
| feasibility_checker | 代码是否能在当前环境运行？ |

---

### Gate TRAINING（训练完成后）

**被验证对象**：`implementation/data/results_{i}.csv`

**参与者**（4 人）：

| 参与者 | 验证问题 |
|--------|---------|
| modeler | 训练过程是否严格遵循模型设计？ |
| code_translator | 训练代码是否正确执行？ |
| validator | 结果是否合理？有没有造假？是否符合常识？ |
| reader | 结果是否符合题目假设？Sanity check |

**特别注意**：
- 这是最容易出问题的阶段
- 验证者必须严格检查结果是否在合理范围
- 检查是否有明显的造假迹象

---

### Gate PAPER（论文完成后）

**被验证对象**：`paper/paper_{i}.md`

**参与者**（4 人）：

| 参与者 | 验证问题 |
|--------|---------|
| reader | 论文是否回答了所有题目要求？ |
| validator | 论文中的数据是否与 CSV 一致？ |
| advisor | 论文质量是否足够？与优秀论文差距？ |
| writer | 表达是否清晰？逻辑是否通顺？ |

---

### Gate SUMMARY（摘要完成后）

**被验证对象**：`paper/summary/summary_1page.md`

**参与者**（2 人）：

| 参与者 | 验证问题 |
|--------|---------|
| validator | 摘要数据是否与论文一致？ |
| reader | 摘要是否准确概括了解决方案？ |

**硬性要求**：编译后必须恰好 1 页

---

### Gate FINAL（最终检查）

**被验证对象**：所有文件

**参与者**（3 人）：

| 参与者 | 验证问题 |
|--------|---------|
| validator | 全局一致性：paper = summary = CSV？ |
| advisor | 整体质量评估 |
| reader | 是否完全满足题目要求 |

**最终检查清单**：
- [ ] 论文数据与 CSV 完全一致
- [ ] 摘要数据与论文完全一致
- [ ] 所有图表清晰可读
- [ ] 页数符合要求
- [ ] 格式符合 MCM 规范

---

## 四、验证结果

### 4.1 结果类型

| 结果 | 含义 | 后续 |
|------|------|------|
| ✅ **APPROVED** | 通过 | 进入下一阶段 |
| ⚠️ **CONDITIONAL** | 有条件通过 | 记录问题，继续（需关注） |
| ❌ **REJECTED** | 未通过 | 返回修复，重新验证 |

### 4.2 判定规则

- 全部 APPROVED → 进入下一阶段
- 有 CONDITIONAL → 记录问题，继续
- 任一 REJECTED → 返工

---

## 五、验证流程

```
Director 触发某 Stage 的 Validation
    │
    ├── 并行调用多个 Agent
    │   ├── Agent A 验证 → 写入 docs/validation/{i}_{stage}_{agent}.md
    │   ├── Agent B 验证 → 写入 docs/validation/{i}_{stage}_{agent}.md
    │   └── Agent C 验证 → 写入 docs/validation/{i}_{stage}_{agent}.md
    │
    ▼
Director 汇总所有验证报告
    │
    ├── 全部 APPROVED → 进入下一阶段
    ├── 有 CONDITIONAL → 记录问题，继续
    └── 有 REJECTED → 返回修复，重新验证
```

---

## 六、验证报告格式

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
| 2 | {item} | ✅/⚠️/❌ | {note} |

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

## 七、返工不免验机制

### 7.1 核心原则

> **返工后的产出必须以同样高标准重新验证**

验证者收到返工版本时，必须：
1. 以同样的高标准进行审查
2. 不因为是返工版本就降低要求
3. 不假设问题已修复，重新检查所有项
4. 如果发现新问题，必须指出

### 7.2 返工时的验证者提醒

每个验证者在收到返工版本时，会看到以下提醒：

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

### 7.3 返工计数

- 每个 Gate 最多返工 3 次
- 超过 3 次：需要讨论是否回退到更早阶段

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

---

## 八、与 Director 的通信

### 8.1 验证者汇报（简洁）

```
Director，已完成 {stage} 阶段验证，判定：{结果}，报告：docs/validation/{i}_{stage}_{agent}.md
```

### 8.2 Director 调用验证者

```
@{agent} 请参与 {stage} 阶段验证。

验证对象：{file_path}
验证视角：{perspective}
输出位置：docs/validation/{i}_{stage}_{agent}.md

这是第 {n} 次验证。请严格审查。
```

---

## 九、禁止事项

在 Validation 阶段：

- ❌ **禁止发起 Consultation**（独立判断）
- ❌ 禁止修改被验证的文件
- ❌ 禁止编造检查结果
- ❌ 返工验证时降低标准

---

## 十、总结

**验证机制的核心**：
1. **多人多视角**：每个 Gate 有多个 Agent 从不同角度验证
2. **独立判断**：不允许 Consultation，避免相互影响
3. **并行验证**：Director 可以并行调用多个验证者
4. **汇总决策**：Director 综合所有报告决定是否通过
5. **返工不免验**：返工版本必须以同样标准审查

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
