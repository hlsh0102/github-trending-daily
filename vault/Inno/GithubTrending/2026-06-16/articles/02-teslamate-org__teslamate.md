---
tags:
  - trending
  - article
repo: teslamate-org/teslamate
date: 2026-06-16
language: Elixir
stars_total: 8309
stars_today: 33
---
## 项目概述

TeslaMate 是一款专为 Tesla 车主设计的自托管数据记录工具。它能够自动从您的 Tesla 车辆获取详细的行车数据，并将其存储在本地数据库中，再通过 Grafana 可视化面板呈现丰富的统计图表。这个项目解决的核心问题是：让车主完全掌控自己的车辆数据，不受官方服务器限制，实现深度数据分析与长期记录。目标用户是希望深入了解自己车辆状态、能耗模式、充电习惯，并对数据隐私有较高要求的 Tesla 车主与技术爱好者。

## 核心功能

- 自动数据记录：通过 Tesla API 定期获取车辆状态，包括位置、速度、电池水平、温度、车门状态等信息。
- 行程与充电追踪：自动识别每次行程的起点、终点、里程、能耗和充电会话数据，支持导出 CSV 格式。
- Grafana 可视化：提供预设的仪表板，可直观展示行程历史、能耗趋势、充电统计、驾驶效率等指标。
- 自定义告警与通知：通过集成的 MQTT 消息系统，可触发自定义规则并推送通知到手机或智能家居平台。
- 多车辆支持：一个实例可同时监控多辆 Tesla，数据在 Grafana 中以不同颜色区分显示。
- 本地数据存储：所有数据保存在你自有的 PostgreSQL 数据库中，无第三方访问，保障隐私安全。

## 技术架构

TeslaMate 采用 Elixir 语言编写，利用其高并发与容错特性，确保长时间稳定运行。核心组件包括：

- Elixir/Phoenix 应用：负责后台调度任务，周期调用 Tesla API 并处理数据。
- PostgreSQL 数据库：存储所有原始数据与聚合统计，支持复杂查询与历史回溯。
- Grafana：作为前端可视化层，连接 PostgreSQL 数据源，提供丰富的图表和仪表板。
- MQTT 代理：将车辆实时数据发布到本地 MQTT 主题，便于集成其他自动化系统（如 Home Assistant）。  
  整体架构采用 Docker Compose 部署，所有组件在容器中运行，易于维护和迁移。数据流从 Tesla API 流入，经 Elixir 处理后存储到 PostgreSQL，同时推送到 MQTT；Grafana 从数据库拉取数据渲染图表。

## 安装与使用

**前提条件**：Docker 与 Docker Compose。

1. 克隆仓库：
   ```bash
   git clone https://github.com/teslamate-org/teslamate.git
   cd teslamate
   ```
2. 复制环境变量文件：
   ```bash
   cp docker-compose.yml.example docker-compose.yml
   ```
3. 编辑 `docker-compose.yml` 设置 `TESLA_API_TOKEN`（通过 Tesla API 获取）及数据库密码。
4. 启动服务：
   ```bash
   docker-compose up -d
   ```
5. 访问 `http://localhost:4000` 查看 TeslaMate Web 管理界面；访问 `http://localhost:3000` 查看 Grafana 仪表板（默认登录凭据 `admin/admin`）。

**最小可用示例**：  
只需完成上述步骤并正确配置 API 令牌，即可自动开始记录数据。如果车辆处于停车状态，系统会按默认间隔（如每小时）采集静态数据；行驶时会实时更新位置与能耗。无需手动干预，数据即自动填充至 Grafana。

## 适用场景

- **车况长期监控**：定期检查电池健康度、充电习惯、能耗波动，发现异常行为（如待机耗电过高）。
- **行程分析**：回顾每次出行的里程、平均速度、能量消耗，对比不同驾驶模式或路线的效率。
- **家庭多车管理**：用同一个实例监控全家多辆 Tesla，统一在仪表板中对比使用情况。
- **自动化联动**：通过 MQTT 将车辆状态集成到 Home Assistant，实现离家自动充电、到站自动开空调等场景。

## 项目亮点

- **完全自托管**：所有数据存储于本地，不依赖任何第三方云服务，隐私可控。
- **开源免费**：代码遵循 AGPL-3.0 许可证，社区活跃，长期维护。
- **深度可视化**：Grafana 提供预设仪表板，并允许用户自定义指标与图表，满足不同分析需求。
- **高扩展性**：MQTT 接口让数据可以自由接入其他系统，生态丰富。
- **低资源占用**：Elixir 运行时高效，典型部署仅需 1GB 内存和少量磁盘空间。

## 相关链接

- [GitHub 仓库](https://github.com/teslamate-org/teslamate)
- [官方文档](https://docs.teslamate.org)
- [Grafana 仪表板预览](https://grafana.com/grafana/dashboards/10022)
