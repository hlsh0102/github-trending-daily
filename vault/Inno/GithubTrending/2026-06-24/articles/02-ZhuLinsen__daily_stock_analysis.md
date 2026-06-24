---
tags:
  - trending
  - article
repo: ZhuLinsen/daily_stock_analysis
date: 2026-06-24
language: Python
stars_total: 47488
stars_today: 1119
---
## 项目概述

股票智能分析系统是一个基于 AI 大语言模型构建的多市场股票智能分析平台，由开发者 ZhuLinsen 创建并开源在 GitHub 上。该项目主要解决了个人投资者在同时关注 A股、港股、美股、日股和韩股等跨市场自选股时，难以高效获取多源行情、实时解读新闻并做出快速决策的痛点。

项目的目标用户是具有一定投资经验、需要自动化分析工具来辅助日常决策的个人投资者，以及希望快速搭建股票监控与推送系统的技术爱好者。通过集成大语言模型的分析能力，系统能够自动抓取最新行情与新闻，生成结构化的「决策仪表盘」，并通过多种即时通讯渠道推送到用户手中，实现全自动、低成本的每日股票分析工作流。

目前该项目在 GitHub 上已获得超过 47000 颗星标，社区活跃度极高，反映出其在量化分析领域的实用价值。

## 核心功能

- **多市场自选股覆盖**：支持 A股、港股、美股、日股、韩股五大市场的自选股配置，用户可在单一系统中统一管理跨市场的投资组合。
- **多源行情数据聚合**：自动从多个公开数据源获取实时行情数据（如股价、涨跌幅、成交量、换手率等），并整合为统一的概览视图。
- **实时新闻与信息爬取**：针对每只自选股，自动抓取当日的相关新闻、公告及社交媒体讨论，为 AI 分析提供最新素材。
- **LLM 驱动智能分析**：利用大语言模型对行情数据和新闻内容进行综合解读，生成每只股票的短期走势判断、风险提示及交易建议，并汇总为「决策仪表盘」。
- **多渠道自动推送**：分析完成后，支持通过企业微信、飞书、Telegram、Discord、Slack 以及电子邮件等多种渠道，定时自动推送决策仪表盘至用户手机或电脑。
- **零成本定时运行**：充分利用 GitHub Actions 的免费配额，支持无服务器环境下的每日定时自动执行，用户无需自备服务器即可长期稳定使用。

## 技术架构

该项目采用典型的 Python 后端架构，核心组件包括：

- **数据采集层**：基于 akshare、yfinance 等开源金融数据库，以及自定义的网页爬虫，获取行情、新闻等原始数据。
- **分析引擎层**：集成 OpenAI API（或其他兼容的 LLM 接口）作为分析核心，通过精心设计的 Prompt 模板，将原始数据转化为结构化的决策仪表盘。
- **推送适配层**：通过 Webhook、Bot API 等协议，实现对企业微信、飞书、Telegram、Discord、Slack 等十余种即时通讯平台的消息格式化与发送。
- **调度组件**：基于 GitHub Actions 的 cron 触发器，实现每日指定时间自动启动工作流；同时支持本地 Docker 部署，以满足需要私有化运行的场景。
- **配置管理**：所有敏感信息（如 API Key、推送 Token、自选股列表）均通过 GitHub Secrets 或环境变量注入，确保安全与可追溯性。

整体设计遵循模块化、可扩展的原则，用户只需修改配置文件即可添加新的市场、股票或推送渠道，无需修改核心代码。

## 安装与使用

### 快速开始（使用 GitHub Actions，推荐）

1. **Fork 仓库**：将本项目 Fork 到自己的 GitHub 账号下。
2. **配置 Secrets**：在 Settings → Secrets and variables → Actions 中，添加必要的环境变量，包括 LLM API Key（如 `OPENAI_API_KEY`）、推送渠道的 Webhook URL（如 `WECHAT_WEBHOOK`）以及自选股列表（如 `STOCK_LIST`）。
3. **启用 Actions**：进入 Actions 页面，确认已启用 GitHub Actions。系统默认会在每个交易日自动运行，并推送结果。

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git
cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt

# 设置环境变量（示例：仅使用 OpenAI）
export OPENAI_API_KEY="your-key"
# 其他推送渠道配置同理

# 运行分析脚本
python main.py
```

### Docker 部署

```bash
docker run -d \
  -e OPENAI_API_KEY="your-key" \
  -e STOCK_LIST="AAPL,TSLA,0700.HK" \
  -e PUSH_CHANNEL="telegram" \
  -e TELEGRAM_BOT_TOKEN="your-token" \
  -e TELEGRAM_CHAT_ID="your-chat-id" \
  zhulinsen/daily_stock_analysis:latest
```

## 适用场景

- **个人投资者日常决策**：每日开盘前或收盘后，自动获取自选股的技术面与消息面分析，节省手动查阅各平台的时间。
- **多市场跨品种监控**：同时跟踪 A股、港股、美股等不同市场的持仓股，系统统一产出分析报告，便于横向比较。
- **团队信息共享**：在投资小组或工作群中，通过企业微信/飞书等协作工具定时推送分析结果，提升团队决策效率。
- **技术学习与实验**：作为 LLM 与金融数据结合的示范项目，适合开发者学习 Prompt Engineering、API 集成以及自动化工作流搭建。

## 项目亮点

- **完全开源免费**：基于 MIT 许可证开源，无任何隐藏收费；利用 GitHub Actions 的免费额度即可实现每日定时运行，真正零成本。
- **极低门槛**：用户只需配置环境变量，无需编写代码即可完成部署；同时提供了 Docker 镜像和一键部署模板，适合不同技术水平的用户。
- **推送渠道丰富**：支持企业微信、飞书、Telegram、Discord、Slack、邮箱等十余种渠道，覆盖绝大多数办公与社交平台。
- **分析质量可控**：用户可通过修改 Prompt 模板或切换不同的 LLM 模型（如 GPT-4、Claude、本地模型）来控制分析风格与准确性。
- **社区活跃迭代快**：该项目在 GitHub 上拥有大量 Star 和 Fork，Issue 与 PR 响应迅速，持续集成新市场和推送渠道。

## 相关链接

- [GitHub 仓库](https://github.com/ZhuLinsen/daily_stock_analysis)
- [完整文档中心](docs/INDEX.md)
