---
tags:
  - trending
  - article
repo: twentyhq/twenty
date: 2026-05-30
language: TypeScript
stars_total: 48490
stars_today: 578
---
## 项目概述

Twenty 是一个开源的企业级客户关系管理（CRM）系统，被设计为 Salesforce 的替代方案。它由 TypeScript 编写，核心定位是“为 AI 设计的 CRM”。该项目旨在解决传统 CRM 系统过于复杂、成本高昂、缺乏灵活性的问题，同时为现代企业提供一个可自由定制、数据自主可控的客户管理平台。Twenty 的目标用户包括需要高效管理销售流程的中小企业、追求数据隐私的团队、希望深度定制 CRM 的开发者，以及希望在 CRM 基础上集成 AI 功能的组织。

## 核心功能

- **联系人管理**：支持快速录入、搜索和分类联系人信息，包括姓名、公司、职位、联系方式等字段，并提供自定义字段扩展。
- **销售管道（Pipeline）管理**：可视化展示销售阶段（如潜在客户、谈判、成交），拖拽操作推进交易状态，实时追踪成交进度。
- **时间线（Timeline）**：自动记录与客户的所有互动历史，包括邮件、备注、任务和活动，形成完整的交互视图。
- **自定义对象与字段**：允许用户根据业务需求创建新的数据对象（如项目、订单）或为现有对象添加自定义字段，无需修改代码。
- **AI 集成能力**：提供 API 和插件机制，支持接入外部 AI 服务，实现智能线索评分、邮件自动摘要等功能。
- **团队协作**：支持角色权限管理，团队成员可协同查看、编辑客户数据，并通过内置评论功能进行讨论。

## 技术架构

Twenty 采用前后端分离的现代 Web 架构。前端基于 React 构建，使用 GraphQL 与后端通信，确保了数据查询的灵活性和高效性。后端采用 Node.js 运行时，结合 TypeScript 提供强类型保障和良好的可维护性。数据库方面，Twenty 默认使用 PostgreSQL，利用其强大的关系型数据存储和查询能力支持复杂的 CRM 数据模型。项目的另一个关键技术特点是模块化设计，核心业务逻辑（如联系人、销售管道）被拆分为独立的包，便于开发者按需扩展或替换组件。此外，Twenty 的设计思路中注重数据所有权，用户可以将数据部署在自己的服务器上，避免了 SaaS 模式下数据托管在第三方的问题。

## 安装与使用

Twenty 提供了多种部署方式，包括 Docker 容器化部署和从源代码构建。

### Docker 快速部署（推荐）

1.  确保系统已安装 Docker 和 Docker Compose。
2.  克隆仓库：
    ```bash
    git clone https://github.com/twentyhq/twenty.git
    cd twenty
    ```
3.  复制环境变量文件并配置：
    ```bash
    cp .env.example .env
    ```
4.  启动服务：
    ```bash
    docker compose up -d
    ```
5.  访问 `http://localhost:3000` 开始初始化设置，包括创建管理员账号和配置数据库。

### 从源代码构建

1.  确保已安装 Node.js（v18+）和 Yarn。
2.  克隆仓库并安装依赖：
    ```bash
    git clone https://github.com/twentyhq/twenty.git
    cd twenty
    yarn install
    ```
3.  配置数据库连接（默认使用 PostgreSQL），启动开发服务器：
    ```bash
    yarn dev
    ```
4.  访问 `http://localhost:3000` 进行配置和使用。

**最小可用示例**：部署完成后，登录系统即可创建联系人和建立销售管道。无需额外集成，默认界面即可支持基本的客户管理操作。

## 适用场景

- **中小企业销售管理**：团队规模较小，需要快速搭建一套低成本、可扩展的 CRM 系统，替代昂贵的 Salesforce 许可。
- **数据敏感型行业**：医疗、金融等对数据隐私要求高的领域，希望将客户数据部署在自有服务器上，避免外部云服务的数据泄露风险。
- **开发团队产品集成**：技术团队希望将 CRM 功能集成到现有产品中（如企业资源计划系统 ERP），基于 Twenty 的开源代码进行二次开发。
- **AI 驱动的销售流程优化**：企业计划引入 AI 辅助销售，例如自动分析客户邮件、预测成交概率，需一个开放的、支持 AI 插件的数据平台。

## 项目亮点

Twenty 的核心差异化优势在于它既开源又面向 AI 时代。相比传统 CRM（如 Salesforce、HubSpot），Twenty 完全开放源代码，用户可以自由修改、审计和扩展，避免了供应商锁定和昂贵的许可费用。与许多其他开源 CRM 相比，Twenty 具备更现代化的技术栈（TypeScript + React + GraphQL），开发体验友好，且内置了针对 AI 的集成接口，这使得它天然适合构建下一代智能化的客户管理工具。此外，其美观的用户界面和拖拽式操作降低了使用门槛，使得非技术用户也能快速上手。

## 相关链接

- [GitHub 仓库](https://github.com/twentyhq/twenty)
- [官方网站](https://twenty.com)
- [官方文档](https://docs.twenty.com)
- [Roadmap（路线图）](https://github.com/orgs/twentyhq/projects/1)
- [Figma 设计文件](https://www.figma.com/file/xt8O9mFeLl46C5InWwoMrN/Twenty)
