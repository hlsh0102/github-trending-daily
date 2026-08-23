---
tags:
  - trending
  - article
repo: modular/modular
date: 2026-08-23
language: Mojo
stars_total: 28863
stars_today: 395
---
## 项目概述

Modular Platform 是一个面向 AI 开发和部署的统一平台，由 Modular 公司开源维护。该仓库托管了平台的核心开源组件，其中最引人注目的是 **MAX Framework** 和 **Mojo Language** 两大项目。

MAX Framework 提供了一个高性能的 AI 推理和服务框架，旨在简化从模型训练到生产部署的全流程。Mojo Language 则是一门专为 AI 和科学计算设计的编程语言，结合了 Python 的易用性与 C/C++ 的性能优势，被视为 AI 基础设施领域的重要创新。

该项目的目标用户包括 AI 研究者、ML 工程师、数据科学家以及对高性能计算感兴趣的开发者。无论你是在构建生产级推理服务，还是希望编写高性能的 AI 算法，Modular Platform 都提供了相应的工具链和运行时支持。

## 核心功能

- **MAX Framework**：提供端到端的 AI 开发与部署能力，支持模型加载、优化、推理和服务化部署。
- **Mojo Language**：一门融合 Python 语法与系统级性能的编程语言，支持编译为高效原生代码。
- **OpenAI 兼容端点**：MAX 内置的推理服务器（`max/serve`）提供与 OpenAI API 兼容的接口，可无缝替换现有服务。
- **模型流水线**：MAX 支持构建 Python 为基础的模型推理图（`max/pipelines`），方便组合复杂的推理逻辑。
- **加速器内核库**：MAX 包含一个高性能的加速器内核库（`max/kernels`），针对多种硬件架构进行了深度优化。
- **丰富的代码示例**：仓库内附带大量 MAX 和 Mojo 的示例代码，覆盖从基础语法到完整模型部署的各个层次。

## 技术架构

Modular Platform 的技术架构围绕「统一内核 + 多语言前端」的设计理念展开。

底层是 **MAX 内核库**（`max/kernels`），提供了一组高度优化的计算内核，支持 CPU、GPU 以及未来的专用加速硬件。这些内核采用 Mojo 语言编写，通过编译期元编程和 MLIR 中间表示，实现了跨硬件的可移植性和极致性能。

中间层是 **MAX 运行时**，负责模型加载、内存管理、算子调度等核心任务。运行时通过 Python 绑定暴露给上层，使得开发者可以使用熟悉的 Python 生态来构建和部署模型。

最上层是 **Mojo 编译器**和 **MAX Python SDK**。Mojo 编译器基于 LLVM 和 MLIR 技术栈，将 Mojo 源码编译为可执行文件或动态库；MAX SDK 则提供了一套 Python API，让用户能够以声明式或命令式的方式构建推理流水线。

架构上的关键特点在于**分层解耦**：各组件可以独立使用，例如你可以只使用 Mojo 编写高性能算法，也可以仅通过 MAX 部署已有模型，无需了解底层细节。此外，项目正在逐步开源更多组件，社区参与度持续提升。

## 安装与使用

### 安装

目前最便捷的安装方式是通过官方安装脚本。在终端中执行以下命令即可安装 Modular CLI 工具：

```bash
curl -s https://get.modular.com | sh
```

安装完成后，你可以通过 `modular` 命令管理 Mojo 和 MAX 的安装与版本更新。

### 使用 MAX 部署模型（最小示例）

1. 首先确保安装了 MAX 运行时：`modular install max`
2. 使用 Python 快速启动一个推理服务：

```python
from max.serve import Server
from max.pipelines import PipelineConfig, Pipeline

# 加载一个预训练模型（例如 Llama 3）
config = PipelineConfig("llama3")
pipeline = Pipeline(config)

# 启动 OpenAI 兼容的推理服务
server = Server(pipeline)
server.serve(host="0.0.0.0", port=8080)
```

保存上述脚本为 `serve.py`，运行 `python serve.py` 后，即可通过 `http://localhost:8080/v1/chat/completions` 调用模型。

### 使用 Mojo 编写第一个程序

1. 安装 Mojo：`modular install mojo`
2. 创建一个 `hello.mojo` 文件：

```mojo
fn main() raises:
    print("Hello from Mojo!")
```

3. 运行：`mojo hello.mojo`

## 适用场景

- **生产级模型服务**：利用 MAX 的高性能推理引擎和 OpenAI 兼容接口，快速将数据模型部署为稳定的 API 服务，适用于各类在线推理应用。
- **高性能算法研发**：使用 Mojo 编写计算密集型的科学计算或 AI 算法，在保持 Python 类开发体验的同时获得接近原生的执行效率。
- **边缘与嵌入式部署**：Mojo 支持编译为独立的二进制文件，适合在资源受限的边缘设备上运行 AI 推理任务。
- **构建自定义 AI 基础设施**：借助 MAX 的可扩展架构，你可以在内核层面调整或添加自定义算子，打造针对特定硬件或业务场景的推理引擎。

## 项目亮点

- **性能与易用性兼得**：Mojo 语言的独创设计打破了 Python 性能不足的瓶颈，同时保留了优秀的代码可读性。
- **与主流生态兼容**：MAX 的 OpenAI 兼容端点、Python 优先的 SDK 设计，大大降低了从现有技术栈迁移的门槛。
- **持续开源透明**：Modular 正持续将平台核心组件开源，并欢迎社区贡献，这与许多商业闭源 AI 平台形成鲜明对比。
- **架构前瞻性**：通过 MLIR 和统一内核抽象，平台可以灵活适配未来出现的各类新型硬件，具有很强的横向扩展能力。
- **活跃的社区生态**：仓库已累计获得近 3 万星标，每日增长显著，展示了社区的高关注度和快速迭代势头。

## 相关链接

- [GitHub 仓库](https://github.com/modular/modular)
- [MAX 官方文档](https://max.modular.com/get-started)
- [Mojo 官方文档](https://mojolang.org/docs/manual/quickstart/)
- [Modular 公司官网](https://www.modular.com)
