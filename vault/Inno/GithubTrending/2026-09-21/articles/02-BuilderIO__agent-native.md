---
tags:
  - trending
  - article
repo: BuilderIO/agent-native
date: 2026-09-21
language: TypeScript
stars_total: 5447
stars_today: 98
---
## 项目概述

Agent-Native 是由 BuilderIO 团队开源的 TypeScript 框架，用于构建「智能体原生（agentic）」应用。它的核心出发点在于：当前多数 LLM 应用仍停留在对话框形态，而实际的智能体（agent）工作往往需要上下文展示、工具调用、文件操作、审批与分享等交互环节。Agent-Native 试图提供一个统一的编程模型，让开发者既能定义智能体的自主执行能力，又能同时获得一套为其量身打造的界面，从而弥补纯聊天界面的不足。

该项目面向需要在产品中集成智能体能力的应用开发者，尤其是希望以较低成本同时交付「agent 能力」与「可视化管理界面」的团队。项目使用 Apache 类开源许可（具体以仓库为准）发布，目前已在 GitHub 上获得约 5447 颗星标。

## 核心功能

- **Action（动作）统一抽象**：开发者只需将每一项能力定义一次为 action，agent 可将其作为工具调用，UI 则可在代码中直接调用同一 action，从而避免为「工具调用」与「界面按钮」维护两套逻辑。
- **内建脚手架与模板**：提供 `create` 命令行工具和 `chat` 等模板，可一键生成可运行的项目骨架。
- **智能体 UI 运行时**：框架提供与 agent 配套的界面层，用于展示 agent 可以做什么，并让用户检视、编辑、批准和分享其产出。
- **TypeScript 优先**：整个框架以 TypeScript 编写并提供类型支持，便于在既有 TS 项目中集成并获得良好的开发体验。
- **面向独立部署的 `--standalone` 模式**：生成的模板项目可独立运行，降低本地尝试与环境搭建的门槛。

## 技术架构

Agent-Native 的设计核心是「一次定义、两处调用」。传统做法中，开发者通常需要分别为 LLM 准备工具 schema，再为 UI 编写调用后端或本地函数的代码，二者容易脱节。Agent-Native 将这种能力抽象为 action：action 既是 agent 可调用的工具描述，也是 UI 可直接调用的函数入口。这样 agent 自主执行与用户手动触发共享同一份实现，行为和权限控制也更容易保持一致。

在语言与运行层面，框架基于 TypeScript，使用现代 JS/TS 工程链，并以 npm 包 `@agent-native/core` 的形式发布。项目通过 CLI（`npx @agent-native/core create`）生成模板工程，降低起步成本。README 中强调「agent 的环境应当提供上下文、工具、文件、测试与预览」，因此框架在架构上不仅提供 agent 执行层，也提供了对应的 UI 支撑，使 agent 的工作过程与结果对人类可见、可干预。这种「agent + 专用界面」的组合，是该框架区别于纯 SDK 类项目的主要架构特征。

## 安装与使用

前置要求为 Node.js 环境（建议使用较新的 LTS 版本）。可通过 npm 直接创建项目：

```bash
npx --yes @agent-native/core@latest create my-agent --standalone --template chat
```

该命令会基于 `chat` 模板生成名为 `my-agent` 的项目。生成后进入目录并按模板说明安装依赖、启动开发服务即可：

```bash
cd my-agent
npm install
npm run dev
```

随后可在生成的项目中找到 action 定义文件，按模板结构新增或修改 action；框架会自动将新 action 暴露给 agent 作为工具，同时供 UI 调用。更完整的入门流程可参考官方文档中的 Getting Started 指南。

## 适用场景

- **需要人工审批的智能体工作流**：agent 先执行搜索、生成或修改，再由用户在界面中检视、编辑、批准后落地。
- **内部效率工具**：把重复性的知识工作（如整理资料、批量修改文件、生成报告）封装为 action，由 agent 自动执行、由 UI 兜底干预。
- **带可视化的 AI 产品原型**：需要同时演示 agent 能力与交互界面时，可借助模板快速搭建。
- **为既有系统增加 agent 能力**：在已有 TypeScript 项目中引入统一 action 层，使工具定义与前端调用共享实现。

## 项目亮点

与仅提供 SDK 或仅提供对话式前端的方案相比，Agent-Native 的差异化在于把 action 作为 agent 与 UI 的共同契约，从而减少重复实现和行为漂移。同时，它把「界面」视为 agent 运行环境的一部分而非附属品，强调上下文、工具、文件与预览对人类监督的价值。再加上开箱即用的 CLI 模板和 TypeScript 类型支持，它对希望快速落地可交互 agent 应用的团队较为友好。

## 相关链接

- [GitHub 仓库](https://github.com/BuilderIO/agent-native)
- [官方文档](https://agent-native.com/docs/getting-started)
- [Actions 概念说明](https://agent-native.com/docs/actions-overview)
