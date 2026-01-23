# LLM-MM-Agent: 测试基础设施

> Path: `clean version/LLM-MM-Agent/test workplace/`

---

## Tests 目录 (`tests/`)

包含35+自动化测试文件，覆盖系统的各个模块和功能点。

### `01_error_logging_test.py`
错误日志验证测试，验证错误日志是否正确记录。检查日志格式、内容完整性、文件写入。

### `02_evaluation_always_runs.py`
评估系统始终运行测试，确保评估阶段在任何情况下都会执行。测试异常情况下的评估流程。

### `03_llm_code_correction_robustness.py`
LLM代码修正鲁棒性测试，测试LLM生成错误代码时的自动修正能力。模拟各种代码错误。

### `04_chart_generation_end_to_end.py`
图表生成端到端测试，测试从描述到图表的完整流程。验证各种图表类型的生成。

### `05_chart_data_schema_validation.py`
图表数据模式验证，检查生成的图表数据是否符合模式定义。验证数据结构、类型、约束。

### `06_import_validation.py`
导入验证测试，检查代码中的导入语句是否安全。验证只允许白名单中的模块。

### `07_data_validation.py`
数据验证测试，验证数据处理流程的正确性。检查数据加载、清洗、转换。

### `08_retry_strategy.py`
重试策略验证，测试API调用失败时的重试机制。验证重试次数、间隔、最终失败处理。

### `09_timeout_handling.py`
超时处理测试，测试代码执行超时的处理。验证超时检测、中断、资源清理。

### `10_chart_method.py`
图表方法测试，测试各种图表方法的正确性。验证数据映射、样式、输出。

### `11_stage4_output.py`
第4阶段输出测试，测试解决方案报告阶段的输出。验证PDF、LaTeX、JSON生成。

### `12_latex_generation.py`
LaTeX生成测试，测试LaTeX代码的生成和编译。验证语法、编译成功。

### `13_pdf_generation.py`
PDF生成测试，测试PDF文件的生成。验证文件完整性、内容正确性。

### `20_checkpoint_resume.py`
检查点恢复测试，测试管道状态保存和恢复。验证中断后能正确恢复。

### `30_method_recursion.py`
方法递归测试，测试HMML方法检索的递归逻辑。验证避免无限递归、正确终止。

### `31_chart_verification.py`
图表验证测试，验证生成图表的质量和正确性。检查图表元素、数据准确性。

### `40_latent_reporter.py`
潜在报告生成器测试，测试后处理研究日志的生成。验证日志内容、格式、完整性。

### `41_template_validation.py`
模板验证测试，验证提示词模板的正确性。检查变量替换、格式化。

### `42_safe_placeholder.py`
SafePlaceholder模式测试，测试模板格式化的容错能力。验证缺失变量时的处理。

### 更多测试文件...
覆盖集成测试、边界测试、性能测试、安全测试等各个方面。

---

## Docs 目录 (`docs/`)

### `README.md`
测试套件文档（中文），介绍测试框架、使用方法、测试策略。

### 测试文档文件
每个测试文件都有对应的文档说明，如：
- `01_error_logging_test.md`：错误日志测试文档
- `02_evaluation_always_runs.md`：评估测试文档
- `03_llm_code_correction_robustness.md`：代码修正鲁棒性文档
- ... (50+详细测试文档)

每个测试文档包含：
- 测试目的
- 测试方法
- 预期结果
- 相关bug修复记录

### `ultrathink/` 目录
深度分析报告，记录各次bug修复会话的详细分析：
- `ALL_FIXES_SUMMARY_2026_01_18.md`：完整bug修复总结
- `CHAT_WITH_CLAUDE1_FIXES_2026_01_18.md`：特定会话bug修复
- `COMPREHENSIVE_FIX_REPORT_ALL_SESSIONS_2026_01_18.md`：综合修复报告
- ... (40+详细分析文档)

---

## Results 目录 (`results/`)

存储测试执行结果，如：
- `01_error_logging_test.txt`
- `02_evaluation_always_runs.txt`
- `03_llm_code_correction_robustness.txt`
- ...

记录每次测试的输出、通过/失败状态、执行时间。

---

## Scripts 目录 (`scripts/`)

### `auto_monitor_charts.py`
自动图表监控脚本，监控图表生成过程并报告问题。

### `monitor_*.py`
运行时监控脚本，监控特定运行ID的执行状态。如：
- `monitor_170228.py`
- `monitor_174312.py`

### `periodic_chart_check.py`
周期性图表验证脚本，定期检查生成的图表是否符合要求。

---

## 其他文件

### `.pytest_cache/README.md`
Pytest缓存文档，说明pytest缓存机制。

### `.vscode/settings.json`
VS Code配置，包含测试相关的编辑器设置。

---

**文档版本**: v1.0
