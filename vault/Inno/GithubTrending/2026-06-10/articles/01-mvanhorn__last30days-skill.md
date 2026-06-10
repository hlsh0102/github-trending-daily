---
tags:
  - trending
  - article
repo: mvanhorn/last30days-skill
date: 2026-06-10
language: Python
stars_total: 37997
stars_today: 3191
---
## 项目概述

`/last30days` 是一个 AI 驱动的搜索与分析技能（Skill），它能够跨越 Reddit、X (Twitter)、YouTube、Hacker News、Polymarket 以及整个互联网，自动研究任意话题，并合成一份有依据的摘要。该项目解决了传统搜索引擎依赖编辑推荐或商业排名的问题——它根据点赞、投票和 Polymarket 上的真实资金押注来排序结果，而非人为干预。目标用户包括开发者、研究人员、内容创作者以及任何需要快速了解某个话题在近期社交媒体和公众讨论中生态的全貌的人。

## 核心功能

- **多源横向搜索**：自动同时查询 Reddit、X、YouTube、Hacker News、Polymarket 和通用网页，覆盖主流讨论阵地。
- **基于社交信号的排序**：结果以 Reddit 的 upvotes、X 的 likes、YouTube 的点赞数、Polymarket 的押注额为权重进行排序，确保高可信度、高关注度的内容优先展示。
- **零配置快速启动**：Reddit、Hacker News、Polymarket 和 GitHub 无需任何 API 密钥或配置即可使用；运行一次后会通过交互式向导在 30 秒内解锁 X、YouTube、TikTok 等源。
- **合成式摘要生成**：AI 将来自不同来源的碎片化信息整合为结构化的、带引用的摘要，而非简单罗列链接。
- **符合 Agent Skills 标准**：兼容 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等 50 多种 AI 开发工具，且支持一键安装与自动更新。
- **开源与可扩展**：基于 MIT 协议发布，开发者可 fork 修改或自定义搜索源。

## 技术架构

该项目采用 Python 编写，以“技能包”（Skill Package）的形式封装，遵循 [Agent Skills](https://agentskills.io) 协议。其核心设计分为三层：

1. **接入层**：通过统一的 CLI 命令（`/last30days <topic>`）接收用户查询，并将指令分发至各数据源适配器。
2. **数据源层**：每个平台（Reddit、X、YT 等）对应一个独立的爬虫/API 适配器，使用异步 I/O 并行采集数据。Polymarket 的数据通过其公开的预测市场 API 获取。
3. **分析与合成层**：所有原始数据带回后，调用语言模型进行去重、排序（依据社交信号权重）、摘要生成。最终输出包含来源链接、关键统计（如总 upvotes）、以及多角度观点总结的 Markdown 报告。

架构特点是“即插即用”：新增数据源只需实现一个适配器接口并注册即可，无需改动核心流水线。当前代码标为 v3 流水线，具体运行时命令与配置以仓库内 `skills/last30days/SKILL.md` 为最终依据。

## 安装与使用

**前提**：需要 Node.js 环境（用于 `npx`）或兼容 Agent Skills 的 CLI 工具（如 Claude Code）。

**推荐方式（Claude Code）**：
```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```
此方式会自动更新至最新版。

**通用方式（Codex、Cursor、Copilot、Gemini CLI 等）**：
```bash
npx skills add mvanhorn/last30days-skill -g
```
参数 `-g` 表示全局安装，所有项目均可调用；不加则仅为当前项目安装。

**使用**：安装完成后，在支持的 AI 工具中直接输入命令即可：
```
/last30days 苹果发布会最新动态
```
AI 将自动搜索并返回一份涵盖 Reddit 热帖、X 讨论、YouTube 评测、HN 技术评论、Polymarket 押注结果的综合摘要。

## 适用场景

- **市场调研与竞品分析**：产品经理或创业者想要了解某款新产品（如 Rabbit R1、Vision Pro 上市 30 天）在各大社交平台上的真实口碑，而非被编辑筛选过的报道。
- **热点事件追踪**：记者或研究人员需要快速掌握一个突发话题（如 OpenAI 董事会风波）在 Reddit、X、HN 上的讨论风向、情绪分布和关键人物发声。
- **内容创作灵感搜集**：YouTuber 或自媒体作者想做一个关于“AI 编程工具”的选题，可以用它获取近期多个平台上的高赞帖子和爆款视频标题，直接获得选题方向和数据支撑。
- **个人知识管理**：开发者或投资人想持续跟踪某个技术（如 Rust for Web）在行业内的实际讨论热度与争议焦点，避免被算法推荐困在信息茧房。

## 项目亮点

与常见的 AI 搜索工具（如 Perplexity、Google Gemini 的搜索结果摘要）相比，`/last30days` 的核心差异在于：

- **信号源优势**：不是抓取整网权威页面，而是专注于 Reddit、X、HN 等讨论型与预测市场平台。这类平台的“赞”和“押注”体现了真实的人类判断，而非 SEO 流量。
- **时间窗口聚焦**：默认只分析“最近 30 天”的内容（名称即体现），非常契合“某个话题当下在讨论什么”的时效性需求。
- **面向 AI 代理**：设计为可被 AI 工具自动调用的技能，而非独立的网页应用。这意味着它可以嵌入到你的自动化工作流中——比如让 Claude 在生成文档前自动运行该技能做背景调研。
- **预测市场数据**：引入 Polymarket 作为数据源，让“观点”与“真实金钱押注”挂钩，这在同类工具中极为罕见，提供了独特的市场情绪维度。

## 相关链接

- [GitHub 仓库](https://github.com/mvanhorn/last30days-skill)
- [Agent Skills 官方站点](https://agentskills.io)（了解技能标准与集成列表）
- [Polymarket](https://polymarket.com)（预测市场数据源）
