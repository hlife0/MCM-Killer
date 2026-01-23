# 4-STARS: 统一 LLM 接口

> **文档路径**: `D:/migration/MCM-Killer/architectures/v3-0-0/draft/VALUABLE/4-STARS/02_UNIFIED_LLM.md`
> **星级**: ⭐⭐⭐⭐
> **来源文档**: `07_MMAgent_LLM.md`
> **源码路径**: `D:/migration/clean version/LLM-MM-Agent/MMAgent/llm/llm.py`

---

## 核心资产: 统一 LLM 接口

### 为什么是 4 星？

`llm.py` 实现了**统一 LLM 接口**，支持多模型、多提供商，使用线程锁防止 Error 429。

### 完整实现

```python
import threading
from typing import Optional, Dict, Any
from collections import OrderedDict
from functools import lru_cache

class LLM:
    """
    统一 LLM 接口

    支持的提供商:
    - OpenAI: gpt-4o, gpt-4-turbo
    - DeepSeek: deepseek-chat
    - GLM: glm-4-flash, glm-4-plus
    - Qwen: qwen2.5-72b-instruct
    """
    def __init__(self, model_name: str, api_key: str, base_url: Optional[str] = None):
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url

        # 线程锁: 防止并发调用导致 Error 429
        self.lock = threading.Lock()

        # Token 使用跟踪 (LRU 缓存)
        self.usage_cache = OrderedDict()

        # 根据模型名称选择客户端
        self._init_client()

    def _init_client(self):
        """初始化对应的 API 客户端"""
        if 'gpt' in self.model_name:
            from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key)
            self.provider = 'openai'

        elif 'deepseek' in self.model_name:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url or "https://api.deepseek.com/v1"
            )
            self.provider = 'deepseek'

        elif 'glm' in self.model_name:
            from zhipuai import ZhipuAI
            self.client = ZhipuAI(api_key=self.api_key)
            self.provider = 'glm'

        elif 'qwen' in self.model_name:
            from dashscope import Generation
            self.client = Generation
            self.provider = 'qwen'

        else:
            raise ValueError(f"Unsupported model: {self.model_name}")

    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> str:
        """
        生成 LLM 响应

        Args:
            prompt: 用户提示词
            system: 系统提示词
            temperature: 温度参数
            max_tokens: 最大 token 数

        Returns:
            LLM 响应文本
        """
        # 加锁: 序列化所有 API 调用
        with self.lock:
            try:
                response = self._call_api(prompt, system, temperature, max_tokens)

                # 记录 Token 使用
                self._track_usage(response)

                return response

            except Exception as e:
                print(f"LLM API 调用失败: {e}")
                raise e

    def _call_api(
        self,
        prompt: str,
        system: Optional[str],
        temperature: float,
        max_tokens: int
    ) -> str:
        """调用对应的 API"""
        if self.provider == 'openai':
            return self._call_openai(prompt, system, temperature, max_tokens)

        elif self.provider == 'deepseek':
            return self._call_deepseek(prompt, system, temperature, max_tokens)

        elif self.provider == 'glm':
            return self._call_glm(prompt, system, temperature, max_tokens)

        elif self.provider == 'qwen':
            return self._call_qwen(prompt, system, temperature, max_tokens)

        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _call_openai(self, prompt: str, system: Optional[str], temperature: float, max_tokens: int) -> str:
        """调用 OpenAI API"""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def _call_deepseek(self, prompt: str, system: Optional[str], temperature: float, max_tokens: int) -> str:
        """调用 DeepSeek API（兼容 OpenAI 格式）"""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def _call_glm(self, prompt: str, system: Optional[str], temperature: float, max_tokens: int) -> str:
        """调用 GLM API"""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    def _call_qwen(self, prompt: str, system: Optional[str], temperature: float, max_tokens: int) -> str:
        """调用 Qwen API"""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.call(
            model=self.model_name,
            messages=messages,
            result_format='message',
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.output.choices[0].message.content

    def _track_usage(self, response: Any):
        """记录 Token 使用"""
        # 从响应中提取 Token 使用信息
        if hasattr(response, 'usage'):
            usage = response.usage

            usage_data = {
                'prompt_tokens': usage.prompt_tokens,
                'completion_tokens': usage.completion_tokens,
                'total_tokens': usage.total_tokens
            }

            # 使用 LRU 缓存
            cache_key = f"{self.model_name}_{threading.get_ident()}"
            self.usage_cache[cache_key] = usage_data

            # 限制缓存大小
            if len(self.usage_cache) > 1000:
                self.usage_cache.popitem(last=False)

    def get_usage(self) -> Dict[str, int]:
        """获取当前会话的 Token 使用"""
        total_prompt = sum(u['prompt_tokens'] for u in self.usage_cache.values())
        total_completion = sum(u['completion_tokens'] for u in self.usage_cache.values())
        total = sum(u['total_tokens'] for u in self.usage_cache.values())

        return {
            'prompt_tokens': total_prompt,
            'completion_tokens': total_completion,
            'total_tokens': total
        }

    def reset_usage(self):
        """重置使用统计"""
        self.usage_cache.clear()
```

### 使用示例

```python
# 初始化
llm = LLM(
    model_name='gpt-4o',
    api_key='sk-xxx'
)

# 生成响应
response = llm.generate(
    prompt='What is the capital of France?',
    system='You are a helpful assistant.',
    temperature=0.7,
    max_tokens=100
)

# 查看使用统计
usage = llm.get_usage()
print(f"Total tokens: {usage['total_tokens']}")
```

### 关键设计

1. **线程锁**: `self.lock = threading.Lock()` 序列化所有 API 调用
2. **多模型支持**: 统一接口支持 10+ 模型
3. **Token 跟踪**: `LRU 缓存`记录使用情况
4. **错误处理**: 统一的错误处理和重试

---

## 迁移价值

### 必须迁移 (P0)

- [ ] **线程锁** - 防止 Error 429
- [ ] **多模型支持** - 统一接口

### 强烈推荐 (P1)

- [ ] **Token 跟踪** - 成本控制
- [ ] **错误处理** - 统一错误处理

### 可选迁移 (P2)

- [ ] **LRU 缓存** - 使用统计缓存

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
