---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-07-09
language: JavaScript
stars_total: 54466
stars_today: 1218
---
## 项目概述

System Prompts Leaks 是一个持续更新的开源项目，专门收集和整理各大 AI 聊天机器人的系统提示（System Prompt）指令。这些系统提示是 AI 模型运行时的底层规则，决定了模型的行为模式、能力边界和使用限制。项目涵盖了 Anthropic（Claude 系列）、OpenAI（ChatGPT、GPT、Codex）、Google（Gemini）、xAI（Grok）以及 Microsoft（Copilot）等主流厂商的模型，并通过社区贡献不断补充新内容。

该项目解决了两个核心问题：一是为研究人员和开发者提供了查看 AI 模型“底层指令”的窗口，帮助理解不同模型的设计哲学和行为差异；二是通过公开这些原本属于黑盒的内部规则，促进了 AI 透明度和可审查性。

## 核心功能

- **模型系统提示收集**：收录了包括 Claude Fable 5、Opus 4.8、Sonnet 5，ChatGPT 5.5 Thinking、GPT 5.5 Instant、Codex，Gemini 3.5 Flash、3.1 Pro，以及 Grok、Cursor、Copilot、VS Code、Perplexity 等数十款 AI 模型的系统提示全文
- **差异对比**：为同一模型的不同版本提供差异对比功能。例如，项目支持对比 **Claude Opus 4.8 → Claude Fable 5** 之间的系统提示变化，使用 Diffchecker 工具展示具体改动
- **持续更新**：项目保持活跃更新，按月跟踪模型迭代。例如 2026 年 7 月更新了 Claude Sonnet 5，6 月更新了 GPT-5.5 Codex 和 Copilot macOS 应用版本
- **格式化文档**：所有系统提示以 Markdown 文件形式存储，按供应商和模型分类组织，便于阅读和对比
- **开源开放**：采用 CC0-1.0 许可证，允许任何人自由使用、复制和分发

## 技术架构

项目以纯文本和 Markdown 文件为主要存储格式，采用仓库目录结构按照供应商名称（如 `Anthropic/`、`OpenAI/`、`Microsoft/`）进行组织，每个模型对应一个独立的 Markdown 文件。

设计上遵循以下原则：
- **零依赖**：项目不需要编译、运行或构建工具，直接通过 Git 托管文本内容即可工作
- **版本化管理**：利用 GitHub 的版本历史记录每一次系统提示的更新，便于追踪变化
- **社区协作**：通过 Pull Request 接受来自全球贡献者的补充和修正，降低维护成本
- **多媒体支持**：包含图片展示（如系统提示泄漏的截图）和外部工具链接（如 Diffchecker 对比结果）

这种轻量级架构使得项目易于维护、传播和二次利用。

## 安装与使用

由于本项目是纯文档仓库，无需安装任何软件。使用方式如下：

1. **直接浏览**：访问 GitHub 仓库首页，按目录结构查找感兴趣的模型
2. **克隆仓库**：
   ```bash
   git clone https://github.com/asgeirtj/system_prompts_leaks.git
   cd system_prompts_leaks
   ```
3. **查看系统提示**：进入对应供应商目录，打开 Markdown 文件即可阅读完整内容
4. **对比版本更新**：点击 README 中的 Diff 链接，跳转到 Diffchecker 查看不同版本间的具体差异

最小示例：在仓库中找到 `Anthropic/claude-sonnet-5.md` 文件，即可查看 Claude Sonnet 5 的全部系统提示指令。

## 适用场景

- **AI 安全研究**：研究人员可以通过分析系统提示了解模型的安全措施、内容审核策略和道德约束，评估潜在风险
- **产品竞品分析**：AI 产品团队可以对比不同厂商模型的设计思路，借鉴其在行为引导、错误处理、用户交互等方面的做法
- **开发者调优参考**：应用开发者通过理解底层提示词设计，可以更好地设计自己的 AI 应用提示，或在微调模型时参考这些规则
- **透明度审查**：新闻机构（如 The Washington Post 已引用该项目）、政策制定者和公众可以利用这些信息监督 AI 产品的合规性和公平性

## 项目亮点

- **独家收录深度**：不仅捕获了通用对话模型，还包含了 Claude Design（附带 48 个工具、16 个技能、9 个启动来源的完整信息）、GPT-5.5 Codex（完整提示词）等专业模型的系统提示，内容深度远超同类项目
- **媒体背书**：项目已被《华盛顿邮报》引用（2026 年 5 月），标志着其在新闻编辑室和研究领域获得了权威认可
- **版本追踪体系**：通过 Diff 链接对比同一模型不同版本的变化，为用户呈现模型行为调整的精确细节
- **高影响力**：截至 2026 年 7 月，获得超过 54,000 颗星标，单日新增 1,200+，说明社区对其价值的高度认可
- **实时性**：紧跟模型发布节奏，在 Claude Sonnet 5 发布当天就完成了系统提示的提取和提交

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [华盛顿邮报报道](https://wapo.st/49t4gSb)（需付费阅读）
- [Diff: Claude Opus 4.8 → Claude Fable 5](https://www.diffchecker.com/QJn9jFNk/)
