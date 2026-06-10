---
tags:
  - trending
  - article
repo: x1xhlol/system-prompts-and-models-of-ai-tools
date: 2026-06-10
language: Unknown
stars_total: 139277
stars_today: 79
---
## 项目概述

System Prompts and Models of AI Tools 是一个系统提示词与 AI 模型信息的大型开源集合库。该项目旨在系统性地收集、整理并公开当今主流 AI 编码助手、智能代理和开发工具所使用的幕后系统提示词、内部工具定义以及相关模型信息。它解决的核心问题是：开发者和研究人员难以了解 AI 工具在底层如何配置、提示和限制其行为，尤其对于闭源工具而言。项目的目标用户包括 AI 工程师、提示工程师、技术研究者、希望深度理解工具行为的高级开发者，以及关注 AI 应用透明度的社区成员。目前该仓库已获得超过 13.9 万颗星标，是 AI 工具逆向工程和信息共享领域最受关注的项目之一。

## 核心功能

- **系统提示词收录**：收集了大量 AI 编码工具（如 Cursor、Windsurf、Replit、Devin AI、Claude Code 等）的系统级提示词，帮助理解每个工具如何引导 AI 的行为模式、回复格式和操作权限。
- **模型信息清单**：整理了多个工具使用的底层 AI 模型名称、版本及其切换机制，便于比较不同工具在模型选择上的差异。
- **内部工具与函数定义**：公开了部分工具内置的辅助函数、文件操作 API、Web 搜索工具、Shell 执行工具等内部定义，揭示 AI 代理能力的具体实现方式。
- **跨工具对比整合**：覆盖超过 25 个主流工具，包括 Cursor、CodeBuddy、Perplexity、NotionAI、Trae、Traycer AI、Xcode 等，以及开源替代方案 Dia 与 v0。
- **结构化的文件组织**：每个工具或模型以独立文件或子目录形式组织，便于针对性查阅和引用。

## 技术架构

该项目本质上是一个静态信息集合库，采用纯文本 Markdown 和 JSON 文件作为数据载体。核心设计思路是“透明化逆向工程”——通过分析 AI 工具在交互过程中暴露的客户端提示词、配置文件和 API 行为，提取并结构化存储其核心提示逻辑。技术特点包括：

- **轻量无依赖**：全仓库只包含 Markdown、JSON 和少量辅助脚本，无需构建或运行时环境，任何能浏览 GitHub 的用户均可直接阅读。
- **社区驱动协作**：通过 GitHub Issues 和 Pull Request 机制接受贡献，许多提示词由社区成员通过官网抓取、客户端调试或逆向分析获得。
- **版本追踪**：利用 Git 的版本控制能力，记录每个工具有所更新时其系统提示词的变化历史，便于对比不同时间线的版本差异。
- **模块化目录结构**：每个工具对应一个单独的文件（如 `cursor-system-prompt.md`、`windsurf-system-prompt.md`），特殊情况以子文件夹存放多个版本或补充资料。

## 安装与使用

本项目为纯内容仓库，无需安装。使用方式如下：

1. **克隆或查阅**：直接访问仓库页面 `https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools`，或在本地执行：
   ```bash
   git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools.git
   ```

2. **查阅特定工具的提示词**：在仓库根目录或子目录中寻找对应文件。例如，查看 Cursor 的所有系统提示词，可打开 `cursor/` 文件夹下的 `cursor-system-prompt.md`。

3. **搜索对比**：通过 GitHub 的搜索功能或本地 grep，在不同工具的文件中搜索关键字（如 `restricted actions`、`output format`），以比较不同工具对 AI 行为的约束差异。

4. **参考与引用**：开发者可将这些提示词用于自己的项目设计、提示工程学习，或在研究报告中作为引用资料。

最小示例：只需一条命令即可查看 Cursor 的核心系统行为规则：
```bash
cat cursor/cursor-system-prompt.md | head -50
```

## 适用场景

- **提示工程研究**：研究顶尖团队如何设计系统级提示词来精确控制 AI 助手的输出风格、安全边界和协作模式，从而优化自己的提示策略。
- **AI 工具选型比较**：在选择 AI 编码助手（如 Cursor vs Windsurf vs Replit）时，通过对比它们的系统提示词来了解各工具在上下文长度、代码审查深度、自动工具调用等方面的差异。
- **AI 透明性审计**：安全研究人员或隐私倡导者可以审查这些闭源工具的内部行为约束是否合规，例如是否过度收集数据、是否限制用户对代码库的操作权限。
- **教育与培训**：将真实案例用于提示工程课程或技术会议演讲，让学生或同行看到 AI 工具背后的核心逻辑。

## 项目亮点

- **极高的社区认可度**：超过 13.9 万星标，表明该项目在开发者社区中拥有高度信任和广泛引用，是 AI 工具透明化运动的标志性项目。
- **覆盖面广**：从开发者环境（Cursor、Windsurf、Xcode）到通用 AI 代理（Devin AI、Manus、NotionAI）再到流行服务（Perplexity、Claude Code），几乎囊括全部主流 AI 编码和办公助手。
- **动态更新**：项目会追踪工具的版本迭代，当 Cursor 或 Windsurf 更新系统提示词时，社区会迅速更新对应文件，保持内容时效性。
- **无学术壁垒**：无需特殊许可或付费，任何人都能自由获取和分发这些信息，符合开源精神的透明性与可访问性。

## 相关链接

- [GitHub 仓库](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [LeaksLab Discord 社区](https://discord.gg/NwzrWErdMU)（用于讨论和贡献）
- [Trendshift 项目趋势页](https://trendshift.io/repositories/14084)
