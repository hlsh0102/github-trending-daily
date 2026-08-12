---
tags:
  - trending
  - article
repo: ZhuLinsen/daily_stock_analysis
date: 2026-08-12
language: Python
stars_total: 62263
stars_today: 243
---
## 项目概述

daily_stock_analysis 是一个基于大语言模型（LLM）驱动的多市场股票智能分析系统，由开发者 ZhuLinsen 创建并维护。该项目专注于解决个人投资者在信息过载环境下的决策难题：面对 A股、港股、美股、日股、韩股、台股等多个市场的海量行情数据与实时新闻，人工筛选和解读信息的成本极高。该系统通过自动采集多源行情与新闻，利用 LLM 进行深度分析，最终生成一份结构化的「决策仪表盘」并推送到用户常用的通讯工具中。目标用户是希望通过自动化工具提升投资研究效率的个人投资者、量化爱好者以及需要快速获取市场概览的金融从业者。项目采用 MIT 协议开源，当前在 GitHub 上已获得超过 6 万 Star，属于热门的开源金融分析工具。

## 核心功能

- **多市场覆盖**：内置对 A股、港股、美股、日股、韩股、台股六大市场的支持，可自定义自选股列表，统一进行数据抓取与分析。
- **多源行情与新闻聚合**：整合多个免费数据源获取实时行情和财经新闻，确保分析基于充分的信息输入，减少单一数据源带来的偏差。
- **LLM 智能分析**：调用大语言模型对行情数据、新闻事件进行交叉解读，生成包括趋势判断、风险提示、事件驱动分析在内的综合报告。
- **决策仪表盘推送**：将分析结果渲染为清晰直观的仪表盘卡片，自动推送到企业微信、飞书、Telegram、Discord、Slack 或邮箱。
- **零成本定时运行**：深度集成 GitHub Actions，支持通过 Cron 语法配置每日定时任务，利用免费额度实现全自动运行，无需自建服务器。
- **高度可配置**：支持通过 YAML 或环境变量灵活配置股票池、推送渠道、分析模型、语言（中文/英文/繁体中文）等参数。

## 技术架构

项目采用 Python 作为核心开发语言，整体架构设计遵循模块化与配置驱动原则。在数据层，系统通过抽象接口对接多个免费的数据提供商（如 Yahoo Finance、东方财富等），完成行情和新闻的获取与标准化。在分析层，系统使用 LangChain 等 LLM 应用框架编排提示词，将结构化数据和非结构化新闻组装成上下文，调用 OpenAI、Claude 或其他兼容 API 的模型进行推理。在输出层，项目设计了模板化的消息生成器，将模型输出的文本转化为适配不同 IM 平台的富文本卡片格式。调度方面，项目提供了 Dockerfile 和 GitHub Actions 工作流文件，支持两种运行模式：一是本地或服务器上通过 Docker 运行常驻服务；二是利用 GitHub Actions 的调度功能，在云端无服务器环境下定时执行分析任务。这种设计使得系统既保留了本地部署的灵活性，又提供了零成本的云原生运行方案。

## 安装与使用

安装过程较为简便，推荐使用 Docker 方式快速部署：

```bash
# 1. 克隆仓库
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git
cd daily_stock_analysis

# 2. 使用 Docker 构建并运行（需先配置环境变量）
docker run -d --name stock-analysis \
  -e LLM_API_KEY="your_api_key" \
  -e LLM_MODEL="gpt-4o-mini" \
  -e PUSH_CHANNEL="telegram" \
  -e TELEGRAM_BOT_TOKEN="your_bot_token" \
  -e TELEGRAM_CHAT_ID="your_chat_id" \
  -v $(pwd)/config.yaml:/app/config.yaml \
  zhulinsen/daily_stock_analysis
```

若希望使用 GitHub Actions 免费定时运行，只需将仓库 Fork 到自己的账号下，在 Settings -> Secrets 中配置所需的 API 密钥和推送凭证，然后编辑 `.github/workflows/daily-analysis.yml` 中的 Cron 表达式（例如 `0 1 * * *` 表示每天凌晨 1 点运行）。最小配置的 `config.yaml` 示例如下：

```yaml
stocks:
  - market: "A股"
    code: "600519"
  - market: "港股"
    code: "00700"
analysis:
  language: "zh-CN"
  focus: ["趋势", "风险"]
```

运行后，系统会根据股票列表抓取数据并调用 LLM 生成报告，最终推送到指定渠道。

## 适用场景

- **投资晨报**：投资者在每天早上通过企业微信或 Telegram 接收一份由 AI 生成的持仓股或自选股晨报，包含隔夜市场动态、关键新闻解读和当日关注要点，帮助快速决策。
- **多市场跟踪**：对于同时关注美港股和 A股的投资者，系统可以统一在一个仪表盘中展示不同市场的自选股表现，避免在不同 App 之间切换。
- **事件驱动监控**：设置较短的分析间隔（如每小时），系统可捕捉突发新闻对持仓股的影响，及时推送风险预警，辅助短线操作。
- **团队研究协作**：小型投研团队可将系统接入飞书或 Slack 群组，自动发布每日市场研判，作为团队讨论的起点，提高信息同步效率。

## 项目亮点

与同类开源项目相比，daily_stock_analysis 的差异化优势体现在三个层面：其一，**多市场一体化支持**，绝大多数竞品仅聚焦单一市场（通常是美股），而本项目开箱即用地覆盖六大市场，尤其对亚太市场有良好适配。其二，**推送渠道丰富且开箱即用**，项目内置了五种以上主流 IM 平台的通知适配器，无需二次开发即可接入团队既有协作工具。其三，**零成本运行设计**，充分利用 GitHub Actions 免费额度，让普通用户无需购买服务器即可获得每日稳定的分析服务。此外，项目的文档质量较高，提供了中英繁三语 README 和完整指南，降低了上手门槛。得益于 LLM 的通用理解能力，系统分析维度丰富，不局限于技术指标，能够融合新闻情绪进行研判。

## 相关链接

- [GitHub 仓库](https://github.com/ZhuLinsen/daily_stock_analysis)
- [完整文档中心](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/INDEX.md)
- [Docker 镜像](https://hub.docker.com/r/zhulinsen/daily_stock_analysis)
