---
tags:
  - trending
  - article
repo: mvanhorn/last30days-skill
date: 2026-06-08
language: Python
stars_total: 32056
stars_today: 1111
---
## 项目概述

`/last30days` 是一个 AI 代理驱动的搜索技能（Agent Skill），能够同时检索 Reddit、X（Twitter）、YouTube、Hacker News、Polymarket 以及通用网络上的信息，并基于这些来源生成一份有根据的摘要。该项目旨在解决传统搜索引擎依赖编辑推荐或模糊算法排名的问题，转而使用点赞数、评分和实际市场赔率等具体指标来评估内容质量。目标用户包括开发者、研究人员、内容创作者以及任何需要快速了解某个话题在过去 30 天内真实讨论热度的人。

## 核心功能

- **多源同步搜索**：一次查询即可覆盖 Reddit、X、YouTube、Hacker News、Polymarket 等多个平台，无需手动切换。
- **基于社区指标的排名**：结果按照帖子在 Reddit 上的评分、X 上的点赞、YouTube 的观看量、Polymarket 的赔率等真实数据排序，而非搜索引擎的未知算法。
- **零配置启动**：Reddit、Hacker News、Polymarket 和 GitHub 无需任何 API 密钥即可立即工作。
- **一键配置向导**：首次运行后，内置向导会在 30 秒内解锁 X、YouTube、TikTok 等平台的 API 密钥设置。
- **跨平台兼容**：支持 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等超过 50 种 AI 代理和 IDE 环境。
- **可定制摘要**：自动将搜索结果整合为一条有依据的总结，帮助用户快速把握舆论趋势。

## 技术架构

项目采用 v3 版本管道设计，核心逻辑由 Python 实现。技能规范以 Markdown 文件形式定义在仓库的 `skills/last30days/SKILL.md` 中，作为最新命令和设置行为的最终来源。

架构上，项目与 Agent Skills 生态深度集成，通过 `npx skills add` 或 Claude Code 的插件命令进行部署。这种设计使得技能可以被移植到任意支持 Agent Skills 的主机中，而无需为每个平台重写搜索逻辑。管道本身包括一个调度器，负责向各平台 API 发送并行请求，然后一个聚合器根据预定义的评分规则（如 Reddit 评分、X 点赞数）对结果加权排序，最后由一个生成器调用 LLM 构建摘要。

## 安装与使用

### 安装

推荐使用 **Claude Code**（自动更新通过市场）：

```bash
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

对于 **Codex、Cursor、Copilot、Gemini CLI** 等环境，使用：

```bash
npx skills add mvanhorn/last30days-skill -g
```

添加 `-g` 标志将技能全局安装到用户层面，可用于所有项目；省略该标志仅作用于当前项目目录。

### 最小可用示例

安装完成后，任何支持 Agent Skills 的主机内，直接输入类似以下的命令即可：

```
/last30days "大型语言模型开源社区发展动态"
```

技能会依次检索 Reddit、Hacker News、YouTube 等平台，随后输出类似如下格式的摘要：

```
Reddit: r/LocalLLaMA 帖子评分 350，讨论集中在量化模型的性能提升。
YouTube: 两个 10w+ 播放视频对比了 Qwen 与 Llama 的微调成本。
Polymarket: “2025年开源模型能力超越GPT-4” 赌注赔率为 1:3。
综合结论：过去 30 天，开源社区在高效微调和量化部署上进展显著，社区整体情绪乐观。
```

## 适用场景

- **技术趋势追踪**：开发者可以使用 `/last30days` 快速了解某个框架、工具或语言在过去一个月的社区讨论热度和主要观点变化。
- **市场情绪调研**：研究人员结合 Polymarket 赔率和社交媒体讨论，分析某个事件（如总统选举、公司重大发布）的市场预期。
- **内容创作选题**：博主或视频创作者通过对比 Reddit、YouTube 和 X 上的热度数据，找到当前最受关注的低竞争话题。
- **投资前研究**：在 Polymarket 上下注或评估某个新兴项目（如代币、论文）前，利用该技能收集多维度评论和数据。

## 项目亮点

与市面上其他 AI 搜索工具相比，`/last30days` 的差异化优势在于：

1. **透明排名依据**：不是“算法觉得重要”，而是“社区真的在点赞、投注、评分”。每个来源的排序指标都明确写在技能文档中。
2. **极低上手门槛**：无需配置任何 API 密钥即可开始使用四个核心平台，大大降低了进入成本。
3. **一技能多用**：搜索技能不再绑定特定 IDE 或聊天界面，而是通过 Agent Skills 标准在任何支持的环境中运行。
4. **开源与许可友好**：采用 MIT 许可证，允许自由修改和商用。在 GitHub 上已获得超过 3 万星标，社区活跃度高。

## 相关链接

- [GitHub 仓库](https://github.com/mvanhorn/last30days-skill)
- [Agent Skills 官网](https://agentskills.io)
