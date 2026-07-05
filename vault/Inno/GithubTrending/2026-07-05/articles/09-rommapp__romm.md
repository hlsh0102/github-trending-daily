---
tags:
  - trending
  - article
repo: rommapp/romm
date: 2026-07-05
language: Python
stars_total: 10279
stars_today: 398
---
## 项目概述

RomM（ROM Manager）是一个开源的、自托管的游戏 ROM 管理器与在线播放器，专为拥有大量游戏 ROM 收藏的玩家设计。它能够自动扫描你的游戏文件，从多个知名游戏数据库（如 IGDB、Screenscraper 和 MobyGames）获取元数据、封面和截图，并将你的零散 ROM 文件整理成一个干净、可搜索、可在线游玩的数字游戏库。目标用户是那些使用模拟器玩游戏、收藏了大量 ROM 文件，并希望在一个统一美观的界面中管理、浏览和直接游玩这些游戏的玩家。

## 核心功能

- **自动识别与元数据增强**：支持 400 多个游戏平台，自动识别 ROM 文件并匹配游戏名称，从 IGDB、Screenscraper、MobyGames 获取详尽的元数据（描述、发行年份、封面、截图等）。
- **自定义封面与成就系统**：集成 SteamGridDB 获取自定义艺术封面，并支持从 Retroachievements 获取游戏成就数据，让收藏界面更具个性。
- **浏览器内直接游玩**：内置 EmulatorJS 模拟器和 RuffleRS Flash 模拟器，无需额外安装模拟器软件，直接在浏览器中游玩复古游戏。
- **智能文件管理**：支持多盘游戏、DLC、修改版、汉化版、补丁和手册的解析，能够根据文件名中的标签（如 `[Hack]`, `[Patch]`）进行过滤和分类。
- **用户权限与分享**：支持创建用户，设置受限访问权限，允许与朋友共享部分游戏库，而不会暴露全部收藏。
- **跨平台集成**：提供官方应用，可集成到 Windows 的 Playnite 游戏管理器中，并支持 Android 启动器（Argosy）和定制固件（Grout）访问。

## 技术架构

RomM 采用 Python 开发，后端基于现代 Web 框架构建，前端使用响应式设计，确保在不同设备（桌面、平板、手机）上均有良好体验。项目架构围绕“扫描-存储-展示”三个核心环节设计：

- **扫描引擎**：自动检测本地或网络存储中的 ROM 文件，使用预设的命名规则和哈希值匹配游戏身份，避免手动整理。
- **元数据聚合**：通过插件化架构集成多个第三方 API（IGDB、Screenscraper、MobyGames、SteamGridDB、Retroachievements），用户可配置优先顺序和数据来源。
- **静态文件服务**：所有 ROM 文件和元数据图片按平台、字母、标签等维度组织，通过 RESTful API 高效服务前端请求。
- **内嵌模拟器**：利用浏览器兼容的 EmulatorJS（基于 RetroArch 核心）和 RuffleRS，在服务端无需模拟器环境，所有模拟计算在客户端浏览器中完成，降低部署复杂度。
- **数据存储**：使用轻量级数据库（如 SQLite 或 PostgreSQL）存储游戏元数据、用户设置、标签等信息，支持 Docker 容器化部署。

## 安装与使用

RomM 推荐通过 Docker 部署，以下是基本安装步骤：

1. **准备环境**：在服务器或 NAS 上安装 Docker 和 Docker Compose。
2. **创建目录结构**：准备存放 ROM 文件的目录（例如 `/path/to/roms`），并预留 RomM 配置文件目录（例如 `/path/to/romm-data`）。
3. **编写 docker-compose.yml**：
   ```yaml
   version: "3"
   services:
     romm:
       image: rommapp/romm:latest
       container_name: romm
       restart: unless-stopped
       ports:
         - "8080:8080"
       volumes:
         - /path/to/roms:/roms          # ROM 文件挂载
         - /path/to/romm-data:/data     # 配置与数据库
       environment:
         - ROMM_DB_ENGINE=sqlite        # 数据库类型（可选 sqlite/postgres）
         - ROMM_SECRET_KEY=your-secret  # 用于 session 签名的密钥
   ```
4. **启动服务**：执行 `docker-compose up -d`，然后通过 `http://localhost:8080` 访问 RomM。
5. **首次使用**：进入界面后，RomM 会自动扫描挂载的 ROM 目录，识别游戏并获取元数据。你也可以手动上传 ROM 文件或管理已有游戏。

**最小可用示例**：只需一个 Docker 容器，挂载包含 ROM 文件（例如 `.nes`, `.sfc`, `.gba` 等常见格式）的目录，即可在浏览器中浏览和游玩。

## 适用场景

- **个人游戏收藏管理员**：拥有大量杂乱散布在不同硬盘的 ROM 文件，希望统一整理、美化封面、方便搜索和游玩。
- **家庭或朋友共享游戏库**：在家庭服务器上部署 RomM，为不同成员设置独立账户和访问权限，让每个人只看自己的游戏。
- **复古游戏直播或演示**：直播主或教学者需要快速调取某个平台的游戏，RomM 的在线播放功能允许直接从浏览器打开游戏，无需切换模拟器窗口。
- **NAS 用户的功能扩展**：在 Synology、QNAP 等 NAS 的 Docker 环境中部署，将游戏库与现有存储系统整合，利用 NAS 的 7×24 运行特性随时可玩。

## 项目亮点

- **全栈开源且自托管**：基于 AGPL-3.0 许可发布，所有代码开源，用户完全掌控自己的游戏数据和隐私，不受第三方服务限制。
- **零配置在线游玩**：无需在用户端安装模拟器或配置运行环境，RomM 通过浏览器直接模拟运行，大幅降低使用门槛。
- **强大的元数据整合能力**：集成多个权威游戏数据库，支持自定义元数据源优先级，能自动覆盖从街机到主机的主流游戏平台。
- **活跃的社区与生态**：拥有 10,000+ 的 GitHub Stars，社区活跃，开发迭代快；提供 Playnite 集成、Android 启动器等多平台客户端扩展使用场景。

## 相关链接

- [GitHub 仓库](https://github.com/rommapp/romm)
- [官方文档](https://romm.app/docs)
- [Discord 社区](https://discord.gg/romm)
