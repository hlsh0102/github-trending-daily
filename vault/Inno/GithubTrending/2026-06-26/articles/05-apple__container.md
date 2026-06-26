---
tags:
  - trending
  - article
repo: apple/container
date: 2026-06-26
language: Swift
stars_total: 43347
stars_today: 1351
---
## 项目概述

`container` 是 Apple 官方推出的一款用于在 Mac 上创建和运行 Linux 容器的工具。它将轻量级虚拟机技术与容器化理念相结合，使用户能够在 Apple Silicon 架构的 Mac 上高效地运行标准 Linux 容器。该项目完全由 Swift 语言编写，并针对 Apple Silicon 芯片进行了深度优化。

该项目主要解决了一个长期存在的痛点：在 macOS 上运行 Linux 容器通常需要借助 Docker Desktop 等第三方工具，这些工具往往需要额外的虚拟机层，性能开销较大。`container` 利用 macOS 原生的虚拟化框架，直接创建轻量级 Linux 虚拟机来运行容器，大幅减少了性能损失。

目标用户包括：macOS 开发者、DevOps 工程师、系统管理员以及任何需要在 Apple Silicon Mac 上以接近原生速度运行 Linux 容器的人群。对于依赖容器化技术进行开发测试、持续集成/部署（CI/CD）的用户来说，这是一个非常有吸引力的原生方案。

## 核心功能

- **原生容器运行**：在 Apple Silicon Mac 上直接运行 Linux 容器，无需安装或配置 Docker Desktop 等额外软件。
- **OCI 兼容**：完全兼容 Open Container Initiative（OCI）镜像规范，可以从 Docker Hub、GitHub Container Registry 等标准容器仓库拉取和推送镜像。
- **轻量级虚拟机**：利用 macOS 的虚拟化框架创建极简的 Linux 虚拟机，仅包含运行容器所需的最小系统组件，启动速度快，资源占用低。
- **镜像构建与管理**：支持基于标准 OCI 格式构建自定义容器镜像，并提供完整的镜像生命周期管理功能。
- **自动化安装**：提供 macOS 原生的 .pkg 安装包，支持通过双击安装或命令行静默安装，便于企业级批量部署。
- **进程与网络管理**：集成 Containerization Swift 包，实现底层的容器进程隔离和网络配置，确保容器运行的安全性和稳定性。

## 技术架构

`container` 的技术架构体现了 Apple 对性能和简洁性的追求。核心组件基于 [Containerization](https://github.com/apple/containerization) Swift 包，这是一个低层次的容器化工具库，负责处理容器、镜像和进程管理的底层细节。

从架构上看，`container` 的工作流程如下：
1. **镜像拉取**：通过 OCI 标准从远程仓库拉取容器镜像。
2. **虚拟机创建**：使用 macOS 的 `Virtualization.framework` 创建一个精简的 Linux 虚拟机。该虚拟机不含完整桌面环境，仅包含运行容器所需的内核和初始化系统。
3. **容器化运行**：在虚拟机的隔离环境中启动容器进程，确保与宿主机 macOS 完全隔离。
4. **网络桥接**：通过虚拟网络接口将容器网络暴露给宿主机，实现端口映射和通信。

由于完全基于 Apple 原生库编写，`container` 能够充分利用 Apple Silicon 芯片的硬件加速能力（如虚拟化扩展、统一内存架构），相较于 x86 模拟方案，性能提升显著。

## 安装与使用

### 系统要求
- Apple Silicon 芯片的 Mac（M1、M2、M3 系列）
- macOS 26（Sequoia 或更高版本）
- 管理员权限

### 安装步骤
1. 访问 [GitHub 发布页面](https://github.com/apple/container/releases) 下载最新的 .pkg 安装包。
2. 双击安装包，按照提示输入管理员密码完成安装。
3. 安装完成后，在终端中执行 `container` 命令验证是否成功。

### 最小可用示例
```bash
# 拉取一个官方 Ubuntu 镜像
container pull ubuntu:latest

# 运行一个交互式 Ubuntu 容器
container run -it ubuntu:latest /bin/bash

# 运行一个后台 Nginx 容器并映射端口
container run -d -p 8080:80 nginx:latest
```

`container` 的命令行接口与 Docker 类似，但更简洁。它默认使用符合 OCI 标准的 Docker Hub 镜像仓库，用户也可以指定其他私有仓库。

## 适用场景

- **本地开发与测试**：开发者在本地 Mac 上快速启动一个轻量级 Linux 环境，用于测试 Python、Node.js、Go 等应用，无需配置复杂的虚拟机或双系统。
- **持续集成与部署**：在 macOS 的 CI/CD 流水线中运行 Linux 容器化构建任务，利用统一的容器环境确保构建一致性。
- **教育与培训**：教学环境中，讲师和学员可以在自己的 Mac 上快速创建隔离的实验环境，无需安装额外的虚拟化软件。
- **隔离运行服务**：在开发或演示环境中，将不同微服务隔离在独立的容器中运行，每个服务拥有独立的文件系统和网络栈。

## 项目亮点

与 Docker Desktop、Podman 等同类工具相比，`container` 具有以下差异化优势：

- **原生性能**：完全基于 macOS 原生虚拟化框架，无额外的中间虚拟化层，CPU 和内存开销更小。
- **轻量级设计**：安装包仅包含必要组件，不像 Docker Desktop 那样捆绑了完整的 Linux 虚拟机、Kubernetes 集群等臃肿功能。
- **Apple 官方支持**：由 Apple 官方团队开发和维护，与 macOS 生态系统深度集成，未来版本兼容性有保障。
- **Swift 原生实现**：完全使用 Swift 语言编写，对于 Swift 开发者来说，代码更易理解和贡献。
- **OCI 标准兼容**：确保与现有容器生态无缝对接，可复用已有镜像和仓库。

## 相关链接

- [GitHub 仓库](https://github.com/apple/container)
- [Containerization Swift 包](https://github.com/apple/containerization)
