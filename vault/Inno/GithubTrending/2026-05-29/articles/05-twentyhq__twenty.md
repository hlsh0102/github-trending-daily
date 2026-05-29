---
tags:
  - trending
  - article
repo: twentyhq/twenty
date: 2026-05-29
language: TypeScript
stars_total: 48003
stars_today: 493
---
## 项目概述

Twenty 是一个开源的客户关系管理（CRM）系统，旨在成为 Salesforce 的现代替代品。该项目以“为 AI 而设计”为核心理念，不仅提供传统 CRM 的数据管理功能，更强调与人工智能技术的深度整合。目标用户包括寻求数据自主权的企业、希望定制化 CRM 的开发者团队，以及对现代 UI/UX 有高要求的中小型企业。Twenty 采用 TypeScript 开发，拥有超过 48,000 个 GitHub Star，是目前最受关注的开源 CRM 项目之一。

## 核心功能

- **丰富的对象建模**：支持自定义对象、字段和关系，包括标准对象（联系人、公司、机会）以及用户定义的任意业务实体。每个对象均可添加自定义字段，并支持关联、循环引用等复杂关系。
- **高级搜索与过滤**：提供全文搜索、多条件组合过滤、保存搜索视图等功能，支持按日期、状态、归属人等属性快速筛选数据。
- **协作功能**：内置评论、提及、活动日志和任务分配系统，支持团队成员在同一记录上进行实时协作，并保留完整的操作历史。
- **自动化工作流**：通过可视化的触发器与动作配置，支持自动化邮件发送、字段更新、任务创建等操作。可基于事件（如记录创建/更新）或时间条件（定时任务）触发。
- **AI 集成能力**：提供可扩展的 AI 助手接口，支持自然语言查询记录、自动生成摘要、智能推荐下一步行动。开发者可通过插件系统接入自定义 AI 模型或第三方 AI 服务。
- **REST/GraphQL API**：提供完整的 RESTful 和 GraphQL API，支持外部系统集成。API 遵循标准化命名规范，并自动生成交互式文档。

## 技术架构

Twenty 采用前后端分离的现代架构。前端基于 React 与 TypeScript 构建，使用 GraphQL 作为 API 查询语言，配合 Apollo Client 进行状态管理。后端基于 Node.js 与 Prisma ORM 构建，数据库采用 PostgreSQL。整体架构具有以下特点：

1. **模块化设计**：核心功能按领域划分为独立模块（如联系人、公司、自动化），模块间通过定义良好的接口通信，便于扩展和维护。
2. **实时能力**：借助 WebSocket 实现推送通知和实时数据更新，用户无需手动刷新即可看到其他成员的协作变动。
3. **可观测性**：内置日志、审计和性能监控接口，支持接入外部监控系统（如 Prometheus、Sentry）。
4. **安全架构**：支持细粒度的权限控制（记录级、字段级），并提供基于 OAuth 2.0 的身份认证方案，可与主流身份提供商（如 Google、GitHub）集成。

技术栈核心包括：TypeScript、React、GraphQL、Prisma、PostgreSQL、Node.js、Redis（用于缓存和会话管理）。

## 安装与使用

Twenty 提供两种安装方式：使用 Docker 一键部署，或通过本地开发环境手动安装。

**使用 Docker（推荐）**：
```bash
# 克隆仓库
git clone https://github.com/twentyhq/twenty.git
cd twenty

# 使用 Docker Compose 启动所有服务
docker compose up -d
```

访问 `http://localhost:3000` 即可使用。首次启动会自动创建初始管理员账户（用户名和密码在启动日志中显示）。

**本地开发环境**：
```bash
# 安装依赖
cd server
npm install
cd ../front
npm install

# 配置环境变量
cp server/.env.example server/.env
cd server
npx prisma migrate dev
npx prisma db seed

# 启动后端（终端1）
npm run dev

# 启动前端（终端2）
cd ../front
npm run dev
```

**最小可用示例**：启动后，进入“设置” → “数据模型”，创建自定义对象“项目”，添加字段“预算”（数字）和“截止日期”（日期）。回到仪表板，添加一条测试记录，尝试使用搜索功能查找该记录，并通过 GraphQL 端点 `http://localhost:3000/api/graphql` 使用以下查询验证 API 可用性：
```graphql
{
  objects(limit: 5) {
    id
    name
  }
}
```

## 适用场景

1. **中小企业的客户管理**：替代昂贵的 Salesforce 订阅，提供联系人管理、销售管道追踪、客户互动记录等核心功能，支持按需扩展字段和对象。
2. **定制化 CRM 需求**：企业需要在其 CRM 中存储非标准数据（如技术指标、产品配置信息），使用 Twenty 的自定义对象功能可构建专属数据模型。
3. **AI 驱动的销售辅助**：利用内置 AI 集成能力，实现自动记录注释、智能客户评分、对话摘要生成，提升销售团队效率。
4. **多系统数据协同**：通过 REST/GraphQL API，将 Twenty 作为统一的客户数据平台，与 ERP、客服系统、营销自动化工具进行数据同步，打破信息孤岛。

## 项目亮点

- **真正的开源**：采用 AGPLv3 许可证，代码完全透明，用户拥有数据的完全控制权。与 Salesforce 的封闭生态形成鲜明对比，Twenty 允许企业自由修改、审计和自托管。
- **AI 原生设计**：不同于传统 CRM 事后补加 AI 功能，Twenty 从架构层面为 AI 集成预留了接口和抽象层。开发者可以轻松接入自定义模型，实现从自然语言查询到智能工作流编排的深度应用。
- **现代化用户体验**：采用最新的 React 技术和设计语言，界面流畅、响应迅速。暗色模式、无限滚动、拖拽排序等现代交互特性贯穿产品始终，降低了用户学习成本。
- **活跃的社区生态**：拥有 48,000+ Star 和 700+ 贡献者，社区活跃度在开源 CRM 中名列前茅。官方提供 Figma 设计源文件、完善的文档和活跃的 Discord 社区，降低定制开发门槛。

## 相关链接

- [GitHub 仓库](https://github.com/twentyhq/twenty)
- [官方网站](https://www.twenty.com)
- [在线文档](https://docs.twenty.com)
- [社区讨论（Discord）](https://discord.gg/cx5n4Jzs57)
- [设计资源（Figma）](https://www.figma.com/file/xt8O9mFeLl46C5InWwoMrN/Twenty)
