# LLM-MM-Agent: 项目根目录

> Path: `clean version/LLM-MM-Agent/`

---

## 配置文件

### `config.yaml`
主配置文件，控制整个系统的运行参数。定义了迭代轮次（problem_analysis_round: 3, problem_modeling_round: 3）、任务限制（num_tasks: 5, num_charts: 5）、方法检索数量（top_method_num: 6）、路径配置（paths.root_data, paths.output_root）以及调试模式开关。这是系统运行的单一配置入口。

### `requirements.txt`
Python依赖包清单，列出项目所需的所有第三方库及其版本要求。包括数据处理（pandas, numpy）、可视化（matplotlib, seaborn）、LLM接口（openai）、日志（loguru）等核心依赖。

## 文档

### `README.md`
项目主文档，包含简介、安装指南、使用示例、配置说明。面向国际用户的英文文档，提供快速开始教程和基本用法说明。

### `README_zh.md`
中文版README，为中文用户提供详细的安装步骤、使用指南和常见问题解答。

### `doc/User_Guide.md`
详细用户指南，包含完整的安装说明、工作流程解释、各阶段详解、高级用法、故障排除等。比README更深入的技术文档。

### `CLAUDE.md`
Claude Code指导文档，为AI助手提供项目架构概览、开发指南、核心模式说明、关键路径标注。帮助Claude理解项目结构和开发规范。

## 启动脚本

### `run.py`
启动引导脚本，自动设置Python路径环境并启动主程序。处理导入路径问题，确保从正确目录运行。

### `__init__.py`
包初始化文件，将目录标记为Python包。

## 其他文件

### `LICENSE`
开源许可证文件，规定项目的使用、修改、分发条款。

### `.DS_Store`
Mac系统自动生成的文件，存储文件夹显示属性。

### `.gitattributes`
Git属性配置，定义文件的换行符处理、差异比较工具等。

### `logo.png`
项目Logo图片，用于文档和展示。

### `demo.mp4`
演示视频，展示系统运行效果和用户交互流程。

---

**文档版本**: v1.0
