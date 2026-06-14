---
tags:
  - trending
  - article
repo: microsoft/PowerToys
date: 2026-06-14
language: C
stars_total: 134750
stars_today: 370
---
## 项目概述

Microsoft PowerToys 是一套面向 Windows 高级用户的开源系统工具集，旨在通过提供超过 30 个实用工具来增强 Windows 系统的可定制性和日常操作效率。该项目由微软官方发起并维护，目标用户是希望深度优化 Windows 体验的开发者、IT 专业人士以及任何对生产力提升有需求的普通用户。PowerToys 填补了 Windows 原生功能在文件管理、窗口布局、快捷键扩展等方面存在的空白，以模块化、轻量级的方式为用户提供企业级效率工具。

## 核心功能

- **文件管理和窗口操作增强**：包含“FancyZones”窗口布局管理器，允许用户创建自定义窗口区域并快速将窗口吸附到特定位置；“Always on Top”可让选定窗口始终置顶；“File Explorer Add-ons”为文件资源管理器添加预览功能（如 SVG、Markdown 等格式的缩略图）。
- **键盘和输入优化**：“Keyboard Manager”支持重映射任意按键和快捷键组合；“Quick Accent”提供快速输入带变音符号字符的方法；“PowerToys Run”是一个快速启动器，替代 Windows 默认搜索，支持搜索应用、文件、计算器、Shell 命令等。
- **批量文件操作**：“PowerRename”提供高级批量重命名功能，支持正则表达式；“Peek”允许用户像 macOS 的 Quick Look 一样预览文件内容（按 Ctrl+Space 激活）。
- **图像和颜色工具**：“Color Picker”可识别屏幕任意位置的颜色值并支持多种格式输出；“Image Resizer”实现图片的快速缩放和格式转换。
- **系统管理和测量**：“Mouse Without Borders”允许跨多台 Windows 电脑共享鼠标、键盘和剪贴板；“Measure Tool”提供屏幕上的标尺、量角器和十字准线；“Hosts File Editor”简化 hosts 文件的编辑和启用/禁用条目。
- **开发者工具**：“Command Not Found”在 PowerShell 中输入未知命令时，通过 WinGet 提供安装建议；“Registry Preview”以文本方式预览和编辑注册表文件。

## 技术架构

PowerToys 基于 C#/.NET（核心工具模块）和 C++（部分性能敏感组件，如 FancyZones）构建，采用模块化单体架构。每个工具都以独立的动态链接库（DLL）形式存在，由一个中央进程（PowerToys.exe）统一管理启动、停止和配置。
- **集成方式**：工具通过 Windows 系统 API（如 Win32 API、COM 接口、Windows Shell 扩展）深度集成到操作系统中，例如“FancyZones”挂钩窗口管理器，“File Explorer Add-ons”注册为 Shell 扩展。
- **配置系统**：所有设置储存在 JSON 格式的配置文件（%LocalAppData%\Microsoft\PowerToys\）中，由统一的设置界面（Settings UI）管理。用户可通过全局快捷键（默认 Win+Shift+空格）快速访问设置面板。
- **更新机制**：使用 Windows 应用商店分发作为主要渠道，同时支持 GitHub Releases 手动安装。自动更新通过内置的更新检查器实现，基于 .NET 的 Squirrel 框架。
- **跨版本支持**：项目兼容 Windows 10（版本 1803 及以上）和 Windows 11，对 ARM64 架构提供原生支持。

## 安装与使用

1. **通过 Windows 应用商店安装**（推荐）：
   - 在 Microsoft Store 搜索 “Microsoft PowerToys”，点击安装。
   - 或直接访问：https://aka.ms/powertoys

2. **手动安装**（从 GitHub Releases）：
   ```bash
   # 下载最新 .exe 安装程序
   # 运行安装程序，保持默认选项即可
   PowerToysSetup-x.x.x-x64.exe
   ```

3. **通过 winget 安装**（命令行）：
   ```bash
   winget install Microsoft.PowerToys
   ```

**最小可用示例（启用 PowerToys Run 快速启动）**：
- 安装完成后，PowerToys 默认在系统托盘运行。
- 按 `Alt+空格` 打开 PowerToys Run 搜索框。
- 输入 `calc` 按回车，系统将打开计算器。
- 输入 `notepad` 按回车，打开记事本。
- 输入 `ipconfig` 按回车，显示网络配置信息（无需手动打开命令提示符）。

启用窗口自动布局（FancyZones）：
- 打开 PowerToys Settings，进入“FancyZones”页面。
- 点击“启动布局编辑器”，选择一个预设布局（如三列并排）。
- 按住 Shift 键拖动窗口到该区域，窗口会自动吸附到对应大小。

## 适用场景

- **多显示器或多任务办公**：用户使用 FancyZones 快速将不同窗口分配到屏幕特定区域，大幅提升在多个应用间切换的效率，尤其适合程序员、设计师和金融分析师。
- **Windows 系统深度定制**：IT 管理员或高级用户利用 Keyboard Manager 重映射功能键，用 PowerRename 批量重命名文件，或用 Hosts File Editor 管理本地开发环境。
- **跨设备协同工作**：配备多台电脑的用户使用“Mouse Without Borders”共享一套键盘鼠标，无缝在设备间拖放文件和复制粘贴内容，省去额外硬件（如 KVM 切换器）。
- **日常文件与图像处理**：用 Peek 快速预览代码、PDF、Markdown 和 SVG 文件，免去频繁打开特定应用程序；用 Image Resizer 批量缩放照片或截图，无需启动专业图像编辑软件。

## 项目亮点

- **微软官方维护的开源工具**：由微软官方团队开发，代码完全开源（MIT 许可证），背靠 Windows 平台第一手技术支持，确保与系统更新的兼容性。
- **模块化自由组合**：区别于单一的第三方增强工具（如 Listary、Everything），PowerToys 允许用户仅启用所需模块，系统资源占用极低（空闲时约 50MB 内存）。
- **与 Windows 生态系统深度融合**：工具通过原生 API 集成，体验与 Windows 原生功能一致（如右键菜单、文件资源管理器预览），不需要额外学习成本。
- **持续且活跃的社区驱动**：项目在 GitHub 上有超过 13 万星标，每月更新迭代，社区贡献编译的第三方工具（如独立运行的模块）使得功能扩展空间大。
- **辅助功能友好**：多个工具（如 Color Picker、Peek）对视力障碍用户有语音播报和键盘导航支持，设计时考虑了无障碍标准。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/PowerToys)
- [官方文档](https://aka.ms/powertoys-docs)
- [发布博客](https://aka.ms/powertoys-releaseblog)
- [Windows 应用商店下载](https://aka.ms/powertoys)
