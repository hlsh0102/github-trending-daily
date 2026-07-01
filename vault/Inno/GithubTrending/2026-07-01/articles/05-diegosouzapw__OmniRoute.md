---
tags:
  - trending
  - article
repo: diegosouzapw/OmniRoute
date: 2026-07-01
language: TypeScript
stars_total: 8812
stars_today: 387
---
## 项目概述

OmniRoute 是一个开源免费的 AI 网关项目，旨在解决开发者在使用多种 AI 模型时面临的 API 碎片化、配额限制和高昂成本问题。通过提供一个统一端点，OmniRoute 能够将 Claude Code、Codex、Cursor、Cline、Copilot 等主流 AI 工具连接到 236 个 AI 提供商，其中 50 多个提供商完全免费使用。项目核心价值在于“永不停止编码”——利用智能压缩和自动故障转移机制，确保开发者在任何模型限流或不可用时，工作流都能无缝切换至其他可用提供商。

目标用户群体包括：密集使用 AI 辅助编程工具的开发者、需要低成本或免费访问多种大语言模型的团队、以及希望简化 AI 服务集成的企业用户。

## 核心功能

- **统一网关，236 个提供商**：通过单一 API 端点接入 236 个 AI 模型提供商，覆盖 Claude、GPT、Gemini、Llama 等主流系列，其中 50 多个为永久免费提供商，无需额外订阅即可使用。
- **智能令牌压缩（节省 15–95% 成本）**：采用 RTK + Caveman 堆叠压缩技术，自动分析请求内容，在保证语义完整的前提下大幅减少 API 调用中的令牌消耗，实测最高可节省 95% 的令牌用量。
- **自动故障转移（Auto-fallback）**：当主用提供商限流、超时或不可用时，OmniRoute 自动将请求路由到备用提供商，确保开发工作流不中断。
- **多模态 API 支持**：不限于文本模型，支持图像生成、语音识别等多模态 AI 服务，通过同一网关统一调用。
- **MCP / A2A 兼容**：支持 Model Context Protocol 和 Agent-to-Agent 协议，可适配 Cline、Copilot 等 MCP 客户端，以及自定义 Agent 框架。
- **桌面端与 PWA 双形态**：提供桌面应用程序和渐进式 Web 应用两种使用方式，方便开发者在不同环境快速接入。

## 技术架构

OmniRoute 使用 TypeScript 构建，核心设计围绕三个关键原则：**兼容性、弹性、极致性价比**。

- **网关层抽象**：采用适配器模式，为每个 AI 提供商实现统一的 API 转换层，将不同提供商的请求/响应格式标准化为单一协议。用户只需在配置中指定目标模型和备用提供商，无需关心底层差异。
- **压缩引擎**：RTK（Real-Time Tokenization）实时计算令牌并优化提示词结构，Caveman 算法则通过移除冗余空格、注释、换行等方式暴力压缩，两者堆叠使用可在无损前提下大幅降低令牌数。
- **故障转移引擎**：维护一个提供商健康状态表，定期探测各提供商的可用性和响应延迟。当主路由失败时，按优先级从健康列表中选取下一个提供商重试，支持自定义重试次数和超时时间。
- **资源池管理**：后端持续跟踪各提供商的免费配额使用情况，在达到日限前自动切换至其他免费源，最大化利用每月约 16 亿免费令牌的聚合资源池。
- **轻量化部署**：项目提供 Docker 镜像和独立二进制文件，支持单节点部署，无需依赖外部数据库或消息队列，适合个人开发者或小团队快速搭建。

## 安装与使用

### 快速安装（Docker）

```bash
docker run -d \
  --name omniroute \
  -p 3000:3000 \
  -v $(pwd)/config:/app/config \
  ghcr.io/diegosouzapw/omniroute:latest
```

### 最小可用配置

创建 `config/omniroute.yml`：

```yaml
providers:
  - name: free-claude-hack
    provider: anthropic-free
    models: [claude-3-haiku]
    priority: 1
  - name: free-gpt-mirror
    provider: openrouter-free
    models: [gpt-4o-mini]
    priority: 2

fallback:
  enabled: true
  max_retries: 3

compression:
  rtk: true
  caveman: true
```

### 调用示例（兼容 OpenAI 格式）

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:3000/v1",
    api_key="your-omniroute-key"
)

response = client.chat.completions.create(
    model="claude-3-haiku",
    messages=[{"role": "user", "content": "写一个快速排序算法"}]
)

print(response.choices[0].message.content)
```

## 适用场景

- **AI 编程工具集成**：将 Claude Code、Codex、Cursor、Cline 等开发助手指向 OmniRoute，即可同时使用多个免费提供商，避免单一 API 配额耗尽导致编码中断。
- **多模型成本优化**：日常开发使用低价免费模型，复杂任务自动切换至高性能付费模型，压缩引擎进一步降低高频调用的令牌成本。
- **跨地区 AI 服务聚合**：针对不同区域延迟优化，自动选择最邻近或最低延迟的提供商，减少响应等待时间。
- **教育及个人项目**：学生、独立开发者无需购买多个 API 订阅，即可在项目中接入 GPT、Claude、Gemini 等多种模型进行实验和原型开发。

## 项目亮点

- **唯一聚合 50+ 永久免费提供商的统一网关**：大多数同类项目仅代理少数免费源，OmniRoute 深度挖掘并维护了一个不断更新的免费提供商列表，每个月可聚合约 16 亿免费令牌，相比直接使用官方 API 可节省 90% 以上成本。
- **独创堆叠压缩算法**：RTK + Caveman 的组合在业界中首创，实测在代码生成场景中可将令牌消耗降低 60–95%，远超标准提示词压缩工具的效果。
- **极简集成体验**：兼容 OpenAI SDK，现有代码无侵入式迁移；支持 Docker 一键部署，5 分钟内即可完成搭建。
- **活跃社区与快速迭代**：通过 Discord、Telegram、WhatsApp 三大社区渠道收集反馈，每周发布更新；在 GitHub 上已获得超过 8800 星标，日增长量持续攀升。

## 相关链接

- [GitHub 仓库](https://github.com/diegosouzapw/OmniRoute)
- [免费提供商文档](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/reference/FREE_TIERS.md)
- [加入 Discord 社区](https://discord.gg/EkzRkpzKYt)
- [Telegram 群组](https://t.me/omnirouteOficial)
