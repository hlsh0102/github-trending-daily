---
tags:
  - trending
  - article
repo: mvanhorn/last30days-skill
date: 2026-07-07
language: Python
stars_total: 49954
stars_today: 458
---
## 项目概述

`last30days-skill` 是一个由 AI 智能体驱动的搜索技能，能够自动检索 Reddit、X（原 Twitter）、YouTube、Hacker News、Polymarket 以及整个网络上的任意话题，并综合生成有据可查的总结报告。该项目解决了传统搜索引擎依赖编辑推荐或 SEO 排序的问题，转而以点赞数、收藏量和真实金钱（如 Polymarket 的预测市场）作为内容可信度的衡量标准。目标用户包括需要快速了解某个话题近期讨论热点的开发者、研究人员、内容创作者以及做技术趋势研判的产品经理。

## 核心功能

- **多平台聚合搜索**：同时从 Reddit、Twitter、YouTube、Hacker News、Polymarket 及通用网页抓取信息，覆盖社交讨论、视频内容、预测市场和常规资讯。
- **证据驱动的总结生成**：AI 智能体根据平台权重和参与度（点赞、评论、收益）筛选高价值信息，而非仅依赖搜索引擎的文本相关性。
- **零配置即装即用**：安装后无需配置 API 密钥或服务端，通过命令行即可直接使用。
- **跨编辑器/IDE 兼容**：支持 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等 50 多个支持 Agent Skills 标准的主机环境。
- **全局与项目级安装**：通过 `-g` 参数可安装为全局命令，在所有项目中可用；不加参数则局限于当前项目。
- **实时趋势感知**：自动限定在“最近30天”的时间窗口内，确保输出的信息具有时效性。

## 技术架构

该项目基于 **Agent Skills** 开放标准构建，每个技能以独立插件形式运行。核心使用 **Python** 编写，利用异步抓取框架同时向多个平台发起请求，并通过大型语言模型（LLM）对返回结果进行总结与生成。其设计思路强调“搜索即技能”——将搜索引擎的中间层抽象为可插拔的 AI 能力，而非传统的 Web 应用。架构特点包括：

- 使用 `npx skills` 作为技能管理器，实现跨环境的统一安装与调用。
- 技能定义文件 `SKILL.md` 作为单一事实来源，描述命令、参数和执行逻辑。
- 采用模块化处理器分别应对不同数据源，每个处理器负责该平台的认证、限流和数据结构化解析。
- 利用 LLM 的上下文能力，将多源异构数据（如帖子、视频标题、预测市场价格）融合为连贯的总结。

## 安装与使用

**前提条件**：需要 Node.js（用于运行 `npx skills`）以及 Python 3.10+ 环境。

**安装步骤**：

1. **使用 Claude Code（推荐，自动更新）**：
   ```
   /plugin marketplace add mvanhorn/last30days-skill
   /plugin install last30days
   ```

2. **使用其他 Agent Skills 宿主（如 Codex、Cursor、Gemini CLI）**：
   ```
   npx skills add mvanhorn/last30days-skill -g
   ```
   添加 `-g` 标志全局安装，省略则仅作用于当前项目。

3. **验证安装**：
   在支持 Agent Skills 的终端中，输入技能名称（如 `last30days "AI coding assistant trends"`），若返回总结结果即安装成功。

**最小可用示例**：

```
last30days "Rust vs Go in 2024"
```

执行后，技能会自动搜索 Reddit、Hacker News、YouTube 等平台近30天的相关内容，并输出包含来源链接和关键发现的格式化总结。

## 适用场景

- **技术趋势调研**：快速了解某技术栈（如 WebAssembly、边缘计算）过去一个月的讨论热点、常见问题以及社区情绪。
- **事件回顾与分析**：结合 Polymarket 的预测市场数据，分析某个突发事件（如AI监管法案）对市场参与者预期的影响。
- **竞品监测**：监控特定行业关键词在 Reddit 和 Twitter 上的提及频率与情感倾向，辅助产品决策。
- **内容创作素材收集**：为博客文章、视频脚本等搜集网络上已被验证的高赞观点和案例，确保内容有据可查。

## 项目亮点

与传统的搜索工具或 Web Agent 相比，`last30days-skill` 的差异化优势在于：

- **反编辑偏见**：不依赖人工编辑或 SEO 排名，而是以社区互动（点赞、收藏）和真实金融合约（Polymarket）作为内容质量信号。
- **零配置、零服务**：不需要注册第三方 API 或维护持久化服务端，一键安装即拥有完整的搜索能力。
- **生态兼容性**：遵循 Agent Skills 标准，可在主流 AI 编程助手和 CLI 环境中无缝切换，避免了锁定到单一平台。
- **时间窗口限定**：强制聚焦于最近30天，避免了传统搜索中大量过时信息的干扰，确保答案始终具备时效性。

## 相关链接

- [GitHub 仓库](https://github.com/mvanhorn/last30days-skill)
- [Agent Skills 官网](https://agentskills.io)
