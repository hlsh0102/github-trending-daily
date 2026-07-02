---
tags:
  - trending
  - article
repo: diegosouzapw/OmniRoute
date: 2026-07-02
language: TypeScript
stars_total: 9763
stars_today: 1010
---
## 项目概述

OmniRoute 是一个免费的开源 AI 网关，它通过一个统一的端点，将 236 家 AI 服务提供商（其中超过 50 家完全免费）的模型能力聚合起来。无论是 Claude Code、Codex、Cursor、Cline 还是 Copilot，都可以通过这一个入口接入免费的 Claude、GPT、Gemini 等模型。项目解决了开发者在多工具、多模型之间反复切换和配置 API 的痛点，同时也让免费模型的获取和使用变得更加便捷。目标用户包括 AI 应用的开发者、使用 AI 辅助编码工具的开发者，以及希望低成本探索多种模型能力的团队和个人。

## 核心功能

- **200+ 提供商统一接入**：单一路由端支持 236 家 AI 服务提供商，涵盖付费和免费模型，无需为每个工具单独配置 API Key。
- **50+ 完全免费的提供商**：从超过 50 家提供商处获取免费的 AI 模型推理，每月可聚合约 1.6B 免费 token，首月注册后可达约 2.1B。
- **RTK + Caveman 智能压缩**：两种压缩技术联动，可在保持语义的同时节省 15% 到 95% 的 token 消耗，显著降低成本并提升效率。
- **智能自动回退（Auto-fallback）**：当首选模型不可用时（如超量、限流、服务中断），自动切换到备用提供商，确保服务不间断。
- **多协议支持**：兼容 MCP（Model Context Protocol）和 A2A（Agent-to-Agent），可服务于复杂的多智能体工作流和工具调用场景。
- **多模态 API 支持**：除了文本，还支持图像、音频等多模态模型的调用，满足更丰富的 AI 应用需求。
- **桌面端与 PWA 支持**：提供桌面应用和渐进式网页应用（PWA），便于在不同设备上使用和管理。

## 技术架构

OmniRoute 使用 TypeScript 开发，具备良好的类型安全性和跨平台能力。其核心架构围绕统一的请求路由层设计，接收到来自任意 AI 工具的请求后，根据用户配置的选择策略（如首选提供商、备用列表、成本优先级）动态路由到相应的模型端点。压缩层基于 RTK（Retokenization）和 Caveman 算法，在代理层对输入输出进行无损或近无损的 token 缩减，减少与 API 的通信数据量。自动回退机制通过心跳检测和超时管理实时监控提供商状态，当检测到失败时立即切换至预设的备用提供商。网关还内置了请求排队、限流、日志审计等功能，适合生产环境的稳定使用。

## 安装与使用

OmniRoute 提供多种部署方式，包括 Docker、Node.js 直接运行以及桌面端 PWA。

**使用 Docker 快速启动（推荐）**

```bash
docker run -d --name omniroute -p 3000:3000 omniroute/omniroute:latest
```

启动后，访问 `http://localhost:3000` 即可看到仪表盘界面，进行初始配置。

**从源码运行**

```bash
git clone https://github.com/diegosouzapw/OmniRoute.git
cd OmniRoute
npm install
cp .env.example .env   # 编辑 .env 配置你的 API Key 等参数
npm run dev
```

**最小可用示例**

配置完成后，任何支持自定义 API 端点的 AI 工具都可以将请求指向：
```
http://localhost:3000/v1/chat/completions
```

以 cURL 为例：

```bash
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_omniroute_key" \
  -d '{
    "model": "free/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, OmniRoute!"}]
  }'
```

在模型名称中指定 `free/` 前缀即可使用免费提供商池。

## 适用场景

- **AI 辅助编码工具的统一后端**：将 Cursor、Claude Code、Codex、Cline 等工具的 API 请求全部路由到 OmniRoute，节省为每个工具单独申请和配置不同提供商 API 的时间和成本。
- **低成本 AI 应用原型开发**：在开发阶段使用超过 50 家免费提供商进行测试和迭代，大幅降低推理成本，待应用成熟后再切换到付费的大模型。
- **多模型对比与 A/B 测试**：团队需要评估不同模型的推理质量、延迟和成本时，通过 OmniRoute 可以快速切换模型或在多个提供商间自动分配请求。
- **高可靠的 AI 服务层**：在生产环境中配置自动回退机制，当主流模型服务商出现问题（如限流、故障）时，自动切换到备用提供商，保证业务连续性。

## 项目亮点

- **最低的免费推理门槛**：聚合超过 50 家免费提供商的 token 额度，首月可用约 2.1B 免费 token，是目前市面上覆盖最广的免费 AI 网关之一。
- **独创的 token 压缩技术**：RTK + Caveman 组合压缩不是简单的词频缩减，而是通过重分词的方式在保留语义的前提下削减 token 数，最高可节省 95% 的消耗，这在行业内较为少见。
- **极简的迁移成本**：现有工具只需要修改 API 端点地址即可接入 OmniRoute，无需修改任何代码或学习新的 API 接口。
- **开源且社区驱动**：项目采用 MIT 许可证，社区活跃，提供 Discord、Telegram、WhatsApp 等多渠道支持，路线图由用户反馈驱动。
- **全平台兼容**：不仅支持传统的服务器部署，还提供桌面端和 PWA，让开发者可以在任何设备上使用。

## 相关链接

- [GitHub 仓库](https://github.com/diegosouzapw/OmniRoute)
- [Discord 社区](https://discord.gg/EkzRkpzKYt)
- [Telegram 频道](https://t.me/omnirouteOficial)
- [WhatsApp 全球群](https://chat.whatsapp.com/JI7cDQ1GyaiDHhVBpLxf8b?mode=gi_t)
- [WhatsApp 巴西群](https://chat.whatsapp.com/BTGJXIyjeNIIgExvTMGGhI)
