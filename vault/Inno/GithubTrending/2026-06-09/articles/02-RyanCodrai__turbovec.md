---
tags:
  - trending
  - article
repo: RyanCodrai/turbovec
date: 2026-06-09
language: Python
stars_total: 9268
stars_today: 1729
---
## 项目概述

turbovec 是一个基于 Google Research TurboQuant 算法构建的高性能向量索引库，使用 Rust 编写并提供了 Python 绑定。该项目解决了大规模向量检索场景中内存占用过高和检索速度不足的核心问题。以一个包含 1000 万文档的语料库为例，若使用传统的 float32 存储，需要 31 GB 内存，而 turbovec 仅需 4 GB，同时检索速度还超过了 FAISS。目标用户包括需要在大规模稠密向量上进行近似最近邻搜索的开发者、数据科学家和 AI 研究人员，尤其适合那些面临内存预算紧张或需要低延迟检索的应用场景。

## 核心功能

- **领先的压缩率**：基于 TurboQuant 算法，实现无训练数据、即用即量化的数据无关量化器，在数学上逼近了香农失真下界，在极低比特率下仍能保持出色的检索精度
- **在线增量索引**：支持动态添加向量并立即查询，无需训练阶段、无需手动调整参数、无需在数据增长时重建索引，大大简化了生产环境的维护工作
- **超越 FAISS 的检索速度**：使用手工优化的 NEON（ARM 架构）和 AVX-512BW（x86 架构）内核，在 ARM 上比 FAISS IndexPQFastScan 快 12–20%，在 x86 上达到或超越其性能
- **搜索时过滤**：允许在 `search()` 调用时传入 id 白名单或槽位 bitmask，在检索内核中直接完成过滤，避免了大量后过滤的开销
- **多平台支持**：同时通过 PyPI 和 crates.io 分发，方便 Python 和 Rust 生态的开发者集成使用

## 技术架构

turbovec 的技术核心分为两个层次：

底层是 **TurboQuant 量化引擎**，源自 Google Research 在 2025 年发表的论文。与传统乘积量化（PQ）或残差量化（RQ）不同，TurboQuant 是一种数据无关（data-oblivious）的量化器，不需要在数据集上训练码本，也不需要单独的训练阶段。这意味着 turbovec 在第一次插入向量时即可开始使用，不会因为与训练数据的分布差异而导致精度下降。TurboQuant 在数学上被证明能达到香农率失真下界的水平，即在给定量化比特率下实现最小可能的失真。

上层是 **异步搜索内核**，针对不同 CPU 微架构进行了手写 SIMD 优化。ARM 平台采用 NEON 指令集，x86 平台采用 AVX-512BW，重点优化了 L2 距离计算和码字查找这两个最耗时的操作。搜索时过滤功能被直接融入内核流水线，使得带过滤的搜索几乎不产生额外开销。

整个项目采用 Rust 实现核心逻辑以兼顾性能与安全性，并通过 PyO3/maturin 提供 Python 绑定，使 Python 用户可以零开销调用底层算法。架构上保持了极小的依赖链，降低维护成本和编译时间。

## 安装与使用

**安装**（需要 Python 3.8+）：

```bash
pip install turbovec
```

**最小可用示例**：

```python
import numpy as np
import turbovec as tv

# 创建一个索引，使用4比特量化
index = tv.Index(dimension=768, quant_bit=4)

# 模拟插入1000个随机向量
for i in range(1000):
    vec = np.random.randn(768).astype(np.float32)
    index.insert(i, vec)

# 查询最相似的10个结果
query = np.random.randn(768).astype(np.float32)
results = index.search(query, top_k=10)
for id_, dist in results:
    print(f"ID: {id_}, Distance: {dist:.4f}")

# 带过滤的搜索——只从指定的id子集中检索
filter_ids = set(range(500))
results = index.search(query, top_k=10, allowlist=filter_ids)
```

**从 Rust 使用**（在 `Cargo.toml` 中添加）：

```toml
[dependencies]
turbovec = "0.1"
```

## 适用场景

- **信息检索与搜索引擎**：对百万到千万级别的文档嵌入进行实时近似最近邻搜索，在有限的单机内存预算下获得低延迟响应
- **推荐系统**：利用物品或用户的向量化表示进行相似物品检索，支持在查询时根据用户行为或其他条件动态过滤（如只看特定类别的商品）
- **多模态向量检索**：在图像、文本、音频等不同模态的联合嵌入空间中进行跨模态搜索，turbovec 的高压缩率使得整个系统可以部署在边缘设备或服务器环境
- **嵌入服务基础设施**：作为面向 AI 应用的后端向量存储组件，提供稳定的在线插入和低延迟查询能力，特别适合需要频繁更新向量集合的动态场景

## 项目亮点

- **零训练、零参数**：turboquant 的数据无关特性使其从根本上消除了传统量化方法需要预训练码本的痛点，在动态数据集上尤其具有优势
- **性能与精度的双重突破**：在同等比特率下，turbovec 的检索精度相比 FAISS 的量化方案表现更优；在同等精度目标下，turbovec 可以使用更低的比特率从而节省更多内存
- **原生过滤机制**：搜索时过滤被设计为内核内置功能，而非后处理步骤，这使得带约束的搜索在性能上几乎不受影响，适合生产环境中复杂的业务逻辑
- **全栈 Rust 实现**：避免了对 C++ 库的包装依赖，拥有更高的代码可读性和安全性，同时充分利用 Rust 的零成本抽象和跨平台能力

## 相关链接

- [GitHub 仓库](https://github.com/RyanCodrai/turbovec)
- [TurboQuant 论文](https://arxiv.org/abs/2504.19874)
- [PyPI 包](https://pypi.org/project/turbovec/)
- [crates.io 包](https://crates.io/crates/turbovec)
