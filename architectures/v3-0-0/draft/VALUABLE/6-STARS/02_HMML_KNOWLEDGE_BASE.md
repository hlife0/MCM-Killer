# 6-STARS: HMML 知识库

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/6-STARS/02_HMML_KNOWLEDGE_BASE.md`
> **星级**: ⭐⭐⭐⭐⭐⭐
> **来源文档**: `14_HMML.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/HMML/`

---

## 核心资产: HMML (Hierarchical Mathematical Modeling Library)

### 为什么是 6 星？

HMML 是 LLM-MM-Agent 的**核心创新**，是**首个 3 层级数学建模知识库**，包含 98+ 数学建模模式。这是系统的独特资产，没有任何其他系统拥有类似的知识库。

### HMML 结构

```
HMML/
├── 📄 HMML.md          # Markdown 格式的知识库
└── 📄 HMML.json        # JSON 格式的知识库（程序化访问）
```

---

## 1. HMML.md (Markdown 格式)

### 3 层层级结构

```
HMML/
├── Domains (1级)           # 6 个域
│   ├── Optimization
│   ├── Differential Equations
│   ├── Data Analysis
│   ├── Graph Theory
│   ├── Probability & Statistics
│   └── Machine Learning
│
├── Subdomains (2级)        # 20+ 个子域
│   ├── Linear Programming
│   ├── Nonlinear Programming
│   ├── ODE
│   ├── PDE
│   ├── Regression
│   ├── Classification
│   └── ...
│
└── Methods (3级)           # 98+ 方法节点
    ├── Simplex Method
    ├── Gradient Descent
    ├── Euler Method
    ├── Runge-Kutta
    ├── Linear Regression
    ├── Logistic Regression
    └── ...
```

### 方法节点结构

每个方法节点包含：

```markdown
# Method Name

## Description
详细的方法描述

## Mathematical Formulation
数学公式和符号定义

## Algorithm Steps
算法步骤

## Applicable Problems
适用的问题类型

## Implementation Notes
实现注意事项

## References
参考文献
```

**示例**: Linear Regression

```markdown
# Linear Regression

## Description
线性回归是一种用于建模因变量与自变量之间线性关系的统计方法。

## Mathematical Formulation
$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \epsilon$$

其中：
- $y$ 是因变量
- $x_1, x_2, ..., x_n$ 是自变量
- $\beta_0, \beta_1, ..., \beta_n$ 是回归系数
- $\epsilon$ 是误差项

## Algorithm Steps
1. 数据收集和预处理
2. 计算回归系数：$\beta = (X^T X)^{-1} X^T y$
3. 模型评估：$R^2$, RMSE
4. 预测

## Applicable Problems
- 预测连续值
- 变量关系分析
- 趋势预测

## Implementation Notes
- 使用 `sklearn.linear_model.LinearRegression`
- 注意多重共线性
- 检查残差正态性

## References
- [1] Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning.
```

---

## 2. HMML.json (JSON 格式)

### 结构示例

```json
{
  "HMML": {
    "version": "1.0",
    "total_methods": 98,
    "domains": [
      {
        "id": "optimization",
        "name": "Optimization",
        "description": "优化方法",
        "subdomains": [
          {
            "id": "linear_programming",
            "name": "Linear Programming",
            "methods": [
              {
                "id": "simplex_method",
                "name": "Simplex Method",
                "description": "单纯形法",
                "formulation": "...",
                "steps": ["...", "..."],
                "applicable_problems": ["...", "..."],
                "implementation_notes": "...",
                "references": ["...", "..."]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### 程序化访问

```python
import json

with open('HMML.json', 'r') as f:
    hmml = json.load(f)

# 遍历所有方法
for domain in hmml['HMML']['domains']:
    for subdomain in domain['subdomains']:
        for method in subdomain['methods']:
            print(f"{method['name']}: {method['description']}")
```

---

## 3. 嵌入相似度检索

### 核心算法

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_methods(query, hmml_json, top_k=6):
    """
    使用嵌入相似度检索相关方法

    Args:
        query: 查询文本
        hmml_json: HMML JSON 数据
        top_k: 返回前 k 个最相关的方法

    Returns:
        top_k 个最相关的方法列表
    """
    # 提取所有方法
    methods = []
    for domain in hmml_json['HMML']['domains']:
        for subdomain in domain['subdomains']:
            methods.extend(subdomain['methods'])

    # 生成方法嵌入（预计算）
    method_embeddings = []
    for method in methods:
        embedding = get_embedding(
            method['name'] + ' ' +
            method['description'] + ' ' +
            method['applicable_problems'][0]
        )
        method_embeddings.append(embedding)

    method_embeddings = np.array(method_embeddings)

    # 生成查询嵌入
    query_embedding = get_embedding(query)

    # 计算余弦相似度
    similarities = cosine_similarity(
        query_embedding.reshape(1, -1),
        method_embeddings
    )[0]

    # 获取 top_k 索引
    top_indices = np.argsort(similarities)[::-1][:top_k]

    # 返回对应的方法
    top_methods = [methods[i] for i in top_indices]

    return top_methods
```

### 优势

1. **语义匹配**: 比关键词匹配更智能
   - 查询 "如何优化生产计划" → 检索到 "Linear Programming"
   - 查询 "预测股票价格" → 检索到 "Time Series Analysis"

2. **多语言支持**: 嵌入向量支持跨语言检索
   - 中文查询 → 英文方法
   - 英文查询 → 中文方法

3. **可扩展**: 支持大规模向量检索
   - 使用 FAISS 加速
   - 支持分布式检索

---

## 4. 扩展到 400+ 方法

### 当前 vs 目标

| 维度 | 当前 | 目标 |
|------|------|------|
| 方法数量 | 98+ | 400+ |
| 层级深度 | 3 层 | 5 层 |
| 域数量 | 6 | 10+ |
| 子域数量 | 20+ | 50+ |

### 5 层层级结构

```
HMML/
├── Domains (1级)           # 10+ 个域
│
├── Subdomains (2级)        # 50+ 个子域
│
├── Method Categories (3级)  # 150+ 个方法类别
│   ├── Unconstrained Optimization
│   ├── Constrained Optimization
│   ├── Stochastic Optimization
│   └── ...
│
├── Methods (4级)           # 400+ 个方法
│   ├── Gradient Descent
│   ├── Newton's Method
│   ├── Simulated Annealing
│   └── ...
│
└── Method Variants (5级)   # 1000+ 个方法变体
    ├── Gradient Descent (Batch)
    ├── Gradient Descent (Stochastic)
    ├── Gradient Descent (Mini-batch)
    └── ...
```

### 扩展策略

#### 1. 方法注册机制

```python
class HMMLRegistry:
    """HMML 方法注册表"""

    def __init__(self):
        self.methods = {}
        self.embeddings = {}
        self.index = None

    def register_method(self, method):
        """注册新方法"""
        method_id = method['id']
        self.methods[method_id] = method

        # 生成并缓存嵌入
        embedding = get_embedding(
            method['name'] + ' ' +
            method['description']
        )
        self.embeddings[method_id] = embedding

        # 更新向量索引
        self._update_index()

    def retrieve(self, query, top_k=6):
        """检索相关方法"""
        query_embedding = get_embedding(query)

        # 使用 FAISS 检索
        distances, indices = self.index.search(
            query_embedding.reshape(1, -1),
            top_k
        )

        return [self.methods[i] for i in indices[0]]
```

#### 2. 动态方法发现

```python
def discover_methods_from_papers(papers):
    """
    从论文中自动发现新方法

    Args:
        papers: 论文列表

    Returns:
        新方法列表
    """
    new_methods = []

    for paper in papers:
        # 提取方法名称
        method_names = extract_method_names(paper)

        # 提取方法描述
        method_descriptions = extract_method_descriptions(paper)

        # 提取数学公式
        formulations = extract_formulations(paper)

        # 组装方法
        for name, desc, form in zip(
            method_names,
            method_descriptions,
            formulations
        ):
            method = {
                'id': slugify(name),
                'name': name,
                'description': desc,
                'formulation': form,
                'source': paper['citation']
            }
            new_methods.append(method)

    return new_methods
```

#### 3. 方法分类和索引

```python
def classify_method(method):
    """
    自动分类方法到层级结构

    Args:
        method: 方法字典

    Returns:
        分类路径 (domain, subdomain, category)
    """
    # 使用嵌入相似度找到最相似的域
    domain = find_most_similar_domain(method)

    # 在域内找到最相似的子域
    subdomain = find_most_similar_subdomain(
        method,
        domain
    )

    # 在子域内找到最相似的类别
    category = find_most_similar_category(
        method,
        subdomain
    )

    return (domain, subdomain, category)
```

---

## 5. 迁移价值

### 必须迁移 (P0)

- [ ] **HMML 结构** - 3 层层级架构
- [ ] **嵌入相似度检索** - 语义匹配方法
- [ ] **方法节点结构** - 标准化方法描述

### 强烈推荐 (P1)

- [ ] **JSON 格式** - 程序化访问
- [ ] **Markdown 格式** - 人类可读
- [ ] **方法注册机制** - 动态扩展

### 可选迁移 (P2)

- [ ] **方法发现** - 从论文自动提取
- [ ] **方法分类** - 自动分类到层级
- [ ] **向量索引** - FAISS 加速检索

---

## 6. 核心创新点

1. **首个 3 层级数学建模知识库** - 98+ 方法
2. **嵌入相似度检索** - 语义匹配方法
3. **标准化方法描述** - 一致的结构
4. **程序化访问** - JSON 格式
5. **可扩展架构** - 支持 400+ 方法

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
