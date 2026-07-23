---
tags:
  - trending
  - article
repo: ruvnet/RuView
date: 2026-07-23
language: Rust
stars_total: 84101
stars_today: 741
---
## 项目概述

π RuView 是一个基于 WiFi 信号的空间智能感知系统，能够将普通商用 WiFi 无线信号转化为实时空间信息、生命体征监测和存在检测能力。该项目由 ruvnet 开发，使用 Rust 语言编写，核心价值在于完全无需摄像头或可穿戴设备，仅通过分析 WiFi 信号的物理特性变化，即可实现穿透墙壁的人员检测、呼吸心率测量、运动跟踪和房间监控等功能。

项目面向智能家居爱好者、安防监控从业者、医疗健康研究人员以及希望在不侵犯隐私前提下实现空间感知的开发者。RuView 直接兼容四大主流智能家居生态：Home Assistant、Apple Home、Google Home 和 Amazon Alexa，降低了集成门槛。

## 核心功能

- **穿墙存在检测**：利用 WiFi 信号在人体周围产生的衍射和散射效应，判断房间内是否有人，可穿透砖墙、木墙等常见建筑材料
- **生命体征监测**：通过分析 WiFi 信道状态信息的微小波动，测量呼吸频率和心率，精度接近医疗级设备
- **运动跟踪与轨迹还原**：实时追踪人员在空间中的移动轨迹，支持多目标区分
- **智能家居全生态集成**：原生支持 Home Assistant、Apple Home（HAP-1.1 桥接）、Google Home、Amazon Alexa 和 Matter 协议
- **语音查询能力**：Siri、Google Assistant 和 Alexa 可直接查询指定房间的人员存在状态和生命体征数据，无需编写自定义技能
- **零摄像头隐私保护**：完全不使用任何图像传感器，所有数据均来自 WiFi 信号的物理分析，从设计上杜绝隐私泄露风险

## 技术架构

RuView 的核心技术建立在 WiFi 信道状态信息分析之上。传统 WiFi 通信中，信号在室内空间传播时会受到环境物体的影响，人体作为导电介质会引发独特的信号扰动。RuView 从商用 WiFi 网卡获取 CSI 数据，通过 Rust 语言实现的高性能信号处理流水线，实时提取人体运动、呼吸和心跳引起的微多普勒特征。

架构上，RuView 采用模块化设计，主要包括：

- **信号采集层**：通过修改后的 WiFi 驱动或专用网卡获取原始信道状态信息
- **物理分析引擎**：使用滤波算法和机器学习模型分离环境噪声与人体信号，提取呼吸、心跳等微弱特征
- **空间建模模块**：基于多天线信号到达时间差和角度信息，构建室内三维空间模型
- **协议转换层**：将感知结果转换为 Home Assistant MQTT、Apple Home HAP、Matter 等标准协议
- **桥接模式支持**：可通过 `--mqtt` 参数直接接入 Home Assistant，或作为 Matter 端点被 Google Home、Alexa 和 SmartThings 发现

技术设计强调实时性和低延迟，Rust 语言的无 GC 特性确保了信号处理管线的确定性性能。所有计算均在本地完成，无需云端处理，数据隐私得到充分保障。

## 安装与使用

RuView 提供多种安装方式，推荐在具备 Intel 或 ARM 处理器的 Linux 主机上运行。

**基本安装步骤：**

1. 确保系统已安装 Rust 工具链（`rustup` 和 `cargo`）
2. 克隆仓库：
   ```
   git clone https://github.com/ruvnet/RuView.git
   cd RuView
   ```
3. 编译项目：
   ```
   cargo build --release
   ```
4. 启动服务（接入 Home Assistant）：
   ```
   ./target/release/ruview --mqtt -b mqtt://homeassistant.local:1883
   ```

**最小可用示例：**

使用默认配置运行，RuView 将自动扫描可用 WiFi 信号，并开始空间感知分析。接入 Home Assistant 后，会自动创建设备实体，每个房间对应一个 binary_sensor（存在检测）、sensor（呼吸率、心率）等。

## 适用场景

- **智能家居自动化**：根据房间是否有人自动调节灯光、空调、窗帘等设备，实现真正的动态舒适响应
- **老人与婴幼儿监护**：在不安装摄像头的前提下，实时监测房间内人员的呼吸和心跳状态，异常时及时告警
- **办公空间管理**：统计会议室、工位区域的人员密度和驻留时间，优化空间利用率
- **安防与入侵检测**：在无人情况下检测非法闯入，穿透墙壁感知可疑活动，配合智能家居报警系统

## 项目亮点

RuView 与同类产品相比有以下差异化优势：

- **完全无摄像头**：不使用任何图像传感器，从物理层解决隐私焦虑，适合卧室、浴室等敏感区域
- **全本地处理**：所有信号分析在本地完成，不依赖云服务，数据不外传
- **生态无缝集成**：同时支持 Home Assistant、Apple Home、Google Home、Alexa 和 Matter，无需额外网关或桥接软件
- **Rust 高性能**：相比 Python 实现的类似项目，RuView 具有更低延迟和更高吞吐量，支持多房间实时监测
- **开源许可**：采用 MIT 许可，允许商业使用和二次开发

## 相关链接

- [GitHub 仓库](https://github.com/ruvnet/RuView)
- [Home Assistant 集成文档](docs/integrations/home-assistant.md)
- [Apple HomePod 用户指南](docs/user-guide-apple-homepod.md)
- [Matter 集成设计文档](docs/adr/ADR-122-bfld-ruview-ha-matter-exposure.md)
