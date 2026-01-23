# 4-STARS: 叙述生成与报告模块

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/04_NARRATIVE_REPORTING.md`
> **星级**: ⭐⭐⭐⭐
> **来源文档**: `08_MMAgent_Narrative.md`, `10_MMAgent_Reporting.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/narrative/`, `reporting/`

---

## 核心资产概览

### Narrative 模块 (4个)

| 组件 | 文件 | 核心功能 |
|------|------|----------|
| **Narrative Weaver** | `narrative_weaver.py` | 叙述编织器 |
| **Academic Tools** | `academic_tools.py` | 学术写作工具 |
| **Critique Generator** | `critique_generator.py` | 批评生成器 |
| **Abstract Orchestrator** | `abstract_orchestrator.py` | 摘要编排器 |

---

## 1. Narrative Weaver (叙述编织器)

```python
class NarrativeWeaver:
    """
    叙述编织器: 生成连贯的叙述文本
    """
    def __init__(self):
        self.transitions = [
            "首先，",
            "然后，",
            "接着，",
            "此外，",
            "最后，"
        ]

    def weave_narrative(self, sections: list) -> str:
        """
        编织叙述

        Args:
            sections: 章节列表 [(title, content), ...]

        Returns:
            完整叙述文本
        """
        narrative = []

        for i, (title, content) in enumerate(sections):
            # 添加过渡
            if i > 0:
                transition = self.transitions[min(i, len(self.transitions)-1)]
                narrative.append(f"\n{transition}")

            # 添加章节
            narrative.append(f"\n## {title}\n")
            narrative.append(content)

        return '\n'.join(narrative)
```

---

## 2. Academic Tools (学术写作工具)

```python
class AcademicTools:
    """
    学术写作工具集
    """
    def format_citation(self, author: str, year: int, title: str) -> str:
        """格式化引用"""
        return f"{author} ({year}). {title}."

    def generate_bibliography(self, citations: list) -> str:
        """生成参考文献"""
        bibliography = "\n## References\n\n"
        for i, citation in enumerate(citations, 1):
            bibliography += f"{i}. {citation}\n"
        return bibliography

    def format_formula(self, formula: str, label: str = "") -> str:
        """格式化公式"""
        if label:
            return f"$$\\label{{{label}}}\n{formula}\n$$"
        return f"$$\n{formula}\n$$"
```

---

## 3. Critique Generator (批评生成器)

```python
class CritiqueGenerator:
    """
    批评生成器: 生成批评性反馈
    """
    def __init__(self):
        self.critique_templates = [
            "该方法存在以下问题：{problems}",
            "需要改进的方面：{improvements}",
            "潜在风险：{risks}"
        ]

    def generate_critique(self, content: str) -> str:
        """
        生成批评

        Args:
            content: 待批评的内容

        Returns:
            批评文本
        """
        # 分析内容
        problems = self._identify_problems(content)
        improvements = self._suggest_improvements(content)
        risks = self._assess_risks(content)

        # 生成批评
        critiques = []
        critiques.append(self.critique_templates[0].format(problems=problems))
        critiques.append(self.critique_templates[1].format(improvements=improvements))
        critiques.append(self.critique_templates[2].format(risks=risks))

        return '\n\n'.join(critiques)

    def _identify_problems(self, content: str) -> str:
        """识别问题"""
        # 简化实现
        return "需要更详细的分析"

    def _suggest_improvements(self, content: str) -> str:
        """建议改进"""
        return "增加更多实验验证"

    def _assess_risks(self, content: str) -> str:
        """评估风险"""
        return "模型假设可能不成立"
```

---

## 4. Abstract Orchestrator (摘要编排器)

```python
class AbstractOrchestrator:
    """
    摘要编排器: 生成结构化摘要
    """
    def generate_abstract(self, full_text: str) -> dict:
        """
        生成摘要

        Returns:
            摘要字典 {background, methods, results, conclusion}
        """
        # 提取关键信息
        background = self._extract_background(full_text)
        methods = self._extract_methods(full_text)
        results = self._extract_results(full_text)
        conclusion = self._extract_conclusion(full_text)

        return {
            'background': background,
            'methods': methods,
            'results': results,
            'conclusion': conclusion
        }

    def _extract_background(self, text: str) -> str:
        """提取背景"""
        # 简化实现
        return "本研究..."

    def _extract_methods(self, text: str) -> str:
        """提取方法"""
        return "采用的方法..."

    def _extract_results(self, text: str) -> str:
        """提取结果"""
        return "主要结果..."

    def _extract_conclusion(self, text: str) -> str:
        """提取结论"""
        return "结论..."
```

---

## 应用场景

| 场景 | 使用的组件 |
|------|------------|
| **学术论文写作** | Academic Tools + Abstract Orchestrator |
| **报告生成** | Narrative Weaver + Critique Generator |
| **自我评审** | Critique Generator |
| **摘要生成** | Abstract Orchestrator |

---

## 迁移价值

### P0 - 必须迁移
- [ ] **Narrative Weaver** - 叙述连贯性
- [ ] **Academic Tools** - 引用格式化

### P1 - 强烈推荐
- [ ] **Abstract Orchestrator** - 摘要生成
- [ ] **Critique Generator** - 自我评审

### P2 - 可选迁移
- [ ] **完整叙述系统** - 所有组件

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
