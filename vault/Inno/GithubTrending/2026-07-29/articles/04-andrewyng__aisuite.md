---
tags:
  - trending
  - article
repo: andrewyng/aisuite
date: 2026-07-29
language: Python
stars_total: 15738
stars_today: 62
---
## 项目概述

aisuite 是一个轻量级的 Python 库，旨在为开发者提供统一的接口来访问多个生成式 AI 提供商。它解决了当前 AI 开发中常见的痛点：不同模型提供商（如 OpenAI、Anthropic、Google 等）拥有各自独立的 API、参数格式和认证方式，导致开发者需要为每个提供商编写适配代码，切换或组合使用多个模型时变得异常繁琐。

该库面向以下几类目标用户：
- 需要在项目中集成多个 LLM 提供商的 AI 应用开发者
- 希望快速原型验证不同模型效果的研究人员
- 构建需要多模型协同工作的智能体应用的工程师
- 希望减少对单一 AI 服务商依赖的产品团队

aisuite 的核心价值在于“一次学习，多处使用”——开发者只需掌握一套 API 语法，即可无缝调用数十种主流大语言模型。

## 核心功能

- **统一的 Chat Completions API**：提供与 OpenAI SDK 高度兼容的接口，支持所有主流 LLM 提供商。开发者只需更换模型名称和 API 密钥，即可在不同模型间自由切换，无需修改业务逻辑代码。

- **智能体 API 与工具系统**：在基础 Chat Completions 之上，提供了智能体（Agent）API，支持函数调用、工具集成和工具包（Toolkits），便于构建能自主执行任务的 AI 智能体。

- **多提供商即插即用**：内置对 OpenAI、Anthropic、Google、Azure、AWS Bedrock、Groq、Mistral、Together AI、Ollama 等十余家提供商的支持。每个提供商即一个独立的 Python 包，按需安装，不增加冗余依赖。

- **OpenWorker 桌面应用支持**： aisuite 也是 Andrew Ng 团队推出的桌面 AI 助手 OpenWorker 的技术底座，支持对话、深度研究、文件操作、连接 Slack/Email、生成文档报表、定时自动化等能力，支持本地运行和第三方 API 密钥。

## 技术架构

aisuite 采用分层架构设计，分为两个核心层次：

**第一层：统一 Chat Completions API 层**
这一层负责与不同提供商的后端交互。它通过适配器模式（Adapter Pattern）将各提供商的差异化请求参数、认证机制和响应格式进行标准化。核心设计思路是保持与 OpenAI SDK 的接口语义兼容，这意味着任何熟悉 OpenAI API 的开发者无需学习即可上手使用。该层通过模型名称中的前缀自动识别目标提供商（如 `openai:`、`anthropic:`、`google:`），并调用对应的适配器进行请求转换。

**第二层：智能体 API 层**
在基础 API 之上，该层提供了更高层次的抽象——智能体（Agent）。智能体可以完成多轮对话、调用工具、处理工具包等任务。工具包是一组预定义的工具集合，例如文件操作工具包、搜索工具包等。这一层利用了 LLM 的函数调用能力，让智能体能够根据用户指令自主决定调用哪些工具。

架构上，aisuite 采用了最小依赖原则：核心库仅包含必要的适配逻辑，每个提供商的客户端实现作为独立的可选依赖。这种设计使得项目体积轻量，同时允许开发者根据实际需要使用特定的提供商。

## 安装与使用

安装 aisuite 非常简便。首先通过 pip 安装核心库：

```bash
pip install aisuite
```

然后根据需要安装一个或多个提供商的依赖。例如，使用 OpenAI 和 Anthropic：

```bash
pip install 'aisuite[openai,anthropic]'  # 安装 OpenAI 和 Anthropic 支持
```

其他可选提供商包括：`google`、`azure`、`aws`（Bedrock）、`groq`、`mistral`、`together`、`ollama` 等。

以下是一个最小可用示例，展示如何调用不同模型的 Chat Completions：

```python
import aisuite as ai

# 创建客户端
client = ai.Client()

# 使用 OpenAI GPT-4
messages = [{"role": "user", "content": "请用中文写一首短诗"}]
response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages
)
print(response.choices[0].message.content)

# 切换为 Anthropic Claude（只需更换模型名称和 API 密钥）
response = client.chat.completions.create(
    model="anthropic:claude-3-5-sonnet-20240620",
    messages=messages
)
print(response.choices[0].message.content)
```

注意：需要提前设置相应提供商的 API 密钥为环境变量（如 `OPENAI_API_KEY`、`ANTHROPIC_API_KEY`）。

## 适用场景

- **多模型评估与选型**：在 AI 应用开发初期，团队需要对比不同 LLM 在具体任务上的表现。aisuite 允许开发者用统一代码快速切换模型，进行 A/B 测试或成本效益分析。

- **构建弹性 AI 管道**：在面向用户的应用中，当主模型出现故障或配额耗尽时，可以平滑回退到备选模型。aisuite 的接口一致性让这种故障切换逻辑实现变得简单。

- **智能体任务自动化**：结合 OpenWorker 桌面应用，开发者可以构建能够读取本地文件、操作应用程序、连接企业工具（如 Slack、Outlook）的 AI 智能体，执行复杂的办公自动化任务。

- **教育与研究**：对于教学或学术研究，aisuite 提供了一个中立的实验平台，研究者可以控制变量，公平比较不同模型的能力，而不受 API 差异的干扰。

## 项目亮点

aisuite 与同类项目相比的差异化优势在于：

1. **原作者背书与活跃度**：由 Andrew Ng 团队出品，GitHub 上获得超过 15000 颗星，社区活跃度高，代码质量可靠。

2. **极低的迁移成本**：API 设计直接对标 OpenAI SDK，现有 Open AI 用户可以几乎零成本迁移，这是许多其他统一接口库难以做到的。

3. **智能体层的一体化**：不仅提供基础的 Chat API 统一，还集成了智能体框架和工具系统，让设计复杂 AI 应用时不必再引入第三方 Agent 框架。

4. **OpenWorker 桌面应用闭环**：aisuite 不仅是库，还支撑一个可直接使用的桌面产品，从开发框架到终端用户应用形成完整闭环，这在开源 LLM 工具中较为罕见。

5. **轻量与模块化**：按需安装不同提供商的实现，不会因为支持多模型而带来不必要的依赖膨胀。

## 相关链接

- [GitHub 仓库](https://github.com/andrewyng/aisuite)
- [OpenWorker 桌面应用仓库](https://github.com/andrewyng/openworker)
- [OpenWorker macOS 下载](https://github.com/andrewyng/openworker/releases/latest/download/OpenWorker-macos-arm64.dmg)
- [OpenWorker Windows 下载](https://github.com/andrewyng/openworker/releases/latest/download/OpenWorker-windows-setup.exe)
