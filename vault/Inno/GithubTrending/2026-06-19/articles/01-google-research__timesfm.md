---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-06-19
language: Python
stars_total: 23532
stars_today: 844
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一款预训练时序基础模型，专为时间序列预测任务设计。该项目旨在提供一种通用、高效的预测能力，能够处理多种时间序列数据类型，如零售销售、能源消耗、金融指标等。TimesFM 不依赖领域特定的特征工程，而是通过预训练学习时间序列的通用模式，使开发者能够以最小的配置快速获得可靠的预测结果。

目标用户包括数据科学家、机器学习工程师，以及任何需要时间序列预测能力的从业者。无论是构建内部预测系统，还是集成到商业分析工具中，TimesFM 都提供了一种开箱即用的解决方案。该模型在 ICML 2024 上发表，并已在 Google 的 BigQuery ML、Google Sheets 和 Vertex Model Garden 等产品中得到应用。

## 核心功能

- **通用时间序列预测**：支持单变量和多变量时间序列的预测，能够处理从小时级到月级的不同时间频率。
- **预训练基础模型**：基于大规模时序数据预训练，无需针对每个任务重新训练，大幅降低使用门槛。
- **多种输入与输出支持**：接受历史数据窗口作为输入，输出指定长度（如 128 个时间步）的未来预测值。
- **频率自适应**：自动检测时间序列的采样频率（如每天、每小时），并相应调整模型内部处理逻辑。
- **概率预测能力**：支持输出预测区间（如分位数或置信区间），为风险管理提供更多信息。
- **批量推理与部署**：支持批量预测，并可通过 PyPI 安装或使用预构建的 Docker 镜像快速部署。

## 技术架构

TimesFM 采用**解码器仅结构**（decoder-only architecture），这一设计借鉴了大语言模型（LLM）的成功经验，但针对时间序列数据进行了专门优化。模型以时间序列的 patch 化表示作为输入，而不是原始的逐点数据，这有助于捕捉局部和全局的时序依赖。

核心设计思路是：将时间序列视为一种特殊类型的语言，通过自回归方式预测未来值。与传统的循环神经网络（RNN）或 Transformer 编码器-解码器结构不同，TimesFM 仅使用解码器，通过因果注意力机制确保每个预测值只依赖于过去的信息。

关键技术要点：
- **Patch 化输入**：将连续的时间步划分成固定大小的 patches，每个 patch 作为一个 token 输入。这种方式既降低了计算复杂度，又增强了模型对局部模式的感知。
- **位置编码**：使用可学习的位置编码来保留时间顺序信息，支持任意长度的输入窗口。
- **多频率预训练**：模型在多个不同采样频率的数据集上预训练，包括零售、金融、气象等领域，因此能泛化到未见过的数据类型和频率。
- **可扩展性**：模型参数规模适中（如百万级），可以在单 GPU 甚至 CPU 上进行推理，同时支持通过数据并行进一步加速。

架构特点使其在预测准确性、推理速度和泛化能力之间取得了良好平衡。

## 安装与使用

TimesFM 可通过 PyPI 安装，需要 Python 3.10 或更高版本。以下是最小可用示例：

```bash
# 安装最新版本
pip install timesfm
```

基本使用示例：

```python
import timesfm
import numpy as np

# 加载预训练模型（使用最新的 2.5 版本）
tfm = timesfm.TimesFm(
    context_len=512,        # 输入历史窗口长度
    horizon_len=128,        # 预测未来步数
    backend="cpu",          # 可选 "cpu" 或 "gpu"
    model_params="2.5",     # 模型版本
)

# 准备输入数据：形状为 (batch_size, context_len) 的 numpy 数组
# 注意：数据应经过归一化（如减去均值除以标准差）
input_data = np.random.randn(10, 512)  # 10 个样本

# 执行预测
forecasts = tfm.forecast(input_data)
# forecasts 的形状为 (10, 128)，包含每个样本的预测值
```

如果需要概率预测，可以添加 `quantiles` 参数：

```python
forecasts_with_quantiles = tfm.forecast(input_data, quantiles=[0.1, 0.5, 0.9])
```

更详细的用法请参照 GitHub 仓库中的文档和示例 notebook。

## 适用场景

- **零售与供应链预测**：预测产品销售、库存需求或季节性波动，帮助优化库存管理和采购计划。
- **能源与资源管理**：预测电力负载、可再生能源输出（如太阳能、风能）或用水量，支持调度和定价决策。
- **金融与市场分析**：预测资产价格、交易量或宏观经济指标，辅助投资策略和风险评估。
- **运维与监控**：预测系统资源使用率（如 CPU、内存）、网络流量或设备故障率，用于容量规划与预警。

## 项目亮点

- **预训练优势**：与从头训练的传统方法相比，TimesFM 通过大规模预训练直接提供高质量基线，多数场景下可减少 80% 以上的训练数据需求。
- **易用性与集成度**：通过 PyPI 一行安装即可使用，且已集成到 Google BigQuery ML 和 Google Sheets 等产品，方便非技术用户通过 SQL 或电子表格操作。
- **学术严谨性**：在顶级会议 ICML 2024 上发表，具备公开论文和可复现的实验结果，技术透明性高。
- **社区活跃**：GitHub 仓库拥有超过 2.3 万颗星，社区贡献和问题讨论活跃，版本迭代迅速。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [论文：A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688)
- [Hugging Face 模型检查点集合](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
- [Google Research 博客文章](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
