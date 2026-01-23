# 5-STARS: 事件追踪与后处理分析

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/5-STARS/02_EVENT_TRACKING.md`
> **星级**: ⭐⭐⭐⭐⭐
> **来源文档**: `15_Utilities.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/execution_tracker.py`, `latent_reporter.py`

---

## 核心资产概览

| 模块 | 文件 | 核心功能 | 创新点 |
|------|------|----------|--------|
| **Execution Tracker** | `execution_tracker.py` | Truth Mode 日志，完整事件追踪 | 时间戳精确到毫秒 |
| **Latent Reporter** | `latent_reporter.py` | 法医式尸检，后处理分析 | 运行结束后分析 |

---

## 1. Execution Tracker (execution_tracker.py)

### 为什么是 5 星？

`execution_tracker.py` 实现了 **Truth Mode 日志**，记录系统运行的所有事件，是调试和分析的基础设施。

### Truth Mode 完整事件追踪

```python
import json
from datetime import datetime
from threading import Lock

class ExecutionTracker:
    """
    Truth Mode: 完整事件追踪器

    记录系统运行的所有事件，包括:
    - 阶段开始/结束
    - 任务开始/结束
    - LLM 调用
    - 代码执行
    - 错误和警告
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.events = []
        self.start_time = datetime.now()
        self.lock = Lock()  # 线程安全

        # 日志路径
        self.log_dir = os.path.join(output_dir, 'Memory/logs/')
        os.makedirs(self.log_dir, exist_ok=True)

        self.json_log_path = os.path.join(self.log_dir, 'execution_tracker.json')
        self.readable_log_path = os.path.join(self.log_dir, 'execution_tracker_readable.txt')

    def track(self, event_type, data, level='INFO'):
        """
        记录事件

        Args:
            event_type: 事件类型 (stage_start, task_start, llm_call, etc.)
            data: 事件数据 (字典)
            level: 日志级别 (INFO, WARNING, ERROR)
        """
        with self.lock:
            event = {
                'timestamp': datetime.now().isoformat(),
                'elapsed_seconds': (datetime.now() - self.start_time).total_seconds(),
                'type': event_type,
                'level': level,
                'data': data
            }

            self.events.append(event)

            # 立即写入可读日志
            self._append_readable_log(event)

    def _append_readable_log(self, event):
        """追加到可读日志"""
        with open(self.readable_log_path, 'a', encoding='utf-8') as f:
            timestamp = event['timestamp']
            elapsed = event['elapsed_seconds']
            event_type = event['type']
            level = event['level']
            data = event['data']

            f.write(f"[{timestamp}] (+{elapsed:.3f}s) [{level}] {event_type}: {data}\n")

    def save_json_log(self):
        """保存 JSON 格式的完整日志"""
        with open(self.json_log_path, 'w', encoding='utf-8') as f:
            json.dump({
                'start_time': self.start_time.isoformat(),
                'events': self.events,
                'total_events': len(self.events)
            }, f, indent=2)

    def get_events_by_type(self, event_type):
        """获取指定类型的所有事件"""
        return [e for e in self.events if e['type'] == event_type]

    def get_events_by_level(self, level):
        """获取指定级别的所有事件"""
        return [e for e in self.events if e['level'] == level]

    def get_error_events(self):
        """获取所有错误事件"""
        return self.get_events_by_level('ERROR')

    def get_summary(self):
        """获取事件摘要"""
        summary = {
            'total_events': len(self.events),
            'total_duration': (datetime.now() - self.start_time).total_seconds(),
            'events_by_type': {},
            'events_by_level': {}
        }

        for event in self.events:
            # 按类型统计
            event_type = event['type']
            summary['events_by_type'][event_type] = summary['events_by_type'].get(event_type, 0) + 1

            # 按级别统计
            level = event['level']
            summary['events_by_level'][level] = summary['events_by_level'].get(level, 0) + 1

        return summary
```

### 事件类型定义

```python
class EventTypes:
    """标准事件类型"""
    # 阶段事件
    STAGE_START = 'stage_start'
    STAGE_END = 'stage_end'

    # 任务事件
    TASK_START = 'task_start'
    TASK_END = 'task_end'
    TASK_ERROR = 'task_error'

    # LLM 事件
    LLM_CALL_START = 'llm_call_start'
    LLM_CALL_END = 'llm_call_end'
    LLM_CALL_ERROR = 'llm_call_error'

    # 代码执行事件
    CODE_EXEC_START = 'code_exec_start'
    CODE_EXEC_END = 'code_exec_end'
    CODE_EXEC_ERROR = 'code_exec_error'

    # 系统事件
    CHECKPOINT_SAVE = 'checkpoint_save'
    CHECKPOINT_LOAD = 'checkpoint_load'
    ERROR_RECOVERY = 'error_recovery'
```

### 使用示例

```python
# 初始化追踪器
tracker = ExecutionTracker(output_dir)

# 追踪阶段开始
tracker.track(EventTypes.STAGE_START, {
    'stage': 'stage1',
    'name': 'Problem Analysis'
})

# 追踪 LLM 调用
tracker.track(EventTypes.LLM_CALL_START, {
    'model': 'gpt-4o',
    'prompt_length': 1500,
    'stage': 'stage1'
})

# ... LLM 调用 ...

tracker.track(EventTypes.LLM_CALL_END, {
    'model': 'gpt-4o',
    'response_length': 800,
    'tokens_used': 2300,
    'duration': 3.5
})

# 追踪错误
try:
    risky_operation()
except Exception as e:
    tracker.track(EventTypes.TASK_ERROR, {
        'task': 'data_processing',
        'error': str(e),
        'traceback': traceback.format_exc()
    }, level='ERROR')

# 保存完整日志
tracker.save_json_log()
```

### 可读日志输出

```
[2025-01-24T10:30:00.123456] (+0.000s) [INFO] stage_start: {'stage': 'stage1', 'name': 'Problem Analysis'}
[2025-01-24T10:30:00.234567] (+0.111s) [INFO] llm_call_start: {'model': 'gpt-4o', 'prompt_length': 1500, 'stage': 'stage1'}
[2025-01-24T10:30:03.734567] (+3.601s) [INFO] llm_call_end: {'model': 'gpt-4o', 'response_length': 800, 'tokens_used': 2300, 'duration': 3.5}
[2025-01-24T10:30:05.123456] (+5.000s) [INFO] stage_end: {'stage': 'stage1', 'duration': 5.0}
```

### 优势

1. **完整追踪**: 记录所有事件，不遗漏任何细节
2. **时间戳精确**: ISO 8601 格式，精确到毫秒
3. **线程安全**: 使用 Lock 保护，支持并发记录
4. **双格式**: JSON（程序化分析）+ 可读文本（人工阅读）
5. **实时写入**: 每个事件立即追加到可读日志

---

## 2. Latent Reporter (latent_reporter.py)

### 为什么是 5 星？

`latent_reporter.py` 实现了**法医式尸检**（Forensic Autopsy），在系统运行结束后进行后处理分析，生成结构化的失败原因和修复建议报告。

### 法医式尸检分析

```python
import json
import re
from collections import defaultdict, Counter

class LatentReporter:
    """
    法医式尸检: 后处理分析系统

    在系统运行结束后分析:
    1. 失败原因
    2. 自愈尝试
    3. 修复建议
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.log_dir = os.path.join(output_dir, 'Memory/logs/')
        self.report_path = os.path.join(self.log_dir, 'latent_analysis_report.json')

    def generate_report(self):
        """
        生成法医式尸检报告

        Returns:
            报告字典
        """
        # 收集所有日志
        logs = self._collect_all_logs()

        # 分析失败原因
        failure_analysis = self._analyze_failures(logs)

        # 统计自愈尝试
        autofix_stats = self._count_autofix_attempts(logs)

        # 生成修复建议
        fix_suggestions = self._generate_fix_suggestions(
            failure_analysis,
            autofix_stats
        )

        # 组装报告
        report = {
            'timestamp': datetime.now().isoformat(),
            'failure_analysis': failure_analysis,
            'autofix_statistics': autofix_stats,
            'fix_suggestions': fix_suggestions,
            'summary': self._generate_summary(
                failure_analysis,
                autofix_stats
            )
        }

        # 保存报告
        self._save_report(report)

        return report

    def _collect_all_logs(self):
        """收集所有日志文件"""
        logs = []

        # 执行追踪日志
        tracker_log = os.path.join(self.log_dir, 'execution_tracker.json')
        if os.path.exists(tracker_log):
            with open(tracker_log, 'r') as f:
                logs.append(json.load(f))

        # 自愈日志
        autofix_log = os.path.join(self.log_dir, 'autofix_log.json')
        if os.path.exists(autofix_log):
            with open(autofix_log, 'r') as f:
                logs.append(json.load(f))

        # 可读日志
        readable_log = os.path.join(self.log_dir, 'execution_tracker_readable.txt')
        if os.path.exists(readable_log):
            with open(readable_log, 'r', encoding='utf-8') as f:
                logs.append({
                    'type': 'readable_log',
                    'content': f.read()
                })

        return logs

    def _analyze_failures(self, logs):
        """
        分析失败原因

        Returns:
            失败分析字典
        """
        failure_analysis = {
            'total_failures': 0,
            'failures_by_type': defaultdict(int),
            'failures_by_stage': defaultdict(int),
            'critical_failures': [],
            'failure_patterns': []
        }

        for log in logs:
            if isinstance(log, dict) and 'events' in log:
                # 分析 JSON 日志
                for event in log['events']:
                    if event.get('level') == 'ERROR':
                        failure_analysis['total_failures'] += 1

                        # 按类型统计
                        event_type = event['type']
                        failure_analysis['failures_by_type'][event_type] += 1

                        # 按阶段统计
                        stage = event['data'].get('stage', 'unknown')
                        failure_analysis['failures_by_stage'][stage] += 1

                        # 记录关键失败
                        if event_type in ['task_error', 'llm_call_error', 'code_exec_error']:
                            failure_analysis['critical_failures'].append({
                                'timestamp': event['timestamp'],
                                'type': event_type,
                                'stage': stage,
                                'error': event['data'].get('error', 'Unknown error')
                            })

        # 识别失败模式
        failure_analysis['failure_patterns'] = self._identify_failure_patterns(
            failure_analysis
        )

        return failure_analysis

    def _identify_failure_patterns(self, failure_analysis):
        """
        识别失败模式

        Returns:
            失败模式列表
        """
        patterns = []

        # 模式 1: 频繁的 LLM 错误
        llm_errors = failure_analysis['failures_by_type'].get('llm_call_error', 0)
        if llm_errors > 3:
            patterns.append({
                'pattern': 'frequent_llm_errors',
                'description': f'LLM 调用失败 {llm_errors} 次',
                'severity': 'high',
                'suggestion': '检查 API 密钥、网络连接、速率限制'
            })

        # 模式 2: 代码执行错误集中在某个阶段
        for stage, count in failure_analysis['failures_by_stage'].items():
            if count > 2 and stage != 'unknown':
                patterns.append({
                    'pattern': 'stage_specific_failures',
                    'description': f'阶段 {stage} 失败 {count} 次',
                    'severity': 'medium',
                    'suggestion': f'检查 {stage} 的代码生成逻辑'
                })

        # 模式 3: 语法错误
        syntax_errors = failure_analysis['failures_by_type'].get('syntax_error', 0)
        if syntax_errors > 2:
            patterns.append({
                'pattern': 'frequent_syntax_errors',
                'description': f'语法错误 {syntax_errors} 次',
                'severity': 'medium',
                'suggestion': '增强语法修复器'
            })

        return patterns

    def _count_autofix_attempts(self, logs):
        """
        统计自愈尝试

        Returns:
            自愈统计字典
        """
        autofix_stats = {
            'total_attempts': 0,
            'successful_fixes': 0,
            'failed_fixes': 0,
            'fixes_by_type': defaultdict(int),
            'fixes_by_layer': {
                'layer1': 0,  # 快速修复
                'layer2': 0,  # 中度修复
                'layer3': 0   # 深度修复
            }
        }

        for log in logs:
            if isinstance(log, dict) and log.get('type') == 'autofix_log':
                autofix_stats['total_attempts'] += log.get('total_attempts', 0)
                autofix_stats['successful_fixes'] += log.get('successful_fixes', 0)
                autofix_stats['failed_fixes'] += log.get('failed_fixes', 0)

                for fix_type, count in log.get('fixes_by_type', {}).items():
                    autofix_stats['fixes_by_type'][fix_type] += count

                for layer in ['layer1', 'layer2', 'layer3']:
                    autofix_stats['fixes_by_layer'][layer] += log.get('fixes_by_layer', {}).get(layer, 0)

        return autofix_stats

    def _generate_fix_suggestions(self, failure_analysis, autofix_stats):
        """
        生成修复建议

        Returns:
            修复建议列表
        """
        suggestions = []

        # 建议优先级: P0 (关键) > P1 (重要) > P2 (可选)

        # P0: LLM 速率限制
        if any(p['pattern'] == 'frequent_llm_errors' for p in failure_analysis['failure_patterns']):
            suggestions.append({
                'priority': 'P0',
                'category': 'api_management',
                'suggestion': '实现更强的速率限制',
                'details': [
                    '增加线程锁的等待时间',
                    '实现指数退避重试',
                    '使用多个 API 密钥轮询'
                ]
            })

        # P1: 语法修复增强
        if any(p['pattern'] == 'frequent_syntax_errors' for p in failure_analysis['failure_patterns']):
            suggestions.append({
                'priority': 'P1',
                'category': 'code_generation',
                'suggestion': '增强语法修复器',
                'details': [
                    '添加更多语法修复规则',
                    '实现 AST 验证',
                    '增加 LLM 辅助修复'
                ]
            })

        # P2: 改进错误恢复
        if autofix_stats['failed_fixes'] > autofix_stats['successful_fixes']:
            suggestions.append({
                'priority': 'P2',
                'category': 'error_recovery',
                'suggestion': '改进错误恢复机制',
                'details': [
                    '增加 Layer 3 深度修复',
                    '实现更智能的错误诊断',
                    '添加更多修复策略'
                ]
            })

        return suggestions

    def _generate_summary(self, failure_analysis, autofix_stats):
        """生成摘要"""
        total_events = failure_analysis['total_failures'] + autofix_stats['successful_fixes']
        success_rate = autofix_stats['successful_fixes'] / max(autofix_stats['total_attempts'], 1) * 100

        return {
            'total_failures': failure_analysis['total_failures'],
            'total_autofix_attempts': autofix_stats['total_attempts'],
            'autofix_success_rate': f'{success_rate:.1f}%',
            'most_common_failure': max(
                failure_analysis['failures_by_type'].items(),
                key=lambda x: x[1],
                default=('N/A', 0)
            )[0],
            'most_problematic_stage': max(
                failure_analysis['failures_by_stage'].items(),
                key=lambda x: x[1],
                default=('N/A', 0)
            )[0]
        }

    def _save_report(self, report):
        """保存报告"""
        with open(self.report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"✓ Latent analysis report saved: {self.report_path}")
```

### 使用示例

```python
# 系统运行结束后
reporter = LatentReporter(output_dir)
report = reporter.generate_report()

# 查看摘要
print(f"Total failures: {report['summary']['total_failures']}")
print(f"Autofix success rate: {report['summary']['autofix_success_rate']}")
print(f"Most common failure: {report['summary']['most_common_failure']}")

# 查看修复建议
for suggestion in report['fix_suggestions']:
    print(f"\n[{suggestion['priority']}] {suggestion['suggestion']}")
    for detail in suggestion['details']:
        print(f"  - {detail}")
```

### 报告示例

```json
{
  "timestamp": "2025-01-24T10:35:00.123456",
  "failure_analysis": {
    "total_failures": 15,
    "failures_by_type": {
      "llm_call_error": 8,
      "code_exec_error": 5,
      "task_error": 2
    },
    "failures_by_stage": {
      "stage3": 10,
      "stage2": 3,
      "stage1": 2
    },
    "critical_failures": [
      {
        "timestamp": "2025-01-24T10:32:15.123456",
        "type": "llm_call_error",
        "stage": "stage3",
        "error": "Rate limit exceeded"
      }
    ],
    "failure_patterns": [
      {
        "pattern": "frequent_llm_errors",
        "description": "LLM 调用失败 8 次",
        "severity": "high",
        "suggestion": "检查 API 密钥、网络连接、速率限制"
      }
    ]
  },
  "autofix_statistics": {
    "total_attempts": 12,
    "successful_fixes": 9,
    "failed_fixes": 3,
    "fixes_by_layer": {
      "layer1": 7,
      "layer2": 4,
      "layer3": 1
    }
  },
  "summary": {
    "total_failures": 15,
    "total_autofix_attempts": 12,
    "autofix_success_rate": "75.0%",
    "most_common_failure": "llm_call_error",
    "most_problematic_stage": "stage3"
  }
}
```

### 优势

1. **事后分析**: 运行结束后进行全面分析
2. **模式识别**: 识别重复出现的失败模式
3. **结构化报告**: JSON 格式，便于程序化分析
4. **修复建议**: 根据失败模式生成针对性建议
5. **自愈统计**: 追踪自愈机制的成功率

---

## 迁移价值

### 必须迁移 (P0)

- [ ] **Execution Tracker** - 完整事件追踪基础
- [ ] **Latent Reporter** - 后处理分析系统

### 强烈推荐 (P1)

- [ ] **双格式日志** - JSON + 可读文本
- [ ] **失败模式识别** - 自动识别问题模式
- [ ] **修复建议生成** - 智能生成修复方案

### 可选迁移 (P2)

- [ ] **线程安全保护** - Lock 保护并发访问
- [ ] **实时日志写入** - 立即追加到可读日志

---

## 核心创新点

1. **Truth Mode**: 完整、真实的事件记录
2. **法医式尸检**: 运行结束后进行全面分析
3. **失败模式识别**: 自动识别重复出现的失败
4. **结构化报告**: JSON 格式便于分析
5. **修复建议**: 智能生成针对性的修复方案

---

## 与其他资产的集成

| 资产 | 集成方式 |
|------|----------|
| **autofixer.py** (6-STARS) | 追踪自愈尝试，统计成功率 |
| **main.py** (5-STARS) | Checkpoint 包含追踪器状态 |
| **syntax_fixer.py** (5-STARS) | 记录语法修复事件 |

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
