---
tags:
  - trending
  - article
repo: PostHog/posthog
date: 2026-07-19
language: Python
stars_total: 36653
stars_today: 338
---
## 项目概述

PostHog 是一个面向构建自驱型产品的开发者平台。它提供了一套全面的工具集，覆盖 AI 可观测性、产品分析、会话回放、功能开关、A/B 实验、错误追踪、日志管理等功能。项目旨在帮助团队从产品中自动获取上下文信息，诊断问题、发现机会并快速修复。其目标用户包括产品经理、工程师、数据科学家以及任何需要理解产品用户行为、优化产品体验的团队。PostHog 强调自部署（self-hosted）和开源，提供了一个可替代多个商业 SaaS 工具的集成化方案。

## 核心功能

- **AI 可观测性**：监控和调试人工智能模型的行为与性能，追踪推理路径与决策过程。
- **产品分析**：提供事件追踪、用户属性、漏斗分析、留存分析等标准产品分析工具。
- **会话回放**：录制用户实际使用产品的屏幕操作流，帮助复现用户交互中的问题。
- **功能开关与实验**：支持功能灰度发布、A/B 测试以及实验配置，降低变更风险。
- **错误追踪与日志**：收集应用错误堆栈与日志，关联用户会话上下文，加速问题定位。
- **多渠道控制**：支持通过 Slack、Web 界面、桌面应用和 MCP（Model Context Protocol）进行管理操作，灵活调度。

## 技术架构

PostHog 后端主要采用 **Python**（Django） 和 **Go**（用于高性能数据处理），前端使用 **TypeScript**（React）和 **PostgreSQL** 作为主数据库。核心设计特点包括：

- **事件驱动架构**：所有用户交互和系统行为被抽象为事件流，支持实时处理与批处理。
- **可插拔存储**：支持将 ClickHouse 作为高性能分析引擎，用于处理大规模事件数据；也兼容 PostgreSQL 用于元数据存储。
- **自部署优先**：提供一键部署脚本（Docker Compose、Kubernetes）和云托管版本，确保数据主权与隐私合规。
- **模块化插件系统**：通过 插件 扩展数据导入/导出、告警、第三方集成能力，降低核心代码耦合度。
- **事件管道**：使用 Kafka 作为事件缓冲与路由中心，确保高吞吐与数据不丢失。

## 安装与使用

### 安装步骤（快速体验）

1. **环境要求**：Docker 与 Docker Compose（推荐）、Python 3.10+、Node.js 16+
2. **克隆仓库**：
   ```bash
   git clone https://github.com/PostHog/posthog.git
   cd posthog
   ```
3. **启动开发环境**：
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```
   首次启动会自动迁移数据库、编译前端，并启动一系列微服务。
4. **访问后台**：打开浏览器访问 `http://localhost:8000`，按照向导创建组织与项目。

### 最小可用示例（事件追踪）

在 Web 应用中引入 PostHog 的 JavaScript 库：

```javascript
// 安装: npm install posthog-js
import posthog from 'posthog-js';

posthog.init('your-project-api-key', { api_host: 'http://localhost:8000' });

// 追踪点击事件
document.querySelector('button').addEventListener('click', () => {
  posthog.capture('signup_button_clicked', { plan: 'premium' });
});
```

执行后，事件将出现在 PostHog 的“事件”面板中，可进一步用于漏斗分析或实验评估。

## 适用场景

- **产品用户体验优化**：通过会话回放与漏斗分析，识别用户流失节点并针对性改进。
- **功能灰度与 A/B 测试**：使用功能开关对特定用户群发布新功能，结合实验框架验证效果。
- **AI 模型调试**：监控 LLM 调用、向量搜索等 AI 行为的成功率和响应模式，排查异常。
- **一站式数据平台**：替代多个分离的工具（如 Google Analytics + Sentry + LaunchDarkly），降低集成成本与数据孤岛。

## 项目亮点

- **全栈开源**：核心代码完全开源（AGPL 许可），无隐藏的收费功能限制，社区活跃。
- **自部署原生**：数据不出企业网络，满足金融、医疗等强监管行业的合规需求。
- **集成度高**：一个平台覆盖分析、实验、监控、回放，免去多工具维护与数据标准化问题。
- **GitHub 活跃度**：超过 3.6 万星标，每日数百次提交与大量社区贡献，生态成熟。
- **易用性**：提供 SDK 覆盖主流框架（React、Vue、Node、Python、iOS、Android）以及无代码事件捕获。

## 相关链接

- [GitHub 仓库](https://github.com/PostHog/posthog)
- [官方文档](https://posthog.com/docs)
- [社区论坛](https://posthog.com/community)
- [产品路线图](https://posthog.com/roadmap)
- [为什么选择 PostHog](https://posthog.com/why)
