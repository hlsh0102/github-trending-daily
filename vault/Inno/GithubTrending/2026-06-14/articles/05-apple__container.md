---
tags:
  - trending
  - article
repo: apple/container
date: 2026-06-14
language: Swift
stars_total: 36504
stars_today: 1487
---
## 项目概述

`container` 是由 Apple 开发的开源工具，专注于在 Mac 上通过轻量级虚拟机创建和运行 Linux 容器。该项目使用 Swift 编写，针对 Apple 硅芯片进行了深度优化，旨在为 macOS 用户提供原生的容器化体验。

该项目解决了在 macOS 上运行 Linux 容器的性能与兼容性问题。传统方式依赖 Docker Desktop 等第三方工具或通过 x86 模拟运行，而 `container` 直接利用 Apple 硅芯片的虚拟化特性，实现了接近原生的容器执行效率。目标用户包括 macOS 上的开发者、DevOps 工程师以及希望在本地测试或运行 Linux 工作负载的技术人员。

`container` 完全兼容 OCI（Open Container Initiative）镜像规范，这意味着它可以与任何标准容器注册表（如 Docker Hub、GitHub Container Registry）无缝协作。用户可以拉取、运行、构建和推送 OCI 镜像，并将其与其他 OCI 兼容工具（如 Docker 或 Podman）互操作。

## 核心功能

- **原生 macOS 容器运行**：基于 Apple 硅芯片的虚拟化框架，在 macOS 上直接启动 Linux 容器，无需额外虚拟机或模拟层。
- **OCI 镜像兼容**：支持拉取、构建、推送和运行 OCI 标准容器镜像，与主流容器生态完全互通。
- **轻量级虚拟机管理**：每个容器运行在独立的轻量级虚拟机中，提供严格隔离，同时资源开销极低。
- **Swift 原生开发**：使用 Swift 语言编写，并基于 [Containerization](https://github.com/apple/containerization) 包进行底层管理，与 Apple 生态深度集成。
- **macOS 26 优化**：专为 macOS 26 设计，利用该版本新增的虚拟化和网络功能，提供最佳性能和稳定性。

## 技术架构

`container` 的核心设计基于 Apple 硅芯片的虚拟化能力。它通过 macOS 的 Hypervisor 框架和 Virtualization 框架，在用户态创建轻量级虚拟机，每个虚拟机内运行一个精简的 Linux 内核实例，从而承载容器进程。

项目使用 Swift 作为主要开发语言，这带来了内存安全和并发性能优势。底层依赖 [Containerization](https://github.com/apple/containerization) Swift 包，该包处理容器镜像的拉取、存储、挂载以及进程管理等低级操作。这种分层设计使 `container` 专注于上层逻辑，同时保持与 OCI 标准的兼容性。

在镜像管理方面，`container` 遵循 OCI 镜像规范，使用标准化的 manifest 和 layer 结构。网络方面，它充分利用 macOS 26 的新特性，为容器提供高效的网络隔离和端口映射。存储方面，采用 overlayfs 或类似技术实现写时复制，确保容器启动快速且资源占用少。

## 安装与使用

### 安装要求

- 一台搭载 Apple 硅芯片（M1 或更新）的 Mac 电脑。
- macOS 26 或更高版本。
- 如需从源码构建，请参考项目中的 [BUILDING.md](https://github.com/apple/container/blob/main/BUILDING.md) 文档。

### 安装步骤

1. 从 [GitHub Release 页面](https://github.com/apple/container/releases) 下载最新的 `.pkg` 安装包。
2. 双击安装包，按提示完成安装（需要管理员权限）。
3. 安装完成后，`container` 命令即可在终端中使用。

### 最小可用示例

拉取并运行一个 Ubuntu 容器：

```bash
# 拉取 Ubuntu 镜像
container pull ubuntu:latest

# 运行容器并进入交互式 shell
container run -it ubuntu:latest /bin/bash
```

构建并推送自定义镜像：

```bash
# 使用 Dockerfile 构建（假设当前目录有 Dockerfile）
container build -t myapp:latest .

# 推送到注册表（使用之前登录凭证）
container push myapp:latest
```

## 适用场景

- **本地开发与测试**：开发者在 macOS 上需要运行 Linux 环境进行应用开发、调试或测试，使用 `container` 可以快速启动隔离的容器实例，无需切换操作系统或使用远程服务器。
- **CI/CD 流水线本地模拟**：团队在持续集成中使用 Linux 容器，开发者可以通过 `container` 在本地模拟 CI 环境，验证构建和测试步骤，减少远程调试成本。
- **多平台兼容性验证**：需要验证应用在不同 Linux 发行版（如 Ubuntu、Alpine、CentOS）上的行为时，可以快速拉取对应镜像并运行，确保跨平台兼容性。
- **轻量级服务部署**：在个人开发机上运行微服务、数据库或工具链容器，利用轻量级虚拟机提供隔离性，同时保持 Mac 系统的流畅运行。

## 项目亮点

- **Apple 原生支持**：由 Apple 官方开发并维护，深度集成 macOS 和 Apple 硅芯片特性，性能和稳定性有保障。
- **零模拟开销**：直接使用虚拟化硬件加速，无需软件模拟 x86 指令集，运行 Linux 容器时几乎达到原生速度。
- **OCI 生态兼容**：完全遵循 OCI 标准，与现有容器工具和镜像注册表互通，用户无需学习新镜像格式或修改工作流。
- **Swift 代码质量**：代码库以 Swift 编写，遵循现代语言特性，易于阅读、调试和扩展，为 Apple 生态开发者提供了良好的二次开发基础。
- **专为 macOS 26 设计**：利用最新 macOS 的虚拟化和网络增强功能，避免兼容旧版本带来的性能或功能限制。

## 相关链接

- [GitHub 仓库](https://github.com/apple/container)
- [Apple 容器化 Swift 包](https://github.com/apple/containerization)
