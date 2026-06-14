---
tags:
  - trending
  - article
repo: music-assistant/server
date: 2026-06-14
language: Python
stars_total: 2045
stars_today: 270
---
## 项目概述

Music Assistant 是一款免费、开源的媒体库管理器，旨在帮助用户统一管理和播放来自不同流媒体服务及本地设备的音乐内容。它的核心是服务器端组件，必须运行在始终在线的设备上（如 Raspberry Pi、NAS 或 Intel NUC 等）。该项目解决了音乐爱好者常见的痛点：多个流媒体平台账号切换繁琐、不同品牌的智能音箱互不兼容、本地音乐与在线音乐难以统一管理。目标用户包括 Home Assistant 用户、音乐发烧友以及希望构建自动化家庭音乐系统的技术爱好者。

## 核心功能

- **多流媒体服务集成**：支持主流的流媒体音乐平台（如 Spotify、Tidal、Qobuz 等），将不同平台的内容统一到一个界面中管理。
- **广泛设备兼容**：连接并控制多种品牌的智能音箱、流媒体播放器和音频设备，包括 Sonos、Google Cast 设备、AirPlay 兼容设备、DLNA 接收器等。
- **智能播放队列**：提供智能队列功能，可自动混搭不同来源的曲目，并支持基于上下文的播放建议。
- **与 Home Assistant 深度集成**：可作为 Home Assistant 的插件运行，方便通过自动化规则控制音乐播放，例如根据时间、传感器或场景触发播放。
- **元数据管理与收藏**：自动整理音乐库的元数据，支持创建和管理收藏列表、播放列表。
- **多房间同步播放**：支持在不同房间的多个设备上同步播放同一首音乐，实现全屋音频覆盖。

## 技术架构

Music Assistant 采用 Python 编写，核心架构基于异步编程模式（asyncio），确保在高并发场景下（如同时播放流媒体、设备发现、数据传输）保持高效稳定。项目采用模块化设计，主要分为以下层次：

- **传输层**：负责处理不同音频协议的通信，包括 HTTP/HTTPS 流媒体传输、AirPlay 协议、Google Cast 协议等，每个协议有独立的适配器。
- **服务层**：集成各流媒体平台的 API 接口，封装认证、搜索、播放列表管理等功能，统一数据模型。
- **设备管理层**：维护已发现设备的清单和状态，通过 UPnP、mDNS 等协议自动发现网络中的兼容音频设备，并进行生命周期管理。
- **核心引擎**：协调上述模块，处理用户播放指令、队列管理、多房间同步逻辑。
- **用户界面层**：提供 Web UI，可通过浏览器访问；同时暴露 REST API 和 WebSocket 接口，供 Home Assistant 前端或其他第三方客户端调用。

项目的持久化存储采用 SQLite 数据库，兼顾轻量和可靠性，适合在资源受限的嵌入式设备上运行。此外，Music Assistant 通过插件架构支持扩展，未来可轻松添加新的流媒体服务或设备协议。

## 安装与使用

### 安装步骤

1. **推荐方式**：通过 Home Assistant 插件安装
   - 确保 Home Assistant 已安装 Supervisor。
   - 在 Home Assistant 的插件市场中添加 `https://github.com/music-assistant/home-assistant-addon` 仓库。
   - 搜索并安装 "Music Assistant Server" 插件。
   - 配置端口映射（默认使用 8095 端口）并启动。

2. **独立安装**：使用 Docker
   ```bash
   docker run -d \
     --name music-assistant \
     --restart unless-stopped \
     -v /path/to/config:/config \
     -v /path/to/music:/music \
     -p 8095:8095 \
     ghcr.io/music-assistant/server:latest
   ```

3. **手动安装**：需要 Python 3.9+ 环境
   ```bash
   git clone https://github.com/music-assistant/server.git
   cd server
   pip install -r requirements.txt
   python music_assistant/server.py
   ```

### 最小可用示例

安装启动后，通过浏览器访问 `http://<设备IP>:8095`，进入 Web 界面完成初始配置：
1. 添加流媒体服务账号（如 Spotify）。
2. 等待设备自动扫描发现网络中的兼容音箱。
3. 创建播放列表或直接搜索音乐并播放。

## 适用场景

- **智能家居音乐自动化**：与 Home Assistant 联动，设置自动化规则，例如“当早晨闹钟响起时，在卧室音箱播放轻松的音乐”或“当传感器检测到有人进入客厅时，自动继续上次未播完的播放列表”。
- **多平台音乐统一管理**：用户同时订阅了 Spotify 和 Tidal，但需要在同一界面中搜索、收藏和管理来自两个平台的音乐，无需频繁切换应用。
- **全屋多房间同步播放**：家中有多个 Sonos 音箱和一台 AirPlay 兼容的电视，希望在所有设备上同步播放同一首音乐，营造派对氛围。
- **本地音乐和在线音乐混合播放**：用户拥有大量本地无损音乐文件（如 FLAC），同时也使用流媒体服务，希望在同一个队列中混合播放本地和在线曲目。

## 项目亮点

- **开源且免费**：完全开源（Apache-2.0 许可），无任何隐藏收费或限制，社区活跃，用户可自由贡献代码或提出功能建议。
- **与 Home Assistant 原生契合**：作为 Home Assistant 官方认可的插件，自动继承其自动化和场景能力，无需复杂的手动集成。
- **广泛的硬件兼容性**：不仅支持常见品牌（Sonos、Google Cast），还覆盖 DLNA、AirPlay 等开放标准，甚至可自定义添加新设备。
- **轻量高效**：核心 Python 代码优化良好，内存占用在树莓派 4B 上通常低于 150MB，适合嵌入式设备长期运行。

## 相关链接

- [GitHub 仓库](https://github.com/music-assistant/server)
- [官方文档](https://music-assistant.io)
- [测试版文档](https://beta.music-assistant.io)
- [功能请求与讨论](https://github.com/music-assistant/support/discussions/categories/feature-requests-and-ideas)
- [问题跟踪](https://github.com/music-assistant/support/issues)
