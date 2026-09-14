---
tags:
  - trending
  - article
repo: multimodal-art-projection/YuE
date: 2026-09-14
language: Python
stars_total: 7962
stars_today: 487
---
## 项目概述

YuE2 是由 M·A·P（Multimodal Art Projection）团队联合香港科技大学、纽约大学、斯坦福大学、MBZUAI、NOIZ 与 ACE Studio 等机构推出的开源音乐生成模型。项目名称中的 “YuE” 取意于“音乐”，其第二代版本的核心目标是在统一框架下同时处理**符号音乐（symbolic music，如 MIDI、乐谱）与音频音乐（audio music）** 的生成任务，并尝试在两者之间建立可对齐的表示与规划能力。

与大量以“文生音频”为单一目标的音乐生成模型不同，YuE2 试图解决三个相互关联的问题：第一，纯音频模型缺乏对乐理结构的可控性，难以进行精确的音符级编辑；第二，纯符号模型生成的乐谱需要额外渲染才能听到，且难以处理真实人声与音色表现；第三，已有工具在“生成—改写—再生成”的迭代创作流程中缺乏统一的规划机制。YuE2 面向的目标用户包括音乐 AI 研究者、需要可控音乐素材的创作者、以及希望把音乐生成能力集成进 Agent 工作流的开发者。

项目采用 Apache-2.0 协议开源，代码以 Python 为主，当前在 GitHub 上已获得约 8000 星标。原版 YuE 的代码、文档与授权协议完整保留在 `YuE-v1` 分支中，便于旧用户继续使用与对照。

## 核心功能

- **符号规划（Symbolic Planning）**：模型先以符号层面（如音符、和弦、结构段落）进行高层规划，再驱动音频合成，使生成结果具备明确的结构可解释性。
- **零样本翻唱（Zero-shot Covers）**：在无需针对特定歌手或曲目微调的前提下，将给定歌曲转换为目标音色或风格的翻唱版本。
- **Agentic 音乐编辑**：将音乐编辑任务拆解为由智能体驱动的多步操作，支持通过自然语言指令完成改写、续写、局部替换等编辑行为。
- **统一符号与音频生成**：在同一模型体系下同时支持符号域与音频域的生成，并在二者之间进行对齐，减少跨模态转换的信息损失。
- **配套模型与基准**：随项目一同发布 MERT2（音乐理解表征模型）、SheetSage2（乐谱相关模型）以及 WildSongBench 评测数据集，形成可复现的评测闭环。

## 技术架构

YuE2 的整体设计围绕“先规划、后发声”展开。符号层承担结构决策，负责确定曲式、和声走向与节奏骨架；音频层则以这些符号信息为条件进行高保真渲染，从而在保持可控性的同时获得接近前沿水平的音质。这种分层思路使模型既能输出可被程序进一步处理的符号表示，也能直接产出可聆听的音频。

在模型规模上，官方发布了 3B 参数量的 YuE2 版本，托管于 Hugging Face。项目还开源了 MERT2 用于音乐理解与特征表征，SheetSage2 用于乐谱相关的建模任务，二者可作为独立组件被其他研究复用。评测方面，WildSongBench（WSB）提供了面向真实世界歌曲的基准，用于衡量生成质量与可控性。Agentic 编辑部分则通过将编辑指令分解为可执行步骤，把生成模型接入到具备规划能力的智能体循环中。

## 安装与使用

项目为 Python 实现，通常建议在具备 CUDA 环境的机器上运行。基本流程如下：

```bash
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
pip install -r requirements.txt
```

随后可从 Hugging Face 下载 `m-a-p/YuE2-3B` 权重并按仓库内 Quick start 指引加载模型。最小可用示例如下（示意性写法，具体接口以仓库文档为准）：

```python
from yue import YuE2

model = YuE2.from_pretrained("m-a-p/YuE2-3B")
# 以符号规划为条件生成音频
audio = model.generate(symbolic_plan="...", prompt="...")
audio.save("output.wav")
```

对于 Agent 场景，仓库提供了 “Agent skill” 相关说明，可将音乐生成与编辑能力封装为可供智能体调用的工具。若需要旧版 YuE，请切换到 `YuE-v1` 分支获取对应代码与协议。

## 适用场景

- **可控音乐创作**：需要精确控制曲式、和声或具体音符，而非仅靠文本提示“碰运气”的作曲流程。
- **翻唱与音色迁移**：在无训练数据的情况下将已有歌曲转换为指定音色或演唱风格。
- **智能体驱动的编辑工作流**：把音乐改写、续写、局部替换等操作接入自动化 Agent 管线。
- **音乐 AI 研究与评测**：借助 MERT2、SheetSage2 与 WildSongBench 进行表征学习、乐谱建模与基准测试。

## 项目亮点

与多数纯音频音乐生成模型相比，YuE2 的差异点在于**符号与音频的统一建模**：它并不把符号当作辅助条件，而是作为规划层参与生成过程，从而在结构可控性与音频质量之间取得平衡。零样本翻唱与 Agentic 编辑进一步扩展了使用边界，使模型不仅能“生成一段音乐”，还能在既有素材上执行有目标的操作。配套发布的 MERT2、SheetSage2 与 WildSongBench 也降低了复现与横向比较的门槛。此外，项目对 v1 分支的完整保留，体现了对既有用户与授权协议的延续性考虑。

## 相关链接

- [GitHub 仓库](https://github.com/multimodal-art-projection/YuE)
- [在线演示 Demos](https://map-yue2.github.io/)
- [YuE2-3B 模型（Hugging Face）](https://huggingface.co/m-a-p/YuE2-3B)
- [MERT2（Hugging Face）](https://huggingface.co/m-a-p/MERT-v2-FullSong)
- [SheetSage2（Hugging Face）](https://huggingface.co/m-a-p/SheetSage2)
- [WildSongBench 数据集](https://huggingface.co/datasets/m-a-p/WildSongBench)
- [YuE-v1 分支](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1)
