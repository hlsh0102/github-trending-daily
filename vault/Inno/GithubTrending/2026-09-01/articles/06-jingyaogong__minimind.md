---
tags:
  - trending
  - article
repo: jingyaogong/minimind
date: 2026-09-01
language: Python
stars_total: 56506
stars_today: 495
---
## 项目概述

MiniMind 是一个完全从零开始、使用 PyTorch 原生实现的大语言模型（LLM）开源项目。它的核心理念是“大道至简”——仅需约 3 块钱的 GPU 租用成本和 2 小时训练时间，即可训练出一个参数规模约为 64M 的超小语言模型。这个规模大约是 GPT-3 的 1/2700，使得普通个人 GPU 也能轻松完成训练与复现。

该项目不仅是一个模型实现，更是一套完整的 LLM 入门与实践教程。它覆盖了从数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）到 Tool Use、Agentic RL、自适应思考与模型蒸馏的全过程代码。项目还拓展了视觉模态模型 MiniMind-V、多模态 Omni 模型 MiniMind-O、扩散语言模型（MiniMind-dLM）和线性模型（MiniMind-Linear）等一系列衍生项目。

## 核心功能

- **极简模型架构**：提供 64M 参数的主线最小版本，结构清晰易懂，便于学习与二次开发。
- **全阶段训练链路**：覆盖大模型从预训练到对齐的完整流程，包括 MoE、SFT、LoRA、DPO、PPO、GRPO 等多种训练范式。
- **零依赖核心实现**：所有核心算法代码均使用 PyTorch 从零实现，不依赖 transformers 等第三方库的高层抽象接口，可完全透明地理解每个细节。
- **多模态扩展**：在语言模型基础上，提供了视觉（MiniMind-V）和 Omni 多模态（MiniMind-O）的扩展版本，支持图文理解与生成。
- **低成本可复现**：单张 NVIDIA 3090 即可完成全部训练流程，总成本控制在个位数人民币以内。
- **附带完整教程**：项目结构本身就是一套循序渐进的教学材料，适合作为 LLM 学习的入门项目。

## 技术架构

MiniMind 的设计遵循“极简但不简单”的原则。在模型结构上，它采用了经典的 Transformer 解码器架构，通过精心设计的参数分配，在 64M 参数规模下实现了令人满意的语言建模能力。项目针对小模型训练进行了大量工程优化，包括高效的数据加载、混合精度训练、梯度累积等技术，使得在消费级 GPU 上训练成为可能。

在训练链路设计上，MiniMind 采用了模块化设计。预训练阶段使用大规模清洗后的中文语料，通过掩码语言建模学习基础语义；SFT 阶段通过指令微调让模型学会遵循人类指令；对齐阶段则实现了多种强化学习算法（DPO、PPO、GRPO 等），用户可以根据需求自由选择和组合。更值得一提的是，项目将稀疏混合专家（MoE）机制也纳入了实现范围，为研究小规模 MoE 模型提供了参考。

所有实现均基于原生 PyTorch，这使得研究者可以轻松阅读、调试和修改每一行代码，深入理解大模型内部的工作原理，而不是被高层 API 所封装。

## 安装与使用

### 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/jingyaogong/minimind.git
cd minimind
```

2. 创建虚拟环境并安装依赖（推荐使用 conda 或 venv）：

```bash
conda create -n minimind python=3.10
conda activate minimind
pip install -r requirements.txt
```

3. 下载预训练数据与模型权重（可选），或直接从零开始训练。

### 最小可用示例

以下是一个从零开始进行预训练的简单示例：

```python
from model.model import MiniMind
from model.LMConfig import LMConfig
from train_pretrain import PretrainTrainer

# 配置模型参数
config = LMConfig(dim=512, n_layers=8, max_seq_len=512)
model = MiniMind(config)

# 创建数据加载器（使用项目自带的小规模样例数据）
from data_utils import build_pretrain_dataset
dataset = build_pretrain_dataset(config)

# 启动预训练
trainer = PretrainTrainer(model, config, dataset)
trainer.train(epochs=1)
```

训练完成后，可以使用 `generate` 接口进行文本生成：

```python
response = model.generate("中国的首都是", max_new_tokens=50)
print(response)
```

项目的 `scripts` 目录下提供了从预训练到 SFT、对齐、推理的完整 Shell 脚本，用户可以直接运行以复现论文中的实验结果。

## 适用场景

- **LLM 初学者学习与研究**：对于希望深入理解大语言模型内部原理、训练流程和实现细节的学习者，MiniMind 提供了透明、可读的代码和完整的训练链路，是理想的教学工具。
- **低成本原型验证**：研究人员或开发者需要在有限预算内快速验证新的训练算法、模型结构或数据策略时，MiniMind 能以极低成本完成概念验证（PoC）。
- **资源受限环境下的模型部署**：在边缘设备、嵌入式系统或需要轻量级本地语言模型的场景下，64M 参数的小模型依然具备基础的文本理解和生成能力，且推理开销极低。
- **多模态与 Agent 研究的基础平台**：基于 MiniMind 的衍生项目（V、O、dLM 等）为研究多模态对齐、Agentic RL 等前沿方向提供了轻量级实验平台。

## 项目亮点

与同类项目相比，MiniMind 的差异化优势主要体现在以下几点：

- **极低门槛**：用“3 块钱、2 小时”打破了 LLM 训练的高成本壁垒，让个人开发者也能拥有自己的大模型。
- **全链路透明**：不依赖高层封装库，所有算法细节完全暴露，从数据到模型再到对齐，每一步都可追溯、可修改。
- **生态完整**：不仅包含语言模型，还衍生出视觉、多模态、扩散语言模型等多个分支，形成了一个完整的低成本 LLM 研究矩阵。
- **实践导向**：项目本身就是一套优秀的教程，配合在线体验和视频介绍，极大降低了学习曲线。
- **活跃社区**：项目拥有超过 5.6 万 Star，社区活跃，Issue 与 Discussion 中有大量开发者交流与实践经验。

## 相关链接

- [GitHub 仓库](https://github.com/jingyaogong/minimind)
- [在线体验（ModelScope）](https://www.modelscope.cn/studios/gongjy/MiniMind)
- [Hugging Face 模型集合](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)
- [视频介绍（Bilibili）](https://www.bilibili.com/video/BV12dHPeqE72)
- [MiniMind-V（视觉模型）](https://github.com/jingyaogong/minimind-v)
- [MiniMind-O（多模态模型）](https://github.com/jingyaogong/minimind-o)
