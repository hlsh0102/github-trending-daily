---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-07-07
language: JavaScript
stars_total: 51954
stars_today: 1378
---
## 项目概述

System Prompts Leaks 是一个持续更新的开源仓库，专门收集和整理各大 AI 聊天机器人的系统提示词（System Prompt）。这些提示词是模型行为背后的“隐藏规则”，决定了 AI 如何回答、如何思考、遵循哪些约束。项目覆盖 Anthropic（Claude Fable 5、Opus 4.8、Claude Code、Claude Design）、OpenAI（ChatGPT 5.5 Thinking、GPT 5.5 Instant、Codex）、Google（Gemini 3.5 Flash、3.1 Pro、Antigravity）以及 xAI（Grok）、Cursor、Copilot、VS Code、Perplexity 等多个主流 AI 产品。项目面向研究人员、开发者、产品经理以及对 AI 透明度感兴趣的普通用户，帮助他们理解不同 AI 系统的内在运作逻辑。该项目已被《华盛顿邮报》报道，影响力广泛，当前拥有超过 5 万星标。

## 核心功能

- **系统提示词收录**：收集并结构化呈现来自 Anthropic、OpenAI、Google、xAI 等多个厂商的 AI 系统提示词，持续更新最新版本。
- **版本差异对比**：提供关键模型版本之间的系统提示词差异对比，例如 Claude Opus 4.8 到 Claude Fable 5 的详细变化链接。
- **分类组织**：按照厂商和模型名称对提示词文件进行分类，方便用户快速定位特定产品。
- **近期更新追踪**：维护更新表格，标注每个提示词的收录日期和对应的 GitHub 链接，便于用户把握最新进展。
- **开源与可复现**：基于 CC0-1.0 许可证，任何人都可以自由使用、修改和分发这些系统提示词。

## 技术架构

项目采用纯 Markdown 文件组织内容，底层结构简单且易于参与。仓库根目录下按照厂商名称建立子目录（如 `Anthropic/`、`OpenAI/`、`Microsoft/`），每个子目录内放置对应模型的 `.md` 文件。文件内容直接展示完整的系统提示词文本，不涉及解析或渲染逻辑。项目还利用 `diffchecker.com` 等外部工具链接来展示版本间的差异，无需在仓库内维护复杂的差异比较功能。这种轻量级架构使得任何人都可以通过提交 Pull Request 来贡献新的系统提示词，降低了参与门槛并提高了更新频率。

## 安装与使用

由于本项目是纯文档集合，不需要安装任何软件。你只需通过 Git 克隆仓库：

```bash
git clone https://github.com/asgeirtj/system_prompts_leaks.git
cd system_prompts_leaks
```

然后直接进入对应厂商目录，用任何 Markdown 阅读器或文本编辑器打开感兴趣的提示词文件即可。例如，要查看 Claude Design 的系统提示词：

```bash
cat Anthropic/claude-design.md
```

如果你只希望获取特定模型的提示词，也可以直接在浏览器中访问 GitHub 上的文件夹路径，无需下载整个仓库。对于频繁更新的需求，建议定期 `git pull` 以获取最新内容。

## 适用场景

- **AI 研究与透明性分析**：研究人员可以比较不同厂商对 AI 行为约束的差异，分析系统提示词如何影响输出质量、安全性和偏见控制。
- **产品开发与提示工程**：开发者在设计自己的 AI 应用时，可以参考这些真实系统提示词的结构和措辞，优化自己的 prompt 设计。
- **教育与学习**：AI 初学者或爱好者可以通过阅读这些提示词，直观了解“模型是如何被教导的”，加深对 AI 行为机制的理解。
- **安全与合规审计**：安全团队可以审查这些提示词，评估潜在的风险点或不当约束，用于内部合规检查或第三方审计。

## 项目亮点

- **权威性高**：被《华盛顿邮报》引用，说明内容的真实性和影响力得到了主流媒体的认可。
- **更新频率快**：项目持续跟进最新模型发布，例如在 Claude Fable 5 发布后迅速提取其系统提示词并维护差异对比。
- **覆盖范围广**：不仅包括头部厂商的旗舰模型，还涵盖了 Copilot、Cursor、Perplexity 等垂直场景 AI 产品，形成了较完整的生态图谱。
- **协作门槛低**：纯 Markdown 文件、CC0 许可证、清晰的目录结构，任何人都能轻松参与贡献或派生使用。
- **工具集成**：通过 diff 链接直接对比版本变化，降低了手动比对的工作量，提升了阅读效率。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [《华盛顿邮报》相关报道](https://wapo.st/49t4gSb)
- [Claude Opus 4.8 → Claude Fable 5 差异对比](https://www.diffchecker.com/QJn9jFNk/)
