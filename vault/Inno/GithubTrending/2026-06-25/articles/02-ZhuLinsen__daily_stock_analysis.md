---
tags:
  - trending
  - article
repo: ZhuLinsen/daily_stock_analysis
date: 2026-06-25
language: Python
stars_total: 48908
stars_today: 1468
---
## 项目概述

daily_stock_analysis 是一个基于 AI 大语言模型（LLM）的多市场股票智能分析系统，由开发者 ZhuLinsen 开源维护。该项目旨在解决个人投资者在跨市场股票分析中面临的信息碎片化、分析效率低下等问题。系统能够自动获取 A股、港股、美股、日股、韩股等主要市场的实时行情与新闻，借助大模型生成每日决策仪表盘，并通过企业微信、飞书、Telegram、Discord、Slack 和邮箱等渠道推送给用户。项目特别设计了零成本定时运行的能力，支持用户通过 GitHub Actions 完全免费地部署和运行，降低了自动量化分析的门槛。

## 核心功能

- **多市场覆盖**：支持 A股、港股、美股、日股、韩股自选股的行情与新闻数据整合，用户可自由配置关注的股票列表。
- **AI 驱动分析**：接入多个主流大语言模型（如 GPT、Claude 等），对股票数据进行解读，生成包含趋势判断、异动提醒、风险提示在内的简洁分析报告。
- **每日决策仪表盘**：系统每日自动生成一张决策仪表盘视图，以图片形式呈现当日关键分析结论，便于快速决策。
- **多渠道自动推送**：支持企业微信、飞书、Telegram、Discord、Slack 以及邮箱等多种推送方式，用户可根据团队或使用习惯选择。
- **零成本定时运行**：基于 GitHub Actions 实现免费的定时调度，无需购买服务器或支付云函数费用，即可每日自动执行分析流程。
- **模块化配置**：通过 YAML 或环境变量即可完成从数据源、LLM 模型到推送渠道的全部配置，无需修改代码，便于二次开发。

## 技术架构

项目采用 Python 语言开发，核心架构围绕数据采集、LLM 分析、报告生成与推送四个模块设计：

- **数据采集层**：通过多个金融数据接口（如 AKShare、Yahoo Finance 等）获取实时行情、历史数据和相关新闻，保证了多市场数据的覆盖度和及时性。
- **LLM 分析引擎**：调用 OpenAI 兼容的 API 接口，将整理后的市场数据作为提示词（Prompt）传入，利用大模型的语言理解与推理能力生成分析结论。系统内置了针对股票分析的提示词模板，并可自定义模型参数。
- **报告生成模块**：将 LLM 返回的文本结果结合 Matplotlib 或 Pillow 等库，渲染为包含表格、趋势图标的图文仪表盘图片，也支持纯文本输出。
- **推送模块**：抽象了统一的推送接口，分别实现各渠道（企业微信、Telegram 等）的 API 对接，用户只需配置对应的 webhook 或 Token 即可启用。
- **调度与 CI/CD**：主要依赖 GitHub Actions 进行定时触发，Workflow 文件定义了运行环境、依赖安装和执行命令。此外，项目也提供了 Docker 镜像，允许用户在自有服务器上运行。

整体设计强调可扩展性和轻量化，核心代码逻辑清晰，便于开发者理解并贡献自定义数据源或推送渠道。

## 安装与使用

### 前置要求
- Python 3.9 及以上版本
- 一个可用的 LLM API Key（如 OpenAI、Anthropic 等）
- 目标推送渠道的 Webhook 地址或 Token（如企业微信机器人）

### 快速开始（使用 GitHub Actions）

1. **Fork 仓库**：将 `https://github.com/ZhuLinsen/daily_stock_analysis` fork 到自己的 GitHub 账户下。
2. **配置 Secret**：在 fork 后的仓库中，进入 `Settings > Secrets and variables > Actions`，添加以下必要的 Secret：
   - `LLM_API_KEY`：你的大模型 API Key
   - `WECOM_BOT_KEY`：企业微信机器人的 Key（若使用）
   - 其他渠道的配置参考文档
3. **编辑股票列表**：修改 `config/stocks.yaml` 文件，填入你关注的自选股代码（支持多种市场格式，如 `SH.600519`、`HK.00700`、`US.AAPL`）。
4. **自动运行**：默认 Workflow 会在每个交易日早上 8:00（UTC）即北京时间 16:00 自动运行，你也可以手动在 Actions 页面触发 `Run workflow`。
5. **接收推送**：根据配置的渠道，你将在指定时间收到每日股票分析报告。

### 本地运行（Docker）
```bash
docker pull zhulinsen/daily_stock_analysis
# 创建配置文件并设置环境变量后运行
docker run -v /path/to/config:/app/config -e LLM_API_KEY=your_key -e PUSH_CHANNEL=wecom zhulinsen/daily_stock_analysis
```

更多安装方式与高级配置请参阅项目的[完整指南](docs/full-guide.md)。

## 适用场景

- **个人投资辅助决策**：普通股民无法实时盯盘，可通过每日推送的仪表盘快速了解关注股票的走势、财报新闻与市场情绪，提高信息获取效率。
- **团队投研报表自动化**：投资小组或研究团队可将系统集成到企业微信或 Slack 中，每天自动生成一份统一的持仓或关注标的的简报，节省人工整理报告的时间。
- **量化策略信号监控**：结合用户自定义的规则（如涨幅阈值、成交量异动），在 LLM 分析层中加入条件过滤，实现对特定策略信号的监控与提醒。
- **多市场试验性学习**：对海外市场感兴趣的投资者，可以同时配置 A股、港股、美股等标的，通过同一系统获取跨市场的每日观点，辅助学习不同市场的运行规律。

## 项目亮点

- **完全免费托管**：充分利用 GitHub Actions 的免费额度，用户无需支付任何服务器费用即可获得稳定的定时任务执行能力，这是同类项目少有的特性。
- **多模型兼容**：不只绑定单一 LLM 服务商，支持 OpenAI、Anthropic、通义千问等多种模型接入，用户可根据成本、偏好或合规要求自由切换。
- **极致配置灵活性**：从自选股列表、分析提示词、推送时间到输出格式，几乎所有行为均可通过配置文件调整，无需修改一行代码。
- **社区活跃与易贡献**：项目在 GitHub 上已获得近 5 万 Star，拥有详细的中文文档（含繁体与英文版），issue 和 PR 响应积极，新手可以方便地参与贡献或定制作业。

## 相关链接

- [GitHub 仓库](https://github.com/ZhuLinsen/daily_stock_analysis)
- [文档中心](docs/INDEX.md)
- [完整指南](docs/full-guide.md)
- [英文文档](docs/README_EN.md)
