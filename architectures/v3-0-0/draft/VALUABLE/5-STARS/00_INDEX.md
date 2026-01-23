# 5-STARS: 关键资产精选

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/5-STARS/00_INDEX.md`
> **星级**: ⭐⭐⭐⭐⭐
> **数量**: 5 个详细文档
> **迁移价值**: 高度复用，强烈推荐迁移

---

## 详细文档列表

### 01. 系统入口与流程
**文件**: [`01_SYSTEM_ENTRY.md`](01_SYSTEM_ENTRY.md)

**内容**: main.py (4 阶段管道 + Checkpoint + Omni-Survival Kit)

**核心创新**:
- Checkpoint 自动恢复机制
- Omni-Survival Kit 死手开关
- 完整的异常处理与错误恢复

**资产**:
- `main.py` - 系统入口点 (938 行)
- 4 阶段管道架构
- 自动保存和恢复机制

---

### 02. 事件追踪与后处理分析
**文件**: [`02_EVENT_TRACKING.md`](02_EVENT_TRACKING.md)

**内容**: execution_tracker.py, latent_reporter.py

**核心创新**:
- Truth Mode 完整事件追踪
- 法医式尸检后处理分析
- 失败模式识别

**资产**:
- `execution_tracker.py` - 事件追踪器
- `latent_reporter.py` - 后处理分析器
- JSON + 可读文本双格式日志

---

### 03. 代码修复与输出解析
**文件**: [`03_CODE_FIXING.md`](03_CODE_FIXING.md)

**内容**: syntax_fixer.py, json_utils.py

**核心创新**:
- 预防性语法修复
- 多级防御 JSON 解析
- 高成功率解析策略

**资产**:
- `syntax_fixer.py` - LLM 代码语法修复
- `json_utils.py` - 鲁棒 LLM 输出解析
- 3 层解析策略 (Level 1-3)

---

### 04. 数据管理架构
**文件**: [`04_DATA_MANAGEMENT.md`](04_DATA_MANAGEMENT.md)

**内容**: data_manager.py, column_normalization.py

**核心创新**:
- 单一数据源模式
- Schema Registry 防止幻觉
- 列名规范化防止 KeyError

**资产**:
- `data_manager.py` - 数据管理器
- `column_normalization.py` - 列名规范化器
- 数据快照机制

---

### 05. 报告生成与评估框架
**文件**: [`05_REPORTING_EVALUATION.md`](05_REPORTING_EVALUATION.md)

**内容**: reporting/, MMBench/evaluation/

**核心创新**:
- 多格式报告生成管道
- 独立评估框架
- 自我升级和迭代机制

**资产**:
- `reporting/` - 报告生成模块
- `evaluation/` - 评估框架 (用于自我升级)
- JSON → Markdown → LaTeX → PDF 管道

---

## 核心创新点

### 1. Checkpoint 机制 (main.py)

```python
# Auto-resume Checkpointing
checkpoint_path = "output/logs/memory/checkpoints/pipeline_state.pkl"

if os.path.exists(checkpoint_path):
    # 从检查点恢复
    with open(checkpoint_path, 'rb') as f:
        state = pickle.load(f)
        problem, order, solution, completed_tasks = state

# 每个 Stage 后保存检查点
save_checkpoint(problem, order, solution, completed_tasks)
```

**优势**:
- **透明恢复**: 用户无需操作，自动从断点恢复
- **完整状态**: 保存所有必要状态
- **增量保存**: 仅保存变化的部分

### 2. Omni-Survival Kit (main.py)

```python
import atexit

def omni_survival_kit():
    """
    死手开关: 确保用户总能获得输出
    """
    @atexit.register
    def generate_emergency_pdf():
        if not os.path.exists('output/final_report.pdf'):
            # 生成紧急 PDF
            generate_pdf_from_available_outputs()

    try:
        run_pipeline()
    finally:
        generate_emergency_pdf()
```

**优势**:
- **保证输出**: 即使崩溃也生成 PDF
- **自动触发**: 使用 `atexit` 自动注册
- **紧急模式**: 使用可用输出生成 PDF

### 3. Truth Mode 日志 (execution_tracker.py)

```python
class ExecutionTracker:
    """
    Truth Mode: 完整事件追踪
    """
    def __init__(self):
        self.events = []
        self.start_time = datetime.now()

    def track(self, event_type, data):
        """记录事件"""
        event = {
            'timestamp': datetime.now().isoformat(),
            'type': event_type,
            'data': data,
            'elapsed': (datetime.now() - self.start_time).total_seconds()
        }
        self.events.append(event)

    def save_readable_log(self, path):
        """保存可读日志"""
        with open(path, 'w') as f:
            for event in self.events:
                f.write(f"[{event['timestamp']}] {event['type']}: {event['data']}\n")
```

**优势**:
- **完整追踪**: 记录所有事件
- **时间戳**: 精确到毫秒
- **可读格式**: 便于人类阅读

### 4. 法医式尸检 (latent_reporter.py)

```python
def latent_reporter(output_dir):
    """
    法医式尸检: 后处理分析
    """
    # 收集所有日志
    logs = collect_all_logs(output_dir)

    # 分析失败原因
    failure_analysis = analyze_failures(logs)

    # 生成修复建议
    fix_suggestions = generate_fix_suggestions(failure_analysis)

    # 生成报告
    report = {
        'failure_analysis': failure_analysis,
        'fix_suggestions': fix_suggestions,
        'autofix_attempts': count_autofix_attempts(logs)
    }

    return report
```

**优势**:
- **事后分析**: 运行结束后分析
- **结构化报告**: 清晰的失败原因和修复建议
- **自愈统计**: 统计自愈尝试次数

### 5. 语法修复器 (syntax_fixer.py)

```python
def fix_llm_syntax_errors(code):
    """
    修复 LLM 生成的语法错误
    """
    # 常见修复
    fixes = [
        # 缺少闭合括号
        (r'\(\s*$', ')'),
        (r'\[\s*$', ']'),
        (r'\{\s*$', '}'),

        # 缺少冒号
        (r'(if|for|while|def|class)\s+[^\:]+$', r'\1:'),

        # 多余的逗号
        (r',\s*\)', ')'),
        (r',\s*\]', ']'),
    ]

    for pattern, replacement in fixes:
        code = re.sub(pattern, replacement, code, flags=re.MULTILINE)

    return code
```

**优势**:
- **预防性修复**: 执行前修复
- **规则匹配**: 快速修复常见错误
- **提高成功率**: 显著提高代码执行成功率

### 6. 鲁棒 LLM 输出解析 (json_utils.py)

```python
def parse_llm_json(output, max_attempts=3):
    """
    多级防御策略解析 LLM 输出

    Level 1: 直接 JSON 解析
    Level 2: 清理后解析
    Level 3: 提取 JSON 块后解析
    """
    # Level 1: 直接解析
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        pass

    # Level 2: 清理后解析
    try:
        cleaned = clean_llm_output(output)
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Level 3: 提取 JSON 块
    try:
        json_block = extract_json_block(output)
        return json.loads(json_block)
    except json.JSONDecodeError:
        pass

    # 所有尝试失败
    raise ValueError("无法解析 LLM 输出")

def clean_llm_output(output):
    """
    清理 LLM 输出中的常见问题
    """
    # 移除 markdown 代码块标记
    output = re.sub(r'```json\s*', '', output)
    output = re.sub(r'```\s*', '', output)

    # 移除注释
    output = re.sub(r'//.*?\n', '\n', output)

    # 修复常见错误
    output = output.replace('True', 'true')
    output = output.replace('False', 'false')
    output = output.replace('None', 'null')

    return output.strip()
```

**优势**:
- **多级防御**: 3 层解析策略
- **常见问题**: 处理 markdown、注释、布尔值等
- **高成功率**: 显著提高 JSON 解析成功率

---

## 迁移优先级

### 🔴 P0 - 必须迁移

- [ ] **Checkpoint 机制** - Auto-resume 检查点
- [ ] **Omni-Survival Kit** - 死手开关
- [ ] **Truth Mode 日志** - 完整事件追踪
- [ ] **法医式尸检** - 后处理分析

### 🟡 P1 - 强烈推荐

- [ ] **语法修复器** - LLM 代码修复
- [ ] **鲁棒 JSON 解析** - 多级防御策略
- [ ] **数据管理架构** - 单一数据源
- [ ] **列名规范化** - 防止 KeyError

### 🟢 P2 - 可选迁移

- [ ] **变量契约系统** - 多阶段数据一致性
- [ ] **后处理分析提示词** - 日记提示词
- [ ] **报告生成框架** - 多格式报告

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**详细分析**: 见 `../6-STARS/` 目录下的详细文档
