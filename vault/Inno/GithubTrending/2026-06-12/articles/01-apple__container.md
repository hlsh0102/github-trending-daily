---
tags:
  - trending
  - article
repo: apple/container
date: 2026-06-12
language: Swift
stars_total: 33461
stars_today: 2430
---
## 项目概述

`container` 是苹果公司开源的一款命令行工具，专门用于在 Mac 上创建和运行 Linux 容器。与传统容器方案不同，它将每个容器作为轻量级虚拟机来运行，而非共享宿主机内核。项目完全使用 Swift 编写，并针对 Apple Silicon 芯片进行了深度优化。它解决了在 macOS 上原生运行 Linux 容器时面临的虚拟化性能与兼容性问题，目标用户包括需要在本地开发、测试或运行 Linux 应用的 macOS 开发者，以及希望获得接近原生性能的容器化工作负载的运维人员。

## 核心功能

- **OCI 兼容性**：完全遵循 OCI 镜像规范，支持从任意标准容器仓库拉取和推送镜像，也能运行其他 OCI 应用构建的镜像，实现生态互操作。
- **轻量级虚拟机运行**：利用 macOS 26 最新的虚拟化功能，每个容器作为独立虚拟机启动，拥有独立内核，提供接近原生的 Linux 环境运行体验。
- **高效资源管理**：针对 Apple Silicon 的 unified memory 架构进行优化，减少内存和 CPU 开销，支持高效的启动和运行。
- **镜像构建与推送**：支持从 Dockerfile 或自定义配置构建容器镜像，并能将构建结果推送到公有或私有容器仓库。
- **网络与存储集成**：内置对虚拟网络和持久化存储的支持，容器可以像本地进程一样访问网络，数据可以持久化保存。

## 技术架构

`container` 的核心架构基于两层设计：底层依赖 [Containerization](https://github.com/apple/containerization) Swift 包，该包负责处理容器和镜像的底层管理，包括 OCI 镜像的解析、层管理、沙箱隔离等。上层则是 `container` 工具本身，提供简洁的命令行接口和用户交互。

技术关键点包括：
- **虚拟化引擎**：完全使用 macOS 原生的 Virtualization.framework，无需额外安装 QEMU 或其他虚拟化软件，从而获得 Apple Silicon 硬件加速能力。
- **OCI 镜像处理**：原生支持 OCI 镜像规范，包括 manifest、layer 压缩与解压缩、config 处理等，确保与 Docker、Podman 等主流工具的互操作性。
- **进程管理**：每个容器作为独立虚拟机进程运行，由 `container` 负责生命周期管理，包括启动、停止、快照和销毁。
- **网络**：使用 macOS 26 的新网络功能，为每个容器分配独立的虚拟网络接口，支持端口映射和网络隔离。

## 安装与使用

### 安装要求
- 一台搭载 Apple Silicon（M1、M2、M3 等）的 Mac
- macOS 26 或更高版本（必须，因为依赖该版本新增的虚拟化与网络功能）

### 安装步骤
1. 前往 [GitHub Release 页面](https://github.com/apple/container/releases) 下载最新版本的 signed installer 包。
2. 双击 `.pkg` 文件，按提示输入管理员密码完成安装。

### 最小可用示例
安装完成后，即可使用 `container` 命令。

**拉取并运行一个 Alpine 容器：**
```bash
container pull alpine:latest
container run alpine:latest /bin/sh
```

**构建并推送镜像：**
```bash
# 假设当前目录包含 Dockerfile
container build -t myapp:latest .
container push myapp:latest
```

**列出正在运行的容器：**
```bash
container ps
```

**停止容器：**
```bash
container stop <container-id>
```

所有命令都支持 `--help` 参数查看详细选项。

## 适用场景

1. **本地开发与测试**：开发者可以在 Mac 上直接运行 Linux 容器进行应用开发、调试和测试，无需启动完整的 Linux 虚拟机或使用 Docker Desktop 等第三方方案。特别适合使用 Linux 原生工具链（如 GCC、Python 特定版本）的项目。

2. **CI/CD 环境管理**：在 macOS 构建机上运行容器化构建任务，可以利用 Apple Silicon 的高性能同时确保环境一致性。

3. **Linux 应用迁移**：需要将依赖 Linux 内核特性的服务（如某些数据库、网络工具）迁移到 macOS 环境时，使用 `container` 提供接近原生的运行体验，避免性能损失。

4. **学习和实验**：安全地创建隔离的 Linux 环境进行系统管理、安全测试或学习，无需担心影响宿主机。

## 项目亮点

- **完全官方支持**：由苹果公司开发和维护，深度集成 macOS 26 的虚拟化新特性，性能和兼容性有官方保障。
- **零依赖虚拟化**：不依赖 Docker、VirtualBox、QEMU 等第三方软件，仅使用 macOS 原生框架，安装即用。
- **OCI 标准兼容**：与 Docker 生态无缝对接，可以直接使用现有的大量容器镜像和工具链，迁移成本极低。
- **纯 Swift 实现**：利用 Swift 的性能和安全性特点，代码质量高，同时便于开发者参与贡献和二次开发。
- **面向未来**：针对 Apple Silicon 的 architecture 和 memory model 进行了专门优化，性能表现优于通用的 x86 模拟方案。

## 相关链接
- [GitHub 仓库](https://github.com/apple/container)
- [Containerization Swift 包](https://github.com/apple/containerization)
