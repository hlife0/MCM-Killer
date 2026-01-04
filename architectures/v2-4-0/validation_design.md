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
