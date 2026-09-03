---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-09-03
language: Python
stars_total: 30239
stars_today: 343
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一款预训练时间序列基础模型，专注于时间序列预测任务。该模型采用 decoder-only 架构，在大规模时间序列语料上进行预训练，能够以零样本或少样本的方式完成多种时间序列预测任务。

传统时间序列预测通常需要针对特定数据集训练专门模型，不仅成本高昂，而且泛化能力有限。TimesFM 试图借鉴 NLP 和 CV 领域基础模型的成功经验，通过在大规模、多样化的时间序列数据上进行预训练，使模型学到通用的时间序列模式与结构，从而在面对新数据集时无需微调即可获得良好的预测效果。该项目面向数据科学家、机器学习工程师以及任何需要时间序列预测能力的研究者或开发者。

目前 TimesFM 已迭代至 3.0 版本（`google/timesfm-3.0-pytorch`），前代版本（1.0、2.0、2.5）的代码与权重也一并开放，便于研究者复现与对比。

## 核心功能

- **零样本预测能力**：TimesFM 在预训练后，可直接用于未见过的数据集，无需针对特定数据集进行微调，大幅降低了时间序列建模的入门门槛。
- **灵活预测时长**：支持从短期的几步预测到长达数月或数年的长期预测，用户可根据业务需求任意指定预测长度。
- **多粒度支持**：模型可处理分钟、小时、天、周、月等不同频率的时间序列，提供了统一的预测框架。
- **预训练与微调双重模式**：既支持直接加载预训练权重进行零样本预测，也支持在特定数据集上做进一步微调以提升效果。
- **轻量开源实现**：提供完整的 PyTorch 实现代码与模型权重，模型体积远小于同类大型模型，可在单张 GPU 或纯 CPU 环境下运行。
- **与 Google 生态集成**：已上线 BigQuery ML 与 Google Sheets，支持通过 SQL 或电子表格直接触发预测，另提供 Vertex Model Garden 的 Docker 化端点用于 Agent 调用。

## 技术架构

TimesFM 的设计灵感来自大型语言模型（LLM）。其核心是一个基于 decoder-only Transformer 的时序预测模型，将时间序列按固定窗口切分为 patch 后输入网络，通过自回归方式逐步生成未来时段的预测值。

相比传统的 RNN、TCN 或基于矩阵分解的方法，使用 decoder-only Transformer 的核心优势在于：模型能够利用海量数据和超大规模参数进行预训练，在预训练阶段接触了来自金融、能源、交通、Web 流量、气象等多个领域的时序数据，从而学到跨领域的通用时序演化规律。这也是 TimesFM 能够实现零样本预测的基础。

在模型尺寸方面，TimesFM 提供 200M（2.0 版本）和 480M（3.0 版本）两档参数规模。对于时间序列预测任务而言，这属于中等规模，使得模型可以在常规 GPU（甚至 16GB 显存）上完成推理。代码基于 PyTorch 框架，结构清晰，便于二次开发与定制。整个训练与推理流程可通过项目自带的脚本或基于 Hugging Face Transformers 的标准接口驱动。

## 安装与使用

TimesFM 的 Python 包可通过 pip 直接安装：

```bash
pip install timesfm
```

模型权重则通过 Hugging Face 下载，以 PyTorch 版本（3.0）为例：

```python
import timesfm

tfm = timesfm.TimesFm(
    hparams=timesfm.TimesFmHparams(
        backend="gpu",
        per_core_batch_size=32,
        horizon_len=128,
        num_layers=50,
        use_positional_embedding=False,
    ),
    checkpoint=timesfm.TimesFmCheckpoint(
        huggingface_repo_id="google/timesfm-3.0-pytorch",
    ),
)
tfm.load_from_checkpoint()
```

加载完成后即可对任意 pandas DataFrame 格式的历史数据进行预测。基本输入格式为包含 `timestamp` 列和至少一个数值 `series` 列的表结构。通过构造 `forecast_inputs` 字典，调用 `tfm.forecast()` 即可返回未来时段的预测值。对于多种频率的数据，可通过 `frequency_input` 参数（如 `0` 代表高频，`1` 代表日频，`2` 代表低频）显式指定。

完整的示例代码可参考仓库 `timesfm/examples/basic_forecast_timesfm3.ipynb` 笔记本。

## 适用场景

- **多领域零样本预测**：金融时序（股价、营收）、能源负荷、零售销量、气候指标等。由于无需针对每个新数据集重新训练模型，特别适合企业快速上线预测功能，或作为基线模型与新训练的专属模型进行比较。
- **自动化预测服务与 Agent 集成**：TimesFM 已与 BigQuery ML、Google Sheets 深度集成，可借助 SQL 完成大规模并行预测。在 Vertex Model Garden 中提供 Docker 化服务，可无缝嵌入 Agent 调用链，快速构建自动化预测与决策流程。
- **概念验证与科研基线**：对于研究团队，可快速复现论文实验，或以此为零样本基线与新提出的模型对比，验证创新点的实际增益。

## 项目亮点

- **开源且预训练即用**：Google Research 完全开源了模型代码与全部预训练权重（Apache-2.0），用户无需自行训练即可立即使用，这在同类规模的基础模型中极为少见。
- **扎实的学术与工程背书**：论文发表于 ICML 2024，方法经过严格的学术同行评审。同时模型已在 Google 一线产品（BigQuery、Sheets）中大规模服务，工程稳健性得到验证。
- **版本迭代速度快**：从 1.0 到 3.0，模型在预测精度、推理速度与上下文长度上持续改进。3.0 版本将参数量提升至 480M，并重点优化了对更长时间上下文的利用，以支持更长周期的预测。
- **链接生态完善**：Hugging Face 上提供了完整的模型集合与检查点，配合 Python 包可在一行代码内完成模型加载与预测；官方同时提供了与 Vertex AI 和 Sheets 的接口案例，极大降低了从原型到落地的成本。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [论文（arXiv）](https://arxiv.org/abs/2310.10688)
- [TimesFM 3.0 Checkpoint（Hugging Face）](https://huggingface.co/google/timesfm-3.0-pytorch)
- [TimesFM Hugging Face Collection](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
- [Google Research Blog](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
- [BigQuery ML 文档](https://cloud.google.com/bigquery/docs/timesfm-model)
- [Google Sheets 集成公告](https://workspaceupdates.googleblog.com/2026/02/forecast-data-in-connected-sheets-BigQueryML-TimesFM.html)
