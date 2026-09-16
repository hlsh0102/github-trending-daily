---
tags:
  - trending
  - article
repo: melgarafael/DeskcommCRM
date: 2026-09-16
language: TypeScript
stars_total: 2972
stars_today: 193
---
## 项目概述

DeskcommCRM 是一个开源的 AI 销售操作系统（AI Sales OS），本质上是把 CRM、AI 智能体和 WhatsApp 即时通讯渠道整合在同一个自托管平台上。项目面向那些主要通过聊天工具完成销售转化的业务，例如中小型电商、服务型工作室、教育机构和代理商团队。

传统 SaaS CRM（如 Kommo、Octadesk、Intercom）通常按坐席收取月费，AI 功能往往被打包在高价套餐中，且客户数据存放在服务商侧。DeskcommCRM 试图解决三个具体问题：一是降低持续订阅成本，二是把数据主权交还给企业，三是让 AI 智能体直接参与售前咨询、线索资格判断与成交推进，而不只是一个被动的记录工具。项目采用 MIT 许可证，使用 TypeScript 编写，并明确以 LGPD（巴西通用数据保护法）合规为设计前提之一。

## 核心功能

- **原生 AI 智能体**：内置可配置的 AI 代理，能够在 WhatsApp 对话中自动应答、澄清需求、判断线索质量，并将符合条件的线索推进到销售流程的下一阶段。
- **WhatsApp 集成（基于 WAHA）**：通过 WAHA（WhatsApp HTTP API）接入 WhatsApp，无需依赖官方 Business API 的复杂审批流程，适合希望快速上线聊天销售的中小团队。
- **多租户架构**：同一套部署可以服务多个组织或业务单元，各租户之间的数据与配置相互隔离，适合代理商或集团型团队统一运维。
- **MCP 就绪**：支持 Model Context Protocol，便于将外部工具、数据源或自定义 AI 能力以标准化方式挂载到智能体上，扩展对话能力。
- **自托管与一体化部署**：官方提供 `hostgator-setup-kit/` 安装套件，可在单台 VPS 上一条命令部署应用、WhatsApp 通道与数据库，不需要额外维护多套基础设施。
- **LGPD 取向的数据处理**：从架构层面考虑数据驻留与合规要求，数据存放在用户自己的服务器上，减少跨境与第三方托管带来的合规负担。

## 技术架构

项目以 TypeScript 为主语言，前端与全栈框架使用 Next.js，数据层与认证、实时能力依托 Supabase（PostgreSQL + 实时订阅 + 行级安全策略）。WhatsApp 通道由 WAHA 负责，将 WhatsApp Web 协议封装为 HTTP 服务，由 CRM 后端调用。AI 智能体部分围绕 MCP 协议设计，使模型与工具之间保持松耦合，便于替换底层模型或增加新的业务工具。

整体部署形态偏向“单机一体化”：应用进程、WAHA 服务和数据库可以共存于同一台 VPS，降低了运维复杂度，也符合项目面向中小团队和自托管场景的定位。多租户通过 Supabase 的隔离机制实现，仓库中提供 CI 工作流，说明项目对代码质量与自动化验证有一定要求。

## 安装与使用

官方推荐路径是使用 HostGator 合作提供的安装套件，在 VPS 上完成一次性部署：

1. 准备一台可用的 VPS（官方合作方案针对 HostGator，但理论上任何支持 Docker 的 Linux 主机均可）。
2. 克隆仓库并进入安装目录：

   ```bash
   git clone https://github.com/melgarafael/DeskcommCRM.git
   cd DeskcommCRM/hostgator-setup-kit
   ```

3. 按套件内的说明配置环境变量（数据库连接、Supabase 密钥、WAHA 凭据等），然后执行安装脚本，脚本会拉起应用、WAHA 和数据库。
4. 安装完成后访问分配给你的域名，创建管理员账户与首个租户。
5. 在后台绑定 WhatsApp 号码，配置 AI 智能体的提示词、可用工具和转人工规则，即可开始接收与处理对话。

对于本地开发，可参考仓库中 README 与 `ARCHITECTURE.md` 的说明，自行启动 Next.js 开发服务器与 Supabase 本地实例。最小可用示例即“一个租户 + 一个 WhatsApp 号码 + 一个默认 AI 智能体”，足以验证从消息进入到线索创建的完整链路。

## 适用场景

- **以 WhatsApp 为主要销售渠道的中小商家**：希望在聊天中完成咨询、报价与跟进，而不额外购买 SaaS CRM 席位。
- **代理商与多品牌运营团队**：需要在一套系统内管理多个客户或品牌的销售对话，并保持数据隔离。
- **对数据主权有要求的企业**：因 LGPD 或内部合规政策，不能将客户对话与线索数据存放在第三方云服务上。
- **希望试验 AI 销售流程的技术团队**：想基于 MCP 自定义智能体行为、接入自有工具或模型，而不受闭源平台限制。

## 项目亮点

与 Kommo、Octadesk、Intercom 等商业产品相比，DeskcommCRM 的差异点主要在三个方向。其一是完全自托管与 MIT 许可，没有功能锁定和席位月费，企业只需承担服务器成本。其二是 AI 智能体被放在销售流程的核心位置，而不仅是客服辅助，配合 MCP 可以持续扩展能力边界。其三是部署体验被刻意简化，通过与合作方提供的安装套件，把应用、WhatsApp 通道和数据库整合为一条命令的安装流程，降低了自托管 CRM 常见的上手门槛。项目在 GitHub 上已有近 3000 星标，说明它在“开源 + WhatsApp + AI 销售”这一细分方向上获得了实际关注。

## 相关链接

- [GitHub 仓库](https://github.com/melgarafael/DeskcommCRM)
- [HostGator VPS 合作方案](https://www.hostgator.com.br/52708-141-3-52.html)
- 仓库内文档：`VISION.md`、`ARCHITECTURE.md`、`CONTRIBUTING.md`、`docs/runbooks/waha-hostgator.md`
