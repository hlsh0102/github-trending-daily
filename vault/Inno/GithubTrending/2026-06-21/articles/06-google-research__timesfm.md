---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-06-21
language: Python
stars_total: 24642
stars_today: 433
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一个预训练时间序列基础模型，专门用于时间序列预测任务。该项目基于论文《A decoder-only foundation model for time-series forecasting》（ICML 2024）的研究成果，将大规模预训练技术引入时间序列领域，解决了传统时间序列模型需要针对每个数据集单独训练、泛化能力有限的问题。目标用户包括数据科学家、机器学习工程师、金融分析师、供应链规划人员以及任何需要进行时间序列预测的开发者和研究者。当前最新模型版本为 TimesFM 2.5，开源版本非 Google 官方产品。

## 核心功能

- **通用时间序列预测**：支持单变量和多变量时间序列的未来值预测，无需针对特定数据集微调模型。
- **多尺度预测能力**：模型内置了在不同时间粒度（如小时、天、周、月）上的预测能力，适应不同场景需求。
- **零样本预测**：预训练模型可以直接应用于新领域的时间序列数据，无需重新训练或大量标注数据。
- **概率预测输出**：提供预测分位数，支持不确定性量化，帮助用户评估预测可靠程度。
- **灵活的输入长度**：支持任意长度的历史数据输入，自动适配模型内部处理机制。
- **与 Google 生态集成**：可直接通过 BigQuery ML、Google Sheets、Vertex Model Garden 等产品使用，支持 SQL 查询级别调用和 Docker 化部署。

## 技术架构

TimesFM 基于 **decoder-only transformer 架构**设计，这一选择借鉴了大型语言模型（LLM）的成功经验。模型将时间序列数据切分为等长的 patch（补丁），每个 patch 作为基础输入单元送入 transformer 的 decoder 层。网络通过自注意力机制学习时间序列中的长期依赖关系和模式，然后直接输出未来多个时间步的预测值。训练阶段，模型在大量异构公开时间序列数据集上进行预训练，涵盖金融、能源、交通、天气等多个领域，从而学习到跨领域的时序模式表示。推理时，模型采用自回归方式逐步生成预测，同时通过预设的分位数输出概率分布。这一架构设计的核心优势是：减少了对领域特定特征工程的依赖，同时保持了 transformer 的可扩展性和表达能力。

## 安装与使用

TimesFM 支持通过 PyPI 安装，当前版本为 `timesfm=2.0.0`。建议使用 Python 3.10 以上版本。

**安装命令：**
```bash
pip install timesfm==2.0.0
```

**最小可用示例：** 加载预训练模型并对简单序列进行预测。
```python
import timesfm

# 加载预训练模型（自动下载 checkpoint）
model = timesfm.TimesFm(
    backend="cpu",  # 或 "gpu"
    context_len=512,
    horizon_len=96,
)

# 准备输入数据（示例：单变量，输入长度为 512 的时间序列）
import numpy as np
input_ts = np.random.randn(1, 512)  # batch_size=1, time_steps=512

# 进行预测
forecast = model.forecast(input_ts)
print(forecast.shape)  # (1, 96) 预测未来 96 个时间步
```

对于多变量预测或多序列批量预测，可将输入扩展为相应形状。具体 API 细节可参阅 GitHub 仓库中的示例笔记本。

## 适用场景

- **金融时间序列预测**：如股票价格波动、汇率变化、交易量预测，利用模型零样本能力快速适应不同资产类型。
- **能源负载与需求预测**：电力负荷、可再生能源发电量预测，支持小时级精度调度规划。
- **零售与供应链预测**：商品销量、库存需求、物流流量预测，支持季节性模式捕捉。
- **运维与异常检测**：设备传感器数据预测，通过预测偏差识别潜在故障点。

## 项目亮点

TimesFM 的突出优势在于其 **预训练基础模型范式** 在时间序列领域的前沿应用。与传统时间序列模型（如 ARIMA、Prophet）相比，它无需针对每个新场景进行模型选择和调参；与深度学习方法相比，它减少了大量数据标注和训练成本。模型在多个公开基准测试上达到了领先的零样本预测性能，尤其在跨领域迁移时表现稳定。此外，Google 将其集成进 BigQuery ML 和 Google Sheets 等产品，降低了使用门槛，允许数据分析师通过 SQL 或电子表格式界面直接调用前沿预测能力。开源版本同样保持了完整的预测接口和 checkpoint 支持，便于开发者集成到自定义工作流中。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [Hugging Face 模型集合](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
- [研究论文](https://arxiv.org/abs/2310.10688)
- [Google Research 博客](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
