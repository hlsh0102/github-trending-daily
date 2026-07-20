---
tags:
  - trending
  - article
repo: microsoft/terminal
date: 2026-07-20
language: C++
stars_total: 104227
stars_today: 59
---
## 项目概述

Windows Terminal 是由微软开源的一个现代化终端应用程序，同时整合了原有的 Windows 控制台主机（Console Host）。该项目旨在为 Windows 用户提供一款快速、高效、可高度自定义的命令行工具，支持 PowerShell、命令提示符（CMD）、WSL（Windows Subsystem for Linux）以及 Azure Cloud Shell 等多种命令行环境。目标用户包括开发者、系统管理员以及任何需要在 Windows 上频繁使用命令行工作的用户。它不仅是一个单纯的终端模拟器，还内置了对 GPU 加速渲染、多标签页、分割窗格等现代功能的支持，解决了传统 Windows 控制台在美观性、功能和性能上的不足。

## 核心功能

- **多标签页与分割窗格**：支持在同一窗口中打开多个标签页，每个标签页可运行不同的命令行环境（如 PowerShell、CMD、WSL），并支持垂直或水平分割窗格，方便同时查看多个会话。
- **GPU 加速渲染**：利用 GPU 进行文本渲染，大幅提升终端的绘制性能，减少输入延迟，尤其在高分辨率或复杂输出场景下表现优异。
- **高度可自定义**：支持通过 JSON 文件自定义外观（主题、配色方案、背景图片、透明度）、快捷键、启动行为以及每个配置文件的行为（如字体、光标样式）。
- **Unicode 与国际化支持**：原生支持 Unicode、emoji 以及复杂的文字布局，包括对日本汉字、阿拉伯语等非英文语言的正确处理。
- **嵌入式 PowerShell 与 Azure Cloud Shell**：内置对 PowerShell 和 Azure Cloud Shell 的支持，用户可直接从终端访问云环境，无需额外配置。
- **历史记录与搜索**：提供会话历史记录、滚动缓冲区内容搜索功能，方便快速定位之前的命令输出。

## 技术架构

Windows Terminal 采用 C++ 编写，基于 Windows 应用 SDK（Windows App SDK）和 UWP 框架构建，同时深度依赖 Windows 底层的控制台 API。其架构分为三个主要部分：

- **Windows Terminal**：基于 XAML 的前端用户界面，负责多标签页、分割窗格、渲染以及用户交互。它通过 `ConPTY`（控制台伪终端 API）与底层控制台主机通信。
- **Windows Console Host**：传统的控制台主机，负责管理控制台窗口、输入输出缓冲以及命令行进程的调度。项目中对 Console Host 进行了现代化重构，支持 GPU 渲染和更好的 Unicode 兼容性。
- **共享组件**：包括 `ConPTY`、`TextBuffer`（文本缓冲区）、`ColorScheme`（配色方案）等公共模块，它们被 Terminal 和 Console Host 共同使用，确保跨环境的兼容性。

设计上，项目采用模块化架构，使得终端前端与后端控制台主机可以相对独立地演进。此外，其渲染管线基于 DirectX 实现，确保了高效且流畅的视觉效果。

## 安装与使用

### 安装方式

- **Microsoft Store（推荐）**：搜索 "Windows Terminal" 并安装，支持自动更新。
- **GitHub Releases**：访问 [GitHub 仓库](https://github.com/microsoft/terminal) 的 Releases 页面，下载 `.msixbundle` 或 `.msix` 安装包并手动安装。
- **Windows Package Manager（winget）**：在管理员命令行中执行 `winget install Microsoft.WindowsTerminal`。
- **Scoop**：执行 `scoop install windows-terminal`。
- **Chocolatey**：执行 `choco install microsoft-windows-terminal`。

### 最小可用示例

安装完成后，启动 Windows Terminal。默认打开一个 PowerShell 标签页。你可以通过点击标签栏的 "+" 号新建标签页，选择不同的命令行环境。也可以按 `Alt+Shift+-`（或 `Alt+Shift+=`）分割窗格。

若要打开一个新标签页并指定为 WSL，可以通过命令 `wsl` 在当前会话中启动它。如果你启用 WSL 配置文件，Terminal 会自动列出可用的 WSL 发行版，并在下拉菜单中显示。

## 适用场景

- **开发者多环境管理**：同时管理多个项目的命令行环境，如一个标签页运行 PowerShell，另一个标签页运行 WSL 中的 Linux 开发环境，再通过分割窗格实时查看编译输出。
- **系统管理员日常运维**：通过 CMD 或 PowerShell 执行系统管理任务，利用多标签页同时监控多个服务器连接或日志流。
- **学习与实验**：在教学或文档编写场景中，使用拆分窗格同时显示命令输入和输出说明，或通过 Unicode 支持显示特殊字符和图表。
- **云环境集成**：配合 Azure Cloud Shell，无需切换应用即可直接管理云资源，适合混合云运维。

## 项目亮点

- **开源与社区驱动**：采用 MIT 许可，完全开源。微软积极接受社区贡献，包括功能请求、Bug 修复以及本地化翻译。项目拥有超过 10 万颗 Star，社区活跃度极高。
- **现代化与兼容性并重**：在保留对传统 CMD 和 PowerShell 完整兼容的同时，引入 GPU 加速、多标签页、主题自定义等现代特性，是目前 Windows 上最强大且易用的终端之一。
- **与 Windows 生态系统深度集成**：原生支持 WSL、Azure Cloud Shell、Windows 终端服务以及 Windows 应用 SDK，完美融入 Windows 用户的工作流。
- **持续迭代与稳定版本并行**：提供稳定版和 Canary 版（Windows Terminal Canary），方便用户体验最新功能或保持生产环境稳定。微软还发布了配置文档与教程，降低上手门槛。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/terminal)
- [官方文档](https://learn.microsoft.com/windows/terminal/)
- [Microsoft Store 页面](https://apps.microsoft.com/detail/9n0dx20hk701)
