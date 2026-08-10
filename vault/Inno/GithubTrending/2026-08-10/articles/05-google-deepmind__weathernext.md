---
tags:
  - trending
  - article
repo: google-deepmind/weathernext
date: 2026-08-10
language: Python
stars_total: 7129
stars_today: 86
---
## 项目概述

WeatherNext 是由 Google DeepMind 与 Google Research 联合开发的全球中期天气与气旋预报模型项目。该仓库包含 WeatherNext 2（WN2）的完整代码实现，WN2 是一个基于人工智能的全球大气预报系统，能够以高精度和高效率进行中短期天气预报。此外，仓库还包含了前代模型 GraphCast 和 GenCast 的代码，使研究者能够在同一框架下对比和使用三代 AI 天气预报模型。

该项目主要面向气象研究人员、数据科学家、环境监测机构以及对 AI 预报技术感兴趣的开发者。与传统数值天气预报（NWP）模型相比，WeatherNext 在保持预报精度的同时大幅降低了计算成本，使全球范围内的高分辨率天气预报成为可能。

## 核心功能

- **全球中期大气预报**：支持 0.25° 分辨率（约 25 公里）的全球天气预报，预报时效覆盖 1 至 15 天，输出多变量、多高度的完整大气状态场。
- **热带气旋路径与强度预报**：内置专门针对气旋的预报模块，提供气旋轨迹、最大风速等关键指标的预测，可用于灾害预警和应急响应。
- **概率预报能力**：通过 GenCast 和 WN2 的集合预报机制，输出未来天气的分布信息，量化预报不确定性，为极端天气风险评估提供支撑。
- **多代模型统一接口**：在同一个 Python 框架内同时提供 GraphCast、GenCast 和 WN2 三种模型的推理与评估代码，便于横向对比和迁移研究。
- **灵活的数据接入与预处理**：内置标准化的地面实况数据与 ERA5 再分析数据处理流程，支持自定义输入数据格式，适应不同研究需求。
- **预训练权重与模型卡**：提供官方预训练模型权重下载入口和完整的模型文档，新用户可以快速启动推理而不必从零训练。

## 技术架构

WeatherNext 项目的技术核心是一系列基于图神经网络（GNN）和扩散模型的深度学习架构。WN2 模型采用了一种创新的“从边际分布学习联合概率”的方法：它首先独立预测每个变量和格点上的边际分布，然后通过一个轻量级的相关性模块恢复变量之间的空间和时间相关性，从而生成一致的联合概率预报。这种设计在保证概率校准的同时显著减少了模型的参数和推理开销。

GraphCast 作为第一代模型，使用的是编码器-处理器-解码器（Encoder-Processor-Decoder）的经典 GNN 结构，其中处理器包含多个消息传递层，在六面体网格上完成信息的空间传播。GenCast 则引入了基于扩散模型的生成式方法，将预报视为条件生成任务，能够输出多样化的未来天气样本。

代码库采用 JAX 作为主要深度学习框架，充分利用其自动微分和 XLA 编译能力实现高效的模型推理与训练。项目还提供了对 CPU、单 GPU 和多 TPU 环境的支持配置，用户可以根据自身计算资源灵活适配。数据加载部分使用 TensorFlow Dataset 或自定义的 JAX 管道，保证了海量气象数据读取的吞吐量。

## 安装与使用

项目依赖 Python 3.10+ 和 JAX 生态。首先克隆仓库并安装依赖：

```bash
git clone https://github.com/google-deepmind/weathernext.git
cd weathernext
pip install -e .
```

国内用户可通过镜像源加速安装：

```bash
pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple
```

下载预训练模型权重（以 WN2 为例）：

```bash
mkdir -p checkpoints
wget -P checkpoints/ https://storage.googleapis.com/weathernext-public/checkpoints/wn2_marginal_fgn_params
```

使用最小示例进行单步推理：

```python
from weathernext import WN2Forecaster
from weathernext.data import ERA5DataLoader

# 初始化数据加载器（需配置 ERA5 数据路径）
data_loader = ERA5DataLoader(data_path="path/to/era5")

# 加载预训练模型
model = WN2Forecaster(weights_path="checkpoints/wn2_marginal_fgn_params")

# 获取初始状态
state = data_loader.get_latest_state()

# 执行 10 天预报
forecasts = model.forecast(state, lead_time_hours=240)

# 输出特定变量的预报结果
temperature_2m = forecasts.get_variable("2m_temperature", level="surface")
```

## 适用场景

- **气象业务化预报**：气象局和商业预报机构可借助 WN2 的高精度中期预报能力，作为传统数值预报的补充或替代方案，降低超算资源投入。
- **极端灾害预警**：利用气旋路径预测和概率预报模块，政府应急部门可以在台风、寒潮等极端天气来临前更早评估风险影响范围。
- **气候与能源研究**：风电、光伏等新能源企业可通过获取高分辨率风能、辐照度等变量的概率预报，优化调度策略并评估发电量波动。
- **科研基准对比**：高校和实验室研究人员可将 WeatherNext 系列模型作为 AI 天气预报领域的先进基线，开展新算法设计与验证。

## 项目亮点

- **统一的先进模型集合**：在一个代码库中兼容三代里程碑式模型（GraphCast、GenCast、WN2），是当前开源领域覆盖最全的 AI 天气预报代码库。
- **真正意义上的概率预报**：不同于多数只输出确定性预报的模型，WN2 提供经过校准的联合概率预测，直接对接极端事件的风险量化需求。
- **超高的计算效率**：相比传统物理模式，WN2 在同分辨率下推理速度快数十至上百倍，单次全球 10 天预报仅需数分钟（GPU 环境下）。
- **官方数据服务链路**：除开源代码外，Google Cloud、WeatherLab 和 OpenMeteo 上持续提供每日更新的模型预报数据，方便无需自建模型的用户直接使用。
- **完整的评估工具链**：仓库内置与官方报告一致的评测指标和可视化脚本，便于用户复现论文中的结果并验证模型表现。

## 相关链接

- [GitHub 仓库](https://github.com/google-deepmind/weathernext)
- [Google Developers WeatherNext 指南](https://developers.google.com/weathernext/guides/models)
- [WeatherNext 气旋论文（Nature）](https://www.nature.com/articles/s41586-026-10953-2)
- [WN2 技术报告（arXiv）](https://arxiv.org/abs/2506.10772)
