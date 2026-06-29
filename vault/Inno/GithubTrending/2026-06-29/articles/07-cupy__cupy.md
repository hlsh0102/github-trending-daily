---
tags:
  - trending
  - article
repo: cupy/cupy
date: 2026-06-29
language: Python
stars_total: 11608
stars_today: 174
---
## 项目概述

CuPy 是一个专为 GPU 加速计算设计的 Python 数组库，完全兼容 NumPy 和 SciPy 的接口。它的核心目标是为数据科学家和机器学习工程师提供一个零学习成本的解决方案：将现有的 NumPy/SciPy 代码迁移到 GPU 上运行，只需将 `import numpy as np` 替换为 `import cupy as cp`。CuPy 特别适合需要大规模数值计算的场景，如深度学习、科学计算、图像处理和物理模拟。

## 核心功能

- **NumPy/SciPy 接口兼容**：CuPy 实现了 NumPy 和 SciPy 的绝大部分函数和数组操作，用户可以在 CPU 和 GPU 之间无缝切换，无需修改代码逻辑。
- **GPU 加速计算**：利用 NVIDIA CUDA 或 AMD ROCm 平台，CuPy 能显著提升数组运算、线性代数、傅里叶变换等密集型计算的执行速度。
- **低级 CUDA 功能访问**：支持自定义 CUDA 内核（RawKernels）、Stream 管理和内存池，满足对 GPU 资源进行精细控制的需求。
- **多 GPU 支持**：提供 `cupy.cuda.Device` 接口和 `cupyx.distributed` 模块，可在多 GPU 环境下进行数据并行或模型并行计算。
- **自动类型与形状推断**：与 NumPy 一样，CuPy 数组会自动推断数据类型和形状，并支持广播机制，简化代码编写。
- **丰富的高级 API**：包括 `cupyx.scipy`（稀疏矩阵、特殊函数）、`cupyx.ndimage`（图像滤波、形态学操作）和 `cupyx.signal`（信号处理）等。

## 技术架构

CuPy 的核心设计思路是在保持 NumPy 兼容性的同时，将计算尽可能地卸载到 GPU 上。其技术栈包括：

- **NumPy 兼容层**：CuPy 的数组对象 `cupy.ndarray` 实现了与 NumPy 完全相同的接口（如形状、切片、索引、广播），并通过内存布局和数据类型对齐来确保互操作性。
- **CUDA/ROCm 后端**：计算核心使用 CUDA C++ 或 HIP 编写，通过 cuBLAS、cuFFT、cuRAND、cuSOLVER 等 NVIDIA 库，或 ROCm 的 rocBLAS、rocFFT 等效库，实现高效线性代数、快速傅里叶变换和随机数生成。
- **即时编译（JIT）**：CuPy 的 `RawKernel` 和 `ElementwiseKernel` 允许用户用 C++ 编写自定义 GPU 内核，并由 CuPy 在运行时编译为 PTX 或二进制代码，兼顾灵活性和性能。
- **内存管理**：内置内存池（`MemoryPool`）和流管理器，减少 GPU 内存分配和释放的开销，提升连续调用的效率。
- **自动类型转换**：在 CPU 和 GPU 之间传输数据时，CuPy 会自动处理类型转换，并通过 `cupy.asarray()` 和 `cupy.asnumpy()` 实现高效的数据迁移。

## 安装与使用

### 安装步骤

CuPy 支持通过 pip 或 conda 安装。根据你的 CUDA 版本选择对应的 wheel 包：

```bash
# 使用 pip（适用于 CUDA 12.x）
pip install cupy-cuda12x

# 或使用 conda（自动检测 CUDA 版本）
conda install -c conda-forge cupy
```

对于 AMD ROCm 用户，请参考官方文档进行配置。

### 最小可用示例

以下是一个简单的 CuPy 使用示例，展示了如何创建 GPU 数组并执行运算：

```python
import cupy as cp

# 创建 GPU 数组
x = cp.arange(6).reshape(2, 3).astype('f')
print(x)
# 输出：array([[ 0.,  1.,  2.],
#             [ 3.,  4.,  5.]], dtype=float32)

# 执行矩阵运算（CuPy 自动在 GPU 上计算）
y = cp.dot(x, x.T)
print(y)
# 输出：array([[  5.,  14.],
#             [ 14.,  50.]], dtype=float32)

# 将结果传回 CPU
result = cp.asnumpy(y)
print(type(result))  # <class 'numpy.ndarray'>
```

## 适用场景

- **深度学习研究**：作为 PyTorch 或 TensorFlow 的补充，CuPy 可用于实现自定义的 GPU 加速损失函数、数据预处理或验证逻辑，避免在 CPU/GPU 间频繁切换。
- **科学计算与模拟**：在物理模拟（如分子动力学、流体力学）、气候建模和信号处理中，CuPy 可代替 NumPy 处理大规模数组，将计算时间从小时级缩短到分钟级。
- **图像与视频处理**：利用 `cupyx.ndimage` 模块，可对高分辨率图像或视频帧进行实时滤波、边缘检测和形态学操作，适合计算机视觉应用。
- **金融量化分析**：在风险计算、蒙特卡洛模拟和金融时间序列分析中，CuPy 能加速矩阵运算（如协方差矩阵、多元回归），提升回测和实时交易的效率。

## 项目亮点

- **零迁移成本**：CuPy 完全兼容 NumPy/SciPy 接口，用户只需修改 `import` 语句即可将现有代码切换到 GPU，极大降低了学习曲线和移植工作量。
- **多平台支持**：不仅支持 NVIDIA CUDA，还兼容 AMD ROCm，覆盖主流 GPU 生态。
- **低级控制能力**：与高层封装（如 TensorFlow）不同，CuPy 允许用户直接编写 CUDA 内核、管理 Stream 和内存，适合需要极致优化的场景。
- **活跃的社区和文档**：拥有丰富的官方文档、示例和社区论坛，持续跟进最新 GPU 技术和 NumPy 版本更新。
- **开源友好**：基于 MIT 许可证，可自由用于商业和非商业项目，且依赖关系简洁（仅需 NumPy）。

## 相关链接

- [GitHub 仓库](https://github.com/cupy/cupy)
- [项目官网](https://cupy.dev/)
- [安装指南](https://docs.cupy.dev/en/stable/install.html)
- [官方教程](https://docs.cupy.dev/en/stable/user_guide/basic.html)
- [API 参考](https://docs.cupy.dev/en/stable/reference/)
