---
tags:
  - trending
  - article
repo: x1xhlol/system-prompts-and-models-of-ai-tools
date: 2026-06-12
language: Unknown
stars_total: 139976
stars_today: 368
---
## 项目概述

`system-prompts-and-models-of-ai-tools` 是一个精心整理的 AI 工具系统提示词（System Prompts）与模型信息汇总仓库。该项目旨在收集并公开包括 Augment Code、Claude Code、Cursor、Devin AI、Replit、Windsurf、Xcode 等数十款热门 AI 编程工具和 AI 应用背后的系统提示词、内部工具配置以及底层模型信息。

对于 AI 开发者、Prompt 工程师以及对 AI 工具内部机制感兴趣的研究者而言，这个仓库提供了一扇难得的窗口，让社区的每个人都能了解主流 AI 工具是如何通过系统提示词来引导和约束 AI 模型行为的。目前该仓库累计获得近 14 万颗 Star，是 GitHub 上同类主题中最受关注的项目之一。

## 核心功能

- **海量系统提示词收录**：收集了超过 30 款主流 AI 工具的系统提示词，包括产品级工具（如 Claude Code、Devin AI、Cursor、Windsurf）和开源工具（如 v0、Dia）。
- **模型信息汇总**：整理每款工具背后实际使用的 AI 模型（如 GPT-4、Claude Sonnet 等），帮助开发者了解业界最新模型选型动态。
- **内部工具配置公开**：部分条目附有工具的默认配置文件、内置指令集以及行为设定，可用于分析 AI Agent 的设计思路。
- **持续更新维护**：项目保持活跃更新，日均获得数百 Star，内容随新工具发布而动态补充。
- **社区协作生态**：关联 Discord 社群和赞助渠道，形成围绕 AI Prompt 探索的活跃社区。

## 技术架构

该项目本质上是一个基于 Markdown 的文档集合，采用纯文本的静态存储方式。其核心设计思路体现在以下方面：

- **结构化目录**：按照工具名称或类别将内容组织为独立 Markdown 文件，便于按需查找。
- **原生 Markdown 格式**：所有系统提示词以原始代码块形式保存，保留完整的格式和换行，确保可读性和可复制性。
- **版本兼容**：以文本文件形式追踪不同时间点的提示词变更，可以通过 Git 历史回溯内容演化。
- **零依赖**：无需任何运行时环境或构建工具，用户只需任意 Markdown 阅读器或浏览器即可查看全部内容。

## 安装与使用

使用该项目无需额外安装，只需以下几个步骤：

1. 访问 [GitHub 仓库](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
2. 点击右上角 `Code` 按钮，选择 `Download ZIP` 下载压缩包，或使用 Git 克隆仓库：
   ```bash
   git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools.git
   ```
3. 进入项目目录后，按工具名称浏览对应的 Markdown 文件。

**最小使用示例**：

```bash
# 以查看 Cursor 的系统提示词为例
cat "Cursor Prompt.txt"   # 在终端直接输出
# 或直接在 GitHub 仓库中浏览 code/cursor/ 目录
```

您也可以直接通过 Web 界面在线查看，无需本地任何操作。

## 适用场景

- **Prompt 工程研究与设计**：通过分析现有产品的系统提示词编写策略，学习如何构建高效的 AI Agent 指令框架，包括角色设定、行为约束、输出格式化等技巧。
- **工具选型参考**：在团队或项目中选择 AI 编码助手时，通过系统提示词判断不同工具的底层逻辑和适用性。例如了解 Cursor 的上下文管理策略与 Copilot 的差异。
- **AI 产品逆向分析**：在研究竞争产品或进行学术研究时，获取公开可用的系统提示词作为参考，用于理解商业 AI 产品在模型层面的工程化设计。
- **教育学习**：对 AI 初学者和开发者来说，阅读这些真实产品的提示词是理解“如何与 AI 高效沟通”的最佳实践教材。

## 项目亮点

与同类型项目相比，`system-prompts-and-models-of-ai-tools` 具有以下差异化优势：

- **规模最大**：收录的 AI 工具数量超过 30 款，覆盖从代码助手到通用 AI 助手（如 Perplexity、NotionAI）的广泛范围，是 GitHub 上同类主题中内容最全面的集合。
- **高可见度**：超过 13.9 万 Star 和每日数百的增长速度，证明其内容准确性和社区认可度极高，减少了用户甄别信息真伪的成本。
- **实时更新**：团队持续追踪最新版本的系统提示词变化，确保内容不过时。例如对比不同版本的 Claude Code 提示词，可以观察 AI 产品迭代的设计演进。
- **开源精神**：采用 GPL-3.0 开源协议，任何人皆可自由使用、分享和修改，与一些付费 API 解析服务形成鲜明对比。

## 相关链接

- [GitHub 仓库](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [LeaksLab Discord 社群](https://discord.gg/NwzrWErdMU)
