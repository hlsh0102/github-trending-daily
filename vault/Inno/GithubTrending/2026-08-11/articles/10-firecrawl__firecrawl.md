---
tags:
  - trending
  - article
repo: firecrawl/firecrawl
date: 2026-08-11
language: TypeScript
stars_total: 165213
stars_today: 835
---
## 项目概述

Firecrawl 是一个面向开发者的 Web 数据采集与交互 API 平台，致力于解决大规模网页抓取、搜索和内容提取过程中的复杂性问题。无论是构建 AI 应用、训练大语言模型，还是进行市场情报分析，开发者都需要高效、可靠地从互联网获取结构化数据。Firecrawl 将这一过程封装为简洁的 API 调用，使开发者无需关心反爬虫、页面渲染、数据清洗等底层细节，即可轻松获取网页内容。

该项目由 Mendable.ai 团队开发，采用 TypeScript 编写，以 AGPL-3.0 许可证开源。Firecrawl 的目标用户包括 AI 工程师、数据科学家、爬虫开发者以及任何需要从 Web 获取数据的软件团队。其核心理念是提供一个统一的 "Context API"，让开发者可以通过一个接口完成搜索、抓取和交互三类 Web 操作。

## 核心功能

- **网页抓取（Scrape）**：将任意 URL 转换为干净的 Markdown 或结构化 JSON 数据，自动处理 JavaScript 渲染、代理轮换和反爬虫机制，返回适合 LLM 消费的文本内容。
- **搜索 API（Search）**：集成 Google 等搜索引擎，返回特定查询的搜索结果（页面内容而非仅链接），支持按 URL 列表、站点地图或搜索引擎进行批量抓取。
- **批量抓取（Batch Scrape）**：支持同时提交数千个 URL 进行异步抓取，并通过 Webhook 或轮询方式获取结果，适合大规模数据收集任务。
- **爬虫模式（Crawl）**：从一个起始 URL 开始，自动发现并抓取该站点下的所有相关页面，支持控制抓取深度、路径限制和页面数量。
- **提取功能（Extract）**：结合 LLM 能力，从网页中提取特定的结构化字段（如产品价格、新闻标题、联系人信息等），无需编写复杂的解析规则。
- **多语言 SDK 支持**：提供 Python（firecrawl-py）和 TypeScript/JavaScript（firecrawl-ts）官方 SDK，以及社区贡献的 Go、Rust、Java 等语言封装。

## 技术架构

Firecrawl 采用现代 Web API 架构设计，其核心引擎基于 Playwright 无头浏览器，能够处理高度动态的单页应用（SPA）和需要 JavaScript 渲染的页面。整个系统分为几个关键层：

- **调度与代理层**：管理大量并发请求，自动轮换代理 IP，规避目标网站的 IP 封禁和速率限制。
- **渲染引擎**：使用 Playwright 加载页面，执行 JavaScript，等待网络空闲后提取 DOM 结构，确保拿到的是最终渲染结果。
- **内容转换流水线**：将原始 HTML 转换为干净的 Markdown 格式，去除导航栏、广告、脚本等噪声元素，同时保留关键元数据（如标题、描述、OG 标签）。
- **API 网关**：基于 RESTful 原则设计，所有操作通过 `https://api.firecrawl.dev/v1` 统一暴露，支持同步和异步两种模式。对于耗时任务（如批量抓取），采用任务 ID + Webhook 的回调机制。
- **可扩展性设计**：开源版本支持自托管部署，用户可以基于 Docker Compose 快速搭建本地实例，实现数据不出内网的安全要求。

## 安装与使用

Firecrawl 提供了两种使用方式：使用官方托管的云服务（需注册 API Key），或自行部署开源版本。以下以 Python SDK 为例展示基本用法：

**1. 安装 SDK：**
```bash
pip install firecrawl-py
```

**2. 初始化客户端并抓取单个页面：**
```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="your-api-key")

# 抓取网页为 Markdown
scraped = app.scrape_url('https://example.com', params={'formats': ['markdown']})
print(scraped['markdown'])
```

**3. 执行搜索：**
```python
search_result = app.search('OpenAI latest news', limit=5)
for item in search_result['data']:
    print(item['url'], item['title'])
```

**4. 使用异步批量抓取：**
```python
batch = app.batch_scrape_urls(['https://site1.com', 'https://site2.com'], wait_until_done=True)
for doc in batch['data']:
    print(doc['markdown'][:200])
```

对于自托管部署，可参考官方文档使用 Docker 启动 Redis、API 服务、Worker 和 Playwright 服务四个容器，然后通过环境变量配置 API 密钥和访问控制。

## 适用场景

- **AI 应用上下文构建**：为 RAG（检索增强生成）系统提供高质量网页内容，将抓取的 Markdown 直接作为向量数据库的输入，构建知识库。
- **市场情报监控**：定时抓取竞争对手官网、行业新闻网站和社交媒体页面，提取价格、产品变更等关键信息。
- **训练数据准备**：大规模收集特定领域的高质量文本数据，用于微调大语言模型或构建领域数据集。

## 项目亮点

- **一体化 API 设计**：将搜索、抓取、爬取和提取四种能力统一在一个 API 中，开发者无需整合多个工具，显著降低开发成本。
- **原生面向 LLM 的输出**：直接输出干净的 Markdown，与主流 AI 框架（如 LangChain、LlamaIndex）无缝集成，省去繁琐的 HTML 清洗步骤。
- **云端 + 开源自托管双重模式**：既提供开箱即用的托管服务（免费额度），也允许企业级用户完全私有化部署，满足数据合规要求。
- **活跃的社区与迭代速度**：项目在 GitHub 上拥有超过 16 万 Star，社区贡献了多种语言 SDK 和丰富文档，每周都有功能更新。

## 相关链接

- [GitHub 仓库](https://github.com/firecrawl/firecrawl)
- [官方网站](https://firecrawl.dev)
- [API 文档](https://docs.firecrawl.dev)
