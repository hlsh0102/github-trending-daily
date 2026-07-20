---
tags:
  - trending
  - article
repo: PostHog/posthog
date: 2026-07-20
language: Python
stars_total: 37003
stars_today: 411
---
## 项目概述

PostHog 是一个开源的、面向产品开发全生命周期的数据分析与洞察平台。其核心理念是“构建自动驾驶产品（self-driving products）”——通过整合用户行为分析、会话回放、功能开关、A/B 测试、错误追踪、日志管理以及 AI 可观测性等一系列开发者工具，帮助团队自动诊断问题、发现增长机会并快速修复缺陷。目标用户覆盖产品经理、工程师、数据科学家及运营人员，尤其适合需要自托管、重视数据隐私且希望拥有高度可定制工具栈的团队。

## 核心功能

- **产品分析**：提供事件追踪、漏斗分析、留存分析、路径分析等标准功能，支持自定义看板和实时数据展示。
- **会话回放**：录制并回放用户操作流程，结合控制台日志与网络请求，精准定位界面交互问题。
- **功能开关与 A/B 测试**：支持灰度发布、百分比实验和多变量测试，帮助安全迭代产品功能。
- **错误追踪**：自动捕获前端与后端异常，关联用户会话与上下文环境，快速复现并定位根因。
- **日志管理**：集中收集、搜索与可视化应用日志，支持结构化查询与告警配置。
- **AI 可观测性**：提供机器学习模型请求追踪、提示性能监控与智能异常检测，覆盖 AI 应用从实验到上线的全链路。

## 技术架构

PostHog 采用模块化的微服务架构，后端主力使用 Python（基于 Django 框架）与 Go（用于高性能数据处理），前端使用 React 与 TypeScript。其设计特点包括：

- **自托管优先**：提供 Docker Compose 与 Kubernetes 部署方案，用户可将全部数据保留在自有基础设施上，无外部 API 依赖。
- **事件驱动管道**：通过 Apache Kafka 与 ClickHouse 构建实时数据处理引擎，支持海量事件（每秒数万量级）的并行写入与查询。
- **插件生态系统**：支持通过自定义插件（Python 编写）扩展数据接入、转换与导出能力，例如与 Snowflake、BigQuery、Slack 等外部系统集成。
- **多通道交互**：提供 Web 界面、桌面客户端（Electron）、Slack 机器人及 MCP（Model Context Protocol）接口，满足不同工作流的操作需求。

## 安装与使用

### 快速体验（Docker）

```bash
git clone https://github.com/PostHog/posthog.git
cd posthog
docker compose -f docker-compose.dev.yml up
```

访问 `http://localhost:8000` 即可进入管理后台。首次启动后，需通过 `bin/createuser` 命令创建管理员账户。

### 最小使用示例

在应用中嵌入 PostHog 的 JavaScript 追踪代码（支持 npm 包或 CDN 方式）：

```js
import posthog from 'posthog-js'

posthog.init('YOUR_API_KEY', { 
  api_host: 'https://your-instance.com' 
})

// 追踪事件
posthog.capture('signup_completed', { 
  plan: 'premium', 
  referral_source: 'twitter' 
})
```

通过上述代码，即可将用户行为事件实时发送至自托管实例并进行可视化分析。

## 适用场景

- **SaaS 产品团队**：需要掌握用户留存路径、发现功能死点并快速验证实验假设的创业公司或成熟企业。
- **重视数据隐私的组织**：受 GDPR、CCPA 等法规约束，或与敏感行业（金融、医疗）相关，需要将分析数据完全部署在内部环境。
- **全栈开发者为主的小团队**：希望用单一工具替代 Mixpanel、Amplitude、Sentry、LogDNA 等多家服务，降低运维复杂度与成本。
- **AI 驱动的产品团队**：正在开发基于 LLM 的应用，需要监控请求质量、诊断幻觉问题并优化提示策略。

## 项目亮点

- **开源替代**：提供与商业分析平台（如 Amplitude、Hotjar）对等的功能，但完全开源（MIT 许可证），无用户席位或数据量限制。
- **端到端协同**：将分析、会话、实验、错误日志等数据打通在同一平台中，避免跨系统切换的上下文中断。
- **全生命周期覆盖**：从功能设计（A/B 测试）到上线监控（错误追踪及日志），再到后期优化（AI 可观测性），形成闭环。
- **极低的集成门槛**：支持十几种语言的 SDK（JavaScript、Python、iOS、Android 等），并提供自动发现型的插件与 Webhook。
- **强大的社区与文档**：拥有活跃的贡献者社区（超过 1500 位贡献者）、详尽的官方文档及视频教程，企业级支持选项完备。

## 相关链接

- [GitHub 仓库](https://github.com/PostHog/posthog)
- [官方文档](https://posthog.com/docs)
- [社区论坛](https://posthog.com/community)
- [产品路线图](https://posthog.com/roadmap)
