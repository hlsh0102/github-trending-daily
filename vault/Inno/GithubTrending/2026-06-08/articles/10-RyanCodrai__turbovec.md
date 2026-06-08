---
tags:
  - trending
  - article
repo: RyanCodrai/turbovec
date: 2026-06-08
language: Python
stars_total: 7568
stars_today: 1554
---
## 项目概述

turbovec 是一个基于 Google Research TurboQuant 算法构建的高性能向量索引库。它用 Rust 编写，并提供了 Python 绑定，旨在解决大规模向量检索场景下的内存占用和搜索效率问题。传统上，一个 1000 万文档的语料库以 float32 格式存储需要 31 GB 内存，而 turbovec 仅需 4 GB 即可容纳，且搜索速度超过 FAISS。该项目面向需要处理大规模向量数据的开发者，尤其是从事推荐系统、语义搜索、图像检索等领域的工程师和研究人员。

## 核心功能

- **在线增量索引**：支持动态添加向量，无需预训练或重建索引。向量加入后立即可用，corpus 增长时无需重写整个索引结构。
- **远超 FAISS 的搜索性能**：通过手写的 NEON（ARM 架构）和 AVX-512BW（x86 架构）内核，在 ARM 上比 FAISS IndexPQFastScan 快 12–20%，在 x86 上持平或更优。
- **实时搜索过滤**：支持在搜索时传入 id 白名单或槽位位掩码，内核直接对结果进行过滤，无需后处理。
- **无需训练的数据无偏量化**：TurboQuant 算法基于数据无偏量化器，不需要额外的训练阶段或码本学习，开箱即用。
- **极低的内存占比**：相比 float32 原始存储，压缩比可达 8x 左右，大幅降低内存资源需求。
- **多架构原生优化**：针对 ARM NEON 和 x86 AVX-512BW 进行了底层指令级优化，充分利用硬件特性。

## 技术架构

turbovec 的核心是 TurboQuant 量化算法，这是一种数据无偏的量化方法，能够在理论上接近香农失真下界。与传统的乘积量化（PQ）算法不同，TurboQuant 不需要独立的训练阶段来学习码本——它对所有数据点应用统一的量化规则，因此向量可以随时被添加和索引，无需增量更新模型。传统 PQ 方法通常需要在一个训练集上学习码本，然后对所有向量使用该码本进行压缩，如果向量分布发生变化则需要重新学习码本；而 TurboQuant 的“训练-free”特性使其特别适合流式或动态增长的场景。

在搜索时，turbovec 使用了手写的 SIMD 内核来加速距离计算。对于 ARM 设备，它利用 NEON 指令集；对于 x86 设备，则充分利用 AVX-512BW。这些内核经过精心优化，能够并行处理多个向量与查询的距离计算，并通过位操作实现高效的过滤功能。过滤逻辑被直接嵌入到内核中，而不是在搜索完成后进行后过滤，从而减少了不必要的计算开销。

整个索引结构基于 Rust 实现，保证了内存安全和并发性能。Python 绑定通过 PyO3 提供，使得 Python 用户可以无缝调用底层 Rust 实现，同时享受 Rust 的高性能和零开销抽象。

## 安装与使用

安装 turbovec 非常简单，可以通过 pip 直接安装：

```bash
pip install turbovec
```

对于 Rust 用户，可以通过 crates.io 安装：

```bash
cargo add turbovec
```

以下是 Python 的最小可用示例：

```python
import numpy as np
from turbovec import TurboVecIndex

# 创建一个索引，指定向量维度（例如 128 维）
index = TurboVecIndex(dim=128)

# 添加一批向量，每个向量的形状为 (1, 128)
vectors = np.random.randn(1000, 128).astype(np.float32)
index.add(vectors)

# 搜索最相似的 10 个向量
query = np.random.randn(128).astype(np.float32)
results = index.search(query, top_k=10)

# results 包含 (ids, distances) 两个数组
print(results.ids)      # 返回最相似的向量 id
print(results.distances) # 返回对应的距离
```

如果需要过滤，可以在搜索时传入允许的 id：

```python
allowed_ids = list(range(500))  # 只搜索前 500 个向量
filtered_results = index.search(query, top_k=10, allowlist=allowed_ids)
```

## 适用场景

- **大规模语义搜索**：在文档检索或问答系统中，需要对海量嵌入向量进行快速最近邻搜索。turbovec 的低内存占用使得在单台服务器上即可处理千万级语料库。
- **推荐系统**：实时推荐系统需要根据用户请求动态计算相似物品。turbovec 的在线增量索引特性允许在系统运行中持续添加新物品，无需中断服务。
- **图像与视频检索**：使用卷积神经网络提取的图像特征通常为 float32 的高维向量。turbovec 的压缩能力可以显著降低存储成本，同时保持高搜索速度。
- **嵌入式设备或边缘计算**：手写的 ARM NEON 内核使得 turbovec 在树莓派等 ARM 设备上也能发挥出色性能，适合资源受限但需要本地向量搜索的场景。

## 项目亮点

turbovec 相较于同类项目（如 FAISS、Annoy、HNSWlib等）的差异化优势在于：

1. **零训练成本**：TurboQuant 是数据无偏的，无需额外的训练阶段或码本学习，而 FAISS 的 PQ 变体通常需要预处理来学习码本。这使得 turbovec 特别适合流式或动态变化的数据场景。
2. **内置的高效过滤**：过滤逻辑被嵌入到 SIMD 内核中，而不是在搜索完成后进行后过滤，这在大数据集上可以显著减少不必要的距离计算。
3. **跨平台 SIMD 优化**：同时支持 ARM NEON 和 x86 AVX-512BW，覆盖主流硬件平台，且在不同平台上都提供了接近硬件极限的性能。
4. **近乎理论最优的压缩比**：TurboQuant 算法在数学上接近香农失真下界，这意味着同样的精度下，turbovec 的压缩比优于大多数 PQ 变体。
5. **Rust 内核 + Python 接口**：既保证了核心性能和安全，又降低了使用门槛，让数据科学家也能轻松调用。

## 相关链接

- [GitHub 仓库](https://github.com/RyanCodrai/turbovec)
- [PyPI 包](https://pypi.org/project/turbovec/)
- [crates.io 包](https://crates.io/crates/turbovec)
- [TurboQuant 论文](https://arxiv.org/abs/2504.19874)
