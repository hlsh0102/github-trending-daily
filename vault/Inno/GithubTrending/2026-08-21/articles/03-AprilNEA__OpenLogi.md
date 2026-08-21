---
tags:
  - trending
  - article
repo: AprilNEA/OpenLogi
date: 2026-08-21
language: Rust
stars_total: 12001
stars_today: 1545
---
## 项目概述

OpenLogi 是一款面向 Logitech 外设用户的本地优先替代方案，旨在取代官方 Logitech Options+ 软件。项目完全使用 Rust 编写，通过 HID++ 和 UVC 协议直接与罗技鼠标、键盘和网络摄像头通信，实现了按键重映射、DPI 调节和 SmartShift 等高级功能。与官方软件不同，OpenLogi 不需要用户创建账户，不收集任何遥测数据，所有配置均存储在本地设备上。

该项目目前处于积极开发阶段，适合技术爱好者、隐私敏感用户以及希望摆脱官方软件限制的 Logitech 外设使用者。由于是开源项目，用户还可以根据自己的需求定制功能，或参与项目开发。

## 核心功能

- **按键重映射**：支持将鼠标和键盘上的任意按键重新映射为其他功能，包括宏命令、媒体控制、组合键等，完全本地处理，无延迟。
- **DPI 调节**：支持在板载内存中直接修改鼠标 DPI 设置，无需依赖云同步，切换速度更快。
- **SmartShift 支持**：完整实现 Logitech 的 SmartShift 功能，允许用户通过倾斜滚轮或按下特定按键切换滚轮模式。
- **HID++ 协议通信**：使用逆向工程实现的 HID++ 协议，与罗技设备进行底层通信，支持更多设备型号。
- **UVC 摄像头控制**：通过 USB Video Class 标准协议控制 Logitech 网络摄像头的参数，如变焦、曝光和对焦。
- **跨平台支持**：原生支持 Windows、macOS 和 Linux 三大主流操作系统，提供一致的体验。

## 技术架构

OpenLogi 采用了以下技术栈和架构特点：

- **核心语言**：项目完全使用 Rust 编写，利用其内存安全性和高性能特性，确保程序运行时占用资源极少，且不会出现内存泄漏等常见问题。
- **协议层**：通过直接实现 HID++ 2.0/4.0 协议和 UVC 标准协议，实现了与罗技设备的底层通信。这种设计避免了依赖官方 SDK 的限制，使得项目可以长期独立发展。
- **本地存储**：所有配置以 JSON 格式存储在用户本地目录中，不涉及任何云端同步。配置格式结构化清晰，方便用户手动编辑或备份。
- **模块化设计**：项目采用模块化架构，将设备发现、协议解析、配置管理和用户界面分离，便于维护和扩展新设备支持。
- **GUI 框架**：使用 Tauri 作为桌面界面框架，充分利用 Rust 后端与系统级 API 交互的能力，同时通过 Web 前端提供现代化的用户界面体验。

## 安装与使用

### 安装步骤

1. 从 [GitHub Releases](https://github.com/AprilNEA/OpenLogi/releases) 页面下载对应操作系统的安装包（Windows 为 `.msi`，macOS 为 `.dmg`，Linux 为 `.AppImage` 或 `.deb`）。
2. 根据操作系统提示完成安装。macOS 用户可能需要进入“系统设置”>“隐私与安全性”允许应用运行。
3. 连接 Logitech 设备（通过 USB 接收器或蓝牙），确保设备已被系统正确识别。
4. 启动 OpenLogi，软件会自动扫描并识别支持的设备。

### 最小使用示例

```bash
# Linux 下运行（开发模式）
git clone https://github.com/AprilNEA/OpenLogi.git
cd OpenLogi
cargo run

# 创建自定义按键配置
# 在配置目录中找到 openlogi.mouse.json 文件
# 编辑按键映射：
{
  "profile_name": "日常使用",
  "buttons": {
    "4": { "action": "media", "key": "volume_up" },
    "5": { "action": "macro", "keys": ["ctrl", "shift", "s"] }
  },
  "dpi_presets": [400, 800, 1600, 3200],
  "smart_shift": {
    "enabled": true,
    "force": 30
  }
}
```

## 适用场景

- **游戏玩家**：希望为不同游戏分配专属按键配置，或调整 DPI 以满足不同游戏类型的需求，同时追求零延迟的本地响应。
- **开发者和设计师**：将外设按键重映射为高频操作快捷键，提升工作效率；跨平台使用时配置保持一致。
- **隐私敏感用户**：拒绝使用需要注册账户和上传数据的官方软件，希望完全掌控自己的设备设置。
- **Linux 用户**：官方 Options+ 仅支持 Windows/macOS，Linux 用户长期以来缺乏官方管理工具，OpenLogi 填补了这一空白。

## 项目亮点

- **隐私优先**：无需账户、无遥测，所有数据本地处理，是隐私保护的最佳实践。
- **性能优越**：基于 Rust 的原生实现，内存占用低于 20MB，CPU 占用几乎为零，远优于 Electron 架构的官方软件。
- **广泛的设备兼容性**：不仅支持鼠标，还覆盖键盘和摄像头，且持续新增对旧款设备的支持。
- **开放协议**：通过逆向工程实现 HID++ 协议，项目本身开源透明，用户可以审计代码，并参与功能开发。
- **社区驱动**：项目在 GitHub 上拥有超过 12000 星标，社区活跃度高，开发者 AprilNEA 保持每日迭代，问题反馈响应迅速。

## 相关链接

- [GitHub 仓库](https://github.com/AprilNEA/OpenLogi)
- [项目官网](https://openlogi.org)
- [Telegram 社区群组](https://t.me/+VDtkR5OSAT04NzVh)
- [GitHub Releases 页面](https://github.com/AprilNEA/OpenLogi/releases)
