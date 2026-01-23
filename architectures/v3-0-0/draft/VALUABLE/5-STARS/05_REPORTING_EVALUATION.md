# 5-STARS: 报告生成与评估框架

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/5-STARS/05_REPORTING_EVALUATION.md`
> **星级**: ⭐⭐⭐⭐⭐
> **来源文档**: `10_MMAgent_Reporting.md`, `17_MMBench.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/reporting/`, `MMBench/evaluation/`

---

## 核心资产概览

| 模块 | 位置 | 核心功能 | 创新点 |
|------|------|----------|--------|
| **报告生成** | `reporting/` | 多格式报告生成 | JSON → Markdown → LaTeX → PDF |
| **评估框架** | `MMBench/evaluation/` | 独立评估系统 | 用于自我升级和迭代 |

---

## 1. 报告生成框架 (reporting/)

### 为什么是 5 星？

`reporting/` 实现了**多格式报告生成管道**，从 JSON 结果自动生成 Markdown、LaTeX 和 PDF 格式的完整报告。

### 报告生成管道

```python
import json
import markdown
from weasyprint import HTML
from typing import Dict, Any

class ReportGenerator:
    """
    报告生成器: 多格式报告生成

    管道:
    JSON → Markdown → LaTeX → PDF
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.json_dir = os.path.join(output_dir, 'Workspace/json/')
        self.md_dir = os.path.join(output_dir, 'Workspace/markdown/')
        self.latex_dir = os.path.join(output_dir, 'Workspace/latex/')
        self.pdf_dir = os.path.join(output_dir, 'Report/')

        # 创建目录
        for dir_path in [self.json_dir, self.md_dir, self.latex_dir, self.pdf_dir]:
            os.makedirs(dir_path, exist_ok=True)

    def generate_from_json(self, json_data: Dict[str, Any], report_name: str = 'report'):
        """
        从 JSON 生成所有格式的报告

        Args:
            json_data: JSON 结果数据
            report_name: 报告名称
        """
        # 1. 保存 JSON
        self._save_json(json_data, report_name)

        # 2. 生成 Markdown
        md_content = self._generate_markdown(json_data)
        md_path = self._save_markdown(md_content, report_name)

        # 3. 生成 LaTeX
        latex_content = self._generate_latex(json_data)
        latex_path = self._save_latex(latex_content, report_name)

        # 4. 生成 PDF
        pdf_path = self._generate_pdf_from_markdown(md_content, report_name)

        return {
            'json': os.path.join(self.json_dir, f'{report_name}.json'),
            'markdown': md_path,
            'latex': latex_path,
            'pdf': pdf_path
        }

    def _generate_markdown(self, data: Dict[str, Any]) -> str:
        """生成 Markdown 报告"""
        md = []

        # 标题
        md.append(f"# {data.get('title', 'Mathematical Modeling Report')}\n")
        md.append(f"**Generated**: {data.get('timestamp', '')}\n")
        md.append(f"**Problem**: {data.get('problem', '')}\n\n")

        # 摘要
        if 'abstract' in data:
            md.append("## Abstract\n")
            md.append(f"{data['abstract']}\n\n")

        # 问题分析
        if 'problem_analysis' in data:
            md.append("## Problem Analysis\n")
            md.append(f"{data['problem_analysis']}\n\n")

        # 方法
        if 'methods' in data:
            md.append("## Methods\n")
            for method in data['methods']:
                md.append(f"### {method['name']}\n")
                md.append(f"{method['description']}\n\n")

        # 结果
        if 'results' in data:
            md.append("## Results\n")
            md.append(f"{data['results']}\n\n")

        # 图表
        if 'charts' in data:
            md.append("## Figures\n")
            for chart in data['charts']:
                md.append(f"![{chart['caption']}]({chart['path']})\n\n")
                md.append(f"*{chart['caption']}*\n\n")

        # 结论
        if 'conclusion' in data:
            md.append("## Conclusion\n")
            md.append(f"{data['conclusion']}\n\n")

        return '\n'.join(md)

    def _generate_latex(self, data: Dict[str, Any]) -> str:
        """生成 LaTeX 报告"""
        latex = []

        # 文档类
        latex.append("\\documentclass{article}\n")
        latex.append("\\usepackage[utf8]{inputenc}")
        latex.append("\\usepackage{graphicx}")
        latex.append("\\usepackage{amsmath}")
        latex.append("\\usepackage{hyperref}\n")

        # 标题
        latex.append("\\title{" + data.get('title', 'Mathematical Modeling Report') + "}")
        latex.append("\\author{MCM Team}")
        latex.append("\\date{" + data.get('timestamp', '') + "}")
        latex.append("\\begin{document}\n")
        latex.append("\\maketitle\n")

        # 摘要
        if 'abstract' in data:
            latex.append("\\begin{abstract}")
            latex.append(data['abstract'])
            latex.append("\\end{abstract}\n")

        # 章节
        sections = ['Problem Analysis', 'Methods', 'Results', 'Figures', 'Conclusion']
        section_keys = ['problem_analysis', 'methods', 'results', 'charts', 'conclusion']

        for section, key in zip(sections, section_keys):
            if key in data:
                latex.append(f"\\section{{{section}}}\n")
                if key == 'methods':
                    for method in data[key]:
                        latex.append(f"\\subsection{{{method['name']}}}\n")
                        latex.append(method['description'] + "\n\n")
                elif key == 'charts':
                    for chart in data[key]:
                        latex.append(f"\\begin{{figure}}[h]\n")
                        latex.append(f"\\includegraphics[width=0.8\\textwidth]{{{chart['path']}}}\n")
                        latex.append(f"\\caption{{{chart['caption']}}}\n")
                        latex.append(f"\\end{{figure}}\n\n")
                else:
                    latex.append(str(data[key]) + "\n\n")

        latex.append("\\end{document}")

        return '\n'.join(latex)

    def _generate_pdf_from_markdown(self, md_content: str, report_name: str) -> str:
        """从 Markdown 生成 PDF"""
        # 转换为 HTML
        html_content = markdown.markdown(md_content)

        # 添加 CSS
        html_with_style = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
                h1 {{ color: #333; }}
                h2 {{ color: #555; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                img {{ max-width: 100%; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # 生成 PDF
        pdf_path = os.path.join(self.pdf_dir, f'{report_name}.pdf')
        HTML(string=html_with_style).write_pdf(pdf_path)

        return pdf_path

    def _save_json(self, data: Dict[str, Any], report_name: str):
        """保存 JSON"""
        path = os.path.join(self.json_dir, f'{report_name}.json')
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

    def _save_markdown(self, content: str, report_name: str) -> str:
        """保存 Markdown"""
        path = os.path.join(self.md_dir, f'{report_name}.md')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def _save_latex(self, content: str, report_name: str) -> str:
        """保存 LaTeX"""
        path = os.path.join(self.latex_dir, f'{report_name}.tex')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path
```

---

## 2. 评估框架 (MMBench/evaluation/)

### 为什么是 5 星？

`evaluation/` 是**独立评估框架**，用于评估模型在数学建模问题上的表现，可以用于系统的自我升级和迭代。

### 评估框架核心

```python
import os
import json
import subprocess
from typing import Dict, List, Any

class EvaluationFramework:
    """
    评估框架: 独立评估系统

    功能:
    1. 运行模型
    2. 评估结果
    3. 生成报告
    4. 自我升级
    """
    def __init__(self, evaluation_dir):
        self.evaluation_dir = evaluation_dir
        self.results_dir = os.path.join(evaluation_dir, 'results/')
        os.makedirs(self.results_dir, exist_ok=True)

    def evaluate_model(self, model_name: str, problem_dir: str) -> Dict[str, Any]:
        """
        评估模型在所有问题上的表现

        Args:
            model_name: 模型名称
            problem_dir: 问题目录

        Returns:
            评估报告
        """
        # 获取所有问题
        problems = self._get_problems(problem_dir)

        results = []
        for problem in problems:
            # 运行模型
            result = self._run_on_problem(model_name, problem)
            results.append(result)

        # 汇总结果
        report = self._generate_report(model_name, results)

        # 保存报告
        self._save_report(model_name, report)

        return report

    def _get_problems(self, problem_dir: str) -> List[Dict[str, Any]]:
        """获取所有问题"""
        problems = []
        for file in os.listdir(problem_dir):
            if file.endswith('.json'):
                with open(os.path.join(problem_dir, file)) as f:
                    problems.append(json.load(f))
        return problems

    def _run_on_problem(self, model_name: str, problem: Dict[str, Any]) -> Dict[str, Any]:
        """在单个问题上运行模型"""
        # 运行模型
        output = subprocess.run(
            ['python', 'MMAgent/main.py', '--model_name', model_name, '--task', problem['id']],
            capture_output=True,
            text=True
        )

        # 评估结果
        score = self._score_output(problem, output)

        return {
            'problem_id': problem['id'],
            'score': score,
            'output': output,
            'metadata': problem.get('metadata', {})
        }

    def _score_output(self, problem: Dict[str, Any], output: str) -> float:
        """评估输出质量"""
        # 这里可以实现各种评估指标
        # 例如：准确性、完整性、格式正确性等

        score = 0.0

        # 检查输出格式
        if '{' in output and '}' in output:
            score += 0.3

        # 检查输出长度
        if len(output) > 100:
            score += 0.3

        # 检查关键词
        keywords = problem.get('keywords', [])
        found_keywords = sum(1 for kw in keywords if kw.lower() in output.lower())
        if keywords:
            score += 0.4 * (found_keywords / len(keywords))

        return score

    def _generate_report(self, model_name: str, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成评估报告"""
        total_score = sum(r['score'] for r in results)
        avg_score = total_score / len(results) if results else 0.0

        return {
            'model_name': model_name,
            'total_problems': len(results),
            'average_score': avg_score,
            'results': results,
            'timestamp': datetime.now().isoformat()
        }

    def _save_report(self, model_name: str, report: Dict[str, Any]):
        """保存评估报告"""
        path = os.path.join(self.results_dir, f'{model_name}_evaluation.json')
        with open(path, 'w') as f:
            json.dump(report, f, indent=2)

    def compare_models(self, model_names: List[str], problem_dir: str) -> Dict[str, Any]:
        """比较多个模型"""
        comparison = {}
        for model_name in model_names:
            report = self.evaluate_model(model_name, problem_dir)
            comparison[model_name] = report['average_score']

        # 排序
        sorted_models = sorted(comparison.items(), key=lambda x: x[1], reverse=True)

        return {
            'comparison': comparison,
            'ranking': sorted_models,
            'best_model': sorted_models[0][0] if sorted_models else None
        }
```

### 自我升级和迭代

```python
class SelfImprovingSystem:
    """
    自我升级系统: 使用评估框架迭代改进
    """
    def __init__(self, evaluation_framework):
        self.evaluation_framework = evaluation_framework
        self.iteration = 0

    def improve(self, base_model: str, problem_dir: str, max_iterations: int = 10):
        """
        迭代改进

        Args:
            base_model: 基础模型
            problem_dir: 问题目录
            max_iterations: 最大迭代次数
        """
        current_model = base_model

        for i in range(max_iterations):
            self.iteration += 1
            print(f"\n=== Iteration {self.iteration} ===")

            # 评估当前模型
            report = self.evaluation_framework.evaluate_model(current_model, problem_dir)
            print(f"Average score: {report['average_score']:.3f}")

            # 分析弱点
            weaknesses = self._analyze_weaknesses(report)

            # 生成改进策略
            improvements = self._generate_improvements(weaknesses)

            # 应用改进
            improved_model = self._apply_improvements(current_model, improvements)
            improved_model_name = f"{base_model}_iter{self.iteration}"

            # 评估改进后的模型
            improved_report = self.evaluation_framework.evaluate_model(
                improved_model_name, problem_dir
            )
            print(f"Improved score: {improved_report['average_score']:.3f}")

            # 检查是否收敛
            if improved_report['average_score'] - report['average_score'] < 0.01:
                print("Converged!")
                break

            current_model = improved_model_name

    def _analyze_weaknesses(self, report: Dict[str, Any]) -> List[str]:
        """分析弱点"""
        weaknesses = []

        # 找出得分低的问题
        low_score_results = [
            r for r in report['results']
            if r['score'] < 0.5
        ]

        if low_score_results:
            weaknesses.append(f"Low score on {len(low_score_results)} problems")

        return weaknesses

    def _generate_improvements(self, weaknesses: List[str]) -> Dict[str, Any]:
        """生成改进策略"""
        improvements = {}

        for weakness in weaknesses:
            if 'Low score' in weakness:
                improvements['prompt_engineering'] = 'Improve system prompts'

        return improvements

    def _apply_improvements(self, model: str, improvements: Dict[str, Any]) -> str:
        """应用改进"""
        # 这里可以实现具体的改进逻辑
        # 例如：修改提示词、调整参数等
        return f"{model}_improved"
```

### 使用示例

```python
# 评估框架
ef = EvaluationFramework('MMBench/evaluation/')

# 评估单个模型
report = ef.evaluate_model('gpt-4o', 'MMBench/problem/')
print(f"Average score: {report['average_score']:.3f}")

# 比较多个模型
comparison = ef.compare_models(['gpt-4o', 'deepseek-chat', 'glm-4-plus'], 'MMBench/problem/')
print(f"Best model: {comparison['best_model']}")

# 自我升级
sis = SelfImprovingSystem(ef)
sis.improve('gpt-4o', 'MMBench/problem/', max_iterations=5)
```

---

## 迁移价值

### 必须迁移 (P0)

- [ ] **多格式报告生成** - JSON → Markdown → LaTeX → PDF
- [ ] **评估框架** - 独立评估系统
- [ ] **自我升级机制** - 迭代改进

### 强烈推荐 (P1)

- [ ] **Markdown 模板** - 标准化报告格式
- [ ] **LaTeX 模板** - 学术论文格式
- [ ] **模型比较** - 多模型对比

### 可选迁移 (P2)

- [ ] **PDF 生成** - WeasyPrint 或其他工具
- [ ] **评估指标** - 自定义评分函数

---

## 核心创新点

### 报告生成

1. **多格式管道**: JSON → Markdown → LaTeX → PDF
2. **自动化**: 从 JSON 一键生成所有格式
3. **可定制**: 模板可自定义

### 评估框架

1. **独立性**: 不依赖特定实现
2. **自我升级**: 使用评估结果迭代改进
3. **模型比较**: 支持多模型对比

---

## 与其他资产的集成

| 资产 | 集成方式 |
|------|----------|
| **main.py** (5-STARS) | Omni-Survival Kit 使用报告生成 |
| **latent_reporter.py** (5-STARS) | 评估报告包含在法医分析中 |

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
