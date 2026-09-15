---
tags:
  - trending
  - article
repo: multimodal-art-projection/YuE
date: 2026-09-15
language: Python
stars_total: 8661
stars_today: 559
---
## 项目概述

YuE2 是由多模态艺术投影（Multimodal Art Projection，M·A·P）团队联合香港科技大学、纽约大学、斯坦福大学、MBZUAI、NOIZ、ACE Studio 等机构推出的开源音乐生成模型。它在初代 YuE 的基础上重构了整体框架，将符号音乐生成与音频音乐生成统一到同一套体系之下，目标是在开源条件下达到接近前沿水平的音乐创作质量。项目以 Python 为主要实现语言，采用 Apache-2.0 许可证发布，主模型 YuE2-3B 与配套的 MERT2、SheetSage2 权重均已开放下载。

它主要解决三个层面的问题：一是传统音频生成模型"能听不能改"，用户难以对生成结果做结构化编辑；二是符号音乐（乐谱、MIDI）与音频之间存在鸿沟，缺乏统一的生成与转换路径；三是音乐创作流程缺少可与自动化智能体协作的接口。目标用户包括音乐创作者、AI 音乐研究者、需要批量生成或改编音乐内容的产品开发者，以及希望将音乐能力集成进自动化工作流的工程团队。

## 核心功能

- **符号化规划（Symbolic Planning）**：先生成结构化的音乐符号表示，再据此驱动音频渲染，使旋律、和声与曲式具备可解释、可修改的中间层。
- **零样本翻唱（Zero-shot Covers）**：在无需针对特定曲目微调的前提下，将既有歌曲改编为新的演唱风格或音色版本。
- **智能体音乐编辑（Agentic Music Editing）**：通过 Agent skill 接口，让自动化智能体能够对音乐片段执行编辑、续写、重编等操作。
- **统一符号与音频生成**：同一模型框架同时覆盖乐谱级与波形级输出，避免在多个独立模型间来回转换。
- **配套模型组件**：提供 MERT2（音乐理解表征模型）与 SheetSage2（乐谱/符号处理模型），分别承担特征提取与符号转换任务。
- **评测基准 WildSongBench（WSB）**：开放真实场景音乐数据集，用于评估生成模型在非受控条件下的表现。

## 技术架构

YuE2 的核心设计思路是"先符号、后音频"的两阶段生成范式。第一阶段由符号规划模块产出结构化的音乐表示，第二阶段在此基础上合成高质量音频，从而在保持生成可控性的同时提升音质。这种分层设计让编辑操作可以作用在符号层，而不必直接对波形做难以预测的扰动。

模型规模上，主模型 YuE2-3B 为约 30 亿参数级别，配套的 MERT2 负责音乐音频表征学习，SheetSage2 负责符号层面的解析与生成，三者形成理解—规划—生成的协作链路。项目还引入了 Agent skill 机制，将音乐编辑能力封装为可供外部智能体调用的技能，使模型不只是一个生成器，也可作为自动化创作流水线中的一环。评测方面，团队构建了 WildSongBench 数据集，用于在更贴近真实使用场景的条件下衡量生成质量。

## 安装与使用

项目以 Python 发布，通常的接入方式是通过 pip 安装依赖并从 Hugging Face 拉取权重。基本流程如下：

1. 克隆仓库：`git clone https://github.com/multimodal-art-projection/YuE.git`
2. 创建虚拟环境并安装依赖（参考仓库中的 `requirements` 或 `pyproject` 配置）。
3. 从 Hugging Face 下载 `m-a-p/YuE2-3B` 及所需的 MERT2、SheetSage2 权重。
4. 按 README 中的 "Quick start" 章节运行推理脚本，输入文本提示或符号素材，输出对应的音乐音频。

若需使用智能体编辑能力，可参考仓库中的 "Agent skill" 章节，将编辑技能注册到支持的 Agent 框架中。由于模型体量较大，建议在具备充足显存的 GPU 环境下运行。

## 适用场景

- **AI 辅助音乐创作**：创作者通过文本或符号输入快速生成旋律草稿，再在符号层做人工修改。
- **翻唱与风格迁移**：将已有歌曲改编为不同演唱风格或音色，用于内容二次创作。
- **自动化音乐生产流水线**：结合 Agent skill，把音乐生成与编辑嵌入到批量内容生产系统。
- **学术研究与基准评测**：借助 MERT2、SheetSage2 与 WildSongBench，开展音乐生成与理解方向的对比实验。

## 项目亮点

与多数只输出音频的生成模型相比，YuE2 的差异化在于把符号层作为一等公民：生成结果可读、可改、可追踪，这在需要精细控制的应用中尤为关键。零样本翻唱与智能体编辑两项能力进一步把模型从"生成工具"扩展为"可协作的创作组件"。此外，项目同步开源了配套的表征模型、符号模型与评测基准，形成较完整的研究闭环，而 Apache-2.0 许可证也为商业集成提供了较为宽松的条件。初代 YuE 的代码与文档被完整保留在 YuE-v1 分支，便于对照与迁移。

## 相关链接

- [GitHub 仓库](https://github.com/multimodal-art-projection/YuE)
- [在线演示](https://map-yue2.github.io/)
- [YuE2-3B 模型权重](https://huggingface.co/m-a-p/YuE2-3B)
- [MERT2 模型](https://huggingface.co/m-a-p/MERT-v2-FullSong)
- [SheetSage2 模型](https://huggingface.co/m-a-p/SheetSage2)
- [WildSongBench 数据集](https://huggingface.co/datasets/m-a-p/WildSongBench)
- [YuE-v1 分支](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1)
- [Discord 社区](https://discord.gg/ssAyWMnMzu)
