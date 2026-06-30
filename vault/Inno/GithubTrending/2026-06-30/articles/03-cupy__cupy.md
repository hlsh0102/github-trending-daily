---
tags:
  - trending
  - article
repo: cupy/cupy
date: 2026-06-30
language: Python
stars_total: 11898
stars_today: 352
---
## 项目概述

CuPy 是一个与 NumPy 和 SciPy 兼容的 GPU 加速数组计算库，专为 Python 开发者设计。它解决了在 GPU 上高效执行数值计算的关键问题——传统 NumPy 运算受限于 CPU 性能，而直接编写 CUDA 代码又过于复杂。CuPy 作为 NumPy 和 SciPy 的“即插即用”替代品，允许用户将现有的基于 NumPy 的代码无缝迁移到 GPU 上运行，无需修改核心逻辑。目标用户包括数据科学家、机器学习工程师、深度学习研究人员以及任何需要利用 GPU 加速大规模数值计算的开发者。目前，CuPy 已获得近 12000 个 GitHub Star，是 Python GPU 计算领域最活跃的开源项目之一。

## 核心功能

- **GPU 加速的数组操作**：完整支持 NumPy 核心功能，包括数组创建、索引、切片、形状变换和广播等，所有操作均在 GPU 上并行执行。
- **SciPy 兼容的科学计算**：提供 scipy 模块的常用函数，如线性代数（scipy.linalg）、稀疏矩阵（scipy.sparse）、快速傅里叶变换（scipy.fft）等，均针对 GPU 优化。
- **自动内存管理**：基于引用计数的内存分配与回收机制，自动管理 GPU 显存，避免内存泄漏，并提供内存池优化显存使用效率。
- **底层 CUDA 特性支持**：允许用户定义自定义 CUDA 内核（RawKernel）、管理流（Stream）和执行异步操作，实现细粒度性能控制。
- **多 GPU 与分布式计算**：支持多 GPU 环境下的数据并行和模型并行，可通过 MPI 或 NCCL 实现跨节点分布式训练。
- **AMD ROCm 平台兼容**：除 NVIDIA CUDA 外，还支持 AMD ROCm 平台，扩展了 GPU 硬件选择范围。

## 技术架构

CuPy 的核心架构基于 C++ 和 CUDA C 编写的高性能后端，通过 Python 封装提供 NumPy 兼容接口。其设计思路包括：

- **NumPy 兼容性**：CuPy 的 `ndarray` 类完全模仿 NumPy 的 `ndarray` 接口，但底层数据存储在 GPU 显存中。所有 NumPy 函数（如 `numpy.sum`、`numpy.dot`）都有对应的 CuPy 实现，调用时自动在 GPU 上执行。
- **即时编译（JIT）**：自定义内核（如 `RawKernel`）使用 CUDA C 或 HIP C 编写，在运行时编译为 GPU 可执行代码，兼顾灵活性与性能。
- **内存池与懒加载**：使用内存池机制减少显存分配开销，并支持内存的懒分配，仅在需要时才实际占用显存，优化资源使用。
- **异步执行与流管理**：默认使用异步流执行操作，允许 CPU 和 GPU 任务重叠，提升整体吞吐量。用户可手动创建和管理 CUDA 流，实现细粒度同步控制。
- **多后端支持**：通过统一抽象层，同时支持 NVIDIA CUDA 和 AMD ROCm 平台，关键代码路径在编译时根据目标平台选择对应实现。

## 安装与使用

CuPy 的安装依赖于 CUDA 工具包或 ROCm 环境。推荐通过 pip 或 conda 安装：

```bash
# 通过 pip 安装（需已安装 CUDA）
pip install cupy-cuda12x  # 根据 CUDA 版本选择对应的 wheel 包

# 通过 conda 安装（自动处理依赖）
conda install -c conda-forge cupy
```

最小可用示例：将 NumPy 代码迁移到 CuPy，仅需更改包名：

```python
import cupy as cp

# 在 GPU 上创建数组
x_gpu = cp.array([1, 2, 3, 4, 5])
y_gpu = cp.array([6, 7, 8, 9, 10])

# 执行数学运算（自动在 GPU 上并行计算）
z_gpu = cp.dot(x_gpu, y_gpu)  # 点积
result = cp.sqrt(x_gpu)       # 逐元素开方

# 与 NumPy 混合使用（自动同步到 CPU）
import numpy as np
x_cpu = cp.asnumpy(x_gpu)     # 转回 NumPy 数组
```

更复杂的线性代数运算：

```python
import cupy as cp

# 创建随机矩阵
A = cp.random.randn(1000, 1000)
B = cp.random.randn(1000, 1000)

# GPU 加速的矩阵乘法
C = cp.dot(A, B)

# 求解线性方程组
x = cp.linalg.solve(A, B)
```

## 适用场景

- **深度学习预处理与后处理**：在 PyTorch 或 TensorFlow 之外，使用 CuPy 加速数据增强、归一化、特征提取等预处理步骤，以及模型输出的数值计算。
- **科学计算与仿真**：在物理模拟、计算化学、气候建模等需要大规模矩阵运算的领域，使用 CuPy 替代 NumPy 获得显著加速。
- **图像与信号处理**：利用 GPU 并行性加速图像滤波、傅里叶变换、卷积等操作，适用于医学影像、雷达信号处理等实时性要求高的场景。
- **金融量化分析**：加速蒙特卡洛模拟、期权定价、风险计算等金融计算，尤其在处理数百万次独立模拟时效果显著。

## 项目亮点

- **最小迁移成本**：与 NumPy/SciPy 的 API 高度兼容，通常只需将 `import numpy as np` 改为 `import cupy as cp` 即可获得 GPU 加速，无需学习新框架。
- **灵活性与性能平衡**：既提供高层接口（类似 NumPy），又允许用户编写自定义 CUDA 内核，满足从快速开发到极致优化的各种需求。
- **多硬件支持**：同时支持 NVIDIA 和 AMD 两大 GPU 平台，打破硬件锁定，用户可根据成本或性能选择硬件。
- **活跃的社区与生态系统**：作为 NumPy 生态系统的一部分，与 Jupyter、CuDF（GPU DataFrame）等工具良好集成，且有丰富的文档、示例和论坛支持。

## 相关链接

- [GitHub 仓库](https://github.com/cupy/cupy)
- [官方网站](https://cupy.dev/)
- [安装指南](https://docs.cupy.dev/en/stable/install.html)
- [用户手册与教程](https://docs.cupy.dev/en/stable/user_guide/basic.html)
- [API 参考](https://docs.cupy.dev/en/stable/reference/)
- [社区论坛](https://groups.google.com/forum/#!forum/cupy)
