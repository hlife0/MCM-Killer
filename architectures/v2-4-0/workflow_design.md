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
