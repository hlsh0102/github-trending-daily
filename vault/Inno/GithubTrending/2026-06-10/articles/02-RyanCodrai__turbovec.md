---
tags:
  - trending
  - article
repo: RyanCodrai/turbovec
date: 2026-06-10
language: Python
stars_total: 10418
stars_today: 1801
---
## 项目概述

turbovec 是一个基于 Google Research 的 TurboQuant 算法构建的高性能向量索引库，使用 Rust 编写并提供 Python 绑定。它解决了传统向量索引在大规模数据集上内存占用高、索引构建复杂、搜索速度慢的问题。目标用户包括机器学习工程师、数据科学家、推荐系统开发者以及任何需要在大规模向量数据上进行高效相似性搜索的技术人员。

与传统方案相比，turbovec 能够以极低的内存成本实现高性能搜索：一个包含 1000 万文档的语料库，在 float32 格式下需要 31 GB 内存，而 turbovec 仅需 4 GB，并且搜索速度超过 FAISS。

## 核心功能

- **在线增量索引**：向量可以直接添加，无需独立的训练阶段或参数调优。随着语料库增长，索引自动扩展，无需重建。
- **超越 FAISS 的搜索性能**：通过手工优化的 NEON（ARM）和 AVX-512BW（x86）内核，在 ARM 架构上比 FAISS IndexPQFastScan 快 12–20%，在 x86 架构上与之持平或更优。
- **搜索时过滤**：支持在 `search()` 方法中传入 ID 白名单或槽位掩码（slot bitmask），内核直接在量化域内执行过滤，避免后过滤开销。
- **数据无偏量化（Data-Oblivious Quantization）**：无需码本训练，无需训练数据，量化器在理论失真下界附近运行，接近香农下界。
- **内存高效**：通常可将内存占用压缩至原始 float32 的十分之一甚至更低，同时保持高召回率。
- **跨平台支持**：通过 Rust 实现核心算法，并通过 PyO3 提供 Python 绑定，支持 Linux、macOS 和 Windows。

## 技术架构

turbovec 的核心技术栈围绕 TurboQuant 算法设计。TurboQuant 是一种数据无偏量化器（data-oblivious quantizer），它无需像 PQ（乘积量化）那样对数据进行聚类训练码本，而是通过数学变换将高维向量映射到低失真子空间。这消除了传统方法中耗时的训练阶段，并使得索引可以动态生长。

在实现层面，turbovec 使用 Rust 语言编写，利用其零成本抽象和内存安全性来构建高性能内核。关键的搜索内核使用平台特定的 SIMD 指令集进行手工优化：ARM 平台采用 NEON 指令集，x86 平台采用 AVX-512BW 指令集。这些内核直接在量化域内进行距离计算，避免了在搜索时解压缩向量的开销。

索引结构采用倒排链表加量化向量的组合方式，支持高效的在线插入和搜索。过滤机制（ID 白名单或位掩码）被集成到搜索内核中，使得过滤操作与距离计算流水线化，相比先搜索再后过滤的方案有显著的性能提升。

Python 绑定通过 PyO3 实现，提供简洁的 API 接口，使得 Python 用户能够轻松调用底层的高性能实现，无需了解 Rust 或 SIMD 细节。

## 安装与使用

turbovec 可通过 pip 直接安装：

```bash
pip install turbovec
```

对于 Rust 开发者，也可通过 cargo 添加依赖：

```bash
cargo add turbovec
```

最小可用示例（Python）：

```python
import turbovec
import numpy as np

# 创建索引，指定向量维度
index = turbovec.Index(dim=128)

# 添加向量（在线索引，无需训练）
vectors = np.random.rand(10000, 128).astype(np.float32)
ids = np.arange(10000)
index.add(ids, vectors)

# 搜索最近邻
query = np.random.rand(1, 128).astype(np.float32)
distances, indices = index.search(query, top_k=10)

# 带过滤的搜索
allowlist = [1, 2, 3, 100, 200, 500]
filtered_distances, filtered_indices = index.search(query, top_k=10, allowlist=allowlist)
```

## 适用场景

- **大规模文档/图像检索**：对于千万级甚至亿级规模的向量库，turbovec 能够将内存占用降低到传统方案的十分之一以下，同时保持高性能搜索，非常适合生产环境中的检索增强生成（RAG）系统。
- **推荐系统**：在线增量索引特性使得推荐系统可以随时添加新的物品或用户向量，无需定期重建索引，非常适合动态变化的推荐场景。
- **嵌入式与边缘设备**：ARM 平台的性能优势使得 turbovec 非常适合在手机、树莓派等 ARM 设备上运行大规模向量搜索，且低内存占用使其可用于资源受限环境。
- **时间序列与实时监控**：数据无偏量化特性使得 turbovec 对数据分布不敏感，可以稳定地处理实时流入的各类数据，无需像传统量化方法那样定期重新训练码本。

## 项目亮点

- **数据无偏量化——无需训练**：turbovec 完全摆脱了传统乘积量化（PQ）等方法的训练阶段。这意味着用户无需保留训练数据、无需等待聚类收敛，也无需处理训练集与测试集分布不一致的问题。只需向索引添加向量，即可开始搜索。
- **理论保证的量化质量**：TurboQuant 算法在理论上接近香农失真下界，而 turbovec 将其落地为可用的工程实现。用户可以获得接近无损的搜索精度，而内存成本却大幅降低。
- **跨平台的极致性能优化**：turbovec 没有使用通用的 SIMD 自动向量化，而是为 ARM NEON 和 x86 AVX-512BW 编写了手工优化内核。这种针对性优化使其在两种主流架构上都能超越 FAISS——一个已经经过高度优化的工业级向量搜索库。
- **搜索时过滤的流水线化设计**：与大多数向量库在搜索完成后才进行过滤不同，turbovec 将过滤逻辑集成到距离计算循环中。这不仅避免了大量不必要的距离计算，还减少了内存带宽消耗，使带过滤搜索的开销几乎可以忽略不计。

## 相关链接

- [GitHub 仓库](https://github.com/RyanCodrai/turbovec)
- [TurboQuant 论文](https://arxiv.org/abs/2504.19874)
- [PyPI 包](https://pypi.org/project/turbovec/)
- [crates.io 包](https://crates.io/crates/turbovec)
