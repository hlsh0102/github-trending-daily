---
tags:
  - trending
  - article
repo: ggml-org/llama.cpp
date: 2026-06-08
language: C++
stars_total: 115458
stars_today: 158
---
## 项目概述

llama.cpp 是一个使用 C/C++ 编写的高性能大语言模型推理引擎，由 Georgi Gerganov 创建并托管于 ggml-org 组织下。该项目旨在让 LLaMA 系列及其他主流大语言模型能够在消费级硬件上高效运行，无需昂贵的专业 GPU 或大规模集群。它解决了大模型部署中常见的资源门槛过高问题，使开发者、研究人员和爱好者可以在普通 CPU 甚至树莓派、手机等低功耗设备上运行对话、文本生成等任务。目标用户包括希望本地私有化部署 LLM 的开发者、关注边缘计算的研究者、以及需要低成本推理方案的企业。

## 核心功能

- **跨平台 CPU 推理**：基于高度优化的 ggml 张量库，利用 AVX、NEON、Metal 等 SIMD 指令集，在无 GPU 环境下也能获得可用的推理速度。
- **量化支持**：内置多种量化格式（如 Q4_0、Q4_K_M、Q5_K_M、Q8_0 等），支持 2-bit 到 8-bit 非对称 quantization，显存占用可降低至 FP16 的 1/4 甚至更低。
- **多模型兼容性**：不仅支持原始的 LLaMA 模型，还兼容 Mistral、Falcon、Gemma、Qwen、DeepSeek、Phi、Stable LM 等主流架构，以及 GPT-OSS 等新兴模型。
- **内置 HTTP 服务器**：提供 `llama-server` 子命令，可快速启动 REST API 服务，支持 OpenAI 兼容接口、连续批处理、并发请求、上下文缓存等生产级特性。
- **交互与工具集成**：内置交互式对话模式、文本补全、嵌入生成、token/概率感知接口，并支持与 Hugging Face 缓存互通、llamafile 等打包工具集成。
- **持续更新的生态系统**：活跃的社区贡献，支持 Docker 部署、Windows 包管理器安装，以及官方 WebUI 指南，降低入门门槛。

## 技术架构

llama.cpp 采用纯 C/C++ 实现，核心依赖 ggml 张量计算库。ggml 针对 CPU 和 GPU 的异构计算场景做了大量手写优化：对于 x86 平台充分利用 AVX2/AVX512 加 AMX 指令，对 ARM 架构则使用 NEON/ SVE，而对 Apple Silicon 则直接调用 Metal API 利用统一内存架构。整个推理管线包括 tokenizer（基于 BPE 或 SentencePiece）、模型加载、KV 缓存管理、前向传播和采样后处理，全部在本地完成，无需依赖 Python 运行时或 CUDA 生态。设计上强调零外部依赖，一个二进制文件即可完成从模型下载到推理的全流程，极大降低了部署复杂度。近期还加入了与 NVIDIA 合作的 gpt-oss 模型原生 MXFP4 格式支持，展现了与硬件厂商深度协作的开放路线。

## 安装与使用

### 安装

从源码编译（推荐用于最新特性）：
```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
make -j4  # Linux/Mac
# 或使用 CMake: cmake -B build && cmake --build build --config Release
```

Windows 用户也可直接通过 WinGet 安装：
```powershell
winget install llama.cpp
```

或使用 Docker：
```bash
docker pull ghcr.io/ggml-org/llama.cpp:full
```

### 最小可用示例

假设已有 GGUF 格式模型文件（如 `models/mistral-7b-instruct-v0.2.Q4_K_M.gguf`）：

1. 下载模型（若未下载）：
   ```bash
   # HuggingFace 自动下载（推荐）
   ./llama-cli -hf "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
   ```

2. 运行交互式对话：
   ```bash
   ./llama-cli -m models/mistral-7b-instruct-v0.2.Q4_K_M.gguf -p "你好，请介绍一下自己" -n 256
   ```

3. 启动 HTTP 服务（默认 8080 端口）：
   ```bash
   ./llama-server -m models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
   # 然后访问 http://localhost:8080 使用 WebUI
   ```

## 适用场景

- **本地私有化部署**：企业或个人需要将敏感数据留在内部，不希望调用云 API，可在普通 PC 或服务器上部署替代 ChatGPT 的完全离线对话服务。
- **边缘设备推理**：在树莓派 5、Jetson Orin、MacBook Air 等低功耗设备上运行轻量量化模型（如 Gemma-2B、Phi-3-mini），实现现场文本生成、摘要、分类等任务。
- **研究与模型对比**：研究人员快速测试不同量化方案对模型质量的影响，或对比多种架构（LLaMA vs Mistral vs Gemma）在同一硬件上的性能差异。
- **嵌入式与物联网**：经过深度剪枝和 2-3bit 量化的模型，可在 256MB RAM 的单板电脑上运行基础 NLP 任务，如意图识别、简单问答。

## 项目亮点

与其他 LLM 推理方案（如 Ollama、vLLM、text-generation-webui 等）相比，llama.cpp 的核心差异化优势在于：

1. **极致的 CPU 推理性能**：ggml 的手工汇编优化使其在同样硬件上比使用 llama-cpp-python 的 Python 方案快 2-5 倍，甚至接近某些未优化的 GPU 推理。
2. **零 Python 依赖**：完全 C/C++ 实现，避免了 Python 生态的版本冲突和依赖问题，一个二进制文件即可运行，非常适合容器化或弱网环境部署。
3. **原生低内存占用**：量化后 7B 模型仅需 4-6GB 内存即可运行，而 70B 模型在 8 位量化下也只需约 48GB，远低于原生 FP16 的 140GB。
4. **社区驱动的持续迭代**：拥有超过 11 万 GitHub Stars 和极其活跃的 Issues/Pull Requests 社区，新模型发布后数天内就能得到支持，且开发者会及时合并上游进步（如 Flash Attention、RoPE scaling 等）。
5. **与硬件厂商深度合作**：与 NVIDIA 合作的原生 MXFP4 支持、与 Apple 的 Metal 深度集成，展示了非封闭生态下硬件优化的典型路径。

## 相关链接

- [GitHub 仓库](https://github.com/ggml-org/llama.cpp)
- [官方讨论与指南](https://github.com/ggml-org/llama.cpp/discussions)
- [ggml 底层库](https://github.com/ggml-org/ggml)
