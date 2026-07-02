---
tags:
  - trending
  - article
repo: logto-io/logto
date: 2026-07-02
language: TypeScript
stars_total: 13365
stars_today: 113
---
## 项目概述

Logto 是一个面向 SaaS 和 AI 应用的现代开源身份认证与授权基础设施。它基于 OIDC 和 OAuth 2.1 协议构建，内置多租户、企业级单点登录（SSO）和基于角色的访问控制（RBAC）能力。项目旨在解决开发者在构建安全、可生产的认证系统时面临的复杂性，让团队能够更快地集成认证功能，并专注于核心业务逻辑。

Logto 由社区驱动，采用 MPL-2.0 开源许可协议，目前已获得超过 13000 颗 GitHub Star。其目标用户包括 SaaS 产品开发者、AI 应用团队、需要多租户隔离的云服务提供商，以及需要集成企业 SSO 的中大型组织。

## 核心功能

- **基于 OIDC 和 OAuth 2.1 的认证**：完整实现 OpenID Connect 和 OAuth 2.1 协议，提供标准的授权码流程、PKCE、令牌刷新等机制，确保认证过程安全合规。
- **多租户支持**：原生支持多租户架构，每个租户拥有独立的用户池、配置和策略，适用于 B2B SaaS 场景，便于不同客户间的数据隔离。
- **企业级单点登录（SSO）**：支持 SAML、OIDC、CAS 等主流企业 SSO 协议，可对接 Azure AD、Google Workspace、Okta 等身份提供商，满足企业用户从统一入口登录的需求。
- **基于角色的访问控制（RBAC）**：提供灵活的角色和权限管理能力，支持自定义角色、权限粒度定义，并可在 API 资源级别进行精细化授权。
- **用户管理与自助服务**：内置用户注册、登录、密码重置、多因素认证（MFA）等完整用户生命周期管理功能，并提供可定制的登录页和用户自助门户。
- **开发友好与快速集成**：提供 RESTful API、SDK（支持 Node.js、React、Vue、Android、iOS 等主流平台）、以及管理控制台，开发者可在数小时内完成基本认证集成。

## 技术架构

Logto 采用前后端分离的架构设计，后端核心使用 TypeScript 编写，基于 Node.js 运行时。其技术栈亮点包括：

- **协议层**：严格遵循 OIDC 和 OAuth 2.1 规范，实现身份认证与授权标准，确保与第三方服务和工具（如 API 网关、微服务框架）的互操作性。
- **多租户引擎**：通过租户标识进行数据隔离和路由，每个租户拥有独立的身份提供商配置、用户目录和权限模型，支持动态创建和管理租户。
- **插件化设计**：SSO 连接器、密码策略、MFA 等方式均以插件形式实现，方便开发者按需扩展或替换。
- **状态管理**：使用 PostgreSQL 作为主数据库，通过事务和索引保证认证流程的一致性和性能；同时利用 Redis 缓存会话和令牌，提升响应速度。
- **部署灵活性**：支持 Docker 容器化部署，提供 Heroku、Render、GitPod 等云平台一键部署模板，也可自托管于 Kubernetes 或裸机环境。

架构上，Logto 将认证和授权逻辑抽象为独立服务，与业务应用解耦，使得系统可以独立扩展和维护。

## 安装与使用

### 快速安装（Docker）

确保已安装 Docker，执行以下命令启动 Logto：

```bash
docker run --name logto -d -p 3001:3001 logtoio/logto
```

访问 `http://localhost:3001` 打开管理控制台，按向导完成初始配置。

### 在应用中集成

以 Node.js 应用为例，使用官方 SDK：

```bash
npm install @logto/node
```

然后在应用中初始化：

```javascript
import LogtoClient from '@logto/node';

const logtoClient = new LogtoClient({
  endpoint: '你的 Logto 实例地址',
  appId: '你的应用 ID',
  appSecret: '你的应用密钥',
});

// 实现登录路由
app.get('/login', async (req, res) => {
  const redirectUri = await logtoClient.signIn('http://localhost:3000/callback');
  res.redirect(redirectUri);
});

// 回调处理
app.get('/callback', async (req, res) => {
  await logtoClient.handleSignInCallback(req.url);
  res.redirect('/');
});
```

更详细的集成指南和 SDK 列表请参考[官方文档](https://docs.logto.io)。

## 适用场景

- **B2B SaaS 平台**：多租户架构天然适配需要为不同企业客户提供独立认证环境的 SaaS 产品，如项目管理工具、CRM 系统、数据分析平台。
- **AI 应用集成**：AI 应用常需要管理用户订阅、API 密钥和访问权限，Logto 提供的 OAuth 2.1 和 RBAC 可帮助快速搭建用户鉴权层。
- **企业内部系统统一认证**：统一企业内部多个应用系统的登录入口，集成企业 AD/SSO，实现单点登录和用户统一管理。
- **API 网关或微服务鉴权**：作为中央身份服务，为后端微服务提供标准的令牌验证和权限判定，降低每个服务独立实现认证的复杂度。

## 项目亮点

- **协议标准与现代化**：直接基于 OIDC 和 OAuth 2.1 标准构建，而非自行发明协议，确保与生态工具的兼容性，并降低了审计和合规风险。
- **零配置多租户**：多租户支持开箱即用，无需额外开发或复杂配置，极大降低了 B2B 产品的认证实现成本。
- **企业级特性全面**：同时覆盖 SSO、RBAC、MFA 等企业级需求，而不仅仅是基础的登录注册功能，适合中大型组织使用。
- **开发体验优先**：提供丰富的 SDK、CLI 工具、可定制的登录组件，以及直观的管理控制台，显著缩短从概念到上线的时间。
- **开源且可自托管**：核心功能完全开源，开发者可以私有部署，掌控数据安全，避免了依赖第三方服务的锁定风险。

## 相关链接

- [GitHub 仓库](https://github.com/logto-io/logto)
- [官方网站](https://logto.io)
- [官方文档](https://docs.logto.io)
- [云端托管服务](https://cloud.logto.io)
- [API 参考](https://openapi.logto.io)
- [社区博客](https://blog.logto.io)
