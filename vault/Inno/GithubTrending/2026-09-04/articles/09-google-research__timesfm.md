---
tags:
  - trending
  - article
repo: google-research/timesfm
date: 2026-09-04
language: Python
stars_total: 30811
stars_today: 1618
---
## 项目概述

TimesFM（Time Series Foundation Model）是由 Google Research 开发的一款预训练时间序列基础模型，专为时间序列预测任务设计。该模型的核心创新在于采用 decoder-only 架构，将时间序列预测问题统一建模为下一个时间点的预测任务，从而在大规模异构时间序列数据上学习到通用的时序模式。

TimesFM 解决了传统时间序列预测方法长期面临的泛化能力不足问题。以往的时间序列预测模型通常针对特定数据集或特定领域进行训练和调优，迁移到新场景时需要重新训练。TimesFM 通过在大规模时间序列语料上进行预训练，形成了一种类 ChatGPT 的基础模型能力——用户可以直接对未见过的数据集进行预测，无需任何微调即可获得良好的预测结果。其相关论文发表于 ICML 2024，题名为《A decoder-only foundation model for time-series forecasting》。

该项目主要面向数据科学家、机器学习工程师以及需要处理时间序列预测任务的研究人员。截至当前，TimesFM 在 GitHub 上已收获超过 3 万颗星标，是目前最受关注的时间序列基础模型之一。

## 核心功能

- **零样本预测**：TimesFM 支持在不进行任何微调的情况下直接对新的时间序列数据进行预测，具备跨领域的强泛化能力，覆盖金融、零售、能源、交通等多个领域。
- **多样化的频率支持**：模型能处理从分钟级到年级的多种时间粒度数据，适应不同业务场景的需求。
- **灵活的预测长度**：TimesFM 3.0 支持最长 512 个时间点的预测长度（2.0 之前版本为 256 点），且输入长度可根据实际数据进行调整，并不强制要求固定长度。
- **协变量支持**：支持未来已知协变量（如天气、节假日、促销日历等）作为额外特征输入，进一步提升预测精度；同时也支持静态协变量描述时间序列的固有属性。
- **概率预测输出**：模型可输出预测值的分布信息（包括分位数预测），而非仅提供点估计，为 决策者提供不确定性估计。
- **多版本模型权重**：官方提供 1.0、2.0、2.5 以及最新的 3.0 共多个 PyTorch 格式的预训练权重，用户可根据精度和资源需求选择合适的版本。

## 技术架构

TimesFM 的技术核心参考了大语言模型（LLM）的成功经验，设计为基于 Transformer 的 decoder-only 架构。具体地：

- **输入 Patch 化**：TimesFM 将输入的时间序列切分为固定长度的 patch（例如 32 个时间点为一个 patch），每个 patch 通过残差连接映射为 token 嵌入向量。这一设计大幅降低了 token 序列长度，从而减少了自注意力机制的计算复杂度。
- **Decoder-only 架构**：模型仅包含因果自注意力层，约束每个 token 只能参考其之前的历史 token。在推理阶段，模型以自回归方式逐个预测后续 patch，这与 GPT 系列的文本生成方式相吻合。
- **多分辨率预训练**：TimesFM 采用了多分辨率（multi-resolution）预训练策略——对不同时间频率的数据采用不同的 patch 长度进行 tokenization，从而使模型能同时学习从微观到宏观不同尺度的时序模式。该策略显著提升了模型跨频率的泛化能力。
- **蒸馏训练**：TimesFM 3.0 的训练采用知识蒸馏技术，利用大模型在长序列（如 4096 点）上的预测能力来监督小模型在短序列上的预测，使最终开源模型兼具高性能和较低推理成本。
- **灵活的位置编码**：模型能够应对任意长度的输入，通过调整开始位置的 token 编码来应对位移后的时间序列，训练数据覆盖丰富的长程周期模式。

整体上，TimesFM 的设计思路是尽可能复用 LLM 的成功技术（patch tokenization、decoder-only、自回归生成），但针对时间序列预测任务的特殊性做了诸多适配（多分辨率 tokenization、灵活性等），使其成为一个真正意义上跨领域可用的时序基础模型。

## 安装与使用

TimesFM 以 Python 包形式发布，支持通过 pip 直接安装，也可从源码构建。在使用前需要先准备 Python 3.10 及以上环境，并安装 PyTorch（2.0 以上版本）。

**安装步骤**：

```bash
# 创建虚拟环境（推荐）
python3 -m venv timesfm_env
source timesfm_env/bin/activate

# 安装 PyTorch（以 CUDA 12.1 为例，其他配置请参考 PyTorch 官网）
pip install torch --index-url https://download.pytorch.org/whl/cu121

# 从 PyPI 安装 TimesFM
pip install timesfm
```

**最小可用示例**（零样本预测）：

```python
import timesfm

# 1. 加载模型（首次运行会从 Hugging Face 自动下载权重）
tfm = timesfm.TimesFm(
    hparams=timesfm.TimesFmHparams(
        backend="gpu",          # 可选 "cpu"
        per_core_batch_size=32,
        horizon_len=128,        # 预测未来 128 个点
        num_layers=50,          # 对应 3.0 版本模型规格
        model_dims=1280,
        backend="gpu",
    ),
    checkpoint=timesfm.TimesFmCheckpoint(
        huggingface_repo_id="google/timesfm-3.0-pytorch",
    ),
)
tfm.load_from_checkpoint()

# 2. 准备输入数据（batch, time 维）
import numpy as np
frequency_input = [0, 1, 2]  # 0: 分钟级, 1: 小时级, 2: 日级, 3: 周级, 4: 月级, 5: 年级
context = np.random.randn(3, 512)   # 3条序列，每条512个历史点

# 3. 执行预测
point_forecast, quantile_forecast = tfm.forecast(
    context,
    freq=frequency_input,
)
print(point_forecast.shape)  # (3, 128)
```

## 适用场景

- **零售与电商需求预测**：基于历史销售数据预测未来日/周/月销量，用于库存优化与补货计划。TimesFM 可同时处理数千个 SKU（库存量单位）的独立时间序列，实现大规模并行预测。
- **云资源与容量规划**：对服务器负载、网络流量、存储消耗等多指标时间序列进行前瞻性预测，帮助运维团队提前配置资源。
- **金融时序分析**：对宏观经济指标、交易频率、市场波动率等金融时序数据进行快速预判，辅助策略研究或风控模型。

## 项目亮点

- **真正的零样本能力**：与大多数需要在目标数据上重新训练的方法不同，TimesFM 具有开箱即用的能力，在下游任务（如 Monash 基准）上以零样本方式超越了众多有监督训练的专用模型。
- **高效的架构设计**：patch-based tokenization 使模型的 self-attention 层数（50 层）不需要像 LLM 那样处理极长的序列，3.0 版本在维持 SOTA 精度的同时实现了高效长时预测。
- **多分辨率覆盖**：无需针对不同频率（分钟/小时/日/月/年）分别训练模型，同一个模型即可覆盖这些场景，显著降低了模型运维的复杂度。
- **生态与集成**：TimesFM 已无缝集成到 Google BigQuery ML、Vertex Model Garden 以及 Google Sheets 连接器，用户可以直接通过 SQL 或电子表格调用其预测能力，降低了使用门槛。
- **开源性**：模型权重与代码均以 Apache-2.0 许可发布，允许广泛商业应用和二次开发。

## 相关链接

- [GitHub 仓库](https://github.com/google-research/timesfm)
- [论文地址](https://arxiv.org/abs/2310.10688)
- [Google Research 博客](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
- [TimesFM Hugging Face 模型集合](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)
