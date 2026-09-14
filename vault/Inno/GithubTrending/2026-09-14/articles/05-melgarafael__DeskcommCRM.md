---
tags:
  - trending
  - article
repo: melgarafael/DeskcommCRM
date: 2026-09-14
language: TypeScript
stars_total: 2361
stars_today: 432
---
## 项目概述

DeskcommCRM 是一个开源的 AI 销售操作系统（AI Sales OS），定位为面向“以聊天成交”的业务场景的自托管 CRM。它将原生 AI 智能体（AI Agents）与 WhatsApp 客服/销售渠道整合在同一个系统中，让企业可以在自己的服务器上运行完整的客户关系管理平台。项目主打对 Kommo、Octadesk 和 Intercom 等商业闭源产品的开源替代方案，采用 MIT 许可证。

从要解决的问题来看，传统 SaaS CRM 通常按月收取订阅费用，并对 AI、多渠道、多坐席等功能做分级限制；同时客户数据托管在第三方平台，在数据合规和成本控制上存在约束。DeskcommCRM 将 CRM、AI 智能体和 WhatsApp 接入能力打包为可自托管的产品，目标用户是希望通过 WhatsApp 进行销售和客户支持、且在意数据主权与长期成本的中小企业与团队，尤其是对巴西 LGPD（通用数据保护法）合规有要求的用户。

## 核心功能

- **原生 AI 智能体**：内置 AI Agents，可自动接待客户、进行线索资格评估（qualification）并推动成交，而非仅作为外挂插件存在。
- **WhatsApp 渠道集成**：通过 WAHA（WhatsApp HTTP API）对接 WhatsApp，实现消息收发与对话管理。
- **自托管 CRM**：提供完整的销售管道、客户与对话管理能力，数据存放在自有服务器上。
- **多租户（multi-tenant）支持**：可在同一部署实例下服务多个组织或团队，适合服务商与代理机构。
- **MCP-ready**：支持 Model Context Protocol，便于与外部 AI 工具链和模型上下文生态对接。
- **合规与部署工具**：围绕 LGPD 提供合规支持，并附带一键部署工具包。

## 技术架构

项目使用 TypeScript 作为主要开发语言，前端/全栈框架为 Next.js，数据与后端能力构建在 Supabase 之上。这一组合提供了服务端渲染、API 路由与数据库/认证一体化能力，便于快速搭建自托管应用。

WhatsApp 集成层采用 WAHA，以一个独立的 HTTP API 服务来封装 WhatsApp 会话，从而将消息渠道与 CRM 业务逻辑解耦。多租户设计意味着数据模型需要在组织/租户维度上进行隔离。项目还强调 MCP-ready，说明其 AI 智能体层预留了与外部模型和工具协议交互的接口。

在部署上，DeskcommCRM 与 HostGator 合作提供了 `hostgator-setup-kit/` 安装套件，可通过单条命令在 VPS 上安装 CRM 应用、WhatsApp 服务与数据库，并提供面向生产环境的 runbook 文档。仓库同时配置了 GitHub Actions（CI）流程，便于持续集成与质量校验。

## 安装与使用

根据项目说明，推荐的安装路径是在 VPS 上部署。基本流程如下：

1. 准备一台 VPS 服务器（可参考 HostGator 合作方案或自备环境）。
2. 使用仓库中的 `hostgator-setup-kit/` 安装套件，执行单条命令完成 app、WhatsApp 与数据库的部署。
3. 参照 `docs/runbooks/waha-hostgator.md` 生产 runbook 完成环境配置。
4. 启动服务后，登录 CRM 后台配置 AI 智能体、WhatsApp 渠道与销售流程。

由于项目提供的是部署脚本而非 npm 包，具体命令与参数需查阅仓库内的安装首节与 runbook 文档。最小可用示例即：完成安装后接入一个 WhatsApp 号码，创建一个 AI 智能体并绑定销售管道，即可开始自动接待与线索评估。

## 适用场景

- **以 WhatsApp 为主要成交渠道的中小企业**：需要通过聊天完成售前咨询与成交，且希望自动化初步接待。
- **对数据主权与合规有要求的团队**：希望将客户数据保存在自有服务器，并满足 LGPD 等本地合规要求。
- **代理机构与服务商**：借助多租户能力，为多个客户组织统一托管 CRM 与 AI 客服。
- **希望替代商业 SaaS 的企业**：评估 Kommo、Octadesk 或 Intercom 的付费方案后，寻求无月费、无功能分级的开源选择。

## 项目亮点

与同类开源 CRM 相比，DeskcommCRM 的差异化在于“CRM + 原生 AI 智能体 + WhatsApp”三位一体的定位，而非单纯的消息工具或数据库。它明确将自身定位为商业闭源产品的开源替代，强调无月费、无功能锁定、数据自有。多租户与 MCP-ready 的设计使其适配服务商场景并具备接入外部 AI 生态的扩展性。此外，与 HostGator 合作的单命令 VPS 部署方案和面向生产环境的 runbook，降低了自托管门槛，而 LGPD 合规支持也切合巴西市场的实际需求。

## 相关链接

- [GitHub 仓库](https://github.com/melgarafael/DeskcommCRM)
- [架构文档](ARCHITECTURE.md)
- [项目愿景](VISION.md)
- [贡献指南](CONTRIBUTING.md)
- [生产部署 runbook](docs/runbooks/waha-hostgator.md)
