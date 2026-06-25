---
tags:
  - trending
  - article
repo: andreknieriem/headunit-revived
date: 2026-06-25
language: Kotlin
stars_total: 1469
stars_today: 41
---
## 项目概述

Headunit Revived 是一款 Android 应用程序，旨在将您的 Android 平板电脑或手机转变为 Android Auto 接收器。该项目是对 Michael Reid 原版 headunit 项目的复兴与延续，原版项目托管于 https://github.com/mikereidis/headunit。它的核心用途是让不具备原生 Android Auto 功能的旧车载系统、改装中控或自建仪表盘，能够通过手机或平板作为主机，显示 Android Auto 界面并与已连接的手机进行交互。

目标用户主要是车载系统改装爱好者、DIY 智能座舱玩家、以及希望在不更换主机的情况下获得 Android Auto 体验的车主。

## 核心功能

- **Android Auto 显示**：在 Android 设备上作为接收端，完整显示 Android Auto 界面，支持触控操作。
- **多连接方式**：支持通过 USB 线缆或 Wi-Fi 无线方式连接手机，提供灵活的选择。
- **屏幕自适应**：针对不同分辨率和尺寸的屏幕进行优化，支持横竖屏切换，并可调整 UI 元素大小。
- **音频路由**：自动将来自手机的音频流路由至本机扬声器或有线/蓝牙输出设备，支持通话、导航提示和媒体播放。
- **启动器集成**：可作为独立应用启动，也可配置为系统启动时自动运行，适合嵌入车载场景。
- **开源与可定制**：源码完全开放（AGPL-3.0 许可），允许用户自行编译、修改界面或集成额外功能。

## 技术架构

项目使用 Kotlin 语言开发，基于 Android SDK 构建，并集成了 Android Auto 协议中的接收端实现。其关键设计思路包括：

- **通信层**：通过 USB（通过 Android Open Accessory 协议）或 Wi-Fi（基于 Android Auto 的无线标准）与手机通信，实时传输屏幕画面、音频和控制事件。
- **渲染引擎**：接收手机端编码的视频流，解码后通过 SurfaceView 或类似组件在本地屏幕渲染，并处理触摸事件回传到手机。
- **音频处理**：使用 Android 的 AudioTrack API 或 OpenSL ES 实现低延迟播放，同时处理音频焦点和混音。
- **生命周期管理**：针对车载环境优化了后台服务，支持断线重连和自动恢复。

架构上的一个特点是模块化程度较高，使得开发者可以较容易地更换 UI 皮肤或适配特殊硬件（如自定义触摸屏旋钮）。

## 安装与使用

### 安装步骤
1. 从 Google Play 或 Amazon Appstore 直接下载安装 Headunit Revived 应用，或从 GitHub Releases 页面下载 APK 文件手动安装。
2. 在作为接收端的设备（旧手机或平板）上安装应用。
3. 确保接收端设备支持 USB OTG 或具备稳定的 Wi-Fi 连接能力。

### 最小可用示例
1. 在接收端设备上启动 Headunit Revived 应用。
2. 如果使用 USB 连接，用数据线将接收端设备与手机相连（部分手机需在开发者选项中启用“通过 USB 调试 Android Auto”）。
3. 如果使用 Wi-Fi，确保两台设备在同一局域网，然后在接收端应用中选择“无线”模式并搜索设备。
4. 在手机上确认连接授权后，Android Auto 界面将显示在接收端设备上。

## 适用场景

- **改装老旧车载系统**：将旧车的中控屏幕替换为 Android 平板，运行本应用即可获得 Android Auto 的导航、音乐、通话功能，无需更换昂贵的主机。
- **DIY 智能仪表盘**：利用闲置的平板电脑或车载级安卓主板，制作自定义抬头显示器，显示 Android Auto 信息。
- **临时解决方案**：在旅途中作为手机大屏投屏工具，将手机导航或节目投放到车机或显示设备上。
- **开发与测试**：Android Auto 应用开发者可以使用此接收端进行功能验证和界面测试，无需购买支持 Android Auto 的实体车机。

## 项目亮点

与同类项目（如 OpenAuto、CarWebGuru 等）相比，Headunit Revived 的差异化优势在于：

- **成熟的开源协议继承**：基于原版 headunit 项目延续开发，已积累较久的历史和社区经验，bug 修复和功能迭代持续活跃。
- **针对 Android 设备的深度优化**：专门为 Android 平板和手机设计，对屏幕兼容性和触控延迟做了针对性优化，而非简单地移植自 PC 端。
- **多商店发布**：同时上架 Google Play 和 Amazon Appstore，降低了普通用户的安装门槛。
- **详细的 Wiki 文档**：项目 Wiki 提供了大量配置指南和常见问题解答，帮助用户在不同硬件上完成部署。

## 相关链接

- [GitHub 仓库](https://github.com/andreknieriem/headunit-revived)
- [项目 Wiki](https://github.com/andreknieriem/headunit-revived/wiki)
- [Google Play 页面](https://play.google.com/store/apps/details?id=com.andrerinas.headunitrevived)
- [Amazon Appstore 页面](http://www.amazon.com/gp/mas/dl/android?p=com.andrerinas.headunitrevived)
