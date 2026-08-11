---
tags:
  - trending
  - article
repo: LadybirdBrowser/ladybird
date: 2026-08-11
language: C++
stars_total: 65293
stars_today: 56
---
## 项目概述

Ladybird 是一个真正独立于主流浏览器技术栈的网页浏览器项目，由 SerenityOS 社区发起，目标是构建一个完全基于 Web 标准的全新浏览器引擎。与 Firefox、Chrome 等基于既有引擎（Gecko、Blink/WebKit）开发的浏览器不同，Ladybird 从零开始编写了自己的渲染引擎和 JavaScript 引擎，不依赖任何现有浏览器内核代码。

该项目目前处于 pre-alpha 阶段，主要面向浏览器开发者和技术爱好者，而非普通终端用户。Ladybird 的最终目标是成为一个完整、可用的现代 Web 浏览器，能够处理日常网页浏览需求，同时保持代码的可读性和可维护性。

## 核心功能

- **多进程架构**：采用主 UI 进程 + 多个 WebContent 渲染进程 + 独立 ImageDecoder 进程 + 独立 RequestServer 进程的设计，提高稳定性和安全性。
- **进程沙箱隔离**：每个标签页拥有独立的渲染进程，并与系统其他部分隔离；图片解码和网络请求均在独立进程中进行，降低恶意内容带来的风险。
- **原生 Web 标准实现**：渲染引擎 LibWeb 和 JavaScript 引擎 LibJS 完全基于 Web 规范编写，不借用任何现有浏览器引擎的代码。
- **完整组件栈**：内置 HTTP/1.1 客户端、TLS 加密、2D 图形库、Unicode 支持、音视频解码等底层库，形成一套自给自足的浏览器基础设施。
- **跨平台支持**：可在 Linux、macOS、Windows（通过 WSL2）以及多种 \*NIX 系统上构建运行。
- **BSD-2-Clause 开源许可**：宽松的许可证允许自由使用、修改和分发。

## 技术架构

Ladybird 的技术架构体现了“独立”这一核心设计理念。整个浏览器引擎分为多个层次：

在底层，项目从 SerenityOS 操作系统中继承了大量经过实战检验的基础库，包括：

- **LibWeb**：负责 HTML/CSS 解析、DOM 构建和页面渲染，是浏览器的核心渲染引擎。
- **LibJS**：完整的 JavaScript 引擎，支持现代 ECMAScript 规范。
- **LibWasm**：WebAssembly 二进制格式的解释和执行实现。
- **LibCrypto/LibTLS**：提供加密原语和 TLS 协议实现，保证 HTTPS 通信安全。
- **LibHTTP**：实现 HTTP/1.1 协议的客户端库。
- **LibGfx**：2D 图形渲染、图像解码和绘制的基础库。

在进程模型上，Ladybird 采用严格的多进程隔离设计。主 UI 进程负责窗口管理和用户交互，每个浏览器标签页对应一个独立的 WebContent 渲染进程，此外还有专门的 ImageDecoder 进程和 RequestServer 进程分别处理图像解码和网络请求。这种架构使得任何单个渲染进程的崩溃或被攻击都不会影响整个浏览器的稳定性和系统的安全性。

在架构哲学上，Ladybird 强调“从原则出发”的实现方式——每个 Web 功能都从规范文档直接实现，而不是参考现有浏览器的行为。这种做法的好处是代码逻辑清晰、易于审查和调试，但也意味着开发进度相对较慢。

## 安装与使用

Ladybird 目前仅面向开发者使用，需要从源码构建。构建步骤概要如下：

1. **获取源码**：
   ```bash
   git clone https://github.com/LadybirdBrowser/ladybird.git
   cd ladybird
   ```

2. **构建依赖**：确保系统已安装 CMake、Ninja、Clang 编译器以及必要的系统库。具体依赖项请参考 `Documentation/BuildInstructionsLadybird.md`。

3. **编译项目**：
   ```bash
   ./Meta/ladybird.sh run
   ```
   该脚本会自动完成依赖检查、编译配置和构建过程，并在成功构建后启动 Ladybird 浏览器。

4. **运行开发版本**：构建完成后，可以直接运行生成的可执行文件。目前推荐使用脚本方式管理和运行，因为浏览器仍处于早期开发阶段，不同平台上的构建方式可能有所差异。

5. **跨平台构建**：Windows 用户需要使用 WSL2 环境进行构建，macOS 用户和 Linux 用户可直接在本地构建。项目还支持在众多 \*NIX 系统上运行。

由于项目处于 pre-alpha 阶段，需要具备 C++ 开发经验和浏览器引擎基础知识的开发者才能有效使用和参与贡献。

## 适用场景

- **浏览器引擎研究**：对于希望深入理解浏览器工作原理、学习渲染引擎和 JavaScript 引擎实现细节的开发者，Ladybird 提供了一个完整且代码质量较高的参考实现。
- **Web 标准验证**：Ladybird 严格从规范出发的实现方式，使其成为验证 Web 标准可行性的优质平台，尤其适用于测试新规范的实际可实现性。
- **安全研究**：多进程架构和进程沙箱隔离设计为浏览器安全研究提供了良好的实验环境，安全研究人员可以在此基础上分析浏览器攻击面。
- **开源贡献**：对于寻找有影响力开源项目的 C++ 开发者，Ladybird 提供了参与构建现代浏览器引擎的机会，涉及大量底层技术领域。

## 项目亮点

Ladybird 最显著的差异化优势在于其**真正的独立性**。当前主流浏览器中，除 Firefox（Gecko 引擎）和 Safari（WebKit 引擎）外，几乎所有浏览器都基于 Chromium 内核。Ladybird 完全从零构建渲染引擎和 JavaScript 引擎，不包含任何来自 Chrome、Firefox 或 Safari 的代码，这在当今浏览器生态中极为罕见。

其次，Ladybird 继承了 SerenityOS 高度模块化和整洁的代码风格。所有核心库都从操作系统层面设计，确保了组件之间的边界清晰和可复用性。该项目采用多进程隔离设计，将图像解码和网络请求等高风险操作放在独立进程中，展现出对浏览器安全的深刻理解。

此外，Ladybird 拥有活跃的社区和清晰的开发路线图。项目在 GitHub 上获得了超过 6.5 万颗星，吸引了大量贡献者参与，正在快速向可用的现代浏览器目标推进。

## 相关链接

- [GitHub 仓库](https://github.com/LadybirdBrowser/ladybird)
- [官方网站](https://ladybird.org)
- [构建文档](https://github.com/LadybirdBrowser/ladybird/blob/master/Documentation/BuildInstructionsLadybird.md)
- [项目文档目录](https://github.com/LadybirdBrowser/ladybird/tree/master/Documentation)
