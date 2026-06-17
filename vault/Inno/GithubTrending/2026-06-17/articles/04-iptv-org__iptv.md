---
tags:
  - trending
  - article
repo: iptv-org/iptv
date: 2026-06-17
language: TypeScript
stars_total: 124471
stars_today: 1197
---
## 项目概述

IPTV 是一个公开收集全球可用的 IPTV 电视频道列表的开源项目。它解决了传统电视观看受限、频道资源分散、获取成本高的问题，为全球用户提供了一个免费、开放、可编程的互联网电视频道数据源。目标用户包括电视爱好者、开发者、媒体研究人员以及任何希望通过网络观看世界各地公开直播频道的用户。目前该项目在 GitHub 上拥有超过 12.4 万颗星，是 IPTV 领域最受欢迎的开源项目之一。

## 核心功能

- **全球频道聚合**：收录来自世界各地的公开 IPTV 频道，涵盖新闻、体育、娱乐、教育等多种类型
- **标准化播放列表**：提供 `.m3u` 格式的播放列表文件，可直接在支持直播流的视频播放器中使用
- **电子节目指南支持**：提供 EPG（电子节目指南）数据，方便用户查看频道节目时间表
- **多维度分类**：按国家、地区、语言、内容类型对频道进行组织，便于快速筛选
- **开放 API**：提供 RESTful API，允许开发者以编程方式查询和获取频道数据
- **持续自动更新**：通过 GitHub Actions 自动维护频道列表的可用性，定期验证链接有效性

## 技术架构

项目基于 TypeScript 开发，采用模块化的数据管理架构。核心数据存储于独立的 `iptv-org/database` 仓库，通过结构化数据模型管理每个频道的名称、国家、语言、流媒体地址等信息。播放列表生成由自动化脚本完成，每周通过 GitHub Actions 触发更新流程，验证所有流媒体链接的有效性并生成最新的 `.m3u` 文件。EPG 功能由独立的 `iptv-org/epg` 仓库实现，利用 XMLTV 格式提供节目时间表。整个系统采用仓库分离的设计思想，将数据、API、EPG 等不同功能模块交由独立的子仓库管理，既降低了耦合度，也便于社区分工协作和贡献维护。

## 安装与使用

**基本使用步骤**：

1. 获取播放列表链接：
   - 主播放列表：`https://iptv-org.github.io/iptv/index.m3u`
   - 按国家分类的列表见 `PLAYLISTS.md` 文件

2. 在视频播放器中打开：
   - 推荐播放器：VLC、Kodi、PotPlayer、IPTV Smarters 等支持直播流的软件
   - 以 VLC 为例：媒体 → 打开网络串流 → 粘贴播放列表链接 → 播放

**最小可用示例**（使用 curl 和 VLC）：

```bash
# 下载主播放列表
curl -O https://iptv-org.github.io/iptv/index.m3u

# 在 VLC 中打开
vlc index.m3u
```

**API 调用示例**：

```bash
# 获取所有频道列表（API 文档见 iptv-org/api 仓库）
curl https://iptv-org.github.io/api/v1/channels.json
```

## 适用场景

- **家庭娱乐**：通过智能电视或机顶盒安装 IPTV 播放器，免费观看全球公共频道，替代有线电视
- **媒体研究**：记者、学者或媒体分析师收集不同国家的新闻频道素材，用于跨文化研究或信息监测
- **开发测试**：开发者利用公开的电视数据流，测试视频播放器、流媒体处理工具或网络直播功能
- **旅行者与侨民**：身在海外的用户通过观看本国电视频道，保持与家乡的文化联系和新闻获取

## 项目亮点

- **完全免费开放**：采用 Unlicense 许可证，所有数据均可自由使用、修改和分发
- **全球覆盖范围广**：包含超过 8000 个频道，覆盖 190 多个国家和地区，是最大规模的 IPTV 公共频道集合之一
- **社区驱动维护**：由数千名贡献者参与数据更新和错误报告，频道列表始终保持活跃
- **自动化质量保障**：GitHub Actions 自动验证频道可用性，淘汰失效链接，保证播放列表的可靠性
- **模块化生态**：项目不只是一个播放列表，而是一个包含数据库、API、EPG 的完整生态系统，满足不同层次的使用需求

## 相关链接

- [GitHub 仓库](https://github.com/iptv-org/iptv)
- [主播放列表](https://iptv-org.github.io/iptv/index.m3u)
- [频道数据库](https://github.com/iptv-org/database)
- [EPG 仓库](https://github.com/iptv-org/epg)
- [API 仓库](https://github.com/iptv-org/api)
- [推荐播放器列表](https://github.com/iptv-org/awesome-iptv#apps)
