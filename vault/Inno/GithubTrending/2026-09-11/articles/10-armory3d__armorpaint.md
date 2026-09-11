---
tags:
  - trending
  - article
repo: armory3d/armorpaint
date: 2026-09-11
language: C
stars_total: 4525
stars_today: 72
---
## 项目概述

ArmorPaint 是一款面向 3D 资产制作的 PBR（基于物理的渲染）纹理绘制软件，由 armory3d 团队使用 C 语言开发并开源在 GitHub 上。它解决的问题是：让美术人员能够在实时渲染环境中直接在 3D 模型表面绘制材质纹理，而无需依赖昂贵的商业软件授权。项目采用基于节点的程序化材质系统，支持将绘制结果导出为标准的 PBR 贴图集，供游戏引擎和实时渲染管线使用。

需要特别说明的是，该仓库定位为开发者版本，主要服务于希望编译、调试或修改 ArmorPaint 源码的开发者群体。官方分发的稳定二进制版本需要付费购买，以此支撑项目的持续开发；但全部源代码在此仓库中公开，保证了技术上的可访问性。因此，目标用户包括：希望自建纹理绘制工具链的技术美术、需要将 ArmorPaint 集成到自有管线中的工作室开发者，以及关注实时 PBR 绘制技术实现的开源贡献者。

## 核心功能

- **PBR 纹理绘制**：支持在 3D 模型表面直接绘制反照率、粗糙度、金属度、法线、高度等 PBR 通道，并实时预览最终渲染效果。
- **基于节点的材质系统**：通过节点图构建程序化材质逻辑，可将噪声、遮罩、数学运算等节点与手绘纹理混合，实现非破坏性的材质创作流程。
- **多平台支持**：代码库可编译至 Windows、Linux、macOS、Android 与 iOS 平台，为桌面与移动端的纹理绘制提供统一的代码基础。
- **图层与笔刷体系**：提供图层化的绘制结构，支持自定义笔刷、遮罩与填充工具，便于对绘制内容进行分层管理与后期调整。
- **贴图导出**：可将绘制结果烘焙导出为多张标准 PBR 贴图，供外部游戏引擎或渲染器直接使用。
- **GPU 加速的实时渲染**：底层基于图形 API 实现在视口中实时显示绘制效果，降低反复预览的时间成本。

## 技术架构

ArmorPaint 的代码库以 C 语言为主体，采用自研的轻量级引擎架构，并借助 Kha 多媒体框架（armory3d 生态系统的一部分）实现跨平台抽象。Kha 提供了对图形 API（如 Direct3D、OpenGL、Metal、Vulkan 后端）、窗口系统、输入设备与音频的统一封装，使同一套绘制逻辑能够部署到桌面与移动平台。

项目的构建系统并不依赖 CMake 等通用工具，而是通过 `base/make` 脚本生成各平台的工程文件（Visual Studio 工程、Xcode 工程、Android Studio 工程），再由对应 IDE 完成编译。这种设计减少了跨平台构建的环境配置负担，但要求开发者预先安装平台特定的编译工具链（Windows 上的 Visual Studio 与 clang 工具、Linux 上的 clang 及依赖、macOS 上的 Xcode 等）。

渲染层面，ArmorPaint 将绘制操作映射到离屏纹理上，通过着色器在 GPU 中执行混合、遮罩与通道写入，从而实现流畅的实时笔刷反馈。材质节点系统在内部被编译为着色器指令，使程序化逻辑与手绘像素共用同一条渲染管线。此外，项目还包含用于模型导入、UV 处理与烘焙导出的辅助模块，整体结构偏向工程实用而非学术性的架构分层。

## 安装与使用

从源码构建 ArmorPaint 需要先准备编译环境与 git。Windows 用户需安装带 clang 工具的 Visual Studio，Linux 用户需按仓库内 `base/docs/linux_deps.md` 安装 clang 与依赖，macOS/iOS 用户需安装 Xcode，Android 用户需安装 Android Studio。

基本步骤如下：

```bash
git clone https://github.com/armory3d/armorpaint
cd armorpaint/paint
```

随后按平台执行构建：

- **Windows (x64)**：运行 `..\base\make`，打开生成的 `build\ArmorPaint.sln`，编译并运行。
- **Linux (x64)**：运行 `../base/make --run` 直接构建并启动。
- **macOS (arm64)**：运行 `../base/make`，打开 `build/ArmorPaint.xcodeproj`，编译运行。
- **Android (arm64)**：运行 `../base/make --target android`，打开 `build/ArmorPaint` 后为设备构建。
- **iOS (arm64)**：运行 `../base/make --target ios`，在 Xcode 工程中构建部署。

启动后，导入 3D 模型即可在视口中创建材质、添加图层并开始绘制。具体操作流程可参考官方手册（armorpaint.org/manual），其中涵盖了笔刷设置、节点编辑与导出的详细说明。

## 适用场景

- **游戏资产纹理制作**：为角色、道具与场景模型绘制 PBR 贴图，并导出至 Unity、Unreal 等引擎使用。
- **技术美术管线定制**：团队可基于源码修改绘制逻辑、扩展节点类型，或将 ArmorPaint 嵌入自研的内容生产流程。
- **跨平台移动绘制实验**：借助 Android/iOS 构建目标，在平板设备上进行纹理绘制与移动端渲染验证。
- **开源渲染与绘制技术研究**：开发者可研究其 GPU 绘制管线、节点求值与跨平台框架集成方式，作为自研工具的技术参考。

## 项目亮点

与 Substance Painter 等商业纹理绘制软件相比，ArmorPaint 的核心差异在于源码完全开放以及跨平台构建能力。开发者可以直接阅读并修改绘制引擎的实现，而不受二进制授权限制。同时，项目复用了 armory3d 生态中的 Kha 框架，使其能够以相对统一的代码库覆盖桌面与移动端，这在同类开源纹理工具中并不常见。此外，仓库将开发版与付费发行版分离，既保证了资金可持续性，也让技术社区能够跟进最新开发进展。需要注意的是，由于该仓库面向开发者，git 版本可能存在不稳定性，生产环境使用建议以官方发行版为准。

## 相关链接

- [GitHub 仓库](https://github.com/armory3d/armorpaint)
- [官方网站](https://armorpaint.org)
- [官方手册](https://armorpaint.org/manual)
- [下载页面](https://armorpaint.org/download)
