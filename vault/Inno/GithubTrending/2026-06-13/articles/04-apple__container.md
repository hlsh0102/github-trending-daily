---
tags:
  - trending
  - article
repo: apple/container
date: 2026-06-13
language: Swift
stars_total: 35400
stars_today: 3504
---
## 项目概述

`container` 是 Apple 开源的一款工具，用于在 Mac 上通过轻量级虚拟机创建和运行 Linux 容器。它完全使用 Swift 编写，并针对 Apple 芯片进行了深度优化，旨在为开发者提供一种在 macOS 上体验原生容器工作流的新方式。

该项目解决了传统容器方案在 Apple Silicon Mac 上的适配问题——它利用 macOS 26 中新增的虚拟化与网络特性，使得 Linux 容器能够在 Mac 上以接近宿主机性能运行，同时保持 OCI（Open Container Initiative）标准兼容性。目标用户包括：在 Mac 上进行云原生开发的后端工程师、需要使用容器进行本地测试的 iOS 开发者，以及希望探索下一代容器化技术的开源爱好者。

## 核心功能

- **OCI 镜像兼容**：支持拉取、构建、推送和运行标准 OCI 容器镜像，可与 Docker Hub、GitHub Container Registry 等任何 OCI 兼容的注册表无缝协作。
- **轻量级虚拟机运行时**：每个容器运行在一个独立的、精简的虚拟机中，无需 Docker Desktop 或类似软件，直接利用 macOS 的 Virtualization.framework。
- **Apple Silicon 优化**：充分利用 M 系列芯片的硬件虚拟化特性，提供更低的延迟和更好的资源隔离，相比模拟方案性能提升显著。
- **Swift 原生实现**：底层依赖 Apple 开发的 [Containerization](https://github.com/apple/containerization) 包，提供容器的生命周期管理、镜像操作和进程控制等核心能力。
- **简易安装部署**：提供 macOS 原生的 .pkg 安装器签名包，一键安装，无需手动配置复杂依赖。
- **CLI 命令行交互**：通过简洁的命令行界面实现容器启动、停止、镜像管理等操作，适合自动化脚本和 CI/CD 集成。

## 技术架构

`container` 的核心技术栈基于 Swift，并深度依赖 macOS 系统的底层能力：

- **底层依赖**：使用 Apple 的 [Containerization](https://github.com/apple/containerization) 框架，该框架封装了容器运行时、镜像管理层和进程隔离机制，向上提供 Swift 原生 API。
- **虚拟化引擎**：调用 macOS 的 Virtualization.framework，实现虚拟机级别的资源隔离。每个容器被包装为一个独立的轻量 Linux 虚拟机，而不是传统意义上的“进程级容器”。
- **网络模型**：利用 macOS 26 中更新的网络扩展特性，为虚拟机提供高性能的网络接入，包括端口映射、DNS 解析及子网管理。
- **OCI 标准实现**：遵循 OCI Image Spec 和 Distribution Spec，镜像格式与 Docker 相同，支持增量层、压缩和签名验证。
- **Apple Silicon 原生**：针对 arm64 架构编译，无需 Rosetta 模拟，直接调用 Apple 芯片的虚拟化指令集，支持 Linux arm64 容器镜像。

架构设计上，`container` 通过 Swift 的强类型和安全性，简化了传统容器工具的复杂度，同时保持了 Mac 用户熟悉的原生体验。

## 安装与使用

### 安装要求

- 一台搭载 Apple Silicon 芯片（M1/M2/M3/M4 系列）的 Mac
- 操作系统：macOS 26 或更高版本（利用了该版本新增的虚拟化特性）
- 管理员权限（用于安装系统级扩展）

### 安装步骤

1. 访问 [GitHub release 页面](https://github.com/apple/container/releases)，下载最新的 `.pkg` 安装包。
2. 双击安装包，跟随向导完成安装。输入管理员密码以授权安装系统组件。
3. 安装完成后，打开终端验证工具可用：

```bash
container --version
```

### 最小可用示例

1. 拉取一个 Linux 容器镜像：

```bash
container pull alpine:latest
```

2. 运行一个基于 Alpine 的容器：

```bash
container run alpine:latest echo "Hello from container"
```

3. 查看正在运行的容器列表：

```bash
container ps
```

如需构建自定义镜像，可使用 `container build` 命令并指定 Dockerfile（OCI 兼容格式）。

## 适用场景

- **本地开发测试**：在 Mac 上快速拉起 Linux 环境，测试应用在 Docker 容器中的行为，无需切换虚拟机或使用远程服务器。
- **CI/CD 流水线集成**：在 macOS 构建机上运行容器化测试任务，利用 Apple Silicon 的高性能缩短构建时间。
- **教学和实验**：学习容器技术原理，了解 OCI 标准实现，以及 Swift 系统编程在底层虚拟化中的应用。
- **边缘计算场景**：为基于 Apple Silicon 的边缘设备（如 Mac mini 服务器）提供轻量级 Linux 运行时支持。

## 项目亮点

- **Apple 官方出品**：由 Apple 开源，以 Swift 原生实现，体现 Apple 对容器生态在 macOS 上的战略投入，未来可能与 Xcode 和其他开发工具深度集成。
- **性能优势**：相比使用 x86 兼容层或第三方虚拟化工具，`container` 直接调用 Apple 芯片的 arm64 虚拟化，消除模拟开销，容器启动和运行速度更快。
- **标准兼容但不失特色**：完全支持 OCI 标准，可复用现有 Docker 镜像和工具链，同时利用 macOS 26 的最新特性（如增强的网络隔离），提供比传统方案更干净的隔离环境。
- **轻量化部署**：无须 Docker 守护进程或庞大的运行时环境，安装包体积小，适合需要干净、可控的容器运行时的场景。
- **开源透明**：代码完全公开，Apache 2.0 许可证允许自由修改和商用，社区可自行审计安全性和性能。

## 相关链接

- [GitHub 仓库](https://github.com/apple/container)
- [Containerization 底层框架](https://github.com/apple/containerization)
- [OCI 镜像规范](https://github.com/opencontainers/image-spec)
