---
tags:
  - trending
  - article
repo: NVIDIA/cosmos
date: 2026-06-06
language: Jupyter Notebook
stars_total: 9473
stars_today: 479
---
## 项目概述

NVIDIA Cosmos 是一个开源的物理世界模型平台，集成了预训练模型、高质量数据集和开发者工具，旨在帮助开发者构建面向机器人、自动驾驶车辆、智能基础设施等领域的物理 AI 系统。该项目由 NVIDIA 发布，解决了传统 AI 训练中真实世界数据获取成本高、物理理解能力不足等核心问题，目标用户包括机器人研究人员、自动驾驶工程师、计算机视觉开发者以及任何希望在物理世界中部署 AI 系统的工程团队。

Cosmos 的核心价值在于它提供了一套开箱即用的能力——开发者无需从头训练物理世界模型，即可利用预训练模型进行视频生成、场景推理、轨迹预测等任务，从而大幅加速物理 AI 的研发周期。

## 核心功能

- **视频生成与预测**：基于文字或图像输入，生成符合物理规律的视频内容，支持在受限/非受限环境下的场景模拟。
- **物理世界推理**：对输入的视频或图像序列进行理解，输出对物体运动、碰撞、轨迹等物理行为的分析与预测。
- **多模态输入支持**：可接受文本、图像、视频等多种输入形式，并生成对应的视频或文本推理结果。
- **模型家族丰富**：提供多个尺寸的预训练模型（如 Cosmos 3 系列），满足从边缘设备到云端服务器不同性能需求。
- **多种部署方式**：支持通过 Diffusers、vLLM-Omni、Transformers、NIM 等多种框架进行模型加载和推理。
- **开放数据集与工具**：附带经过标注和清洗的训练数据集，以及用于模型微调、评估的开发工具链。

## 技术架构

Cosmos 采用基于 Transformer 的扩散模型架构，核心设计思路是“世界模型”——即让 AI 学习物理世界的底层规律而非简单的视觉模式。其模型架构具备以下特点：

首先，模型支持多种生成设置，包括基于文本提示、初始图像或视频片段的条件生成，能够灵活适应不同输入场景。其次，推理过程中可显式控制物理参数（如运动速度、物体数量、场景光照等），使生成结果更可控。此外，Cosmos 采用了分阶段的训练策略：先在大规模无标注视频数据上进行自监督预训练，再通过少量标注数据微调以提升特定任务的准确性。

技术实现上，Cosmos 依赖 NVIDIA 的 CUDA 生态和 TensorRT 优化，在 A100/H100 等 GPU 上可实现高效的推理性能。推理框架层面，项目既支持 Hugging Face 生态的 Diffusers 和 Transformers，也对接了高性能推理引擎 vLLM 和 NVIDIA 自身的 NIM（NVIDIA Inference Microservice），提供了从研究原型到生产部署的完整路径。

## 安装与使用

### 基本安装步骤

1. **环境要求**：
   - Python == 3.10 或 3.12
   - CUDA 12.4 或更高版本（推荐 12.8+）
   - PyTorch 2.5.1 或 2.7.0
   - GPU 内存建议 16GB 以上

2. **克隆仓库并安装依赖**：
```bash
git clone https://github.com/NVIDIA/cosmos.git
cd cosmos
pip install -r requirements.txt
```

3. **下载模型权重**（以 Cosmos 3 为例）：
```bash
huggingface-cli download nvidia/Cosmos-3-8B --local-dir ./models
```

### 最小可用示例（使用 Diffusers 进行视频生成）

```python
from diffusers import CosmosPipeline
import torch

pipe = CosmosPipeline.from_pretrained(
    "nvidia/Cosmos-3-8B",
    torch_dtype=torch.bfloat16
).to("cuda")

# 文本到视频生成
video = pipe("一辆红色汽车在笔直的公路上匀速行驶", 
             num_frames=25, 
             height=256, 
             width=256).frames[0]

# 保存生成的视频
imageio.mimsave("car_output.mp4", video, fps=8)
```

### 使用 NIM 进行推理（生产环境推荐）

```bash
# 启动 NIM 容器
docker run -it --rm --gpus all \
  -v /path/to/models:/models \
  nvcr.io/nvidia/cosmos-nim:latest \
  --model /models/Cosmos-3-8B
```

## 适用场景

- **自动驾驶仿真**：生成多样化的驾驶场景视频，包括不同天气、光照、交通流量条件下车辆和行人的动态行为，用于训练和评估自动驾驶感知与规划模型。
- **机器人训练**：在虚拟环境中模拟物体抓取、移动避障等任务，生成训练机器人策略所需的视觉数据，减少对真实物理实验的依赖。
- **智能基础设施监控**：对监控视频进行物理推理，预测人流、车流的运动趋势，检测异常事件（如物体坠落、拥堵形成等）。
- **影视内容创作**：辅助视频特效制作，快速生成符合物理规律的背景场景或碰撞特效，提高制作效率。

## 项目亮点

- **开放与可复制性**：与许多闭源的商业物理引擎不同，Cosmos 完全开源，模型权重、训练代码和数据集均以开放许可发布，社区可自由复现和改进。
- **物理理解能力强**：区别于传统的视频生成模型（主要关注视觉真实性），Cosmos 内建了对物体质量、惯性、碰撞等物理属性的建模能力，生成结果具有一致的物理逻辑。
- **模块化架构**：模型、数据集、工具链实现了清晰解耦，开发者可以单独替换或改进其中任一模块，灵活适配特定应用需求。
- **高性能推理支持**：通过与 vLLM 和 NIM 的集成，Cosmos 实现了毫秒级推理延迟，满足实时应用场景的要求。

## 相关链接

- [GitHub 仓库](https://github.com/NVIDIA/cosmos)
- [官方网站](https://www.nvidia.com/en-us/ai/cosmos/)
- [Cosmos Framework](https://github.com/NVIDIA/cosmos-framework)
- [Hugging Face 模型库](https://huggingface.co/collections/nvidia/cosmos3)
