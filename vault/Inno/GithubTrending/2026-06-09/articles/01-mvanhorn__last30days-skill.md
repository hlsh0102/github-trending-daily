---
tags:
  - trending
  - article
repo: mvanhorn/last30days-skill
date: 2026-06-09
language: Python
stars_total: 35273
stars_today: 3558
---
## 项目概述

/last30days 是一个基于 AI 代理的搜索引擎技能（Skill），能够自动跨 Reddit、X（Twitter）、YouTube、Hacker News、Polymarket 以及整个 Web 对任意主题进行研究，并生成一份扎实的摘要报告。该项目解决了传统搜索引擎依赖编辑推荐或算法排序的问题，转而使用来自多个社交平台和预测市场的真实用户反馈信号（如点赞、投票、金钱投入）来评估信息质量。目标用户包括需要快速了解某个话题热度的开发者、研究人员、内容创作者、投资分析师，以及任何希望从多元化社交源头获取权威观点的一线人员。

## 核心功能

- **跨平台全自动研究**：一条命令即可同时搜索 Reddit、X、YouTube、Hacker News、Polymarket 等多个平台，无需手动在不同站点间切换。
- **信号评分机制**：基于 upvotes、likes、以及 Polymarket 上的真实金钱押注来排序结果，而非编辑或算法推荐，确保信息来自真实社区的选择。
- **零配置启动**：Reddit、Hacker News、Polymarket、GitHub 开箱即用，无需 API 密钥；运行一次后通过内置向导可在 30 秒内解锁 X、YouTube、TikTok 等平台。
- **合成摘要输出**：AI 代理将所有搜索结果整合为一份连贯、基于事实的摘要，包含关键趋势、观点分歧和主要信源引用。
- **多云 IDE 兼容**：支持 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等 50 多种 Agent Skills 宿主，安装方式统一。
- **全局或项目作用域安装**：通过 `npx skills add` 命令可选全局安装（`-g` 标志），即可在任何项目中直接调用，或按项目范围安装以保持环境隔离。

## 技术架构

该项目采用 **Agent Skills** 标准架构，本质是一个可被多种 AI 代码助手执行环境加载的“技能包”。其核心技术栈包括：

- **技能定义文件**：`SKILL.md` 是运行时命令和设置行为的唯一真实来源，定义了搜索、摘要生成的接口和流程。它采用类似 OpenAPI 的方式描述 AI 代理可执行的任务。
- **多源聚合引擎**：在 Python 中实现数据抓取与规范化，将不同平台（社交媒体、预测市场、论坛）的异构数据结构（帖文、评论、投注、分）统一处理，便于后续排序与摘要生成。
- **信号权重算法**：为不同平台的反馈信号赋予合理的权重（例如 Polymarket 的金钱押注可能高于常规点赞），综合计算每个资源的“可信度分数”，确保高价值内容出现在结果前列。
- **模块化集成设计**：不同平台作为独立的连接器模块，核心搜索逻辑与平台特定实现解耦。用户只需配置一次 API 密钥，技能会自动选择可用模块工作。
- **安全沙盒执行**：所有网络请求、文件读写和命令执行均在宿主环境的沙盒中运行，安装无需 `sudo` 或额外权限。

该架构的最大特点是 **声明式配置 + 代理驱动执行**：用户只需关心“研究什么”，而 AI 代理负责“怎么研究、怎么总结”。

## 安装与使用

### 安装（推荐方式）

**Claude Code（自动更新）：**
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

**其他宿主（Codex, Cursor, Copilot, Gemini CLI 等）：**
```
npx skills add mvanhorn/last30days-skill -g
```
`-g` 表示全局安装，可在任意项目中使用；去掉 `-g` 则仅当前项目可用。

更多安装选项（claude.ai 网页版、OpenClaw、手动方式）请查看项目的 [Install 章节](https://github.com/mvanhorn/last30days-skill#install)。

### 最小可用示例

1. 安装完技能后，在支持的 AI 助手中输入：
   ```
   /last30days what are the latest trends in AI agents?
   ```

2. 技能自动搜索 Reddit、HN、YouTube、X、Polymarket 等平台，收集过去 30 天内的相关内容。

3. 返回一份结构化摘要：
   - **Top sources by score**：列出得分最高的来源（如某条 Reddit 帖文、某个 YouTube 视频）
   - **Key themes**：总结出现的主要话题和观点
   - **Notable disagreements**：指出不同社区之间的观点分歧
   - **Most referenced papers/code**：如有，列出被多次引用的论文或仓库

初次运行时，技能会提示配置 X、YouTube 等平台的 API 密钥（可选），按提示操作后即可解锁全部搜索能力。

## 适用场景

- **趋势快速调研**：当需要了解某个领域（如“边缘计算”、“开源替代品”）最近 30 天的热门讨论、关键人物和代表性内容时，一条命令即可获得全局视图。
- **产品验证与竞争分析**：创业者或产品经理可用其搜索目标市场在 Reddit、HN 等平台上的用户反馈，结合 Polymarket 的预测信息判断市场接受度。
- **内容创作选题**：博主、YouTuber、Podcaster 可使用该技能发掘当下最具讨论价值的主题，甚至直接获取适合引用的高赞评论或视频。
- **投资与政策分析**：分析师可快速获取关于某个事件（如“美联储加息影响”、“下一代芯片设计”）的多方声音，结合预测市场的金钱信号做出更知情判断。

## 项目亮点

与传统的单一来源搜索或纯 AI 摘要工具相比，/last30days 的核心差异化在于：

1. **非编辑化排序**：摒弃专家/编辑推荐，完全依赖社区真实反馈（点赞、投票、金钱）来评估信息重要性，结果更贴近大众真实关注。
2. **预测市场信号**：引入 Polymarket 数据，使分析结果具备“金钱投票”维度，能反映对未来事件的概率判断，这是常规搜索引擎无法提供的。
3. **零配置即可用**：多数平台无需任何 API 密钥设置，安装后第一个搜索即可执行，大幅降低了工具的试用门槛。
4. **AI 原生集成**：作为 Agent Skills 标准技能，它深深嵌入开发者日常使用的 AI 代码助手环境，而非独立的网页或终端工具，工作流更自然。
5. **模块化扩展性**：用户可自行添加新的数据源连接器，或调整信号权重，以适应特定领域需求。

## 相关链接

- [GitHub 仓库](https://github.com/mvanhorn/last30days-skill)
- [Agent Skills 生态](https://agentskills.io)
- [Trendshift 趋势榜](https://trendshift.io/repositories/21997)
