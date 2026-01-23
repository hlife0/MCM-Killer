# MMAgent: 主程序入口

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/02_MMAgent_Main.md`
> **重要程度**: ⭐⭐⭐⭐⭐ 系统入口
> **迁移价值**: **高** - 管道编排模式可复用

`main.py` 是 LLM-MM-Agent 系统的主入口文件（938 行），实现了完整的 4 阶段管道：Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting。文件包含管道编排、检查点恢复、错误处理、自动评估、Omni-Survival Kit 死手开关等核心功能。

**迁移价值**：main.py 展示了如何组织一个复杂的 AI Agent 管道。管道编排、检查点机制、错误处理、死手开关等模式可以应用到任何长时间运行的 AI 系统。特别是 auto-resume 机制和 Omni-Survival Kit 是系统可靠性的关键保障。

---

## 核心功能

### 1. 管道编排（Pipeline Orchestration）

**4 阶段流程**：
1. **Stage 1: Problem Analysis** - 问题分解为子任务
2. **Stage 2: Mathematical Modeling** - 为每个子任务进行数学建模
3. **Stage 3: Computational Solving** - 为每个子任务生成和执行代码
4. **Stage 4: Solution Reporting** - 生成最终报告（JSON/Markdown/LaTeX）

**关键代码**：
```python
# Stage 1: Problem Analysis
task_descriptions = problem_analysis(
    problem, llm, config, coordinator, logger_manager
)

# Stage 2 & 3: Mathematical Modeling & Computational Solving
for task_id in order:
    task_description, task_analysis, task_modeling_formulas, task_modeling_method, dependent_file_prompt = mathematical_modeling(
        task_id, problem, task_descriptions, llm, config, coordinator, with_code, logger_manager, output_dir, latent_reporter
    )
    solution = computational_solving(
        llm, coordinator, with_code, problem, task_id, ...
    )

# Stage 4: Solution Reporting
generate_paper(...)
```

### 2. 自动恢复（Auto-Resume）

**检查点机制**：
- Stage 1 完成后自动保存
- 每个任务完成后自动保存
- 重启时自动加载检查点并继续

**关键代码**：
```python
# 加载检查点
checkpoint_path = os.path.join(output_dir, "logs/memory/checkpoints/pipeline_state.pkl")
if os.path.exists(checkpoint_path):
    with open(checkpoint_path, 'rb') as pickle.load:
        problem, order, task_descriptions, solution, completed_tasks, coordinator = ...

# 保存检查点
def save_checkpoint():
    state = {
        'problem': problem,
        'order': order,
        'task_descriptions': task_descriptions,
        'solution': solution,
        'completed_tasks': completed_tasks,
        'coordinator': coordinator  # 注意：LLM 实例不保存
    }
    with open(checkpoint_path, 'wb') as f:
        pickle.dump(state, f)
```

**关键设计**：LLM 实例不被 pickled，恢复时重新创建。

### 3. Omni-Survival Kit（死手开关）

**双重触发机制**：
1. `atexit.register()` - Python 退出时触发
2. `finally` 块 - 主程序结束时触发

**功能**：
- 即使系统崩溃也能生成 PDF
- AssetIndexer 扫描所有资产（代码、图表、JSON）
- 自动愈合 LaTeX 编译（注释错误行）
- 保证："只要结束就会启动，且不生成不罢休"

**关键代码**：
```python
def omni_survival_kit():
    """Dead Man's Switch - ensures PDF generation even on crash"""
    atexit.register(lambda: generate_emergency_pdf())

    try:
        # Main pipeline
        run_pipeline()
    finally:
        # Always generate PDF
        generate_emergency_pdf()
```

### 4. 错误处理（Error Handling）

**多层防护**：
- Try-except 包装每个阶段
- FailureHandler 确保最小输出
- ExecutionTracker 记录完整错误日志（trace.jsonl）

**关键代码**：
```python
try:
    # Stage 1: Problem Analysis
    task_descriptions = problem_analysis(...)
except Exception as e:
    logger_manager.get_logger('main').error(f"Stage 1 failed: {e}")
    failure_handler.write_minimal_solution("Problem Analysis", str(e))
```

### 5. 自动评估（Auto Evaluation）

**评估内容**：
- Problem Analysis 质量
- Mathematical Modeling 的完整性
- Computational Solving 的成功率
- Solution Reporting 的格式正确性

**关键代码**：
```python
# Pipeline 结束后自动运行评估
run_auto_evaluation(output_dir, logger_manager)
```

### 6. LatentReporter 集成

**实时日志记录**：
- 每个阶段开始/结束记录
- LLM 调用记录
- 代码生成/执行记录
- 错误发生记录

**后处理分析**：
- 阶段性复盘（reflect_on_stage）
- 错误诊断（diagnose_failure）
- 结果总结（summarize_results）

---

## 文件结构（938 行）

```
main.py (938 lines)
├── 导入模块 (1-60 行)
│   ├── 项目根路径添加
│   ├── Agent 导入
│   ├── Utils 导入
│   └── 平台编码配置
│
├── 辅助函数 (60-150 行)
│   ├── get_model_base_url() - 模型 base URL 自动检测
│   ├── run_mmbench_evaluation() - MMBench 评估
│   └── 其他辅助函数
│
├── 主函数 (150-400 行)
│   ├── 参数解析
│   ├── 配置加载
│   ├── LLM 初始化
│   ├── 检查点恢复
│   ├── Stage 1: Problem Analysis
│   ├── Stage 2-3: 循环处理任务
│   └── Stage 4: Solution Reporting
│
├── 检查点机制 (400-500 行)
│   ├── save_checkpoint()
│   ├── load_checkpoint()
│   └── 状态序列化/反序列化
│
├── Omni-Survival Kit (500-700 行)
│   ├── AssetIndexer - 资产扫描器
│   ├── generate_emergency_pdf() - 紧急 PDF 生成
│   ├── auto_healing_latex() - LaTeX 自动愈合
│   └── register_handlers() - 注册处理器
│
├── 错误处理 (700-800 行)
│   ├── FailureHandler
│   ├── try-except 包装
│   └── 错误日志记录
│
└── 其他功能 (800-938 行)
    ├── MMBench 评估集成
    ├── 自动评估
    ├── LatentReporter 集成
    └── 清理和收尾
```

---

## 关键设计模式

### 1. 管道模式（Pipeline Pattern）

**特点**：
- 顺序执行 4 个阶段
- 每个阶段产生下一阶段的输入
- Stage 2-3 并行处理多个子任务

### 2. 检查点模式（Checkpoint Pattern）

**特点**：
- 状态持久化到 pickle 文件
- 自动保存（Stage 1 + 每个任务后）
- 透明恢复（重启自动继续）
- LLM 实例不保存（恢复时重新创建）

### 3. 死手开关模式（Dead Man's Switch）

**特点**：
- 双重触发（atexit + finally）
- 扫描所有可用资产
- 强制生成 PDF
- 自动愈合编译错误

### 4. 协调器模式（Coordinator Pattern）

**特点**：
- Coordinator 管理任务依赖
- DAG 拓扑排序确定执行顺序
- 状态共享（memory, code_memory）

---

## 重要函数

### `main()` - 主函数

**入口点**，参数：
- `--key`: API key
- `--task`: 任务 ID（如 "2024_C"）
- `--model_name`: 模型名称（如 "gpt-4o"）
- `--method_name`: 方法名称（默认 "default"）
- `--enable_latent_summary`: 是否启用 LatentReporter

**流程**：
1. 解析参数和加载配置
2. 初始化 LLM 和 Coordinator
3. 尝试加载检查点
4. 执行 4 阶段管道
5. 运行自动评估
6. 调用 Omni-Survival Kit

### `problem_analysis()` - Stage 1

**输入**：problem, llm, config, coordinator, logger_manager
**输出**：task_descriptions（子任务列表）
**功能**：将复杂问题分解为可管理的子任务

### `mathematical_modeling()` - Stage 2

**输入**：task_id, problem, task_descriptions, llm, config, coordinator, ...
**输出**：task_modeling_formulas, task_modeling_method
**功能**：为每个子任务进行数学建模

### `computational_solving()` - Stage 3

**输入**：task_id, problem, task_modeling_formulas, ...
**输出**：solution（更新后的解决方案）
**功能**：生成和执行代码，生成图表

### `generate_paper()` - Stage 4

**输入**：problem, solution, output_dir, ...
**输出**：PDF 文件
**功能**：生成最终报告（JSON/Markdown/LaTeX）

---

## 配置参数

### config.yaml 关键参数

```yaml
# 方法检索
top_method_num: 6              # 从 HMML 检索的方法数量

# 迭代轮次
problem_analysis_round: 3     # 问题分析迭代轮次
problem_modeling_round: 3     # 数学建模迭代轮次
task_formulas_round: 5        # 公式推导迭代轮次

# 任务限制
num_tasks: 5                  # 最大子任务数量
num_charts: 5                  # 每个任务的图表数量

# 路径配置
paths.root_data: "MMBench"     # 数据目录
paths.output_root: "MMAgent/output"  # 输出目录
```

---

## 与其他模块的交互

### 调用的模块

- `agent/coordinator.py` - DAG 任务调度
- `utils/problem_analysis.py` - 问题分析
- `utils/mathematical_modeling.py` - 数学建模
- `utils/computational_solving.py` - 计算求解
- `utils/solution_reporting.py` - 解决方案报告
- `utils/execution_tracker.py` - 事件跟踪
- `utils/auto_evaluation.py` - 自动评估
- `utils/latent_reporter.py` - 潜伏报告器
- `llm/llm.py` - LLM 接口

### 被调用的模块

- `prompt/template.py` - 提示词模板
- `HMML/HMML.md` - 知识库
- `MMBench/evaluation/` - 评估框架

---

## 迁移建议

### 高优先级（强烈推荐）

1. **检查点机制** - 任何长时间运行任务都需要
2. **死手开关** - 确保系统崩溃时也能生成输出
3. **4 阶段管道模式** - 适用于任何分步骤的自动化流程

### 中优先级

4. **自动评估** - 质量保障
5. **错误处理多层防护** - 提高鲁棒性
6. **LatentReporter 集成** - 实时日志记录

### 低优先级

7. **MMBench 评估集成** - 仅在需要评估时使用
8. **模型 base URL 自动检测** - 可根据需求定制

---

## 关键发现

1. **main.py 是管道的大脑**：编排所有阶段和模块
2. **检查点 + 恢复机制**：透明的自动恢复是用户体验的关键
3. **死手开关**：确保用户总能获得输出，即使系统崩溃
4. **LLM 实例不保存**：恢复时重新创建，避免 pickling 问题
5. **多层错误处理**：try-except + FailureHandler + ExecutionTracker

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**文件大小**: 938 行
