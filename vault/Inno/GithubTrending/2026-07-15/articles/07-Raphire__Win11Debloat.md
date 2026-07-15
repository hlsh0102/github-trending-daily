---
tags:
  - trending
  - article
repo: Raphire/Win11Debloat
date: 2026-07-15
language: PowerShell
stars_total: 51863
stars_today: 783
---
## 项目概述

Win11Debloat 是一款轻量级、易于使用的 PowerShell 脚本，专为希望快速精简和个性化 Windows 体验的用户设计。无需安装任何软件，只需运行一个脚本，即可批量移除预装应用、禁用遥测功能、去除 intrusive 界面元素，以及执行多种系统定制调整。该项目同时支持 Windows 10 和 Windows 11，是日常用户、系统管理员和高级玩家的一站式系统优化工具。

## 核心功能

- **移除预装应用**：一键卸载 Windows 自带的大量非必要应用（如 Xbox、Bing 天气、OneDrive 等），释放系统空间并减少后台进程。
- **禁用遥测与数据收集**：关闭微软的隐私侵扰性遥测服务，阻止系统向微软发送不必要的诊断数据。
- **去除界面干扰元素**：移除任务栏上的“聊天”（Teams 图标）、Widgets 按钮、推荐内容、搜索高亮等视觉干扰项，回归简洁界面。
- **文件资源管理器优化**：隐藏“开始”菜单中的推荐项、禁用 OneDrive 自动同步、关闭文件夹缩略图预览等。
- **系统服务调整**：禁用 Cortana、Edge 后台进程、Xbox 游戏服务等不必要的后台服务，提升系统响应速度。
- **灵活配置与导出**：支持通过命令行参数进行精细控制；可将当前设置导出为配置文件，导入后在其他电脑上批量应用相同优化。

## 技术架构

Win11Debloat 采用纯 PowerShell 脚本实现，无需外部依赖或编译工具。脚本通过调用 Windows 原生 API（如 `Get-AppxPackage` 用于卸载应用包、`Remove-ItemProperty` 用于编辑注册表、`Set-ItemProperty` 用于修改系统设置）来执行所有操作。其架构特点包括：

- **模块化调整**：每项功能（如移除特定应用、禁用某服务）均为独立函数，便于维护和扩展。
- **参数化控制**：用户可通过命令行参数（如 `-RemoveApps`、`-DisableTelemetry`）选择性启用/禁用功能，避免全盘执行。
- **安全回滚**：脚本在执行前会创建注册表备份，部分调整支持恢复默认设置（通过 `-Revert` 参数）。
- **多用户支持**：支持在 Windows Audit 模式下运行，或指定目标用户账户，满足企业部署场景。
- **配置文件驱动**：通过 JSON 文件保存用户偏好，支持 `-ExportSettings` 和 `-ImportSettings` 参数实现批量部署。

## 安装与使用

Win11Debloat 无需安装，直接下载脚本文件即可运行。基本步骤如下：

1. **下载脚本**：前往 [GitHub Releases 页面](https://github.com/Raphire/Win11Debloat/releases) 下载最新版本的 `Win11Debloat.ps1` 文件，或使用以下命令直接通过 PowerShell 拉取：
   ```powershell
   iwr -Uri "https://raw.githubusercontent.com/Raphire/Win11Debloat/main/Win11Debloat.ps1" -OutFile Win11Debloat.ps1
   ```

2. **启动 PowerShell 并运行**：以管理员身份打开 PowerShell（右键点击开始菜单 -> Windows PowerShell (管理员)），导航到脚本所在目录，执行：
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\Win11Debloat.ps1
   ```
   - 首次运行会显示图形化菜单，列出所有可用调整项，用户可勾选后一键执行。
   - 如需完全自动化（无交互），可使用命令行模式，例如：
     ```powershell
     .\Win11Debloat.ps1 -Silent -RemoveApps -DisableTelemetry -DisableBingSearch -DisableCortana
     ```

3. **查看更改**：脚本执行完成后，重启电脑使部分设置生效。可通过 `-GetConfig` 参数查看当前系统已应用了哪些调整。

## 适用场景

- **个人用户日常优化**：普通用户希望快速清理 Windows 自带垃圾应用、减少后台任务、改善隐私保护，无需手动逐项操作。
- **企业/组织批量部署**：系统管理员在大量电脑上部署统一配置，通过导出/导入配置文件，快速实施标准化精简策略。
- **老旧设备性能提升**：在配置较低的设备上，通过禁用非必要服务和视觉特效，释放系统资源，延长设备使用寿命。
- **测试环境快速准备**：在虚拟机或测试机上运行，一键还原为“纯净”Windows 环境，减少手动设置时间。

## 项目亮点

- **零门槛操作**：提供图形化交互界面和命令行双模式，无论是新手还是高级用户都能快速上手。无需手动搜索每个设置项，一行命令或几个勾选即可完成全部优化。
- **安全性优先**：脚本经过精心设计，避免删除关键系统组件导致功能异常。所有修改均基于已知安全的注册表路径和应用移除规则，且提供 `-Revert` 恢复选项。
- **跨版本兼容**：同时支持 Windows 10 和 Windows 11，自动检测系统类型并应用对应调整，无需用户手动区分。
- **企业级功能**：支持 Windows Audit 模式、多用户操作、配置导入导出等高级特性，满足系统管理员在域环境或大规模部署中的需求。
- **社区驱动更新**：脚本随 Windows 更新持续维护，定期添加对新版系统中新增预装应用或界面元素的屏蔽能力，积极响应用户反馈。

## 相关链接

- [GitHub 仓库](https://github.com/Raphire/Win11Debloat)
- [项目 Wiki](https://github.com/Raphire/Win11Debloat/wiki)（详细参数说明、常见问题等）
- [问题反馈](https://github.com/Raphire/Win11Debloat/issues)
