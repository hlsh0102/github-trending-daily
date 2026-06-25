---
tags:
  - trending
  - article
repo: apple/container
date: 2026-06-25
language: Swift
stars_total: 42545
stars_today: 1838
---
## 项目概述

`container` 是 Apple 推出的一款开源工具，专门用于在搭载 Apple 芯片的 Mac 上创建和运行 Linux 容器。它采用轻量级虚拟机技术，让开发者能够在 macOS 上以接近原生的性能运行 Linux 容器，且完全兼容 OCI（Open Container Initiative）镜像规范。

该项目解决了长期以来 Mac 开发者面临的一个核心痛点：在 macOS 上运行 Linux 容器时需要额外依赖 Docker Desktop 或其他虚拟机方案，这些方案往往存在性能开销大、资源占用高、启动慢等问题。`container` 充分利用 Apple 芯片的虚拟化能力，将容器直接封装为轻量级虚拟机，实现了高效、低延迟的 Linux 容器运行环境。

目标用户包括：需要在 Mac 上进行 Linux 容器开发与测试的软件工程师、DevOps 工程师、以及希望在不额外安装虚拟机管理器的前提下使用标准容器镜像的 macOS 用户。它特别适合那些已经在使用 Apple 芯片 Mac 并希望获得原生级容器体验的开发者。

## 核心功能

- **OCI 兼容镜像管理**：支持拉取、构建、推送和运行符合 OCI 镜像规范的容器镜像，可与 Docker Hub、GitHub Container Registry 等标准镜像仓库无缝协作。
- **轻量级虚拟机容器运行**：利用 Apple 芯片的虚拟化和网络增强特性，将 Linux 容器作为轻量级虚拟机直接运行，无需内核级容器运行时。
- **本地镜像构建**：支持基于 Dockerfile 或 OCI 标准规范在 Mac 上直接构建容器镜像，构建流程与主流容器工具保持一致。
- **高效资源调度**：针对 Apple 芯片进行了深度优化，在 CPU、内存和 I/O 方面实现接近原生的性能表现。
- **命令行接口**：提供简洁直观的命令行工具，支持 `run`、`pull`、`push`、`build` 等标准容器操作，学习成本低。
- **低依赖部署**：采用 Swift 编写，安装包为原生 macOS 安装程序，无需额外安装 Docker 或虚拟机软件。

## 技术架构

`container` 使用 Swift 语言编写，底层依赖 Apple 开源的 [Containerization](https://github.com/apple/containerization) Swift 包，该包提供了容器、镜像和进程管理的基础实现。整体架构设计围绕以下关键点展开：

- **虚拟机化容器**：与共享内核的 Linux 容器不同，`container` 为每个容器分配独立的轻量级虚拟机。每个虚拟机包含一个精简的 Linux 内核和用户空间，通过 Apple 芯片的虚拟化扩展（Virtualization.framework）实现硬件加速。
- **OCI 镜像规范**：完全遵循 OCI 镜像规范（image-spec）和运行时规范（runtime-spec），确保镜像的互操作性。镜像层存储、文件系统联合挂载等机制均基于标准实现。
- **Apple 芯片优化**：充分利用 macOS 26 中新增的虚拟化和网络增强特性，包括高性能虚拟网络设备和内存映射 I/O，减少虚拟化开销。
- **原生集成**：工具内部与 macOS 的 Hypervisor 框架直接交互，避免了额外中间层，启动速度和 I/O 性能显著优于传统嵌套虚拟化方案。

架构特点在于将容器管理、镜像管理和进程管理三者解耦，由 `Containerization` 包提供底层抽象，`container` 工具在此基础上实现面向用户的 CLI 接口。这种分层设计使得未来可以灵活扩展新的运行时特性。

## 安装与使用

### 安装步骤

1. 从 [GitHub Release 页面](https://github.com/apple/container/releases) 下载最新的 `.pkg` 安装包。
2. 双击安装包，按照提示完成安装。系统会要求输入管理员密码。
3. 安装完成后，可通过终端直接使用 `container` 命令。

**系统要求**：
- macOS 26 或更高版本
- Apple 芯片（M1、M2、M3 系列及后续版本）

### 最小可用示例

```bash
# 从 Docker Hub 拉取一个 Ubuntu 镜像
container pull docker.io/library/ubuntu:latest

# 运行 Ubuntu 容器
container run ubuntu:latest

# 进入容器后，运行标准 Linux 命令
# 在容器内：uname -a
# 在容器内：apt update
```

```bash
# 构建本地镜像
# 假设当前目录有一个 Dockerfile
container build -t my-app:latest .

# 推送镜像到 Docker Hub
container push my-app:latest docker.io/your-username/my-app:latest

# 列出本地镜像
container images

# 查看运行中的容器
container ps
```

## 适用场景

- **本地开发环境**：开发者可以在 Mac 上直接运行与生产环境一致的 Linux 容器，用于开发、调试和测试 Web 应用、微服务等。
- **CI/CD 流水线集成**：在 Mac 作为开发工作站时，使用 `container` 构建和测试容器镜像，确保镜像在推送到远程仓库前已经过本地验证。
- **学习与实验**：学生或爱好者可以在 Mac 上安全地运行多种 Linux 发行版，用于学习 Linux 系统管理、网络配置或容器技术。
- **离线容器管理**：对于无法访问 Docker Desktop 或希望减少依赖的场景，`container` 提供了一个轻量的替代方案，尤其适合安全敏感环境。

## 项目亮点

- **原生性能**：相比使用 Docker Desktop 等第三方工具，`container` 直接利用 Apple 芯片的虚拟化能力，在 CPU 和 I/O 吞吐量上实现了显著提升。
- **零额外依赖**：无需安装 Docker、虚拟机软件或额外内核扩展，安装包即可运行，简化了环境配置。
- **完全开放标准**：严格遵循 OCI 规范，确保与现有容器生态系统（Docker、Podman、Kubernetes 等）的互操作性。
- **Apple 官方维护**：由 Apple 核心团队开发维护，与 macOS 的未来更新保持同步，具有长期可靠性和稳定性。

## 相关链接

- [GitHub 仓库](https://github.com/apple/container)
- [Containerization Swift 包](https://github.com/apple/containerization)
- [OCI 镜像规范](https://github.com/opencontainers/image-spec)
