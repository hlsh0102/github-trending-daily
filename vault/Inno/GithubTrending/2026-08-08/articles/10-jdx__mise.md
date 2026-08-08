---
tags:
  - trending
  - article
repo: jdx/mise
date: 2026-08-08
language: Rust
stars_total: 32091
stars_today: 135
---
## 项目概述

mise（全称 mise-en-place，源自法语“准备就绪”之意）是一个用 Rust 编写的高效开发工具管理器。它将开发工具版本管理、环境变量管理和任务运行器整合到一个统一的命令行工具中，解决了开发者在不同项目间切换时需要手动管理工具链版本、环境配置和执行重复任务的痛点。

对于开发者而言，mise 意味着可以用一个工具替代 `asdf`、`direnv`、`make` 等多家工具的集合，从而简化工作流程，减少配置文件的碎片化。无论你是个人开发者、团队协作成员，还是 CI/CD 管道的维护者，mise 都能帮助你更清晰地定义和复现项目所需的完整开发环境。

## 核心功能

- **多语言工具版本管理**：支持 Node.js、Python、Ruby、Go、Java 等主流语言及数百种 CLI 工具的版本安装与切换，每个项目可独立指定所需版本。
- **环境变量管理**：基于目录上下文自动加载 `.env` 文件或 `.mise.toml` 中定义的全局/项目级环境变量，无需额外的 direnv 类工具。
- **任务运行器**：内置任务定义与执行能力，可替代 make/just 等传统任务工具，支持任务依赖、参数传递和条件执行。
- **配置文件即代码**：以 `.mise.toml` 作为项目配置文件，支持 TOML 格式声明工具版本、环境变量和任务，方便版本控制与团队共享。
- **全局与项目级作用域**：平衡全局工具安装与项目隔离，支持 `--global` 和 `--project` 标志，轻松在不同作用域间切换。
- **快速 shell 集成**：提供针对 bash、zsh、fish、powershell 的 shell 钩子，实现进入目录时自动激活对应环境，无需手动 source。

## 技术架构

mise 完全使用 Rust 编写，继承了 Rust 在性能、内存安全和并发方面的优势。其核心架构围绕三个模块构建：

1. **版本解析与下载引擎**：mise 实现了自己的版本解析算法和下载管理逻辑，支持多种下载源（如 GitHub Releases、官方 CDN），并提供了后台预取和缓存机制，确保工具安装快速且可离线使用。

2. **文件系统监听与 shell 集成**：mise 通过 shell 钩子（hook）与用户的 shell 会话进行通信。当用户切换目录时，shell 钩子触发 mise 来读取 `.mise.toml`，并动态调整 `PATH`、`GEM_PATH` 等环境变量。该机制基于事件驱动，避免了冗余的轮询操作。

3. **配置解析与依赖图**：mise 将 `.mise.toml` 解析为内部数据结构，构建工具、环境变量和任务之间的依赖关系。任务运行器支持并行执行和错误传播，可以保证在多任务场景下的执行效率。

mise 设计上遵循“约定优于配置”的原则，大多数操作有默认值，同时提供 `mise settings` 命令允许用户微调行为。整个 CLI 的交互设计注重反馈清晰度，错误信息包含具体的解决建议。

## 安装与使用

mise 支持多种安装方式，包括包管理器（如 Homebrew、apt、cargo）、脚本安装或直接下载二进制。以 curl 脚本安装为例：

```bash
curl https://mise.run | sh
```

安装完成后，将 mise 添加到 shell 配置（以 bash 为例）：

```bash
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
source ~/.bashrc
```

初始化一个项目，定义 Node.js 版本和任务：

```bash
cd myproject
mise use node@20          # 安装并锁定 Node.js 20.x
mise env NODE_ENV=production  # 设置环境变量（可选）
```

创建 `mise.toml` 文件并编写任务：

```toml
[env]
NODE_ENV = "production"

[tasks.build]
run = "npm run build"
```

然后执行任务：

```bash
mise run build
```

常用命令还包括 `mise install`（安装全部依赖工具）、`mise ls`（列出已安装工具）以及 `mise outdated`（检查可更新版本）。

## 适用场景

- **多项目多语言环境隔离**：若你同时维护数个使用不同语言或版本的项目（如一个项目用 Python 3.11，另一个用 Python 3.9），mise 可自动切换，无需手动修改 PATH。
- **团队开发环境标准化**：通过 `.mise.toml` 将完整的工具链及环境变量提交至仓库，新成员拉取代码后只需运行 `mise install` 即可获得完全一致的开发环境。
- **本地开发与 CI 的一致性**：在 CI 流水线中使用 mise 安装依赖，确保部署和本地使用相同的工具版本，减少“环境不一致导致的问题”。
- **替代脚本引擎的任务编排**：对于复杂且依赖于环境变量的工作流，mise 的任务运行器可以集中管理，避免编写冗长的 shell 脚本。

## 项目亮点

- **Rust 带来的性能优势**：与基于 Ruby 的 asdf 或基于 Go 的 direnv 不同，mise 在解析配置、执行命令和 shell 启动检测上响应更快，尤其在大型仓库中感知明显。
- **三合一功能融合**：将版本管理、环境变量和任务执行统一到一个工具，配置文件单一，逻辑内聚，比分开使用多个工具的心智负担更低。
- **友好的迁移路径**：提供从 asdf 和 direnv 的自动迁移命令（`mise migrate`），用户可以从现有工具链平滑过渡，降低转换成本。
- **活跃的社区与商业支持**：项目已获得 32k+ star，拥有 Discord 社区和商业赞助，开发活跃度高，且定期发布新版本。

## 相关链接

- [GitHub 仓库](https://github.com/jdx/mise)
- [官方文档](https://mise.jdx.dev)
- [快速开始指南](https://mise.jdx.dev/getting-started.html)
- [Discord 社区](https://discord.gg/mABnUDvP57)
