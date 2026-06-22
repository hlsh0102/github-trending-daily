---
tags:
  - trending
  - article
repo: ZhuLinsen/daily_stock_analysis
date: 2026-06-22
language: Python
stars_total: 45060
stars_today: 568
---
## 项目概述

股票智能分析系统（daily_stock_analysis）是一个基于 AI 大语言模型（LLM）的多市场股票分析工具。它能够自动化地从多个数据源获取行情、新闻等实时信息，利用大模型进行分析，生成决策看板，并将分析结果推送至企业微信、飞书、Telegram、Discord、Slack 和邮箱等多种渠道。该项目面向需要每日跟踪自选股动态、但又没有时间手动进行分析的散户投资者、量化爱好者以及任何对股市自动化分析感兴趣的开发者。核心价值在于利用 AI 降低日常盯盘和基础分析的时间成本，并支持零成本通过 GitHub Actions 定时运行，无需额外的服务器开销。

## 核心功能

- **多市场自选股分析**：支持同时分析 A 股、港股、美股、日股和韩股的自选股组合，用户可灵活配置。
- **多源实时行情与新闻**：自动聚合来自多个数据源的股票行情数据，并抓取相关实时新闻和公告，为分析提供丰富信息基础。
- **AI 决策看板生成**：集成大语言模型（如 OpenAI 兼容接口），基于行情和新闻自动生成包含技术面、消息面综合判断的决策看板，而非简单输出原始数据。
- **多平台自动推送**：分析结果定时生成后，可一键推送到企业微信、飞书、Telegram、Discord、Slack 以及电子邮件，确保用户随时随地获取。
- **零成本定时运行**：项目深度集成 GitHub Actions，用户完成配置后，可利用 GitHub 提供的免费计算资源实现每日自动化运行，无需自建服务器或支付额外的运行费用。
- **自定义 AI 模型**：支持接入用户自有的 LLM API，可选择不同的模型（如 GPT-4、Claude、国产大模型等）来生成分析报告，灵活控制分析质量和成本。

## 技术架构

该项目采用 Python 语言编写，整体架构设计轻量且模块化。核心思路是“数据采集 -> AI 分析 -> 报告生成 -> 多渠道推送”。

- **数据层**：使用 `requests`、`aiohttp` 等库调用第三方金融数据 API（如 AKShare、新浪财经、雅虎财经等）获取实时行情和财务数据；利用新闻 API 或 RSS 订阅抓取相关新闻信息。数据源可配置，支持多种行情和新闻代理。
- **AI 分析层**：通过调用大语言模型的 API（兼容 OpenAI 格式），将格式化后的行情数据和新闻文本作为上下文，向模型发送精心设计的 prompt，要求其生成包含趋势判断、支撑压力位、新闻情绪评分等信息的结构化看板。这部分是系统的核心智能所在。
- **报告与推送层**：将 AI 返回的分析结果渲染成美观的 HTML 看板或文本摘要，并通过对应的 SDK（如 `msgraph-sdk-python`、`python-telegram-bot`、`slack-sdk`）或 API 调用，推送到配置好的平台。GitHub Actions Workflow 作为定时触发器，驱动整个流水线按设定频率运行（如每日开盘前）。
- **配置管理**：所有用户自定义变量（自选股列表、API 密钥、推送配置、运行频率等）均通过环境变量或 YAML 配置文件管理，便于在 GitHub Actions 的 Secret 中安全存储。

## 安装与使用

推荐使用 Docker 或基于 GitHub Actions 的零成本方式进行部署。

**方式一：基于 GitHub Actions（推荐零成本）**

1.  将本项目 Fork 到自己的 GitHub 账户。
2.  在 Fork 后的仓库中，进入 `Settings` -> `Secrets and variables` -> `Actions`，添加以下必需的 Secrets（变量名需与代码严格一致）：
    - `STOCKS`：你的自选股代码列表，格式如 `["000001.SZ", "00700.HK", "AAPL"]`。
    - `LLM_API_KEY`：你的大模型 API Key。
    - `LLM_BASE_URL`：API 的基础地址（如 OpenAI 或兼容接口）。
    - `PUSH_PLATFORM`：推送平台选择，例如 `wecom`、`telegram`、`email` 等。
    - 根据所选平台配置对应的推送 Key 或 Token（如 `WECOM_KEY`、`TELEGRAM_BOT_TOKEN`、`EMAIL_SMTP` 等）。
3.  进入 `Actions` 选项卡，手动运行 `Daily Stock Analysis` Workflow，或等待它按默认的定时设置自动触发。
4.  查看运行日志及最终在推送平台收到的分析报告。

**方式二：本地运行（Docker）**

```bash
# 拉取镜像
docker pull zhulinsen/daily_stock_analysis:latest

# 运行容器（需提前准备好 .env 配置文件）
docker run -v $(pwd)/.env:/app/.env zhulinsen/daily_stock_analysis:latest
```

**方式三：源码运行（Python）**

```bash
# 克隆仓库
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git
cd daily_stock_analysis
# 安装依赖
pip install -r requirements.txt
# 配置 .env 文件（参考 .env.example）
# 运行分析
python run_analysis.py
```

## 适用场景

- **日常自选股监控**：普通投资者每日只需看一眼推送到手机的决策看板，即可快速了解自己关注股票的技术形态和新闻情绪，无需逐一手动查看。
- **盘前快速复盘**：在开盘前自动生成前一交易日或隔夜的分析报告，帮助用户快速掌握市场动态，制定当日交易策略。
- **多市场跨境投资**：对于同时投资 A股、港股、美股等多个市场的用户，系统可以统一分析来自不同市场的股票，生成一份整合报告，极大提升跨市场信息处理效率。
- **AI 策略验证**：量化爱好者或开发者可以基于此框架，修改 prompt 或接入不同的 LLM，快速验证自定义分析逻辑的有效性。

## 项目亮点

- **极致零成本**：通过 GitHub Actions 免费运行，完全无需用户自购服务器或支付其他运行费用，实现了个人量化分析的低成本化。
- **AI 驱动深度分析**：不同于传统仅显示行情数据的工具，该项目利用 LLM 的语义理解能力，将原始数据转化为具有判断依据的“决策看板”，提供情绪评分、趋势解读等深度分析。
- **一站式多市场与多推送**：同时覆盖五大主要股票市场，并支持多达六种主流推送渠道，用户只需配置一次，每天自动接收整合后的分析结果，体验高度集成。
- **开源与可定制**：项目采用 MIT 许可证，代码完全开源。用户可以自由修改支持的市场、调整 AI 分析 prompt、增加自定义数据源或推送渠道，满足个人化需求。

## 相关链接

- [GitHub 仓库](https://github.com/ZhuLinsen/daily_stock_analysis)
- [完整文档中心](docs/INDEX.md)
- [详细使用指南](docs/full-guide.md)
