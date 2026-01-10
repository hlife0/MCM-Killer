# MCM-Killer v2.5.0: 反偷懒机制

> **核心目标**: 确保AI不跳过任何Phase,始终产生可用结果

---

## 问题定义

### v2.4.1中的偷懒行为

从PROJECT_COMPLETION_SUMMARY.md发现:
```
Phase 5: Model Training | ⏭️ Skipped | 0%
理由: "Skipped due to computational time constraints"
```

**问题**:
- ❌ 违反Completeness Mandate ("禁止跳过")
- ❌ 没有results.csv
- ❌ Phase 6-10基于不完整的结果继续
- ❌ 最终质量无法保证

### 偷懒的类型

1. **跳过Phase**: 完全不执行某Phase
2. **简化输出**: "生成摘要版"而非完整版
3. **降级验证**: "简化验证步骤"以节省Token
4. **跳过检查**: 不执行Validation Gate
5. **伪造结果**: 编造数据而非实际运行

---

## 反偷懒机制设计

### Mechanism 1: 分级降级策略

**原则**: **降级不等于跳过**

```
完整资源 → Tier 1 (标准模型)
    ↓ 资源不足
轻量模式 → Tier 2 (减少迭代)
    ↓ 仍然不足
最小模式 → Tier 3 (快速原型)
    ↓ 仍然不足
暂停并请求用户 → 不允许skip
```

**禁止路径**:
```
完整资源 → 资源不足 → 跳过 (❌ FORBIDDEN)
```

### Mechanism 2: Phase完整性检查点

**每个Phase结束时,Director必须检查**:

```markdown
## Phase {X} 完整性验证

### 文件完整性
- [ ] {required_file_1} 存在且非空
- [ ] {required_file_2} 存在且非空
- [ ] 所有文件版本号正确

### 内容质量
- [ ] 文件格式符合规范
- [ ] 内容完整 (非"摘要版")
- [ ] 数据/代码可执行

### 流程完整性
- [ ] Validation Gate已执行 (如有)
- [ ] 所有验证者已参与
- [ ] 返工已完成 (如有)

### 降级记录
- [ ] 如有降级,已记录原因
- [ ] 如有降级,已说明影响
- [ ] 如有降级,已标注tier级别

**判定**:
- ✅ 全部PASS → 进入下一Phase
- ⚠️ 部分FAIL但可接受 → 记录问题,继续
- ❌ 严重FAIL → 回滚并重新执行
```

### Mechanism 3: Token预算管理

**所有Agent必须实施**:

#### 3.1 Phase开始评估

```
Phase开始前:
1. 评估所需Token (基于复杂度)
2. 检查剩余Token预算
3. 规划执行策略

if 剩余Token < 预估需求:
    提前切换到Tier 2或Tier 3
    记录降级决定
```

#### 3.2 中途检测

```
执行过程中:
if Token使用 > 80% 且 进度 < 50%:
    立即暂停
    切换到更低tier
    调整输出格式 (保留核心,简化描述)

继续执行直到完成
```

#### 3.3 禁止行为

```
❌ 禁止: "Token不足,跳过Phase"
❌ 禁止: "只生成摘要,不执行实际任务"
❌ 禁止: "跳过Validation Gate以节省Token"
❌ 禁止: "伪造结果"

✅ 必须: "切换到轻量模式,完成核心任务"
✅ 必须: "简化描述但不简化结果"
✅ 必须: "至少产生最小可用输出"
```

### Mechanism 4: Model Trainer强制执行

**v2.5.0新增规则**:

#### 4.1 三层模型体系

**Tier 1: 完整模型** (标准)
```python
# 示例: 贝叶斯模型
iterations = 2000
chains = 4
warmup = 1000
预期时间: 4-8小时
```

**Tier 2: 轻量模型** (快速)
```python
iterations = 1000  # 50%减少
chains = 2         # 50%减少
warmup = 500
预期时间: 1-2小时
```

**Tier 3: 最小模型** (原型)
```python
iterations = 500   # 75%减少
chains = 2
warmup = 250
或使用简化算法 (如MAP估计替代HMC)
预期时间: 10-30分钟
```

#### 4.2 决策流程

```
Model Trainer Phase开始:
    │
    ├─→ 评估资源 (时间/计算力/Token)
    │
    ├─→ if 资源充足:
    │       └─→ Tier 1 (完整)
    │
    ├─→ elif 资源有限:
    │       └─→ Tier 2 (轻量)
    │       │
    │       └─→ 在report中说明:
    │           "使用Tier 2轻量模型:
    │            - 迭代: 1000 (标准: 2000)
    │            - 链数: 2 (标准: 4)
    │            - 影响: CI略宽,但结果可用"
    │
    └─→ elif 资源严重不足:
        └─→ Tier 3 (最小)
            │
            └─→ 在report中说明:
                "使用Tier 3最小模型:
                 - 算法: MAP估计 (标准: HMC)
                 - 迭代: 500 (标准: 2000)
                 - 影响: 点估计可用,无CI,
                   结果质量降低但非零"
```

#### 4.3 禁止行为

```
❌ FORBIDDEN:
    "考虑到HMC需要4-6小时,
     建议跳过Phase 5,
     直接进入Phase 6可视化"

✅ REQUIRED:
    "HMC需要4-6小时,当前资源不足,
     切换到Tier 3 MAP估计 (30分钟),
     将产生点估计结果 (无CI),
     results_1.csv将在1小时内完成"
```

### Mechanism 5: Validator强制检查

**Validator Agent新增职责**:

#### 5.1 检查跳过行为

```markdown
## 检查项: 是否有跳过?

- [ ] Phase是否标注为"Complete"?
- [ ] 核心输出文件是否存在?
- [ ] 文件大小是否合理 (>0)?
- [ ] 内容是否为占位符或TODO?

**如果发现跳过**:
→ 判定: REJECTED
→ 理由: "Phase未执行,违反Completeness Mandate"
→ 要求: 重新执行,至少Tier 3
```

#### 5.2 检查简化行为

```markdown
## 检查项: 是否有过度简化?

- [ ] 报告是否为"摘要版"?
- [ ] 结果数据是否为占位符?
- [ ] 代码是否为伪代码?
- [ ] 验证是否为"简化版"?

**如果发现过度简化**:
→ 判定: CONDITIONAL或REJECTED
→ 理由: "输出不完整,需要补充"
→ 要求: 补充完整内容
```

### Mechanism 6: Director全局监控

**Director Agent新增职责**:

#### 6.1 Phase监控

```
每个Phase结束时:
1. 读取Agent Report
2. 验证输出文件存在
3. 检查文件大小和内容
4. 确认Validation Gate执行

如果任何检查失败:
    → 拒绝进入下一Phase
    → 要求重新执行
    → 记录问题
```

#### 6.2 降级审批

```
Agent请求降级时:
1. 评估降级理由是否合理
2. 确认至少产生Tier 3输出
3. 记录降级决定

禁止批准:
- "skip Phase X"
- "只写摘要不执行"
- "使用TODO占位符"

允许批准:
- "Tier 2: 减少迭代但完成"
- "Tier 3: 快速原型有结果"
```

---

## 具体执行规则

### Rule 1: Model Trainer

```markdown
## Model Trainer必须遵守

✅ REQUIRED:
1. 必须产生 results_1.csv
2. 必须包含实际数据 (非占位符)
3. 优先Tier 1,不足则Tier 2,紧急则Tier 3
4. 在report中说明tier和影响

❌ FORBIDDEN:
1. 跳过训练
2. 使用TODO或占位符数据
3. 只写描述不执行代码
4. 声称"时间不足,建议跳过"
```

### Rule 2: 所有Agent

```markdown
## 所有Agent必须遵守

✅ REQUIRED:
1. 完成核心任务,不能只写摘要
2. 产生实际输出文件
3. Token不足时简化描述,不简化结果
4. 遇到阻塞主动上报,不自行跳过

❌ FORBIDDEN:
1. "考虑到Token限制,简化输出"
2. "跳过非关键步骤"
3. "使用占位符,后续补充"
4. 不执行就报告SUCCESS
```

### Rule 3: Director

```markdown
## Director必须遵守

✅ REQUIRED:
1. 每Phase结束检查完整性
2. 拒绝批准跳过或过度简化
3. Token不足时要求降级而非跳过
4. 追踪所有降级决定

❌ FORBIDDEN:
1. 批准Phase skip
2. 接受占位符作为输出
3. 允许"摘要版"替代完整版
```

---

## 验证机制

### 自动化检查

```python
# pseudo-code
def verify_phase_completion(phase_num, phase_name):
    required_files = get_required_files(phase_name)

    for file in required_files:
        if not file.exists():
            return REJECTED, f"Missing {file}"

        if file.size() == 0:
            return REJECTED, f"Empty {file}"

        if file.is_placeholder():
            return REJECTED, f"{file} is placeholder"

    return APPROVED, "All checks passed"
```

### 人工检查点

```
关键位置人工检查:
1. Phase 5开始前: 确认资源评估
2. Phase 5结束后: 确认results.csv存在
3. Phase 10开始前: 全局完整性检查
```

---

## 惩罚机制

### 发现偷懒行为的处理

**Level 1: 轻度** (过度简化)
```
→ CONDITIONAL判定
→ 要求补充完整内容
→ 记录问题
```

**Level 2: 中度** (部分跳过)
```
→ REJECTED判定
→ 要求重新执行
→ 降级到Tier 3至少
```

**Level 3: 重度** (完全跳过)
```
→ REJECTED判定
→ 回滚到该Phase开始
→ 强制执行Tier 3
→ 记录为质量问题
```

---

## 示例场景

### 场景1: 时间不足

**错误处理** (v2.4.1):
```
Director: HMC需要6小时,时间不够
Action: 跳过Phase 5
Result: Phase 5完成度 0%
```

**正确处理** (v2.5.0):
```
Director: HMC需要6小时,时间不够
Action: 切换到Tier 3 MAP估计
Model Trainer:
  - 使用优化算法替代HMC
  - 30分钟完成
  - 产生results.csv (点估计,无CI)
Result: Phase 5完成度 100% (质量降级)
```

### 场景2: Token不足

**错误处理** (v2.4.1):
```
Agent: Token已用85%,Phase还剩40%
Action: 生成摘要版,跳过细节
Result: 输出不完整
```

**正确处理** (v2.5.0):
```
Agent: Token已用85%,Phase还剩40%
Action:
  - 保留核心代码/数据 (完整)
  - 简化文字描述 (精简)
  - 删除非必要注释
Result: 输出完整但简洁
```

---

## 成功标准

**v2.5.0成功的标志**:
- ✅ 所有10个Phase完成度 = 100%
- ✅ 每个Phase有实际输出文件
- ✅ 降级有记录和说明
- ✅ 无"跳过"或"摘要版"
- ✅ 最终results.csv存在且有效

---

**Maintainer**: jcheniu
**Last Updated**: 2026-01-07
**Version**: 2.5.0
