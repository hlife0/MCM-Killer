# MCM-Killer v2.5.0: 执行流程

> **定义完整的 10 阶段工作流程**
>
> **版本**: v2.5.0
> **最后更新**: 2026-01-07

---

## 一、阶段概览

| Phase | 名称 | 主要 Agent | Validation Gate | 估计时间 |
|-------|------|-----------|-----------------|----------|
| 0 | Problem Understanding | reader, researcher | - | 30 min |
| 1 | Model Design | modeler | ✅ MODEL | 1-2 hours |
| 2 | Feasibility Check | feasibility_checker | - | 30 min |
| 3 | Data Processing | data_engineer | ✅ DATA | 1-2 hours |
| 4 | Code Translation | code_translator | ✅ CODE | 1-2 hours |
| 5 | Model Training | model_trainer | ✅ TRAINING | 5A: 30min, 5B: 4-6 hours |
| 6 | Visualization | visualizer | - | 30 min |
| 7 | Paper Writing | writer | ✅ PAPER | 2-3 hours |
| 8 | Summary | summarizer | ✅ SUMMARY | 30 min |
| 9 | Polish | editor | ✅ FINAL | 30 min |
| 10 | Final Review | advisor | - | 30 min |

**总计**：约 10-15 小时（不含 Phase 5B 可选）

---

## 二、各阶段详细流程

### Phase 0: Problem Understanding（问题理解）

```
Director
    │
    ├─→ @reader
    │   ├── 读取 problem/original/*.pdf
    │   ├── 生成 problem/problem_full.md
    │   ├── 生成 problem/problem_requirements_1.md
    │   └── 汇报：docs/report/reader_1.md
    │
    └─→ @researcher
        ├── 阅读 problem_requirements_1.md
        ├── 进行文献/方法调研
        ├── 生成 model/research_notes_1.md
        └── 汇报：docs/report/researcher_1.md
```

**输出**：
- `problem/problem_full.md`
- `problem/problem_requirements_1.md`
- `model/research_notes_1.md`

**无验证门**（信息收集阶段）

---

### Phase 1: Model Design（模型设计）

```
Director
    │
    └─→ @modeler
        ├── 阅读 problem_requirements_1.md
        ├── 阅读 research_notes_1.md
        ├── 设计数学模型
        ├── 生成 model/model_design_1.md
        └── 汇报：docs/report/modeler_1.md

    ↓ (触发 Validation Gate: MODEL)
```

#### Validation Gate: MODEL

**参与者**（4 人）：

| Agent | 验证问题 |
|-------|---------|
| reader | 模型能否解决题目要求？假设是否合理？ |
| feasibility_checker | 设备和时间约束下能否实现？ |
| advisor | 模型创新度是否足够？是否太水？ |
| researcher | 方法是否有理论支撑？ |

**判定规则**：
- ✅ 全部 APPROVED → 进入 Phase 2
- ⚠️ 有 CONDITIONAL → 记录问题，继续
- ❌ 任一 REJECTED → 返工

**返工流程**：
```
Director 收集所有 REJECTED 报告
    │
    └─→ @modeler (返工)
        ├── 阅读所有验证报告
        ├── 修复问题
        └── 生成 model/model_design_2.md

    ↓ (重新触发 Validation Gate: MODEL)
```

---

### Phase 2: Feasibility Check（可行性检查）

```
Director
    │
    └─→ @feasibility_checker
        ├── 阅读 model_design_1.md
        ├── 评估技术可行性
        ├── 评估时间/资源可行性
        ├── 生成 model/feasibility_1.md
        └── 汇报：docs/report/feasibility_checker_1.md
```

**输出**：
- `model/feasibility_1.md`

**判定规则**：
- ✅ APPROVED → 进入 Phase 3
- ❌ REJECTED → 返回 Phase 1（修改模型设计）
- ⚠️ CONDITIONAL → 记录风险，继续

---

### Phase 3: Data Processing（数据处理）

```
Director
    │
    └─→ @data_engineer
        ├── 阅读 model_design_1.md
        ├── 读取 problem/original/ 下的数据
        ├── 数据清洗
        ├── 特征工程
        ├── 自检数据质量 (check_data_quality)
        ├── 生成 implementation/data/features_1.pkl
        ├── 生成 implementation/data/features_1.csv
        ├── 生成 implementation/code/data_prep_1.py
        └── 汇报：docs/report/data_engineer_1.md

    ↓ (触发 Validation Gate: DATA)
```

#### Validation Gate: DATA

**参与者**（3 人）：

| Agent | 验证问题 |
|-------|---------|
| modeler | 特征是否与 model_design 一致？ |
| validator | 数据是否合理？有无异常？ |
| reader | 数据处理是否符合题目约束？ |

**返工流程**：同 MODEL Gate

---

### Phase 4: Code Translation（代码翻译）

```
Director
    │
    └─→ @code_translator
        ├── 阅读 model_design_1.md
        ├── 将数学模型翻译为代码
        ├── 生成 implementation/code/model_1.py
        ├── 生成 implementation/code/test_1.py
        └── 汇报：docs/report/code_translator_1.md

    ↓ (触发 Validation Gate: CODE)
```

#### Validation Gate: CODE

**参与者**（3 人）：

| Agent | 验证问题 |
|-------|---------|
| modeler | 代码是否严格实现了数学模型？ |
| code_translator | 代码语法/逻辑是否正确？ |
| feasibility_checker | 代码能否在当前环境运行？ |

**返工流程**：同 MODEL Gate

---

### Phase 5: Model Training（模型训练）⭐

> **v2.5.0 关键改进**：强制执行快速验证，禁止完全跳过

```
Director
    │
    └─→ @model_trainer
        │
        ├─→ Phase 5A: 快速验证 (mandatory, ≤30 min)
        │   ├── 使用减少样本/迭代
        │   ├── 快速调试代码
        │   ├── 确保模型可运行
        │   ├── 生成 implementation/data/results_quick_1.csv
        │   └── 汇报：docs/report/model_trainer_1.md
        │
        └─→ Phase 5B: 完整训练 (optional, 4-6 hours)
            ├── 完整 HMC 采样
            ├── 生成 implementation/data/results_1.csv
            ├── 生成 implementation/logs/training_1.log
            └── 汇报：docs/report/model_trainer_2.md

    ↓ (触发 Validation Gate: TRAINING)
```

#### 两阶段训练策略

**Phase 5A: 快速验证（mandatory）**

**目的**：确保代码可运行，模型基本可行

**策略**：
- 使用 10-20% 的数据
- 减少迭代次数（500 vs 2000）
- 快速收敛检查
- 预计时间：≤30 分钟

**输出**：
- `implementation/data/results_quick_1.csv`
- `implementation/logs/training_quick_1.log`

**Phase 5B: 完整训练（optional）**

**条件**：
- 5A 成功完成
- 有足够的 Token
- 用户未选择跳过

**策略**：
- 完整数据集
- 完整 HMC 采样（2000+ 迭代）
- 完整收敛诊断
- 预计时间：4-6 小时

**输出**：
- `implementation/data/results_1.csv`
- `implementation/logs/training_1.log`

#### Validation Gate: TRAINING

**参与者**（4 人）：

| Agent | 验证问题 |
|-------|---------|
| modeler | 训练过程是否严格遵循模型设计？ |
| code_translator | 训练代码是否正确执行？ |
| validator | 结果是否合理？是否造假？ |
| reader | 结果是否符合题目假设？Sanity check |

**特别注意**：
- 验证 5A 的结果是否足够验证模型可行性
- 如果只做了 5A，验证报告需要明确说明

#### 禁止行为

```
❌ 禁止：完全跳过 Phase 5
❌ 禁止：理由"时间不足"就跳过
✅ 必须：至少完成 Phase 5A
✅ 允许：Phase 5B 标记为"后续优化"
```

---

### Phase 6: Visualization（可视化）

```
Director
    │
    └─→ @visualizer
        ├── 阅读论文需求和模型结果
        ├── 生成图表
        ├── 生成 paper/figures/figure_*.png
        ├── 更新 paper/figures/figure_index.md
        └── 汇报：docs/report/visualizer_1.md
```

**输出**：
- `paper/figures/figure_*.png`
- `paper/figures/figure_index.md`

**无单独验证门**（与 PAPER 一起验证）

---

### Phase 7: Paper Writing（论文撰写）

```
Director
    │
    └─→ @writer
        ├── 阅读 problem_requirements_1.md
        ├── 阅读 model_design_1.md
        ├── 阅读 results_1.csv
        ├── 撰写论文
        ├── 生成 paper/paper_1.md
        └── 汇报：docs/report/writer_1.md

    ↓ (触发 Validation Gate: PAPER)
```

#### Validation Gate: PAPER

**参与者**（4 人）：

| Agent | 验证问题 |
|-------|---------|
| reader | 论文是否回答了所有题目要求？ |
| validator | 论文数据是否与 CSV 一致？ |
| advisor | 论文质量是否足够？ |
| writer | 表达是否清晰？ |

**返工流程**：
- 数据不一致 → 可能回退 Phase 5
- 表达问题 → writer 修复
- 内容不足 → 可能回退更早阶段

---

### Phase 8: Summary（摘要）

```
Director
    │
    └─→ @summarizer
        ├── 阅读 paper_1.md
        ├── 创建摘要
        ├── 生成 paper/summary/summary_1page.md
        └── 汇报：docs/report/summarizer_1.md

    ↓ (触发 Validation Gate: SUMMARY)
```

#### Validation Gate: SUMMARY

**参与者**（2 人）：

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
    └─→ @editor
        ├── 润色 paper_1.md
        ├── 润色 summary_1page.md
        ├── 生成 paper/paper_revised.md
        └── 汇报：docs/report/editor_1.md

    ↓ (触发 Validation Gate: FINAL)
```

#### Validation Gate: FINAL

**参与者**（3 人）：

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
    └─→ @advisor
        ├── 全面审核所有产出
        ├── 生成最终质量报告
        ├── 评估 submission readiness
        └── 汇报：docs/report/advisor_2.md
```

**输出**：
- `output/PROJECT_COMPLETION_SUMMARY.md`

**如果发现重大问题**：返回相应阶段修复

---

## 三、返工机制

### 3.1 返工不免验

> **核心原则**：返工后的产出必须以**同样高标准**重新验证。

验证者收到返工版本时，必须：
1. 以同样的高标准进行审查
2. 不因为是返工版本就降低要求
3. 不假设问题已修复，重新检查所有项
4. 如果发现新问题，必须指出

### 3.2 返工流程

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
重新触发 Validation Gate（同样标准）
```

### 3.3 返工计数

- 每个 Gate 最多返工 3 次
- 超过 3 次：需要讨论是否回退到更早阶段

### 3.4 回退机制

| 在 Gate | 发现问题 | 回退到 |
|---------|---------|--------|
| CODE | 模型设计有缺陷 | Phase 1 (modeler) |
| TRAINING | 特征不正确 | Phase 3 (data_engineer) |
| PAPER | 结果不合理 | Phase 5 (model_trainer) |
| FINAL | 模型方法论问题 | Phase 1 (modeler) |

---

## 四、验证门总结

| Gate | 位置 | 参与者 | 返工目标 |
|------|------|--------|----------|
| MODEL | Phase 1 后 | 4 | modeler |
| DATA | Phase 3 后 | 3 | data_engineer |
| CODE | Phase 4 后 | 3 | code_translator |
| TRAINING | Phase 5 后 | 4 | model_trainer 或回退 |
| PAPER | Phase 7 后 | 4 | writer 或回退 |
| SUMMARY | Phase 8 后 | 2 | summarizer |
| FINAL | Phase 9 后 | 3 | editor 或回退 |

---

## 五、检查点机制（v2.5.0 新增）

### 5.1 检查点位置

每个 Phase 结束时自动保存检查点：
- `output/.checkpoint_phase{i}.json`

### 5.2 检查点内容

```json
{
  "phase": 5,
  "completed_at": "2026-01-07 12:30:00",
  "outputs": [
    "output/implementation/data/results_quick_1.csv",
    "output/implementation/logs/training_quick_1.log"
  ],
  "manifest_snapshot": {...},
  "token_usage": 125000,
  "token_percentage": 75
}
```

### 5.3 恢复机制

如果需要从检查点恢复：
1. 读取检查点文件
2. 恢复 VERSION_MANIFEST.json
3. 从下一个 Phase 继续

---

## 六、Token 使用估算

| Phase | 估计 Token 使用 | 累计 |
|-------|----------------|------|
| 0 | 10k | 10k |
| 1 | 20k | 30k |
| 2 | 5k | 35k |
| 3 | 25k | 60k |
| 4 | 20k | 80k |
| 5A | 15k | 95k |
| 5B | 50k+ | 145k+ |
| 6 | 10k | 105k |
| 7 | 30k | 135k |
| 8 | 10k | 145k |
| 9 | 15k | 160k |
| 10 | 10k | 170k |

**建议**：
- 如果 Token limit 是 200k，应该完成所有阶段
- Phase 5B 可选，可标记为"后续优化"

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
