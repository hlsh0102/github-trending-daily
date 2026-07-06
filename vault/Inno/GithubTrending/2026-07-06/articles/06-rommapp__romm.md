---
tags:
  - trending
  - article
repo: rommapp/romm
date: 2026-07-06
language: Python
stars_total: 10650
stars_today: 410
---
## 项目概述

RomM（ROM Manager）是一款自托管的 ROM 管理与在线游玩系统，旨在为拥有大量游戏 ROM 文件的用户提供美观、高效的一站式管理方案。它解决了游戏收藏家们在管理庞大 ROM 库时面临的常见痛点：文件散乱缺乏组织、元数据缺失导致难以识别、多平台资源管理割裂，以及无法便捷地与其他设备或好友共享游玩。目标用户包括怀旧游戏爱好者、模拟器玩家、自托管技术爱好者以及任何希望系统化整理和远程游玩 ROM 文件的用户。

## 核心功能

- **智能扫描与元数据增强**：自动扫描本地 ROM 文件，并从 IGDB、Screenscraper 和 MobyGames 等多个游戏数据库 API 获取封面、简介、发行年份、开发商、评分等元数据，使游戏库变得美观且易于浏览。
- **多平台全面支持**：支持 400 多个游戏平台的 ROM 文件，兼容多种常见命名规范（如 No-Intro、Redump 等），并支持多碟游戏、DLC、MOD、汉化版、补丁和说明书等复杂文件结构。
- **浏览器内直接游玩**：集成 EmulatorJS 和 RuffleRS 等模拟器引擎，无需安装任何额外软件即可在任意现代浏览器中直接启动并游玩支持的游戏。
- **标签系统与高级过滤**：支持解析文件名中的自定义标签（如语言、版本、区域等），并允许用户手动添加和管理标签，配合多维度过滤器快速定位目标游戏。
- **用户管理与权限控制**：支持创建多用户账户，可设置不同权限（如只读、上传、管理），方便与家人或朋友安全地共享游戏库。
- **官方社区客户端支持**：提供针对 Playnite、Android（Argosy Launcher）和常用自制系统（CFWs，如 Grout）的官方应用，扩展使用场景。

## 技术架构

RomM 采用 Python 作为后端开发语言，基于异步 Web 框架构建，以提供高效的文件扫描和数据处理能力。前端使用现代 JavaScript 框架（如 Vue.js 或 React，具体请参考仓库代码）打造响应式、直观的用户界面，确保在桌面端和移动端均有良好的操作体验。项目以 Docker 容器化部署为主要方式，简化了安装和环境依赖管理，适合在 NAS、VPS 或树莓派等自托管硬件上运行。设计上采用了模块化的元数据提供者模式，用户可灵活配置首选数据源（IGDB、Screenscraper、MobyGames），并可自定义 artwork 来源（如 SteamGridDB）。文件存储采用本地目录挂载方式，不修改用户原始 ROM 文件，保证数据安全性。

## 安装与使用

RomM 推荐通过 Docker Compose 进行部署。以下是一个最小可用的 `docker-compose.yml` 示例：

```yaml
version: '3'
services:
  romm:
    image: ghcr.io/rommapp/romm:latest
    container_name: romm
    restart: unless-stopped
    ports:
      - "8080:8080" # 将主机 8080 端口映射到容器
    volumes:
      - /path/to/roms:/roms # 挂载你的 ROM 文件夹
      - ./config:/config  # 配置文件持久化
      - ./data:/data      # 数据目录（元数据缓存等）
    environment:
      - DB_HOST=romm_db
      - DB_NAME=romm
      - DB_USER=romm
      - DB_PASSWORD=changeme
      - ROMM_ADMIN_PASSWORD=admin
    depends_on:
      - romm_db

  romm_db:
    image: mariadb:10.6
    container_name: romm_db
    restart: unless-stopped
    volumes:
      - ./db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=rootpass
      - MYSQL_DATABASE=romm
      - MYSQL_USER=romm
      - MYSQL_PASSWORD=changeme
```

部署后，通过浏览器访问 `http://<你的IP>:8080`，首次登录使用环境变量中设定的管理员密码，随后即可开始扫描 ROM 文件夹。扫描完成后，游戏库将以美观的网格形式呈现，点击任意游戏即可查看详情、启动或播放。

## 适用场景

- **个人游戏档案馆**：将散落在不同硬盘、不同文件夹中的数百至数千个 ROM 文件统一管理，自动整理并丰富元数据，建立个人专属的怀旧游戏档案馆。
- **家庭或小团体共享游戏平台**：在一台家用服务器（如 NAS、旧 PC）上部署 RomM，配置多用户权限后，家庭成员或朋友可各自浏览、游玩自己感兴趣的游戏，无需手动复制文件。
- **远程游玩解决方案**：通过公网暴露或 VPN 连接，从任何地方的任何设备上（手机、平板、Chromebook）访问 RomM 的 Web 界面，直接启动模拟器游玩，无需携带实体游戏机或处理繁琐的模拟器配置。
- **游戏开发与研究备份**：对于整理游戏 ROM 的开发者或研究者，RomM 的标签系统和元数据抓取能力有助于分类和检索海量样本。

## 项目亮点

与同类项目（如 RetroArch 的 Web 前端、其他自托管 ROM 管理器）相比，RomM 的核心差异化优势在于：

- **极致的用户体验**：视觉设计精美，操作流程直观流畅，无论是扫描、浏览还是游玩，都享有接近商业游戏管理应用（如 Steam）的体验。
- **开箱即用的模拟能力**：无需手动配置任何模拟器核心或下载插件，EmulatorJS 的集成使得从安装到游玩仅需浏览器点击，降低了使用门槛。
- **高度可定制的元数据与标签**：允许用户自由选择数据源，并通过文件名标签或手动管理实现精细化的游戏分类，满足不同收藏习惯。
- **活跃的社区与生态**：拥有 Discord 社区、完善的文档，以及官方维护的多个平台客户端，生态持续扩展，更新迭代迅速。

## 相关链接

- [GitHub 仓库](https://github.com/rommapp/romm)
- [官方文档](https://romm.app/docs)
- [Discord 社区](https://discord.gg/romm)
