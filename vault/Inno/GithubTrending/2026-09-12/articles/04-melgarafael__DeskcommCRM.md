---
tags:
  - trending
  - article
repo: melgarafael/DeskcommCRM
date: 2026-09-12
language: TypeScript
stars_total: 1464
stars_today: 152
---
## 项目概述

DeskcommCRM 是一个开源的 AI 销售操作系统，核心定位是面向“以聊天方式成交”的业务场景，提供自托管 CRM 与原生 AI 智能体的组合能力。它通过集成 WhatsApp（基于 WAHA，即 WhatsApp HTTP API）打通客户沟通渠道，让 AI 智能体在对话中完成接待、资格筛选与销售推进，相关数据与流程沉淀在 CRM 中统一管理。

项目解决的核心问题是：中小型及成长型团队在使用 Kommo、Octadesk、Intercom 等商业 SaaS 时，面临订阅费用持续支出、功能受套餐限制、客户数据托管在第三方等问题。DeskcommCRM 将 CRM、AI 智能体与 WhatsApp 接入整合为一套可部署在自有服务器上的系统，用户对自己的数据拥有完全控制权，且没有功能上的分级锁定。

目标用户包括：依赖 WhatsApp 进行售前咨询与成交的销售团队、希望以低成本构建客服与销售自动化的中小企业、需要对多客户或多品牌进行隔离管理的服务商，以及因数据合规要求而倾向自托管方案的团队（项目强调遵循 LGPD，即巴西通用数据保护法）。

## 核心功能

- **原生 AI 智能体**：AI 智能体直接嵌入 CRM 工作流，可在 WhatsApp 会话中执行接待、需求询问、线索资格判断和销售推进，而非仅作为独立聊天窗口存在。
- **WhatsApp 集成（WAHA）**：通过 WAHA 连接 WhatsApp，使对话记录、联系人、商机与 CRM 数据保持一致。
- **自托管部署**：整套系统（应用、WhatsApp 网关、数据库）可部署在用户自己的 VPS 上，数据不经过项目方服务器。
- **多租户支持**：面向需要为多个客户或业务单元隔离数据的场景，提供多租户架构。
- **MCP-ready**：支持 Model Context Protocol，便于将外部工具与数据源接入 AI 智能体的能力范围。
- **合规与许可**：项目以 MIT 许可发布，并在设计上考虑 LGPD 相关要求。

## 技术架构

项目主要使用 TypeScript 开发，前端与全栈框架基于 Next.js，数据层采用 Supabase。WhatsApp 通信层通过 WAHA 实现，将 WhatsApp 会话以 HTTP API 形式暴露给应用层，从而让 AI 智能体与 CRM 逻辑能够消费和响应消息。

架构上的几个关键设计点：

- **自托管优先**：官方提供 `hostgator-setup-kit/` 安装套件，与 HostGator 合作，可通过单条命令在 VPS 上部署完整栈（应用 + WhatsApp + 数据库），并配有生产环境 runbook 文档。
- **多租户**：在数据模型与访问控制层面支持租户隔离，适用于服务商或集团型组织。
- **MCP-ready**：AI 智能体的工具调用与上下文扩展遵循 MCP 思路，便于对接第三方系统。
- **CI 与工程化**：仓库配置了 GitHub Actions 工作流（ci.yml），对代码质量与构建流程进行持续验证。

## 安装与使用

项目主推的安装路径是在 VPS 上部署。基本流程如下（具体命令以仓库文档为准）：

1. 准备一台 VPS（官方与 HostGator 有合作套餐，并提供折扣链接）。
2. 获取仓库代码：
   ```bash
   git clone https://github.com/melgarafael/DeskcommCRM.git
   cd DeskcommCRM
   ```
3. 使用 `hostgator-setup-kit/` 中的安装脚本，一条命令完成应用、WhatsApp 网关与数据库的部署。
4. 参照 `docs/runbooks/waha-hostgator.md` 完成生产环境配置，包括 WAHA 的 WhatsApp 连接与 Supabase 相关环境变量。
5. 启动后登录 CRM，配置 AI 智能体与销售流程，并将会话渠道指向已连接的 WhatsApp 实例。

最小可用示例可以理解为：完成部署并连上 WhatsApp 后，创建一个 AI 智能体、绑定一条销售管道，让智能体接管新进对话并生成对应的联系人与商机记录。仓库 README 提供葡萄牙语、英语和西班牙语三种版本，详细步骤以 README 与 `ARCHITECTURE.md` 为准。

## 适用场景

- **WhatsApp 驱动的销售团队**：所有客户沟通集中在 WhatsApp，需要用 AI 做首轮接待与线索筛选，同时把商机沉淀到 CRM 中跟进。
- **中小企业客服与售前自动化**：希望以较低成本替代按坐席或按功能计费的商业 SaaS。
- **多客户/多品牌服务商**：需要多租户隔离，为不同客户分别管理对话、数据与 AI 智能体配置。
- **数据合规敏感型业务**：因 LGPD 或其他合规要求，倾向将客户数据保留在自有基础设施上。

## 项目亮点

与 Kommo、Octadesk、Intercom 等商业产品相比，DeskcommCRM 的差异点在于：开源且 MIT 许可、无订阅费、无功能分级锁定、数据完全自托管。与一般的开源自托管 CRM 相比，它的特点是 AI 智能体是原生能力而非外挂插件，并且直接围绕 WhatsApp 这一销售主渠道构建，同时提供多租户与 MCP 支持。官方与 HostGator 合作的单命令部署套件，也降低了自托管方案常见的运维门槛。项目在 GitHub 上已有约 1,464 个 star，并保持活跃增长。

## 相关链接

- [GitHub 仓库](https://github.com/melgarafael/DeskcommCRM)
- [项目愿景 VISION.md](https://github.com/melgarafael/DeskcommCRM/blob/main/VISION.md)
- [架构说明 ARCHITECTURE.md](https://github.com/melgarafael/DeskcommCRM/blob/main/ARCHITECTURE.md)
- [贡献指南 CONTRIBUTING.md](https://github.com/melgarafael/DeskcommCRM/blob/main/CONTRIBUTING.md)
- [生产环境 Runbook（WAHA + HostGator）](https://github.com/melgarafael/DeskcommCRM/blob/main/docs/runbooks/waha-hostgator.md)
