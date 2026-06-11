---
tags:
  - trending
  - article
repo: x1xhlol/system-prompts-and-models-of-ai-tools
date: 2026-06-11
language: Unknown
stars_total: 139635
stars_today: 393
---
## 项目概述

System Prompts and Models of AI Tools 是一个大规模、持续更新的 AI 工具系统提示词（System Prompts）与内部模型信息收集库。该项目收录了包括 Augment Code、Claude Code、Cursor、Devin AI、Replit、Windsurf、Xcode 等在内的数十款主流 AI 开发工具和平台的内置系统提示词、使用模型以及底层架构信息。项目面向 AI 开发者、提示词工程师、技术研究人员以及所有对 AI 工具内部机制感兴趣的用户，帮助他们理解不同产品如何设计 AI 交互逻辑、限制行为边界以及优化用户体验。

## 核心功能

- **系统提示词收录**：收集了 30+ 款主流 AI 工具（如 Cursor、Claude Code、CodeBuddy、Comet、Perplexity 等）的完整系统提示词原文，涵盖代码助手、UI 生成器、通用对话 Agent 等多种类型。
- **模型信息汇总**：明确列出每款工具所使用的底层 AI 模型（如 GPT-4、Claude 3.5、自研模型等），以及模型版本与切换策略。
- **开源工具补充**：除商业闭源工具外，还包含 Latitude LLM 等开源项目的提示词与架构资料，提供更全面的研究视角。
- **持续追踪更新**：项目活跃维护，每日更新（近期 +393 stars），紧跟新工具发布与既有工具更新。
- **社区资源入口**：提供 Discord 讨论群组、Trendshift 趋势排名等外部链接，方便交流与发现。

## 技术架构

该项目本质上是一个 Markdown 格式的知识仓库，不做复杂的前后端部署。其技术价值主要体现在以下方面：

- **结构化分类**：按工具名称分目录或分文件组织，每份收录内容保持统一的格式（工具介绍、系统提示词原文、使用模型、适用场景等），便于横向对比。
- **逆向工程视角**：多数系统提示词通过分析公开版本、用户反馈、网络抓取等途径获取，反映了 AI 产品在提示设计上的实际商业实践。
- **开源协作机制**：基于 GitHub 仓库的 Issue 和 PR 机制，社区成员可贡献新发现或修正已有内容，结合 GPL-3.0 许可证确保知识自由传播。
- **品牌化展示**：通过 README 中的 Latitude Logo 和广告位，为相关开源项目（如 Latitude LLM）提供曝光，形成生态连接。

## 安装与使用

本仓库为纯静态文档集合，无需安装或编译。使用方式如下：

1. 克隆或下载仓库：
   ```bash
   git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools.git
   ```

2. 浏览仓库目录，找到感兴趣的工具对应的 Markdown 文件（通常以工具名称命名），用任何 Markdown 阅读器（如 VS Code、Typora 或 GitHub 内置预览）打开即可查看。

3. 如需搜索特定关键词（如“code review”或“Claude”），使用 grep 或 GitHub 仓库内的搜索功能。

最小可用示例：直接打开仓库根目录，找到 `cursor/` 或 `devin/` 等文件夹，阅读其中的提示词文件，即可了解该工具的核心交互逻辑。

## 适用场景

- **AI 产品设计参考**：工具开发者在设计自己的 AI Agent 或 Copilot 时，可参考这些已商业验证的系统提示词结构和行为约束策略。
- **提示词工程研究**：研究人员可对比分析不同工具如何通过提示词实现功能隔离、角色扮演、隐私保护等效果。
- **技术拆解与学习**：AI 学习者在理解“大型语言模型如何被商业产品调用”这一黑箱时可以获取一手资料。
- **横向竞品分析**：产品经理和开发者可快速对比多款代码助手/Agent 的底层模型选择与设计哲学差异。

## 项目亮点

- **数量与广度领先**：收录 30+ 款工具，覆盖代码补全、全栈应用生成、通用对话、项目管理等多种 AI 应用形态，远超同类项目。
- **高社区活跃度**：超过 13.9 万 Stars 和每日数百的增长速度，表明项目获得了大量开发者认可和持续关注。
- **真实性承诺**：项目不进行内容润色或虚构，力求原始提示词的准确转录，这对研究和产品设计具有直接参考价值。
- **零门槛访问**：无需注册或付费，所有内容开源可见，且许可证明确允许自由使用和再分发。
- **生态联动**：通过赞助商链接和外部社区（Discord、Patreon、Ko-fi）建立了可持续的协作和财务支持模型。

## 相关链接

- [GitHub 仓库](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [项目 Discord 社区](https://discord.gg/NwzrWErdMU)
- [Trendshift 趋势页](https://trendshift.io/repositories/14084)
