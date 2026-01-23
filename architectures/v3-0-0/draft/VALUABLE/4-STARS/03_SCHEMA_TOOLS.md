# 4-STARS: Schema 管理与代码守卫

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/03_SCHEMA_TOOLS.md`
> **星级**: ⭐⭐⭐⭐
> **来源文档**: `11_MMAgent_Schema.md`, `15_Utilities.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/schema/`, `utils/schema_*.py`, `utils/code_guards.py`

---

## 核心资产概览

| 模块 | 文件 | 核心功能 |
|------|------|----------|
| **Schema Manager** | `schema_manager.py` | 集中式 Schema 管理 |
| **Schema Registry** | `schema_registry.py` | Schema 注册表 |
| **Schema Normalization** | `schema_normalization.py` | Schema 规范化 |
| **Code Guards** | `code_guards.py` | 预执行验证 |
| **Rate Limiter** | `rate_limiter.py` | API 速率限制 |
| **Variable Contract** | `variable_contract.py` | 变量契约系统 |

---

## 1. Schema Manager (Schema 管理器)

```python
class SchemaManager:
    """
    Schema 管理器: 防止列名不匹配导致的 KeyError
    """
    def __init__(self):
        self.aliases = {}  # {canonical_name: [alias1, alias2, ...]}

    def add_alias(self, canonical: str, alias: str):
        """添加别名映射"""
        if canonical not in self.aliases:
            self.aliases[canonical] = []
        self.aliases[canonical].append(alias)

    def resolve_column(self, df: pd.DataFrame, col: str) -> str:
        """解析列名（支持别名）"""
        if col in df.columns:
            return col

        # 查找别名
        for canonical, aliases in self.aliases.items():
            if col in aliases or canonical in df.columns:
                return canonical if canonical in df.columns else col

        raise KeyError(f"列 '{col}' 不存在")
```

---

## 2. Schema Registry (Schema 注册表)

```python
class SchemaRegistry:
    """
    Schema 注册表: 集中式管理数据集 Schema
    """
    def __init__(self):
        self.schemas = {}  # {dataset_name: {column: type}}

    def register(self, dataset_name: str, schema: dict):
        """注册数据集 Schema"""
        self.schemas[dataset_name] = schema

    def validate_columns(self, dataset_name: str, columns: list) -> bool:
        """验证列名合法性"""
        schema = self.schemas.get(dataset_name, {})
        invalid = [col for col in columns if col not in schema]
        if invalid:
            raise ValueError(f"非法列名: {invalid}")
        return True

# 全局单例
schema_registry = SchemaRegistry()
```

---

## 3. Code Guards (代码守卫)

```python
class CodeGuards:
    """
    代码守卫: 预执行验证层
    """
    def __init__(self):
        self.allowed_imports = {'pandas', 'numpy', 'matplotlib.pyplot'}
        self.allowed_paths = {'../data/', '../output/'}

    def validate_imports(self, code: str) -> bool:
        """验证导入语句"""
        for imp in self.allowed_imports:
            if f"import {imp}" in code:
                continue
        return True

    def validate_paths(self, code: str) -> bool:
        """验证文件路径"""
        for path in self.allowed_paths:
            if path in code:
                continue
        return True

    def pre_execute_check(self, code: str) -> tuple[bool, list]:
        """预执行检查"""
        errors = []

        if not self.validate_imports(code):
            errors.append("存在不合法的导入")

        if not self.validate_paths(code):
            errors.append("存在不合法的路径")

        return len(errors) == 0, errors
```

---

## 4. Rate Limiter (速率限制器)

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

    def acquire(self) -> bool:
        """获取许可"""
        with self.semaphore:
            now = time.time()
            # 移除过期时间戳
            while self.timestamps and self.timestamps[0] < now - 60:
                self.timestamps.popleft()

            # 如果达到限制，等待
            if len(self.timestamps) >= self.requests_per_minute:
                sleep_time = 60 - (now - self.timestamps[0])
                time.sleep(sleep_time)

            self.timestamps.append(now)
            return True
```

---

## 5. Variable Contract (变量契约)

```python
class VariableContract:
    """
    变量契约系统: 多阶段数据一致性
    """
    def __init__(self):
        self.contracts = {}  # {stage: {variable: type}}

    def define_contract(self, stage: str, variable: str, var_type: type):
        """定义变量契约"""
        if stage not in self.contracts:
            self.contracts[stage] = {}
        self.contracts[stage][variable] = var_type

    def validate_contract(self, stage: str, variables: dict) -> bool:
        """验证变量契约"""
        if stage not in self.contracts:
            return True

        for var, expected_type in self.contracts[stage].items():
            if var not in variables:
                raise ValueError(f"变量 '{var}' 缺失")
            if not isinstance(variables[var], expected_type):
                raise TypeError(f"变量 '{var}' 类型错误")
        return True
```

---

## 迁移价值

### P0 - 必须迁移
- [ ] **Schema Registry** - 集中式管理
- [ ] **Code Guards** - 预执行验证
- [ ] **Rate Limiter** - 防止 Error 429

### P1 - 强烈推荐
- [ ] **Schema Manager** - 别名映射
- [ ] **Variable Contract** - 多阶段一致性

### P2 - 可选迁移
- [ ] **Schema Normalization** - 三态分类

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
