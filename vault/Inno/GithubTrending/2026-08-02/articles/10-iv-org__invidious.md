---
tags:
  - trending
  - article
repo: iv-org/invidious
date: 2026-08-02
language: Crystal
stars_total: 21668
stars_today: 435
---
## 项目概述

Invidious 是一个开源、轻量级的 YouTube 替代前端，旨在为用户提供一个不依赖 Google 官方接口、无广告、尊重隐私的 YouTube 访问方式。它由 Crystal 语言编写，采用 AGPL-3.0 许可证，目前已在 GitHub 上积累了超过 2.1 万颗星。Invidious 的核心价值在于：用户无需 JavaScript 即可浏览视频、订阅频道、观看视频，同时规避了 Google 的追踪和广告注入。它的目标用户包括注重隐私的普通用户、希望在低性能设备上流畅访问 YouTube 的用户，以及希望完全控制自身媒体消费环境的开发者。

## 核心功能

- **无 JavaScript 播放**：默认情况下列表、播放、搜索等功能均不依赖 JavaScript，兼容纯 HTML 浏览器，提升了可访问性和安全性。
- **内置订阅与频道管理**：用户可以在 Invidious 上创建本地订阅，跟踪频道更新，而无需将数据发送给 Google。
- **隐私保护**：移除了 YouTube 的追踪参数、Cookie 和指纹识别脚本，访问记录保存在服务端而非浏览器中。
- **去广告与赞助内容过滤**：默认屏蔽视频内广告及赞助片段，也可以选择手动启用赞助商片段跳过。
- **API 支持**：提供完整的 REST API，可供第三方应用集成，实现自定义播放器、下载工具或数据分析。
- **多实例与自定义**：支持用户自行部署，并允许调整主题、默认播放速度、字幕语言等偏好。

## 技术架构

Invidious 基于 Crystal 语言构建，利用了其高性能和低资源占用特性。服务端采用 MVC 架构，核心路由使用 Kemal 框架（一个类似 Sinatra 的 Web 微框架）。它直接与 YouTube 的匿名内部 API 交互，获取视频元数据、流地址、评论等信息，并在服务端进行解析和缓存（默认使用 SQLite，可配置为 PostgreSQL）。前端渲染使用纯 HTML 和 CSS，配合少量可选 JavaScript 实现动态交互，但这部分完全可以禁用。这种设计使得 Invidious 能在极低配置的 VPS 或树莓派上运行，同时保证了响应速度。项目采用模块化设计，将网络请求、解析、缓存、API 层分离，便于扩展和测试。

## 安装与使用

Invidious 提供了多种部署方式，最推荐的是 Docker Compose。以下是一个最小化部署示例：

```bash
git clone https://github.com/iv-org/invidious
cd invidious
cp config/config.example.yml config/config.yml
# 编辑 config.yml，设置数据库连接等参数
docker-compose up -d
```

启动后，在浏览器访问 `http://localhost:3000` 即可使用。如果你不想自行部署，也可以直接使用社区维护的公共实例列表（见相关链接），无需安装即可体验。对于开发者，可以通过 API 快速集成：

```bash
curl "https://your-instance.com/api/v1/search?q=crystal+language"
```

该请求会返回 JSON 格式的视频搜索结果。

## 适用场景

- **隐私敏感用户**：希望避免 Google 数据收集，在观看视频时不被追踪。
- **嵌入式设备或低性能平台**：在树莓派、老旧电脑或路由器上运行，提供流畅的 YouTube 访问能力。
- **内容归档与自托管**：配合 youtube-dl 等工具，可以将 Invidious 作为下载、转码、归档的中间层。
- **开发者工具**：利用其 API 构建自定义播放器、在线学习平台或视频聚合应用。

## 项目亮点

与现有 YouTube 替代方案（如 Piped、FreeTube）相比，Invidious 的差异化优势体现在：

- **成熟度与活跃度**：项目维护多年，社区庞大，更新频繁，支持大量 YouTube 功能（如评论区、播放列表、直播）。
- **轻量化**：服务端资源占用极低，单实例可服务数百并发用户，且对客户端要求极低。
- **透明度高**：无任何前端二进制闭源组件，所有代码公开可审计，部署者可完全掌控数据流。
- **灵活性**：既可作为个人自托管工具，也可作为公共服务，并提供细粒度的配置选项（如禁用注册、限制 API 调用）。

## 相关链接

- [GitHub 仓库](https://github.com/iv-org/invidious)
- [官方网站](https://invidious.io/)
- [公共实例列表](https://instances.invidious.io/)
- [文档与 FAQ](https://docs.invidious.io/)
