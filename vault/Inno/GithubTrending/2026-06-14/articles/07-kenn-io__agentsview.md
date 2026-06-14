---
tags:
  - trending
  - article
repo: kenn-io/agentsview
date: 2026-06-14
language: Go
stars_total: 2451
stars_today: 190
---
## 项目概述

agentsview 是一个本地优先的 AI 编程代理会话智能与数据分析工具。它解决了开发者在使用多种 AI 编程代理（如 Claude Code、Codex 等）时面临的会话碎片化、成本难以追踪、信息分散等问题。通过一个轻量级的二进制文件，即可完成对所有代理会话的浏览、搜索和成本统计，无需注册账户，所有数据均存储于本地。目标用户是使用 AI 编程代理辅助开发的程序员和团队，特别是那些同时使用多种代理工具的用户。

## 核心功能

- **会话浏览与搜索**：在一个统一的 Web UI 中查看所有代理的会话记录，支持关键词搜索和过滤。
- **成本追踪**：自动计算并汇总所有代理的每日、每周、每月使用成本，支持命令行快速查看。
- **多代理支持**：原生支持 Claude Code、Codex 等 20 多种主流编程代理，自动发现并整合数据。
- **本地优先**：所有数据存储在本地 SQLite 数据库中，无需第三方云服务，保障隐私安全。
- **100 倍性能提升**：作为 cusage 的替代品，在数据分析速度上有量级上的显著优势。
- **远程访问安全**：通过请求 Host 头验证和绑定 loopback 地址，抵御 DNS-rebinding 攻击，适应 SSH 端口转发、反向代理等远程场景。

## 技术架构

agentsview 使用 Go 语言开发，编译为单个可执行二进制文件，部署极为简便。其核心设计思路如下：

1. **本地数据库引擎**：采用 SQLite 作为存储后端，所有会话数据、使用记录和成本信息均以结构化方式存放于本地文件中，无需网络连接即可访问。
2. **自动发现机制**：启动时自动扫描用户机器上所有已支持的代理工具的会话目录（如 `~/.claude/projects`、`~/.forge` 等），解析会话文件并同步到数据库中。这一过程通过文件系统监听和定时扫描结合实现增量更新。
3. **Web 前端与 CLI 双模式**：既提供基于 Web 的图形界面（默认运行在 `http://127.0.0.1:8080`），也提供命令行工具（如 `agentsview usage daily`），满足不同使用习惯。
4. **多协议解析层**：每个代理的会话格式不同，agentsview 内部通过插件式解析器统一处理，支持超过 20 种代理的日志格式，并持续扩展。
5. **安全设计**：默认绑定到本地 loopback 地址，并校验请求的 Host 头，防止外部未授权访问。同时支持通过环境变量配置远程目录映射，适应开发容器或远程开发环境。

## 安装与使用

安装方式多样，可选择最适合的方式：

**一键安装（macOS / Linux）：**
```bash
curl -fsSL https://agentsview.io/install.sh | bash
```

**一键安装（Windows）：**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://agentsview.io/install.ps1 | iex"
```

**Homebrew（macOS）：**
```bash
brew install --cask agentsview
```

**Docker：**
```bash
docker run --rm -p 127.0.0.1:8080:8080 \
  -v agentsview-data:/data \
  -v "$HOME/.claude/projects:/agents/claude:ro" \
  -v "$HOME/.forge:/agents/forge:ro" \
  -e CLAUDE_PROJECTS_DIR=/agents/claude \
  -e FORGE_DIR=/agents/forge \
  ghcr.io/kenn-io/agentsview:latest
```

**最小可用示例：**
启动服务并查看每日成本：
```bash
agentsview serve           # 启动服务器，自动打开 Web UI
agentsview usage daily     # 在终端打印每日成本摘要
```

首次运行时会自动发现所有已支持的代理会话，同步到本地 SQLite 数据库，之后即可在 Web 界面中浏览、搜索和统计。

## 适用场景

1. **多代理开发工作流**：团队或个人同时使用 Claude Code、Codex、Cursor 等多种编程代理，需要统一查看所有项目会话记录和成本，避免数据分散。
2. **成本审计与优化**：企业需要监控 AI 编程代理的使用成本，分析哪些项目、任务或时段产生了高额费用，以便优化资源分配。
3. **远程开发环境**：使用 SSH 端口转发、CodeSpaces、exe.dev 等远程开发环境时，安全地访问本地会话数据，无需暴露服务到公网。
4. **本地优先的隐私敏感场景**：对将数据上传至云端有顾虑的开发组织，选择完全本地化的方案进行会话管理和成本追踪。

## 项目亮点

- **极致的本地化与隐私保护**：所有数据仅存在于用户本地，无需注册账户或联网，避免了云端存储带来的隐私风险。
- **广泛的多代理支持**：覆盖超过 20 种主流 AI 编程代理，是目前支持种类最丰富的本地工具之一，解决了代理碎片化问题。
- **惊人的性能提升**：作为 cusage 的替代品，在数据处理速度和查询响应上实现了 100 倍的提升，即使大量会话数据也能秒级响应。
- **单二进制部署**：编译后的单个可执行文件即可运行全部功能，无需安装 Node.js、Python 等依赖环境，极大简化了部署流程。
- **双模式交互**：同时提供强大的 Web UI 和便捷的 CLI 工具，满足图形界面和终端用户的各自偏好。

## 相关链接

- [GitHub 仓库](https://github.com/kenn-io/agentsview)
- [官方网站](https://agentsview.io)
- [GitHub Releases 下载页面](https://github.com/kenn-io/agentsview/releases)
