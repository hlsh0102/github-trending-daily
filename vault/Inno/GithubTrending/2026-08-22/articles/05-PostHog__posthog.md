---
tags:
  - trending
  - article
repo: PostHog/posthog
date: 2026-08-22
language: Python
stars_total: 38314
stars_today: 335
---
## 项目概述

PostHog 是一个开源的产品分析平台，旨在帮助团队构建“自动驾驶”型产品。它通过整合多种开发者工具，在统一的数据基础上提供 AI 可观测性、产品分析、会话回放、功能开关、实验评估、错误跟踪和日志管理等功能。无论您使用的是 Web、移动端还是 AI 应用，PostHog 都能捕获完整的用户行为与系统上下文，帮助团队诊断问题、发现机会并快速发布修复。

PostHog 解决了传统分析工具数据孤岛、调试链路冗长、难以统一管理遥测数据等痛点。它适合产品经理、工程师、数据团队以及 AI 应用开发者使用，尤其适用于需要快速迭代、高度关注用户体验和系统稳定性的技术团队。

## 核心功能

- **产品分析**：提供事件追踪、漏斗分析、趋势分析、留存分析等基础产品数据的可视化洞察。
- **会话回放**：录制并回放用户真实操作，帮助团队直观理解用户行为，复现问题。
- **AI 可观测性**：专为 AI 应用设计，跟踪模型调用、Token 用量、提示词与响应，支持调试与成本监控。
- **功能开关**：支持按用户、按流量百分比等条件动态开启或关闭功能，实现灰度发布与定向测试。
- **实验评估**：内置 A/B 测试框架，无需额外集成即可创建实验并评估版本效果。
- **错误跟踪与日志**：自动捕获前端异常与后端日志，关联会话与用户，提升故障排查效率。

## 技术架构

PostHog 采用模块化、事件驱动的架构设计。核心数据处理基于 Python（使用 Django 框架）构建，后端服务依赖 PostgreSQL 存储业务数据，使用 ClickHouse 作为高性能的分析型数据库，以支持大规模事件数据的快速写入与查询。

项目采用活动记录（event-based）数据模型，所有分析能力建立在统一的事件流之上。前端使用 React 构建交互界面，并提供丰富的 REST API 及多种语言（JavaScript、Python、Node.js、Go 等）的 SDK 用于数据采集。此外，PostHog 支持通过 Slack、Web、桌面客户端以及 MCP（Model Context Protocol）接口进行控制与访问，使得团队可以在多种工作流中轻松集成。

其架构思路强调开箱即用与服务端自托管两种模式的灵活性。系统设计允许从单体应用平滑扩展到微服务集群，适合从小团队到大型组织的不同规模部署。

## 安装与使用

PostHog 支持云端一站式服务，也提供本地部署选项。以下为 Docker 本地快速安装示例：

```bash
# 克隆仓库
git clone https://github.com/PostHog/posthog.git
cd posthog

# 使用 Docker Compose 启动
docker-compose up -d
```

访问 `http://localhost:8000` 完成初始账号配置。若使用命令行启用全部功能，可运行：

```bash
python manage.py migrate
python manage.py createsuperuser
```

安装完成后，可通过 SDK 快速接入数据。例如，在 JavaScript 项目中：

```javascript
import posthog from 'posthog-js'

posthog.init('your-project-api-key', {
  api_host: 'http://localhost:8000',
  autocapture: true
})

// 发送自定义事件
posthog.capture('user_signed_up', { email: 'user@example.com' })
```

PostHog 还提供 Python、iOS、Android 等多端 SDK，支持告警与 API 集成，使用体验简单直观。

## 适用场景

- **AI 应用开发与调试**：监控模型调用、记录提示词与输入输出，量化延迟和成本，快速定位链路问题。
- **增长与留存的实验驱动**：产品团队可通过功能开关、A/B 测试评估新功能影响，基于会话回放理解用户真实行为。
- **多端产品统一分析**：将 Web、移动端、后端日志统一收集，构建跨平台用户行为全景视图，减少工具切换成本。
- **快速迭代与故障排除**：错误跟踪与日志关联，帮助工程师在几分钟内定位线上问题，并借助会话回放预览用户遭遇的具体上下文。

## 项目亮点

- **一体化平台**：PostHog 将分析、回放、实验、错误追踪等工具集于一身，避免数据隔离和重复建设，降低工具链复杂度。
- **开源与可自托管**：源代码完全开放，可私有化部署，保证数据安全与合规性，适合对数据掌控要求高的组织。
- **AI 原生支持**：在 AI 时代率先提供可观测性与调试功能，特别适应当前生成式 AI 应用的发展趋势。
- **极佳的交互体验**：界面现代、交互流畅，降低了非技术团队成员的使用门槛。
- **活跃的社区与迭代速度**：拥有大量贡献者和频繁的版本更新，BUG 修复与新特性持续演进。

## 相关链接

- [GitHub 仓库](https://github.com/PostHog/posthog)
- [官方文档](https://posthog.com/docs)
- [社区交流](https://posthog.com/community)
- [版本发布记录](https://posthog.com/changelog)
