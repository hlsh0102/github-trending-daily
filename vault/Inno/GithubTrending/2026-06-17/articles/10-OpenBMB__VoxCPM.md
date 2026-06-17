---
tags:
  - trending
  - article
repo: OpenBMB/VoxCPM
date: 2026-06-17
language: Python
stars_total: 30279
stars_today: 408
---
## 项目概述

VoxCPM2 是由 OpenBMB 团队开发的新一代语音生成模型，旨在实现无分词器的多语言语音合成、创意语音设计和高保真语音克隆。该项目解决了传统 TTS（文本到语音）系统依赖复杂分词器、跨语言能力弱、音色定制困难等问题。目标用户包括语音应用开发者、内容创作者、AI 研究人员以及需要高质量语音合成的企业用户。VoxCPM2 基于先进的自回归语言模型架构，能够直接从文本生成原始音频，无需额外的声学特征提取或分词处理步骤。

## 核心功能

- **多语言语音生成**：支持中文、英文、日文、韩文等多种语言的语音合成，能在同一模型中实现多语言混合输出，无需切换不同的语音引擎。
- **无分词器架构**：模型直接处理文本和音频的原始序列，避免了传统分词器带来的误差累积和信息丢失，实现了更自然的语音生成。
- **创意语音设计**：用户可以通过文本提示或参考音频灵活控制语音的风格、情感、语速、音高等属性，轻松定制独特的语音输出。
- **高保真语音克隆**：仅需数秒参考音频即可克隆任意说话人的音色、语气和韵律，克隆结果几乎与人声无区别，具备“活人感”而非机械感。
- **零样本语音合成**：无需针对特定说话人进行微调，直接利用预训练模型的泛化能力，为未见过的说话人生成高质量语音。
- **实时交互能力**：支持流式语音生成，适合聊天机器人、虚拟助手等需要低延迟交互的应用场景。

## 技术架构

VoxCPM2 的核心技术架构基于**无分词器的自回归 Transformer 语言模型**。它采用统一的序列建模方式，将文本和原始音频 token（通过音频编解码器量化得到）视为同质的序列数据，直接在连续语言空间中进行建模和生成。这一设计跳过了传统 TTS 中文本到声学特征（如 Mel 频谱）再到波形（如 Vocoder）的级联流程，简化了生成管线，同时避免了中间表示的信息损失。

在训练阶段，VoxCPM2 使用大规模多语言语音数据对模型进行预训练，学习语音与文本之间的深层映射关系。其关键技术包括：(1) 高效的音频 token 化方法，将原始波形压缩为紧凑的离散序列；(2) 多任务学习策略，同时支持文本到语音、语音到语音、语音克隆等任务；(3) 变长上下文注意力机制，能够处理任意长度的参考音频，实现灵活的音色和风格提取。此外，模型采用了 MoE（混合专家）架构的部分设计，在保持推理速度的同时提升了多语言和多样本场景下的生成质量。

## 安装与使用

VoxCPM2 的安装和使用相对简单，主要依赖 Python 环境和 PyTorch 框架。以下为基本步骤：

1. **环境要求**：Python 3.8+，PyTorch 2.0+，CUDA 11.8+（推荐）
2. **从 GitHub 克隆仓库**：
   ```bash
   git clone https://github.com/OpenBMB/VoxCPM.git
   cd VoxCPM
   ```
3. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```
4. **下载模型权重**（可选，也可在运行时自动下载）：
   ```bash
   python scripts/download_model.py
   ```

**最小可用示例（Python 脚本）**：
```python
from voxcpm import VoxCPM

# 初始化模型
model = VoxCPM.from_pretrained("openbmb/VoxCPM2")

# 基础文本转语音
audio = model.tts("今天天气真好，我们去散步吧。", speaker="普通话女声")
model.save_audio(audio, "output.wav")

# 语音克隆：使用参考音频
reference_audio = "path/to/speaker.wav"
audio = model.clone_voice("欢迎使用VoxCPM2语音克隆功能", reference_audio)
model.save_audio(audio, "cloned_output.wav")
```

模型也提供了命令行界面及在线演示（Hugging Face Spaces），用户无需部署即可体验核心功能。

## 适用场景

- **内容创作与媒体制作**：播客、有声书、短视频配音等场景中，创作者使用 VoxCPM2 快速生成多风格语音，或克隆嘉宾音色，大幅降低录制成本。
- **虚拟数字人与语音助手**：集成到聊天机器人、客服系统或虚拟主播中，实现自然、个性化的语音回复，提升用户体验。
- **跨语言语音应用**：多语言翻译助手、语言学习工具等，VoxCPM2 支持在同一对话中混合使用中文、英文等语言进行语音输出。
- **教育与辅助技术**：为视障用户、阅读障碍者提供高质量的语音朗读服务，或为语言学习者提供模仿范例。

## 项目亮点

- **无分词器创新**：率先在 TTS 领域大规模实践无分词器方法，简化了多语言和跨语言场景下的适配难度，尤其对日语、韩语等复杂书写系统友好。
- **高真实感语音克隆**：与市面主流方案相比，VoxCPM2 克隆的语音在自然度、情感表达和韵律一致性上表现更优，尤其擅长保留参考音中的微妙语气变化。
- **零样本泛化能力**：无需针对特定说话人进行微调或训练，直接利用模型的知识迁移能力，极大降低了使用门槛和部署成本。
- **丰富的生态支持**：项目提供了详细的文档（ReadTheDocs）、在线演示、Hugging Face 模型权重、ModelScope 镜像以及技术论文，方便用户快速上手和研究。
- **开源友好许可**：采用 Apache-2.0 许可证，允许自由使用、修改和商业化，社区活跃度高，持续收到用户反馈和贡献。

## 相关链接

- [GitHub 仓库](https://github.com/OpenBMB/VoxCPM)
- [在线演示（Hugging Face Spaces）](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo)
- [官方文档（ReadTheDocs）](https://voxcpm.readthedocs.io/en/latest/)
- [Hugging Face 模型库](https://huggingface.co/openbmb/VoxCPM2)
- [ModelScope 镜像](https://modelscope.cn/models/OpenBMB/VoxCPM2)
- [Demo 音频页面](https://openbmb.github.io/voxcpm2-demopage/)
- [技术报告（arXiv）](https://arxiv.org/abs/2606.06928)
