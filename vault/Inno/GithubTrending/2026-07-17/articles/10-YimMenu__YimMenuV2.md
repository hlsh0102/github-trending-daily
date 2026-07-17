---
tags:
  - trending
  - article
repo: YimMenu/YimMenuV2
date: 2026-07-17
language: C++
stars_total: 1519
stars_today: 128
---
## 项目概述

YimMenuV2 是一个针对《Grand Theft Auto V: Enhanced》（即 GTA 5 增强版）的实验性菜单工具，由 YimMenu 团队使用 C++ 开发并开源。该项目主要解决用户在 GTA 5 增强版中无法使用传统模组菜单的问题，特别是针对新版 BattlEye 反作弊系统的兼容性挑战。目标用户为 GTA 5 增强版玩家中希望进行本地测试、功能探索或体验模组功能的资深用户。

## 核心功能

- **基础功能框架**：提供可扩展的菜单系统，支持未来功能模块的加载与切换
- **键盘快捷键控制**：支持通过 `INSERT` 键或 `Ctrl+\` 快捷键呼出/隐藏菜单界面
- **FSL 集成支持**：与 FSL（本地 GTA Online 存档重定向）工具兼容，允许用户将在线进度保存到本地磁盘
- **BattlEye 绕过支持**：用户可手动禁用游戏内 BattlEye 反作弊系统（通过启动参数或启动器设置）
- **动态注入加载**：支持通过 Xenos 等第三方注入器在游戏主菜单阶段注入 DLL 文件
- **夜间构建版本**：提供持续更新的 GitHub Releases 页面，用户可获取最新实验性功能

## 技术架构

YimMenuV2 基于 C++ 编写，使用标准 Windows DLL 注入技术实现运行时加载。其核心设计思路是：

1. **钩子与内存操作**：通过函数钩子和内存读写实现与游戏客户端的交互，这是 GTA 模组工具的常见技术路线。
2. **FSL 存档重定向**：利用 FSL 工具将游戏原本受保护的在线存档（通过 Rockstar 云服务同步）重定向至用户本地磁盘，从而允许菜单在修改游戏数据时不触发服务器端的检测。
3. **模块化设计**：虽然目前仍处于实验阶段，但代码结构预留了功能模块扩展接口，便于未来添加具体功能（如载具生成、玩家操控等）。
4. **反作弊规避策略**：当前版本无法绕过 BattlEye 的心跳检测，因此采用了“在启用 BattlEye 之前注入”的策略（用户需手动关闭 BattlEye），并通过 FSL 隔离本地与在线数据以降低封号风险。

## 安装与使用

**前置准备**：
- 下载并安装最新的 GTA 5 增强版（通过 Rockstar Launcher 或 Steam/Epic Games 客户端）
- 可选但强烈建议：从 [FSL 下载页面](https://www.unknowncheats.me/forum/grand-theft-auto-v/616977-fsl-local-gtao-saves.html) 获取 `version.dll` 并放置到 GTA V 安装目录下，用于保护在线存档

**安装步骤**：
1. 从 [YimMenuV2 发布页](https://github.com/YimMenu/YimMenuV2/releases/tag/nightly) 下载最新的 `YimMenuV2.dll`
2. 下载一个 DLL 注入器（如 [Xenos](https://www.unknowncheats.me/forum/general-programming-and-reversing/124013-xenos-injector-v2-3-2-a.html)）
3. 在 Rockstar Launcher 中：选择《Grand Theft Auto V Enhanced》→ 设置 → 禁用 BattlEye。若使用 Steam 或 Epic Games，需额外添加启动参数 `-nobattleye`
4. 启动 GTA V 增强版，等待进入主菜单界面
5. 使用注入器将 `YimMenuV2.dll` 注入到游戏进程

**使用示例**：
```bash
# 启动游戏（手动禁用 BattlEye）
# Steam 用户可在库中右键 GTA V → 属性 → 启动选项，添加：
-nobattleye
# 然后在主菜单使用 Xenos 注入 DLL
```

注入成功后，按 `INSERT` 键或 `Ctrl+\` 即可打开菜单界面。

## 适用场景

- **本地测试与开发**：模组开发者可在关闭 BattlEye 的本地环境中测试新功能，而不影响在线账户安全
- **单人模式扩展**：在单人故事模式中体验修改后的玩法，例如生成载具、修改角色属性等
- **社区功能预览**：抢先体验 YimMenu 团队为增强版开发的新功能，参与测试并反馈 Bug
- **教育研究**：对游戏逆向工程和 Windows DLL 注入技术感兴趣的开发者可作为学习案例

## 项目亮点

- **开源透明**：基于 GPL-2.0 许可完全开源，用户可自由审查代码，避免后门风险
- **实验性定位**：明确声明为“实验性菜单”，不承诺稳定性，降低了用户对完美功能的预期
- **FSL 集成策略**：通过强制性提示和存档重定向机制，显著降低因使用作弊工具导致的账号被封概率
- **持续迭代**：项目活跃度高（单日 Star 增长 128），团队持续更新以适配 GTA 5 增强版的版本变化
- **跨平台兼容**：支持 Rockstar Launcher、Steam、Epic Games 三种启动方式，通过参数配置覆盖主流分发平台

## 相关链接

- [GitHub 仓库](https://github.com/YimMenu/YimMenuV2)
- [GitHub 发布页（夜间构建）](https://github.com/YimMenu/YimMenuV2/releases/tag/nightly)
- [FSL 本地存档工具下载页](https://www.unknowncheats.me/forum/grand-theft-auto-v/616977-fsl-local-gtao-saves.html)
- [Xenos DLL 注入器下载页](https://www.unknowncheats.me/forum/general-programming-and-reversing/124013-xenos-injector-v2-3-2-a.html)
