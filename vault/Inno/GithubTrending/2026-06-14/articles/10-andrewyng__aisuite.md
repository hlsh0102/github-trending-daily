---
tags:
  - trending
  - article
repo: andrewyng/aisuite
date: 2026-06-14
language: Python
stars_total: 14193
stars_today: 127
---
## 项目概述

aisuite 是一个轻量级的 Python 库，旨在为开发者提供统一的接口，以接入多个生成式 AI 提供商。它解决了在使用不同 AI 模型（如 OpenAI、Anthropic、Google 等）时需要分别编写适配代码的痛点，让开发者只需学习一套 API 就能切换或组合多种底层模型。目标用户包括需要快速原型开发、希望降低供应商锁定风险、或想灵活选择最合适模型的 AI 应用开发者。

aisuite 分为两个层次：底层是统一的 **Chat Completions API**，用于处理基础的对话生成；上层是 **Agents API**，支持工具（tools）和工具包（toolkits），用于构建更智能的 AI 代理（agent）。该项目还包含一个基于 aisuite 构建的桌面 AI 代理应用 **OpenCoworker**，可以作为参考实现。

## 核心功能

- **统一 Chat Completions API**：通过一致的接口调用 OpenAI、Anthropic、Google 等多家模型的对话生成能力，无需学习每个供应商的特定 API。
- **Agents API 与工具支持**：在统一 API 之上提供构建 AI 代理的框架，支持定义和使用自定义工具（如文件读写、消息发送）以及工具包（如 Slack、Email 集成），让模型能执行实际任务。
- **多提供商无缝切换**：只需更改模型名称字符串（如 `openai/gpt-4`、`anthropic/claude-3`、`google/gemini-pro`），即可在代码中切换不同的底层模型，方便进行模型对比或混合使用。
- **本地运行支持**：支持通过 Ollama 运行完全本地的模型，无需联网或支付 API 费用，数据完全保留在本地机器上。
- **OpenCoworker 桌面代理**：附带一个功能完整的桌面 AI 代理应用，能聊天、深度研究、执行计算机任务（如读文件、发消息、生成报告），并支持定时自动化（如每日新闻摘要）。
- **开源参考实现**：OpenCoworker 的完整源代码位于仓库的 `platform/` 目录下，可以作为开发者构建自定义 AI 代理的起点和参考。

## 技术架构

aisuite 的核心设计理念是 **简单与统一**。底层使用一个轻量的抽象层，将不同提供商的 Chat Completions API 映射为统一的 Python 接口。开发者只需指定模型名称（如 `openai/gpt-4`），库内部会负责进行认证、请求格式转换和响应解析。

Agents API 构建在统一 API 之上，通过执行循环（run loop）协调模型与外部工具的交互。模型生成工具调用（tool call）后，代理会执行对应的函数，并将结果返回给模型以生成最终响应。这种设计类似于 ReAct（Reasoning + Acting）模式，但封装为简洁的 API。

技术栈方面，aisuite 基于 Python 语言，依赖 `pydantic` 进行数据验证，并使用 `httpx`（或 `requests`）进行 HTTP 通信。OpenCoworker 桌面应用则使用 Electron 或类似框架（具体技术待确认）构建用户界面，通过本地进程调用 aisuite 库实现 AI 功能。

架构上的一个显著特点是 **无中心依赖**：所有模型调用都是直接发送到对应提供商的 API 端点，不经过中间服务器，这有利于隐私保护和低延迟。对于本地 Ollama 部署，网络请求仅在本地回环地址进行。

## 安装与使用

安装 aisuite 非常简单，通过 pip 即可完成：

```bash
pip install aisuite
```

如果需要某个特定提供商的额外依赖（如 OpenAI），可以安装对应的插件：

```bash
pip install "aisuite[openai]"
```

一个最小可用的 Chat Completions 示例：

```python
import aisuite as ai

client = ai.Client()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

response = client.chat.completions.create(
    model="openai/gpt-4",
    messages=messages,
)

print(response.choices[0].message.content)
```

要使用 OpenAI 模型，需要设置环境变量 `OPENAI_API_KEY`；同理，使用 Anthropic 需设置 `ANTHROPIC_API_KEY`，Google 需设置 `GOOGLE_API_KEY`。

使用本地 Ollama 模型则更简单，无需 API 密钥，只需确保 Ollama 服务运行中：

```python
response = client.chat.completions.create(
    model="ollama/llama3",
    messages=messages,
)
```

对于构建代理（OpenCoworker 或自定义代理），可以参考仓库中 `platform/` 目录下的源码，或查阅 `docs/opencoworker-quickstart.md` 快速入门指南。

## 适用场景

- **多模型快速对比与迁移**：在开发阶段，需要快速对比不同 LLM 的输出质量或价格；或在生产环境中需要从某个模型迁移到另一个时，只需修改一行代码即可完成切换。
- **本地优先的 AI 应用**：在数据隐私敏感的场景中（如处理公司内部文件或个人健康数据），使用 aisuite 搭配 Ollama 运行本地模型，确保数据不离开用户设备。
- **桌面 AI 助手与自动化**：使用 OpenCoworker 或基于 aisuite Agents API 构建的桌面代理，执行日常任务自动化，如阅读邮件、整理文件、生成报告或定时抓取新闻。
- **快速原型与教育演示**：希望快速验证一个 AI 应用想法，而不想花时间对接不同提供商的 SDK；或者在教学场景中演示不同模型的差异。

## 项目亮点

aisuite 与同类库（如 LangChain、Haystack）相比，最大的差异化优势在于 **极简设计**。它不强行绑定复杂的链式调用、记忆管理、向量存储等组件，而是专注于提供一个最薄、最干净的统一 API 层。这使得：

1. **学习成本极低**：任何熟悉 OpenAI API 的开发者都可以立即上手，因为接口设计高度相似。
2. **高度透明**：没有黑盒魔法，所有请求和响应的结构清晰可见，便于调试和自定义。
3. **轻量无负担**：依赖树极小，不会引入大量你不需要的第三方库，对资源受限的环境（如树莓派或低配笔记本）友好。
4. **OpenCoworker 作为活文档**：桌面应用不仅是产品，更是展示了如何基于 aisuite 构建真实 AI 代理的完整示例，这比单独阅读文档更具参考价值。

## 相关链接

- [GitHub 仓库](https://github.com/andrewyng/aisuite)
- [OpenCoworker 快速入门指南](https://github.com/andrewyng/aisuite/blob/main/docs/opencoworker-quickstart.md)
- [PyPI 包页面](https://pypi.org/project/aisuite/)
