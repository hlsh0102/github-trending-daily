---
tags:
  - trending
  - article
repo: diegosouzapw/OmniRoute
date: 2026-07-23
language: TypeScript
stars_total: 25685
stars_today: 1651
---
## 项目概述

OmniRoute 是一个开源的 AI 网关项目，旨在解决开发者在调用多种 AI 模型时面临的碎片化问题。它通过一个统一的 API 端点，聚合了 278 家 AI 提供商（其中 90 余家提供免费额度）、超过 500 个模型，每月可提供约 15.3 亿免费 Token 的预算。项目目标用户是 AI 应用开发者、提示工程师以及需要将 Claude、GPT、Gemini 等多种模型集成到工作流中的技术团队。OmniRoute 完全免费且采用 MIT 许可证，由超过 500 名贡献者共同维护。

## 核心功能

- **统一端点与多提供商聚合**：一个 API 端点对接 278 家 AI 提供商，包括 Kimi、Claude、GPT、OpenAI、Gemini、GLM、DeepSeek、MiniMax 等，覆盖 500+ 模型。
- **免费额度智能管理**：聚合 43 个提供商池、460+ 模型的文档化免费额度，在仪表盘上实时显示可用预算，经去重后每月稳定提供约 15.3 亿免费 Token。
- **配额感知自动回退**：当当前提供商触发速率限制或配额耗尽时，自动将请求回退到备选提供商，确保服务不中断。
- **高性能 Token 压缩**：结合 RTK（Real-Time Knowledge）和 Caveman 堆叠压缩技术，可节省 15–95% 的 Token 消耗（平均约 89%），显著降低成本。
- **多协议支持**：兼容 Claude Code、Codex、Cursor、OpenCode、Cline 以及 Copilot 等流行工具，支持 MCP（Model Context Protocol）和 A2A（Agent-to-Agent）通信。
- **可观测性与桌面端支持**：提供实时仪表盘（/dashboard/free-tiers）展示免费额度状态，同时提供桌面 PWA 应用版本。

## 技术架构

OmniRoute 基于 TypeScript 开发，采用模块化架构设计。核心组件包括：

- **提供商适配层**：每个提供商有独立的适配器，处理认证、速率限制、错误重试等逻辑。这些适配器统一对外暴露标准接口，使得新增提供商只需编写适配器代码。
- **回退引擎**：基于配额感知的智能路由，维护每个提供商的使用状态。当请求失败（如 429 限流或 403 配额不足）时，引擎按优先级顺序执行自动回退，负载均衡策略可配置。
- **Token 压缩管线**：在请求发送前，压缩管线将用户输入通过 RTK（剪枝无关上下文）和 Caveman（语义压缩）进行两级优化，显著减少发送给模型的实际 Token 数。压缩率因模型和上下文而异。
- **仪表盘与统计模块**：前端基于 React 构建，后端统计模块聚合来自各提供商的配额信息，经过去重计算后展示。所有数据存储在内存或可选的持久化后端中。
- **架构特点**：设计上强调零依赖集成——用户无需安装额外 SDK，只需配置一个环境变量并指向 OmniRoute 端点即可。同时，项目遵循“诚实计数”原则，每一个免费额度都基于文档化的速率限制计算，避免了虚标。

## 安装与使用

### 快速开始

1. **克隆仓库**
```bash
git clone https://github.com/diegosouzapw/OmniRoute.git
cd OmniRoute
```

2. **安装依赖**
```bash
npm install
```

3. **配置环境变量**
创建 `.env.local` 文件，参考 `.env.example` 填入你需要使用的提供商 API 密钥（例如 `OPENAI_API_KEY`、`ANTHROPIC_API_KEY` 等）。如果使用免费额度，通常无需配置密钥。

4. **启动服务**
```bash
npm run dev
```

服务默认运行在 `http://localhost:3000`。

### 最小可用示例

在任意支持 HTTP 请求的客户端中，直接调用 `/api/chat/completions` 端点：

```bash
curl http://localhost:3000/api/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

OmniRoute 会自动匹配可用的提供商，如果配置了多个密钥，则会按策略选择最优路径。如需强制使用某个提供商，可在请求中添加 `x-provider` 头部。

## 适用场景

- **AI 辅助编程环境**：与 Claude Code、Cursor 或 Copilot 配合使用，将代码补全、解释、重构等需求路由到免费或低成本的模型，降低企业 AI 工具订阅成本。
- **多模型轮询与压力测试**：在开发 AI 产品时，需要对不同提供商进行对比测试。OmniRoute 允许通过统一端点快速切换模型，并自动规避速率限制，提高测试效率。
- **Token 敏感型应用**：对于需要处理长上下文或高频调用的场景（如客服机器人、文档分析），利用内置的 Token 压缩功能可以显著降低 API 费用。
- **学习与原型验证**：个人开发者或学生可以利用聚合的免费额度（每月 15.3 亿 Token）进行 AI 技术探索，无需付费即可实验多种模型。

## 项目亮点

- **极致免费额度**：相比其他聚合网关（如 LiteLLM、OpenRouter），OmniRoute 专注于挖掘和聚合免费额度，并提供实时的、诚实去重的预算面板。
- **零学习成本**：与现有工具无缝兼容，无需改变代码即可切换提供商。配置复杂度远低于同类项目。
- **强健的自动回退**：在层叠限流、密钥轮换、提供商故障等场景下，自动回退机制保证了服务的持续可用，尤其适合生产环境。
- **开源社区驱动**：500+ 贡献者持续添加新提供商和优化特性，社区活跃度高，问题响应迅速。

## 相关链接

- [GitHub 仓库](https://github.com/diegosouzapw/OmniRoute)
