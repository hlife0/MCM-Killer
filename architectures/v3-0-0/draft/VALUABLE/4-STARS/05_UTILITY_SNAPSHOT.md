# 4-STARS: 核心工具快照

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/05_UTILITY_SNAPSHOT.md`
> **星级**: ⭐⭐⭐⭐
> **来源文档**: `15_Utilities.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/`

---

## 核心工具概览

utils/ 目录包含 40+ 工具模块，以下是核心工具快照：

### 数据处理工具 (6星)

已在 6-STARS/03_UTILITY_COLLECTIONS.md 中详细说明：
- `mathematical_modeling.py` - Context Pruning 策略
- `computational_solving.py` - Schema Registry
- `data_manager.py` - 单一数据源模式
- `autofixer.py` - 3 层自愈机制
- `embedding.py` - FAISS 向量检索
- `auto_evaluation.py` - 自动评估框架

### 事件追踪工具 (5星)

已在 5-STARS/02_EVENT_TRACKING.md 中详细说明：
- `execution_tracker.py` - Truth Mode 日志
- `latent_reporter.py` - 法医式尸检

### 代码修复工具 (5星)

已在 5-STARS/03_CODE_FIXING.md 中详细说明：
- `syntax_fixer.py` - 语法修复
- `json_utils.py` - JSON 解析

---

## 其他重要工具 (4星)

### 1. Path Guard (路径守卫)

```python
class PathGuard:
    """
    路径守卫: 防止路径违规
    """
    def __init__(self, allowed_paths: set):
        self.allowed_paths = allowed_paths

    def validate_path(self, path: str) -> bool:
        """验证路径是否合法"""
        for allowed in self.allowed_paths:
            if path.startswith(allowed):
                return True
        return False
```

### 2. Import Guard (导入守卫)

```python
class ImportGuard:
    """
    导入守卫: 控制代码依赖
    """
    def __init__(self, whitelist: set, blacklist: set):
        self.whitelist = whitelist
        self.blacklist = blacklist

    def validate_imports(self, code: str) -> tuple[bool, list]:
        """验证导入"""
        imports = self._extract_imports(code)

        violations = []
        for imp in imports:
            if imp in self.blacklist:
                violations.append(f"禁止导入: {imp}")
            elif self.whitelist and imp not in self.whitelist:
                violations.append(f"未授权导入: {imp}")

        return len(violations) == 0, violations
```

### 3. Execution FSM (执行状态机)

```python
class ExecutionFSM:
    """
    执行状态机: 管理代码执行状态
    """
    def __init__(self):
        self.state = 'idle'
        self.transitions = {
            'idle': ['running'],
            'running': ['completed', 'error', 'timeout'],
            'completed': ['idle'],
            'error': ['idle', 'retry'],
            'timeout': ['idle', 'retry']
        }

    def transition(self, new_state: str) -> bool:
        """状态转移"""
        if new_state in self.transitions.get(self.state, []):
            self.state = new_state
            return True
        return False
```

### 4. Safe Merge (安全合并)

```python
def safe_merge(df1: pd.DataFrame, df2: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """
    安全合并 DataFrame

    提供详细的错误信息
    """
    try:
        return pd.merge(df1, df2, **kwargs)
    except Exception as e:
        # 诊断信息
        print(f"Merge failed: {e}")
        print(f"df1 columns: {df1.columns.tolist()}")
        print(f"df2 columns: {df2.columns.tolist()}")
        print(f"Merge keys: {kwargs.get('on', 'not specified')}")
        raise e
```

### 5. Failure Handler (失败处理器)

```python
class FailureHandler:
    """
    失败处理器: 确保最小输出
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.failure_log = os.path.join(output_dir, 'failure_log.json')

    def handle_failure(self, error: Exception, context: dict):
        """处理失败"""
        failure_record = {
            'timestamp': datetime.now().isoformat(),
            'error': str(error),
            'type': type(error).__name__,
            'context': context
        }

        # 保存失败记录
        with open(self.failure_log, 'a') as f:
            f.write(json.dumps(failure_record) + '\n')

        # 确保最小输出
        self._ensure_minimal_output()

    def _ensure_minimal_output(self):
        """确保最小输出"""
        minimal_output = os.path.join(self.output_dir, 'minimal_output.txt')
        if not os.path.exists(minimal_output):
            with open(minimal_output, 'w') as f:
                f.write("System failed. Check failure_log.json for details.")
```

---

## 工具分类

| 类别 | 工具数量 | 代表工具 |
|------|----------|----------|
| **数据处理** | 10+ | data_manager, column_normalization |
| **代码安全** | 8+ | code_guards, ast_validator, import_guard |
| **错误恢复** | 6+ | autofixer, failure_handler |
| **Schema 管理** | 5+ | schema_manager, schema_registry |
| **事件追踪** | 3+ | execution_tracker, latent_reporter |
| **其他** | 8+ | rate_limiter, embedding, json_utils |

---

## 迁移优先级

### P0 - 必须迁移
已在 6-STARS 和 5-STARS 中详细说明

### P1 - 强烈推荐
- [ ] **Path Guard** - 路径保护
- [ ] **Import Guard** - 依赖控制
- [ ] **Execution FSM** - 状态管理

### P2 - 可选迁移
- [ ] **Safe Merge** - 数据合并
- [ ] **Failure Handler** - 失败处理

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
