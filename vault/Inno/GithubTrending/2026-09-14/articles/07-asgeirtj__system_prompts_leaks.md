---
tags:
  - trending
  - article
repo: asgeirtj/system_prompts_leaks
date: 2026-09-14
language: JavaScript
stars_total: 66322
stars_today: 706
---
## 项目概述

System Prompts Leaks 是一个持续维护的公开资料库，用于收录各大 AI 聊天机器人与编程助手实际使用的系统提示词（system prompts）。系统提示词是模型在收到用户第一条消息之前就被注入的隐藏指令，决定了模型的角色设定、行为边界、工具调用规则、拒答策略以及输出格式。普通用户通常无法直接看到这些内容，而该仓库通过逆向、抓取或用户投稿等方式，将这些文本以接近原文的形式保存下来。

该项目解决的核心问题是信息不对称：研究者和开发者难以获知闭源模型的实际约束逻辑，而官方文档往往只披露抽象原则。仓库以纯文本 Markdown 文件的形式提供这些提示词，便于检索、对比与引用。目标用户包括 AI 研究者、提示词工程师、安全与合规从业者、产品经理，以及希望理解模型行为成因的普通开发者。

仓库采用 CC0-1.0 许可，意味着内容可自由使用，无需署名。项目已获得超过 6.6 万颗星标，并被《华盛顿邮报》等媒体引用作为报道的数据来源。

## 核心功能

- **多厂商提示词收录**：覆盖 Anthropic（Claude Fable 5.1、Opus 5、Claude Design、Claude Code）、OpenAI（ChatGPT GPT-6-Astra、Codex）、Google（Gemini 3.8 Flash、3.1 Pro、Antigravity）、xAI（Grok、Grok Bot）以及 Cursor、Kimi 等第三方产品。
- **逐字原文保存**：以接近原始注入文本的形式记录，保留格式、分段与特殊标记，减少二次加工带来的失真。
- **变更追踪表**：README 中维护“最近新增/变更”表格，标注具体产品、日期与对应文件链接，便于跟踪模型迭代带来的提示词调整。
- **按厂商与产品分类的目录结构**：文件按 OpenAI、Google 等目录组织，命名与产品线对应，方便定位特定版本。
- **社区投稿机制**：通过 Pull Request 接受新增或修正内容，README 中提供投稿入口徽章。
- **持续更新**：更新频率较高，紧跟各家模型的新版本发布。

## 技术架构

仓库本体以 JavaScript 作为标注语言，但主体内容是 Markdown 文档，结构轻量。其设计思路偏向“数据归档”而非“软件系统”：

- **扁平化存储**：每个系统提示词对应一个独立 Markdown 文件，避免数据库依赖，直接利用 Git 的版本控制能力记录历史变化。
- **目录即分类**：以厂商名作为顶层目录，产品名作为文件名前缀，形成可预测的路径规则。
- **以 Git 为审计层**：每次提交对应一次提示词变更，通过 commit 历史和 blame 可以追溯某条规则的引入时间。
- **资源与文档分离**：`assets/` 存放品牌图片等静态资源，与提示词正文解耦。
- **零构建流程**：无需编译或运行环境，克隆后即可直接阅读，降低了使用门槛。

这种架构的取舍在于牺牲了结构化查询能力（如按规则类型检索），换取了可读性和低维护成本。

## 安装与使用

项目本身无需安装，使用方式以克隆和阅读为主：

```bash
git clone https://github.com/asgeirtj/system_prompts_leaks.git
cd system_prompts_leaks
```

随后可直接浏览目录，例如查看某个产品的提示词：

```bash
cat OpenAI/Codex/gpt-6-astra-chatgpt-work-local.md
```

若需检索特定关键词（如工具调用或拒答规则），可结合 grep：

```bash
grep -ri "refuse" Google/
```

如需获取最新内容，执行 `git pull` 即可。由于是纯文本仓库，也可直接通过 GitHub 网页界面在线查看，无需本地环境。

## 适用场景

- **提示词工程参考**：对比不同厂商如何组织角色设定、格式约束与工具描述，作为设计自有系统提示词的参考样本。
- **模型行为分析**：研究特定拒答、安全策略或语气设定的措辞，解释模型在边界情况下的表现。
- **安全与合规审查**：评估模型被注入的约束是否符合组织的合规要求，识别潜在风险点。
- **教学与媒体报道**：作为课程素材或新闻调查的一手数据来源，仓库已被媒体用于构建交互式报道与数据仪表盘。

## 项目亮点

与同类零散收集的提示词仓库相比，该项目的主要差异在于：

- **覆盖广度**：同时收录 Anthropic、OpenAI、Google、xAI 及多个第三方产品，便于横向对比。
- **更新及时性**：在新模型或新版本发布后较快跟进，README 中的变更表提供明确的时间线。
- **原文保真**：强调逐字捕获，而非概括或改写，对需要精确引用措辞的研究尤为重要。
- **许可宽松**：CC0-1.0 允许在商业与二次创作场景中自由使用，降低了引用门槛。
- **外部验证**：被主流媒体与欧洲智库项目引用，具备一定的公开可信度参考。

## 相关链接

- [GitHub 仓库](https://github.com/asgeirtj/system_prompts_leaks)
- [Latitude：开源 Agent 分析平台](https://go.asgeirtj.workers.dev/latitude)
- [《华盛顿邮报》基于本仓库的交互报道](https://archive.today/pYtPk)
- [CEPS AI World 数据仪表盘](https://aiworld.eu/story/system-prompts-and-what-they-tell-us-about-the-chat-before-the-chat)
