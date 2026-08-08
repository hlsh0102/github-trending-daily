---
tags:
  - trending
  - article
repo: goauthentik/authentik
date: 2026-08-08
language: Python
stars_total: 23652
stars_today: 530
---
## 项目概述

authentik 是一个开源的身份提供商（IdP），专注于为现代应用提供统一的单点登录（SSO）解决方案。它支持 SAML、OAuth2/OIDC、LDAP、RADIUS 等多种主流认证协议，能够作为自托管环境中的统一认证中心，服务于从个人实验室到大型生产集群的各类场景。项目定位为“认证粘合剂”，旨在帮助企业或个人将分散的应用认证需求整合到一个可靠、可扩展的平台上。对于需要替代 Okta、Auth0、Entra ID 等商业 IdP 的组织，authentik 提供了一个开源、可审计且成本可控的选择。

## 核心功能

- **多协议支持**：原生支持 SAML、OAuth2/OIDC、LDAP 和 RADIUS，几乎涵盖了所有主流应用的认证接口需求。
- **灵活的应用接入**：通过集中式管理界面，可以快速为各类 Web 应用、API 服务或传统桌面系统配置 SSO 接入。
- **用户与权限管理**：提供完整的用户生命周期管理，包括创建、禁用、分组、属性映射以及细粒度的授权策略配置。
- **可定制化的流程**：支持自定义认证流程，例如多因素认证（MFA）、密码重置、账户恢复等，并允许通过 Python 表达式编写高级逻辑。
- **自托管与高可用**：官方提供 Docker Compose、Kubernetes Helm Chart 以及 AWS CloudFormation 模板，方便在不同规模环境中部署。
- **企业级扩展选项**：针对大型组织提供商业版本，包含与主流企业目录的深度集成、高级审计功能及专业支持。

## 技术架构

authentik 的核心后端基于 Python（具体使用 Django 框架）构建，同时包含一个名为“outpost”的轻量级服务组件，负责处理如 LDAP 和 RADIUS 这类需要常驻监听特定端口的协议。这种前后端分离的架构设计使其具备较高的灵活性和可扩展性：Django 主服务处理核心的业务逻辑、Web 界面和 API 请求，而 outpost 则可以被独立部署和水平扩展，以应对高并发或特定协议的压力。此外，项目前端采用现代 Web 框架（基于 Web 组件技术）构建，保证了用户界面的响应速度。数据存储默认依赖 PostgreSQL，缓存和任务队列则使用 Redis，确保了在集群模式下的状态一致性。

## 安装与使用

### Docker Compose（推荐用于小型或测试环境）

1.  下载官方提供的 `docker-compose.yml` 和 `.env` 文件。
2.  `cd` 进入文件所在目录，编辑 `.env` 文件修改预设的密钥和数据库密码。
3.  执行 `docker compose up -d` 启动所有服务。
4.  访问 `http://localhost:9000` 完成初始管理员账户设置（if you set the env var `AUTHENTIK_BOOTSTRAP_TOKEN`，也可通过 API 自动初始化）。

### 最小使用示例

```bash
# 1. 拉取仓库并启动
git clone https://github.com/goauthentik/authentik
cd authentik
# 根据官方文档调整 .env 后
docker compose up -d

# 2. 通过 Web UI 登录后，创建第一个应用
#    - 进入“资源” -> “应用” -> “创建”
#    - 填写应用名称和 Slug，并选择你需要的认证协议（如 OAuth2/OIDC）
#    - 保存后即可获得 Client ID 和 Secret

# 3. 在目标应用（例如 Grafana、Nextcloud 或任意 OIDC 客户端）中配置：
#    - 认证端点（Authorization URL）：https://your-domain/application/o/authorize/
#    - 令牌端点（Token URL）：https://your-domain/application/o/token/
#    - 用户信息端点（Userinfo URL）：https://your-domain/application/o/userinfo/
```

## 适用场景

- **个人技术栈统一认证**：面向拥有自建 NAS、Dashboard、Git 服务、媒体管理工具等多样技术的个人用户，一键解决多套账号密码的痛点。
- **中小团队内部系统集成**：为研发团队内部的 GitLab、Jira、Confluence、Kubernetes Dashboard 等系统提供统一的账号和权限入口，简化入职与离职管理。
- **企业级身份治理**：作为传统 IDaaS 的替代，企业可以使用其精细的权限模型和审计日志功能，满足合规性要求，并实现包括社交登录在内的复杂身份源联合。

## 项目亮点

- **开源与代码透明**：相比商业 IdP 的黑盒逻辑，authentik 允许企业完全掌控代码，便于进行安全审计和自定义扩展。
- **全面的协议覆盖度**：在一个平台内同时提供 SAML、OIDC、LDAP 和 RADIUS 支持，避免了部署多个单项认证服务的复杂性和维护成本。
- **部署灵活性**：提供了从轻量级 Docker Compose 到云原生 Helm Chart 及 AWS 正式模板的完整部署路径，这使得项目可以很好地适应基础设施的演进。
- **活跃的社区与语言支持**：借助 Transifex 平台，项目界面支持多语言本地化，并拥有活跃的 Discord 技术社区，便于获取帮助和交流实践。

## 相关链接

- [GitHub 仓库](https://github.com/goauthentik/authentik)
- [官方网站](https://goauthentik.io/)
- [官方文档](https://docs.goauthentik.io/)
- [Helm Chart 仓库](https://github.com/goauthentik/helm)
