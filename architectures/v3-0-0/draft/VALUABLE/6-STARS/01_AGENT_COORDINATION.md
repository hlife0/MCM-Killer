# 6-STARS: Agent 协作核心

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/6-STARS/01_AGENT_COORDINATION.md`
> **星级**: ⭐⭐⭐⭐⭐⭐
> **来源文档**: `04_MMAgent_Agent.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/agent/`

---

## 核心资产概览

| 模块 | 文件 | 核心功能 | 创新点 |
|------|------|----------|--------|
| DAG 调度器 | `coordinator.py` | 拓扑排序任务调度 | 类型归一化 + 循环检测 |
| 任务求解器 | `task_solving.py` | 分阶段任务处理 | SafePlaceholder 防崩溃 |
| 方法检索器 | `retrieve_method.py` | 嵌入相似度检索 | HMML 知识库检索 |
| 问题分析器 | `problem_analysis.py` | Actor-Critic 迭代 | 动态优化模式 |
| 数据分析器 | `data_description.py` | 数据分析引擎 | 自动数据探索 |

---

## 1. DAG 调度器 (coordinator.py)

### 为什么是 6 星？

`coordinator.py` 是 LLM-MM-Agent 的**核心调度引擎**，使用图论算法解决复杂任务依赖管理问题。

### 核心算法: 拓扑排序

```python
def topological_sort(tasks):
    """
    使用拓扑排序解决任务依赖关系
    返回: 按依赖顺序排列的任务列表
    """
    # 构建依赖图
    graph = {task: [] for task in tasks}
    in_degree = {task: 0 for task in tasks}

    for task in tasks:
        for dependency in task.dependencies:
            graph[dependency].append(task)
            in_degree[task] += 1

    # Kahn 算法
    queue = [task for task in tasks if in_degree[task] == 0]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(tasks):
        raise ValueError("存在循环依赖")

    return result
```

### 关键创新

#### 1. 类型归一化

```python
def normalize_task_id(task_id):
    """将所有 task_id 转换为字符串，防止类型不匹配"""
    return str(task_id)

# 应用到所有任务操作
task_id = normalize_task_id(task_id)
dependency = normalize_task_id(dependency)
```

**问题**: Python 中整数和字符串 `'1' != 1`
**解决**: 强制所有 task_id 为字符串类型

#### 2. 循环检测

```python
def detect_cycle(tasks):
    """检测任务依赖图中是否存在循环"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {task: WHITE for task in tasks}

    def dfs(node):
        color[node] = GRAY
        for neighbor in dependencies[node]:
            if color[neighbor] == GRAY:
                return True  # 发现循环
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for task in tasks:
        if color[task] == WHITE:
            if dfs(task):
                raise ValueError("检测到循环依赖")
```

#### 3. Memory 管理

```python
class Coordinator:
    def __init__(self):
        self.memory = {}  # 任务结果存储
        self.code_memory = {}  # 代码结构存储

    def add_task_result(self, task_id, result):
        """存储任务结果"""
        self.memory[normalize_task_id(task_id)] = result

    def get_task_result(self, task_id):
        """获取任务结果"""
        return self.memory.get(normalize_task_id(task_id))
```

**单数据源模式**: 所有任务结果统一存储在 `memory` 字典中

### 扩展到数百个子任务

**当前**: 支持数十个子任务
**目标**: 支持数百个子任务

**优化策略**:
1. **并行调度**: 使用多线程并行执行无依赖的任务
2. **增量调度**: 动态添加新任务，重新计算拓扑排序
3. **缓存优化**: 缓存拓扑排序结果，避免重复计算

---

## 2. 任务求解器 (task_solving.py)

### 为什么是 6 星？

`task_solving.py` 实现了**SafePlaceholder 模式**，防止模板格式化崩溃，这是 LLM 生成代码执行的基础设施。

### 核心创新: SafePlaceholder

```python
class SafePlaceholder:
    """
    防止模板格式化崩溃
    当变量缺失时，返回自身而不是抛出 KeyError
    """
    def __getattr__(self, name):
        return self

    def __format__(self, format_spec):
        return str(self)

# 使用示例
template = "Task {task_id}: {task_description}"
safe_ctx = SafePlaceholder()

# 即使 task_description 缺失，也不会崩溃
formatted = template.format(task_id=1, safe_ctx)
# 结果: "Task 1: "
```

**问题**: `"{missing_var}".format()` 抛出 `KeyError`
**解决**: SafePlaceholder 返回空字符串而不是崩溃

### 分阶段任务处理

```python
def solve_task(task, context):
    """
    分阶段处理任务:
    1. 问题分析
    2. 方法选择
    3. 代码生成
    4. 结果验证
    """
    # Stage 1: Problem Analysis
    problem = analyze_problem(task, context)

    # Stage 2: Method Selection
    methods = retrieve_methods(problem)

    # Stage 3: Code Generation
    code = generate_code(problem, methods)

    # Stage 4: Result Validation
    result = validate_and_execute(code)

    return result
```

**关键设计**:
- **顺序执行**: 每个阶段的输出是下一个阶段的输入
- **错误隔离**: 一个阶段的错误不影响其他阶段
- **结果可追踪**: 每个阶段生成中间结果

---

## 3. 方法检索器 (retrieve_method.py)

### 为什么是 6 星？

`retrieve_method.py` 实现了**嵌入相似度检索**，是从 HMML 知识库智能检索相关方法的核心技术。

### 核心算法: 嵌入相似度匹配

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_methods(query, hmml_embeddings, top_k=6):
    """
    使用嵌入相似度检索相关方法

    Args:
        query: 查询文本
        hmml_embeddings: HMML 方法的嵌入向量
        top_k: 返回前 k 个最相关的方法

    Returns:
        top_k 个最相关的方法列表
    """
    # 生成查询嵌入
    query_embedding = get_embedding(query)

    # 计算余弦相似度
    similarities = cosine_similarity(
        query_embedding.reshape(1, -1),
        hmml_embeddings
    )[0]

    # 获取 top_k 索引
    top_indices = np.argsort(similarities)[::-1][:top_k]

    # 返回对应的方法
    methods = [hmml_methods[i] for i in top_indices]

    return methods
```

**优势**:
- **语义匹配**: 比关键词匹配更智能
- **多语言支持**: 嵌入向量支持跨语言检索
- **可扩展**: 支持大规模向量检索

### 扩展到 400+ 方法

**当前**: 98+ 方法
**目标**: 400+ 方法

**优化策略**:
1. **向量索引**: 使用 FAISS 或 Annoy 加速检索
2. **分层检索**: 先检索域，再检索方法
3. **缓存机制**: 缓存常见查询的结果

---

## 4. 问题分析器 (problem_analysis.py)

### 为什么是 6 星？

`problem_analysis.py` 实现了**Actor-Critic 迭代优化**，这是一个通用的质量提升模式。

### Actor-Critic 迭代

```python
def actor_critic_iteration(problem, rounds=3):
    """
    Actor-Critic 迭代优化

    Args:
        problem: 问题描述
        rounds: 迭代轮数

    Returns:
        优化后的问题分析
    """
    # Actor: 生成初始分析
    analysis = actor(problem)

    for _ in range(rounds):
        # Critic: 评估分析质量
        critique = critic(analysis)

        # Actor: 根据批评改进分析
        improved_analysis = actor(problem, critique)

        # 检查是否收敛
        if is_converged(analysis, improved_analysis):
            break

        analysis = improved_analysis

    return analysis
```

**关键设计**:
- **Actor 生成**: 生成初始分析
- **Critic 评估**: 评估分析质量
- **迭代改进**: 根据批评改进分析
- **收敛检测**: 防止无限迭代

### 动态假设生成

```python
def generate_hypotheses(problem):
    """
    为问题生成多个假设

    Returns:
        假设列表
    """
    # 使用 LLM 生成假设
    hypotheses = llm_generate(
        f"Generate 3 hypotheses for: {problem}"
    )

    # 评估假设可行性
    feasible_hypotheses = []
    for hypothesis in hypotheses:
        if is_feasible(hypothesis):
            feasible_hypotheses.append(hypothesis)

    return feasible_hypotheses
```

**创新点**: 不是静态模板，而是动态 LLM 驱动

---

## 5. 数据分析器 (data_description.py)

### 为什么是 6 星？

`data_description.py` 实现了**自动数据探索**，是理解数据集的第一步。

### 核心功能

```python
def analyze_dataset(data_path):
    """
    自动分析数据集

    Returns:
        数据集描述报告
    """
    # 加载数据
    data = pd.read_csv(data_path)

    # 基本统计
    report = {
        "shape": data.shape,
        "columns": list(data.columns),
        "dtypes": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "summary_statistics": data.describe().to_dict()
    }

    # 数据类型推断
    for col in data.columns:
        report[f"{col}_type"] = infer_column_type(data[col])

    # 可视化建议
    report["visualization_suggestions"] = suggest_visualizations(data)

    return report
```

**自动生成**:
- 数据类型推断
- 缺失值检测
- 统计摘要
- 可视化建议

---

## 迁移清单

### 必须迁移 (P0)

- [ ] `coordinator.py` - DAG 调度核心
- [ ] `SafePlaceholder` - 防崩溃模式
- [ ] `retrieve_method.py` - 嵌入相似度检索
- [ ] `actor_critic_iteration` - 迭代优化模式

### 强烈推荐 (P1)

- [ ] 类型归一化 - 防止类型不匹配
- [ ] 循环检测 - 防止死锁
- [ ] Memory 管理 - 单数据源模式
- [ ] 动态假设生成 - LLM 驱动分析

### 可选迁移 (P2)

- [ ] `problem_analysis.py` - 问题分析流程
- [ ] `data_description.py` - 数据探索

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
