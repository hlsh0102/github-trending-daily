---
tags:
  - trending
  - article
repo: akitaonrails/ai-memory
date: 2026-08-18
language: Rust
stars_total: 2182
stars_today: 207
---
## 项目概述

ai-memory 是一个为 AI 编码代理（coding agent）提供长期记忆的解决方案，旨在解决多代理协作场景下的上下文丢失问题。当开发者使用 Claude Code 中途暂停任务，切换到 OpenAI Codex 继续同一个项目时，以往需要手动重新描述架构设计、失败的尝试和待解决问题。ai-memory 通过持久化记忆机制，让不同的 AI 代理能够共享项目上下文，实现无缝交接。该项目使用 Rust 编写，采用 MIT 许可证开源，目前已在 GitHub 上获得超过 2000 星标，增长势头显著。目标用户包括使用 AI 辅助编程的专业开发者、技术团队以及依赖多种代理工具进行开发的工程师。

## 核心功能

- **跨代理记忆持久化**：支持在不同 AI 编码代理（如 Claude Code、OpenAI Codex）之间共享项目记忆，避免重复解释上下文
- **任务状态追踪**：自动记录任务进度、已完成的工作、失败的方案和未解决的问题，便于后续会话快速恢复
- **会话无缝交接**：支持在同一目录下切换代理继续工作，无需重新初始化上下文
- **多平台支持**：完整支持 Linux、macOS 和 Windows（通过 WSL2），原生 Windows 版本提供实验性支持
- **Docker 部署**：官方提供 linux/amd64 和 linux/arm64 的 Docker 镜像，方便服务端部署
- **原生包分发**：为 Arch Linux 提供 AUR 包，为 macOS 提供原生二进制，支持自定义安装路径

## 技术架构

ai-memory 采用 Rust 编写，利用其内存安全和并发性能优势，确保记忆读写的高效性。项目设计上遵循“本地优先”原则，将记忆数据存储在项目目录内，保持与工作目录的强关联。架构分为几个关键层次：

- **记忆存储层**：通过结构化的数据格式保存项目状态、架构信息和决策记录，支持快速的序列化和反序列化
- **代理适配层**：为不同的 AI 代理提供统一的接口，使 Claude Code、OpenAI Codex 等工具能以各自的 hook 机制接入记忆读写
- **命令行界面**：提供直观的 CLI 工具，让用户可以主动管理记忆内容，查看或修改存储的状态数据
- **系统服务集成**：在 Linux/macOS 上支持 systemd 用户服务，实现后台持久化运行，确保记忆实时更新

这种分层设计使 ai-memory 能够灵活适配不同代理的 hook 规范，而无需修改代理本身的代码。同时，Rust 的高性能和低资源占用特性，使其适合作为常驻后台进程运行。

## 安装与使用

安装 ai-memory 有多种方式，以下介绍最常见的几种：

**macOS 原生安装**（推荐 Apple Silicon 用户）：

```bash
# 下载最新发布版本
curl -L -o ai-memory.tar.gz https://github.com/akitaonrails/ai-memory/releases/latest/download/ai-memory-macos-aarch64.tar.gz
tar -xzf ai-memory.tar.gz
sudo mv ai-memory /usr/local/bin/
```

**Linux Docker 部署**：

```bash
docker pull ghcr.io/akitaonrails/ai-memory:latest
docker run -d --name ai-memory -v $(pwd):/workspace ai-memory
```

**Arch Linux（AUR）安装**：

```bash
yay -S ai-memory
systemctl --user enable --now ai-memory
```

**最小可用示例**：

```bash
# 在工作目录中初始化记忆
cd your-project
ai-memory init

# 查看当前记忆状态
ai-memory show

# 记录一个决策
ai-memory record "采用 Rust 重写核心模块，因为性能瓶颈在解析环节"

# 切换代理后恢复上下文
ai-memory context load
```

对于具体的代理配置（如 Claude Code 的 hook 设置），请参考项目的 `docs/` 目录下的详细文档。

## 适用场景

1. **多代理协作开发**：团队中不同开发者偏好不同的 AI 编码代理，ai-memory 确保所有代理能够共享项目上下文，减少沟通成本
2. **长时间任务中断恢复**：当大型重构或复杂调试被中断，需要隔天或隔周继续时，代理能够快速恢复到之前的思维状态
3. **CI/CD 集成**：在自动化流水线中嵌入 ai-memory，让不同阶段的 AI 辅助任务能够衔接，例如代码审查与自动修复
4. **多项目并行管理**：开发者在多个项目间频繁切换，ai-memory 按目录隔离记忆，避免不同项目的上下文互相干扰

## 项目亮点

与同类工具相比，ai-memory 有几个显著优势：

- **代理无关性**：不像一些方案绑定特定 AI 供应商，ai-memory 设计上与代理解耦，支持任意符合 hook 协议的代理
- **原生性能**：使用 Rust 实现，资源占用低、响应快速，适合常驻运行
- **跨平台完善**：从 Linux 服务器到 macOS 桌面再到 Windows WSL2，覆盖主流开发环境，并针对每种平台提供专门的优化方案
- **开发活跃**：项目正处于快速增长期，社区反馈积极，迭代速度快
- **安全透明**：数据存储于本地项目目录，开发者拥有完全控制权，没有云端存储的隐私顾虑

## 相关链接

- [GitHub 仓库](https://github.com/akitaonrails/ai-memory)
- [macOS 使用指南](https://github.com/akitaonrails/ai-memory/blob/main/docs/macos.md)
- [发布版本页面](https://github.com/akitaonrails/ai-memory/releases)
