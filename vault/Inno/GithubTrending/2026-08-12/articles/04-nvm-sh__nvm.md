---
tags:
  - trending
  - article
repo: nvm-sh/nvm
date: 2026-08-12
language: Shell
stars_total: 94512
stars_today: 22
---
## 项目概述

NVM（Node Version Manager）是一个遵循 POSIX 标准的 bash 脚本，用于管理多个活动状态的 Node.js 版本。它解决了开发者在不同项目中需要切换不同 Node.js 版本的核心痛点——无论是为了兼容旧项目、测试新特性，还是满足特定框架对运行时版本的要求。nvm 的目标用户是使用类 Unix 操作系统（如 macOS、Linux 及 Windows Subsystem for Linux）的前端工程师、后端开发者、DevOps 人员以及任何需要在同一台机器上并行使用多个 Node.js 版本的技术从业者。

## 核心功能

- **多版本并行管理**：支持在系统中同时安装任意数量的 Node.js 版本，并通过简单命令即时切换当前使用的版本。
- **版本安装与下载**：直接通过 `nvm install <version>` 从官方源下载指定版本，支持语义化版本号（如 `14.0.0`）、LTS 代号（如 `lts/fermium`）以及 `node`（最新版）等便捷别名。
- **灵活切换机制**： `nvm use` 命令可在当前 shell 会话中临时切换版本；`nvm alias` 允许设置自定义别名（如 `default` 或 `project-stable`），并支持通过 `.nvmrc` 文件实现项目级别的自动版本选择。
- **全局包迁移**：在安装新版本时，可自动将旧版本中已安装的全局 npm 包迁移到新版本，避免重复安装。
- **离线安装支持**：对于无法直接访问互联网的环境，支持从本地缓存或预下载的二进制文件进行安装。
- **Shell 集成**：提供与 bash、zsh、fish 等主流 shell 的补全和提示集成，并支持在 `cd` 进入目录时自动读取 `.nvmrc` 切换版本。

## 技术架构

nvm 的核心是一个纯 bash 脚本实现，不依赖任何外部二进制或运行时。它通过修改 shell 的环境变量（特别是 `PATH`）来调整当前 shell 会话中 `node` 和 `npm` 命令的指向。当用户执行 `nvm use` 时，脚本会计算目标版本对应的安装目录，并将该目录的 `bin` 路径注入到 `PATH` 的最前端。这种设计使得版本切换无需修改实际的 Node.js 安装文件，仅需改变环境变量，因此切换过程极其快速且无副作用。nvm 自身存储于用户主目录下的 `~/.nvm` 文件夹中，每个 Node.js 版本分别安装在独立子目录内。安装脚本通过检查 `NVM_DIR` 环境变量来确定安装位置，并自动配置 shell 启动文件（如 `.bashrc`、`.zshrc`）以确保每次打开终端时 nvm 可用。此外，nvm 还实现了对系统架构（x86、x64、ARM 等）的自动检测，以选择正确的预编译二进制包。

## 安装与使用

**安装**（通过官方脚本）：
在终端中执行以下任意一种方式：

```bash
# 使用 cURL
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# 或使用 wget
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

安装完成后，重新加载 shell 配置（如 `source ~/.bashrc`）或重开终端。

**最小可用示例**：

```bash
# 检查是否安装成功
nvm --version

# 安装最新的 Node.js 20 LTS 版本
nvm install 20

# 查看已安装版本列表
nvm ls

# 切换到 Node.js 18
nvm use 18

# 设置默认版本（每次新 shell 自动使用）
nvm alias default 20

# 运行当前目录 .nvmrc 指定的版本
nvm use
```

## 适用场景

- **多项目并行开发**：本地同时维护多个前端或后端项目，各项目依赖不同的 Node.js 主版本（如一个需要 16.x，另一个需要 20.x），利用 nvm 可以随时无缝切换。
- **CI/CD 本地模拟**：在持续集成环境中通常需要在多个 Node.js 版本上运行测试，开发者可在本地通过 nvm 快速安装所需版本矩阵，复现构建和测试流程。
- **教学与实验环境**：学习或教授 Node.js 新特性时，不必担心影响既有开发环境，可以隔离版本安全地进行尝试。
- **遗留系统维护**：维护依赖较老 Node.js 版本（如 12.x）的遗留项目，同时在新项目中使用最新版本，避免因系统级 Node 版本升级导致生产事故。

## 项目亮点

- **零依赖纯 Shell 实现**：不依赖 Python、Ruby 或其他运行时，安装和运行开销极低，适用于最精简的服务器环境。
- **兼容性极广**：严格遵循 POSIX 标准，支持几乎所有 Linux 发行版、macOS 以及 Windows 的 WSL 环境。
- **社区标准地位**：作为 Node.js 官方推荐（在 nodejs.org 安装指南中明确建议）的版本管理器，超过 9 万 Stars 的 GitHub 仓库，拥有极高的可信度和活跃维护。
- **丰富的生态集成**：支持 `nvm ls-remote` 查看远程可用列表、`.nvmrc` 文件自动加载、`nvm exec` 以指定版本运行子命令等高级功能，满足从初学者到高级用户的需求。
- **与 CI 工具良好协同**：提供 Docker 安装示例以及针对 GitHub Actions 等环境的优化建议，便于将版本管理策略编入自动化流程。

## 相关链接

- [GitHub 仓库](https://github.com/nvm-sh/nvm)
- [项目 Logo 及版权信息](https://github.com/nvm-sh/logos)
- [OpenSSF 最佳实践状态](https://bestpractices.dev/projects/684)
