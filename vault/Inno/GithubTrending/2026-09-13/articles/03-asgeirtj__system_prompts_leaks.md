---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-09-13
language: JavaScript
stars_total: 65604
stars_today: 217
---
## 项目概述

system_prompts_leaks 是一个持续维护的系统提示词（system prompt）归档仓库，主要收集各大 AI 聊天与编程助手在用户发送第一条消息之前所接收到的隐藏指令与规则。仓库以“逐字捕获”（captured verbatim）为原则，尽可能保留原文，供研究者、开发者与普通用户了解这些模型的行为边界从何而来。

项目覆盖范围并不局限于单一厂商，而是横跨 Anthropic、OpenAI、Google、xAI 等主流提供方，同时也包含 Cursor、Kimi、Grok Bot 等集成或衍生工具。对希望了解“模型为何这样回答”的人来说，该仓库提供的是一手材料，而非二手解读。其目标用户包括 AI 产品开发者、提示词工程实践者、学术研究者、媒体从业者，以及关注 AI 透明度与合规议题的观察者。

## 核心功能

- **多厂商系统提示词归档**：涵盖 Anthropic 的 Claude Fable 5.1、Opus 5、Claude Design、Claude Code，OpenAI 的 ChatGPT GPT-6-Astra、Codex，Google 的 Gemini 3.8 Flash、3.1 Pro、Antigravity，以及 xAI 的 Grok 系列、Cursor、Kimi 等。
- **逐字原文保存**：以纯文本或 Markdown 形式保留捕获到的提示词内容，减少在转录过程中引入的改写与失真。
- **变更记录追踪**：README 中以表格形式列出最近新增与变更的条目，标注日期与对应文件链接，便于回溯版本演进。
- **产品维度分类**：按厂商与产品线组织目录结构，例如 `Anthropic/claude-code/`、`OpenAI/Codex/`，方便定位特定模型的提示词文件。
- **持续更新**：仓库声明定期更新，以跟进各厂商随模型迭代而调整的系统提示词。

## 技术架构

该仓库以 JavaScript 作为主要语言，但核心内容形态是结构化的文本文件，而非可执行代码。整体设计偏向“资料库”而非“应用”：通过 GitHub 的目录与文件系统组织内容，借助 README 中的索引表提供导航入口。

这种设计带来两个特点。第一，内容以纯文本为主，便于直接阅读、diff 对比与机器解析；第二，使用 GitHub 原生的版本控制能力，天然支持变更历史的追溯，也便于社区通过 Pull Request 提交新增或修正内容——README 中即带有 "make a pull request" 徽章，说明其协作模式依赖开放贡献。

由于厂商的系统提示词本身不在官方文档中公开，仓库的准确性依赖于捕获过程的可信度。因此其技术价值更多体现在“记录”与“可验证”上：每一条目通常附有对应的模型或产品标识与日期，使外部读者可以判断其时效性。

## 安装与使用

该仓库无需安装依赖，最直接的用法是克隆或下载后直接阅读文件。

```bash
git clone https://github.com/asgeirtj/system_prompts_leaks.git
cd system_prompts_leaks
```

随后可按厂商目录浏览，例如查看 Claude Code 相关提示词：

```bash
ls Anthropic/claude-code/
cat Anthropic/claude-code/claude-code-headless-fable-5.1.md
```

若希望将提示词用于自己的分析流程，可直接读取 Markdown 文件：

```javascript
import { readFileSync } from "node:fs";

const prompt = readFileSync(
  "OpenAI/Codex/gpt-6-astra.md",
  "utf8"
);

console.log(prompt.slice(0, 500));
```

也可通过 GitHub 网页端的文件浏览器在线查看，无需本地环境。由于内容随上游模型更新而变化，建议在使用前先确认对应文件的日期标注。

## 适用场景

- **提示词工程参考**：对比不同厂商在角色设定、工具调用约束、安全边界描述上的写法差异，为自研 agent 的提示词设计提供参照。
- **AI 透明度研究**：用于分析模型被赋予的隐藏规则如何影响输出行为，支持媒体调查、政策讨论与学术研究。
- **应用开发与调试**：在集成某模型 API 时，了解其默认系统提示词有助于判断哪些行为来自平台层、哪些来自自身调用参数。
- **内容创作与教学**：作为案例材料，用于讲解大模型对齐、指令层级与系统提示词的实际形态。

## 项目亮点

与零散的单篇提示词分享相比，该仓库的差异点在于覆盖广度与维护持续性。它同时收录多家厂商的多个产品线，并保持更新，使跨厂商横向比较成为可能。其次，"verbatim" 的定位强调了记录的原始性，降低了二次加工带来的误差。

此外，该项目已产生实际的外部影响：据 README 记载，华盛顿邮报基于该仓库的提示词制作了互动报道，CEPS 的 AI World 也据此构建了实时数据看板。这说明其内容被媒体与研究机构视为可引用的素材来源。仓库采用 CC0-1.0 许可，允许在几乎无限制的条件下复用内容，进一步降低了使用门槛。较高的关注度（数万 star）也反映出 AI 透明性话题在开发者群体中的持续需求。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [Washington Post 互动报道（存档）](https://archive.today/pYtPk)
- [CEPS AI World 数据看板](https://aiworld.eu/story/system-prompts-and-what-they-tell-us-about-the-chat-before-the-chat)
