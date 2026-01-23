# 6-STARS: 工具集核心资产

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/6-STARS/03_UTILITY_COLLECTIONS.md`
> **星级**: ⭐⭐⭐⭐⭐⭐
> **来源文档**: `15_Utilities.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/`

---

## 核心资产概览

| 模块 | 文件 | 核心功能 | 创新点 |
|------|------|----------|--------|
| 数学建模 | `mathematical_modeling.py` | 建模流程 + Context Pruning | 智能依赖上下文管理 |
| 计算求解 | `computational_solving.py` | 求解引擎 + Schema Registry | 单一数据源模式 |
| 问题分析 | `problem_analysis.py` | 动态分析 + 假设生成 | LLM 驱动分析 |
| 数据管理 | `data_manager.py` | 数据快照 + Schema 管理 | 防止数据幻觉 |
| 自愈机制 | `autofixer.py` | 错误恢复基础设施 | 3 层自愈模式 |
| 嵌入相似度 | `embedding.py` | 向量检索引擎 | FAISS 加速 |
| 自动评估 | `auto_evaluation.py` | 质量评估框架 | 多维度评估 |

---

## 1. 数学建模流程 (mathematical_modeling.py)

### 为什么是 6 星？

实现了 **Context Pruning Strategy**（远近亲疏策略），这是智能依赖上下文管理的核心创新。

### Context Pruning Strategy

```python
def get_dependency_prompt(task_id, dependencies, memory):
    """
    Context Pruning: 根据依赖远近调整上下文详细程度

    策略:
    - 直接前驱 (task_id - 1): 完整上下文 + 字符限制
    - 其他依赖: 最小上下文 (仅结果 + 文件输出)

    Args:
        task_id: 当前任务 ID
        dependencies: 依赖任务 ID 列表
        memory: 任务结果存储

    Returns:
        精简后的上下文字符串
    """
    context_parts = []

    for dep_id in dependencies:
        dep_result = memory.get(dep_id)

        # 判断依赖距离
        distance = task_id - dep_id

        if distance == 1:
            # 直接前驱: 完整上下文 (限制 2000 字符)
            full_context = format_full_context(dep_result)
            context_parts.append(truncate(full_context, 2000))
        else:
            # 其他依赖: 最小上下文
            minimal_context = format_minimal_context(dep_result)
            context_parts.append(minimal_context)

    return "\n\n".join(context_parts)

def format_minimal_context(result):
    """
    最小上下文: 仅包含结果和文件输出
    """
    return f"""
Task {result['task_id']} Results:
- Output: {result['output'][:500]}
- Files: {result.get('file_outputs', [])}
"""
```

**远近亲疏策略**:
- **近** (直接前驱): 完整上下文，2000 字符限制
- **远** (其他依赖): 最小上下文，仅结果 + 文件
- **亲**: 优先级高的依赖给予更多上下文
- **疏**: 优先级低的依赖给予最少上下文

**优势**:
1. **防止上下文溢出**: 智能裁剪长上下文
2. **保持关键信息**: 直接前驱获得完整信息
3. **降低 Token 成本**: 减少不必要的上下文

### 数学建模 4 阶段流程

```python
def mathematical_modeling_pipeline(problem):
    """
    数学建模 4 阶段流程

    Stage 1: Problem Analysis
    Stage 2: Method Selection (from HMML)
    Stage 3: Computational Solving
    Stage 4: Solution Reporting
    """
    # Stage 1: 问题分析
    analysis = analyze_problem(problem)

    # Stage 2: 方法选择
    methods = retrieve_methods_from_hmml(analysis)

    # Stage 3: 计算求解
    solution = solve_computationally(methods, problem)

    # Stage 4: 结果报告
    report = generate_report(solution)

    return report
```

---

## 2. 计算求解引擎 (computational_solving.py)

### 为什么是 6 星？

实现了 **Schema Registry**（模式注册表），防止 LLM 产生幻觉列名，这是单一数据源模式的核心。

### Schema Registry

```python
class SchemaRegistry:
    """
    Schema 注册表: 防止 LLM 产生幻觉列名
    """
    def __init__(self):
        self.schemas = {}  # {dataset_name: {column: type}}

    def register_schema(self, dataset_name, schema):
        """注册数据集的 Schema"""
        self.schemas[dataset_name] = schema

    def get_schema(self, dataset_name):
        """获取数据集的 Schema"""
        return self.schemas.get(dataset_name, {})

    def validate_columns(self, dataset_name, columns):
        """验证列名是否合法"""
        schema = self.get_schema(dataset_name)
        invalid_cols = [col for col in columns if col not in schema]
        if invalid_cols:
            raise ValueError(f"Invalid columns: {invalid_cols}")
        return True

# 全局单例
schema_registry = SchemaRegistry()
```

**单一数据源模式**:
1. **数据加载时注册 Schema**: 数据加载后立即注册到 Schema Registry
2. **代码生成时查询 Schema**: 生成代码前查询合法列名
3. **执行时验证列名**: 执行代码前验证列名合法性

### 数据快照机制

```python
class DataSnapshot:
    """
    数据快照: 记录数据集的某个时间点的状态
    """
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.timestamp = datetime.now()
        self.schema = self._extract_schema()
        self.sample = self._extract_sample()
        self.statistics = self._compute_statistics()

    def _extract_schema(self):
        """提取 Schema"""
        data = pd.read_csv(self.dataset_path)
        return {
            col: str(dtype)
            for col, dtype in data.dtypes.items()
        }

    def _extract_sample(self, n=5):
        """提取样本数据"""
        data = pd.read_csv(self.dataset_path)
        return data.head(n).to_dict()

    def _compute_statistics(self):
        """计算统计信息"""
        data = pd.read_csv(self.dataset_path)
        return data.describe().to_dict()
```

**用途**:
- **防止列名幻觉**: LLM 必须基于快照生成代码
- **版本控制**: 记录数据集的演变历史
- **调试辅助**: 快速查看数据集状态

### 3 层目录组织

```
output/
├── json/          # JSON 格式的结果
├── markdown/      # Markdown 格式的报告
├── latex/         # LaTeX 格式的论文
├── code/          # 生成的代码
└── charts/        # 生成的图表
```

**清晰分离**: 不同格式的内容分开存储

---

## 3. 自愈机制 (autofixer.py)

### 为什么是 6 星？

实现了 **3 层自愈模式**，从快速修复到彻底修复，这是系统鲁棒性的关键。

### 3 层自愈模式

```python
class AutoFixer:
    """
    3 层自愈模式:
    Layer 1: 快速修复 (常见错误)
    Layer 2: 中度修复 (LLM 辅助)
    Layer 3: 深度修复 (完整诊断)
    """

    def fix(self, code, error):
        """
        尝试修复代码错误

        Args:
            code: 错误代码
            error: 错误信息

        Returns:
            修复后的代码或 None
        """
        # Layer 1: 快速修复
        fixed_code = self._layer1_fix(code, error)
        if fixed_code:
            return fixed_code

        # Layer 2: 中度修复
        fixed_code = self._layer2_fix(code, error)
        if fixed_code:
            return fixed_code

        # Layer 3: 深度修复
        fixed_code = self._layer3_fix(code, error)
        return fixed_code

    def _layer1_fix(self, code, error):
        """
        Layer 1: 快速修复 (规则匹配)
        - 常见语法错误
        - 缺失导入
        - 路径错误
        """
        # 缺失导入
        if "NameError" in str(error):
            missing_var = extract_missing_var(error)
            return add_import(code, missing_var)

        # 路径错误
        if "FileNotFoundError" in str(error):
            return fix_paths(code)

        # 语法错误
        if "SyntaxError" in str(error):
            return fix_syntax(code)

        return None

    def _layer2_fix(self, code, error):
        """
        Layer 2: 中度修复 (LLM 辅助)
        - 逻辑错误
        - 类型错误
        - 运行时错误
        """
        prompt = f"""
Fix this code:
{code}

Error:
{error}

Provide only the fixed code.
"""
        fixed_code = llm_generate(prompt)
        return fixed_code

    def _layer3_fix(self, code, error):
        """
        Layer 3: 深度修复 (完整诊断)
        - 复杂错误
        - 设计问题
        - 架构问题
        """
        # 完整诊断
        diagnosis = diagnose_error(code, error)

        # 生成修复方案
        solution = generate_solution(diagnosis)

        # 应用修复
        fixed_code = apply_fix(code, solution)

        return fixed_code
```

**渐进式修复**:
1. **快速修复**: 规则匹配，毫秒级响应
2. **中度修复**: LLM 辅助，秒级响应
3. **深度修复**: 完整诊断，分钟级响应

---

## 4. 嵌入相似度 (embedding.py)

### 为什么是 6 星？

实现了 **FAISS 加速的向量检索**，支持大规模知识检索。

### FAISS 索引

```python
import faiss
import numpy as np

class EmbeddingRetriever:
    """
    使用 FAISS 加速向量检索
    """
    def __init__(self, embedding_dim=768):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []

    def add_documents(self, documents):
        """
        添加文档到索引

        Args:
            documents: 文档列表
        """
        # 生成嵌入
        embeddings = [
            get_embedding(doc)
            for doc in documents
        ]
        embeddings = np.array(embeddings).astype('float32')

        # 添加到索引
        self.index.add(embeddings)
        self.documents.extend(documents)

    def retrieve(self, query, top_k=6):
        """
        检索最相关的文档

        Args:
            query: 查询文本
            top_k: 返回前 k 个文档

        Returns:
            top_k 个最相关的文档
        """
        # 生成查询嵌入
        query_embedding = get_embedding(query)
        query_embedding = np.array([query_embedding]).astype('float32')

        # 检索
        distances, indices = self.index.search(query_embedding, top_k)

        # 返回文档
        results = [
            self.documents[i]
            for i in indices[0]
        ]

        return results
```

**FAISS 优势**:
- **速度快**: 比暴力搜索快 1000 倍
- **可扩展**: 支持十亿级向量
- **内存效率**: 压缩索引减少内存占用

---

## 5. 自动评估 (auto_evaluation.py)

### 为什么是 6 星？

实现了 **多维度质量评估**，这是系统健康检查的核心。

### 多维度评估

```python
def auto_evaluation(output_dir):
    """
    多维度自动评估

    Dimensions:
    1. Completeness: 是否所有阶段都完成
    2. Correctness: 结果是否正确
    3. Consistency: 结果是否一致
    4. Quality: 结果质量如何
    """
    evaluation = {
        'completeness': evaluate_completeness(output_dir),
        'correctness': evaluate_correctness(output_dir),
        'consistency': evaluate_consistency(output_dir),
        'quality': evaluate_quality(output_dir)
    }

    # 计算总分
    total_score = sum(evaluation.values()) / len(evaluation)

    # 生成报告
    report = generate_evaluation_report(evaluation, total_score)

    return report

def evaluate_completeness(output_dir):
    """
    评估完整性: 是否所有阶段都完成
    """
    required_files = [
        'problem_analysis.json',
        'method_selection.json',
        'computational_results.json',
        'final_report.pdf'
    ]

    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join(output_dir, file)):
            missing_files.append(file)

    if missing_files:
        return 0.0
    else:
        return 1.0

def evaluate_correctness(output_dir):
    """
    评估正确性: 结果是否正确
    """
    # 加载结果
    results = load_results(output_dir)

    # 检查关键指标
    if 'error' in results:
        return 0.0

    # 检查输出格式
    if not validate_output_format(results):
        return 0.5

    return 1.0

def evaluate_consistency(output_dir):
    """
    评估一致性: 结果是否一致
    """
    # 加载所有阶段结果
    all_results = load_all_results(output_dir)

    # 检查阶段间一致性
    inconsistencies = check_consistency(all_results)

    if inconsistencies:
        return 0.5
    else:
        return 1.0

def evaluate_quality(output_dir):
    """
    评估质量: 结果质量如何
    """
    # 加载结果
    results = load_results(output_dir)

    # 评估维度
    scores = []

    # 1. 结果详细程度
    detail_score = evaluate_detail(results)
    scores.append(detail_score)

    # 2. 可视化质量
    viz_score = evaluate_visualizations(output_dir)
    scores.append(viz_score)

    # 3. 报告质量
    report_score = evaluate_report(output_dir)
    scores.append(report_score)

    return sum(scores) / len(scores)
```

---

## 迁移清单

### 必须迁移 (P0)

- [ ] **Context Pruning Strategy** - 智能依赖上下文管理
- [ ] **Schema Registry** - 单一数据源模式
- [ ] **数据快照机制** - 防止列名幻觉
- [ ] **3 层自愈模式** - 渐进式错误恢复
- [ ] **FAISS 向量检索** - 大规模知识检索
- [ ] **多维度评估** - 系统健康检查

### 强烈推荐 (P1)

- [ ] **4 阶段流程** - 标准化建模流程
- [ ] **3 层目录组织** - 清晰分离
- [ ] **渐进式修复** - Layered Fixing

### 可选迁移 (P2)

- [ ] **动态假设生成** - LLM 驱动分析
- [ ] **完整诊断** - 深度错误分析

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
