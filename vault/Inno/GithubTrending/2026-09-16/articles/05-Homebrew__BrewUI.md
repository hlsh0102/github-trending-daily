---
tags:
  - trending
  - article
repo: Homebrew/BrewUI
date: 2026-09-16
language: Swift
stars_total: 1599
stars_today: 271
---
## 项目概述

BrewUI 是 Homebrew 官方推出的 macOS 图形界面应用，使用 Swift 编写。Homebrew 长期以命令行工具的形式存在，虽然功能强大，但对不熟悉终端的用户存在较高的使用门槛。BrewUI 的目标是让这部分用户能够以图形化方式完成软件包的发现、安装、更新与管理，同时保持对底层 Homebrew 操作的完全透明——界面不会隐藏实际执行的命令，用户依然可以清楚地知道 Homebrew 在做什么。

项目面向的主要用户是偏好图形界面、但又希望使用 Homebrew 生态的 macOS 用户，以及需要在团队或非技术场景中推广 Homebrew 的使用者。它并不替代命令行版本，而是为同一套包管理体系提供一个原生入口。

## 核心功能

- **软件包发现与浏览**：通过 Homebrew JSON API 获取 formula 与 cask 的元数据，支持在图形界面中检索和查看软件包信息。
- **安装、卸载与更新**：提供常规的包管理操作入口，涵盖安装、卸载、升级等日常动作。
- **操作透明化**：界面展示底层实际调用的 Homebrew 命令，用户可确认每一步操作的真实行为。
- **应用自更新**：BrewUI 自身也通过 Homebrew 完成升级，与包管理体系保持一致。
- **原生 macOS 体验**：基于 SwiftUI 构建，遵循 macOS 的交互与外观规范。

## 技术架构

BrewUI 使用 Swift 6.0 编写，并启用了严格并发（strict concurrency）检查，配合 SwiftUI 与 Swift Package Manager 组织项目。应用要求 macOS Tahoe 26 及以上版本。

数据来源有两处：本地 `brew` 命令行工具，以及 Homebrew 官方的 JSON API（formulae.brew.sh）。前者用于执行实际的管理操作，后者用于获取软件包的结构化元数据。

在调用 Homebrew 的方式上，BrewUI 做了较为严格的设计：始终通过 `/bin/zsh` 启动 `brew`，并附加 `--no-rcs --no-global-rcs` 参数，禁用用户和系统的 shell 启动文件，同时提供一个干净的环境变量集合。`PATH` 中只包含定位到的 `brew` 可执行文件所在目录以及 `/usr/bin:/bin`。这意味着用户的登录 shell、别名、导出的变量和自定义 `PATH` 都不会影响 BrewUI 中的 Homebrew 行为。需要配置 Homebrew 变量时，应写入相应作用域的 `brew.env` 文件，由 Homebrew 自行读取。

## 安装与使用

通过 Homebrew Cask 安装：

```bash
brew install --cask homebrew-app
```

安装后直接启动应用即可，无需额外配置。首次运行时 BrewUI 会定位系统中的 `brew` 可执行文件并建立连接。

如需自定义 Homebrew 行为，请按作用域写入 `brew.env` 文件，而不是依赖 shell 环境变量：

| 作用域 | 文件位置 |
| --- | --- |
| 用户 | `~/.homebrew/brew.env` |
| 安装 | `<Homebrew prefix>/etc/homebrew/brew.env` |
| 系统 | `/etc/...` |

由于应用禁用了 shell 启动文件，任何在 `.zshrc` 等文件中导出的 Homebrew 相关变量都不会生效，这一点在迁移既有配置时需要特别注意。

## 适用场景

- **不熟悉命令行的 macOS 用户**：希望在图形界面中完成软件安装与更新，避免记忆命令和参数。
- **教学与演示场景**：需要向他人展示 Homebrew 操作过程，界面能直观呈现底层命令。
- **环境一致性要求较高的用户**：通过 `brew.env` 与干净环境变量机制，保证 Homebrew 行为可预测、不受 shell 配置干扰。
- **日常包管理维护**：定期检查更新、批量管理已安装的 formula 与 cask。

## 项目亮点

与第三方 Homebrew 图形客户端相比，BrewUI 的核心差异在于其官方身份与设计取向。它不试图隐藏 Homebrew 的工作方式，而是把实际执行的命令暴露给用户，兼顾易用性与可解释性。在环境隔离方面，项目通过 `--no-rcs`、受控 `PATH` 与 `brew.env` 机制，消除了 shell 配置带来的不确定性，使操作结果更可复现。技术栈上采用 Swift 6.0 严格并发与 SwiftUI，与 macOS 系统能力结合紧密，属于原生实现而非跨平台封装。

## 相关链接

- [GitHub 仓库](https://github.com/Homebrew/BrewUI)
- [Homebrew JSON API 文档](https://formulae.brew.sh/docs/api/)
