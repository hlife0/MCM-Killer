# LLM-MM-Agent: 工具集

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/04_Utilities.md`
> **重要程度**: ⭐⭐ 辅助功能支撑层
> **迁移价值**: **中** - 部分工具可复用，但大部分可由 Claude Code 处理

本目录包含 40+ 工具模块，为系统提供安全验证、数据处理、代码执行、图表生成、日志管理、质量评估等辅助功能。这些工具模块被各个 Agent 和核心组件调用，构成了系统的基础设施。安全验证模块确保代码执行的安全性，是在不可信环境中运行生成代码的关键保障。数据处理模块提供数据清洗、转换、标准化等功能。计算与执行模块负责代码执行和状态跟踪。质量保证模块自动评估和修复代码。

**迁移价值**：工具集中的大部分模块是针对具体实现细节的，在迁移时需要选择性保留。安全验证模块（ast_path_guard.py, ast_validator.py, canonical_whitelist.py, code_guards.py, import_guard.py）是代码执行安全的保障，如果在迁移后系统也需要执行生成代码，这些模块的设计思想值得借鉴。嵌入生成模块（embedding.py）是实现基于相似度的知识检索的基础，如果新系统也有类似需求，这个模块很有价值。执行跟踪系统（execution_tracker.py）提供了完整的事件记录能力，对于调试和系统分析非常有帮助。其他工具（如数据处理、图表生成、模型训练等）在迁移时可以由 Claude Code 的内置能力替代，不需要特别关注。

---

## 核心流程模块

### `mathematical_modeling.py` ⭐⭐⭐⭐⭐
**数学建模管道**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/mathematical_modeling.py`。实现从 HMML 知识库检索方法、构建数学模型、推导公式的完整流程。核心特性包括：Context Pruning Strategy（"远近亲疏"策略）智能管理依赖上下文，防止 LLM 溢出；立即前驱任务获得完整上下文（描述1000字符、建模过程1000字符、结果2000字符、代码结构2000字符），早期依赖任务仅获得最小上下文（结果500字符、文件输出始终保留）。嵌入相似度匹配从 98+ 个建模方法中检索最相关的 top-K 方法。集成 LatentReporter 进行 LLM 驱动的叙述性日志记录。

**迁移价值**：数学建模的核心流程，展示了如何从知识库选择方法并应用。Context Pruning Strategy 防止上下文溢出的设计思想值得借鉴。依赖上下文管理的"远近亲疏"策略可以应用到任何需要处理复杂任务依赖的系统。

---

### `computational_solving.py` ⭐⭐⭐⭐⭐⭐
**计算求解管道**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/computational_solving.py`。生成和执行求解代码，将数学模型转换为可执行代码，在安全环境中执行，收集结果，生成图表。核心特性包括：Schema Registry 扫描输入文件和任务生成文件，提供列名和数据快照注入 LLM 提示词；AutoFixer 集成实现代码自愈；Workspace 三层目录结构（code/、json/、charts/）；路径自动修复防止硬编码路径问题；图表生成质量检查（SUCCESS/PARTIAL/FAILED 三态分类）。P0-1 过滤仅使用规范输入文件，防止提示词爆炸。

**迁移价值**：展示了"模型→代码→执行→可视化"的完整流程。Schema Registry 的数据快照机制防止 LLM 产生幻觉列名，值得借鉴。AutoFixer 自愈机制提高系统鲁棒性。三层目录组织结构清晰，可复用。

---

### `problem_analysis.py` ⭐⭐⭐⭐⭐⭐
**问题分析模块**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/problem_analysis.py`。采用 SURGICAL STRIKE 3 策略，动态生成专家级建模假设（不再依赖硬编码）。LLM 现场分析问题背景和需求，生成专家级假设。这个模块替代了之前的静态专家提示词库。

**迁移价值**：动态 LLM 驱动的问题分析方法比静态提示词库更灵活。分析阶段生成假设的思想可以应用到其他问题求解系统。

---

## 安全验证模块

### `ast_path_guard.py` ⭐⭐
**AST 路径保护模块**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/ast_path_guard.py`。验证和保护抽象语法树中的文件路径，防止恶意代码通过路径遍历攻击访问敏感文件（如 /etc/passwd、环境变量、密钥文件）。使用白名单机制，只允许访问特定的安全路径。

**迁移价值**：如果迁移后的系统需要执行不可信的生成代码，路径保护是必要的安全措施。这个模块的白名单机制值得借鉴。

---

### `ast_validator.py` ⭐⭐⭐
**抽象语法树验证器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/ast_validator.py`。检查生成代码的 AST 合法性，识别安全风险、语法错误、逻辑问题。核心功能包括：完整性检查（检测截断的代码）、未定义变量检测、导入验证、自动 save_fig 注入。提供详细的 ValidationIssue 报告。

**迁移价值**：静态代码分析是保障代码安全的重要手段。这个模块的 AST 分析思想和详细的验证报告机制值得借鉴。预执行验证层可以在运行前捕获大部分错误。

---

### `canonical_whitelist.py` ⭐⭐
**代码安全白名单**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/canonical_whitelist.py`。定义允许的 Python 操作和模块的官方列表，任何不在白名单中的操作都会被拒绝执行。⚠️ **DEPRECATED** - 功能已迁移到 DataManager.CANONICAL_INPUT_FILES（单一数据源）。

**迁移价值**：白名单机制是简单有效的安全控制方法。在迁移时可以采用类似的安全策略，但应该使用统一的单数据源模式。

---

### `code_guards.py` ⭐⭐⭐
**P0 工程守卫**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/code_guards.py`。10 个 P0 级别的工程守卫保障管道稳定性。Guard 1-5（预执行）：check_csv_reading 只允许 load_csv(name) 使用白名单，ban 直接 pd.read_csv 调用；check_column_usage 硬性验证拒绝使用不存在列的代码。Guard 6-10（运行时安全网）：各种运行时保护机制。

**迁移价值**：守卫模式防止崩溃。预执行验证和运行时安全网的组合可以应用到任何需要执行生成代码的系统。特别是列名硬验证可以有效防止 KeyError。

---

### `code_guards_enhanced.py` ⭐⭐
**增强型代码守卫**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/code_guards_enhanced.py`。P0 关键修复用于图表生成稳定性。ARROWPROPS_PATTERNS 修复 arrowprops 语法；check_synthetic_data 禁止合成数据（np.random、np.linspace）；enforce_code_block_only 强制仅代码块输出。

**迁移价值**：针对特定问题的守卫增强模式值得参考。合成数据检测可以防止模型使用假数据。

---

### `import_guard.py` ⭐⭐⭐
**P0-3 修复：AST 导入验证**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/import_guard.py`。基于 AST 的导入验证，DEFAULT_IMPORT_WHITELIST 定义允许的导入（pandas、numpy、matplotlib、seaborn、sklearn.model_selection 等），FORBIDDEN_IMPORTS 定义禁止的导入（torch、tensorflow、keras、sklearn.decomposition 等）。防止依赖死亡螺旋。

**迁移价值**：导入白名单和黑名单机制是简单有效的依赖控制方法。在迁移时可以采用类似的安全策略，防止不必要或危险的依赖。

---

### `env_guard.py` ⭐⭐
**环境验证**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/env_guard.py`。启动时验证环境（Direction 6, Option B）。检查缺失包和版本要求。REQUIRED_PACKAGES 定义最低版本（pandas 1.3.0、numpy 1.20.0、matplotlib 3.3.0）。

**迁移价值**：环境验证在启动时提前发现问题，防止运行时崩溃。版本要求机制值得借鉴。

---

## 数据处理模块

### `data_manager.py` ⭐⭐⭐⭐⭐⭐
**项目的"唯一数据指挥官"（CRITICAL FIX #5）**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/data_manager.py`。数据文件管理的单一真实源（Single Source of Truth）。核心功能：CANONICAL_INPUT_FILES 定义规范 CSV 文件集合（clean_athletes.csv、clean_hosts.csv、clean_medal_counts.csv、clean_programs.csv）；Schema 扫描和数据快照；get_data_snapshot() 生成数据的"全息指纹"。替代 canonical_whitelist.py，解决多数据源问题。

**迁移价值**：数据管理的核心架构。单一数据源模式、数据快照机制、Schema 管理都是非常通用的设计模式，强烈推荐迁移。

---

### `data_normalization.py` ⭐⭐⭐
**CSV 列名规范化**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/data_normalization.py`。处理 UTF-8 BOM 编码问题。normalize_column_name() 四步骤：移除 BOM、去除空白、转大写、空格替下划线。normalize_dataframe_columns() 批量规范化所有列名。read_csv_with_normalized_columns() 读取时自动规范化（utf-8-sig 默认，fallback latin1）。

**迁移价值**：防止数据加载错误。BOM 处理和列名规范化是数据管道的常见需求，这个模块的实现可以直接复用。

---

### `column_normalization.py` ⭐⭐⭐
**自动列名规范化**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/column_normalization.py`。为所有 DataFrame 操作创建自动列规范化包装器。normalize_dataframe_columns() 提供可配置的规范化选项（BOM、空白、大小写）。load_csv() 辅助函数带白名单验证。

**迁移价值**：防止 Schema 不匹配导致的 KeyError。自动规范化包装器模式可以应用到任何需要处理 DataFrame 的系统。

---

### `data_preprocessing.py` ⭐⭐⭐
**防御性数据摄取层 - "Data Customs"**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/data_preprocessing.py`。实现 Direction 5：在 Agent 看到数据之前扫描和预处理所有 CSV 文件。DataPreprocessor 类功能：移除 BOM、统一编码（UTF-8）、标准化列名、生成 data_profile.json（数据类型、值范围、样本值）。确保 LLM 只看到"完美"的干净数据。

**迁移价值**：彻底消灭 BOM 和 KeyError 连锁崩溃问题。Data Customs 模式是防御性编程的典范，值得在任何处理外部数据的系统中实施。

---

### `schema_manager.py` ⭐⭐⭐
**Schema 管理器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/schema_manager.py`。列名规范化带别名映射。normalize_column_name() 应用别名映射。处理 BOM 问题、大小写敏感性、空白字符。

**迁移价值**：防止列名不匹配导致的 KeyError。别名映射机制允许灵活的列名匹配，值得借鉴。

---

### `schema_registry.py` ⭐⭐⭐
**Schema 注册表**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/schema_registry.py`。动态 Schema 扫描从 CSV 文件。维护数据集 Schema 的集中注册表。SchemaRegistry 类：scan_directory() 扫描目录，format_for_prompt() 格式化为 LLM 提示词，get_statistics() 获取统计信息。

**迁移价值**：Schema 注册表是框架无关的，可以直接应用到其他评估场景。集中式 Schema 管理防止数据不一致。

---

### `schema_normalization.py` ⭐⭐⭐
**P0 Schema 稳定性修复**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/schema_normalization.py`。normalize_chart()、normalize_solution()、assert_syntax_ok()。图表三态分类：SUCCESS（代码+图片）/PARTIAL（仅代码）/FAILED（均无）。问题 5 修复：计算状态。

**迁移价值**：崩溃预防机制。三态分类提供更细粒度的质量评估，值得借鉴。

---

### `safe_merge.py` ⭐⭐⭐
**安全数据合并**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/safe_merge.py`。带类型断言和诊断的安全数据合并。防止合并脆弱性（类型不匹配、缺失键）。safe_merge_datasets() 四个关键步骤：验证合并键存在、类型断言和规范化、执行合并带 indicator、诊断输出。

**迁移价值**：健壮的数据处理模式。类型断言和诊断输出可以帮助快速定位数据问题，值得借鉴。

---

## 错误处理与自愈模块

### `autofixer.py` ⭐⭐⭐⭐⭐⭐
**通用自愈执行器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/autofixer.py`。Draft → Validate → Catch → Reflect & Fix → Loop 模式。fix_code() LLM 驱动的代码修复带历史跟踪。fix_json() JSON 修复带专门提示词。FixResult 数据类记录修复过程。

**迁移价值**：核心错误恢复基础设施。自愈模式可以显著提高系统鲁棒性，强烈推荐迁移到任何处理 LLM 生成代码的系统。

---

### `syntax_fixer.py` ⭐⭐⭐⭐
**P0-GUARD8：自动语法错误修复**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/syntax_fixer.py`。执行前语法清理，防止 80%+ 的语法错误。两个关键修复：移除等号后的逗号（pattern_comma_after_equals）、移除双逗号（pattern_double_comma）。pre_syntax_sanitize() 返回清理后的代码和修复列表。

**迁移价值**：防止常见的 LLM 生成语法垃圾。预处理修复可以显著提高代码执行成功率。

---

### `path_autofix.py` ⭐⭐⭐
**统一路径 AutoFix**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/path_autofix.py`。Chart 和 Computational 阶段的统一路径自动修复。apply_path_autofix_with_validation() 重写硬编码路径为 basename only。autofix_hardcoded_paths() 模式：pd.read_csv("C:/Users/.../file.csv") → pd.read_csv("file.csv")。

**迁移价值**：防止路径相关的 Guard 违规。硬编码路径自动修复可以显著减少代码执行错误。

---

### `fix_pattern_library.py` ⭐⭐
**错误修复模式库**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/fix_pattern_library.py`。P2 阶段：积累常见错误和修复方案，实现"秒回"建议。FixPatternLibrary 类：get_known_fix() 根据错误指纹检索已知修复，learn_fix() 学习新的修复模式，持久化到 JSON 文件。

**迁移价值**：错误知识库模式可以加速问题诊断，但需要长期积累才能发挥作用。

---

### `failure_handler.py` ⭐⭐⭐
**故障处理器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/failure_handler.py`。确保即使在管道失败时也能生成最小 JSON 输出。write_minimal_solution() 防止级联崩溃。

**迁移价值**：错误处理模式。保证最小输出是系统可靠性的关键，值得借鉴。

---

### `execution_fsm.py` ⭐⭐⭐
**任务执行有限状态机**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/execution_fsm.py`。用确定性状态转换替代"重试直到成功或最大次数"循环。ExecutionFSM.execute_task() 状态转换：START → VALIDATING → AUTO_FIXING → EXECUTING → VERIFYING → SUCCESS/FAILED。

**迁移价值**：可靠的执行模式。FSM 比简单的重试循环更可预测和可调试，值得借鉴。

---

## 日志与跟踪模块

### `execution_tracker.py` ⭐⭐⭐⭐⭐
**综合事件跟踪系统（Truth Mode）**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/execution_tracker.py`。记录所有执行事件的详细日志，包括 LLM 调用、代码执行、错误发生、状态变化等。log_error() 记录完整的 Python traceback 到 trace.jsonl 用于法医分析。track_llm_call()、track_code_execution() 等方法跟踪各种事件。

**迁移价值**：完整的事件追踪对于系统调试和分析非常重要。Truth Mode 日志记录的思想值得借鉴，可以用于任何需要详细审计的系统。

---

### `latent_reporter.py` ⭐⭐⭐⭐⭐
**潜伏报告器：后处理科研日记生成器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/latent_reporter.py`。观察者模式的科研日记生成器。读取 trace.jsonl 进行全面事件分析。reflect_on_stage() 阶段级复盘（problem_analysis、mathematical modeling）。diagnose_failure() 【Truth Mode】当 Pipeline 崩溃时进行法医式尸检分析。log_execution_failure() 生成深度调试报告（"1000 字报告"）。集成 FixPatternLibrary 实现结构化修复建议。

**迁移价值**：后处理分析系统。法医式尸检分析和结构化修复建议是非常通用的模式，可以应用到任何复杂系统的调试。

---

### `logging_config.py` ⭐⭐
**MMExperimentLogger**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/logging_config.py`。精简目录结构。单个 debug.log 包含所有事件。log_progress()、log_code_execution()、log_chart_generation()、log_llm_api_call() 等结构化日志方法。

**迁移价值**：日志模式可复用。结构化日志方法提供一致的日志接口，值得借鉴。

---

## 数据模型与工具模块

### `data_models.py` ⭐⭐⭐
**统一数据类**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/data_models.py`。ChartOutput、TaskResult、SolutionOutput 等数据类。防止管道阶段之间的字段命名不一致。TaskResult 使用 'modeling_formulas' 而非 'preliminary_formulas'（CRITICAL）。

**迁移价值**：数据契约定义对系统可靠性至关重要。统一的字段命名约定可以防止数据丢失，值得借鉴。

---

### `variable_contract.py` ⭐⭐⭐⭐
**变量契约系统**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/variable_contract.py`。建模和编码阶段之间的变量契约。VariableDefinition 数据类定义变量名、源类型、源列、推导公式、数据类型、必需性标志。验证变量对可用列，防止 UnboundLocalError。

**迁移价值**：对多阶段系统的变量依赖管理非常有用。契约系统可以防止阶段间的数据不一致。

---

### `embedding.py` ⭐⭐⭐⭐⭐
**嵌入相似度知识检索**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/embedding.py`。EmbeddingScorer 类为文本生成向量嵌入，用于 HMML 方法检索。使用 gte-multilingual-base 模型，fallback 关键词匹配。CRITICAL FIX 2026-01-21：使用 local_files_only=True 防止网络访问。

**迁移价值**：嵌入相似度是实现智能知识检索的核心技术。如果新系统也需要从大型知识库中检索相关内容，这个模块的实现思想非常重要。

---

### `utils.py` ⭐⭐⭐
**通用工具函数**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/utils.py`。PlatformUtils 类封装平台特定逻辑（Windows vs Linux/Mac）。normalize_task_fields() 任务字段向后兼容别名。parse_llm_output_to_json() 解析 LLM 输出为 JSON。robust_json_load() 使用 json_repair 的鲁棒解析。json_to_markdown() 转换论文字典为 Markdown。mkdir() 创建输出目录结构。load_config()、get_info() 配置和路径解析。

**迁移价值**：工具函数集合。平台封装、JSON 解析、目录创建等都是非常通用的功能，大部分可以复用。

---

### `json_utils.py` ⭐⭐⭐⭐
**多级防御 JSON 解析器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/json_utils.py`。Level 1：标准 json.loads；Level 2：json_repair 本地修复；Level 3：Regex 提取启发式；Level 4：AutoFixer LLM 驱动修复。JSONParser.parse() 统一解析接口。

**迁移价值**：鲁棒的 LLM 输出解析。多级防御策略提供从快速到彻底的解析选项，值得借鉴。

---

### `convert_format.py` ⭐
**格式转换**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/convert_format.py`。使用 regex 解析将 Markdown 转换为 JSON 方法格式。

**迁移价值**：格式转换工具，可重新实现。

---

## 质量保证模块

### `auto_evaluation.py` ⭐⭐⭐⭐⭐⭐
**自动质量评估**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/auto_evaluation.py`。管道运行后自动评估。评估 Problem Analysis、Mathematical Modeling、Computational Solving、Solution Reporting。

**迁移价值**：质量评估框架。自动评估提供系统健康检查，值得借鉴。

---

### `medal_allocation.py` ⭐⭐
**奖牌分配约束**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/medal_allocation.py`。强制总池约束（114000.05 → 2280.00）。三种分配方法：proportional、rank-based、hybrid。allocate_medals_with_constraint() 核心函数。

**迁移价值**：领域特定但约束模式可复用。约束优化模式值得借鉴。

---

## 图表生成模块

### `chart_config.py` ⭐⭐
**图表配置系统**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/chart_config.py`。基于 JSON 的图表配置带验证。ChartConfig 数据类定义图表类型、标题、尺寸、系列配置。模板化代码生成从 JSON 配置。

**迁移价值**：图表生成可由 Claude Code 处理。

---

### `chart_templates.py` ⭐⭐
**图表模板**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/chart_templates.py`。预定义图表模板库。

**迁移价值**：图表生成可由 Claude Code 处理。

---

### `minimal_chart_renderer.py` ⭐⭐
**最小稳定图表渲染器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/minimal_chart_renderer.py`。统一成功判定：仅检查 PNG 文件是否存在（代码可选）。render_chart() 返回布尔值。

**迁移价值**：图表生成可由 Claude Code 处理。

---

## 基础设施模块

### `rate_limiter.py` ⭐⭐⭐
**全局速率限制器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/rate_limiter.py`。LLM API 调用的全局速率限制（防止 Error 429）。Singleton 模式带 semaphore 并发控制。GlobalRateLimiter.acquire() 获取许可带超时。

**迁移价值**：防止 API 速率限制问题。Singleton 模式和 semaphore 并发控制是经典模式，值得借鉴。

---

### `solution_reporting.py` ⭐⭐⭐
**解决方案报告模块（Omni-Survival Kit）**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/utils/solution_reporting.py`。确保即使系统崩溃也能生成 PDF 报告。死手开关机制：atexit.register() 和 finally 块双重触发。AssetIndexer 扫描工作区所有资产。自动愈合 LaTeX 编译（注释错误行、移除缺失图片）。保证："只要结束就会启动，且不生成不罢休"。

**迁移价值**：系统可靠性的关键保障。死手开关机制确保用户总能获得输出，值得借鉴。自动愈合编译模式可以应用到其他文档生成场景。

---

**文档版本**: v2.0 (完整版)
**最后更新**: 2026-01-24
**文件总数**: 40+ 个工具模块
