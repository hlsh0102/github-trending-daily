---
tags:
  - trending
  - article
repo: goauthentik/authentik
date: 2026-08-09
language: Python
stars_total: 24009
stars_today: 467
---
## 项目概述

authentik 是一个开源的身份提供商（Identity Provider，IdP），专为现代单点登录（SSO）场景而设计。它支持 SAML、OAuth2/OIDC、LDAP、RADIUS 等多种主流认证协议，能够满足从个人实验室到大规模生产集群的各类身份验证与授权需求。

该项目旨在解决企业在多云、多应用环境下身份管理碎片化的问题。通过将 authentik 作为统一的身份认证中枢，用户可以使用一组凭据安全地访问所有内部与外部应用，而管理员则能够在一个集中式平台上管理用户、组、策略与访问权限。

authentik 的目标用户包括：需要自托管身份解决方案的中小型团队、希望替换 Okta、Auth0 或 Entra ID 等商业 IdP 的企业、以及希望在 Kubernetes 或 Docker 环境中快速部署完整身份体系的技术人员。

## 核心功能

- **多协议支持**：原生支持 SAML、OAuth2/OIDC、LDAP、RADIUS 和 Proxy 认证，可无缝对接绝大多数现代应用与遗留系统。
- **可视化流程编辑器**：通过拖拽式界面设计认证流程，支持 MFA、密码重置、用户注册、条件访问等复杂逻辑，无需编写代码。
- **集中式策略引擎**：基于用户属性、组、IP、设备状态等条件动态授权，实现细粒度的访问控制。
- **用户与组管理**：内置完整的用户生命周期管理功能，支持批量导入、目录同步以及自定义用户属性。
- **事件日志与审计**：记录所有认证、授权和管理操作，提供可检索的审计日志，满足合规性要求。
- **高可用与扩展性**：支持水平扩展组件，可部署在 Kubernetes 集群中，提供 worker 和 broker 分离架构，适应大规模并发场景。

## 技术架构

authentik 后端基于 Python（主要使用 Django 框架）构建，前端采用 Web 组件技术，保证界面在不同环境下的流畅体验。其架构由几个核心组件构成：

- **Core（核心服务）**：负责处理 API 请求、认证逻辑和流程执行，是整个系统的心脏。
- **Worker（工作进程）**：异步执行后台任务，如发送邮件、执行策略更新和事件处理，与 Core 通过消息队列（Redis）通信。
- **Outpost（前哨）**：轻量级代理组件，部署在应用旁，用于执行 Proxy 认证和反向代理功能，可独立于核心进行弹性伸缩。
- **数据库层**：默认支持 PostgreSQL，用于持久化所有配置、用户和事件数据。

这种组件化设计使得 authentik 能够灵活适配不同规模的部署：小规模场景可单机运行所有组件，而大规模生产环境则可以将各个组件拆分为独立服务，配合 Kubernetes 实现自动扩缩容。此外，项目大量采用插件化设计，允许开发者通过编写自定义源（Source）和属性映射（Property Mapping）来扩展功能，极大提升了系统的可定制性。

## 安装与使用

authentik 提供多种安装方式，推荐从 Docker Compose 开始体验。

**1. 下载安装脚本**

```bash
git clone https://github.com/goauthentik/authentik.git
cd authentik
```

**2. 配置环境变量**

复制 `.env.example` 为 `.env`，修改 `AUTHENTIK_SECRET_KEY` 和 `AUTHENTIK_POSTGRESQL__PASSWORD` 等必要变量。

**3. 启动服务**

```bash
docker compose up -d
```

服务启动后，访问 `http://localhost:9000` 并按照引导创建管理员账号。

**4. 最小使用示例**

登录管理员界面后，进入“应用程序”页面，点击“创建”：

- 选择应用类型（例如 OAuth2/OIDC）；
- 填写应用名称，如 `my-app`；
- 配置重定向 URI 为你的应用回调地址；
- 保存后，系统会生成客户端 ID 和 Secret。

接着在“提供程序”中完成协议细节配置，即可在你的应用中使用 authentik 作为认证网关。对于 LDAP 或 RADIUS 场景，只需在“协议”中启用对应服务并进行简单绑定。

## 适用场景

- **企业内部应用统一认证**：将多个内部工具（如 GitLab、Jira、Grafana）接入 authentik，员工只需一次登录即可访问所有平台，简化账号管理。
- **Kubernetes 集群门户**：在云原生环境中部署 authentik，为集群内所有服务提供 OIDC 认证，实现统一的入口控制和审计。
- **面向客户的身份平台**：利用其可自定义的注册、登录和 MFA 流程，构建对外部用户开放的认证系统，并通过策略引擎区分普通用户与管理员权限。
- **替代商业 IdP 的迁移场景**：需要降低身份管理成本或实现数据本地化的组织，可使用 authentik 逐步替换 Okta 或 Auth0，同时保持协议兼容性。

## 项目亮点

- **高度模块化**：核心、Worker、Outpost 可独立部署，从单机到大型集群无缝过渡，架构选择灵活。
- **流程可视化**：将复杂的认证逻辑转化为可视化流程图，业务人员也能参与设计，大幅降低维护门槛。
- **开源透明**：项目完全开源（遵循企业友好协议），无隐藏收费功能，社区活跃，问题响应迅速。
- **部署方式多样**：除 Docker、Kubernetes 外，还提供 AWS CloudFormation 模板和 DigitalOcean 市场镜像，适配主流云环境。
- **生态集成能力**：不仅支持标准协议，还提供 Python SDK 和 REST API，便于开发者将 authentik 集成到自研系统中。

## 相关链接

- [GitHub 仓库](https://github.com/goauthentik/authentik)
- [官方文档](https://docs.goauthentik.io)
- [官方网站](https://goauthentik.io)
- [Helm Chart 仓库](https://github.com/goauthentik/helm)
