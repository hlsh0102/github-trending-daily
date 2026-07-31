---
tags:
  - trending
  - article
repo: huggingface/speech-to-speech
date: 2026-07-31
language: Python
stars_total: 9194
stars_today: 628
---
## 项目概述

Speech To Speech 是由 Hugging Face 推出的低延迟、全模块化语音智能体流水线项目。它将完整的语音对话链路抽象为 **VAD（语音活动检测）→ STT（语音转文本）→ LLM（大语言模型）→ TTS（文本转语音）** 四个阶段，并通过一个 **OpenAI Realtime 兼容的 WebSocket API** 对外提供服务。

该项目解决的核心问题是：开发者希望构建语音对话智能体时，不再需要手动拼接多种语音模型和推理服务，也无需依赖封闭的云厂商 API。通过 Speech To Speech，你可以用一套标准化的接口，自由组合任意开源语音模型，并在本地硬件上运行完整链路，实现数据的完全自主可控。该流水线已在生产环境中作为数千台 [Reachy Mini](https://huggingface.co/blog/reachy-mini) 机器人的对话后端稳定运行，证明了其可靠性和实用性。

目标用户包括：语音应用开发者、机器人工程师、本地优先（local-first）技术实践者，以及希望快速原型验证语音对话方案的研究人员。

## 核心功能

- **OpenAI Realtime 兼容接口**：客户端无需修改代码，只需切换 WebSocket 端点，即可从 OpenAI 托管服务无缝迁移到自托管服务，极大降低迁移成本。
- **完全模块化设计**：VAD、STT、LLM、TTS 四个组件均可独立替换。开发者可针对每个环节自由选择最合适的开源模型，例如用更轻量的 VAD 模型降低延迟，或用领域微调后的 ASR 模型提升识别准确率。
- **LLM 插槽兼容 OpenAI 协议**：语言模型环节支持任何遵循 OpenAI Chat Completions 协议的服务，包括云端托管、[HF Inference Providers](https://huggingface.co/inference-providers) 以及本地 vLLM、llama.cpp 服务器。
- **全本地运行能力**：支持构建完全本地、完全开源的语音智能体栈，保障数据隐私并消除 API 调用成本。
- **一键启动体验**：通过 pip 安装后，仅需设置环境变量并执行单条命令，即可启动完整的语音对话服务。
- **生产级稳定性**：已在真实机器人产品中大规模部署，具备处理并发会话和长时间稳定运行的工程能力。

## 技术架构

Speech To Speech 的核心架构思路是“标准协议 + 可插拔组件”。项目没有绑定任何特定模型，而是通过定义清晰的接口边界，让每个环节的模型都可以独立演进和替换。

在链路设计上，VAD 模块负责检测用户语音的起止边界，有效节省后续计算资源；STT 模块将音频流转为文本；LLM 负责语义理解和回复生成；TTS 将文本回复合成语音并回传客户端。整个链路的通信采用 WebSocket 全双工模式，支持流式音频输入和输出，从而保证端到端的低延迟交互体验。

一个重要的架构决策是让 LLM 插槽直接使用 OpenAI 兼容协议。这一设计让项目能够无缝接入生态中大量的推理后端（如 vLLM、llama.cpp 等），同时保持对 OpenAI 官方服务的兼容性，用户可以在云端和本地服务之间灵活切换，而无需改动上层业务代码。

此外，项目采用 Python 实现，依赖环境简单，官方提供 PyPI 包和 Docker 部署方式。模块间的独立性也使得开发者可以针对单个组件进行性能优化或功能扩展，而无需触及流水线的其他部分。

## 安装与使用

### 安装步骤

Speech To Speech 的安装非常直接，可通过 pip 完成：

```bash
pip install speech-to-speech
```

### 最小可用配置

1. 设置你的 OpenAI API 密钥（作为 LLM 后端的默认凭证）：

```bash
export OPENAI_API_KEY=sk-...
```

2. 启动服务：

```bash
speech-to-speech
```

3. 服务启动后，会在本地监听 WebSocket 连接，默认地址为 `ws://localhost:8765/v1/realtime`。

### 示例用法

任何兼容 OpenAI Realtime API 的客户端都可以直接连接。例如，使用官方 OpenAI Python SDK 时，只需指定自定义端点：

```python
from openai import OpenAI

client = OpenAI(
    api_key="dummy",  # 本地服务不需要真实密钥
    base_url="ws://localhost:8765/v1/realtime"
)

# 后续调用方式与使用 OpenAI Realtime API 一致
# ...
```

对于完全本地化的部署，你可以将 LLM 环境变量指向本地运行的 vLLM 或 llama.cpp 服务，并替换 STT/TTS 组件为本地模型，即可得到一个不依赖任何外部 API 的完整语音对话系统。

## 适用场景

- **机器人语音交互**：如 Reachy Mini 等实体机器人需要低延迟、可定制的语音对话能力，项目提供的高效流水线非常适合嵌入机器人操作系统。
- **本地优先的语音助手**：对数据隐私要求严格的企业或组织，可以在内网服务器上部署完全本地的语音智能体，确保敏感语音数据不外流。
- **语音应用快速原型开发**：开发者希望快速验证语音产品 idea 时，无需关心底层模型集成细节，通过标准 API 即可在数分钟内搭建起可交互的语音 agent。
- **研究与教学**：需要对比不同 VAD/STT/TTS 模型组合效果的场景，模块化设计便于进行控制变量实验。

## 项目亮点

- **零迁移成本兼容**：市面上的语音 agent 框架通常需要锁定特定供应商或 SDK，而 Speech To Speech 直接兼容 OpenAI Realtime 协议，使得现有 OpenAI 用户可以实现分钟级迁移。
- **真正的组件可替换性**：很多项目声称模块化，但实际每一层的替换都需要重写接口。本项目通过协议标准化真正做到了“即插即用”，且每个环节都有丰富的开源模型可供选择。
- **生产验证**：不仅有理论设计，还有数千台机器人规模的实战检验，这意味着项目的并发处理、错误恢复、音频流管理等工程细节已经过充分打磨。
- **开源与本地化导向**：在多数厂商推动用户绑定云端服务的背景下，项目坚持开源和本地可运行，让开发者拥有完整的模型主权和数据控制权。

## 相关链接

- [GitHub 仓库](https://github.com/huggingface/speech-to-speech)
- [Reachy Mini 机器人项目博客](https://huggingface.co/blog/reachy-mini)
