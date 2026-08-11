---
tags:
  - trending
  - article
repo: ruvnet/RuView
date: 2026-08-11
language: Rust
stars_total: 89421
stars_today: 154
---
## 项目概述

RuView（π RuView）是一个基于 Rust 编写的开源项目，致力于将普通的 WiFi 信号转化为实时空间智能、生命体征监测和存在检测能力——全程不依赖任何摄像头或可穿戴设备。项目的核心理念是“透过墙壁看世界”，利用射频信号在室内环境中的传播特性，实现对人员存在、呼吸频率、心率以及移动轨迹的感知。

该项目由 ruvnet 团队开发，面向智能家居爱好者、安防监控领域开发者、医疗健康监测研究人员以及对隐私保护有高要求的用户群体。RuView 完全基于物理学原理工作，无需部署额外硬件，只需利用环境中已有的 WiFi 路由器即可构建一套非侵入式传感系统。

## 核心功能

- **穿墙人体检测**：通过分析 WiFi 信道状态信息（CSI）的变化，实现隔墙检测人员存在，不受光线和视线遮挡影响。
- **生命体征监测**：实时提取呼吸频率和心率数据，精度足以满足日常健康监测和睡眠分析需求。
- **运动轨迹追踪**：在室内环境中追踪人员的移动路径和位置，支持多房间场景下的活动感知。
- **智能家居生态集成**：原生支持 Home Assistant、Apple Home（HomePod）、Google Home 和 Amazon Alexa 四大主流智能家居平台。
- **语音交互能力**：通过 Siri、Google Assistant 和 Alexa，用户可以直接语音询问各房间的人员存在状态和生命体征数据。
- **隐私零牺牲**：不采集任何图像或音频数据，完全基于射频信号处理，从根本上杜绝隐私泄露风险。

## 技术架构

RuView 采用 Rust 语言开发，充分利用了 Rust 在内存安全、并发处理和性能表现方面的优势，确保实时信号处理任务的高效与可靠。

项目的核心架构包含以下关键组件：

1. **WiFi 前端采集模块**：负责从标准 WiFi 网卡捕获信道状态信息（CSI）数据，利用商用 WiFi 芯片组的底层接口提取细粒度的射频特征。
2. **信号处理引擎**：对 CSI 时序数据进行滤波、去噪和特征提取，采用先进的信号处理算法分离环境静态成分与人体反射动态成分。
3. **生物特征提取层**：针对呼吸和心跳引起的微多普勒效应，使用频域分析算法精确解析生命体征参数。
4. **空间定位引擎**：综合多天线和多通道的相位信息，通过到达角（AoA）和飞行时间（ToF）技术实现亚米级定位精度。
5. **HA-DISCO MQTT 发布器**：以标准 MQTT 协议向 Home Assistant 等平台推送标准化数据，实现无缝对接。
6. **HAP-1.1 桥接层**：作为可发现的 Apple HomeKit 桥接设备，直接接入 Apple 生态系统，无需额外设置。

整体设计遵循模块化和可扩展原则，支持通过插件或配置添加新的智能家居协议支持（如 Matter 端点）。

## 安装与使用

RuView 的安装过程相对简洁，适用于具备基本命令行操作经验的用户。

**安装步骤：**

1. 确保系统已安装 Rust 工具链（建议使用 rustup 安装最新稳定版）。
2. 克隆仓库并进入项目目录：
   ```bash
   git clone https://github.com/ruvnet/RuView.git
   cd RuView
   ```
3. 构建项目：
   ```bash
   cargo build --release
   ```
4. 根据文档配置 WiFi 网卡驱动和 CSI 采集参数，生成配置文件。

**最小可用示例：**

```bash
# 启动基础感知服务（默认监听端口 8080）
cargo run --release -- --config config.toml

# 通过 MQTT 推送到 Home Assistant
# 在 config.toml 中设置：
# [mqtt]
# host = "homeassistant.local"
# port = 1883
# topic_prefix = "ruview"
```

对于 Apple Home 用户，RuView 在局域网内会自动被发现为 HomeKit 配件，通过家庭 App 即可直接添加并查看各房间的状态信息。

## 适用场景

- **智能家居自动化**：根据房间是否有人自动调节照明、空调和安防系统，同时通过语音助手查询各房间状态。
- **老年人与婴幼照护**：非接触式监测睡眠质量和呼吸异常，在跌倒或长时间静止时及时告警，无需佩戴任何设备。
- **隐私敏感型安防**：在办公室、酒店房间或更衣室等严禁摄像头的区域，实现可靠的入侵检测和人员活动监控。
- **医疗健康追踪**：长期记录家庭成员的呼吸和心率变化趋势，为慢性病管理和康复评估提供数据参考。

## 项目亮点

与现有的基于摄像头、红外传感器或可穿戴设备的方案相比，RuView 具有以下显著优势：

- **零硬件成本**：利用现有 WiFi 基础设施，不增加任何额外传感器或终端设备。
- **真正的穿透感知**：不受墙壁、烟雾、黑暗等视觉限制影响，感知范围覆盖整个房间甚至跨房间。
- **隐私绝对安全**：物理层面不接触任何图像或声音数据，完全消除隐私顾虑和合规风险。
- **生态兼容性极强**：一次部署即可同时接入 HomeKit、Home Assistant、Google Home 和 Alexa，省去多渠道适配工作量。
- **纯 Rust 实现**：内存安全、无 GC 停顿，适合嵌入式设备和低功耗场景长期运行。

## 相关链接

- [GitHub 仓库](https://github.com/ruvnet/RuView)
- [Home Assistant 集成文档](https://github.com/ruvnet/RuView/blob/main/docs/integrations/home-assistant.md)
- [Apple HomePod 用户指南](https://github.com/ruvnet/RuView/blob/main/docs/user-guide-apple-homepod.md)
- [Matter 暴露方案 (ADR-122)](https://github.com/ruvnet/RuView/blob/main/docs/adr/ADR-122-bfld-ruview-ha-matter-exposure.md)
