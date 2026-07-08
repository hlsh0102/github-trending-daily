---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-07-08
language: JavaScript
stars_total: 53262
stars_today: 1691
---
## 项目概述

System Prompts Leaks 是一个持续更新的开源仓库，专门收集和整理各大 AI 聊天机器人的系统提示词（System Prompt）。该项目从 Anthropic 的 Claude 系列、OpenAI 的 ChatGPT/GPT 系列、Google 的 Gemini 系列，到 xAI 的 Grok、GitHub Copilot、VS Code、Perplexity 等主流 AI 产品，系统性地收录了被“泄露”或公开的系统层指令。项目由开发者 asgeirtj 维护，目标用户包括 AI 研究人员、提示词工程师、产品经理、安全分析师以及对 AI 行为机制感兴趣的普通用户。其核心理念在于揭示这些模型在接受用户输入前被设定的“规则”，帮助人们理解 AI 输出背后的隐性约束。

## 核心功能

- **跨平台系统提示词收集**：收录 Anthropic（Claude Fable 5、Opus 4.8、Claude Code、Claude Design）、OpenAI（ChatGPT 5.5 Thinking、GPT 5.5 Instant、Codex）、Google（Gemini 3.5 Flash、3.1 Pro、Antigravity）、xAI（Grok）以及 Microsoft（Copilot、VS Code）、Perplexity 等十余种 AI 产品的系统提示词。
- **版本差异对比**：提供 Claude Opus 4.8 到 Claude Fable 5 等模型的系统提示词变更对比（Diff），直观展示每次更新中模型行为规则的调整。
- **完整提示词还原**：部分条目（如 Claude Design）不仅包含核心指令，还还原了完整的工具定义、技能列表、推荐资源来源等细节，呈现模型的完整运行上下文。
- **持续更新追踪**：仓库以近乎实时的频率更新，标记有“Recently Updated”表格，包含最新泄露日期和对应的文件链接。
- **结构化分类存储**：按公司（Anthropic、OpenAI、Google、Microsoft、xAI 等）分目录组织文件，命名规范，便于检索和引用。

## 技术架构

该项目是一个纯文档仓库，采用 Markdown 格式存储系统提示词文本，不需要编译或运行。其技术架构特点包括：

- **静态文件存储**：所有系统提示词以 `.md` 文件形式按公司目录存放，无数据库或后端依赖，方便任何人直接浏览和 Fork。
- **差异对比支持**：利用 Diffchecker 等外部工具链接而非内建 diff 功能，将系统提示词的版本变化呈现为可控的 URL，降低仓库体积。
- **轻量级展示**：仓库使用 GitHub 原生功能（README 表格、图片、徽章）提供预览，无需构建工具或 CI/CD 流程。
- **开源许可**：采用 CC0-1.0 协议，允许自由使用、复制、修改和分发，降低再利用门槛。
- **社区驱动更新**：依赖用户通过 Issue 或 Pull Request 提交新发现的提示词，形成分布式收集网络。

## 安装与使用

由于该项目本质上是一个公开的文档集合，无需“安装”即可使用。用户可直接通过 GitHub 仓库浏览器端访问：

1. 访问仓库主页：`https://github.com/asgeirtj/system_prompts_leaks`
2. 查看 README 中的“Recently Updated”表格，点击链接进入具体模型页面。
3. 例如，要查看 Claude Fable 5 的系统提示词，点击 `Anthropic/claude-fable-5.md` 即可看到完整文本。

若需本地使用，可执行：

```bash
git clone https://github.com/asgeirtj/system_prompts_leaks.git
cd system_prompts_leaks
# 直接查看对应文件
cat Anthropic/claude-fable-5.md
# 或使用文本编辑器打开
```

也可以直接使用 GitHub 的 Web 界面或 Raw 文件链接进行查阅。对于批量分析，可使用 `grep`、`sed` 等工具结合文件路径进行文本挖掘。

## 适用场景

- **AI 行为分析与审计**：研究人员通过对比不同模型的系统提示词，分析其安全策略、价值观对齐方式以及内容过滤规则，评估模型的行为边界。
- **提示词工程优化**：提示词工程师通过阅读官方系统提示词，了解模型被设定遵循的指令层级，从而设计更精准、更高效的提示策略。
- **产品竞争情报**：产品经理和创业者通过跟踪各大 AI 公司在系统提示层做出的调整（如 Claude 从 Opus 到 Fable 的变更），洞察行业趋势和产品迭代方向。
- **教育与科普**：AI 科普作者或教育者利用这些真实案例，向公众解释 AI 模型为何具有某些行为模式，以及“系统提示”作为隐性规则的运作机制。

## 项目亮点

- **权威性与时效性**：已受《华盛顿邮报》引用报道（2026年5月），且更新频率极高（日更级别），收录的提示词通常来自最新模型版本。
- **覆盖广度**：从主流大厂（Anthropic、OpenAI、Google）到新兴玩家（xAI、Cursor）再到工具类 AI（Copilot、Perplexity），覆盖面远超同类项目。
- **差异化分析支持**：不仅提供静态快照，还通过外部 Diff 工具实现版本间差异对比，方便追踪细微调整。
- **开源与透明**：CC0-1.0 协议允许任何形式的再利用，研究者可将其纳入自己的分析工具链，无需额外授权。
- **结构清晰**：按公司-模型-版本的三级目录组织，搭配 README 表格索引，在数百个文件中保持可浏览性。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [Claude Opus 4.8 → Fable 5 Diff](https://www.diffchecker.com/QJn9jFNk/)
- 《华盛顿邮报》报道：[See the hidden rules behind AI. Then use them to rewrite this article.](https://wapo.st/49t4gSb)
