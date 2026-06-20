---
tags:
  - trending
  - article
repo: withastro/flue
date: 2026-06-20
language: TypeScript
stars_total: 5896
stars_today: 309
---
## 项目概述

Flue 是一个面向 TypeScript 开发者的智能体编排框架（Agent Harness Framework），旨在解决当前 AI 智能体开发中“从 SDK 到生产级自主智能体”之间存在的巨大鸿沟。传统的 LLM SDK 适用于简单的聊天机器人和脚本化任务，但难以支撑能够真正自主完成复杂任务的智能体（如 Claude Code、Codex）。Flue 提供了一套可编程的“鞍具”（Harness），让开发者能够为智能体赋予上下文、工具、技能和安全的执行沙箱，从而构建出可信任的、端到端自主工作的 AI 智能体。目标用户是希望在生产环境中构建和部署高级 AI 智能体应用的 TypeScript 开发者。

## 核心功能

- **智能体编排引擎**：提供 `createAgent` 核心函数，允许开发者声明式地组装智能体所需的模型、工具、技能指令和沙箱环境，而非编写繁琐的胶水代码。
- **技能（Skill）装配**：支持以 Markdown 文件的形式定义智能体的技能（如 `SKILL.md`），通过 `import ... with { type: 'skill' }` 语法直接导入并注入到智能体上下文中，实现模块化的行为能力扩展。
- **工具集成系统**：允许轻松集成自定义工具，如代码示例中的 `githubTools`，使智能体能够执行真实的 API 调用和外部操作。
- **沙箱安全执行**：内置沙箱机制，支持虚拟、本地或远程容器化执行环境（如 `local()`），确保智能体在执行代码、访问文件等操作时的安全性和可控性。
- **HTTP 路由暴露**：通过 `AgentRouteHandler` 接口，可以将智能体安全地暴露为 HTTP 端点，方便与其他服务或前端集成。
- **跨模型支持**：支持接入多种 LLM 模型（如示例中的 `anthropic/claude-sonnet-4-6`），提供灵活的模型选择。

## 技术架构

Flue 采用模块化的运行时架构，核心包为 `@flue/runtime`。其设计思路强调“编程式框架”而非传统 SDK：开发者编写的不是简单的 API 调用序列，而是定义智能体行为的完整“计划”。架构的关键元素包括：`createAgent` 工厂函数，它接受一个返回配置对象的回调，配置中包含模型 ID、工具列表、技能引用、沙箱类型和指令字符串。技能使用标准的 Markdown 格式，通过 TypeScript 的导入语法与代码分离，实现了行为逻辑的独立维护。沙箱抽象层（`@flue/runtime/node` 中的 `local()`）将执行环境与智能体逻辑解耦，支持从本地进程到远程 Docker 容器的切换，从而适配开发、测试和生产等不同环境的隔离要求。路由系统（`AgentRouteHandler`）则提供了标准化的 Web 服务集成点。

## 安装与使用

**前置条件**：确保已安装 Node.js 18+ 和 TypeScript 5+。

**安装**：
```bash
npm install @flue/runtime @flue/runtime/node
```

**最小使用示例**：

1. 创建一个技能文件 `skills/triage/SKILL.md`：
```markdown
# Triage Skill
You are an expert bug triager. Analyze the given bug report and:
- Reproduce the issue
- Diagnose root cause
- Verify if behavior is intentional
- Propose or attempt a fix
```

2. 创建智能体文件 `agents/triage.ts`：
```typescript
import { createAgent, type AgentRouteHandler } from '@flue/runtime';
import { local } from '@flue/runtime/node';
import triage from '../skills/triage/SKILL.md' with { type: 'skill' };

const instructions = `Triage a bug report end-to-end...`;

export const route: AgentRouteHandler = async (_c, next) => next();

export default createAgent(() => ({
  model: 'anthropic/claude-sonnet-4-6',
  tools: [],
  skills: [triage],
  sandbox: local(),
  instructions,
}));
```

3. 启动服务（具体启动方式取决于项目脚手架，建议参考仓库文档）。

## 适用场景

- **自动化 Bug 处理工作流**：如示例所示，智能体可以端到端地处理 Bug 报告，从复现、诊断到尝试修复，无需人工干预每一步。
- **代码审查与质量保障**：集成代码仓库工具，让智能体自动审查 Pull Request、分析代码质量或识别安全漏洞。
- **复杂数据分析流水线**：让智能体自主调用数据库查询、运行分析脚本，并根据结果生成报告或执行下一步操作。
- **客服与技术支持增强**：将智能体暴露为 HTTP 服务，用于处理用户工单，包括查询解决方案、调用后台系统或引导用户操作。

## 项目亮点

区别于 LangChain、Vercel AI SDK 等框架，Flue 的核心差异化在于：

- **以“鞍具”为核心的设计理念**：它提供的是一个完整的执行环境（Sandbox + Skills + Tools），而不是一个 API 调用链。开发者配置的是智能体“如何自主工作”，而不是“调用哪些 API”，这使得构建真正的自主代理成为可能。
- **原生 TypeScript 一等公民**：技能、工具和配置全部使用 TypeScript 语法（包括导入 Markdown 作为模块），与现有 TypeScript 生态无缝集成，无需学习新语言或 DSL。
- **内置安全沙箱**：许多框架忽略智能体执行代码时的安全问题，Flue 将沙箱作为核心抽象，赋予了生产级部署所需的安全基线。
- **专注于自主性**：框架的设计哲学强调“交给智能体任务而非步骤”，鼓励开发者构建能够独立解决问题的代理，而非简单的工具链。

## 相关链接

- [GitHub 仓库](https://github.com/withastro/flue)
- [项目官网](https://flue.sh)（待补充，请以仓库信息为准）
