---
tags:
  - trending
  - article
repo: home-assistant/core
date: 2026-07-13
language: Python
stars_total: 89176
stars_today: 400
---
## 项目概述

Home Assistant 是一个开源的本地化家庭自动化平台，由全球范围内的技术爱好者与 DIY 玩家社区共同驱动。项目核心目标在于让用户完全掌控自己的智能家居设备，将数据与操作保留在本地网络中，从而最大化隐私保护。Home Assistant 非常适合在 Raspberry Pi 或本地服务器上运行，为家庭或小型办公环境提供一套统一、可编程的智能设备管理中枢。无论是从零开始搭建全屋自动化，还是集成已有各种品牌的智能设备，Home Assistant 都能提供稳定且高度可定制的解决方案。

## 核心功能

- **本地控制与隐私优先**：所有自动化逻辑和设备状态数据默认存储于本地，无需依赖云端服务，有效杜绝数据泄露风险。
- **广泛设备兼容性**：支持超过 2000 种不同品牌和协议的智能设备，包括灯光、传感器、开关、温控器、摄像头、门锁等，覆盖主流 IoT 生态。
- **强大的自动化引擎**：用户可通过图形化界面或 YAML 配置文件创建复杂的规则、条件和动作，实现设备间的智能联动，例如“当室外光照低于阈值且家中无人时关闭所有窗帘”。
- **丰富的第三方集成**：提供大量官方与社区维护的组件，可对接语音助手（Amazon Alexa、Google Assistant）、媒体播放器、日历、天气服务等外部系统。
- **深度可扩展性**：采用模块化架构，开发者可自定义组件、主题与前端面板，满足个性化或进阶需求。
- **实时监控与可视化仪表板**：内置仪表板编辑器，支持拖拽配置，可实时查看设备状态、历史趋势图表，并支持移动端响应式访问。

## 技术架构

Home Assistant 使用 **Python** 语言开发，核心采用异步事件驱动模型（基于 asyncio），保证高并发下设备状态同步的低延迟。系统整体分为三个层次：

- **核心层**：负责设备状态管理、自动化规则引擎、服务调用与持久化存储（默认使用 SQLite，也可切换至 PostgreSQL 或 MySQL）。
- **集成层**：通过标准化接口（Entity、Platform、Service）与各类设备协议（MQTT、Zigbee、Z-Wave、Wi-Fi、Bluetooth）交互，各集成模块彼此隔离，便于独立开发与维护。
- **前端层**：基于 Polymer Web Components 构建的前端界面，以 WebSocket 与后端实时通信，提供流畅的仪表板体验。同时提供 REST API 和 WebSocket API 供外部程序调用。

设计上强调松耦合与可替换性，核心与集成的代码仓库分离（`home-assistant/core` 提供核心框架，`home-assistant/integrations` 负责具体设备驱动），用户可选择性安装所需集成，避免资源浪费。

## 安装与使用

**基本安装步骤（以 Raspberry Pi 为例，推荐使用 Home Assistant OS）：**

1. 下载 Home Assistant OS 镜像并写入 SD 卡（可使用 Raspberry Pi Imager 或 BalenaEtcher）。
2. 将 SD 卡插入 Raspberry Pi，连接网线并启动。
3. 在浏览器中访问 `http://homeassistant.local:8123`（或根据路由器分配的 IP 访问）。
4. 完成初始向导设置：创建账户、选择所在时区与位置（用于日出日落自动化）。
5. 进入主界面后，通过“配置”->“设备与服务”发现并添加你的智能设备。

**最小可用示例（通过配置文件创建自动化）**：
在 `configuration.yaml` 文件中添加如下内容，实现“当运动传感器检测到有人时，打开灯”：

```yaml
automation:
  - alias: 'Turn on light when motion detected'
    trigger:
      platform: state
      entity_id: binary_sensor.motion_sensor
      to: 'on'
    action:
      service: light.turn_on
      target:
        entity_id: light.office_light
```

保存文件后，重启 Home Assistant 即可生效。此外，图形化的自动化编辑器可在“配置”->“自动化与场景”中使用。

## 适用场景

- **全屋智能照明与环境控制**：根据时间、室内外光照、人在与否自动调节灯光、窗帘与温控系统，降低能耗并提升舒适度。
- **安全监控与告警**：集成门窗传感器、摄像头、烟雾探测器，在异常触发时发送手机通知或联动警笛，实现本地化的安防方案。
- **语音控制与场景联动**：将 Home Assistant 与 Alexa/Google Assistant 关联，通过语音命令执行“离家模式”（关闭所有电器、安防布防）、“影院模式”（调暗灯光、关闭窗帘）等场景。
- **能源管理**：监测电表、太阳能板与充电桩的实时功率，通过自动化在电费低谷时段为电动汽车充电，并生成可视化能耗报表。

## 项目亮点

- **本地优先理念**：不同于多数云依赖的智能家居平台，Home Assistant 所有核心功能完全离线可用，即使断网也不影响自动化执行，从根本上解决隐私与可靠性问题。
- **零锁定效应**：开源（Apache-2.0 许可）且数据格式公开，用户可随时迁移到其他系统，无需担心品牌绑定。
- **活跃的社区生态**：全球超过 80000 名社区贡献者，提供海量设备支持与预置蓝图（Blueprint），初学者也能快速上手。
- **跨平台支持**：除了 Raspberry Pi，还能在 Docker、NAS、Windows 虚拟机等任意 x86/ARM 设备上运行，部署灵活。
- **持续的前沿更新**：项目维护极为活跃，平均每周发布一个新版本，及时适配新的协议标准与设备。

## 相关链接

- [GitHub 仓库](https://github.com/home-assistant/core)
- [官方网站](https://home-assistant.io)
- [在线演示](https://demo.home-assistant.io)
- [安装指南](https://home-assistant.io/getting-started/)
- [开发者文档](https://developers.home-assistant.io)
