---
tags:
  - trending
  - article
repo: OpenBMB/VoxCPM
date: 2026-06-01
language: Python
stars_total: 23785
stars_today: 635
---
## 项目概述

VoxCPM2 是由 OpenBMB 团队开发的新一代免分词器文本转语音（Tokenizer-Free TTS）模型，专注于多语言语音生成、创意音色设计以及高保真语音克隆。该项目旨在打破传统 TTS 系统对分词器和音素标注的依赖，通过端到端的生成方式，在保持自然度和表现力的同时，显著降低语音合成系统的复杂度。

对于语音交互开发者、内容创作者、无障碍技术研究者以及需要个性化语音解决方案的用户，VoxCPM2 提供了一套开箱即用、效果优异的开源工具。无论是为虚拟角色赋予独特声线，还是为多语言场景生成统一音色的语音，VoxCPM2 都展现出了强大的能力。

## 核心功能

- **免分词器多语言语音生成**：VoxCPM2 原生支持中英文等多语言混合文本的语音合成，无需繁琐的语言检测和音素转换，输入即可生成。
- **零样本语音克隆**：仅需数秒的参考音频，即可高保真地克隆任意说话人的音色、语调和风格，无需针对目标说话人进行额外训练。
- **创意音色设计**：支持通过文字描述或音频混合等方式，自由设计并生成全新的、不存在的虚拟音色，适用于游戏、动画等创意产业。
- **跨语言语音克隆**：即使参考音频使用的语言与待合成文本的语言不同，也能保持音色一致性，实现真正的跨语言语音生成。
- **灵活的语音控制**：提供对语速、停顿、情感基调等超语言特征的细粒度控制接口，允许用户微调输出效果。
- **实时交互体验**：优化后的推理引擎支持边缘端部署，在消费级 GPU 上即可实现接近实时的语音合成，满足交互式应用需求。

## 技术架构

VoxCPM2 的核心创新在于其 **免分词器（Tokenizer-Free）** 的架构设计。传统 TTS 模型通常需要先将文本转换为音素序列等中间表征，这引入了语言特定的预处理流水线和误差累积风险。VoxCPM2 直接对原始文本进行编码，利用大规模多语言语料预训练的编码器捕获文本的发音与语义特征。

模型基于 **Voice-Continuity Pretraining Model（VCPM）** 范式，将语音连续信号与文本语义空间对齐。通过精心设计的对比学习与生成式预训练目标，模型学会了在不依赖离散符号的情况下，理解文本到语音的映射关系。其解码器采用流匹配（Flow Matching）或扩散模型（Diffusion Model）架构，从高斯噪声逐步演化为高质量语音波形，确保输出具有极高的自然度和清晰度。

一个显著的设计特点是模型输入仅需文本和可选的参考音频。在 zero-shot 克隆模式下，模型通过交叉注意力机制提取参考音频的音色特征，并将其注入生成过程，从而实现对说话人身份的精确迁移。这种端到端的架构极大简化了部署流程，用户无需准备复杂的语言学前端资源。

## 安装与使用

VoxCPM2 基于 Python 和 PyTorch 框架开发。推荐使用 Conda 或 pip 管理依赖环境。

**基本安装步骤：**

```bash
# 1. 克隆仓库
git clone https://github.com/OpenBMB/VoxCPM.git
cd VoxCPM

# 2. 创建并激活虚拟环境（推荐 Python 3.9+）
conda create -n voxcpm python=3.9
conda activate voxcpm

# 3. 安装依赖
pip install -r requirements.txt

# 4. 下载预训练模型（首次运行会自动下载，或手动从 Hugging Face 模型库获取）
# 模型权重位于：https://huggingface.co/openbmb/VoxCPM2
```

**最小可用示例——零样本语音克隆：**

```python
import torch
from voxcpm import VoxCPM2

# 加载模型
model = VoxCPM2.from_pretrained("openbmb/VoxCPM2")
model.cuda()

# 准备参考音频（假设已录制一段说话人的音频样本 audio_reference.wav）
# 文本内容
text = "你好，欢迎使用 VoxCPM2 语音克隆系统。这是一个免分词器的多语言语音合成模型。"

# 执行语音克隆合成
wav = model.tts(
    text=text,
    reference_audio="audio_reference.wav",  # 参考音频路径
    language="zh",  # 语言标识
)

# 保存生成的音频
import soundfile as sf
sf.write("output_audio.wav", wav, samplerate=24000)
```

## 适用场景

- **短视频与多语言内容创作**：创作者无需逐音录制，即可用同一声线或设计的新音色，为不同语言的视频配音，提高内容生产效率。
- **智能语音助手与虚拟角色**：为智能设备、车载系统、游戏 NPC 等场景快速生成符合角色个性的语音，支持情感变化和实时交互。
- **无障碍阅读与教育**：将电子书、网页内容或学习资料实时转换为自然语音，特别适合多语言学习材料的语音化呈现。
- **个性化语音服务**：为个人用户提供专属语音助手，或为盲人用户生成亲友音色的语音消息，增强情感连接。

## 项目亮点

- **突破传统范式**：免去分词器和音素标注，大幅降低系统复杂度和部署门槛，尤其适合非英语语言和混合语言场景。
- **零样本克隆质量领先**：相比其他开源方案，VoxCPM2 在语音克隆的自然度、音色相似度和稳定性上均有明显优势。
- **多语言与跨语言能力**：无需额外适配即可处理中英混合文本，并能完成跨语言音色迁移，这是许多现有系统难以做到的。
- **活跃的社区与生态**：作为 OpenBMB 开源社区的项目，拥有完善的中英文文档、Hugging Face 演示页面和 ModelScope 模型库，方便开发和集成。
- **Apache-2.0 许可**：宽松的开源许可允许商业使用，促进了技术创新与实际应用的快速落地。

## 相关链接

- [GitHub 仓库](https://github.com/OpenBMB/VoxCPM)
- [在线演示（Hugging Face）](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo)
- [音频示例页](https://openbmb.github.io/voxcpm2-demopage/)
- [官方文档](https://voxcpm.readthedocs.io/en/latest/)
- [Hugging Face 模型权重](https://huggingface.co/openbmb/VoxCPM2)
- [ModelScope 模型权重](https://modelscope.cn/models/OpenBMB/VoxCPM2)
