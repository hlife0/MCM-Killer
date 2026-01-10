# MCM-Killer v2.5.0: 咨询机制

> **定义 Agent 间信息交换的规则和流程**
>
> **版本**: v2.5.0
> **最后更新**: 2026-01-07

---

## 一、核心原则

### 1.1 咨询的本质

**Consultation = Agent 在执行过程中向其他 Agent 寻求信息**

特点：
1. **同步阻塞**：发起咨询后，Director 立即处理，获得回复后才继续
2. **立即响应**：不存在"待处理"状态
3. **有记录**：所有咨询记录到 `docs/consultation/` 目录

### 1.2 单线程执行

> **重要前提**：系统是单线程的，同一时间只有一个 Agent 工作。

这意味着：
- 不存在并发咨询
- 咨询总是 blocking 的
- Director 充当中转站

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
Director 将回复写入 consultation/{i}_{from}_{to}.md
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

### 5.1 发起方格式

```
Director，我需要咨询 @{agent_name}：

**问题**：{具体问题}
**背景**：{为什么需要问这个}（可选）
**我的理解**：{自己的初步判断}（可选）
```

### 5.2 被咨询方格式

```
FROM @{agent_name}：

**回答**：{直接回答问题}
**补充说明**：{额外需要注意的点}（可选）
```

---

## 六、发起方准则

> **鼓励发起咨询**：有任何不确定的问题都应该 consult，而不是自己猜测。

- ✅ 不确定就问
- ✅ 说明自己的理解，请对方确认或纠正
- ❌ 禁止在不确定时自行假设
- ❌ 禁止编造信息

---

## 七、回复方准则

> **诚实回答**：只回答自己确切知道的，不知道就说不知道。

- ✅ 如实回答自己知道的内容
- ✅ 不知道/不确定时如实说明，建议对方 consult 其他 Agent
- ✅ Implementation 相关 Agent 可运行程序验证
- ✅ Reader 等可读取文件获取信息
- ❌ **禁止在被 consult 时申请 consult 第三方**（不能套娃）
- ❌ 禁止编造不知道的内容

---

## 八、文件记录

### 8.1 文件路径

**路径**：`docs/consultation/{i}_{from}_{to}.md`

> `{i}` 是**全局咨询计数**，从 VERSION_MANIFEST 获取。

### 8.2 文件格式

```markdown
# Consultation #{i}: {from} → {to}

| 字段 | 值 |
|------|------|
| 编号 | {i} |
| 发起方 | {from} |
| 接收方 | {to} |
| 时间 | {timestamp} |
| 状态 | COMPLETED |

---

## 问题

{咨询内容，发起方填写}

---

## 回复

{回复内容，回复方填写}

---

## 不确定点

{回复方不确定的内容，建议发起方继续 consult 其他 Agent}（可选）
```

---

## 九、与 Validation 的关系

**Validation 不是 Consultation**：
- Validation 是**强制性质量检查**，有固定的 Gate 位置
- Consultation 是**可选的信息交换**，随时可能发生

但 Validation 可能**触发** Consultation：
- Validator 发现问题 → REJECTED
- 如果问题需要讨论，Validator 可以发起 Consultation 请求相关 Agent 澄清

---

## 十、与 Director 的通信

### 10.1 发起方通信

```
Director，我需要咨询 @{agent}，文件：docs/consultation/{i}_{from}_{to}.md
```

### 10.2 回复方通信

```
Director，已完成 @{agent} 的咨询回复，文件：docs/consultation/{i}_{from}_{to}.md
```

---

## 十一、禁止事项

- ❌ **禁止套娃咨询**（被咨询时不能再发起咨询）
- ❌ 禁止编造回复内容
- ❌ 禁止在 Validation 期间发起 Consultation
- ❌ 禁止咨询后不记录文件

---

## 十二、总结

**咨询机制的核心**：
1. **同步阻塞**：发起后立即处理
2. **单线程**：同一时间只有一个 Agent 工作
3. **Director 中转**：Agent 间不直接通信
4. **文件记录**：所有咨询写入 docs/consultation/
5. **诚实原则**：不知道就说不知道

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
