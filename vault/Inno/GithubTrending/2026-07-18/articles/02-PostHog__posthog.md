---
tags:
  - trending
  - article
repo: PostHog/posthog
date: 2026-07-18
language: Python
stars_total: 36257
stars_today: 438
---
## 项目概述

PostHog 是一个开源的、面向产品团队的一站式数据分析与行为洞察平台。该项目旨在帮助团队“构建自动驾驶型产品”——即让产品能自动发现用户行为模式、诊断问题并引导优化决策。与传统的产品分析工具不同，PostHog 提供从用户行为追踪、会话回放到实验管理和功能开关的完整工具链，支持自托管（Self‑Hosted）和云端部署两种方式。

该项目主要面向产品经理、工程师和数据团队的成员，帮助他们替代商业工具如 Amplitude、Hotjar、LaunchDarkly 或 FullStory 的混合使用。PostHog 强调数据隐私和可扩展性，用户可完全控制自己的数据基础设施。

## 核心功能

- **AI 可观测性 (AI Observability)**：追踪 AI 模型的请求、延迟和错误，为构建代理型应用提供上下文诊断能力。
- **用户行为分析**：支持自动捕捉事件（Pageview、Click、Custom Events）并生成漏斗、留存、趋势等分析报表。
- **会话回放 (Session Replay)**：录制并回放用户真实浏览过程，支持过滤和标记关键交互，方便定位用户体验问题。
- **功能开关 (Feature Flags)**：通过灰度发布、A/B 测试实现渐进式功能发布，并支持基于用户属性或随机分组的动态开关逻辑。
- **实验管理 (Experiments)**：内置实验引擎，支持统计分析（如贝叶斯或频率学派），自动计算显著性并生成结果报告。
- **错误追踪与日志管理**：捕获前端和后端错误，并关联到用户会话，同时提供日志查询与归因功能。

## 技术架构

PostHog 采用微服务与单体应用相结合的混合架构，核心后端使用 Python (Django) 编写，前端基于 React/TypeScript 构建。系统主要包含以下组件：

- **PostHog App**：Django 应用提供 REST API 和后台管理界面，负责事件消费、用户画像计算、插件管理等。
- **ClickHouse**：作为分析型数据库，用于存储海量事件数据并支撑高性能的漏斗、留存等聚合查询。
- **Kafka / PostgreSQL**：采用 Kafka 作为事件缓冲层接收异步写入，PostgreSQL 则用于存储元数据（如用户属性、组织配置）。
- **Pydantic 与 AsyncIO**：在数据处理流水线中使用 Pydantic 进行 schema 验证，并利用 asyncio 实现高效的事件摄取。
- **部署灵活性**：支持 Docker Compose 一键部署（All‑in‑One 模式），也提供 Helm Chart 用于 Kubernetes 集群部署，适配从单机测试到生产规模。

这种架构设计允许 PostHog 在不牺牲查询性能的前提下，处理亿级事件量，同时通过插件系统支持与 Slack、Zapier 等外部工具集成。

## 安装与使用

PostHog 提供多种安装方式，最推荐的生产部署方式为自托管 (Self‑Host)。

### 快速安装（本地开发/小规模测试）

```bash
git clone https://github.com/PostHog/posthog.git
cd posthog
cp env.example .env
docker compose up -d
```

访问 `http://localhost:8000` 即可进入管理后台，注册后通过前端代码中的 `window.posthog.init('YOUR_API_KEY', ...)` 开始发送事件。

### 最小可用示例（Python）

安装 PostHog Python SDK：

```bash
pip install posthog
```

在代码中初始化并发送事件：

```python
import posthog

posthog.project_api_key = 'YOUR_API_KEY'
posthog.host = 'https://app.posthog.com'  # 或自托管地址

# 捕获事件
posthog.capture('user_distinct_id', 'event_name', properties={'plan': 'pro'})
# 识别用户属性
posthog.identify('user_distinct_id', {'email': 'user@example.com'})
```

对于 React 前端，可使用提供的 NPM 包 (`posthog-js`) 实现自动页面跟踪和会话录制。

## 适用场景

- **SaaS 产品迭代优化**：产品经理可通过漏斗分析发现用户流失点，配合会话回放还原操作细节，并利用实验引擎验证新功能效果。
- **AI/ML 应用监控**：开发团队能追踪模型调用频率、错误类型和推理延迟，将 AI 行为纳入整体产品分析体系。
- **增长黑客与 A/B 测试**：营销团队使用功能开关实现分地域或分用户群的实验，结合统计结果快速决策。
- **中小团队替代商业工具栈**：用单一开源平台替换多个商业服务（如 Amplitude + Hotjar + LaunchDarkly），降低数据隐私合规风险与费用。

## 项目亮点

- **开源且不限制功能**：与许多“开源版”功能受限的项目不同，PostHog 的核心功能（包括自托管）完全免费开放，无隐藏付费墙。
- **AI 原生集成**：率先推出 AI 可观测性，将大模型行为纳入产品分析范畴，适合构建智能代理类应用的团队。
- **数据主权与合规**：自托管部署允许用户将数据保留在自己的基础设施中，满足 GDPR、HIPAA 等合规要求。
- **活跃的社区与插件生态**：拥有超过 80 个可安装的插件（如 Slack、Mixpanel、Zapier），且社区贡献者极为活跃，Bug 修复和功能迭代速度远超同类闭源产品。

## 相关链接

- [GitHub 仓库](https://github.com/PostHog/posthog)
- [官方文档](https://posthog.com/docs)
- [社区论坛](https://posthog.com/community)
- [Roadmap](https://posthog.com/roadmap)
