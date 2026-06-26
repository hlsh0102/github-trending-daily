---
tags:
  - trending
  - article
repo: every-app/open-seo
date: 2026-06-26
language: TypeScript
stars_total: 2675
stars_today: 57
---
## 项目概述

OpenSEO 是一款面向大众的开源 SEO 工具，旨在成为 Semrush 和 Ahrefs 等商业工具的免费替代品。对于许多个人站长、小型团队或自由职业者而言，传统的 SEO 工具不仅价格昂贵，而且功能臃肿。OpenSEO 采用按需付费的模式，用户只需支付底层 API 的实际调用费用，无需承担高额的订阅成本。此外，无论是个人手动操作，还是集成到 AI Agent 中，用户都能完全掌控自己的数据和工具链。

## 核心功能

- **核心 SEO 工作流**：提供现代、简洁的用户界面，专注于关键任务，如关键词研究、网站审计、反向链接分析等，避免功能冗余。
- **AI Agent 集成**：原生支持与 Claude Code、OpenClaw、Hermes 等 AI Agent 连接，可通过预置技能或自定义技能自动化执行 SEO 工作流。
- **MCP 协议支持**：内置 OpenSEO MCP 接口，允许开发者通过标准协议与 AI 代理交互，实现高度灵活的数据访问和操作。
- **技能市场**：包含预构建的 AI 技能，用户可直接使用；同时支持创建自定义技能，以满足特定的 SEO 策略和流程需求。
- **多数据源支持**：支持连接 DataForSEO API 和 Google Search Console，获取准确的搜索引擎数据。
- **自托管选项**：提供 Docker 和 Cloudflare 两种自托管方案，用户可以将数据保留在自己的服务器上。

## 技术架构

OpenSEO 采用 TypeScript 开发，后端通过 API 层与 DataForSEO、Google Search Console 等外部数据源交互。前端采用现代 UI 框架构建，确保操作流畅。项目的核心设计特点是模块化——核心 SEO 工作流与 AI Agent 技能层分离，使得用户可以独立更新或定制技能模块。MCP 协议的引入让 OpenSEO 更易于与各类 AI 系统集成，降低了开发者的接入门槛。整体架构支持云端托管和自托管两种部署模式，满足不同用户对数据隐私和控制力的需求。

## 安装与使用

### 快速开始（Docker 自托管）

1. 克隆仓库：
   ```bash
   git clone https://github.com/every-app/open-seo.git
   cd open-seo
   ```

2. 创建 `.env` 文件并配置以下环境变量：
   - `DATAFORSEO_API_KEY` 和 `DATAFORSEO_API_SECRET`：注册 DataForSEO 账户后获取。
   - （可选）`GOOGLE_SEARCH_CONSOLE_CREDENTIALS`：连接 Google Search Console 的凭证。

3. 使用 Docker Compose 启动：
   ```bash
   docker compose up -d
   ```

4. 访问 `http://localhost:3000` 开始使用。

### 最小可用示例

假设你已经配置了 DataForSEO API，可以通过 UI 界面执行一次关键词研究：
- 打开 OpenSEO 仪表板。
- 选择“关键词研究”工作流。
- 输入目标关键词，点击分析。
- 系统将返回搜索量、竞争度等数据。

若要结合 AI Agent 使用，可在技能市场中激活“每日排名监控”技能，然后连接到 Claude Code，Agent 将自动获取并报告排名变化。

## 适用场景

- **个人站长与博客作者**：无需订阅昂贵的 SEO 工具，即可完成关键词分析、内容优化和排名追踪。
- **自由职业 SEO 顾问**：为客户提供审计报告和优化建议，利用 AI Agent 批量处理任务，提高效率。
- **开发者和 AI 爱好**：将 OpenSEO 集成到自定义 AI 工作流中，构建智能 SEO 自动化系统。
- **小型营销团队**：自托管部署，确保数据安全，同时在不同成员间共享 SEO 洞察。

## 项目亮点

- **成本透明可控**：与月费数百美元的 Semrush 或 Ahrefs 不同，OpenSEO 仅按实际 API 调用付费，适合预算有限的用户。
- **AI 原生集成**：不仅仅是工具，更是 AI Agent 的数据源和执行器，预置技能让自动化唾手可得。
- **完全开源**：采用 MIT 许可证，用户可以自由使用、修改和分发，无需担心供应商锁定。
- **简洁且专注**：避免商业工具中常见的功能冗余，只保留最核心的 SEO 工作流，降低学习成本。

## 相关链接

- [GitHub 仓库](https://github.com/every-app/open-seo)
- [官方托管版本](https://openseo.so)
