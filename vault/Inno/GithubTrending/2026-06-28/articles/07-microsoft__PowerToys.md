---
tags:
  - trending
  - article
repo: microsoft/PowerToys
date: 2026-06-28
language: C
stars_total: 135758
stars_today: 57
---
## 项目概述

Microsoft PowerToys 是微软官方推出的一套开源 Windows 实用工具集，旨在通过一系列轻量、高效的小工具帮助用户深度定制 Windows 系统，并显著提升日常工作效率。该项目解决了 Windows 系统原生功能在生产力与个性化方面存在的诸多短板——例如窗口管理不便、文件批量重命名繁琐、颜色拾取缺乏系统级工具等。目标用户涵盖普通办公人员、软件开发工程师、设计师、系统管理员以及所有希望通过少量配置提升 Windows 操作体验的用户。PowerToys 以 MIT 许可证开源，目前包含超过 30 个独立工具，且社区活跃度极高，GitHub 星标数超过 13 万。

## 核心功能

- **FancyZones（窗口分区管理）**：允许用户自定义复杂的窗口布局模板，将桌面划分为多个区域，拖拽窗口时自动吸附到预设区域，支持多显示器及动态布局切换。
- **PowerToys Run（快速启动器）**：使用快捷键 `Alt+Space` 呼出，可快速搜索文件、程序、系统命令、计算器结果，支持插件扩展（如搜索浏览器书签或网络路径）。
- **File Explorer Add-ons（文件资源管理器增强）**：包括缩略图预览（如 SVG、Markdown 和 G 代码文件）以及文件预览窗格扩展，无需打开文件即可在资源管理器中查看内容。
- **Image Resizer（图片批量调整）**：右键菜单集成，可批量调整图片尺寸、旋转或转换格式，支持自定义预设及其命名规则。
- **Keyboard Manager（键盘键位重映射）**：允许用户重新映射单个按键或组合键（如将 `Caps Lock` 映射为 `Ctrl`），并可创建针对特定应用程序的键位方案。
- **PowerRename（批量重命名）**：在文件资源管理器右键菜单中调用，支持使用正则表达式、搜索与替换、文件编号等规则进行高级批量重命名。

## 技术架构

PowerToys 采用模块化架构，每个实用工具作为独立的组件运行，并通过统一的中央管理界面进行配置和启用。项目后端主要使用 C# 和 C++（部分工具为 C#，系统底层功能如键盘钩子、窗口管理使用 C++），前端 UI 采用 Windows Presentation Foundation (WPF) 构建，确保与现代 Windows 操作系统的深度集成。关键设计特点包括：

- **低资源占用**：大多数工具在后台以守护进程方式运行，仅在触发特定操作时激活，避免持续占用 CPU 或内存。
- **系统级钩子**：诸如 Always on Top、Keyboard Manager 等工具通过 Windows 消息钩子和事件订阅实现全局热键和窗口行为控制，无需轮询。
- **可扩展性**：PowerToys Run 等工具支持插件架构，允许第三方开发者编写自定义搜索插件；同时所有工具均可独立启用或禁用，用户可按需加载。

## 安装与使用

PowerToys 提供多种安装方式，推荐通过微软商店或官方 GitHub Releases 页面获取。以下是基本安装步骤：

1. **从微软商店安装**：打开 Microsoft Store，搜索 "Microsoft PowerToys"，点击获取并安装。
2. **从 GitHub 手动安装**：访问 [PowerToys Releases 页面](https://github.com/microsoft/PowerToys/releases)，下载 `PowerToysSetup-x.y.z-x64.exe`（最新版本），运行安装程序即可。
3. **使用 winget 命令行**：打开终端，执行 `winget install Microsoft.PowerToys`，系统将自动下载并静默安装。

安装完成后，PowerToys 图标会出现在系统托盘中，双击即可打开设置界面。所有工具默认处于停用状态，用户可根据需要逐一开启。最小可用示例：

- **启用 FancyZones**：在设置中打开该功能 → 按下 `Win+`（反引号）呼出布局编辑器 → 选择预设布局（如三列）→ 拖拽任意窗口到分区即可自动吸附。
- **使用 PowerToys Run**：默认激活后按下 `Alt+Space` → 输入 "calc" 回车可打开计算器，输入 "10*12" 可直接显示计算结果。

## 适用场景

- **开发者日常开发**：使用 PowerToys Run 快速切换项目目录，用 FancyZones 布置代码编辑器和终端窗口，通过 Keyboard Manager 将 `Ctrl+Shift+W` 映射为关闭程序快捷键。
- **设计师与图像处理**：利用 Color Picker 在屏幕任何位置拾取颜色并复制为 HEX/RGB 值，用 Image Resizer 批量压缩或转换设计素材。
- **系统管理与维护**：使用 Awake 保持计算机在长时间任务（如大规模备份或渲染）中不进入睡眠模式，通过 PowerRename 批量修正文件名中的日期格式。
- **普通办公与文档处理**：借助 Snippet Text（文本批量替换）快速输入常用模板，使用 Always on Top 将参考资料窗口固定在视频会议工具上方。

## 项目亮点

与同类工具（如 WindowGrid、AutoHotkey 脚本或独立小工具）相比，PowerToys 的差异化优势在于：

- **官方级支持与可靠性**：由微软维护，与 Windows 系统深度集成，兼容性高，更新及时；经过大规模用户测试，稳定性有保障。
- **一站式工具集**：单个安装包即可获得超过 30 种功能，无需分别下载、管理和更新多个第三方工具；统一设置界面降低学习成本。
- **开源与社区驱动**：完全开源（MIT 协议），社区可贡献新功能或修复 Bug；用户可通过 GitHub Issues 直接提交需求，开发过程透明。
- **零配置精简设计**：大多数工具开箱即用，无需复杂配置；无后台广告或付费墙，完全免费使用。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/PowerToys)
- [官方文档](https://aka.ms/powertoys-docs)
- [最新博客发布](https://aka.ms/powertoys-releaseblog)
- [微软商店安装页面](ms-windows-store://pdp/?productid=XP89DCGQ3K6VLD)
