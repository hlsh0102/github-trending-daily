---
tags:
  - trending
  - article
repo: NVIDIA/cosmos
date: 2026-06-05
language: Jupyter Notebook
stars_total: 9136
stars_today: 133
---
## 项目概述

NVIDIA Cosmos 是一个面向物理 AI 的开源平台，提供世界模型、数据集和工具，旨在帮助开发者构建能够理解和交互物理世界的智能系统。无论是机器人、自动驾驶车辆，还是智能基础设施，Cosmos 都致力于降低物理 AI 的开发门槛，让开发者能够更高效地训练和部署具备空间理解与物理常识的模型。

该项目的核心理念是“世界模型”——即能够预测物理世界状态演变的 AI 系统。通过 Cosmos，开发者可以获取预训练的世界模型、大规模的物理场景数据集，以及用于模型微调和部署的工具链，从而加速从感知到决策的完整 AI 流程。

## 核心功能

- **世界模型生成器（Generator）**：基于文本或图像输入，生成符合物理规律的视频序列，用于模拟机器人操作、车辆行驶等场景。
- **世界模型推理器（Reasoner）**：接收视频或图像序列，输出对物理状态、物体运动轨迹、场景布局的理解，支持事件预测和因果推理。
- **多模态输入支持**：支持文本、图像、视频等多种输入形式，提供灵活的交互方式。
- **模型族覆盖**：提供不同规模和能力的模型变体，从轻量级到高精度版本，适应不同计算资源场景。
- **多种推理后端**：支持通过 Diffusers、vLLM-Omni、Transformers、NIM 等框架运行模型，便于集成到现有技术栈。
- **预训练数据集**：附带大规模物理场景数据集，涵盖机器人操控、自动驾驶、环境交互等典型场景。

## 技术架构

NVIDIA Cosmos 的技术架构围绕“世界模型”这一核心概念构建，主要分为生成器和推理器两大模型类型。

生成器采用扩散模型架构，通过逐步去噪的过程从随机噪声中恢复出符合物理规律的视频序列。其设计借鉴了文本到图像扩散模型的经验，但针对视频生成中的时序一致性进行了专门的优化，能够保持帧与帧之间的物理运动连贯性。

推理器则基于 Transformer 架构，能够对输入的视觉序列进行深度的物理状态分析。它不同于普通的图像分类模型，而是能够理解物体间的空间关系、运动趋势以及潜在的物理约束（如重力、碰撞等）。模型支持因果推理，可以从观察到的状态推断出之前发生的事件或预测后续的结果。

整个平台采用模块化设计，模型训练与推理解耦，预训练模型可以通过标准化接口接入不同的推理框架（Diffusers、vLLM-Omni、Transformers 等）。这种设计使得 Cosmos 既可以作为独立的推理服务运行，也可以嵌入到更大的 AI 系统（如机器人行为规划、自动驾驶决策链）中作为子模块使用。

## 安装与使用

Cosmos 的安装基于常见的深度学习环境，建议使用 CUDA 12.x 及以上版本。以下以生成器（Generator）为例说明基本使用方式。

**环境准备**：
```bash
pip install diffusers transformers torch accelerate
```

**使用 Generator with Diffusers 生成视频**：
```python
from diffusers import CosmosDiffusionPipeline
import torch

pipe = CosmosDiffusionPipeline.from_pretrained(
    "nvidia/cosmos-generator",
    torch_dtype=torch.bfloat16,
    variant="fp16"
)
pipe.to("cuda")

# 从文本生成视频
prompt = "A robot arm picking up a red cube from a table"
video = pipe(prompt, num_frames=32, height=512, width=512).frames[0]

# 保存或使用生成的视频
video.save("output.mp4")
```

**使用 Reasoner with Transformers 进行物理推理**：
```python
from transformers import AutoModelForCausalLM, AutoProcessor

model = AutoModelForCausalLM.from_pretrained(
    "nvidia/cosmos-reasoner",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained("nvidia/cosmos-reasoner")

# 输入视频帧，获取物理状态描述
inputs = processor(video_frames, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs)
description = processor.decode(outputs[0], skip_special_tokens=True)
print(description)  # 输出如 "The robot arm is moving towards the cube at 30 degrees angle"
```

## 适用场景

- **机器人仿真与训练**：在部署到真实机器人之前，使用 Cosmos 生成大量物理场景数据，训练机器人的抓取、移动、操作等技能，减少真实环境测试成本。
- **自动驾驶决策验证**：构建自动驾驶系统时，利用世界模型预测不同驾驶策略下的场景演变，验证决策的安全性和合理性，覆盖 corner case。
- **智能基础设施监控**：通过分析监控视频中的物理运动（如人流、车辆轨迹），预测拥堵、碰撞等事件，辅助运维决策。
- **物理 AI 研究与教育**：作为物理 AI 研究的基础平台，用于验证新的世界模型架构、评估物理推理能力，或作为教学工具展示物理智能的实现原理。

## 项目亮点

- **开源开放**：模型权重、数据集、工具链均开源，开发者可自由使用、修改和部署，避免了商业平台的黑盒限制。
- **物理世界理解深度**：不同于普通的视频生成或分类模型，Cosmos 专注于理解物理规律（运动、力学、物体交互），输出具有因果意义的结果。
- **灵活多样的部署方式**：支持 Diffusers、vLLM-Omni、Transformers、NIM 等多种推理后端，适应从科研实验到工业部署的不同需求。
- **与 NVIDIA 生态深度集成**：原生支持 CUDA 加速、TensorRT 优化，并可无缝对接 NVIDIA 的物理仿真平台（如 Isaac Sim），构建完整的物理 AI 开发闭环。

## 相关链接

- [GitHub 仓库](https://github.com/NVIDIA/cosmos)
- [官方网站](https://www.nvidia.com/en-us/ai/cosmos/)
- [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework)
