---
tags:
  - trending
  - article
repo: goauthentik/authentik
date: 2026-08-07
language: Python
stars_total: 23202
stars_today: 138
---
## 项目概述

authentik 是一个开源的身份提供者（Identity Provider，IdP），旨在为现代应用提供统一的单点登录（SSO）解决方案。它解决了企业在多云、多应用环境下身份认证和授权管理碎片化的问题，让用户只需一套凭据即可安全访问所有内部系统。

该项目专注于自托管场景，覆盖范围从小型实验室环境到大规模生产集群，支持 SAML、OAuth2/OIDC、LDAP、RADIUS 等主流认证协议。对于希望在自建环境中实现集中身份管理、无需依赖商业云服务的团队而言，authentik 提供了一个免费且功能完整的替代方案。同时，项目也提供企业版，供需要大规模身份治理的组织替换 Okta、Auth0 或 Entra ID 等商业产品。

## 核心功能

- **统一认证协议支持**：原生支持 SAML 2.0、OAuth2/OIDC、LDAP、RADIUS 和 Proxy 认证，可对接绝大多数现代应用与旧系统。
- **自动化流程引擎**：基于 Flow 的可视化配置，实现注册、登录、密码重置、MFA 设备管理、用户邀请等流程的自动化编排，无需编写代码。
- **多因素认证（MFA）**：内置 TOTP、WebAuthn/U2F 硬件密钥支持，可针对不同用户或组强制启用不同强度的认证策略。
- **用户生命周期管理**：提供用户、组、权限的集中管理，支持通过 LDAP 或 API 批量导入导出用户，并可与外部目录（如 Active Directory）同步。
- **访问控制策略**：基于角色的权限分配和细粒度的应用访问策略，可按用户属性、IP 段、设备状态等条件动态决定是否放行。
- **内置审计与日志**：记录所有认证事件、管理操作和流程执行情况，支持日志导出到外部 SIEM 系统，满足合规需求。

## 技术架构

authentik 采用前后端分离的架构，后端基于 Python 语言的 Django 框架构建，前端则使用 TypeScript 与 Web Components 技术。系统的核心组件包括：

- **Core**：负责 Web 界面、API、数据持久化和 Flow 引擎，是整个系统的控制平面。
- **Outpost**：一个轻量级代理组件（用 Go 编写），部署在受保护应用侧，负责处理实际的身份验证请求、会话刷新和最终的用户重定向。每个 Outpost 同时支持多种协议，减少了多应用环境下的部署复杂度。

数据存储默认采用 PostgreSQL，缓存和 session 管理则使用 Redis，确保多节点部署时的状态一致性和性能。Flow 引擎是 authenticik 最具特色的设计——它将每个认证过程拆解为一系列可编排的步骤（如输入校验、检查用户状态、触发验证器等），通过可视化界面拖拽配置，极大提升了灵活性和可维护性。

系统支持 Docker Compose、Kubernetes（Helm Chart）和 AWS CloudFormation 等多种部署方式，适合从单机到容器化的各类环境。

## 安装与使用

### Docker Compose 快速启动

1. 下载 `docker-compose.yml` 和 `.env` 文件：

```bash
curl -L https://goauthentik.io/docker-compose.yml -o docker-compose.yml
curl -L https://goauthentik.io/.env -o .env
```

2. 编辑 `.env` 文件，至少设置 `AUTHENTIK_SECRET_KEY`、`AUTHENTIK_COOKIE_DOMAIN` 和 `AUTHENTIK_BOOTSTRAP_PASSWORD`。

3. 启动服务：

```bash
docker-compose up -d
```

4. 访问 `http://localhost:9000`（或设置的域名），使用 `akadmin` 和之前在 `.env` 中设定的密码登录管理员界面。

### 最小接入示例（OIDC）

1. 在管理界面创建 Provider，选择 OIDC 类型。
2. 配置客户端 ID、重定向 URL 等参数。
3. 在“应用”中创建一个应用，并关联到刚创建的 Provider。
4. 在目标应用中将认证端点指向 `http://your-authentik-host/application/o/{slug}/` 即可。

## 适用场景

- **企业内部统一登录门户**：为多个自建 Web 应用（如 GitLab、Grafana、Jenkins）接入统一登录体验，员工一次登录即可访问全部服务。
- **面向用户的多租户 SaaS**：作为认证后端，为不同客户提供独立的身份空间和品牌化登录界面，同时支持社交登录等扩展。
- **实验室与测试环境**：小型团队或开发者在测试集群中快速搭建 IdP，验证 OIDC 或 SAML 集成，无需负担商业软件许可成本。
- **替代商业 IdP 的过渡阶段**：企业和机构在迁移过程中使用 authentik 作为自托管方案，逐步将本地目录对接并淘汰旧系统。

## 项目亮点

- **全协议覆盖**：在开源 IdP 领域，authentik 是少数几乎覆盖所有主流认证协议的项目，从 SAML、OIDC 到 LDAP 和 RADIUS 一应俱全，降低了技术选型的风险。
- **可编排的 Flow 引擎**：相比大多数 IdP 使用固定模板，authentik 允许管理员用可视化方式自定义每个交互流程，真正做到按需定制。
- **规模化部署友好**：架构中核心与 Outpost 分离的设计，使得在大型集群中扩展时无需改动现有应用，也便于将认证代理下沉到网络边缘。
- **活跃的社区治理**：项目拥有超过两万个 Star，持续维护频率高，文档完善，社区支持积极，且核心代码完全开源（GPLv3），无“开放核心”陷阱。

## 相关链接

- [GitHub 仓库](https://github.com/goauthentik/authentik)
- [官方文档](https://docs.goauthentik.io)
- [官网](https://goauthentik.io)
- [Helm Chart 仓库](https://github.com/goauthentik/helm)
