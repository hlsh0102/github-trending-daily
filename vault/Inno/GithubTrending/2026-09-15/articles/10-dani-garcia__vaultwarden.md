---
tags:
  - trending
  - article
repo: dani-garcia/vaultwarden
date: 2026-09-15
language: Rust
stars_total: 67596
stars_today: 115
---
## 项目概述

Vaultwarden 是一个使用 Rust 编写的非官方 Bitwarden 服务端实现，前身为 bitwarden_rs。它实现了 Bitwarden 客户端 API，可与官方 Bitwarden 客户端（浏览器扩展、桌面端、移动端、命令行工具等）配合使用。项目的核心目标是提供一个轻量、资源占用低的替代方案，使自托管密码管理服务的部署门槛大幅降低。官方 Bitwarden 服务端基于 .NET 与大量依赖组件，运行时通常需要数 GB 内存；而 Vaultwarden 编译为单一二进制文件，在树莓派、低配 VPS 或家用 NAS 上即可流畅运行，内存占用常在几十到数百 MB 级别。目标用户是希望自主掌控密码数据、但又不愿承担官方服务端运维成本与硬件开销的个人用户、家庭用户及小型团队。

## 核心功能

- **兼容官方客户端**：实现 Bitwarden Client API，官方浏览器扩展、桌面应用、移动 App 与 CLI 均可直接连接，无需改动客户端。
- **多用户与组织支持**：支持多账户注册、组织（Organization）管理、成员与权限配置，可满足家庭或小团队的共享密码库需求。
- **附件与多因素认证**：支持文件附件存储、TOTP 两步验证，以及通过邮件邀请成员等流程。
- **灵活的数据库与存储后端**：默认使用 SQLite，同时支持 MySQL/MariaDB 与 PostgreSQL；附件可存于本地文件系统或兼容 S3 的对象存储。
- **多种部署方式**：提供官方 Docker 镜像（Docker Hub、GitHub Container Registry、Quay.io），也支持直接从源码编译运行。
- **管理面板**：内置 `/admin` 管理页面，用于配置用户注册策略、邮件服务、备份等运行参数。

## 技术架构

项目以 Rust 编写，采用 Actix Web 作为 HTTP 框架，注重性能与内存安全。数据层通过 Diesel 等 ORM 对不同数据库进行抽象，使 SQLite、MySQL、PostgreSQL 可以共用同一套业务逻辑。运行时配置主要通过环境变量注入，配合 `.env` 文件加载，便于容器化部署。架构上，服务端对外暴露与 Bitwarden 官方一致的 REST 接口与 WebSocket 通知通道，客户端因此感知不到后端实现的差异。附件存储、邮件发送、身份认证等模块均做了解耦设计，可独立替换实现。安全方面依赖 Rust 生态的加密库完成密钥派生与加密操作，服务端默认以「零知识」方式存储用户保险库数据。项目遵循 AGPL-3.0 许可证，社区贡献活跃。

## 安装与使用

最简方式是通过 Docker 运行。以下为基本步骤（示意，具体以官方文档为准）：

1. 准备一个数据目录，例如 `data/`，用于持久化数据库与附件。
2. 生成一个用于签名的安全令牌（如使用 `openssl rand -base64 48`）。
3. 启动容器，将数据目录挂载到 `/data`，并设置 `SIGNUPS_ALLOWED`、`ADMIN_TOKEN` 等环境变量。

示例命令：

```bash
docker run -d --name vaultwarden \
  -v /path/to/data/:/data/ \
  -p 80:80 \
  -e SIGNUPS_ALLOWED=true \
  -e ADMIN_TOKEN='your_secure_token' \
  vaultwarden/server:latest
```

启动后访问服务地址即可。首次注册管理员账户后，建议将 `SIGNUPS_ALLOWED` 改为 `false`，防止他人注册。随后在 Bitwarden 客户端的「自托管环境」设置中填入服务器 URL，即可登录使用。若需 HTTPS，通常在前端配合 Caddy、Nginx 或 Traefik 反向代理完成证书与转发配置。

## 适用场景

- **个人自托管密码库**：在低配 VPS 或树莓派上搭建，完全掌控数据，避免依赖第三方云服务。
- **家庭或小团队共享**：通过组织功能共享部分凭据，同时保持成员各自私有保险库隔离。
- **资源受限环境**：内存与磁盘有限的设备，官方服务端难以运行，Vaultwarden 可作为替代。
- **内网/离线部署**：在企业内网或隔离网络中部署，满足合规与数据不出境的要求。

## 项目亮点

与官方 Bitwarden 服务端相比，Vaultwarden 最显著的差异在于资源占用极低，单一二进制或一个容器即可完成部署，运维成本小。它保持与官方客户端的接口兼容，用户无需更换已有客户端。同时提供 SQLite 默认配置，省去独立数据库的部署步骤；在需要时又可切换至 MySQL/PostgreSQL。项目拥有超过 6.7 万 Star 和活跃的社区讨论渠道（Matrix、Discourse），问题反馈与版本迭代较为及时。需要说明的是，这是非官方实现，作者明确声明与 Bitwarden 官方无隶属关系，使用者应自行评估安全与合规要求。

## 相关链接

- [GitHub 仓库](https://github.com/dani-garcia/vaultwarden)
- [社区讨论区（Discourse）](https://vaultwarden.discourse.group/)
- [Matrix 聊天室](https://matrix.to/#/#vaultwarden:matrix.org)
- [官方 Bitwarden 客户端下载](https://bitwarden.com/download/)
