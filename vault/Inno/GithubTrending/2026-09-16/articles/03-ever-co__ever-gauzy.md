---
tags:
  - trending
  - article
repo: ever-co/ever-gauzy
date: 2026-09-16
language: TypeScript
stars_total: 6906
stars_today: 634
---
## 项目概述

Ever® Gauzy™ 是一个开源的企业业务管理平台，将 ERP（企业资源规划）、CRM（客户关系管理）、HRM（人力资源管理）、ATS（申请人跟踪系统）和 PM（项目管理）等多个模块整合到同一套系统中。项目由 Ever Co. 团队发起并持续维护，采用 TypeScript 编写，主仓库在 GitHub 上已获得约 6900 颗星标。

它要解决的问题很直接：中小型企业和协作型组织通常需要同时使用多套商业软件来覆盖财务、客户、员工、招聘和项目等环节，由此产生数据孤岛、账号割裂和授权成本高的问题。Gauzy 试图用一套开源、可自托管的平台替代这些分散的工具，并特别面向协作经济、按需服务和共享经济类组织设计。

目标用户包括：希望自主掌控业务数据的企业 IT 团队、处于早期阶段需要一体化后台的创业公司，以及需要二次开发能力的集成商和开发者。

## 核心功能

- **企业资源规划（ERP）**：提供库存、会计、费用、收入等基础财务与运营管理能力，支撑企业日常记账与资源调度。
- **客户关系管理（CRM）**：管理线索、客户、联系人、销售管道和活动记录，帮助销售团队跟踪商机进展。
- **人力资源管理（HRM）**：覆盖员工档案、组织架构、考勤、时间跟踪、薪酬与休假管理。
- **申请人跟踪系统（ATS）**：支持职位发布、候选人管理、面试流程和招聘管道，与企业 HRM 模块打通。
- **项目管理（PM）**：提供任务、看板、里程碑、工时统计等功能，用于协作式项目推进。
- **多租户与角色权限**：平台采用多租户架构，支持不同组织、团队和角色在同一实例中隔离运行。

## 技术架构

Gauzy 全栈以 TypeScript 为主要语言，采用前后端分离的模块化设计。

后端基于 Node.js 与 NestJS 框架，使用 TypeORM 作为 ORM 层，可在 SQLite、PostgreSQL、MySQL 等数据库间切换。各业务模块（ERP、CRM、HRM 等）以独立模块形式组织，便于按需启用或裁剪。平台提供 Headless API（官方在 api.gauzy.co/docs 提供 API 文档），前端或第三方系统均可通过 REST 接口接入。

前端使用 Angular 构建管理后台，另有独立的 Ever Teams 项目采用 React（Next.js）与 React Native（Expo）技术栈，同样连接同一套 Gauzy API，说明平台在设计上刻意将 API 与 UI 解耦，支持多客户端接入。

多租户、角色权限和国际化是架构中的横切关注点，分别通过租户上下文、Guard/策略机制和 i18n 资源文件实现。项目同时提供 Gitpod 一键开发环境和 DeepWiki 文档入口，降低本地搭建与理解代码库的门槛。

## 安装与使用

Gauzy 提供多种部署方式，常见流程如下（具体命令以仓库文档为准）：

1. 克隆仓库：
   ```bash
   git clone https://github.com/ever-co/ever-gauzy.git
   cd ever-gauzy
   ```
2. 安装依赖（项目使用 Yarn 工作区管理 monorepo）：
   ```bash
   yarn install
   ```
3. 配置环境变量，设置数据库连接（如 PostgreSQL）及其他必要参数。
4. 运行数据库迁移与种子数据：
   ```bash
   yarn run migration:run
   yarn run seed
   ```
5. 启动 API 与前端：
   ```bash
   yarn start:api
   yarn start:gauzy
   ```

此外，也可以直接使用官方托管的 API（api.gauzy.co），或通过 Gitpod 在浏览器中获得预配置的开发环境。生产部署建议参考仓库中的 Docker 与 Kubernetes 相关说明。

## 适用场景

- **中小企业的统一后台**：用一个平台替代分散的 CRM、HR 和项目管理工具，减少系统间数据同步成本。
- **协作与共享经济组织**：面向按需用工、自由职业者协作等场景，需要同时管理人员、客户和项目。
- **自托管与数据合规需求**：对数据主权有要求、希望将业务系统部署在自有基础设施上的团队。
- **二次开发与集成**：开发者基于 Gauzy 的 Headless API 和模块化代码库，构建垂直行业解决方案或对接现有系统。

## 项目亮点

与同类开源 ERP/CRM 项目相比，Gauzy 的差异点在于模块覆盖广且相互打通，ERP、CRM、HRM、ATS、PM 并非各自独立的产品线，而是共享同一套数据模型与权限体系。技术栈统一在 TypeScript 生态内，前后端开发者可以复用语言与工具链。平台以 Headless API 为核心，前端 UI 可替换，官方自身就用 Angular 和 React 两套实现验证了这一点。AGPL-3.0 授权加上活跃的社区更新，也使其在开源商业管理平台中具有较高的可见度。

## 相关链接

- [GitHub 仓库](https://github.com/ever-co/ever-gauzy)
- [官网](https://gauzy.co)
- [API 文档](https://api.gauzy.co/docs)
- [DeepWiki 文档](https://deepwiki.com/ever-co/ever-gauzy)
- [Gitpod 在线开发环境](https://gitpod.io/#https://github.com/ever-co/ever-gauzy)
- [Ever Teams 项目](https://github.com/ever-co/ever-teams)
