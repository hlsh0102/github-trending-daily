---
tags:
  - trending
  - article
repo: jellyfin/jellyfin
date: 2026-05-27
language: C#
stars_total: 52425
stars_today: 83
---
## 项目概述

Jellyfin 是一个完全免费、开源的媒体系统软件，旨在帮助用户构建个人媒体服务器，实现电影、电视节目、音乐、照片等媒体内容的集中管理与跨设备播放。该项目由社区驱动开发，所有代码均以 GPL-2.0 许可证发布，没有任何付费版本或隐藏功能。核心服务器（Server Backend）采用 C# 编写，提供 RESTful API 供各平台客户端调用。

该项目最初源于 Emby 3.5.2 版本的一个分支，当 Emby 转向闭源商业模式后，社区决定维护一个完全自由的替代方案。Jellyfin 的目标用户包括：希望自主管理媒体库的家庭用户、注重隐私且不愿将数据交给第三方云服务的爱好者、以及需要离线或局域网内稳定播放的小型组织。

## 核心功能

- **多格式媒体转码与直通**：支持常见的视频、音频和字幕格式，并根据客户端能力自动转码（如 H.264/H.265、AAC/AC3 等），同时支持硬件加速转码（Intel QuickSync、NVIDIA NVENC、AMD VAAPI 等）。
- **跨平台客户端支持**：官方提供 Android、iOS、iPadOS、Android TV、Apple TV、Roku、Kodi 插件以及 Web 播放器，社区还维护了 PS4/PS5、Xbox、LG/Samsung 智能电视等非官方客户端。
- **元数据自动获取**：集成 The Movie Database（TMDB）、TheTVDB、MusicBrainz、OpenSubtitles 等数据源，自动为媒体文件匹配封面、简介、演员、评分等信息。
- **用户管理与家长控制**：支持创建多个独立用户账户，为每个账户设置内容访问限制（如年龄分级、禁止特定库）、观看记录分离及播放权限。
- **DLNA 与 Chromecast 支持**：自动发现局域网的 DLNA 设备，支持将媒体推送到 Chromecast 协议设备播放。
- **集成直播电视**：配合 IPTV 或电视棒（如 HDHomeRun），提供可录制、回放的直播电视频道管理功能。

## 技术架构

Jellyfin 服务器端基于 .NET Core 框架（现为 .NET 平台）构建，采用跨平台设计，可运行于 Windows、macOS、Linux 以及 Docker 容器环境中。其核心架构遵循以下几个设计特点：

1. **插件化扩展**：服务器核心通过接口定义对外暴露，播放器、转码器、元数据获取等功能均由独立的插件系统加载。用户可以从客户端或 Web 界面浏览、安装社区开发的插件，例如自定义皮肤、增强型搜索、通知推送等。
2. **数据库持久化**：使用轻量级的 SQLite 数据库存储媒体库元数据、用户配置、播放进度等信息，同时也支持外部数据库如 PostgreSQL 和 MariaDB 进行替换。
3. **流媒体传输优化**：采用 HTTP Live Streaming（HLS）和传统 RTMP 协议进行媒体传输，支持动态段大小调整以适配不稳定的网络。对于快速跳转场景，采用关键帧对齐技术减少缓冲区延迟。
4. **微服务化的内部通信**：虽然整体架构为单体应用，但通过依赖注入（DI）模式将媒体扫描、转码、音频处理等模块解耦。配合消息队列（如基于 Redis 的 pub/sub）实现异步任务处理，例如在后台运行媒体库扫描而不阻塞用户请求。

## 安装与使用

Jellyfin 的部署方式非常灵活，以下是几种常见方式：

**Docker 部署（推荐）**：
```bash
# 创建持久化目录
mkdir -p /path/to/jellyfin/{config,cache}
# 启动容器（端口8096为Web界面，8920为HTTPS可选）
docker run -d \
  --name jellyfin \
  -p 8096:8096 \
  -v /path/to/jellyfin/config:/config \
  -v /path/to/jellyfin/cache:/cache \
  -v /path/to/media:/media \
  --restart unless-stopped \
  jellyfin/jellyfin
```

**Windows 安装**：
从 GitHub Releases 页面下载最新的安装包（.msi 或 .exe），运行后按照向导设置媒体库路径和网络端口。服务器启动后，浏览器访问 `http://localhost:8096` 即可进入初始化界面。

**Linux 手动安装**：
以 Ubuntu/Debian 为例，添加官方仓库后通过 apt 安装：
```bash
wget -O - https://repo.jellyfin.org/ubuntu/jellyfin_team.gpg.key | sudo apt-key add -
echo "deb https://repo.jellyfin.org/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/jellyfin.list
sudo apt update && sudo apt install jellyfin
sudo systemctl start jellyfin
```

首次运行需通过 Web 界面完成设置向导：选择媒体库类型（电影、剧集、音乐等）、添加媒体目录、配置语言和元数据源。完成后，即可通过任意客户端应用登录并开始播放。

## 适用场景

- **家庭媒体中心**：将散落在不同设备上的电影、电视剧和家庭录像集中管理，全家多成员通过手机、平板、电视同时观看，且各人独立记录观看进度。
- **离线旅行媒体库**：出差或旅行前，使用 Jellyfin 下载功能将内容缓存到移动设备，无需网络即可在飞机或地铁中观看，同时避免付费平台的内容合法性担忧。
- **小型教育或社区分支库**：工作室、学校或小区局域网内搭建，用于共享教学视频、培训材料或社区活动记录，可利用用户权限控制仅特定人可访问某些资源。
- **直播电视与录制服务**：配合 IPTV 源或数字电视接收器，实现电视频道的直播、回看及自动录制，替代传统电视盒子的部分功能。

## 项目亮点

- **完全自由无收费**：与 Plex（部分功能需订阅 Plex Pass）和 Emby（高级转码需购买解锁）不同，Jellyfin 的所有功能包括硬件转码、挂载云盘、多用户权限等完全免费，且不会在播放界面插入任何广告或推荐内容。
- **社区驱动生态**：超过 5000 名贡献者在 GitHub 上活跃迭代，平均每月发布 1-2 个稳定更新。用户可通过 Fider 网站直接投票决定新增功能，Matrix/Riot 聊天室和论坛提供即时技术支持，决策过程透明开放。
- **灵活的硬件转码**：支持几乎所有主流 CPU 和 GPU 硬件加速方案（包括 Intel 的 QSV、NVIDIA 的 NVENC、AMD 的 VCE 等），且可通过 Docker 绑定设备快速启用。相比之下，Plex 仅对部分硬件提供非完整支持，且需验证身份。
- **高度可定制性**：从服务器插件到客户端皮肤（如 Jellyfin-Vue 前端项目）全部开源，开发者可任意修改代码或提交 PR。普通用户也能通过配置文件调整转码参数、缓存策略等细节，在低配置设备上也能流畅运行。

## 相关链接

- [GitHub 仓库](https://github.com/jellyfin/jellyfin)
- [官方文档](https://jellyfin.org/docs/)
- [功能需求投票](https://features.jellyfin.org/)
- [Docker 镜像](https://hub.docker.com/r/jellyfin/jellyfin)
- [在线演示（Demo）](https://demo.jellyfin.org/stable)
