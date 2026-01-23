# MMAgent: LLM 接口

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/07_MMAgent_LLM.md`
> **重要程度**: ⭐⭐ 统一 LLM 调用
> **迁移价值**: **极高** - 统一接口模式强烈推荐

本目录（`MMAgent/llm/`）包含 LLM-MM-Agent 系统的统一 LLM 接口，支持多种 LLM 提供商（OpenAI、DeepSeek、GLM、Qwen）。实现了线程锁防止 API 速率限制（Error 429），提供 Token 使用跟踪和 LRU 缓存驱逐策略。

---

## 核心文件

### `llm.py` ⭐⭐
**统一 LLM 接口**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/llm/llm.py`。

**核心功能**：

1. **多模型支持**：
   - OpenAI: `gpt-4o`, `gpt-4`
   - DeepSeek: `deepseek-chat`, `deepseek-reasoner`
   - GLM (Zhipu AI): `glm-4-plus`, `glm-4-flash`, `glm-4.7`
   - Qwen: `qwen2.5-72b-instruct`

2. **线程锁**：
   - 所有 API 调用通过 `threading.Lock()` 串行化
   - 防止 Error 429 速率限制
   - 即使并发调用也会排队执行

3. **Token 使用跟踪**：
   - 记录每次调用的 token 使用量
   - LRU 缓存驱逐策略（限制缓存大小）
   - 支持使用量和成本统计

4. **温度设置**：
   - 默认温度 0.7
   - 平衡创造性和可靠性

**关键代码**：
```python
class LLM:
    def __init__(self, model_name, api_key, base_url=None):
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = get_model_base_url(model_name, base_url)
        self.lock = threading.Lock()  # 线程锁
        self.usage_cache = LRUCache(maxsize=1000)  # Token 使用缓存

    def generate(self, prompt, system=None, temperature=0.7):
        with self.lock:  # 串行化所有 API 调用
            # 调用 LLM API
            # 记录 token 使用
            # 返回结果
```

**支持的模型**：

| 模型系列 | 模型名称 | API Base URL |
|---------|----------|-------------|
| OpenAI | gpt-4o, gpt-4 | https://api.openai.com/v1 |
| DeepSeek | deepseek-chat, deepseek-reasoner | https://api.deepseek.com |
| GLM | glm-4-plus, glm-4-flash, glm-4.7 | https://open.bigmodel.cn/api/paas/v4 |
| Qwen | qwen2.5-72b-instruct | https://dashscope.aliyuncs.com/compatible-mode/v1 |

**API 环境变量**：
- `OPENAI_API_KEY` - OpenAI API 密钥
- `DEEPSEEK_API_KEY` - DeepSeek API 密钥
- `ZHIPU_API_KEY` - GLM API 密钥（格式：id.secret）
- `DASHSCOPE_API_KEY` - Qwen API 密钥

---

## 迁移价值

### 极高（强烈推荐迁移）

1. **统一接口模式**：
   - 单一接口支持多个 LLM 提供商
   - 便于切换和比较不同模型
   - 降低供应商锁定风险

2. **线程锁机制**：
   - 防止 API 速率限制
   - 简单有效的设计模式
   - 适用于任何需要 API 调用的系统

3. **Token 使用跟踪**：
   - 成本控制和优化
   - LRU 缓存策略

### 高（推荐迁移）

4. **Base URL 自动检测**：
   - 根据模型名称自动选择 API 端点
   - 简化配置

5. **温度控制**：
   - 平衡创造性和可靠性

---

## 关键设计模式

### 1. 策略模式（Strategy Pattern）

不同模型使用不同的 API 格式和认证方式，LLM 类封装这些差异。

### 2. 单例模式（Singleton Pattern）

线程锁确保所有 LLM 调用串行化。

### 3. LRU 缓存模式

Token 使用记录采用 LRU 缓存，限制内存使用。

---

## 与其他模块的集成

### 被调用方

- `agent/` - 所有 Agent 都通过 LLM 类调用 LLM
- `utils/` - 各种工具模块通过 LLM 类调用 LLM

### 调用方

- `prompt/template.py` - 提供提示词模板
- `HMML/` - 提供知识库内容

---

## 使用示例

```python
from llm.llm import LLM

# 初始化 LLM
llm = LLM(
    model_name="gpt-4o",
    api_key="sk-...",
    base_url=None  # 自动检测
)

# 生成文本
result = llm.generate(
    prompt="What is mathematical modeling?",
    system="You are a helpful assistant.",
    temperature=0.7
)

# 检查 token 使用
usage = llm.get_usage()
print(f"Total tokens: {usage['total_tokens']}")
```

---

## 关键发现

1. **线程锁是防止 Error 429 的关键**：所有 API 调用必须串行化
2. **Token 跟踪对成本控制重要**：LRU 缓存防止内存爆炸
3. **Base URL 自动检测简化配置**：用户只需提供模型名称
4. **统一接口支持供应商切换**：降低供应商锁定风险

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**支持模型**: 10+ 模型
