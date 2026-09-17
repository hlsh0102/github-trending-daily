---
tags:
  - trending
  - article
repo: Lakr233/vphone-cli
date: 2026-09-17
language: Swift
stars_total: 13491
stars_today: 547
---
## 项目概述

vphone-cli 是一个命令行工具，用于在 Apple Silicon Mac 上启动虚拟 iPhone。它基于 Apple 的 Virtualization.framework，并借助 PCC（Private Cloud Compute）研究虚拟机基础设施，将原本用于云端研究的虚拟化能力引入本地开发环境。

长期以来，在 Mac 上运行 iOS 环境主要依赖官方模拟器，而模拟器与真实设备的系统行为存在差异，难以覆盖底层启动流程、固件安装和越狱等场景。vphone-cli 通过完整的「下载 → 补丁 → DFU 恢复 → CFW 安装 → 首次启动」流水线，在本地创建可运行的虚拟 iPhone，填补了模拟器与实体设备之间的空白。

目标用户包括 iOS 越狱与安全研究人员、需要复现底层系统行为的研究者，以及希望在本地环境中测试设备级流程的开发者。使用前提是 Apple Silicon 主机、macOS 15+、Xcode 与 iOS SDK，并需要对 SIP/AMFI 进行放宽以允许未签名二进制携带私有 PV=3 权限。

## 核心功能

- **一键创建虚拟机**：`vphone-cli vm create` 将下载、打补丁、DFU 恢复、CFW 安装与首次启动整合为单条命令，降低完整流程的操作成本。
- **自定义变体**：通过 `-V` / `--variant` 参数选择不同变体（如 `jb`），适配越狱等不同用途的镜像配置。
- **虚拟机生命周期管理**：提供 `vm launch` 启动虚拟机，`vm l` 列出已有虚拟机，便于多实例管理。
- **分步驱动**：完整流水线中的每个阶段均可单独执行，方便手动控制、调试或在失败后仅重跑某一环节。
- **访客守护进程交叉编译**：构建流程会交叉编译 `vphoned` 访客守护进程，配合主机侧工具完成通信与状态上报。

## 技术架构

项目以 Swift 编写，主体依赖 Apple 的 Virtualization.framework 来管理虚拟机生命周期，并复用 PCC 研究虚拟机基础设施中的启动与恢复逻辑，使虚拟 iPhone 能够执行接近真实设备的引导链路。

构建体系由脚本驱动：`scripts/setup_tools.sh` 负责安装依赖、构建子模块工具链并创建 Python 虚拟环境；`scripts/build.sh` 负责编译并签名 vphone-cli、打包 `.app`，同时交叉编译访客端 `vphoned`。仓库使用 `--recurse-submodules` 拉取，说明工具链与相关组件以子模块形式维护。

签名与权限方面，项目依赖 `ldid-procursus` 以及 SIP/AMFI 放宽，以便未签名二进制能够携带私有 PV=3 权限。虚拟机创建阶段需要处理 IPSW 固件、DFU 恢复与自定义固件（CFW）安装，因此外部依赖较多，包括 `ipsw`、`aria2`、`wget`、`gnu-tar`、`openssl@3`、`keystone`、`cmake`、`libusb`、`zstd`、`sshpass` 与 Python 3.13。

## 安装与使用

通过 Homebrew 安装：

```bash
brew install zqxwce/tap/vphone-cli
```

如需从源码构建：

```bash
git clone --recurse-submodules https://github.com/Lakr233/vphone-cli.git

./scripts/setup_tools.sh      # 安装依赖、构建工具链子模块、创建 Python venv
./scripts/build.sh            # 构建并签名 vphone-cli、打包 .app、交叉编译 vphoned

cd .build/vphone-cli.app/Contents/MacOS/
vphone-cli --help
```

最小可用示例是端到端创建并启动一台虚拟机：

```bash
vphone-cli vm create myphone -V jb

vphone-cli vm launch myphone
```

`vm create` 会自动完成下载、补丁、DFU 恢复、CFW 安装与首次启动；如需手动控制，可单独执行各阶段命令。使用前请先确认主机满足 Apple Silicon、macOS 15+ 与 SIP/AMFI 放宽等前提条件。

## 适用场景

- **越狱与系统研究**：在本地虚拟设备上验证越狱流程、固件补丁与系统行为，无需依赖实体设备。
- **底层流程复现**：研究 DFU 恢复、CFW 安装与引导链路等通常难以在模拟器中触发的环节。
- **CI 或脚本化测试**：借助命令行接口，将虚拟 iPhone 的创建与启动纳入自动化流程。
- **多环境并行验证**：使用 `vm l` 管理多台虚拟机，在不同变体或配置之间切换对比。

## 项目亮点

与官方 iOS 模拟器相比，vphone-cli 走的是完整设备虚拟化路线，覆盖固件下载、恢复模式与自定义固件安装，可触及模拟器无法覆盖的底层环节。与依赖实体设备的传统流程相比，它在 Apple Silicon Mac 上以纯软件方式创建虚拟 iPhone，并通过单条命令封装了复杂的多阶段流水线。此外，项目直接复用 PCC 研究虚拟机基础设施，将原本面向云端研究的虚拟化能力开放给本地开发者，在同类方案中较为少见。

## 相关链接

- [GitHub 仓库](https://github.com/Lakr233/vphone-cli)
- [中文文档](./docs/README_zh.md)
