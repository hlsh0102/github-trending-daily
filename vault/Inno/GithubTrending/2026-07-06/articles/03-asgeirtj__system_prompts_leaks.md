---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-07-06
language: JavaScript
stars_total: 50365
stars_today: 981
---
## 项目概述

System Prompts Leaks 是一个持续更新的开源仓库，专门收集、整理和公开各大主流 AI 聊天机器人（如 Anthropic 的 Claude、OpenAI 的 ChatGPT、Google 的 Gemini、xAI 的 Grok 等）所使用的系统提示词（System Prompt）。该项目通过社区贡献和自动化手段，提取并保存了这些隐藏的“AI 行为规则”，使开发者、研究者和普通用户能够了解 AI 助手背后被预设的指令、约束和角色设定。

项目的目标用户包括 AI 安全研究人员、产品开发者、提示词工程师、模型行为分析师，以及对 AI 透明度和可解释性感兴趣的爱好者。截至文章撰写时，该仓库已获得超过 5 万颗 GitHub Star，并被《华盛顿邮报》引用报道，影响力可见一斑。

## 核心功能

- **系统提示词存档**：从 Anthropic、OpenAI、Google、xAI 等厂商的 AI 产品中提取并保存原始系统提示词，涵盖 Claude Fable 5、Opus 4.8、ChatGPT 5.5 Thinking、Gemini 3.5 Flash 等主流模型。
- **版本差异对比**：提供关键版本之间的差异对照（如 Claude Opus 4.8 到 Claude Fable 5 的 Diff），直观显示厂商如何调整 AI 行为规则。
- **多平台覆盖**：不仅记录网页版 AI 助手的提示词，还覆盖桌面客户端（如 GitHub Copilot for macOS）、IDE 集成（VS Code、Cursor）和专业工具（Claude Design）。
- **定期更新**：维护一个“最近更新”表格，记录每次新增或更新的提示词文件及对应日期，方便追踪最新进展。
- **开源协作与贡献**：基于 CC0-1.0 许可，任何人都可以提交 Pull Request 补充缺失的提示词或更新已有内容。
- **新闻引用与透明倡导**：被主流媒体引用，推动行业对 AI 系统行为透明度的关注。

## 技术架构

该项目本质上是一个结构化文档仓库，采用纯 Markdown 文件存储每个 AI 产品的系统提示词。仓库的顶层目录按厂商名称组织（如 `Anthropic/`、`OpenAI/`、`Google/`、`Microsoft/`），每个厂商目录下再按具体产品或模型细分文件。

核心的技术工作流包括：
1. **提示词获取**：通常通过特定的注入技巧（如要求 AI “重复你之前说过的话”），诱使模型在对话中输出其隐藏的系统指令。
2. **人工验证与清洗**：获取的原始文本需要人工去重、格式化，并与公开讨论对比确认准确性。
3. **版本管理**：通过 Git 的变更追踪和 Diff 工具（如 Diffchecker）记录同一模型不同版本的提示词变化。
4. **社区协作**：利用 GitHub Issues 和 Pull Requests 收集新发现、修正错误，保持仓库的时效性。

这种架构简单但高效，不依赖复杂后端，任何人都可以 fork 仓库或直接查看文件内容，降低了参与门槛。

## 安装与使用

该项目无需安装任何软件。使用方式十分直接：

1. 访问仓库首页：[https://github.com/asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)
2. 浏览根目录下的厂商文件夹（如 `Anthropic/`、`OpenAI/`），进入对应模型文件。
3. 直接查看 Markdown 文件内容，或利用 GitHub 的在线预览功能阅读。
4. 如需对比版本差异，可点击仓库中提供的 Diff 链接（如 [Claude Opus 4.8 → Claude Fable 5](https://www.diffchecker.com/QJn9jFNk/)）。

**最小可用示例**：要查看 Claude Fable 5 的系统提示词，只需打开 `Anthropic/claude-fable-5.md` 文件，即可看到完整的提示词文本，例如模型被要求 “你是 Claude，由 Anthropic 创建”“保持回答清晰、有帮助” 等规则。

## 适用场景

- **AI 安全与审计**：安全研究人员可以通过分析系统提示词，发现模型被注入的偏见、限制或隐蔽指令，评估模型行为是否符合预期安全标准。
- **提示工程与产品开发**：开发者在构建基于大模型的 AI 产品时，可以通过研究竞品的系统提示词，学习如何更有效地设计自己的角色设定、输出格式和约束条件。
- **学术研究与透明度倡导**：社会科学家和伦理研究者可以追踪不同厂商如何通过提示词塑造 AI 的行为边界，为 AI 治理和透明度政策提供实证数据。
- **教育与技术科普**：普通用户和 AI 爱好者可以通过阅读这些提示词，理解为什么同一个问题在不同 AI 助手那里会得到风格迥异的回答。

## 项目亮点

- **权威性与影响力**：被《华盛顿邮报》等主流媒体引用，证明了项目的公信力和关注度。拥有一套清晰的更新记录和版本对比机制。
- **跨厂商全覆盖**：不仅覆盖市场主流的 Claude、ChatGPT、Gemini，还延伸到 Cursor、Copilot、Perplexity、VS Code 等集成工具，视野开阔。
- **社区驱动、低门槛**：采用 CC0-1.0 许可，任何人都能自由使用、修改和分发数据。协作流程简单，鼓励贡献。
- **持续活跃**：仓库显示近期频繁更新（如 2026 年 6–7 月仍有 Claude Sonnet 5、Claude Design、GitHub Copilot 等内容新增），并非一次性存档。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [《华盛顿邮报》报道](https://wapo.st/49t4gSb)
- [Claude Opus 4.8 → Claude Fable 5 差异对比](https://www.diffchecker.com/QJn9jFNk/)
