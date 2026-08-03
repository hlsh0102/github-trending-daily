---
tags:
  - trending
  - article
repo: lyogavin/airllm
date: 2026-08-03
language: Jupyter Notebook
stars_total: 25907
stars_today: 819
---
## 项目概述

AirLLM 是一个旨在彻底改变大语言模型（LLM）推理内存瓶颈的开源项目。传统上，运行 70B 级别的模型通常需要多张高端 GPU（如 A100/H100）才能完成推理，这极大地限制了个人开发者和小型团队对前沿模型的访问。AirLLM 通过创新的分块推理和优化调度技术，宣称可以在**单张 4GB 显存的 GPU** 上运行 70B 模型，并且无需对模型进行量化、剪枝或蒸馏操作。

该项目由中国开发者 lyogavin 发起，在 GitHub 上已获得超过 25,000 颗星，是目前社区中最受欢迎的轻量化 LLM 推理方案之一。其核心目标用户包括：资源受限的独立开发者、希望在消费级硬件上体验大模型能力的 AI 爱好者、以及对数据隐私敏感并希望本地部署大型模型的机构。

## 核心功能

- **单卡运行超大规模模型**：支持在单张 4GB GPU 上推理多达 400B 参数的 Llama 3.1，在约 12GB 显存上运行 DeepSeek-V3（671B），甚至可以在不足 4GB 的显存下运行近期发布的稀疏 MoE 模型 Kimi K3（2.8T）。
- **完全保真推理**：不需要对模型进行 4-bit 或 8-bit 量化、无需稀疏化剪枝或其他有损压缩操作，生成的 token 结果与全精度模型一致。
- **稀疏 MoE 流式调度**：针对混合专家（Mixture of Experts）模型结构进行优化，通过逐专家（Expert）而非逐层（Layer）的流式加载机制，极大减少中间激活的驻留内存。
- **极其简单的 API 接口**：与 HuggingFace Transformers 兼容，通过类似 `AutoModelForCausalLM` 的调用方式即可完成模型加载与生成。
- **跨平台支持**：不仅支持 Linux 下的 NVIDIA GPU，还提供了 macOS 的 MPS 后端支持，让 Apple Silicon 用户也能运行百亿级模型。
- **零配置快速启动**：安装即用，自动处理缓存调度与内存映射，无需手动调整复杂的推理参数。

## 技术架构

AirLLM 的技术核心建立在两个设计理念之上：**层级流式重组** 与 **稀疏专家路由**。

对于稠密模型（如 Llama 3.1 70B），AirLLM 借鉴了操作系统层面的“局部性”原理，重构了 Transformer 的前向传播过程。它不再同时将整个模型权重载入显存，而是将计算图按 Transformer 层（或更细粒度）进行切分。对于每一个微批次的输入数据，系统动态地执行以下循环：将权重段从主存（CPU RAM）或磁盘加载至 GPU 显存，执行计算，输出中间结果到主存，随后立即释放显存并加载下一段权重。这种基于块感知的重计算机制，保证了在整个推理过程中，显存峰值仅需容纳单个层权重的规模，从而大幅降低硬件门槛。

对于稀疏 MoE 模型（如 Mixtral、DeepSeek-V3、Kimi K3），AirLLM 采用了一种更激进的设计：**候选专家预取**。在给定输入 token 时，门控网络只激活全部专家中的极少数（通常为前 1-2 个）。AirLLM 通过提前解析路由权重，仅将被激活的专家参数加载入显存，并缓存常驻的共享注意力层。这种策略使得 2.8T 权重的模型在物理上拥有极低的显存足迹，因为每一刻计算所需的权重仅仅是一个很小的子集。

项目底层主要基于 PyTorch 实现了自定义的 `LowMemoryLinear` 和 `Sequential` 替换层，通过 CUDA 流和异步 prefetch 技术隐藏 PCIe 传输延迟，同时利用免拷贝内存映射技术减少页缓存开销。

## 安装与使用

AirLLM 的安装非常便捷，可通过 PyPI 直接获取。推荐在 Python 3.8 及更高版本的环境中使用。

**安装步骤**：

```bash
pip install airllm
```

**最小可用示例**（以运行 70B 模型为例）：

```python
from airllm import AutoModelForCausalLM, AutoTokenizer

# 仅需替换推理模型类，其余加载方式与 HF 保持一致
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-chat-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-chat-hf")

input_text = "Explain the theory of relativity in simple terms."
inputs = tokenizer(input_text, return_tensors="pt")

# 推理过程与常规 PyTorch 无异
with torch.no_grad():
    output = model.generate(inputs.input_ids, max_new_tokens=100)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

**注意事项**：

- 首次运行时需要将模型权重下载至本地或 HuggingFace 缓存目录。
- 在 MacOS 上，需通过 `USE_MPS=1` 环境变量启用 MPS 后端以加速推理。
- 建议合理设置 `--max_length` 字段以控制 KV Cache 的显存占用。

## 适用场景

- **个人本地 AI 工作站**：使用消费级显卡（如 NVIDIA RTX 3050 或 4060）即可运行具有完整能力的 70B 模型，满足代码生成、文本总结和复杂推理的研究需求，避免云端 API 的高昂费用与数据外泄风险。
- **边缘计算与隐私保护**：在医疗、金融和法律领域，数据必须保留在本地。AirLLM 允许在无联网的独立机器上运行万亿参数级别的诊断或合规审阅模型，确保敏感信息不外传。
- **MoE 架构模型的研究与验证**：研究者无需申请大规模 GPU 集群资源，即可在实验室的普通工作站上对 DeepSeek-V3、Kimi K3 等稀疏模型的输出质量、路由机制进行离线测试与分析。

## 项目亮点

与 llama.cpp、ExLlama 或 vLLM 等主流推理框架相比，AirLLM 具有三个显著的差异化优势。**其一是零性能损失**：它不依赖任何量化技术，解决了低比特量化在复杂指令遵循任务中的精度回退问题。**其二是架构通用性**：不仅支持 Llama 和 Mistral 等常见架构，更是迄今为止公开方案中首个能将 2.8T 参数稀疏模型（Kimi K3）跑在单卡上的项目，这一成就源于其对 MoE 路由的深度系统级优化。**其三是易用性与社区生态**：仅需替换一行导入语句即可无缝从标准的 Transformers 流程切换，并且提供了丰富的示例 Notebook 与 Discord 社区支持。

## 相关链接

- [GitHub 仓库](https://github.com/lyogavin/airllm)
- [PyPI 项目页面](https://pypi.org/project/airllm/)
- [项目博客（含技术细节）](https://gavinliblog.com)
