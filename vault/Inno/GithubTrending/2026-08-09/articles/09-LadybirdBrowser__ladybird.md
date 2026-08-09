---
tags:
  - trending
  - article
repo: LadybirdBrowser/ladybird
date: 2026-08-09
language: C++
stars_total: 65030
stars_today: 48
---
## 项目概述

Ladybird 是一个真正独立的开源网页浏览器，由 SerenityOS 社区发起并发展而来。它的核心目标是从零开始构建一套完全自主的浏览器引擎，不依赖 Chromium、Firefox 或 WebKit 等现有浏览器内核。该项目目前处于 pre-alpha 阶段，主要面向浏览器开发者和技术爱好者，用于探索现代 Web 平台的实现细节。

Ladybird 的“独立”体现在两个层面：其一，其渲染引擎和 JavaScript 引擎均为原创实现，而非对现有引擎的封装或复用；其二，项目由一个活跃的开发者社区驱动，不受大型商业公司的技术路线或商业利益影响。目前，该仓库在 GitHub 上已获得超过 65,000 颗星，反映了开发者社区对新兴浏览器引擎的浓厚兴趣。

## 核心功能

- **多进程架构**：采用主 UI 进程与多个 WebContent 渲染进程分离的设计，每个标签页拥有独立的渲染进程，并通过沙箱隔离，增强系统安全性。
- **原创渲染引擎（LibWeb）**：基于 Web 标准从零实现 HTML、CSS 和 DOM 的解析与渲染，支持现代 Web 页面所需的布局、样式和交互特性。
- **自研 JavaScript 引擎（LibJS）**：包含完整的 ECMAScript 语法解析和运行时，支持 ES2023+ 标准的大部分特性，并配有 JIT 编译器优化路径。
- **开箱即用的网络与安全模块**：内置 HTTP/1.1 客户端（LibHTTP）、TLS 加密（LibTLS）以及加密原语库（LibCrypto），图片解码和网络连接均在独立进程中执行，以隔离恶意内容风险。
- **多媒体支持**：通过 LibMedia 模块提供音频和视频播放能力，支持常见的媒体封装格式和编解码器。
- **跨平台运行**：支持 Linux、macOS、Windows（通过 WSL2）以及其他类 Unix 系统，提供统一的构建脚本和开发环境。

## 技术架构

Ladybird 的架构设计遵循“模块化 + 进程隔离”的原则。所有核心功能以静态库的形式组织在 `Lib*` 系列目录下，例如 `LibWeb`（渲染引擎）、`LibJS`（JavaScript引擎）、`LibWasm`（WebAssembly实现）等。这些库既可以被浏览器直接使用，也可以被其他项目单独引用。

在运行层面，浏览器启动时会产生多个进程类型：
- **UI 进程**：负责窗口管理和用户交互，运行基于 Qt 的跨平台界面。
- **WebContent 进程**：每个标签页独立对应一个，负责页面的 DOM 解析、样式计算、布局绘制和 JavaScript 执行。
- **ImageDecoder 进程**：专门处理图片解码，避免解码漏洞直接影响主进程。
- **RequestServer 进程**：统一管理网络请求和协议栈，隔离网络数据解析过程。

进程间通信通过 `LibIPC` 库完成，采用异步消息传递机制。这种设计参考了现代浏览器的安全实践，但 Ladybird 在实现上完全自主，并不依赖 Chromium 的现有代码。此外，项目的构建系统使用 CMake，并提供了详细的 [构建说明文档](Documentation/BuildInstructionsLadybird.md)，支持 Debug 和 Release 等多种编译模式。

## 安装与使用

由于 Ladybird 目前处于早期开发阶段，官方不提供预编译二进制包，用户需要从源码构建。以下以 Ubuntu/Linux 为例的简要步骤：

1. **安装系统依赖**（以 Debian/Ubuntu 为例）：
   ```bash
   sudo apt install build-essential cmake ninja-build qt6-base-dev qttools6-dev libqt6svg6-dev libgl1-mesa-dev libfreetype-dev libharfbuzz-dev
   ```

2. **克隆仓库并构建**：
   ```bash
   git clone https://github.com/LadybirdBrowser/ladybird.git
   cd ladybird
   ./Meta/ladybird.sh build
   ```

3. **启动浏览器**：
   ```bash
   ./Build/ladybird/Symbol/ladybird https://example.com
   ```

构建脚本会自动下载依赖的第三方库（如 Qt 和 OpenGL）并配置编译环境。对于 macOS 用户，可使用 `brew install qt ninja` 安装依赖；Windows 用户建议启用 WSL2 后遵循 Linux 流程。首次构建可能需要较长时间（取决于机器性能，约 30 到 60 分钟），后续增量编译会更快。

## 适用场景

- **浏览器引擎研究**：对于希望深入理解浏览器渲染管线、JavaScript 运行时或网络栈实现的开发者，Ladybird 提供了一个结构清晰且注释详尽的参考实现。
- **Web 标准测试**：由于 Ladybird 从零实现标准，其进展直接反映 Web 标准的复杂度和边界情况，可作为新的测试目标，帮助发现规范中的模糊之处。
- **嵌入式或定制浏览器**：得益于模块化架构和三方许可（BSD-2-Clause），开发人员可以便捷地裁剪和复用 `LibWeb`、`LibJS` 等库，构建轻量级的专用浏览器环境。
- **Web 开发调试**：Web 开发者可使用 Ladybird 作为预览引擎，检查页面的跨浏览器兼容性，尤其是在布局和 JavaScript 行为方面。

## 项目亮点

- **真正独立的技术栈**：不借用任何主流浏览器引擎代码，包括渲染、脚本、网络、加密和图形库，全部原创实现，这在业界极为罕见。
- **卓越的代码可读性**：项目采用现代 C++（C++20/23）编写，目录结构清晰，每个模块的功能边界明确，注释充分，适合学习研究。
- **开放透明的开发节奏**：项目拥有公开的 [开发计划](https://github.com/LadybirdBrowser/ladybird/wiki/Development-Plan)，每周发布多篇开发日志，社区讨论活跃，决策过程对参与者公开。
- **跨进程安全实践**：通过将图片解码和网络请求隔离在独立进程中，并配合沙箱机制，在早期阶段就构建了较强的安全基线。

## 相关链接

- [GitHub 仓库](https://github.com/LadybirdBrowser/ladybird)
- [官网](https://ladybird.org)
- [构建说明文档](https://github.com/LadybirdBrowser/ladybird/blob/master/Documentation/BuildInstructionsLadybird.md)
- [开发计划与 Wiki](https://github.com/LadybirdBrowser/ladybird/wiki)
