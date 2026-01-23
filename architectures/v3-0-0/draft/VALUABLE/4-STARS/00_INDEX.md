# 4-STARS: 重要组件精选

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/00_INDEX.md`
> **星级**: ⭐⭐⭐⭐
> **数量**: 6 个详细文档
> **迁移价值**: 值得参考借鉴

---

## 详细文档列表

### 01. 核心组件与引擎集合
**文件**: [`01_CORE_ENGINES.md`](01_CORE_ENGINES.md)

**内容**: core/ (5个组件), engine/ (10个引擎)

**核心创新**:
- Abduction Engine - 溯因推理
- Red Team Critic - 红队测试
- Research Strategist - 动态规划
- FSM - 状态机管理
- Feature Engineer - 特征工程
- Knowledge Retriever - 知识检索
- Sensitivity Analyzer - 敏感度分析

---

### 02. 统一 LLM 接口
**文件**: [`02_UNIFIED_LLM.md`](02_UNIFIED_LLM.md)

**内容**: llm/llm.py

**核心创新**:
- 统一接口支持 10+ 模型
- 线程锁防止 Error 429
- Token 使用跟踪 (LRU 缓存)
- 多提供商支持 (OpenAI, DeepSeek, GLM, Qwen)

---

### 03. Schema 管理与代码守卫
**文件**: [`03_SCHEMA_TOOLS.md`](03_SCHEMA_TOOLS.md)

**内容**: schema/, code_guards, rate_limiter, schema_registry等

**核心创新**:
- Schema Manager - 集中式管理
- Code Guards - 预执行验证
- Rate Limiter - Singleton 速率限制
- Variable Contract - 多阶段一致性

---

### 04. 叙述生成与报告模块
**文件**: [`04_NARRATIVE_REPORTING.md`](04_NARRATIVE_REPORTING.md)

**内容**: narrative/, reporting/

**核心创新**:
- Narrative Weaver - 叙述编织器
- Academic Tools - 学术写作工具
- Critique Generator - 批评生成器
- Abstract Orchestrator - 摘要编排器

---

### 05. 核心工具快照
**文件**: [`05_UTILITY_SNAPSHOT.md`](05_UTILITY_SNAPSHOT.md)

**内容**: utils/ 部分核心工具

**核心创新**:
- Path Guard - 路径保护
- Import Guard - 依赖控制
- Execution FSM - 状态管理
- Safe Merge - 数据合并
- Failure Handler - 失败处理

---

### 06. 基础设施与目录导航
**文件**: [`06_INFRASTRUCTURE.md`](06_INFRASTRUCTURE.md)

**内容**: 00_INDEX.md, MMBench/, evaluation/, test workplace/

**核心创新**:
- 完整架构导航 (22 文档)
- MMBench 数据集 (111 题目)
- 独立评估框架
- 35+ 自动化测试

---

## 1. 核心: 溯因推理引擎 (abduction_engine.py)

### 为什么是 4 星？

实现了**溯因推理模式**，可以用于诊断分析、根因分析等场景。

```python
class AbductionEngine:
    """
    溯因推理引擎: 从观察结果推理最可能的原因

    Args:
        observations: 观察结果
        knowledge_base: 知识库 (可能的假设)
    """
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def abduct(self, observations):
        """
        溯因推理: 找到最能解释观察结果的假设

        Returns:
            最可能的假设列表，按概率排序
        """
        # 生成所有可能的假设
        hypotheses = self._generate_hypotheses(observations)

        # 评估每个假设的解释力
        scored_hypotheses = []
        for hypothesis in hypotheses:
            score = self._score_hypothesis(hypothesis, observations)
            scored_hypotheses.append((hypothesis, score))

        # 按分数排序
        scored_hypotheses.sort(key=lambda x: x[1], reverse=True)

        return scored_hypotheses

    def _generate_hypotheses(self, observations):
        """生成可能的假设"""
        return self.knowledge_base.get_relevant_hypotheses(observations)

    def _score_hypothesis(self, hypothesis, observations):
        """
        评估假设的解释力

        Score = P(observations|hypothesis) * P(hypothesis)
        """
        # 计算似然性
        likelihood = self._compute_likelihood(hypothesis, observations)

        # 计算先验概率
        prior = self._compute_prior(hypothesis)

        return likelihood * prior
```

**应用场景**:
- 错误诊断: 从错误信息推理根本原因
- 故障排查: 从症状推理故障点
- 调试辅助: 从崩溃信息推理 bug 位置

---

## 2. 核心: 红队批评家 (red_team_critic.py)

### 为什么是 4 星？

实现了**红队测试模式**，可以用于质量评估和风险识别。

```python
class RedTeamCritic:
    """
    红队批评家: 从攻击者角度评估系统

    Args:
        system: 待评估的系统
        attack_scenarios: 攻击场景列表
    """
    def __init__(self, attack_scenarios):
        self.attack_scenarios = attack_scenarios

    def critique(self, system_output):
        """
        评估系统输出，发现潜在问题

        Returns:
            批评报告，包含发现的问题
        """
        critique_report = {
            'vulnerabilities': [],
            'weaknesses': [],
            'improvements': []
        }

        # 尝试各种攻击场景
        for scenario in self.attack_scenarios:
            result = self._test_attack(system_output, scenario)
            if result['success']:
                critique_report['vulnerabilities'].append(result)

        # 评估弱点
        weaknesses = self._identify_weaknesses(system_output)
        critique_report['weaknesses'] = weaknesses

        # 提出改进建议
        improvements = self._suggest_improvements(system_output)
        critique_report['improvements'] = improvements

        return critique_report

    def _test_attack(self, system_output, scenario):
        """测试特定攻击场景"""
        # 实现攻击逻辑
        pass

    def _identify_weaknesses(self, system_output):
        """识别系统弱点"""
        # 实现弱点识别
        pass

    def _suggest_improvements(self, system_output):
        """提出改进建议"""
        # 实现改进建议
        pass
```

**应用场景**:
- 质量评估: 从批评角度评估输出
- 风险识别: 发现潜在问题
- 改进建议: 提出优化方向

---

## 3. 引擎: 统一 LLM 接口 (llm.py)

### 为什么是 4 星？

实现了**统一 LLM 接口**，支持多模型、多提供商，使用线程锁防止 Error 429。

```python
import threading

class LLM:
    """
    统一 LLM 接口

    支持的提供商:
    - OpenAI: gpt-4o, gpt-4-turbo
    - DeepSeek: deepseek-chat
    - GLM: glm-4-flash, glm-4-plus
    - Qwen: qwen2.5-72b-instruct
    """
    def __init__(self, model_name, api_key, base_url=None):
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url

        # 线程锁: 防止并发调用导致 Error 429
        self.lock = threading.Lock()

        # Token 使用跟踪
        self.usage_cache = LRUCache(maxsize=1000)

    def generate(self, prompt, system=None, temperature=0.7):
        """
        生成 LLM 响应

        Args:
            prompt: 用户提示词
            system: 系统提示词
            temperature: 温度参数

        Returns:
            LLM 响应
        """
        # 加锁: 序列化所有 API 调用
        with self.lock:
            # 调用 LLM API
            response = self._call_api(prompt, system, temperature)

            # 记录 Token 使用
            self._track_usage(response)

            return response

    def _call_api(self, prompt, system, temperature):
        """调用 LLM API"""
        # 根据 model_name 选择对应的 API
        if 'gpt' in self.model_name:
            return self._call_openai(prompt, system, temperature)
        elif 'deepseek' in self.model_name:
            return self._call_deepseek(prompt, system, temperature)
        elif 'glm' in self.model_name:
            return self._call_glm(prompt, system, temperature)
        elif 'qwen' in self.model_name:
            return self._call_qwen(prompt, system, temperature)
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")

    def _track_usage(self, response):
        """记录 Token 使用"""
        prompt_tokens = response['usage']['prompt_tokens']
        completion_tokens = response['usage']['completion_tokens']
        total_tokens = response['usage']['total_tokens']

        self.usage_cache[self.model_name] = {
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total_tokens
        }
```

**关键设计**:
1. **线程锁**: `self.lock = threading.Lock()` 防止并发调用
2. **多模型支持**: 统一接口支持 10+ 模型
3. **Token 跟踪**: `LRUCache` 记录使用情况
4. **错误处理**: 统一的错误处理和重试

**迁移价值**:
- **防 Error 429**: 线程锁序列化所有 API 调用
- **多模型**: 可以轻松切换不同模型
- **成本控制**: Token 跟踪帮助控制成本

---

## 4. 工具: 速率限制器 (rate_limiter.py)

### 为什么是 4 星？

实现了 **Singleton 模式** 的速率限制器，防止 API 速率限制问题。

```python
import time
import threading
from collections import deque

class RateLimiter:
    """
    速率限制器: Singleton 模式

    限制: 每分钟最多 60 个请求
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, requests_per_minute=60):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize(requests_per_minute)
        return cls._instance

    def _initialize(self, requests_per_minute):
        self.requests_per_minute = requests_per_minute
        self.interval = 60 / requests_per_minute
        self.timestamps = deque()
        self.semaphore = threading.Semaphore(requests_per_minute)

    def acquire(self):
        """
        获取许可，如果超过速率限制则等待

        Returns:
            True 如果获得许可
        """
        with self.semaphore:
            # 移除过期的请求时间戳
            now = time.time()
            while self.timestamps and self.timestamps[0] < now - 60:
                self.timestamps.popleft()

            # 如果达到限制，等待
            if len(self.timestamps) >= self.requests_per_minute:
                sleep_time = 60 - (now - self.timestamps[0])
                time.sleep(sleep_time)

            # 记录当前请求时间戳
            self.timestamps.append(now)

            return True
```

**关键设计**:
1. **Singleton 模式**: 确保全局只有一个实例
2. **Semaphore 并发控制**: 限制并发请求数
3. **滑动窗口**: 使用 deque 维护请求时间戳

---

## 5. 工具: Schema 注册表 (schema_registry.py)

### 为什么是 4 星？

实现了**集中式 Schema 管理**，防止数据不一致。

```python
class SchemaRegistry:
    """
    Schema 注册表: 集中式管理数据集 Schema
    """
    def __init__(self):
        self.schemas = {}  # {dataset_name: {column: type}}

    def register(self, dataset_name, schema):
        """注册数据集 Schema"""
        self.schemas[dataset_name] = schema

    def get_schema(self, dataset_name):
        """获取数据集 Schema"""
        return self.schemas.get(dataset_name, {})

    def validate_columns(self, dataset_name, columns):
        """验证列名合法性"""
        schema = self.get_schema(dataset_name)
        invalid_cols = [col for col in columns if col not in schema]
        if invalid_cols:
            raise ValueError(f"Invalid columns: {invalid_cols}")
        return True

    def get_column_type(self, dataset_name, column):
        """获取列类型"""
        schema = self.get_schema(dataset_name)
        return schema.get(column, None)

# 全局单例
schema_registry = SchemaRegistry()
```

**用途**:
- **防止列名幻觉**: LLM 必须基于注册的 Schema 生成代码
- **类型验证**: 验证数据类型是否匹配
- **集中管理**: 所有 Schema 在一个地方管理

---

## 迁移清单

### 🔴 P0 - 必须迁移

- [ ] **统一 LLM 接口** - 多模型支持 + 线程锁
- [ ] **速率限制器** - 防止 Error 429

### 🟡 P1 - 强烈推荐

- [ ] **Schema 注册表** - 集中式 Schema 管理
- [ ] **变量契约系统** - 多阶段数据一致性
- [ ] **代码守卫** - 预执行验证

### 🟢 P2 - 可选迁移

- [ ] **溯因推理引擎** - 诊断分析
- [ ] **红队批评家** - 质量评估
- [ ] **叙述生成模块** - 科研写作
- [ ] **报告生成框架** - 多格式报告

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**详细分析**: 见原始文档 `../../LLM-MM-Agent/` 目录
