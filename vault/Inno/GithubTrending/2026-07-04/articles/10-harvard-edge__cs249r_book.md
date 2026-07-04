---
tags:
  - trending
  - article
repo: harvard-edge/cs249r_book
date: 2026-07-04
language: Python
stars_total: 26268
stars_today: 793
---
## 项目概述

**Machine Learning Systems**（机器学习系统）是哈佛大学 CS249r 课程的开源教科书与配套实验项目，由 Harvard EDGE 实验室维护。该项目系统性地讲授人工智能系统工程的设计原理与实践方法，旨在弥合机器学习算法理论与生产级部署之间的鸿沟。目标用户包括希望深入理解 ML 系统全栈的高年级本科生、研究生、工程师以及研究人员。

该项目不仅仅是一本书，而是一个完整的教学资源包，包含交互式 Jupyter Notebook 实验、微型自动微分框架 TinyTorch、硬件实验套件以及 CI/CD 自动化验证流水线。它强调从底层数学推导到上层分布式推理的端到端工程思维，帮助读者建立对 ML 系统“如何工作以及为何如此工作”的深刻理解。

## 核心功能

- **多媒体教科书**：使用 Jupyter Book 构建，支持 HTML、PDF 等多种格式；内容涵盖从自动微分、计算图优化到分布式训练、模型压缩、边缘部署等完整主题。
- **TinyTorch 教学框架**：一个从零实现的、轻量级的 PyTorch 风格自动微分与神经网络库，代码不到 2000 行，用于教学演示反向传播的实现本质。
- **可交互的实验环境**：每个章节配套 Jupyter Notebook 实验，读者可在线执行代码、调整参数，直观观察系统行为变化（如梯度消失、内存布局对计算速度的影响）。
- **硬件实验套件**：提供基于 Arduino 等微控制器的动手项目，演示如何将 ML 模型部署到资源受限的设备上（TinyML 场景）。
- **自动化质量保障**：GitHub Actions 流水线对书籍编译、TinyTorch 单元测试、实验代码执行、硬件套件构建进行自动验证，确保教学材料始终处于可用状态。
- **多语言支持**：README 已提供英文、中文、日文、韩文版本，降低非英语读者的入门门槛。

## 技术架构

项目的技术栈围绕**教学可理解性**和**可复现性**设计：

- **文档层**：基于 Jupyter Book（MyST Markdown + Jupyter Notebooks）构建，利用 Jupyter Notebook 支持代码、数学公式 LaTeX 与实时可视化混排，方便读者直接在浏览器中编辑运行。
- **教学框架层**：TinyTorch 纯 Python 实现，依赖仅使用 NumPy，核心代码采用模块化设计——张量类 `Tensor` 统一管理数据与梯度，`Function` 基类通过重写 `forward`/`backward` 方法实现可微分操作，`Module` 封装神经网络层。这种设计使得学生能够在单文件中追踪整个自动微分与计算图构建的全过程。
- **实验层**：每个实验 Notebook 遵循“理论基础→代码演示→练习任务”的结构，使用 `nbval` 和 `pytest` 对关键断言进行自动检查。
- **硬件层**：TinyML 实验基于 TensorFlow Lite Micro 和 PlatformIO 构建，包含预训练的模型转换脚本和固件烧录指南。
- **CI/CD**：GitHub Actions 工作流分为四个独立的管道（Book、TinyTorch、Labs、Kits），每个管道在 dev 分支的 pull request 和 push 时自动触发并行验证，有效防止教材断裂。

架构的核心思想是**从零构建，但不重复造轮子**：通过重写最微小的神经网络库来理解底层原理，而后逐步引入生产级工具（如 PyTorch、TensorFlow Lite、ONNX）进行实际部署。

## 安装与使用

### 环境要求
- Python >= 3.9
- Git、Jupyter 环境（推荐 VSCode + Remote Containers 或 Google Colab）

### 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/harvard-edge/cs249r_book.git
   cd cs249r_book
   ```
2. 创建虚拟环境并安装依赖（以书为例）：
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. 构建书籍（可选在线预览）：
   ```bash
   jupyter-book build book/
   # 输出目录为 book/_build/html，直接用浏览器打开 index.html 即可
   ```

### 最小可用示例
在配套实验目录中运行 TinyTorch 的线性回归演示：
```python
# 从 tiny_torch 目录导入教学框架
from tiny_torch.tensor import Tensor
from tiny_torch.nn import Linear, MSELoss
import numpy as np

# 构建一个单层网络
model = Linear(1, 1)
loss_fn = MSELoss()
inputs = Tensor(np.array([[1.], [2.], [3.]]))
targets = Tensor(np.array([[2.], [4.], [6.]]))

# 手动执行训练循环（展示自动微分）
outputs = model(inputs)
loss = loss_fn(outputs, targets)
loss.backward()
print(f"Gradient: {model.w.grad}")  # 观察权重的梯度
```

## 适用场景

- **高校研究生机器学习系统课程**：可以直接作为 CS249r 的教学材料，也可作为任何机器学习/深度学习课程的补充读物，尤其是在讲授反向传播、计算图、分布式训练章节时。
- **自学者系统学习 ML 工程**：读者既能通过 TinyTorch 理解底层数学与实现细节，又能在后续实验中学习模型裁剪、量化和 TensorRT 部署等实用技能，形成完整知识闭环。
- **工业工程师团队内培训**：项目中关于模型导出、移动端部署和性能分析的实验可以作为企业内部的技术分享或新员工培训素材。
- **黑客马拉松/研究原型验证**：利用 TinyTorch 快速构建自定义操作和梯度计算的实验性网络，配合 Jupyter Notebook 可以实时可视化结果。

## 项目亮点

- **教学深度与实用性的罕见平衡**：大多数 ML 教科书要么停留在数学推导，要么只讲 API 调用。该项目用不到 2000 行的 TinyTorch 实现让读者同时理解 *Why* 和 *How*，而硬件套件又验证了 *What works in practice*。
- **完整且自包含的教学生态**：一本好书 + 一个教学框架 + 可执行实验 + 硬件套件 + CI 验证，所有资源在同一个仓库内保持同步更新，学生不需要在多个网站间奔波寻找资料。
- **高度可复现与可扩展**：所有实验结果由 CI 自动运行验证，保证在任何新环境下都能复现教材中的输出；教学框架的模块化设计也允许学生轻松添加自定义算子。
- **活跃的社区与实时构建**：拥有近 2.6 万 GitHub 星标，每天持续更新；四个独立的 CI 管道确保书籍、框架、实验、硬件套件始终处于健康状态。

## 相关链接

- [GitHub 仓库](https://github.com/harvard-edge/cs249r_book)
- [在线阅读书籍（HTML 版）](https://harvard-edge.github.io/cs249r_book/)（假设存在，实际请确认仓库中的部署地址）
