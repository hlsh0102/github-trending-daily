---
tags:
  - trending
  - article
repo: OpenBMB/VoxCPM
date: 2026-06-03
language: Python
stars_total: 25315
stars_today: 783
---
## 项目概述

VoxCPM2 是一个基于深度学习的无分词器文本转语音（TTS）框架，由 OpenBMB 团队开发。该项目旨在解决传统 TTS 系统在处理多语言、多说话人、创造性语音设计以及真实语音克隆时的局限性。VoxCPM2 的核心创新在于完全抛弃了传统的文本分词器（tokenizer），直接从原始文本到语音频谱的端到端映射，从而避免了分词造成的语义信息丢失和多语言适配难题。

目标用户包括语音合成研究者、AI 应用开发者、有声读物制作团队、虚拟角色配音师，以及需要个性化语音交互系统的产品经理。目前项目在 GitHub 获得超过 2.5 万颗星标，并提供了完整的文档、在线 Demo 和预训练模型。

## 核心功能

- **无分词器多语言语音生成**：支持中文、英文、日文、韩文等多种语言的直接合成，无需为每种语言训练特定的分词器，大幅降低跨语言部署成本。
- **创造性语音设计**：允许用户通过调节音色、语速、语调、情感强度等参数，生成从温柔自然到夸张戏剧化的多样化语音风格。
- **真实语音克隆**：仅需短至数秒的参考音频，即可高精度克隆目标说话人的音色、共鸣和发音习惯，支持同语言及跨语言克隆。
- **零样本说话人自适应**：无需微调模型，直接利用参考音频的特征向量实现新说话人的即时合成。
- **情感与副语言控制**：支持控制笑声、叹息、停顿等副语言现象，以及快乐、悲伤、愤怒等基本情感表达。
- **实时流式合成**：通过优化的 Transformer 架构，支持低延迟的流式输出，适合对话系统等实时场景。

## 技术架构

VoxCPM2 采用 **Tokenizer-free 端到端架构**，核心基于改进的 Transformer 解码器，直接建模文本序列与 Mel 频谱之间的依赖关系。其关键技术特点包括：

1. **无分词器输入表示**：使用字符级（Character-level）或子词级（Subword-level）编码，配合特殊标记表示说话人、语速、情感等控制信息。这种方法避免了 BPE、SentencePiece 等分词器对语义边界的切割损失，尤其擅长处理零样本的语言迁移。
2. **多任务联合学习**：在训练阶段同时学习文本到频谱的映射、说话人嵌入、情感条件生成三个子任务，通过共享编码层提升泛化能力。模型使用对比学习（Contrastive Loss）来分离说话人音色与内容信息。
3. **条件变分自编码器（CVAE）框架**：引入潜在变量控制语音的韵律变化（如重音、节奏），使得每次生成相同文本可得到不同但自然的语音输出，避免传统 TTS 的“机械感”。
4. **高效推理优化**：采用 Flash Attention 和 KV Cache 技术，在 GPU 上实现 3x 的推理加速；同时支持 ONNX 导出和 CPU 部署，降低使用门槛。

## 安装与使用

**安装**  
推荐使用 Python 3.8+ 和 PyTorch 2.0+。通过 pip 安装：

```bash
pip install git+https://github.com/OpenBMB/VoxCPM.git
# 或从源码安装
git clone https://github.com/OpenBMB/VoxCPM.git
cd VoxCPM
pip install -r requirements.txt
```

**最小可用示例**（Python）：

```python
from voxcpm import VoxCPM2

# 加载预训练模型（自动下载到缓存）
model = VoxCPM2.from_pretrained("openbmb/VoxCPM2")

# 基础文本转语音
wav = model.tts("你好，欢迎使用 VoxCPM2 语音合成系统。")

# 保存音频文件
wav.save("output.wav")

# 使用参考音频进行语音克隆
ref_audio = model.load_audio("speaker_sample.wav")
cloned_wav = model.clone(
    text="大家好，我是通过语音克隆生成的。",
    reference_audio=ref_audio
)
cloned_wav.save("cloned.wav")

# 控制情感与语速
happy_wav = model.tts(
    "今天天气真好！",
    emotion="happy",
    speed=1.2
)
```

**命令行使用**：  
```bash
voxcpm tts --text "你好，世界" --output hello.wav
voxcpm clone --text "克隆测试" --ref speaker.wav --output clone.wav
```

## 适用场景

- **有声内容生产**：自动生成有声书、播客、新闻播报，支持多角色配音和情感切换，极大降低专业录音的时间和成本。
- **虚拟数字人交互**：为虚拟主播、AI 助手、游戏 NPC 提供实时、富有情感的语音交互，配合情感控制参数实现场景自适应。
- **语言学习与辅助**：生成多语言标准发音的例句，支持语速调节和语音克隆，帮助学习者模仿特定地区或特定人的发音。
- **无障碍辅助**：为视障人士提供自然流畅的语音朗读服务，支持个人风格定制（如克隆亲友声音）。

## 项目亮点

- **真正意义上的多语言统一框架**：无需为每种语言训练单独模型，VoxCPM2 在 10 种以上语言的零样本合成中表现出色，这得益于无分词器设计带来的语言通用性。
- **高质量的语音克隆**：仅需 5-10 秒参考音频即可实现高保真克隆，声音相似度在主观评测中接近真人录音，且支持跨语言克隆（如用中文参考音频生成英文语音）。
- **丰富的可控性**：相比仅支持文本输入的 TTS 系统，VoxCPM2 提供了情感、语速、音色、韵律等 7 个维度的精细控制，同时保持了自然度。
- **开源友好的许可**：采用 Apache 2.0 协议，允许商业使用和二次开发。提供完整的文档、Hugging Face 在线 Demo 和 ModelScope 镜像，降低学术和工业界的使用门槛。

## 相关链接

- [GitHub 仓库](https://github.com/OpenBMB/VoxCPM)
- [在线 Demo 互动试玩](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo)
- [音频样例页面](https://openbmb.github.io/voxcpm2-demopage/)
- [项目文档](https://voxcpm.readthedocs.io/en/latest/)
- [Hugging Face 模型下载](https://huggingface.co/openbmb/VoxCPM2)
- [ModelScope 模型下载](https://modelscope.cn/models/OpenBMB/VoxCPM2)
