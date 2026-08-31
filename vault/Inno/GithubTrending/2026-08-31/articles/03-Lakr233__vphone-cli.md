---
tags:
  - trending
  - article
repo: Lakr233/vphone-cli
date: 2026-08-31
language: Swift
stars_total: 9872
stars_today: 361
---
## 项目概述

vphone-cli 是一个基于 Swift 构建的命令行工具，它利用 Apple 官方的 Virtualization.framework 和 PCC（Private Cloud Compute）研究虚拟机基础设施，在 Apple Silicon Mac 上启动虚拟 iPhone。该项目解决了开发者在没有实体 iPhone 的情况下进行 iOS 系统开发、测试和安全研究的痛点，提供了一套完整的虚拟机生命周期管理方案。

该项目主要面向 iOS 安全研究员、系统开发者和需要跨版本测试的移动应用开发者。通过 vphone-cli，用户可以在 macOS 上创建、启动和管理多个虚拟 iPhone 实例，每个实例都运行真实的 iOS 系统，而非模拟器。

## 核心功能

- **一键创建虚拟机**：`vphone-cli vm create` 命令自动完成从固件下载、系统补丁、DFU 恢复、CFW 安装到首次启动的完整流程
- **多实例管理**：支持创建和管理多个独立的虚拟 iPhone，通过 `vm l` 命令查看所有实例状态
- **变体选择**：支持 `-V` 参数选择不同系统变体（如越狱版 `jb`），满足不同研究需求
- **分阶段执行**：提供细粒度的子命令，允许用户手动控制或重跑管线的每个阶段
- **原生性能**：基于 Virtualization.framework 实现硬件加速，性能接近真实设备
- **命令行集成**：完全通过 CLI 操作，适合脚本化和自动化工作流

## 技术架构

vphone-cli 的技术架构体现了多个层级的巧妙设计：

**底层虚拟化**：项目直接使用 Apple 的 Virtualization.framework，这是 macOS 上最底层的虚拟化 API，能够直接利用 Apple Silicon 的虚拟化扩展，提供接近原生的执行效率。

**访客守护进程**：项目包含一个名为 `vphoned` 的跨编译守护进程，它运行在虚拟 iOS 系统内部，负责与宿主机通信，实现文件共享、端口转发和系统控制等功能。这个守护进程需要借助 Xcode 和 iOS SDK 进行交叉编译。

**固件处理管线**：虚拟机的创建过程包含一套完整的处理管线：首先下载原始 IPSW 固件，然后应用必要的补丁修改系统映像，接着通过 DFU 模式恢复固件，再安装定制的 CFW（Custom FirmWare），最后完成引导。这一管线借鉴了 PCC 研究社区的技术积累。

**工具链依赖**：项目依赖多个成熟的开源工具，包括用于解包固件的 `ipsw`、用于处理签名的 `ldid-procursus`、用于密钥管理的 `keystone`，以及 aria2 下载加速器、Python 3.13 等，构建了一个完整的工具链环境。

**签名处理**：为了在虚拟环境中运行未经 Apple 官方签名的代码，项目需要放宽 SIP/AMFI 安全策略，以允许私有 PV=3 entitlements 与未签名二进制文件的加载。

## 安装与使用

**安装依赖**：

```bash
brew install python@3.13 aria2 wget gnu-tar openssl@3 ldid-procursus sshpass keystone cmake libusb ipsw zstd
```

**通过 Homebrew 安装**：

```bash
brew install zqxwce/tap/vphone-cli
```

**从源码构建**：

```bash
git clone --recurse-submodules https://github.com/Lakr233/vphone-cli.git
./scripts/setup_tools.sh   # 安装依赖并构建工具链
./scripts/build.sh         # 编译并签名 vphone-cli 及 vphoned

cd .build/vphone-cli.app/Contents/MacOS/
vphone-cli --help
```

**快速启动**：

```bash
# 创建一台越狱版虚拟 iPhone
vphone-cli vm create myphone -V jb

# 启动虚拟机
vphone-cli vm launch myphone
```

**前置要求**：宿主机必须为 Apple Silicon 芯片，运行 macOS 15+（Sequoia），并且需要按照项目文档放宽 SIP/AMFI 安全策略以允许特定 entitlements 的使用。

## 适用场景

- **iOS 安全研究**：安全研究员可以在隔离的虚拟环境中分析系统漏洞、测试越狱工具、进行恶意软件行为分析，而无需担心影响实体设备
- **多版本兼容性测试**：应用开发者可以同时运行多个不同 iOS 版本的虚拟实例，快速验证应用的版本兼容性
- **CI/CD 集成**：团队可以将 vphone-cli 集成到持续集成流水线中，自动化执行 UI 测试、性能基准和回归测试
- **系统开发与调试**：iOS 系统开发者可以利用虚拟化环境调试系统组件，测试内核扩展和系统级修改

## 项目亮点

与现有的 iOS 模拟器和云端真机方案相比，vphone-cli 提供了几个独特的差异化优势：

- **真实系统体验**：与 Xcode 模拟器不同，vphone-cli 运行完整的 iOS 系统镜像，支持越狱环境，行为与实体设备完全一致
- **资源效率**：基于 Virtualization.framework 的硬件虚拟化比模拟器更高效，一台 Mac 上可以并发运行多个实例
- **全自动化管线**：从固件下载到系统引导的完整流程一条命令完成，无需手动操作 iTunes 或配置网络恢复
- **研究与社区导向**：项目继承了 PCC Research VM 的技术成果，为 iOS 安全研究社区提供了可复用的基础设施
- **开放源码**：MIT 许可证发布，开发者可以审查、修改和扩展所有功能

## 相关链接

- [GitHub 仓库](https://github.com/Lakr233/vphone-cli)
- 多语言文档：仓库内 `docs` 目录提供中文、日文和韩文版本
