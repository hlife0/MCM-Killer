# 5-STARS: 系统入口与流程

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/5-STARS/01_SYSTEM_ENTRY.md`
> **星级**: ⭐⭐⭐⭐⭐
> **来源文档**: `02_MMAgent_Main.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/main.py`

---

## 核心资产: main.py (938 行)

### 为什么是 5 星？

`main.py` 是 LLM-MM-Agent 系统的**单一入口点**，实现了完整的 4 阶段数学建模管道，包含三大可靠性保障机制：Checkpoint 自动恢复、Omni-Survival Kit 死手开关、异常处理与错误恢复。

### 4 阶段管道

```python
def run_4_stage_pipeline(problem):
    """
    LLM-MM-Agent 4 阶段管道

    Stage 1: Problem Analysis (问题分析)
    Stage 2: Mathematical Modeling (数学建模)
    Stage 3: Computational Solving (计算求解)
    Stage 4: Solution Reporting (结果报告)
    """
    # Stage 1: 问题分析
    problem_analysis = analyze_problem(problem)
    print("✓ Stage 1 Complete: Problem Analysis")

    # Stage 2: 数学建模
    mathematical_model = build_model(problem_analysis)
    print("✓ Stage 2 Complete: Mathematical Modeling")

    # Stage 3: 计算求解
    solution = solve_computationally(mathematical_model)
    print("✓ Stage 3 Complete: Computational Solving")

    # Stage 4: 结果报告
    report = generate_report(solution)
    print("✓ Stage 4 Complete: Solution Reporting")

    return report
```

**关键设计**:
- **顺序执行**: 每个阶段依赖前一个阶段的输出
- **状态传递**: 阶段间通过返回值传递状态
- **进度反馈**: 每个阶段完成后打印进度

---

## 核心创新 1: Checkpoint 自动恢复机制

### 为什么重要？

长时间运行的 AI Agent 系统必须能够从崩溃中恢复。Checkpoint 机制实现了**透明的自动恢复**，用户无需任何手动操作。

### 实现细节

```python
import pickle
import os
from datetime import datetime

class CheckpointManager:
    """
    Checkpoint 管理器: 自动保存和恢复管道状态
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.checkpoint_path = os.path.join(
            output_dir,
            "logs/memory/checkpoints/pipeline_state.pkl"
        )

    def save_checkpoint(self, state):
        """
        保存管道状态到检查点

        Args:
            state: 包含以下键的字典
                - problem: 问题描述
                - order: 任务顺序
                - solution: 当前解决方案
                - completed_tasks: 已完成的任务列表
                - coordinator: 调度器状态
        """
        # 创建检查点目录
        os.makedirs(os.path.dirname(self.checkpoint_path), exist_ok=True)

        # 保存状态
        with open(self.checkpoint_path, 'wb') as f:
            pickle.dump(state, f)

        # 记录检查点时间
        timestamp = datetime.now().isoformat()
        print(f"✓ Checkpoint saved at {timestamp}")

    def load_checkpoint(self):
        """
        从检查点恢复管道状态

        Returns:
            状态字典，如果检查点不存在则返回 None
        """
        if not os.path.exists(self.checkpoint_path):
            return None

        with open(self.checkpoint_path, 'rb') as f:
            state = pickle.load(f)

        timestamp = datetime.fromtimestamp(
            os.path.getmtime(self.checkpoint_path)
        ).isoformat()
        print(f"✓ Checkpoint loaded from {timestamp}")

        return state

    def has_checkpoint(self):
        """检查是否存在检查点"""
        return os.path.exists(self.checkpoint_path)
```

### 使用方式

```python
def main():
    checkpoint_manager = CheckpointManager(output_dir)

    # 尝试从检查点恢复
    if checkpoint_manager.has_checkpoint():
        state = checkpoint_manager.load_checkpoint()
        problem = state['problem']
        order = state['order']
        solution = state['solution']
        completed_tasks = state['completed_tasks']
        coordinator = state['coordinator']

        print("Resuming from checkpoint...")
    else:
        # 初始化新状态
        problem = load_problem()
        order = create_task_order()
        solution = {}
        completed_tasks = set()
        coordinator = Coordinator()

    # 运行管道
    try:
        # Stage 1
        if 'stage1' not in completed_tasks:
            problem_analysis = run_stage1(problem)
            solution['stage1'] = problem_analysis
            completed_tasks.add('stage1')
            checkpoint_manager.save_checkpoint({
                'problem': problem,
                'order': order,
                'solution': solution,
                'completed_tasks': completed_tasks,
                'coordinator': coordinator
            })

        # Stage 2-4 类似...

    except Exception as e:
        # 保存检查点后崩溃
        checkpoint_manager.save_checkpoint({
            'problem': problem,
            'order': order,
            'solution': solution,
            'completed_tasks': completed_tasks,
            'coordinator': coordinator
        })
        raise e
```

### 优势

1. **透明恢复**: 用户无需任何操作，系统自动检测并恢复
2. **完整状态**: 保存所有必要状态，包括 problem、solution、coordinator
3. **增量保存**: 仅在关键阶段保存，减少 I/O 开销
4. **时间戳记录**: 便于追踪检查点创建时间

---

## 核心创新 2: Omni-Survival Kit (死手开关)

### 为什么重要？

AI Agent 系统可能在任何时刻崩溃（API 错误、内存溢出、网络问题）。Omni-Survival Kit 确保用户**总能获得输出**，即使系统崩溃。

### 实现细节

```python
import atexit
from datetime import datetime

class OmniSurvivalKit:
    """
    死手开关: 确保用户总能获得输出
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.final_report_path = os.path.join(output_dir, 'final_report.pdf')

        # 注册退出钩子
        atexit.register(self.generate_emergency_report)

    def generate_emergency_report(self):
        """
        生成紧急报告（如果最终报告不存在）

        这是最后的安全网，确保即使崩溃也生成输出
        """
        # 检查是否已有最终报告
        if os.path.exists(self.final_report_path):
            return

        print("⚠ Generating emergency report...")

        # 收集所有可用输出
        available_outputs = self._collect_available_outputs()

        # 如果没有任何输出，生成占位报告
        if not available_outputs:
            self._generate_placeholder_report()
            return

        # 从可用输出生成报告
        self._generate_report_from_outputs(available_outputs)

    def _collect_available_outputs(self):
        """
        收集所有可用的输出文件

        Returns:
            可用输出列表
        """
        outputs = []

        # 检查 JSON 输出
        json_dir = os.path.join(self.output_dir, 'Workspace/json/')
        if os.path.exists(json_dir):
            for file in os.listdir(json_dir):
                if file.endswith('.json'):
                    outputs.append(os.path.join(json_dir, file))

        # 检查 Markdown 输出
        md_dir = os.path.join(self.output_dir, 'Workspace/markdown/')
        if os.path.exists(md_dir):
            for file in os.listdir(md_dir):
                if file.endswith('.md'):
                    outputs.append(os.path.join(md_dir, file))

        # 检查图表
        charts_dir = os.path.join(self.output_dir, 'Workspace/charts/')
        if os.path.exists(charts_dir):
            for file in os.listdir(charts_dir):
                if file.endswith(('.png', '.jpg', '.pdf')):
                    outputs.append(os.path.join(charts_dir, file))

        return outputs

    def _generate_placeholder_report(self):
        """
        生成占位报告（当没有任何输出时）
        """
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter

        c = canvas.Canvas(self.final_report_path, pagesize=letter)

        # 标题
        c.setFont("Helvetica-Bold", 24)
        c.drawString(100, 750, "Mathematical Modeling Report")

        # 时间戳
        c.setFont("Helvetica", 12)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.drawString(100, 720, f"Generated: {timestamp}")

        # 错误信息
        c.setFont("Helvetica-Oblique", 14)
        c.drawString(100, 680, "Note: This report was auto-generated due to system failure.")
        c.drawString(100, 660, "Please check the logs for more details.")

        c.save()

        print(f"✓ Placeholder report generated: {self.final_report_path}")

    def _generate_report_from_outputs(self, outputs):
        """
        从可用输出生成报告
        """
        import markdown
        from weasyprint import HTML

        # 创建临时 Markdown 文件
        temp_md = os.path.join(self.output_dir, 'emergency_report.md')

        with open(temp_md, 'w') as f:
            f.write("# Mathematical Modeling Report\n\n")
            f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Available Outputs\n\n")

            for output in outputs:
                f.write(f"- {os.path.basename(output)}\n")

            # 如果有 JSON，尝试提取摘要
            json_files = [f for f in outputs if f.endswith('.json')]
            if json_files:
                f.write("\n## Results Summary\n\n")
                for json_file in json_files:
                    try:
                        with open(json_file, 'r') as jf:
                            data = json.load(jf)
                            f.write(f"### {os.path.basename(json_file)}\n\n")
                            f.write(f"```json\n{json.dumps(data, indent=2)}\n```\n\n")
                    except:
                        pass

        # 转换为 PDF
        with open(temp_md, 'r') as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)
        HTML(string=html_content).write_pdf(self.final_report_path)

        print(f"✓ Emergency report generated: {self.final_report_path}")

    def arm(self):
        """
        激活死手开关

        必须在管道开始前调用
        """
        # atexit 钩子已在 __init__ 中注册
        print("✓ Omni-Survival Kit armed")
```

### 使用方式

```python
def main():
    output_dir = "output/MM-Agent/test_problem_20250124/"
    survival_kit = OmniSurvivalKit(output_dir)
    survival_kit.arm()

    try:
        # 运行管道
        run_pipeline()
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        # atexit 会自动调用 generate_emergency_report
        raise e
```

### 优势

1. **保证输出**: 即使崩溃也生成 PDF
2. **自动触发**: 使用 `atexit` 自动注册，无需手动调用
3. **紧急模式**: 从可用输出生成报告，而非从头开始
4. **占位报告**: 即使没有任何输出也生成占位 PDF

---

## 核心创新 3: 异常处理与错误恢复

### 实现细节

```python
import traceback
import logging

class PipelineRunner:
    """
    管道运行器: 完整的异常处理和错误恢复
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.logger = self._setup_logger()
        self.checkpoint_manager = CheckpointManager(output_dir)
        self.survival_kit = OmniSurvivalKit(output_dir)

    def _setup_logger(self):
        """设置日志记录器"""
        logger = logging.getLogger('MMAgent')
        logger.setLevel(logging.DEBUG)

        # 文件日志
        log_file = os.path.join(self.output_dir, 'logs/pipeline.log')
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)

        # 控制台日志
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 格式化
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger

    def run(self):
        """
        运行管道，带有完整的异常处理
        """
        try:
            # 激活死手开关
            self.survival_kit.arm()

            # 尝试从检查点恢复
            if self.checkpoint_manager.has_checkpoint():
                self.logger.info("Resuming from checkpoint...")
                state = self.checkpoint_manager.load_checkpoint()
                problem = state['problem']
                completed_tasks = state['completed_tasks']
            else:
                self.logger.info("Starting new pipeline...")
                problem = self._load_problem()
                completed_tasks = set()

            # 运行管道
            self._run_pipeline_stages(problem, completed_tasks)

            self.logger.info("✓ Pipeline completed successfully")

        except KeyboardInterrupt:
            self.logger.warning("Pipeline interrupted by user")
            raise

        except Exception as e:
            self.logger.error(f"Pipeline failed: {e}")
            self.logger.error(traceback.format_exc())

            # 保存检查点
            self.checkpoint_manager.save_checkpoint({
                'problem': problem,
                'completed_tasks': completed_tasks,
                'error': str(e),
                'traceback': traceback.format_exc()
            })

            # 重新抛出异常（让 atexit 处理）
            raise e

    def _run_pipeline_stages(self, problem, completed_tasks):
        """运行管道的各个阶段"""
        stages = [
            ('stage1', self._run_stage1),
            ('stage2', self._run_stage2),
            ('stage3', self._run_stage3),
            ('stage4', self._run_stage4),
        ]

        for stage_name, stage_func in stages:
            if stage_name not in completed_tasks:
                self.logger.info(f"Running {stage_name}...")
                result = stage_func(problem)

                # 保存检查点
                completed_tasks.add(stage_name)
                self.checkpoint_manager.save_checkpoint({
                    'problem': problem,
                    'completed_tasks': completed_tasks,
                    f'{stage_name}_result': result
                })
            else:
                self.logger.info(f"Skipping {stage_name} (already completed)")
```

---

## 迁移价值

### 必须迁移 (P0)

- [ ] **Checkpoint 自动恢复** - 长时间运行系统的基础
- [ ] **Omni-Survival Kit** - 确保用户总能获得输出
- [ ] **异常处理框架** - 完整的错误恢复机制

### 强烈推荐 (P1)

- [ ] **4 阶段管道架构** - 标准化数学建模流程
- [ ] **进度反馈机制** - 每个阶段完成后打印进度
- [ ] **日志记录系统** - 详细的调试信息

### 可选迁移 (P2)

- [ ] **时间戳记录** - 追踪检查点和报告时间

---

## 核心创新点

1. **透明恢复**: Checkpoint 机制自动检测并恢复
2. **死手开关**: Omni-Survival Kit 确保总是有输出
3. **异常处理**: 完整的错误恢复框架
4. **进度反馈**: 每个阶段完成后打印进度
5. **日志记录**: 详细的调试信息和错误追踪

---

## 与其他资产的集成

| 资产 | 集成方式 |
|------|----------|
| **coordinator.py** (6-STARS) | 调度器状态保存到 Checkpoint |
| **execution_tracker.py** (5-STARS) | 事件追踪器记录所有阶段 |
| **autofixer.py** (6-STARS) | 错误恢复时调用自愈机制 |
| **latent_reporter.py** (5-STARS) | 崩溃后进行法医式分析 |

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
