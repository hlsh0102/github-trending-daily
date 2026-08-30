---
tags:
  - trending
  - article
repo: p-e-w/heretic
date: 2026-08-30
language: Python
stars_total: 28827
stars_today: 150
---
## 项目概述

Heretic 是一款专为 Transformer 架构语言模型设计的全自动审查去除工具，旨在通过先进的技术手段移除模型中的“安全对齐”（即审查机制），同时避免昂贵的后训练过程。该项目由 p-e-w 开发并维护，采用 AGPL-3.0 许可证，在 GitHub 上已获得超过 2.8 万星标，社区关注度极高。

对于研究人员、开发者以及需要无限制语言生成能力的用户而言，Heretic 解决了传统审查移除方法依赖人工调参、对模型内部结构理解要求高、且容易损害模型智能水平的痛点。其最大特点是“全自动”——用户无需理解 Transformer 内部机制，只需掌握基本的命令行操作，即可完成模型的去审查处理。

## 核心功能

- **全自动参数优化**：基于 TPE（Tree-structured Parzen Estimator）参数优化器，由 Optuna 驱动，自动搜索高质量的 abliteration 参数组合，无需人工干预。
- **双重目标协同优化**：同时最小化模型拒答次数与原始模型的 KL 散度，确保去审查后的模型在保留智能水平的同时，尽可能减少拒绝回答的行为。
- **广泛模型支持**：支持大多数稠密模型（dense models），包括多种多模态模型，兼容性良好。
- **无需后训练**：采用方向性消融（directional ablation）技术，直接在推理层面改变模型行为，避免昂贵的微调或重新训练。
- **直观的命令行界面**：设计简洁，任何具备基础命令行技能的用户均可快速上手。
- **社区生态整合**：提供 Discord 及 Matrix 社区支持，并托管于 Hugging Face 组织，便于模型共享与协作。

## 技术架构

Heretic 的核心技术基于**方向性消融**（directional ablation），该概念在学术文献中也被称为“abliteration”，源自 Arditi 等人 2024 年的研究。项目在此基础上进行了深度优化，融合了 Lai 于 2025 年提出的两种改进算法：投影消融（projected abliteration）和范数保持双投影消融（norm-preserving biprojected abliteration），从而提升消融操作的精度与稳定性。

在具体实现上，Heretic 构建了一个由 Optuna 驱动的 TPE 参数优化器。该优化器以拒答次数减少和 KL 散度最小化为双目标，在参数空间中搜索最佳消融方向与强度。这种设计使得 Heretic 能够在无需理解模型内部细节的前提下，自动找到高质量的处理参数，从而在去除审查的同时，最大限度保留模型的原始能力。

值得注意的是，Heretic 采用纯推理架构，不需要访问模型的训练数据或进行梯度计算，这极大地降低了使用门槛和硬件需求。对于大多数消费级 GPU，即可完成模型的去审查处理。

## 安装与使用

### 安装步骤

1. 确保系统已安装 Python 3.10 或更高版本。
2. 通过 pip 安装 Heretic：

```bash
pip install heretic
```

3. 如需支持多模态模型，建议同时安装额外的依赖项（可通过 `pip install heretic[multimodal]` 安装）。

### 最小可用示例

假设您已经有一个 Hugging Face 格式的模型，使用 Heretic 进行去审查处理只需执行一行命令：

```bash
heretic decensor --model-path /path/to/model --output-dir /path/to/output
```

其中：
- `--model-path` 指定原始模型的本地路径或 Hugging Face 模型 ID。
- `--output-dir` 指定去审查后模型的保存目录。

处理完成后，您可以在输出目录中找到与原始模型结构一致、但已去除审查的模型文件，可直接加载用于推理。

## 适用场景

- **研究与学术探索**：研究人员可以快速、可复现地获得无审查模型，用于分析审查机制的工作原理，或作为后续微调的基础模型。
- **创意写作与对话系统**：需要无限制文本生成的创意写作、角色扮演或开放式聊天机器人项目，可借助 Heretic 获得更自由的模型输出。
- **多语言与多模态应用**：对于支持多模态输入的模型，Heretic 同样适用，可为图像描述、视频理解等任务提供更少限制的生成能力。
- **本地化部署与隐私保护**：用户可在本地完成去审查处理，避免将模型或数据发送至第三方服务，保障隐私安全。

## 项目亮点

与同类工具相比，Heretic 的差异化优势显著：

- **完全自动化**：多数现有方案需要手动分析模型内部神经元或注意力头，具有一定的专业知识门槛，而 Heretic 只需一行命令即可完成。
- **智能保留**：通过 KL 散度约束，Heretic 在移除审查的同时，尽可能不损伤模型的推理、生成等核心智能能力，避免了“粗暴消融”导致的能力骤降问题。
- **学术前沿技术整合**：项目紧随 2025 年的最新算法进展，采用范数保持双投影消融等先进方法，使处理效果更为精细。
- **活跃的社区与生态**：项目拥有 Discord 与 Matrix 社区，并能通过 Hugging Face 直接分享处理后的模型，形成了良好的协作环境。

## 相关链接

- [GitHub 仓库](https://github.com/p-e-w/heretic)
- [Heretic 官方 Discord](https://discord.gg/gdXc48gSyT)
- [Heretic Matrix 空间](https://matrix.to/#/#heretic:matrix.org)
- [Hugging Face 组织](https://huggingface.co/heretic-org)
