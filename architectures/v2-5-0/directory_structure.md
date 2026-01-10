# MCM-Killer v2.5.0: 目录结构规范

> **解决架构路径访问问题的关键文档**

---

## 设计原则

### Principle 1: Workspace自包含

每个workspace必须包含完整的项目文件,包括:
- `.claude/architecture/` - 架构副本
- `.claude/agents/` - Agent定义
- `output/` - 输出目录

**原因**: AI在workspace中工作时无法访问父目录的`architectures/`

### Principle 2: Architectures作为模板

`architectures/`目录是**模板库**,不是运行时依赖:
- 存储不同版本的架构定义
- 用于创建新workspace
- 作为参考文档

### Principle 3: 相对路径引用

所有引用使用**相对路径**:
- ✅ `.claude/architecture/architecture.md`
- ❌ `architectures/v2-5-0/architecture.md`

---

## 完整目录结构

```
MCM-Killer/                           # 项目根目录
│
├── architectures/                    # 全局架构模板库
│   ├── v2-3-0.md
│   ├── v2-4-0/
│   │   ├── architecture.md
│   │   ├── methodology.md
│   │   └── retrospective.md
│   ├── v2-4-1/
│   │   ├── architecture.md
│   │   ├── methodology.md
│   │   └── retrospective.md
│   └── v2-5-0/                      # ← 当前版本
│       ├── CHANGELOG.md
│       ├── README.md
│       ├── architecture.md          # 核心架构定义
│       ├── directory_structure.md   # 本文件
│       ├── anti_lazy_mechanisms.md
│       └── agents/                  # Agent模板
│           ├── director.md
│           ├── reader.md
│           ├── researcher.md
│           ├── modeler.md
│           ├── data_engineer.md
│           ├── code_translator.md
│           ├── model_trainer.md
│           ├── validator.md
│           ├── visualizer.md
│           ├── writer.md
│           ├── summarizer.md
│           ├── editor.md
│           ├── advisor.md
│           └── feasibility_checker.md
│
├── workspace/                       # 项目工作区
│   └── 2025_C/                     # 具体项目 (MCM 2025 Problem C)
│       │
│       ├── .claude/                # Claude配置 (隐藏目录)
│       │   │
│       │   ├── architecture/       # ← 项目专用架构副本
│       │   │   └── architecture.md # 从architectures/v2-5-0复制
│       │   │
│       │   ├── agents/             # Agent定义副本
│       │   │   ├── director.md
│       │   │   ├── reader.md
│       │   │   ├── researcher.md
│       │   │   ├── modeler.md
│       │   │   ├── data_engineer.md
│       │   │   ├── code_translator.md
│       │   │   ├── model_trainer.md
│       │   │   ├── validator.md
│       │   │   ├── visualizer.md
│       │   │   ├── writer.md
│       │   │   ├── summarizer.md
│       │   │   ├── editor.md
│       │   │   ├── advisor.md
│       │   │   └── feasibility_checker.md
│       │   │
│       │   └── settings.local.json # Claude本地设置
│       │
│       ├── output/                 # 所有输出 (唯一可写目录)
│       │   ├── VERSION_MANIFEST.json
│       │   │
│       │   ├── problem/            # 问题文件
│       │   │   ├── original/
│       │   │   │   ├── 2025_MCM_Problem_C.pdf
│       │   │   │   └── 2025_Problem_C_Data/
│       │   │   ├── problem_full.md
│       │   │   └── problem_requirements_1.md
│       │   │
│       │   ├── docs/               # 协作文档
│       │   │   ├── consultation/
│       │   │   │   ├── 1_modeler_researcher.md
│       │   │   │   └── ...
│       │   │   ├── validation/
│       │   │   │   ├── 1_MODEL_reader.md
│       │   │   │   ├── 2_MODEL_advisor.md
│       │   │   │   └── ...
│       │   │   └── report/
│       │   │       ├── reader_1.md
│       │   │       ├── modeler_1.md
│       │   │       └── ...
│       │   │
│       │   ├── model/              # 模型设计
│       │   │   ├── research_notes_1.md
│       │   │   ├── model_design_1.md
│       │   │   └── feasibility_1.md
│       │   │
│       │   ├── implementation/     # 实现相关
│       │   │   ├── .venv/          # Python虚拟环境
│       │   │   ├── data/
│       │   │   │   ├── raw/
│       │   │   │   ├── processed/
│       │   │   │   ├── features_1.pkl
│       │   │   │   └── results_1.csv
│       │   │   ├── code/
│       │   │   │   ├── data_prep_1.py
│       │   │   │   ├── model_1.py
│       │   │   │   └── test_1.py
│       │   │   ├── logs/
│       │   │   │   └── training_1.log
│       │   │   └── analysis/
│       │   │       └── model_trainer_summary_1.md
│       │   │
│       │   └── paper/              # 论文相关
│       │       ├── paper_1.tex
│       │       ├── paper_1.pdf
│       │       ├── figures/
│       │       │   ├── fig_trends_1.png
│       │       │   ├── fig_trends_1.pdf
│       │       │   ├── figure_index.md
│       │       │   └── ...
│       │       └── summary/
│       │           ├── summary_sheet_1.tex
│       │           └── summary_sheet_1.pdf
│       │
│       ├── reference_papers/        # 参考论文 (只读)
│       ├── latex_template/         # LaTeX模板 (只读)
│       │
│       └── CLAUDE.md               # 项目入口文档
│
└── README.md                       # MCM-Killer总体说明
```

---

## 关键目录说明

### `/architectures/`

**用途**: 架构模板和版本控制

**内容**:
- 历史版本 (v2-3-0, v2-4-0, v2-4-1)
- 当前版本 (v2-5-0)
- Agent模板
- 文档和CHANGELOG

**访问权限**:
- ✅ 用户读写
- ✅ 创建workspace时复制
- ❌ AI在workspace中不可访问

### `/workspace/{project}/.claude/architecture/`

**用途**: 项目专用架构副本 (运行时依赖)

**内容**:
- 从`architectures/v2-5-0/`复制的架构文件
- 可能包含项目特定的修改

**访问权限**:
- ✅ AI完全可访问
- ✅ 相对路径引用
- ❌ 不应该手动修改 (应该修改模板后重新复制)

### `/workspace/{project}/.claude/agents/`

**用途**: Agent定义副本

**内容**:
- 13个Agent的prompt文件
- 每个Agent引用`.claude/architecture/architecture.md`

**访问权限**:
- ✅ AI完全可访问
- ✅ Director调用其他Agent时读取
- ❌ 不应该手动修改

### `/workspace/{project}/output/`

**用途**: 所有输出 (唯一可写目录)

**规则**:
- ✅ 所有Agent必须写入这里
- ❌ 禁止修改`output/`以外的文件
- ❌ 禁止修改`.claude/`, `reference_papers/`, `latex_template/`

---

## 路径引用规范

### 在CLAUDE.md中

**正确** (v2.5.0):
```markdown
> **权威参考**: `.claude/architecture/architecture.md`
```

**错误** (v2.4.1):
```markdown
> **权威参考**: `architectures/v2-4-1/architecture.md`
```

### 在Agent prompts中

**正确** (v2.5.0):
```markdown
## Agent定义

> **基于**: `.claude/architecture/architecture.md`
```

**错误** (v2.4.1):
```markdown
## Agent定义

> **基于**: `architectures/v2-4-1/architecture.md`
```

### 在代码中

**Python示例**:
```python
# 读取架构
ARCHITECTURE_PATH = ".claude/architecture/architecture.md"
with open(ARCHITECTURE_PATH) as f:
    architecture = f.read()
```

---

## 创建新Workspace

### 方法1: 手动创建

```bash
# 1. 创建目录结构
mkdir -p workspace/2026_A/.claude/{architecture,agents}
mkdir -p workspace/2026_A/{output,reference_papers,latex_template}

# 2. 复制架构
cp architectures/v2-5-0/*.md workspace/2026_A/.claude/architecture/

# 3. 复制agents
cp architectures/v2-5-0/agents/*.md workspace/2026_A/.claude/agents/

# 4. 创建CLAUDE.md
cp architectures/v2-5-0/CLAUDE.template.md workspace/2026_A/CLAUDE.md

# 5. 初始化output目录
cd workspace/2026_A/output
mkdir -p {problem,docs/{consultation,validation,report},model,implementation/{.venv,data,code,logs,analysis},paper/{figures,summary}}
```

### 方法2: 使用脚本 (推荐)

创建`scripts/create_workspace.sh`:

```bash
#!/bin/bash
PROJECT_NAME=$1  # e.g., 2026_A

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: ./create_workspace.sh <project_name>"
    exit 1
fi

WORKSPACE="workspace/$PROJECT_NAME"
ARCH_VERSION="v2-5-0"

echo "Creating workspace: $WORKSPACE"

# 创建目录结构
mkdir -p "$WORKSPACE/.claude/architecture"
mkdir -p "$WORKSPACE/.claude/agents"
mkdir -p "$WORKSPACE/output/"{problem,docs/{consultation,validation,report},model,implementation/{.venv,data/{raw,processed},code,logs,analysis},paper/{figures,summary}}
mkdir -p "$WORKSPACE/reference_papers"
mkdir -p "$WORKSPACE/latex_template"

# 复制架构
echo "Copying architecture from $ARCH_VERSION..."
cp "architectures/$ARCH_VERSION"/*.md "$WORKSPACE/.claude/architecture/"

# 复制agents
echo "Copying agents..."
cp "architectures/$ARCH_VERSION/agents"/*.md "$WORKSPACE/.claude/agents/"

# 创建CLAUDE.md
echo "Creating CLAUDE.md..."
cp "architectures/$ARCH_VERSION/CLAUDE.template.md" "$WORKSPACE/CLAUDE.md"

# 创建VERSION_MANIFEST.json
echo "Creating VERSION_MANIFEST.json..."
cat > "$WORKSPACE/output/VERSION_MANIFEST.json" << EOF
{
  "created_at": "$(date '+%Y-%m-%d %H:%M:%S')",
  "last_updated": "$(date '+%Y-%m-%d %H:%M:%S')",
  "files": {},
  "agent_calls": {},
  "consultation_count": 0,
  "validation_count": 0
}
EOF

echo "Workspace created successfully!"
echo "Location: $WORKSPACE"
```

使用:
```bash
chmod +x scripts/create_workspace.sh
./scripts/create_workspace.sh 2026_A
```

---

## 验证Workspace完整性

### 检查脚本

创建`scripts/verify_workspace.sh`:

```bash
#!/bin/bash
WORKSPACE=$1

if [ -z "$WORKSPACE" ]; then
    echo "Usage: ./verify_workspace.sh <workspace_path>"
    exit 1
fi

echo "Verifying workspace: $WORKSPACE"
echo ""

ERRORS=0

# 检查架构文件
if [ ! -f "$WORKSPACE/.claude/architecture/architecture.md" ]; then
    echo "❌ Missing: .claude/architecture/architecture.md"
    ERRORS=$((ERRORS + 1))
else
    echo "✅ Found: .claude/architecture/architecture.md"
fi

# 检查agents
EXPECTED_AGENTS=13
ACTUAL_AGENTS=$(ls "$WORKSPACE/.claude/agents"/*.md 2>/dev/null | wc -l)
if [ "$ACTUAL_AGENTS" -ne "$EXPECTED_AGENTS" ]; then
    echo "❌ Agent count mismatch: expected $EXPECTED_AGENTS, found $ACTUAL_AGENTS"
    ERRORS=$((ERRORS + 1))
else
    echo "✅ Found: $EXPECTED_AGENTS agents"
fi

# 检查CLAUDE.md
if [ ! -f "$WORKSPACE/CLAUDE.md" ]; then
    echo "❌ Missing: CLAUDE.md"
    ERRORS=$((ERRORS + 1))
else
    echo "✅ Found: CLAUDE.md"
fi

# 检查output目录
OUTPUT_DIRS=("problem" "docs" "model" "implementation" "paper")
for dir in "${OUTPUT_DIRS[@]}"; do
    if [ ! -d "$WORKSPACE/output/$dir" ]; then
        echo "❌ Missing: output/$dir"
        ERRORS=$((ERRORS + 1))
    else
        echo "✅ Found: output/$dir"
    fi
done

echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Workspace verification PASSED"
    exit 0
else
    echo "❌ Workspace verification FAILED: $ERRORS errors"
    exit 1
fi
```

使用:
```bash
chmod +x scripts/verify_workspace.sh
./scripts/verify_workspace.sh workspace/2025_C
```

---

## 版本管理

### 升级Workspace到新架构版本

```bash
# 从v2-4-1升级到v2-5-0
OLD_VERSION="v2-4-1"
NEW_VERSION="v2-5-0"
PROJECT="2025_C"

# 备份
cp -r "workspace/$PROJECT" "workspace/${PROJECT}_backup_$(date +%Y%m%d)"

# 更新架构
cp "architectures/$NEW_VERSION"/*.md "workspace/$PROJECT/.claude/architecture/"

# 更新agents
cp "architectures/$NEW_VERSION/agents"/*.md "workspace/$PROJECT/.claude/agents/"

# 验证
./scripts/verify_workspace.sh "workspace/$PROJECT"
```

---

## 常见问题

### Q1: 为什么不能直接引用`architectures/`?

**A**: AI在workspace中工作时,工作目录是`workspace/2025_C/`,无法访问父目录的`architectures/`。相对路径`.claude/architecture/`确保AI可以读取。

### Q2: 架构更新后需要同步所有workspace吗?

**A**: 是的。修改`architectures/v2-5-0/`后,需要重新复制到所有使用该版本的workspace。

### Q3: 可以在workspace中直接修改架构吗?

**A**: 不建议。应该在`architectures/v2-5-0/`中修改,然后重新复制。直接修改会导致版本不一致。

---

**Maintainer**: jcheniu
**Last Updated**: 2026-01-07
**Version**: 2.5.0
