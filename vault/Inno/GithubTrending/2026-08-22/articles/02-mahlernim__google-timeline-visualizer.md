---
tags:
  - trending
  - article
repo: mahlernim/google-timeline-visualizer
date: 2026-08-22
language: Kotlin
stars_total: 2258
stars_today: 1053
---
## 项目概述

Timeline Visualizer 是一款将 Google 位置历史（Timeline）数据转化为动画旅行视频的工具。它由开发者 mahlernim 发布，采用 Kotlin 语言编写，支持 Android 原生应用和 iPhone 网页应用两种形态。该项目解决了用户查看静态位置记录不够直观的问题，让用户能够以动态视频的形式回顾自己一年中的旅行轨迹，目标用户是那些关心个人出行记录、喜欢制作旅行纪念内容的 Google 地图用户。

## 核心功能

- **时间范围选择**：支持精确到月份甚至具体日期的筛选，用户可以选择任意时间片段来生成视频。
- **旅行路径预览**：在正式生成视频前，用户可在地图上预览整个旅程的动画效果，确认路径和视角是否符合预期。
- **MP4 视频导出**：直接生成标准 H.264 编码的 MP4 文件，兼容主流播放器和社交平台分享。
- **多端支持**：Android 用户可通过安装 APK 使用原生应用，iPhone 用户则通过 Safari 访问网页应用，无需安装任何软件。
- **隐私保护**：所有处理均在本地设备完成，不涉及 Timeline 数据上传，网页版也明确声明不会收集用户数据。
- **多语言界面**：提供中文、韩语、日语、英语等多种语言支持，方便不同地区的用户使用。

## 技术架构

该项目在技术实现上采用了双端共用的设计思路。Android 端使用 Kotlin 开发，充分利用了 Android 平台的硬件加速能力和图形渲染接口，实现了流畅的地图动画和视频编码。iPhone 端则是一个纯前端网页应用，基于现代 Web 技术（如 Canvas 和 MediaRecorder API）在浏览器内完成地图渲染和视频生成，并调用了 Safari 16.4 以上版本支持的 H.264 硬件编码能力。

值得关注的是，两个端共享相同的核心算法和交互逻辑。项目通过抽象层将地图渲染、路径插值、相机运动等核心模块与具体平台解耦，使得功能保持一致性的同时，也减少了维护成本。此外，项目通过 Gradle 构建系统管理依赖，并使用 GitHub Releases 分发 Android 安装包，流程清晰简洁。

## 安装与使用

**Android 安装步骤：**

1. 访问项目的 [latest release](https://github.com/mahlernim/google-timeline-visualizer/releases/latest) 页面。
2. 在 Assets 区域下载最新的 `TimelineVisualizer-*.apk` 文件（忽略 `.sha256` 校验文件）。
3. 在手机上打开下载的 APK 文件。
4. 若系统阻止安装，请在设置中允许浏览器或文件管理器“安装未知应用”。
5. 安装完成后，从应用列表打开 Timeline Visualizer。

**Android 使用流程：**

1. 在 Google 地图中导出 Timeline 数据：点击个人头像 → 设置 → 个人内容 → 导出 Timeline 数据，获取 `Timeline.json` 文件。
2. 在应用中导入该文件。
3. 选择月份范围或具体日期，设置相机运动方式。
4. 确认地图隐私提示后，预览旅程动画。
5. 点击“创建 MP4”生成视频，完成保存或分享。

**iPhone 使用流程：**

1. 在 Safari 中打开 [网页应用](https://ahn-lab.org/google-timeline-visualizer/)。
2. 同样先导出 `Timeline.json` 文件，然后点击“选择 Timeline.json”导入。
3. 后续操作与 Android 端一致。网页版要求 Safari 16.4 或更高版本，生成视频期间请保持标签页打开。
4. 如需将应用添加到主屏幕，可使用 Safari 的分享菜单选择“添加到主屏幕”。

## 适用场景

- **年度旅行回顾**：用户可在年末将一年的地理轨迹整合成一段数分钟的视频，直观展示自己在过去一年中走过的地方。
- **旅行 Vlog 素材**：内容创作者可以将 Timeline 动画嵌入旅行记录视频中，作为路线展示的辅助画面。
- **出行数据分析**：对个人出行习惯感兴趣的用户，可以通过视频方式更直观地观察自己的活动半径和常去区域。
- **家庭记忆存档**：将家庭出游的路径做成视频保存，作为数字记忆册的一部分。

## 项目亮点

相较于市面上的位置轨迹可视化工具，Timeline Visualizer 最大的差异化优势在于它完全在本地设备上完成数据处理和视频渲染，无需将敏感的位置历史上传到任何第三方服务器，这对于注重隐私的用户来说是重要的考量点。此外，项目提供了 iPhone 和 Android 双平台的覆盖，特别是网页版的实现，让 iOS 用户无需安装任何应用即可使用完整功能。视频输出的质量也经过了优化，生成的 MP4 采用标准的 H.264 编码，兼容性极佳。最后，项目采用 MIT 开源许可，代码完全公开透明，用户可自行审计，也便于开发者在此基础上进行二次开发。

## 相关链接

- [GitHub 仓库](https://github.com/mahlernim/google-timeline-visualizer)
- [iPhone 网页应用](https://ahn-lab.org/google-timeline-visualizer/)
- [最新版本下载](https://github.com/mahlernim/google-timeline-visualizer/releases/latest)
