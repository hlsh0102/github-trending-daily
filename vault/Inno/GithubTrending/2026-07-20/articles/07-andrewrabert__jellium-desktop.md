---
tags:
  - trending
  - article
repo: andrewrabert/jellium-desktop
date: 2026-07-20
language: Rust
stars_total: 1332
stars_today: 43
---
## 项目概述

Jellium Desktop 是一款非官方的 Jellyfin 桌面客户端，专为希望获得更流畅、更强大播放体验的 Jellyfin 用户设计。Jellyfin 是一个开源媒体服务器软件，而 Jellium Desktop 则充当其客户端，将媒体内容直接呈现在用户的桌面设备上。该项目主要解决了官方 Jellyfin 网页端在播放性能和功能扩展方面的局限性，通过集成 CEF（Chromium Embedded Framework）和 mpv 播放器，为用户提供接近原生应用的体验。目标用户是那些需要高性能播放、跨平台支持以及对 Jellyfin 媒体库有深度控制需求的个人或家庭用户。

## 核心功能

- **高性能媒体播放**：基于 mpv 播放器核心，支持硬件加速解码和多种视频格式，提供流畅的 4K、HDR 内容播放体验，并支持字幕、音轨切换等高级功能。
- **跨平台支持**：提供 Linux（AppImage、Flatpak、AUR）、macOS（Apple Silicon 与 Intel）、Windows（x64 与 arm64）的全平台二进制分发版本，用户无需自行编译即可安装使用。
- **原生窗口体验**：利用 CEF 将 Jellyfin Web 界面嵌入为桌面窗口，保留所有网页端功能（如浏览、搜索、设置），同时避免浏览器标签页的干扰，提供专注的媒体浏览体验。
- **集成式播放控制**：将 mpv 的播放能力与 Jellyfin 界面无缝集成，在客户端窗口内即可完成播放、暂停、进度拖拽、音量调节等操作，无需额外切换窗口。
- **低资源占用**：相比使用完整浏览器访问 Jellyfin 网页端，CEF 容器化方案可减少内存和 CPU 占用，尤其适合在低功耗设备或旧电脑上运行。
- **持续集成构建**：通过 GitHub Actions 自动为每个提交生成跨平台构建产物，用户可从 nightly.link 获取最新版本，确保及时获取修复和改进。

## 技术架构

Jellium Desktop 采用 Rust 语言作为主要开发语言，结合 CEF 和 mpv 两个核心组件。其技术架构可概括为：

- **Rust 基础层**：利用 Rust 的安全性和性能优势，负责应用的启动、配置管理、进程调度以及与 CEF 和 mpv 的底层通信。Rust 的内存安全特性降低了崩溃和安全漏洞的风险。
- **CEF 容器**：作为用户界面的核心，CEF 将 Jellyfin 的 React 前端嵌入为桌面窗口。它处理页面渲染、JavaScript 执行、输入事件（键盘、鼠标）和网络请求，确保与 Jellyfin 服务器的完整交互。CEF 的版本与最新 Chromium 同步，保证了现代 Web 标准的兼容性。
- **mpv 播放引擎**：作为独立的子进程运行，通过进程间通信（IPC）与 CEF 窗口交互。mpv 负责实际的媒体解码、渲染和输出，利用 OpenGL 或 Vulkan 后端实现低延迟播放。其强大的滤镜和配置系统允许高级用户自定义播放行为。
- **跨平台构建系统**：使用 `just` 作为任务运行器，通过条件编译和平台特定脚本（如 Linux 下的 AppImage、macOS 下的 DMG、Windows 下的 ZIP）生成最终分发包。构建配置位于 `justfile` 中，支持 `appimage`、`flatpak`、`dmg` 等命令。

## 安装与使用

### 安装步骤

1. **下载对应平台的构建产物**：从项目的 GitHub 仓库的“Releases”或 nightly.link 页面获取匹配您操作系统的压缩包。
2. **安装基本依赖**（Linux 用户需要安装 mpv 和基础运行时库）：
   ```bash
   sudo apt install mpv libgtk-3-0 libnotify4
   ```
3. **解压并运行**：
   - **Linux**：运行解压出的 `jellium-desktop` 可执行文件或安装 AUR 包。
   - **macOS**：将 `.app` 包拖入“应用程序”文件夹，并执行 `sudo xattr -cr /Applications/Jellium\ Desktop.app` 解除隔离。
   - **Windows**：解压后直接运行 `Jellium.exe`。

### 最小可用示例

1. 启动应用后，输入您的 Jellyfin 服务器地址（例如 `http://192.168.1.100:8096`）并登录。
2. 浏览媒体库，选择一个视频或音频文件。
3. 点击播放按钮，内容将在 mpv 引擎中播放，支持全屏、字幕切换、进度条拖拽。
4. 使用键盘快捷键（如 `Space` 暂停/继续，`F` 全屏）控制播放。

## 适用场景

- **家庭媒体中心**：在客厅的 PC 或 HTPC 上安装 Jellium Desktop，通过 Jellyfin 服务器管理电影、电视剧和音乐，利用 mpv 的高画质输出到电视或投影仪。
- **远程办公娱乐**：在工作的 Mac 或 Windows 笔记本上部署，远程连接家中的 Jellyfin 服务器，利用硬件加速解码在午休时间流畅观看高清内容。
- **多语言字幕需求**：对于有外挂字幕需求的用户（如外语电影、动漫），mpv 原生支持 ASS/SSA、SRT 等字幕格式，并提供基于 libass 的精准渲染。
- **低配置设备优化**：在旧笔记本或廉价迷你 PC 上运行，相比完整浏览器节省资源，同时仍能获得良好的播放性能。

## 项目亮点

- **性能优先**：直接对接 mpv 播放引擎，绕过浏览器播放器的限制，支持硬解码和高级渲染配置，比使用 Firefox 或 Chrome 播放 Jellyfin 网页端时 CPU 占用更低、画面更流畅。
- **原生跨平台**：无需 Electron 或 WebView，通过 CEF 和 Rust 实现真正的原生体验，体积优化到几十兆字节，启动速度秒级。
- **社区驱动**：作为非官方客户端，开发节奏紧跟 Jellyfin 前端更新，可通过 GitHub Issues 和 PR 快速反馈问题，比等待官方桌面客户端更灵活。
- **定制化潜力**：Rust 的模块化设计和 mpv 的配置文件支持（如自定义着色器、音频输出模式），允许高级用户调整播放行为，满足 HTPC 发烧友的个性化需求。

## 相关链接

- [GitHub 仓库](https://github.com/andrewrabert/jellium-desktop)
- [项目 License (GPL-2.0)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
