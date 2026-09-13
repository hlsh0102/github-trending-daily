---
tags:
  - trending
  - article
repo: melgarafael/DeskcommCRM
date: 2026-09-13
language: TypeScript
stars_total: 1919
stars_today: 504
---
## 项目概述

DeskcommCRM 是一个开源的 AI 销售操作系统（AI Sales OS），将自托管 CRM 与原生 AI 智能体、WhatsApp 消息通道整合在同一个系统中。项目以葡萄牙语社区为主要起点，同时提供英语和西班牙语版本，定位为 Kommo、Octadesk 和 Intercom 的开源替代方案，面向所有以聊天为主要销售渠道的企业。

它要解决的核心问题是：传统 SaaS CRM 通常按席位或功能模块收取月费，AI 能力被锁在更高价位的套餐里，且客户数据存放在服务商侧。DeskcommCRM 把 CRM、AI 智能体和 WhatsApp 接入整体部署到用户自己的服务器上，没有订阅费用，也没有被锁定在付费墙后的功能。目标用户包括中小企业销售团队、使用 WhatsApp 作为主要成交渠道的商家、需要数据自主可控的团队，以及希望基于开源代码做二次开发的技术团队。

## 核心功能

- **原生 AI 智能体**：内置可配置的 AI 智能体，能够在 WhatsApp 对话中完成接待、需求挖掘、线索资格判定（qualification）和推进成交，而非仅作为被动问答机器人。
- **WhatsApp 集成（基于 WAHA）**：通过 WAHA（WhatsApp HTTP API）接入 WhatsApp，使对话流直接进入 CRM 管道，与客户记录、销售阶段关联。
- **自托管 CRM**：完整的销售管道、线索与客户管理能力，部署在用户自己的 VPS 或服务器上，数据不经过第三方 SaaS。
- **多租户支持**：单一部署实例可服务多个组织或业务单元，适合代理商、集团型团队或 SaaS 场景。
- **MCP-ready**：遵循 Model Context Protocol，便于让外部 AI 工具或模型安全地调用系统能力，扩展智能体的行为边界。
- **LGPD 合规取向**：设计上考虑巴西《通用数据保护法》（LGPD）对数据存储与处理的要求，配合自托管模式降低合规风险。

## 技术架构

项目使用 TypeScript 作为主要开发语言，前端与全栈框架基于 Next.js，数据库与认证等后端能力构建在 Supabase 之上。WhatsApp 消息层通过 WAHA 独立运行，与主应用解耦，便于单独升级或替换。这种「应用 + WhatsApp 网关 + 数据库」的分层结构，使整体可以通过一条命令部署到 VPS。

项目在工程化上提供了一些配套文档与工具：`ARCHITECTURE.md` 描述整体架构，`VISION.md` 说明产品方向，`docs/runbooks/` 下有针对 HostGator 生产环境的运行手册。项目与 HostGator 合作提供了 `hostgator-setup-kit/`，用于在 VPS 上一键安装完整栈，CI 流程也已配置，说明项目对可重复部署和自动化有一定要求。多租户与 MCP 支持则表明其架构从一开始就考虑了隔离性与可扩展性，而不只是单店铺的聊天工具。

## 安装与使用

官方推荐路径是在 VPS 上进行生产部署。基本流程如下：

1. 准备一台满足要求的 VPS（HostGator 合作方案已提供安装套件与运行手册）。
2. 获取仓库代码并进入 `hostgator-setup-kit/` 目录，按套件说明执行一键安装命令，该命令会同时部署应用、WhatsApp 网关和数据库。
3. 配置环境变量，包括 Supabase 连接信息、WAHA 相关参数以及 AI 模型提供方的 API 密钥。
4. 启动服务后，登录 CRM 后台，创建租户、连接 WhatsApp 实例，并配置 AI 智能体的行为与销售流程。

最小可用示例可以理解为：完成部署后，向已连接的 WhatsApp 号码发送一条消息，AI 智能体自动应答并将其作为线索写入 CRM 管道——这条闭环即为系统的基本工作单元。由于仓库以自托管为主、辅以 HostGator 安装套件，具体命令与变量名请以仓库内 `hostgator-setup-kit/` 与运行手册的当前说明为准。

## 适用场景

- **WhatsApp 为主要成交渠道的中小企业**：把散落在个人手机上的客户对话收敛到统一的 CRM 管道中，并由 AI 智能体承担初步接待与筛选。
- **需要数据自主可控的团队**：因合规或商业机密原因，不愿将客户数据托管给第三方 SaaS 的企业，可通过自托管满足要求。
- **代理商与多业务集团**：借助多租户能力，用一套部署服务多个客户或业务线，降低运维成本。
- **希望二次开发的团队**：基于 MIT 许可和 TypeScript 代码库，按自身销售流程定制 AI 智能体行为或接入其他消息渠道。

## 项目亮点

与同类项目相比，DeskcommCRM 的差异化主要体现在三点。其一，它将 AI 智能体作为一等公民嵌入销售流程，而非在传统 CRM 上附加一个聊天插件，AI 的职责从「回答」延伸到「资格判定与销售推进」。其二，自托管 + 多租户 + LGPD 取向的组合，使其在数据主权敏感的市场中具备实用价值。其三，MCP-ready 的设计让系统可以更容易被外部 AI 工具调用和扩展，适应快速演进的智能体生态。MIT 许可也降低了商业使用的法律门槛。

## 相关链接

- [GitHub 仓库](https://github.com/melgarafael/DeskcommCRM)
- [VISION.md（项目愿景）](https://github.com/melgarafael/DeskcommCRM/blob/main/VISION.md)
- [ARCHITECTURE.md（架构说明）](https://github.com/melgarafael/DeskcommCRM/blob/main/ARCHITECTURE.md)
- [CONTRIBUTING.md（贡献指南）](https://github.com/melgarafael/DeskcommCRM/blob/main/CONTRIBUTING.md)
- [HostGator VPS 合作方案](https://www.hostgator.com.br/52708-141-3-52.html)
