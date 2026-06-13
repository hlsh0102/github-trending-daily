---
tags:
  - trending
  - article
repo: music-assistant/server
date: 2026-06-13
language: Python
stars_total: 1842
stars_today: 20
---
## 项目概述

Music Assistant 是一款免费、开源的媒体库管理工具。它的核心使命是将用户分散在多个流媒体服务中的音乐资源，以及本地或网络上的智能音箱设备统一管理起来。项目的核心是一个名为 `music-assistant-server` 的 Python 后端服务，它相当于整个系统的“心脏”，必须运行在始终开机的设备上（如树莓派、NAS、Intel NUC 等）。对于追求家庭自动化、且希望将音乐播放深度集成到智能家居场景中的用户来说，它提供了一种轻量、灵活的解决方案。

该项目的目标用户包括：家庭自动化爱好者（特别是 Home Assistant 用户）、拥有多个流媒体平台订阅但希望统一管理的用户、希望摆脱单一品牌音箱生态束缚的用户，以及对音乐文件组织和播放有自托管需求的用户。

## 核心功能

- **多平台音乐源整合**：支持连接多个主流流媒体服务（如 Spotify、Tidal、Qobuz 等），同时支持本地音乐文件库。用户无需在多个应用间切换即可访问所有音乐。
- **设备兼容性广泛**：支持众多品牌的智能音箱、音频播放器和网络播放器（如 Sonos, Google Cast, AirPlay, MPD 等）。它能将音乐无缝推送到不同品牌的设备上。
- **统一的播放控制**：提供一个中心化的界面，允许用户跨不同平台和设备进行播放控制，包括播放、暂停、下一曲、音量和播放队列管理。
- **深度 Home Assistant 集成**：虽然可以独立运行，但项目从设计上就与 Home Assistant 紧密配合。它可以作为一个 Home Assistant 插件（Add-on）安装，实现自动化播放场景（例如，当您回家时自动播放音乐）。
- **强大的媒体管理与库功能**：自动抓取和管理音乐元数据（如专辑封面、艺术家信息），并提供搜索和浏览功能，让您的音乐库井然有序。
- **开源与自托管**：代码完全开源，用户可以将服务器部署在自己的硬件上，完全掌控数据隐私与服务可用性。

## 技术架构

Music Assistant 采用客户端-服务器（Client-Server）架构，服务器端是整个系统的基础。

- **后端技术栈**：项目主要使用 **Python** 编写，得益于 Python 丰富的生态，能够方便地集成各种流媒体服务 API、网络协议和硬件设备驱动。
- **核心特性**：服务器运行一个中央调度引擎，负责管理所有连接的音乐源和播放器。它使用统一的内部模型来表示音乐曲目、艺术家、专辑以及播放队列，对外屏蔽了不同服务商之间的接口差异。
- **与 Home Assistant 的集成**：项目专门提供了一个 Home Assistant 插件。该插件通过 Home Assistant 的 Supervisor 系统与服务进行交互，使得 Music Assistant 能够利用 Home Assistant 的事件、状态和自动化引擎。从架构上看，Music Assistant 作为一个独立的守护进程（Daemon）运行，通过 WebSocket 等协议与 Home Assistant 通信，确保了主系统的稳定性不会因音乐服务故障而受损。
- **可扩展性**：由于采用开源组件和模块化设计，开发者可以方便地通过添加 Provider 来支持新的流媒体服务或音频设备。其播放队列和音频流处理环节也具有良好的抽象层，便于未来扩展更多音频处理功能。

## 安装与使用

**基础环境**：您需要一台始终开机的设备（如树莓派 4/5、NAS、Intel NUC 或旧 PC），并为其安装 Linux 或基于 Linux 的系统。

**推荐安装方式（Home Assistant 插件）**：
1.  确保您已经安装了 Home Assistant 操作系统或 Supervisor。
2.  在 Home Assistant 界面的“插件商店（Add-on Store）”中，点击右上角菜单，选择“仓库（Repositories）”。
3.  添加以下仓库地址：`https://github.com/music-assistant/home-assistant-addon`。
4.  返回插件商店，找到 “Music Assistant Server”，点击安装。
5.  安装完成后，启动插件，并通过其 Web UI 进行配置（添加流媒体账户、搜索播放器等）。

**最小可用示例（独立运行）**：
如果您不使用 Home Assistant，也可以直接运行 Docker 镜像：
```bash
docker run -d \
  --name music-assistant \
  --restart always \
  -v /path/to/config:/config \
  -v /path/to/music:/media \
  --network host \
  musicassistant/music-assistant:latest
```
启动后，通过浏览器访问 `http://your-server-ip:8095` 即可进入配置向导。

## 适用场景

1.  **家庭自动化音乐播放**：您希望客厅的 Sonos 音箱在检测到有人时自动播放 Spotify 日推；或当儿童卧室的智能灯关闭时，音箱自动播放轻柔的摇篮曲。通过 Home Assistant 集成，这些场景可以轻松实现。
2.  **多平台音乐账户整合**：您有 Spotify 的年度订阅，也偶尔使用 Tidal 听高音质。您希望在一个统一的界面中浏览、搜索和播放来自两个平台的音乐，而不必来回切换 App。
3.  **跨品牌音箱统一管理**：您家中同时拥有 Google Nest 音箱、一台 AirPlay 音箱和一台支持 DLNA 的功放。您希望将它们组成同一个播放组，或者在不同房间之间轻松切换播放目标。
4.  **私有媒体库管理**：您拥有大量高品质的本地音乐文件（如 FLAC 格式），并希望将它们与在线流媒体服务一起，通过手机或平板进行统一浏览和播放。

## 项目亮点

- **以自动化为基因**：与 Home Assistant 深度集成是其最突出的优势。相比其他独立媒体服务器（如 Plex、Jellyfin），它更适合智能家居场景，可以轻松触发基于事件（如传感器、时间、状态）的音乐播放。
- **设备兼容性广泛**：不仅支持 AirPlay、Google Cast 等主流协议，还专门支持 Sonos 等生态封闭的设备，覆盖了市面上大多数智能音频设备。
- **对用户友好**：代码和文档质量高，提供 Docker 和 Home Assistant 插件等多种安装方式，降低了部署门槛。同时，其 Web UI 设计得相对直观，非技术用户也能完成基础配置。
- **开源与社区驱动**：采用 Apache 2.0 许可证，社区活跃，能够快速响应用户需求和新设备支持。

## 相关链接

- [GitHub 仓库](https://github.com/music-assistant/server)
- [官网与文档](https://music-assistant.io)
- [Beta 版本文档](https://beta.music-assistant.io)
