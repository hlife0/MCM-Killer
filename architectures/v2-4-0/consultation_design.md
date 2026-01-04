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
