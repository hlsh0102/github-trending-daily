---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-09-15
language: JavaScript
stars_total: 66993
stars_today: 764
---
## 项目概述

System Prompts Leaks 是一个持续维护的系统提示词（system prompt）归档仓库。项目从 Anthropic、OpenAI、Google、xAI 等主流 AI 厂商的对话产品与编程工具中，提取并逐字记录模型在接收用户第一条消息之前所加载的隐藏指令，覆盖 Claude、ChatGPT、Gemini、Grok、Cursor、Kimi 等产品线。

这些系统提示词通常不会对用户公开，但它们实质上决定了模型的行为边界：语气风格、拒答策略、工具调用规则、安全约束、输出格式要求等。开发者、研究者与产品经理往往只能通过逆向推测来了解这些规则，而该项目提供了一个集中、可检索、带时间戳的原始文本集合，解决了提示词不透明、难以对比、版本变化无迹可循的问题。

目标用户包括：构建 AI 应用的开发者（需要参考官方提示词工程实践）、AI 安全与对齐研究者、撰写行业分析的产品与媒体人员，以及对模型行为机制感兴趣的普通用户。项目采用 CC0-1.0 许可，允许自由使用与再分发。截至仓库统计，已获得约 6.7 万星标。

## 核心功能

- **多厂商提示词归档**：按厂商与产品分目录整理，包括 Anthropic（Claude Fable 5.1、Opus 5、Claude Design、Claude Code）、OpenAI（ChatGPT GPT-6-Astra、Codex）、Google（Gemini 3.8 Flash、3.1 Pro、Antigravity）、xAI（Grok、Grok Bot），以及 Cursor、Kimi 等第三方工具。
- **逐字原文记录**：以 Markdown 文件保存提示词原文，而非摘要或转述，便于直接阅读与比对。
- **变更时间线追踪**：仓库首页维护「最近新增/变更」表格，标注具体日期与文件链接，可观察同一产品提示词的迭代过程。
- **多形态产品覆盖**：不仅包含聊天助手，也包含本地运行形态（如 ChatGPT Work Codex local）、无头模式（如 Claude Code headless）等不同部署场景下的提示词。
- **开放贡献机制**：接受 Pull Request，社区可提交新捕获的提示词或更新版本。
- **被外部引用验证**：华盛顿邮报基于本仓库提示词制作交互报道，CEPS 的 AI World 基于仓库文件构建了实时数据看板，说明内容具备一定的行业参考价值。

## 技术架构

仓库以 JavaScript 为主要语言，但核心内容资产是结构化组织的 Markdown 文档，而非复杂应用逻辑。整体设计思路偏向「内容优先」：

- **目录即分类**：按厂商（OpenAI、Google、Anthropic、xAI 等）划分顶层目录，再按产品或模型分文件，命名体现模型名称与形态（如 `gpt-6-astra-chatgpt-work-local.md`、`gemini-3.8-flash.md`）。
- **元数据靠约定维护**：通过 README 中的表格记录变更时间，而非依赖数据库或构建流程，降低了维护门槛。
- **静态可消费**：由于全部为纯文本 Markdown，外部项目可以直接抓取、解析或生成为数据集，无需专用 API。
- **低依赖、易分发**：JavaScript 部分主要用于仓库的辅助脚本与展示，整体不依赖重型框架，便于长期存续与镜像。

这种轻量架构的取舍是明确的：牺牲自动化采集与校验能力，换取可读性、可审计性与低维护成本。

## 安装与使用

作为内容型仓库，通常不需要构建即可使用：

1. 克隆仓库：

```bash
git clone https://github.com/asgeirtj/system_prompts_leaks.git
cd system_prompts_leaks
```

2. 浏览目录结构，按厂商或产品定位目标文件：

```bash
ls OpenAI/Codex/
cat Google/gemini-3.8-flash.md
```

3. 若仓库包含 JavaScript 辅助脚本，可按 README 说明安装依赖并运行：

```bash
npm install
npm run <script>
```

最小可用示例即直接打开任意 `.md` 文件阅读提示词原文。由于提示词会随产品更新而变化，建议结合 README 的变更表格确认文件对应的时间版本，并在引用时标注捕获日期。若需集成到自有系统，可将 Markdown 解析为纯文本后作为参考文本注入到评测或对比流程中。

## 适用场景

- **提示词工程参考**：开发者在设计自有 Agent 或助手的系统提示词时，可参考头部厂商在工具调用、格式约束、拒答边界上的写法。
- **模型行为分析与评测**：研究者对比不同厂商、不同版本提示词的差异，观察安全策略与产品定位如何通过文本体现。
- **AI 安全与合规研究**：分析厂商在提示词层面设置的内容边界与免责机制，用于政策讨论或审计。
- **媒体与教学素材**：记者、讲师可直接引用原文，向公众解释「AI 在回答之前被交代了什么」。

## 项目亮点

- **原文而非二手转述**：逐字捕获保证了信息保真度，避免了二次加工带来的失真。
- **覆盖广度与更新频率**：同时覆盖多家厂商的聊天与编程产品，并以日期表格持续追踪变化，同类仓库中较少见。
- **跨形态采集**：包含本地部署、无头模式等非典型形态的提示词，扩展了观察视角。
- **宽松许可与社区驱动**：CC0-1.0 许可消除了使用顾虑，Pull Request 机制使内容可持续扩充。
- **获得外部权威引用**：被主流媒体与研究机构用于公开报道和数据看板，间接验证了内容的可用性与准确性。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [华盛顿邮报相关交互报道](https://archive.today/pYtPk)
- [CEPS AI World 数据看板报道](https://aiworld.eu/story/system-prompts-and-what-they-tell-us-about-the-chat-before-the-chat)
