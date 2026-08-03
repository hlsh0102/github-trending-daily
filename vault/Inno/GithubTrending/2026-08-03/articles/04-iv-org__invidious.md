---
tags:
  - trending
  - article
repo: iv-org/invidious
date: 2026-08-03
language: Crystal
stars_total: 22057
stars_today: 305
---
## 项目概述

Invidious 是一个开源的 YouTube 替代前端，旨在为用户提供一个轻量、隐私友好且无广告的 YouTube 观看体验。它解决了 YouTube 官方界面中存在的若干问题：侵入式广告、数据追踪、臃肿的页面脚本以及日益严苛的访问限制。通过自建实例或使用社区托管的公共实例，用户可以在一个干净、响应迅速的界面中浏览和播放 YouTube 视频，同时无需登录 Google 账号即可完成订阅、播放列表管理等操作。该项目主要面向重视隐私的普通用户、希望在低性能设备上流畅观看视频的用户，以及希望摆脱算法推荐和个性化追踪内容的技术爱好者。

## 核心功能

- **无追踪与无广告**：所有页面和播放器均不加载 Google 的追踪脚本和广告，有效保护用户隐私。
- **无需账号即可使用**：支持不登录 YouTube 账号创建本地订阅列表、收藏视频和建立播放列表，数据仅保存在服务器本地。
- **轻量级网页播放器**：采用自定义的 HTML5 播放器，比 YouTube 官方播放器更轻量，支持视频/音频下载、速度调节、自动播放等实用选项。
- **RSS 订阅支持**：为频道和播放列表提供标准 RSS 输出，方便用户通过任何 RSS 阅读器跟踪更新。
- **多实例与高度可定制**：官方维护了多个公共实例，同时支持自托管，并允许通过实例参数调整界面语言、默认质量、主题等。
- **丰富的 API 接口**：提供完整的 JSON API，便于第三方客户端或脚本集成 Invidious 数据。

## 技术架构

Invidious 使用 Crystal 语言编写，Crystal 是一种语法类似 Ruby 但编译为原生代码的编程语言，具备极高的运行效率和低内存占用。项目采用服务端渲染（SSR）模式，后端直接与 YouTube 的内部 API 进行交互，抓取视频元数据、流地址、评论等信息，并在服务端解析后生成干净的 HTML 或 JSON 响应。这种架构使得客户端无需执行任何 JavaScript 即可完成核心浏览功能，大幅降低了页面体积和资源消耗。

项目的主要技术亮点包括：

- **三个核心组件**：`yt` 模块负责与 YouTube 后端通信，`extractor` 模块负责解析返回的数据，Web 控制器则负责路由和页面渲染。
- **无 JavaScript 依赖**：除了播放器本身和少量增强功能，Invidious 的核心界面完全依靠服务端渲染，保证了极快的首屏加载速度和良好的兼容性。
- **内置高速缓存**：对视频元数据和搜索建议进行缓存，减少对 YouTube API 的请求频率，提升响应速度。
- **原生支持 HTTP/2**：Crystal 的 HTTP 服务器天然支持 HTTP/2，确保了并发连接下的性能稳定。

## 安装与使用

Invidious 提供了多种部署方式，包括 Docker、Debian/Ubuntu 二进制包和源码编译。以下是最简单的 Docker 部署示例：

1. **使用 Docker 快速部署**：

```bash
docker run -d --name invidious \
  -p 3000:3000 \
  -v invidious-data:/invidious \
  quay.io/invidious/invidious
```

启动后，访问 `http://localhost:3000` 即可使用。

2. **使用官方公共实例**：如果不想自建，可直接访问 [instances.invidious.io](https://instances.invidious.io/) 选择一个公共实例。例如访问 `https://invidious.fdn.fr`，即可体验无需注册的 YouTube 浏览。

3. **基础使用示例**：部署完成后，你可以直接通过 URL 参数定制界面。例如访问 `https://your-instance.com/watch?v=dQw4w9WgXcQ` 播放视频，或访问 `https://your-instance.com/feed/subscriptions` 查看本地订阅的更新。

## 适用场景

- **隐私敏感型用户**：不愿意让 Google 收集观看历史和搜索记录的用户，可以完全脱离 YouTube 账号体系使用 Invidious。
- **低性能设备**：树莓派、老旧电脑或低端 Android 设备运行 Invidious 网页版比官方客户端流畅得多，因为页面脚本极少且无广告加载。
- **内容聚合与研究**：借助其 RSS 输出和 JSON API，可以方便地进行视频数据抓取、频道监控和自动化内容整理。
- **企业内部或教育网络**：在某些屏蔽 YouTube 或限制 Google 服务的网络环境中，自建 Invidious 实例可以作为访问 YouTube 内容的代理层。

## 项目亮点

Invidious 在同类开源替代前端中具备独特的优势：

- **性能极佳**：基于 Crystal 的服务端渲染架构使其在低配置 VPS 上即可稳定支撑数千并发请求，而同类 Node.js 项目通常需要更高硬件要求。
- **无 JavaScript 核心**：与部分依赖浏览器端渲染的前端项目不同，Invidious 在没有 JS 的环境下依然可以浏览和播放视频，这在安全性要求较高的环境中极为实用。
- **高度活跃的社区**：项目拥有超过 2 万 Star，社区贡献者持续跟进 YouTube 接口变化，保证了项目的长期可用性。同时，多语言翻译在 Weblate 平台进行，中文支持完备。
- **轻量级安装**：官方提供静态二进制和 Docker 镜像，安装和升级过程极为简单，且没有 Node.js 或 Python 等重型运行时的额外负担。

## 相关链接

- [GitHub 仓库](https://github.com/iv-org/invidious)
- [官方网站](https://invidious.io/)
- [公共实例列表](https://instances.invidious.io/)
- [文档与 FAQ](https://docs.invidious.io/)
