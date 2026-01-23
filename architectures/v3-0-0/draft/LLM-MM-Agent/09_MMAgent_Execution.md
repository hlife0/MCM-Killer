# MMAgent: Execution 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/09_MMAgent_Execution.md`
> **重要程度**: ⭐⭐⭐ 执行模块
> **迁移价值**: **低** - 可由沙箱替代

本目录（`MMAgent/execution/`）包含代码执行相关模块，提供安全的代码执行环境。

---

## 核心文件

### `kernel_client.py` ⭐⭐⭐
**内核客户端**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/execution/kernel_client.py`。管理代码执行的内核客户端，提供超时控制、输出捕获等功能。

**功能**：
- 在隔离环境中执行代码
- 超时控制（默认 300 秒）
- 捕获标准输出和错误输出
- 异常处理和报告

**迁移价值**：沙箱执行模式是安全运行生成代码的标准做法。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
