# 4-STARS: 核心组件与引擎集合

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/01_CORE_ENGINES.md`
> **星级**: ⭐⭐⭐⭐
> **来源文档**: `05_MMAgent_Core.md`, `06_MMAgent_Engine.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/core/`, `engine/`

---

## 核心资产概览

### Core 组件 (5个)

| 组件 | 文件 | 核心功能 | 迁移难度 |
|------|------|----------|----------|
| **Abduction Engine** | `abduction_engine.py` | 溯因推理 | 高 |
| **Red Team Critic** | `red_team_critic.py` | 红队测试 | 中 |
| **Research Strategist** | `research_strategist.py` | 研究策略 | 高 |
| **FSM** | `research_strategist_fsm.py` | 状态机 | 低 |
| **State Manager** | `state_manager.py` | 状态管理 | 低 |

### Engine 组件 (10个)

| 引擎 | 文件 | 核心功能 | 迁移难度 |
|------|------|----------|----------|
| **Chart Renderer** | `chart_renderer.py` | 图表渲染 | 中 |
| **Diagram Engine** | `diagram_engine.py` | 图表生成 | 中 |
| **Feature Engineer** | `feature_engineer.py` | 特征工程 | 高 |
| **Knowledge Retriever** | `knowledge_retriever.py` | 知识检索 | 高 |
| **Model Arena** | `model_arena.py` | 模型对比 | 中 |
| **Robustness Tester** | `robustness_tester.py` | 鲁棒性测试 | 中 |
| **Scientific Renderer** | `scientific_renderer.py` | 科学渲染 | 低 |
| **Sensitivity Analyzer** | `sensitivity_analyzer.py` | 敏感度分析 | 高 |
| **Sensitivity Engine** | `sensitivity_engine.py` | 敏感度引擎 | 高 |
| **Validation Suite** | `validation_suite.py` | 验证套件 | 中 |

---

## 1. Abduction Engine (溯因推理引擎)

### 为什么是 4 星？

实现了**溯因推理模式**，从观察结果推理最可能的原因，适用于错误诊断、故障排查等场景。

```python
from typing import List, Dict, Tuple

class AbductionEngine:
    """
    溯因推理引擎: 从观察推理原因

    公式: Score = P(observations|hypothesis) × P(hypothesis)
    """
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def abduct(self, observations: Dict[str, Any]) -> List[Tuple[Dict, float]]:
        """
        溯因推理: 找到最能解释观察结果的假设

        Args:
            observations: 观察结果

        Returns:
            按分数排序的假设列表 [(hypothesis, score), ...]
        """
        # 生成候选假设
        hypotheses = self._generate_hypotheses(observations)

        # 评估每个假设
        scored_hypotheses = []
        for hypothesis in hypotheses:
            score = self._score_hypothesis(hypothesis, observations)
            scored_hypotheses.append((hypothesis, score))

        # 按分数排序
        scored_hypotheses.sort(key=lambda x: x[1], reverse=True)

        return scored_hypotheses

    def _score_hypothesis(self, hypothesis: Dict, observations: Dict) -> float:
        """评估假设解释力"""
        # 计算似然性
        likelihood = self._compute_likelihood(hypothesis, observations)

        # 计算先验概率
        prior = self._compute_prior(hypothesis)

        return likelihood * prior

    def _compute_likelihood(self, hypothesis: Dict, observations: Dict) -> float:
        """计算似然性 P(observations|hypothesis)"""
        # 简化实现
        score = 0.0
        for key, value in observations.items():
            if key in hypothesis:
                if hypothesis[key] == value:
                    score += 1.0
        return score / len(observations)

    def _compute_prior(self, hypothesis: Dict) -> float:
        """计算先验概率 P(hypothesis)"""
        # 基于知识库
        return self.knowledge_base.get_prior(hypothesis)
```

**应用场景**:
- 错误诊断: 从错误信息推理根本原因
- 故障排查: 从症状推理故障点
- 调试辅助: 从崩溃信息推理 bug 位置

---

## 2. Red Team Critic (红队批评家)

### 为什么是 4 星？

实现了**红队测试模式**，从攻击者角度评估系统输出，发现潜在问题。

```python
class RedTeamCritic:
    """
    红队批评家: 从攻击者角度评估
    """
    def __init__(self, attack_scenarios: List[Dict]):
        self.attack_scenarios = attack_scenarios

    def critique(self, system_output: Dict) -> Dict:
        """
        评估系统输出，发现潜在问题

        Returns:
            批评报告
        """
        report = {
            'vulnerabilities': [],
            'weaknesses': [],
            'improvements': []
        }

        # 测试各种攻击场景
        for scenario in self.attack_scenarios:
            result = self._test_attack(system_output, scenario)
            if result['success']:
                report['vulnerabilities'].append(result)

        # 评估弱点
        weaknesses = self._identify_weaknesses(system_output)
        report['weaknesses'] = weaknesses

        # 提出改进建议
        improvements = self._suggest_improvements(system_output)
        report['improvements'] = improvements

        return report

    def _test_attack(self, output: Dict, scenario: Dict) -> Dict:
        """测试特定攻击场景"""
        # 实现攻击逻辑
        pass
```

**应用场景**:
- 质量评估: 从批评角度评估输出
- 风险识别: 发现潜在问题
- 改进建议: 提出优化方向

---

## 3. Research Strategist (研究策略家)

### 为什么是 4 星？

实现了**动态策略制定**，根据当前状态和目标制定最优策略。

```python
class ResearchStrategist:
    """
    研究策略家: 动态策略制定
    """
    def __init__(self):
        self.strategies = []

    def plan_strategy(self, current_state: Dict, goal: Dict) -> List[Dict]:
        """
        制定策略

        Args:
            current_state: 当前状态
            goal: 目标

        Returns:
            策略步骤列表
        """
        # 分析差距
        gap = self._analyze_gap(current_state, goal)

        # 制定计划
        plan = self._create_plan(gap)

        return plan

    def _analyze_gap(self, current: Dict, goal: Dict) -> Dict:
        """分析当前状态与目标的差距"""
        gap = {}
        for key in goal:
            if key not in current:
                gap[key] = goal[key]
            elif current[key] != goal[key]:
                gap[key] = goal[key] - current[key]
        return gap
```

**应用场景**:
- 动态规划: 根据状态调整策略
- 资源分配: 优化资源使用
- 任务调度: 动态任务分配

---

## 4. FSM (有限状态机)

### 为什么是 4 星？

实现了**FSM 模式**，管理复杂流程的经典模式。

```python
from enum import Enum

class State(Enum):
    INIT = 'init'
    RUNNING = 'running'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    ERROR = 'error'

class FSM:
    """
    有限状态机
    """
    def __init__(self):
        self.state = State.INIT
        self.transitions = {
            State.INIT: [State.RUNNING, State.ERROR],
            State.RUNNING: [State.PAUSED, State.COMPLETED, State.ERROR],
            State.PAUSED: [State.RUNNING, State.ERROR],
            State.COMPLETED: [],
            State.ERROR: [State.INIT]
        }

    def transition(self, new_state: State) -> bool:
        """状态转移"""
        if new_state in self.transitions[self.state]:
            self.state = new_state
            return True
        return False
```

**应用场景**:
- 流程控制: 管理复杂流程
- 状态管理: 跟踪系统状态
- 错误恢复: 定义错误恢复流程

---

## 5. Feature Engineer (特征工程引擎)

### 为什么是 4 星？

实现了**自动特征工程**，数据分析和机器学习的基础。

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class FeatureEngineer:
    """
    特征工程引擎
    """
    def __init__(self):
        self.scalers = {}
        self.encoders = {}

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """拟合并转换数据"""
        # 数值特征标准化
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            scaler = StandardScaler()
            df[col] = scaler.fit_transform(df[[col]])
            self.scalers[col] = scaler

        # 类别特征编码
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])
            self.encoders[col] = encoder

        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """转换新数据"""
        for col, scaler in self.scalers.items():
            df[col] = scaler.transform(df[[col]])

        for col, encoder in self.encoders.items():
            df[col] = encoder.transform(df[col])

        return df
```

**应用场景**:
- 数据预处理: 标准化、归一化
- 特征创建: 交互特征、多项式特征
- 特征选择: 选择最重要的特征

---

## 6. Knowledge Retriever (知识检索引擎)

### 为什么是 4 星？

实现了**智能知识检索**，从大型知识库中检索相关内容。

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class KnowledgeRetriever:
    """
    知识检索引擎
    """
    def __init__(self, knowledge_base: List[Dict]):
        self.knowledge_base = knowledge_base
        self.embeddings = None
        self._build_index()

    def _build_index(self):
        """构建向量索引"""
        texts = [self._text_for_item(item) for item in self.knowledge_base]
        self.embeddings = self._get_embeddings(texts)

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """检索相关知识"""
        query_embedding = self._get_embedding(query)

        # 计算相似度
        similarities = cosine_similarity(
            query_embedding.reshape(1, -1),
            self.embeddings
        )[0]

        # 获取 top_k
        top_indices = np.argsort(similarities)[::-1][:top_k]

        return [self.knowledge_base[i] for i in top_indices]

    def _get_embedding(self, text: str) -> np.ndarray:
        """获取文本嵌入"""
        # 使用 embedding 模型
        pass
```

**应用场景**:
- 知识检索: 从知识库检索相关内容
- 问答系统: 检索相关答案
- 推荐: 推荐相关内容

---

## 7. Sensitivity Analyzer (敏感度分析器)

### 为什么是 4 星？

实现了**敏感度分析**，评估模型对参数变化的敏感程度。

```python
class SensitivityAnalyzer:
    """
    敏感度分析器
    """
    def analyze(self, model, params: Dict, baseline_result: Dict) -> Dict:
        """
        分析参数敏感度

        Args:
            model: 模型
            params: 参数字典
            baseline_result: 基线结果

        Returns:
            敏感度分析报告
        """
        report = {}

        for param_name, param_value in params.items():
            # 扰动参数
            perturbed_values = self._perturb_param(param_value)

            # 评估影响
            sensitivities = []
            for perturbed_value in perturbed_values:
                new_params = params.copy()
                new_params[param_name] = perturbed_value

                new_result = model(new_params)

                sensitivity = self._compute_sensitivity(baseline_result, new_result)
                sensitivities.append(sensitivity)

            # 计算平均敏感度
            report[param_name] = {
                'mean_sensitivity': np.mean(sensitivities),
                'max_sensitivity': np.max(sensitivities),
                'min_sensitivity': np.min(sensitivities)
            }

        return report

    def _perturb_param(self, value: float) -> List[float]:
        """扰动参数"""
        perturbations = [0.9, 0.95, 1.05, 1.1]
        return [value * p for p in perturbations]

    def _compute_sensitivity(self, baseline: Dict, new_result: Dict) -> float:
        """计算敏感度"""
        # 简化实现: 使用结果差异的绝对值
        key = list(baseline.keys())[0]
        return abs(new_result[key] - baseline[key]) / abs(baseline[key])
```

**应用场景**:
- 参数调优: 识别敏感参数
- 鲁棒性分析: 评估模型鲁棒性
- 风险评估: 识别高风险参数

---

## 迁移价值

### 🔴 P0 - 必须迁移

- [ ] **Abduction Engine** - 诊断分析
- [ ] **FSM** - 流程控制

### 🟡 P1 - 强烈推荐

- [ ] **Red Team Critic** - 质量评估
- [ ] **Feature Engineer** - 特征工程
- [ ] **Knowledge Retriever** - 知识检索
- [ ] **Sensitivity Analyzer** - 敏感度分析

### 🟢 P2 - 可选迁移

- [ ] **Research Strategist** - 动态规划
- [ ] **State Manager** - 状态管理
- [ ] **Chart Renderer** - 图表渲染
- [ ] **Model Arena** - 模型对比
- [ ] **Robustness Tester** - 鲁棒性测试
- [ ] **Validation Suite** - 验证套件

---

## 核心创新点

### Core 组件

1. **溯因推理**: 从观察推理原因
2. **红队测试**: 从攻击者角度评估
3. **动态策略**: 根据状态调整策略
4. **FSM 模式**: 管理复杂流程
5. **状态管理**: 跟踪系统状态

### Engine 组件

1. **自动特征工程**: 数据预处理和特征创建
2. **智能知识检索**: 向量相似度检索
3. **敏感度分析**: 评估参数影响
4. **模型对比**: 多模型性能对比
5. **鲁棒性测试**: 压力测试

---

## 与其他资产的集成

| 资产 | 集成方式 |
|------|----------|
| **autofixer.py** (6-STARS) | Abduction Engine 用于错误诊断 |
| **hmml_embedding.py** (6-STARS) | Knowledge Retriever 使用嵌入 |
| **data_manager.py** (5-STARS) | Feature Engineer 处理数据 |

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
