---
tags:
  - trending
  - article
repo: jingyaogong/minimind
date: 2026-09-02
language: Python
stars_total: 57373
stars_today: 1005
---
## 项目概述

MiniMind 是一个完全从零开始、使用 PyTorch 原生代码训练超小规模语言模型的开源项目。其目标非常明确：让普通个人开发者仅凭一块消费级 GPU（如 NVIDIA 3090）和约 3 元人民币的算力成本，在 2 小时内训练出一个参数规模约为 6400 万（64M）的可运行语言模型。该项目由 jingyaogong 发起，目前已获得超过 5.7 万 Star，是 GitHub 上备受关注的开源教育项目之一。

MiniMind 的核心价值在于“大道至简”——它将大语言模型复杂的训练链路浓缩为一个可复现、可理解的最小实现。其主模型体积约为 GPT-3 的 1/2700，但麻雀虽小，五脏俱全。项目不仅覆盖了从数据清洗、预训练（Pretrain）、监督微调（SFT）到 LoRA、RLHF（DPO）、RLAIF（PPO/GRPO/CISPO）的全流程代码，还进一步扩展了 Tool Use、Agentic RL、自适应思考与模型蒸馏等前沿方向。项目的主要受众是希望深入理解 LLM 底层原理的学生、研究人员以及希望在有限算力条件下进行快速实验的工程师。

## 核心功能

- **极轻量模型设计**：MiniMind 主线模型参数仅为 64M，单卡 3090 即可完成全流程训练与推理，极大降低了大模型学习与实验的硬件门槛。
- **全阶段训练链路覆盖**：从零开始实现并开源了包括数据清洗、词表构建、预训练、SFT、LoRA 微调、DPO、PPO、GRPO 在内的完整训练代码，让用户能够亲眼目睹一个“婴儿”模型的完整成长过程。
- **纯 PyTorch 原生实现**：所有核心算法代码不依赖 HuggingFace Transformers 或 DeepSpeed 等第三方库的高层封装，仅使用 PyTorch 基础算子从零搭建，有助于使用者深入理解每个模块的数学原理与工程实现。
- **多模态生态拓展**：项目不仅局限于文本模型，还衍生出视觉模型 MiniMind-V、多模态 Omni 模型 MiniMind-O、扩散语言模型（dLM）以及线性注意力模型，展现了统一的架构设计思路。
- **知识蒸馏与高效对齐**：集成了模型蒸馏技术，允许用户利用更大的教师模型来提升小模型的性能上限，同时提供了完整的 RLHF/RLAIF 对齐代码。
- **免费可商用授权**：项目遵循 Apache 2.0 协议完全开源，无论是学习研究还是商业应用均无授权壁垒。

## 技术架构

MiniMind 采用经典的 Decoder-only Transformer 架构，但在设计上做了针对小规模模型的优化：
1. **深度与宽度平衡**：在 64M 参数限制下，项目通过调整层数（如 8 层）和隐藏维度（如 512）来保证模型具备足够的学习容量，同时避免过深的网络导致训练收敛困难。
2. **数据工程优先**：项目开源了高质量的中文语料清洗流程，这是一个常被初学者忽略但实际决定模型智商天花板的关键环节。MiniMind 提供了一整套从原始网页到训练样本的清洗与去重脚本。
3. **全流程代码解耦**：项目将预训练、SFT、RLHF 等阶段拆分为独立可运行的 Python 脚本，各阶段通过统一的模型定义与数据接口衔接。这种设计使得用户既可以选择端到端跑通完整流程，也可以单独在某一个阶段进行详尽的调试学习。
4. **异构模态统一**：在拓展的视觉或多模态版本中，MiniMind 采用类似 Llama 的投影层将图像编码器与文本解码器桥接，保持了主干结构的简洁性。扩散语言模型则探索了将连续扩散过程应用于离散文本 token 的生成范式。

## 安装与使用

**环境准备**
项目基于 Python 3.9+ 与 PyTorch 2.0+。建议使用 Anaconda 创建虚拟环境，并安装依赖：

```bash
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

**数据下载与预处理**
项目提供了轻量级的数据集下载脚本，可自动拉取预训练语料与 SFT 指令集：

```bash
python scripts/download_data.py
```

**启动预训练**
修改 `train_pretrain.py` 中的模型配置参数后，直接执行：

```bash
python train_pretrain.py
```

**SFT 微调**
完成预训练后，加载 checkpoint 进行指令微调：

```bash
python train_sft.py
```

**推理验证**
训练完成后，可以通过交互式命令行进行对话测试：

```bash
python generate.py
```

## 适用场景

- **LLM 教学与自学**：对于希望理解 Transformer 内部机制、损失函数设计、RLHF 策略梯度推导等核心概念的初学者，MiniMind 是一份极佳的活教材。所有代码均可断点调试，摆脱了只能调用黑盒 API 的困境。
- **低成本原型验证**：研究者在提出新算法（如新的注意力变体或对齐策略）时，不必先在 7B/13B 大模型上进行昂贵实验，可以先在 MiniMind 上验证有效性，再放大规模。
- **垂直领域小模型定制**：企业或开发者若需要训练一个针对特定行业（如法律、医疗）的轻量级对话模型，且数据量在几 GB 以内，MiniMind 提供了一个快速的基线方案。
- **智能体与工具调用研究**：由于模型体积小，在 CPU 或边缘设备上也能运行，特别适合用于探究 Tool Use、Function Calling 或 Agentic RL 循环逻辑的研究场景。

## 项目亮点

与目前市面上众多的开源大模型项目相比，MiniMind 的核心差异化优势在于其“显微镜”属性。主流开源权重模型（如 Llama 3 或 Qwen）虽然强大，但对绝大多数学习者而言只是一个无法窥探内部的成品。而 MiniMind 则是将炼丹炉的每一根柴火都清晰地摆在你面前。

1. **门槛极低且完整**：不像其他教程只展示预训练代码，MiniMind 将 SFT、DPO、PPO 等高级对齐技术也以最小可用形式呈现，这在开源社区并不多见。
2. **真正的从零实现**：不依赖 huggingface 的 Trainer 或 Accelerate，让用户习惯于亲手计算 loss 与梯度，这对于深度学习从业者的内功修习大有裨益。
3. **极致的可复现性**：训练数据、脚本、参考 checkpoint 均随仓库发布。只要硬件满足要求，跑出的最终模型与论文报告的指标高度一致，杜绝了“开源即跑路”的现象。
4. **生态协同**：由单一文本模型扩展出的视觉、Omni 等系列，展示了一套主干架构如何以极小的代码改动适应多类任务，为读者提供了宏观的架构视野。

## 相关链接

- [GitHub 仓库](https://github.com/jingyaogong/minimind)
- [在线 Demo 体验（ModelScope）](https://www.modelscope.cn/studios/gongjy/MiniMind)
- [B站视频介绍](https://www.bilibili.com/video/BV12dHPeqE72)
- [MiniMind-V 视觉模型仓库](https://github.com/jingyaogong/minimind-v)
- [MiniMind-O 多模态模型仓库](https://github.com/jingyaogong/minimind-o)
- [HuggingFace 模型权重集合](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)
