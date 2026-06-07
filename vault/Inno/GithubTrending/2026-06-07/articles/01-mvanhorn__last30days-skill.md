---
tags:
  - trending
  - article
repo: mvanhorn/last30days-skill
date: 2026-06-07
language: Python
stars_total: 29134
stars_today: 439
---
## 项目概述

/last30days 是一个由 AI 代理驱动的搜索引擎技能，旨在帮助用户快速了解任何话题在过去30天内的最新动态。它能够跨 Reddit、X（Twitter）、YouTube、Hacker News、Polymarket 以及整个网络进行深度研究，然后综合生成一份有据可依的摘要。该项目特别适合需要追踪热点、监测舆论或进行快速市场研究的用户——无论是开发者、产品经理、研究员还是普通网民，都能从中受益。它最大的特点在于：排名依据是点赞数、投票数和真金白银的下注，而非编辑的主观判断。

## 核心功能

- **跨平台多源搜索**：同时检索 Reddit、X、YouTube、Hacker News、Polymarket 预测市场和通用网络，覆盖主流信息源。
- **智能摘要合成**：AI 代理自动汇总各平台的搜索结果，生成一份结构清晰、包含数据支撑的综合报告。
- **基于影响力的排序**：搜索结果的排名由帖子获得的点赞数、评论互动量、Polymarket 交易金额等客观指标决定，而非编辑或算法偏好。
- **即时可用与零配置**：Reddit、Hacker News、Polymarket 和 GitHub 无需任何配置即可直接使用；首次运行内置设置向导，30秒即可解锁 X、YouTube、TikTok 等平台。
- **跨平台集成**：支持 Claude Code（通过市场自动更新）、Codex、Cursor、Copilot、Gemini CLI 及其他 50 多种 Agent Skills 宿主环境。
- **一次安装，全局可用**：通过 `npx skills add` 命令配合 `-g` 参数即可实现用户级全局安装，对所有项目生效。

## 技术架构

/last30days 的核心架构基于 v3 管道设计，采用 Python 编写。其关键技术栈包括：

- **多源数据采集层**：通过针对不同平台（Reddit API、YouTube Data API、X API、Hacker News API、Polymarket 数据接口）的适配器，并行收集近期内容。
- **AI 代理编排引擎**：负责调度搜索任务、合并去重、并调用大语言模型（LLM）生成摘要。该引擎设计为与 Agent Skills 生态兼容，能够无缝嵌入各种 AI 编程助手或聊天界面。
- **影响力评分模型**：对每条内容计算综合得分（点赞数、评论数、市场交易额等），并据此排序。这种设计确保了最受社区关注的内容优先展示，而非靠关键词匹配度。
- **配置与状态管理**：运行时技能规范保存在 `skills/last30days/SKILL.md` 文件中，作为命令和行为配置的权威来源。首次运行时启动的配置向导，会帮助用户完成第三方平台 API Key 的绑定。

整体设计强调“即用性”和“扩展性”：基础平台开箱可用，高级功能通过向导式配置解锁。

## 安装与使用

**推荐方式（Claude Code）：**
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```
此方式会自动更新，保持最新版本。

**其他宿主环境（Codex、Cursor、Copilot、Gemini CLI 等）：**
```
npx skills add mvanhorn/last30days-skill -g
```
- 加上 `-g` 参数表示全局安装，对所有项目可用；去掉则仅在当前项目生效。
- 该命令适用于50多种支持 Agent Skills 协议的 IDE 和终端工具。

**首次使用：**
安装后直接运行技能即可。Reddit、Hacker News、Polymarket、GitHub 无需配置。运行一次后，设置向导会自动弹出，引导你完成 X、YouTube、TikTok 等平台的 API 密钥绑定，整个过程约30秒。

**最小可用示例：**
在 Claude Code 中，你可以直接输入类似“研究过去30天AI Agent的最新进展”的指令，技能会自动执行跨平台搜索并返回摘要。

## 适用场景

- **热点追踪与舆情监测**：产品经理和市场研究人员可以用它快速了解某个话题在社交媒体和技术社区中的最新讨论热度及主要观点。
- **投资与市场研究**：结合 Polymarket 预测市场的真实资金流动数据，帮助用户判断市场情绪和潜在趋势，辅助决策。
- **技术趋势分析**：开发者通过检索 GitHub、Hacker News 和 Reddit 的相关讨论，快速掌握某项技术（如新框架、新模型）在过去一个月的关注度变化和生态发展。
- **内容创作与竞品分析**：自媒体作者或编辑可以利用它找到近期内最受欢迎的文章、视频和讨论话题，作为选题参考或素材来源。

## 项目亮点

- **真实信号，不是算法推荐**：与其他以编辑或算法喜好为主导的搜索工具不同，/last30days 直接使用点赞、投票和金钱作为排名依据，呈现的是社区真正认可的内容。
- **零配置启动，30秒解锁全平台**：上手门槛极低。基础平台无需任何配置，高级平台通过一次性的向导式操作即可完成绑定，对新手非常友好。
- **跨50+宿主生态**：不仅支持 Claude Code，还兼容 Codex、Cursor、Copilot、Gemini CLI 等主流工具链，一次安装，随处可用。
- **透明的配置管理**：将技能规范存储在 `SKILL.md` 文件中，便于开发者审查和自定义行为。
- **开源且持续迭代**：项目代码开源，基于 MIT 协议，社区可以自由修改和扩展。

## 相关链接

- [GitHub 仓库](https://github.com/mvanhorn/last30days-skill)
- [Agent Skills 生态](https://agentskills.io)
