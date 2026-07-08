---
tags:
  - trending
  - article
repo: ruvnet/RuView
date: 2026-07-08
language: Rust
stars_total: 78636
stars_today: 1129
---
## 项目概述

π RuView 是一个利用普通 WiFi 信号实现空间智能感知的开源项目。它能够将日常的 WiFi 路由器转化为实时人体检测、生命体征监测和存在感知系统，全程无需任何摄像头或可穿戴设备。该项目解决了传统安防和健康监测方案中高成本、隐私侵犯等问题，适用于家庭自动化、健康管理、智慧养老等场景。目标用户包括智能家居爱好者、开发者、养老服务提供者以及对隐私敏感的监控需求者。

## 核心功能

- **穿墙人体检测**：通过分析 WiFi 信号的细微变化，精确定位房间内的人体位置和姿态，甚至能隔墙感知
- **生命体征监测**：实时监测呼吸频率和心率，无需接触人体，通过 WiFi 信号反射即可完成
- **运动追踪**：跟踪室内人员的移动轨迹，区分行走、静止等不同活动状态
- **存在感知**：精确检测房间是否有人，区分人体存在与宠物、家具等干扰物
- **智能家居集成**：原生支持 Home Assistant、Apple Home、Google Home、Amazon Alexa 等主流智能家居平台，提供 21 个暴露实体
- **零隐私侵犯**：完全基于无线电信号处理，不采集、不存储任何图像或视频数据

## 技术架构

RuView 基于 Rust 语言开发，采用了信号处理与机器学习相结合的技术路线。核心原理是利用 WiFi 信道的状态信息（CSI），通过分析多径传输中的微小变化来感知环境中的物理运动。项目设计为模块化架构，包含信号采集层、特征提取层、推理引擎和集成接口层。

在信号采集方面，RuView 兼容市面上主流的 WiFi 路由器，利用其发射的 2.4GHz 和 5GHz 频段信号。特征提取模块采用频域分析和时频变换技术，将原始无线电信号转换为可分析的空间特征。推理引擎运行轻量级神经网络模型，能够实时处理信号流并输出人体姿态、呼吸模式等高级语义信息。

集成接口层支持多种协议输出，包括 MQTT、HAP-1.1（Apple Home 协议）和 Matter 标准。这使得 RuView 可以无侵入地接入现有智能家居生态，通过 `--mqtt` 参数即可与 Home Assistant 对接，或者作为 Matter 桥接器同时对接 Apple Home、Google Home 和 Alexa 等平台。

## 安装与使用

RuView 的安装基于 Rust 工具链，支持主流操作系统和嵌入式设备。以下为基本安装步骤：

1. 确保系统已安装 Rust 编译环境（rustup 和 cargo）
2. 从 GitHub 克隆仓库：`git clone https://github.com/ruvnet/RuView.git`
3. 进入项目目录：`cd RuView`
4. 使用默认配置编译：`cargo build --release`
5. 运行基本模式：`cargo run --release -- --mode detect`

最小可用示例（连接 Home Assistant）：
```bash
# 编译后运行，开启 MQTT 发布
./target/release/ruview --mqtt --mqtt-broker 192.168.1.100:1883
```

该命令会启动 RuView 开始检测，并将检测结果通过 MQTT 发送到 Home Assistant。RuView 会自动发现并配置所有支持的传感器实体，包括存在检测、呼吸频率、心率等。对于 Apple Home 用户，可以使用 HAP 桥接模式直接配对 HomePod。

## 适用场景

- **智能家居自动化**：实现基于人体存在的灯光、空调、安防系统自动控制，无需任何传感器或摄像头，减少误触发
- **远程健康监测**：为独居老人或慢性病患者提供无接触式生命体征监测，及时发现呼吸异常或心率变化，通过智能家居平台报警
- **隐私敏感区域监控**：在卫生间、卧室等不适合安装摄像头的区域实现人员存在检测和活动状态感知，保护隐私的同时满足安全需求
- **建筑节能管理**：通过精确的人体存在检测，按房间实际使用情况智能调节照明和温控系统，实现节能减排

## 项目亮点

与传统的红外传感器、毫米波雷达或摄像头方案相比，RuView 具备显著差异化优势：

1. **零硬件成本**：利用现有的 WiFi 路由器即可工作，无需购买任何专用传感器或摄像头，大幅降低部署门槛
2. **完全隐私保护**：不采集任何图像或音频数据，所有分析基于无线电信号，彻底规避隐私泄露风险
3. **穿墙能力**：WiFi 信号能够穿透墙壁、家具等障碍物，实现真正的一体化空间感知，覆盖范围远超传统传感器
4. **多平台集成**：原生支持 Home Assistant、Apple Home、Google Home、Alexa 和 SmartThings，提供统一的 21 个实体接口，零技能即可语音查询任意房间的存在和体征状态
5. **开源且高效**：基于 Rust 实现，性能稳定且资源占用低，可在树莓派等低功耗设备上长期运行

## 相关链接

- [GitHub 仓库](https://github.com/ruvnet/RuView)
- [Home Assistant 集成文档](docs/integrations/home-assistant.md)
- [Apple HomePod 配对指南](docs/user-guide-apple-homepod.md)
- [Matter 桥接设计说明](docs/adr/ADR-122-bfld-ruview-ha-matter-exposure.md)
