# 5-STARS: 数据管理架构

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/5-STARS/04_DATA_MANAGEMENT.md`
> **星级**: ⭐⭐⭐⭐⭐
> **来源文档**: `15_Utilities.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/data_manager.py`, `column_normalization.py`

---

## 核心资产: 单一数据源模式

### 为什么是 5 星？

`data_manager.py` 实现了**单一数据源模式**，通过 Schema Registry 和数据快照机制，防止 LLM 产生幻觉列名，确保数据处理的一致性。

### DataManager 核心架构

```python
import pandas as pd
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

class DataManager:
    """
    数据管理器: 单一数据源模式

    核心功能:
    1. Schema Registry: 集中管理数据集 Schema
    2. Data Snapshot: 记录数据集状态
    3. 列名验证: 防止幻觉列名
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.data_dir = os.path.join(output_dir, 'data/')
        os.makedirs(self.data_dir, exist_ok=True)

        # Schema Registry: {dataset_name: {column: dtype}}
        self.schema_registry = {}

        # Data Snapshots: {dataset_name: snapshot}
        self.snapshots = {}

    def load_dataset(self, dataset_path: str, dataset_name: str) -> pd.DataFrame:
        """
        加载数据集并注册 Schema

        Args:
            dataset_path: 数据集路径
            dataset_name: 数据集名称

        Returns:
            DataFrame
        """
        # 加载数据
        data = pd.read_csv(dataset_path)

        # 注册 Schema
        schema = {
            col: str(dtype)
            for col, dtype in data.dtypes.items()
        }
        self.register_schema(dataset_name, schema)

        # 创建数据快照
        self.create_snapshot(dataset_name, data)

        return data

    def register_schema(self, dataset_name: str, schema: Dict[str, str]):
        """注册数据集 Schema"""
        self.schema_registry[dataset_name] = schema

    def get_schema(self, dataset_name: str) -> Dict[str, str]:
        """获取数据集 Schema"""
        return self.schema_registry.get(dataset_name, {})

    def validate_columns(self, dataset_name: str, columns: List[str]) -> bool:
        """
        验证列名是否合法

        Args:
            dataset_name: 数据集名称
            columns: 列名列表

        Returns:
            True 如果所有列名合法

        Raises:
            ValueError: 如果存在非法列名
        """
        schema = self.get_schema(dataset_name)
        invalid_cols = [col for col in columns if col not in schema]

        if invalid_cols:
            raise ValueError(
                f"非法列名 '{invalid_cols}' "
                f"在数据集 '{dataset_name}' 中。"
                f"合法列名: {list(schema.keys())}"
            )

        return True

    def create_snapshot(self, dataset_name: str, data: pd.DataFrame):
        """
        创建数据集快照

        Args:
            dataset_name: 数据集名称
            data: DataFrame
        """
        snapshot = {
            'timestamp': datetime.now().isoformat(),
            'shape': data.shape,
            'schema': {col: str(dtype) for col, dtype in data.dtypes.items()},
            'sample': data.head(5).to_dict(),
            'statistics': data.describe().to_dict()
        }

        self.snapshots[dataset_name] = snapshot

        # 保存到文件
        snapshot_path = os.path.join(self.data_dir, f'{dataset_name}_snapshot.json')
        with open(snapshot_path, 'w') as f:
            json.dump(snapshot, f, indent=2)

    def get_snapshot(self, dataset_name: str) -> Dict[str, Any]:
        """获取数据集快照"""
        return self.snapshots.get(dataset_name, {})

    def get_column_type(self, dataset_name: str, column: str) -> Optional[str]:
        """获取列类型"""
        schema = self.get_schema(dataset_name)
        return schema.get(column)
```

### ColumnNormalization 列名规范化

```python
import re
from functools import wraps

class ColumnNormalizer:
    """
    列名规范化器: 防止 KeyError

    功能:
    1. 列名规范化 (小写、下划线)
    2. 别名映射
    3. 自动包装
    """
    def __init__(self):
        # 列名映射: {normalized: original}
        self.column_mapping = {}

    def normalize_column_name(self, col: str) -> str:
        """
        规范化列名

        规则:
        1. 转小写
        2. 替换空格为下划线
        3. 移除特殊字符
        """
        normalized = col.strip().lower()
        normalized = re.sub(r'\s+', '_', normalized)
        normalized = re.sub(r'[^\w_]', '', normalized)
        return normalized

    def normalize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        规范化 DataFrame 列名

        Args:
            df: 原始 DataFrame

        Returns:
            规范化后的 DataFrame
        """
        # 创建映射
        mapping = {}
        for col in df.columns:
            normalized = self.normalize_column_name(col)
            mapping[normalized] = col
            self.column_mapping[normalized] = col

        # 重命名列
        df_normalized = df.rename(columns=lambda x: self.normalize_column_name(x))

        return df_normalized

    def safe_get_column(self, df: pd.DataFrame, col: str) -> pd.Series:
        """
        安全获取列（支持别名）

        Args:
            df: DataFrame
            col: 列名（可以是原始名或规范名）

        Returns:
            Series

        Raises:
            KeyError: 如果列不存在
        """
        # 尝试直接获取
        if col in df.columns:
            return df[col]

        # 尝试别名
        normalized = self.normalize_column_name(col)
        if normalized in df.columns:
            return df[normalized]

        # 尝试映射
        original = self.column_mapping.get(normalized)
        if original and original in df.columns:
            return df[original]

        raise KeyError(f"列 '{col}' 不存在")

# 全局单例
column_normalizer = ColumnNormalizer()
```

### 使用示例

```python
# 初始化
dm = DataManager(output_dir)

# 加载数据集（自动注册 Schema）
data = dm.load_dataset('data/problem_data.csv', 'problem_data')

# 获取 Schema
schema = dm.get_schema('problem_data')
print(f"Schema: {schema}")

# 验证列名（防止幻觉）
try:
    columns = ['Year', 'Value', 'InvalidColumn']
    dm.validate_columns('problem_data', columns)
except ValueError as e:
    print(f"验证失败: {e}")

# 获取列类型
col_type = dm.get_column_type('problem_data', 'Year')
print(f"Year 列类型: {col_type}")

# 规范化列名
cn = ColumnNormalizer()
df_normalized = cn.normalize_dataframe(data)
print(f"规范化后的列名: {df_normalized.columns.tolist()}")
```

### 优势

1. **单一数据源**: 所有数据访问通过 DataManager
2. **Schema 验证**: 防止 LLM 产生幻觉列名
3. **数据快照**: 记录数据集状态
4. **列名规范化**: 防止因列名不匹配导致的 KeyError
5. **别名支持**: 支持原始列名和规范列名

---

## 迁移价值

### 必须迁移 (P0)

- [ ] **DataManager** - 单一数据源模式
- [ ] **ColumnNormalizer** - 列名规范化

### 强烈推荐 (P1)

- [ ] **Schema Registry** - 集中管理 Schema
- [ ] **Data Snapshot** - 数据集状态记录
- [ ] **列名验证** - 防止幻觉列名

### 可选迁移 (P2)

- [ ] **别名映射** - 支持列名别名

---

## 核心创新点

1. **单一数据源**: 防止数据不一致
2. **Schema 验证**: 防止 LLM 幻觉
3. **数据快照**: 版本控制和调试
4. **列名规范化**: 防止 KeyError
5. **别名支持**: 灵活的列名访问

---

## 与其他资产的集成

| 资产 | 集成方式 |
|------|----------|
| **task_solving.py** (6-STARS) | 代码生成前验证列名 |
| **schema_registry.py** (6-STARS) | 集中式 Schema 管理 |
| **data_normalization.py** (6-STARS) | 数据清洗和规范化 |

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
