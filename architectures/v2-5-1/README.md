# MCM-Killer v2.5.1: Architecture

> **LaTeX 强制编译版本** - 修复只生成Markdown的问题

---

## 版本目标

v2.5.1的核心目标是**强制LaTeX编译**,确保:

1. **PDF输出**: Writer必须生成可编译的.tex和.pdf
2. **文档一致**: 架构文档与agent配置完全同步
3. **编译验证**: 论文必须通过xelatex编译
4. **模板强制**: 必须使用latex_template/模板

---

## 关键改进

### 1. Writer Agent契约修复

**v2.5.0 (错误)**:
```
输出: paper/paper_{i}.md
```

**v2.5.1 (正确)**:
```
输出:
- paper/paper_{i}.tex      (LaTeX源文件)
- paper/paper_{i}.pdf      (编译后的PDF)
- paper/paper_{i}.md       (可选，Markdown备份)
```

### 2. 新增编译验证

Writer Agent完成后必须:
1. ✅ 使用xelatex编译.tex文件
2. ✅ 验证.pdf文件生成成功
3. ✅ 检查.pdf页数符合要求
4. ✅ 在Report中声明编译状态

### 3. Editor Agent契约同步

**v2.5.1要求**:
- 输入: `paper_{i}.tex` (不是.md)
- 输出: `paper_{i+1}.tex` + `paper_{i+1}.pdf`
- 必须重新编译验证

### 4. LaTeX模板路径

所有项目必须包含:
```
workspace/{year}_{letter}/
└── latex_template/          # [只读] MCM论文模板
    ├── mcmthesis.cls
    ├── mcmthesis-demo.tex
    └── figures/
```

Writer必须:
1. 复制模板到 `output/paper/`
2. 在复制的模板基础上修改
3. ❌ 禁止从零创建.tex

---

## Phase 7-9 流程变更

### Phase 7: Paper Writing (writer)

**输入**:
- `problem/problem_requirements_{i}.md`
- `model/model_design_{i}.md`
- `implementation/data/results_{i}.csv`
- `latex_template/` (只读)

**输出**:
- `output/paper/paper_{i}.tex` ✅ **新增**
- `output/paper/paper_{i}.pdf` ✅ **新增**
- `output/paper/paper_{i}.md` (可选)

**验证要求**:
- 必须通过xelatex编译
- PDF必须可读
- 页数≥20页

### Phase 8: Summary (summarizer)

**输入**:
- `paper/paper_{i}.tex`

**输出**:
- `paper/summary/summary_sheet_{i}.tex`
- `paper/summary/summary_{i}.md`

### Phase 9: Polish (editor)

**输入**:
- `paper/paper_{i}.tex`
- `paper/summary/summary_sheet_{i}.tex`

**输出**:
- `paper/paper_{i+1}.tex`
- `paper/paper_{i+1}.pdf` ✅ **重新编译**
- `paper/summary/summary_sheet_{i+1}.tex`
- `paper/summary/summary_sheet_{i+1}.pdf` ✅ **新增**

---

## 编译错误处理

### 环境问题

如果遇到:
- 缺失字体
- 缺失LaTeX包
- 编译失败

**正确流程**:
1. Writer停止编译
2. 通过Consultation请求feasibility_checker
3. feasibility_checker安装缺失包
4. Writer重新编译

**禁止**:
- ❌ 跳过编译只输出.md
- ❌ 使用简化方案绕过
- ❌ 修改系统环境

### 编译日志

必须记录:
```
output/paper/compile_{i}.log
```

包含:
- xelatex命令
- 编译输出
- 错误信息
- 最终状态

---

## 验证Gate变更

### PAPER Gate

**验证者**: reader, validator, advisor, writer

**新增检查项**:
- [ ] paper_{i}.tex文件存在且非空
- [ ] paper_{i}.pdf文件存在且可读
- [ ] PDF页数符合要求
- [ ] 编译日志无ERROR
- [ ] PDF内容与题目要求一致

**REJECTED条件**:
- 缺少.tex或.pdf文件
- PDF无法打开
- PDF内容为空或乱码
- 编译有未解决的错误

### FINAL Gate

**新增检查项**:
- [ ] 最终paper.pdf存在
- [ ] 最终summary_sheet.pdf存在
- [ ] 所有PDF可正常打开
- [ ] 文件大小合理（>10KB）

---

## 文件系统规则

### LaTeX模板目录

```
latex_template/               # [只读]
├── mcmthesis.cls            # MCM论文类文件
├── mcmthesis-demo.tex       # 示例论文
└── figures/                 # 示例图表
    ├── example-image-a.pdf
    ├── example-image-b.pdf
    └── example-image-c.pdf
```

**规则**:
- ✅ Writer可以读取
- ❌ Writer禁止修改
- ✅ Writer必须复制到output/paper/使用

### 输出目录结构

```
output/paper/
├── paper_{i}.tex            # LaTeX源文件
├── paper_{i}.pdf            # 编译后的PDF
├── paper_{i}.md             # Markdown备份(可选)
├── compile_{i}.log          # 编译日志
├── figures/                 # 论文图表
│   ├── figure_*.png
│   └── figure_index.md
└── summary/                 # 摘要
    ├── summary_sheet_{i}.tex
    ├── summary_sheet_{i}.pdf
    └── summary_1page.md
```

---

## 版本对比

| 特性 | v2.5.0 | v2.5.1 |
|------|--------|--------|
| Writer输出 | .md | .tex + .pdf (强制) |
| 编译要求 | 无 | 强制xelatex编译 |
| Editor输入 | .md | .tex |
| 文档一致性 | 部分不一致 | 完全同步 |
| 编译验证 | 无 | 每Phase必须验证 |

---

## 升级指南

### 从v2.5.0升级

1. **更新架构文档**:
```bash
cp architectures/v2-5-1/*.md workspace/2025_C/.claude/architecture/
```

2. **更新agents**:
```bash
cp -r architectures/v2-5-1/agents/* workspace/2025_C/.claude/agents/
```

3. **验证LaTeX环境**:
```bash
which xelatex
xelatex --version
```

4. **检查模板**:
```bash
ls -la latex_template/mcmthesis.cls
```

---

## 维护者

**Maintainer**: jcheniu
**Created**: 2026-01-11
**Based on**: v2.5.0
**Changes**: 修复LaTeX编译缺失问题
