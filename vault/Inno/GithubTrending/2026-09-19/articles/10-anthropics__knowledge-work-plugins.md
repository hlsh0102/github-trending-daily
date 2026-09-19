---
tags:
  - trending
  - article
repo: anthropics/knowledge-work-plugins
date: 2026-09-19
language: Python
stars_total: 24944
stars_today: 299
---
## 项目概述

Knowledge Work Plugins 是由 Anthropic 开源的一组插件集合，主要面向知识工作者（knowledge workers），用于在 Claude Cowork 中扩展 Claude 的能力。Claude Cowork 是 Anthropic 推出的协作式 AI 产品，用户只需设定目标，Claude 即可交付完整、专业的工作成果。而插件机制在此基础上更进一步：它允许用户告诉 Claude“工作应该怎么做”——使用哪些工具和数据源、如何处理关键工作流、暴露哪些斜杠命令，从而让团队获得更一致、更符合自身习惯的输出结果。

该项目解决的核心问题是：通用大模型在具体岗位、具体团队中往往缺乏必要的业务上下文和流程规范。通过将技能（skills）、连接器（connectors）、斜杠命令（slash commands）和子代理（sub-agents）按职能打包，插件把一个“什么都懂一点”的 Claude，变成某一岗位的专属助手。目标用户包括产品、销售、市场、运营、财务等各类知识工作者，以及希望统一团队 AI 使用方式的企业管理员。

## 核心功能

- **按职能打包的插件**：每个插件面向一个特定岗位（如 productivity、sales 等），内置该岗位常用的工作流与提示词，开箱即可使用。
- **连接器集成**：内置对 Slack、Notion、Asana、Linear、Jira、Monday、ClickUp、Microsoft 365、HubSpot、Close、Clay、ZoomInfo、Fireflies 等主流工具的连接能力，使 Claude 能直接读写业务数据。
- **斜杠命令**：为常见操作提供快捷指令入口，减少重复输入，提高交互效率。
- **子代理（sub-agents）**：把复杂任务拆解为可复用的子代理协作流程，提升多步骤工作的可控性。
- **可定制性**：团队成员可按公司自身的工具链、术语和流程对插件进行调整，让 Claude 更像“为团队量身定做”。
- **插件市场**：目前开源了 11 个由 Anthropic 自身实践衍生的插件，便于用户直接选用或作为二次开发的模板。

## 技术架构

项目以 Python 为主要开发语言，采用插件化架构。每个插件是一个自包含的目录，内部以声明式的方式组织技能、连接器、斜杠命令和子代理等资源，从而把“能力”与“运行时”解耦。这种设计的思路是：运行时（Claude Cowork 或 Claude Code）负责解析插件描述并调度执行，而插件本身专注于描述业务逻辑和集成点，不需要关心底层推理过程。

连接器层负责与外部 SaaS 工具交互，屏蔽了各家 API 的差异；技能与斜杠命令层负责把岗位知识固化为可复用的提示与流程；子代理层负责编排多步骤任务。整体上遵循“约定优于配置”的原则，降低了非工程背景的知识工作者定制插件的门槛。项目以 Apache-2.0 许可证开源，允许企业内部修改和再分发。

## 安装与使用

由于插件需在 Claude Cowork 或 Claude Code 环境中使用，基本流程通常如下：

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/anthropics/knowledge-work-plugins.git
   ```
2. 根据目标岗位进入对应插件目录，例如 `cd productivity`。
3. 阅读该目录下的说明文档（通常是 README），按其指引配置所需的连接器凭据（如 Slack、Notion 的 API Token）。
4. 在 Claude Cowork 或 Claude Code 中加载该插件，然后通过斜杠命令或自然语言调用其能力。

最小可用示例：在 Claude Cowork 中载入 productivity 插件并连接 Slack 后，可以直接输入“总结今天 Slack 中与我相关的待办事项”，Claude 会调用插件中预置的工作流完成任务。如需企业级定制，可在插件目录内修改提示词、术语和连接配置后重新加载。

## 适用场景

- **个人效率管理**：统一管理任务、日历和日常流程，减少重复性的上下文输入。
- **销售流程支持**：调研潜在客户、准备通话、审阅销售管道、撰写外联邮件、构建竞品对阵卡。
- **团队协作规范化**：把团队惯用的工具链和术语固化进插件，让所有成员获得一致的 AI 输出。
- **企业二次开发**：以开源插件为基础，结合内部系统打造符合自身流程的专属助手。

## 项目亮点

与一般的提示词集合或单体 AI 助手相比，该项目有几个相对明确的差异点。其一，插件是按“岗位”而非按“功能”组织的，更贴近知识工作者的实际工作方式。其二，它同时提供技能、连接器、斜杠命令和子代理四类构件，覆盖了从数据接入到任务编排的完整链路。其三，全部插件由 Anthropic 基于自身工作实践构建并开源，具备真实使用场景的验证背景。其四，Apache-2.0 许可证和企业级定制能力，使其既可直接使用，也可作为组织内部 AI 工作流的起点。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/knowledge-work-plugins)
- [Claude Cowork 产品页](https://claude.com/product/cowork)
- [Claude Code 产品页](https://claude.com/product/claude-code)
