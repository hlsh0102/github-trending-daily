---
tags:
  - trending
  - article
repo: agalwood/Motrix
date: 2026-08-19
language: TypeScript
stars_total: 53747
stars_today: 609
---
## 项目概述

Motrix 是一款现代化、功能全面的开源下载管理器，支持 HTTP、FTP、BitTorrent 和磁力链接等多种下载协议。它以简洁直观的用户界面为核心设计理念，旨在为用户提供无需学习成本即可上手的下载体验。Motrix 适用于 macOS、Windows 和 Linux 三大桌面平台，同时提供无头服务器模式，可运行在 NAS 或家庭服务器上。

目前 Motrix v2（代号 Motrix Turbo）正处于 Beta 测试阶段。v2 从底层重构，采用 Electron、React 和 TypeScript 技术栈，在保留 v1 简洁体验的基础上，将下载核心与 UI 完全解耦，并引入了开放的通信协议与插件沙箱机制，为扩展生态奠定了基础。

## 核心功能

- **多协议支持**：原生支持 HTTP、FTP、BitTorrent 和磁力链接，覆盖主流下载场景。
- **桌面应用与无头服务器双模式**：同一套下载核心既可运行于桌面环境，也可作为无界面服务部署在 Node.js 或 Docker 中，并附带 Web UI 供远程管理。
- **MDXP 开放协议**：基于 JSON-RPC 2.0 构建的 Motrix Download eXchange Protocol，允许浏览器扩展、命令行工具等外部程序通过标准接口与下载核心通信。
- **插件沙箱隔离**：插件在独立沙箱环境中运行，与主进程隔离，提升安全性和稳定性。
- **现代化界面**：基于 React 构建的干净、直观的用户界面，操作逻辑清晰，无冗余功能。
- **跨平台一致性**：桌面应用在 macOS、Windows 和 Linux 上提供一致的体验，无头服务器则确保在无图形环境下功能完整。

## 技术架构

Motrix v2 的架构设计遵循“核心与 UI 分离”的原则。下载核心独立于界面层，通过定义良好的接口与外部通信。这一设计带来了几个关键优势：

1. **解耦与可扩展性**：核心不依赖任何特定 UI 框架，使得桌面应用、Web UI、命令行工具和浏览器扩展可以共享同一套下载能力。
2. **MDXP 协议**：作为基于 JSON-RPC 2.0 的开放协议，MDXP 为所有客户端提供了统一的调用入口。无论是浏览器扩展还是 CLI 工具，都通过标准 JSON 消息与核心交互，降低了集成门槛。
3. **插件沙箱**：插件运行在隔离的沙箱环境中，即便是恶意或异常插件也无法直接影响核心进程，保障了整体稳定性。
4. **技术栈**：前端采用 Electron 与 React 构建跨平台桌面壳，TypeScript 提供类型安全，提升代码维护性。无头服务器模式则直接运行于 Node.js，且支持 Docker 容器化部署。

## 安装与使用

**桌面应用**：从 [GitHub Releases](https://github.com/agalwood/Motrix/releases) 下载对应平台的安装包（macOS 的 dmg、Windows 的 exe、Linux 的 AppImage 或 deb），安装后即可启动。

**无头服务器（Docker）**：

```bash
docker run -d \
  --name motrix \
  -p 16800:16800 \
  -v ~/motrix-data:/root/.config/Motrix \
  -v ~/downloads:/downloads \
  agalwood/motrix:latest
```

启动后通过浏览器访问 `http://localhost:16800` 使用 Web UI 管理下载任务。

**命令行工具**（示例）：安装 motrix-cli 后，可通过以下命令添加下载任务：

```bash
motrix add https://example.com/file.zip
```

**浏览器扩展**：安装 Motrix 浏览器扩展后，可自动接管浏览器下载请求，转发至 Motrix 核心处理。

## 适用场景

1. **日常文件下载**：替代浏览器内置下载器，获得更快的速度和更稳定的断点续传能力。
2. **BT/磁力资源获取**：直接下载 BitTorrent 文件或磁力链接，无需额外安装 BT 客户端。
3. **NAS 与家庭服务器**：通过 Docker 部署无头服务，结合 Web UI 实现集中式下载管理，并支持远程访问。
4. **自动化集成**：开发人员可利用 MDXP 协议或 CLI 工具将 Motrix 集成到脚本或自动化流程中，实现批量下载任务。

## 项目亮点

- **极简但不简陋**：Motrix 的界面设计去除了所有不必要元素，但功能上覆盖了绝大多数下载需求，没有为简洁牺牲能力。
- **开放协议与生态**：MDXP 协议是公开的，第三方开发者可以自由构建客户端、扩展或集成方案，形成一个开放的下载生态系统。
- **双模式架构**：桌面与无头服务器的双模式设计，使得同一套代码既能满足个人桌面用户，也能服务服务器场景，降低了开发和维护成本。
- **重构的技术基础**：v2 采用 TypeScript 与 React 重写，代码质量和可维护性显著提升，为长期迭代打下坚实基础。

## 相关链接

- [GitHub 仓库](https://github.com/agalwood/Motrix)
- [v2.0.0-beta.19 发布说明](https://github.com/agalwood/Motrix/releases/tag/v2.0.0-beta.19)
- [简体中文 README](https://github.com/agalwood/Motrix/blob/master/README.zh-CN.md)
