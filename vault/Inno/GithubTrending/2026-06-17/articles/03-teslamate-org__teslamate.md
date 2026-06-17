---
tags:
  - trending
  - article
repo: teslamate-org/teslamate
date: 2026-06-17
language: Elixir
stars_total: 8449
stars_today: 215
---
## 项目概述

TeslaMate 是一个开源的、自托管的特斯拉车辆数据记录器。它能够持续从您的 Tesla 车辆获取行驶、充电、能耗等数据，并将这些信息存储到本地数据库中，最终通过功能强大的可视化界面（Grafana）呈现给用户。该项目主要面向希望深度了解自己特斯拉车辆使用情况的车主，特别是注重隐私、希望将数据保留在自己手中的用户。与特斯拉官方 App 提供的有限数据不同，TeslaMate 允许您以任意粒度查看历史数据，并搭建完全属于您自己的数据分析体系。

## 核心功能

- **全量数据自动记录**：通过连接您的 Tesla 账户或车辆 API，自动记录每次行程、充电会话、停车位置、电池状态等关键数据。
- **Grafana 可视化仪表盘**：内置多套 Grafana 仪表盘，展示行驶里程、能耗效率、充电成本、电池健康度、足迹地图等丰富图表。
- **MQTT 实时数据推送**：将车辆实时状态持续发布到本地 MQTT 代理，方便对接 Home Assistant、Node-RED 等智能家居或自动化平台。
- **多车辆支持**：可同时监控多台 Tesla 车辆，每辆车的数据独立管理。
- **充电成本计算**：支持配置电价和充电损耗，自动计算每次及累计的充电费用。
- **数据导出与历史分析**：所有数据存储在 PostgreSQL 数据库中，用户可随时导出或通过 SQL 进行自定义分析。

## 技术架构

TeslaMate 采用 Elixir 语言编写，基于高并发、容错性优秀的 Erlang/OTP 平台。其核心架构围绕两个关键组件构建：一个负责与 Tesla 服务器通信、获取数据并存入 PostgreSQL 数据库的后端服务；另一个是可选但强烈推荐的 Grafana 可视化层。PostgreSQL 负责持久化所有历史数据，提供了强大的查询能力。MQTT 则作为实时数据流的一条轻量化通道，将车辆状态变化推送给其他系统。整个项目以 Docker 容器化方式交付，使用 `docker-compose` 即可一键部署，大幅降低了自托管的门槛。这种设计使得 TeslaMate 在长期运行中保持稳定，并易于扩展或与其他自托管服务集成。

## 安装与使用

安装 TeslaMate 需要您具备基本的 Docker 和 Docker Compose 知识。以下是快速部署步骤：

1. **准备环境**：确保已安装 Docker 和 Docker Compose（V2 及以上）。
2. **获取配置**：下载 TeslaMate 的 `docker-compose.yml` 文件到您的服务器目录。
   ```bash
   mkdir teslamate && cd teslamate
   curl -O https://raw.githubusercontent.com/teslamate-org/teslamate/main/docker-compose.yml
   ```
3. **修改配置**：编辑 `docker-compose.yml`，根据您的需求设置 `MQTT_USERNAME`、`MQTT_PASSWORD`、`DB_PASS` 等环境变量。同时需要获取一个 Tesla API 访问令牌，编辑 `TESLAMATE_TOKEN` 变量。
4. **启动服务**：
   ```bash
   docker compose up -d
   ```
5. **登录 Grafana**：启动成功后，访问 `http://localhost:3000`（默认端口），使用初始管理员账户（admin/teslamate）登录，即可看到预置的 Tesla 仪表盘。
6. **开始监控**：安装完成后，车辆数据便会自动开始采集。您可以在 Grafana 中查看实时数据，或通过 MQTT 客户端订阅特定主题（例如 `teslamate/cars/1/state`）获取实时状态。

## 适用场景

- **私家车主深度分析**：希望详细了解自己驾驶习惯、车辆能耗与性能，并长期追踪电池健康度的车主。
- **车队或共享车辆管理**：管理者需要同时监控多辆特斯拉的运行状态、维护计划和充电成本。
- **智能家居集成**：将车辆数据（如位置、剩余电量、充电状态）接入 Home Assistant，实现自动化场景（例如离家自动开启充电）。
- **开发者/数据爱好者**：对车辆数据有自定义分析需求，希望利用 PostgreSQL 和 MQTT 进行二次开发或数据对接。

## 项目亮点

- **完全自托管，数据私密**：所有车辆数据存储在本地的 PostgreSQL 数据库中，不经过任何第三方云服务，完全由用户掌控。
- **可视化能力强大**：基于 Grafana 的企业级仪表盘，开箱即用，同时也支持用户自由编辑和创建自定义图表。
- **MQTT 优先的实时集成**：通过 MQTT 协议将数据实时推送给其他系统，比单纯依靠 API 轮询更高效、更易扩展。
- **活跃的社区与严格的安全维护**：项目拥有超过 8,400 颗 GitHub Stars，维护者定期发布更新。官方反复强调仅使用官方版本，防止恶意 fork 带来的安全风险。

## 相关链接

- [GitHub 仓库](https://github.com/teslamate-org/teslamate)
- [官方文档](https://docs.teslamate.org)
