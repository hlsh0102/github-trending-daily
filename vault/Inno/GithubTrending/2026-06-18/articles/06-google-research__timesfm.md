---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-06-18
language: Python
stars_total: 22095
stars_today: 606
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一个预训练时间序列基础模型，专注于时间序列预测任务。该项目基于 decoder-only 架构，旨在提供一个通用、高效的时间序列预测解决方案，可以应用于各类时间序列数据，如金融、天气、能源、物联网等领域。TimesFM 的目标用户包括数据科学家、机器学习工程师、研究人员以及需要在业务中集成时间序列预测功能的开发者。通过预训练的方式，TimesFM 能够在一定程度上泛化到未见过的数据，减少传统方法中针对每个数据集单独训练的工作量。

## 核心功能

- **通用时间序列预测**：支持多种时间跨度、频率和模式的数据，无需针对特定领域重新训练模型。
- **预训练模型**：基于大规模时间序列数据预训练，提供快速的零样本或少量样本预测能力。
- **多版本模型支持**：提供 TimesFM 1.0、2.0 和最新的 2.5 版本，用户可根据需求选择合适的模型。
- **与 Google 产品无缝集成**：支持在 BigQuery ML、Google Sheets、Vertex Model Garden 中使用，方便企业级部署。
- **开源可定制**：模型权重和代码开源，用户可以在本地或云端运行，并根据自身需求进行微调。
- **简洁的 API 接口**：提供 Python 包，几行代码即可完成预测任务。

## 技术架构

TimesFM 采用 **decoder-only 架构**，借鉴了自然语言处理中大语言模型的设计理念。该模型不依赖时序的显式周期分解或特定的数学假设，而是通过 Transformer 的注意力机制学习时间序列中的依赖关系。

模型先在大规模、多样化的时间序列数据上进行预训练，学习通用的时序模式。预训练过程使用了数据增强、掩码建模等技术，增强了模型对噪声和缺失数据的鲁棒性。推理时，用户只需提供历史数据，模型即可输出未来多步的预测值。TimesFM 的设计强调通用性，同类模型相比，它不需要用户指定季节性或趋势等参数，降低了使用门槛。

模型权重以 PyTorch 格式发布，同时支持 JAX 版本，方便在不同框架下运行。代码库结构清晰，包含模型定义、训练脚本、推理脚本以及工具函数，便于二次开发。

## 安装与使用

TimesFM 可通过 PyPI 安装，建议在 Python 3.10 及以上环境中使用：

```bash
pip install timesfm
```

如果使用最新开发版本，也可直接从 GitHub 安装：

```bash
git clone https://github.com/google-research/timesfm.git
cd timesfm
pip install -e .
```

以下是最小可用示例：

```python
import pandas as pd
import timesfm

# 加载预训练模型
model = timesfm.TimesFm(hparams=timesfm.TimesFmHparams(
    backend="cpu",  # 可选 "gpu"
    num_layers=20,
    model_dims=256,
    num_heads=8,
    per_core_batch_size=32,
), checkpoint=timesfm.TimesFmCheckpoint(
    repo_id="google/timesfm-2.0"
))

# 准备数据：假设有 512 个时间步的历史数据
data = pd.DataFrame({
    "timestamp": pd.date_range("2020-01-01", periods=512, freq="D"),
    "value": np.random.randn(512)
})

# 预测未来 96 个时间步
forecast = model.forecast(
    contexts=data["value"].values,
    freq=1,  # 每日数据
    p=96     # 预测长度
)
print(forecast)
```

该示例输出长度为 96 的预测数组。用户可根据实际数据调整输入长度、预测长度和时间间隔。

## 适用场景

- **业务预测与规划**：企业可根据历史销售、库存或流量数据，预测未来趋势，用于库存管理、人员排班和市场策略制定。
- **金融时间序列分析**：预测股票价格、交易量、汇率变化等，辅助投资决策和风险管理。
- **物联网与传感器监测**：对工业设备、环境传感器采集的数据进行异常与趋势预测，实现预测性维护和实时监控。
- **能源与天气预测**：预测可再生能源发电量、电力负荷、气温变化等，支持智能电网和气候分析。

## 项目亮点

- **零样本预测能力**：无需针对每个新数据集重新训练模型，开箱即用，大幅降低时间序列预测的成本和复杂度。
- **decoder-only 架构**：在时间序列领域引入了 NLP 中最先进的架构设计，模型具备长依赖捕捉能力。
- **Google 生态集成**：可直接在 BigQuery、Google Sheets 和 Vertex AI 等产品中使用，适合企业级架构。
- **多版本支持**：从 1.0 到 2.5，模型性能逐步提升，用户可以根据性能和资源需求灵活选择。
- **活跃维护与社区**：项目在 GitHub 上拥有超过 2.2 万星标，持续更新，有大量用户讨论和贡献。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [论文：A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688)
- [模型权重下载（Hugging Face）](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
- [Google Research 博客介绍](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
