---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-06-20
language: Python
stars_total: 24162
stars_today: 1510
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一个预训练时间序列基础模型，专门用于时间序列预测任务。该项目旨在将大语言模型（LLM）的成功经验迁移到时间序列领域，通过海量数据预训练一个通用的预测模型，使得用户无需针对每个特定场景重新训练模型，即可获得高质量的时间序列预测结果。

该项目的核心创新在于提出了一种纯解码器架构的预训练时间序列模型，相关工作于 ICML 2024 发表。TimesFM 的目标用户包括数据科学家、机器学习工程师以及在金融、能源、零售、气象等领域需要时间序列预测能力的开发者和研究人员。目前，TimesFM 已集成到 Google 的 BigQuery ML、Google Sheets 和 Vertex Model Garden 等产品中，为企业级应用提供了便捷的访问途径。

最新模型版本为 TimesFM 2.5，此前 1.0 和 2.0 版本的代码已归档至 v1 子目录。

## 核心功能

- **零样本预测**：无需针对特定数据集进行微调，预训练模型可直接用于多种时间序列预测场景，显著降低使用门槛和计算成本。
- **多尺度预测能力**：支持从短到长不同时间跨度的预测需求，能够灵活适配各种业务场景中的预测时间范围。
- **灵活输入长度**：可接受任意长度的历史时间序列作为输入，不需要固定窗口大小，增强了实际应用的灵活性。
- **概率预测输出**：不仅提供点预测值，还能输出预测的置信区间和概率分布，为风险敏感场景提供更多信息。
- **多频率支持**：可处理小时级、日级、周级、月级等不同频率的时间序列数据，适应多样化的数据采集节奏。
- **Hugging Face 模型集成**：模型权重和完整检查点已在 Hugging Face 平台发布，方便社区直接加载使用。

## 技术架构

TimesFM 采用了纯解码器（decoder-only）的 Transformer 架构，这一设计灵感来源于 GPT 等大语言模型。与传统的编码器-解码器架构或基于 RNN 的模型不同，TimesFM 将时间序列 patches 视为类似语言模型中的 token，通过自注意力机制捕获时间依赖关系。

模型的核心设计思路包括以下几个关键点：
1. **Patch 化处理**：将连续的时间序列切分为固定长度的 patches，每个 patch 作为模型的基本处理单元，有效减少序列长度，降低计算复杂度。
2. **预训练策略**：在海量真实世界的时间序列数据上进行预训练，涵盖金融、气象、交通等多个领域，使模型学习到通用的时间模式。
3. **解码器结构**：采用因果掩码（causal masking）确保模型在预测时只能使用历史信息，符合时间序列预测的基本要求。
4. **相对位置编码**：使用旋转位置编码（RoPE）或类似机制，使模型能够感知时间序列中的时间顺序关系。

这种架构设计使得 TimesFM 在保持计算效率的同时，能够处理复杂的时序依赖，并且天然支持可变长度的输入输出。

## 安装与使用

通过 PyPI 安装最新版本：

```bash
pip install timesfm
# 若需旧版本（如 1.3.0）可安装：pip install timesfm==1.3.0
```

最小使用示例：

```python
import timesfm
import numpy as np

# 1. 初始化模型
tfm = timesfm.TimesFm(
    hparams=timesfm.TimesFmHparams(
        backend="cpu",  # 或 "gpu"
        per_core_batch_size=32,
    ),
    checkpoint=timesfm.TimesFmCheckpoint(
        huggingface_repo_id="google/timesfm-2.5-200m",  # 从 Hugging Face 加载
    ),
)

# 2. 准备输入数据（示例：100 个时间点的单变量时间序列）
input_ts = np.random.randn(100)  # 形状: (T,)

# 3. 执行预测（预测后续 20 个时间点）
forecast = tfm.forecast(
    inputs=[input_ts],  # 支持多序列输入
    freq_hours=24,      # 数据频率（小时）
    forecast_length=20, # 预测长度
)

predictions = forecast[0].mean  # 点预测值
# predictions.shape: (20,)
```

更详细的使用说明和 API 文档，请参考 GitHub 仓库中的 README 和示例代码。

## 适用场景

- **零售与供应链预测**：利用历史销售数据预测未来需求，优化库存管理和物流调度，减少缺货或库存积压风险。
- **金融时间序列分析**：对股票价格、交易量、利率等金融指标进行短期和中期波动预测，辅助投资决策和风险评估。
- **能源与资源规划**：预测电力负荷、可再生能源发电量（如太阳能、风能）、水消耗量等，支持电网调度和资源分配。
- **物联网与监控领域**：预测传感器数据变化趋势，提前发现设备异常或系统故障，实现主动维护和预警。

## 项目亮点

- **真正的预训练基础模型**：不同于传统方法需要针对每个数据集从头训练，TimesFM 的零样本预测能力大幅降低了实际应用中的计算资源和时间成本。
- **Google 级海量数据预训练**：模型在多领域、大规模真实数据上预训练，泛化能力远超市面上多数开源时间序列模型。
- **产品级集成**：已集成到 BigQuery ML、Google Sheets 等 Google 主打产品中，证明了其企业级的可靠性和实用性。
- **高精度与可解释性结合**：在保持高预测精度的同时，提供概率输出和置信区间，帮助用户理解预测的不确定性。
- **活跃的社区与持续更新**：作为开源项目，TimesFM 拥有活跃的社区支持，迭代速度快（已更新至 2.5 版本），且完全基于 Apache-2.0 许可协议。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [论文：A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688)
- [Hugging Face 模型集合](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
- [Google Research 博客](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
