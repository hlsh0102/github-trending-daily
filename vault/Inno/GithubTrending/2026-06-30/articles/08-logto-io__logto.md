---
tags:
  - trending
  - article
repo: logto-io/logto
date: 2026-06-30
language: TypeScript
stars_total: 12828
stars_today: 158
---
## 项目概述

Logto 是一个现代化的开源身份认证与授权基础设施，专为 SaaS 和 AI 应用而设计。它基于 OIDC（OpenID Connect）和 OAuth 2.1 标准构建，内置多租户、企业级单点登录（SSO）和基于角色的访问控制（RBAC）能力，旨在帮助开发者快速构建生产就绪的认证系统，而不必深入理解复杂的身份协议细节。

无论您是正在开发多租户 SaaS 平台、AI 应用，还是需要为企业客户提供集成登录功能，Logto 都能提供开箱即用的解决方案。该项目采用 MPL-2.0 开源协议，由 TypeScript 编写，当前在 GitHub 上拥有超过 12,800 颗星，社区活跃度极高。

## 核心功能

- **多租户支持**：原生支持多租户架构，每个租户拥有独立的用户池、配置和品牌定制，适合 SaaS 和平台型应用。
- **企业级 SSO**：支持 SAML、OIDC、OAuth 等多种企业身份提供商集成，满足企业客户对单点登录的刚性需求。
- **细粒度 RBAC**：提供基于角色的权限管理，支持自定义角色、权限和作用域，实现精确的访问控制。
- **完整的用户管理**：内置注册、登录、密码重置、多因素认证（MFA）、社交登录等功能，覆盖用户生命周期的全场景。
- **可定制的登录体验**：支持拖拽式 UI 自定义，可调整登录页面的品牌、颜色和样式，无需编写前端代码。
- **审计日志与安全合规**：提供详细的用户操作日志，支持 GDPR、SOC2 等合规要求，确保安全可追溯。

## 技术架构

Logto 采用现代化的前后端分离架构，后端基于 Node.js 和 TypeScript 构建，使用 Koa 框架提供高性能的 API 服务。前端使用 React 开发管理控制台，并提供了丰富的 SDK 支持主流语言和框架。

- **协议层**：严格遵循 OIDC 和 OAuth 2.1 规范，确保与其他标准身份提供者的互操作性。支持授权码流程（PKCE 增强）、隐式流程、客户端凭据流等主流认证模式。
- **数据库**：默认使用 PostgreSQL 作为持久化存储，支持水平扩展和高可用部署。
- **模块化设计**：核心认证逻辑、用户管理、租户管理、API 网关等模块独立拆分，便于二次开发和自定义扩展。
- **安全实践**：内置 CSRF 防护、HTTPS 强制、密码哈希（bcrypt）、JWT 签名验证等安全机制，遵循业界最佳实践。
- **部署灵活**：支持 Docker 容器化部署、Kubernetes 编排，以及一键部署到 Render、Gitpod 等云平台。

## 安装与使用

### 快速开始（Docker）

Logto 提供了最简单的一键启动方式，只需安装 Docker 即可：

```bash
# 拉取并运行 Logto（使用 Docker Compose）
curl -fsSL https://raw.githubusercontent.com/logto-io/logto/master/docker-compose.yml | \
  docker compose -p logto -f - up -d
```

启动后，访问 `http://localhost:3001` 即可进入管理控制台。首次访问需要设置管理员账号。

### 集成到应用

以 Node.js 应用为例，安装 Logto SDK：

```bash
npm install @logto/node
```

然后配置认证中间件：

```javascript
const { LogtoClient } = require('@logto/node');

const client = new LogtoClient({
  endpoint: 'http://localhost:3001',   // Logto 服务地址
  appId: 'your-app-id',               // 从控制台创建的应用 ID
  appSecret: 'your-app-secret',       // 应用密钥
});

// 在路由中使用
app.get('/protected', client.requireAuth(), (req, res) => {
  res.json({ user: req.user });
});
```

## 适用场景

- **SaaS 平台开发**：多租户 SaaS 应用需要为每个客户提供独立的用户管理和认证配置，Logto 的原生多租户能力可以大幅降低开发成本。
- **AI 应用集成**：AI 工具通常需要快速上线并支持社交登录、API 密钥认证等功能，Logto 提供了开箱即用的集成方案。
- **企业级应用**：需要支持 SAML/OIDC SSO、RBAC 权限控制、审计日志等功能的企业内部系统或 B2B 应用。

## 项目亮点

- **开箱即用的企业级特性**：许多开源身份平台仅提供基础认证功能，需要大量二次开发才能支持多租户和 SSO。Logto 将这些企业级能力作为核心功能，开箱即用。
- **现代化技术栈**：基于 TypeScript 全栈开发，前后端统一语言，降低团队维护成本。对新兴的 AI 和 SaaS 开发者非常友好。
- **丰富的文档与 API**：提供完善的开发者文档、OpenAPI 规范、交互式 API 控制台，以及详细的迁移指南和示例代码。
- **活跃的社区与商业支持**：开源社区活跃，同时提供 Logto Cloud 托管服务，适合不想自建基础设施的团队。
- **对标准协议的深入支持**：严格遵循 OIDC 和 OAuth 2.1 规范，确保与其他身份系统（如 Okta、Azure AD）的无缝集成。

## 相关链接

- [GitHub 仓库](https://github.com/logto-io/logto)
- [官方网站](https://logto.io/)
- [文档中心](https://docs.logto.io)
- [API 参考](https://openapi.logto.io/)
- [Logto Cloud（托管服务）](https://cloud.logto.io/)
- [社区 Discord](https://discord.gg/vRvwuwgpVX)
