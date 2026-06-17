---
tags:
  - trending
  - article
repo: music-assistant/server
date: 2026-06-17
language: Python
stars_total: 2623
stars_today: 157
---
## 项目概述

Music Assistant 是一款免费、开源的媒体库管理器，旨在统一管理来自不同流媒体服务和本地存储的音乐资源，并将其无缝推送到各类智能音箱设备。该项目解决了音乐爱好者面临的常见痛点：音乐资源分散在多个平台（如 Spotify、Tidal、本地 NAS），而不同品牌音箱又各自为政，缺乏统一的播放控制中心。

Music Assistant Server 是整个系统的核心组件，必须运行在始终在线的设备上，如 Raspberry Pi、NAS 或 Intel NUC 等。目标用户包括希望整合家庭音乐生态的发烧友、Home Assistant 自动化玩家，以及希望摆脱单一平台束缚的普通用户。

## 核心功能

- **多流媒体服务集成**：支持连接 Spotify、Tidal、Qobuz 等主流流媒体平台，以及本地音乐库（NAS、USB 存储等），在一个界面中完成所有音乐资源的浏览和管理。
- **广泛音箱兼容**：支持 AirPlay、Chromecast、Sonos、Squeezebox、UPnP/DLNA、蓝牙等多种协议的智能音箱，实现跨品牌设备的统一控制。
- **智能播放队列**：提供跨平台统一播放队列，可以将来自不同服务的歌曲混合排列，并支持队列编辑、随机播放、循环播放等功能。
- **高质量音频传输**：支持 FLAC、WAV、ALAC 等无损格式，并提供音频重采样和音量归一化功能，确保最佳音质体验。
- **Home Assistant 深度集成**：作为 Home Assistant 插件运行，可将音乐播放状态和设备控制暴露为传感器和服务，便于自动化场景配置。
- **多区播放与同步**：支持将多台音箱分组同步播放，实现全宅音乐同步或独立分区控制。

## 技术架构

Music Assistant Server 采用 Python 编写，基于异步事件循环架构，确保高效处理多路音频流和设备通信。其核心设计思路如下：

- **模块化驱动层**：每种流媒体服务和音箱协议都实现为独立插件，便于社区贡献和扩展。目前支持的协议包括 AirPlay 2、Google Cast、Sonos API、SqueezeBox 协议等。
- **统一抽象层**：在上层提供统一的媒体元数据模型和播放控制接口，屏蔽底层协议差异。这种设计使得开发者添加新设备或服务时，只需实现少量接口。
- **轻量数据库**：使用 SQLite 作为元数据缓存，维护播放历史、收藏夹和播放列表，无需外部数据库依赖，适合嵌入式设备运行。
- **RESTful API**：对外提供基于 HTTP 的 REST API，允许第三方客户端或自动化系统（如 Home Assistant）通过标准接口控制播放。
- **始终在线设计**：采用守护进程模式运行，支持自动检测新设备、网络恢复重连和自动更新播放队列。

## 安装与使用

### 安装步骤

推荐通过 Home Assistant 插件方式安装：

1. 确保已安装 Home Assistant Supervisor（适用于 Raspberry Pi OS、HA OS 等）。
2. 在 Home Assistant 管理界面中，通过“配置” > “加载项”进入加载项商店。
3. 添加仓库地址：`https://github.com/music-assistant/home-assistant-addon`。
4. 找到 Music Assistant Server 加载项，点击安装。
5. 根据需要配置流媒体服务凭据和设备发现选项。

最小可用示例（Docker 独立运行）：

```bash
# 拉取镜像
docker pull ghcr.io/music-assistant/server:latest

# 创建数据目录
mkdir -p ~/music_assistant/data

# 运行容器
docker run -d \
  --name music-assistant \
  -p 8095:8095 \
  -v ~/music_assistant/data:/data \
  ghcr.io/music-assistant/server:latest
```

启动后，通过浏览器访问 `http://<设备IP>:8095` 即可进入 Web 管理界面。首次使用需配置至少一个音乐源（如本地文件夹或流媒体服务），然后系统会自动发现局域网内的兼容音箱设备。

## 适用场景

- **家庭多房间音乐系统**：用户在不同房间放置不同品牌的音箱（如客厅 Sonos、卧室 HomePod、书房 Chromecast），通过 Music Assistant 统一控制播放列表和音量，并支持全宅同步播放。
- **自动化音乐场景**：结合 Home Assistant 实现自动化，例如在离家时自动停止所有播放、在特定时间播放轻柔背景音乐、或与门铃联动播放提示音。
- **离线/高质量音乐管理**：拥有大量本地无损音乐库的用户，可以使用 Music Assistant 代替 iTunes 或 WMP 进行管理，并支持多端同步播放。
- **跨平台音乐订阅整合**：同时使用 Spotify 和 Tidal 的用户，可以创建混合播放列表，避免频繁切换客户端。

## 项目亮点

- **完全开源免费**：采用 Apache-2.0 许可，不限制商业或个人使用，社区驱动积极迭代。
- **设备中立性**：不绑定任何特定品牌或生态，真正实现跨平台、跨厂商的统一控制。
- **Home Assistant 原生集成**：作为 HA 插件直接安装，与智能家居自动化深度结合，这是许多商业音乐管理工具无法提供的。
- **低资源占用**：核心服务轻量高效，可在树莓派 3B+ 等入门级设备上流畅运行。
- **丰富的社区支持**：拥有完善的官方文档（包括 Beta 文档）和活跃的用户社区，问题响应快速。

## 相关链接

- [GitHub 仓库](https://github.com/music-assistant/server)
- [官方文档](https://music-assistant.io)
- [Beta 文档](https://beta.music-assistant.io)
- [Home Assistant 插件仓库](https://github.com/music-assistant/home-assistant-addon)
