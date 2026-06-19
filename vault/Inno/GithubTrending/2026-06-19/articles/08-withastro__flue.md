---
tags:
  - trending
  - article
repo: withastro/flue
date: 2026-06-19
language: TypeScript
stars_total: 5575
stars_today: 162
---
## 项目概述

Flue 是一个面向 AI Agent 的 **沙箱框架**（Agent Harness Framework），它不再只是另一个 SDK，而是为构建自主 Agent 和强大 AI 工作流而设计的可编程 TypeScript 框架。

传统 AI Agent 构建方式存在明显局限：早期基于裸 LLM API 调用开发的 Agent 只能处理简单的聊天机器人和脚本化任务，无法应对复杂的自主决策场景。而像 Claude Code 和 Codex 这样的新一代 Agent 证明了真正的 Agent 应当是自主的——你只需交给它一个任务，而不是预设好一系列步骤，然后信任它能独立完成。

Flue 解决了这个核心问题：它提供了一套完整的基础设施，让开发者能够构建具备自主决策能力、可在沙箱环境中安全执行真实工作的 Agent。目标用户是希望开发生产级 AI Agent 的 TypeScript 开发者、AI 工程师以及需要构建复杂 AI 工作流的团队。

## 核心功能

- **沙箱化执行环境**：支持虚拟、本地或远程容器沙箱，让 Agent 在隔离环境中安全执行代码和操作，避免对宿主系统造成影响。
- **可组合的 Agent 编排**：通过 `createAgent` 工厂函数，开发者可以轻松组合模型、工具、技能和指令，构建具备完整能力的 Agent 单元。
- **HTTP 路由集成**：内置 `AgentRouteHandler` 支持，可将 Agent 通过 HTTP 暴露为 API，方便集成到现有 Web 服务中。
- **技能（Skills）与工具（Tools）分离管理**：支持通过 `.md` 文件定义技能（如 `SKILL.md`），并为 Agent 绑定外部工具（如 GitHub API 工具），实现知识扩展和能力增强。
- **多模型支持**：通过简单配置即可指定使用不同 LLM 模型（如 `anthropic/claude-sonnet-4-6`），灵活适配不同任务需求。
- **自主任务执行**：Agent 可以接收高层级指令（如“对 bug 进行端到端分类”），自主规划步骤、调用工具、验证结果，无需人类干预。

## 技术架构

Flue 采用 **TypeScript** 作为主要开发语言，充分利用了 TypeScript 的类型系统和模块化能力。其核心设计理念是“框架而非 SDK”——不会强制开发者遵循特定的编程范式，而是提供一个灵活的容器（Harness）来承载 Agent 的各种能力。

架构上，Flue 将 Agent 的各个组成部分解耦为独立模块：
- **Runtime**（`@flue/runtime`）：负责 Agent 的生命周期管理，包括模型调用、上下文维护和执行流控制。
- **Sandbox**（沙箱层）：提供隔离的执行环境，支持 `local()`（本地沙箱）以及未来的远程容器沙箱，确保 Agent 操作的安全性。
- **Skills**（技能模块）：以 Markdown 文件形式定义的领域知识，Agent 可以动态加载和理解这些技能描述。
- **Tools**（工具集）：可调用的外部 API 或函数，Agent 根据任务需要自主选择和调用。

这种架构设计使得 Agent 的构建变得高度模块化和可定制。开发者可以像搭积木一样，为不同的 Agent 组合不同的模型、工具和技能，而底层的沙箱和执行机制由框架统一管理。

## 安装与使用

Flue 基于 Node.js 环境，需要通过 npm 或 pnpm 安装核心运行时包：

```bash
npm install @flue/runtime
```

**最小可用示例**：

创建一个简单的 Agent，配置模型、工具和沙箱环境：

```ts
// agents/simple-agent.ts
import { createAgent } from '@flue/runtime';
import { local } from '@flue/runtime/node';

// 定义 Agent 使用的工具
const searchTool = {
  name: 'web_search',
  description: '搜索互联网信息',
  execute: async (query: string) => {
    // 实现搜索逻辑
    return `搜索结果: ${query}`;
  },
};

// 创建 Agent 实例
const agent = createAgent(() => ({
  model: 'openai/gpt-4',
  tools: [searchTool],
  sandbox: local(),
  instructions: '你是一个有帮助的助手，可以回答用户问题并执行搜索。',
}));

// 运行 Agent
const result = await agent.run('请搜索最新的 TypeScript 版本信息');
console.log(result);
```

如果需要将 Agent 暴露为 HTTP 服务，可以使用内置的路由处理器：

```ts
import { createAgent, type AgentRouteHandler } from '@flue/runtime';

export const route: AgentRouteHandler = async (_c, next) => next();

export default createAgent(() => ({
  model: 'anthropic/claude-sonnet-4-6',
  sandbox: local(),
  instructions: '处理传入的 API 请求并返回响应。',
}));
```

## 适用场景

- **自动化 Bug 分类与修复**：Agent 可以接收 bug 报告，自动复现问题、诊断根因、验证行为是否属于预期，并尝试提交修复——整个流程完全自主完成。
- **代码审查与质量检测**：集成 GitHub 工具后，Agent 可以自动检查 PR 代码，检测潜在问题、不符合规范的写法，并生成审查意见。
- **数据处理与清洗流水线**：Agent 根据高层指令自主规划和执行数据处理任务，调用外部工具完成数据抓取、清洗、转换和存储。
- **智能客服与工单处理**：基于技能和工具的组合，Agent 可以理解用户问题、查询知识库、调用后端 API 处理工单，并在需要时升级给人工。

## 项目亮点

- **真正的自主性**：与其他 Agent 框架不同，Flue 不是让你编写预定义的工作流步骤，而是授权 Agent 根据任务自主决策、规划和执行，接近 Claude Code 和 Codex 的自主水平。
- **沙箱安全机制**：内置沙箱层让 Agent 操作天然具备隔离性，开发者无需额外担心安全风险，适合生产环境部署。
- **模块化的“装备”体系**：通过工具（Tools）、技能（Skills）、指令（Instructions）的组合，开发者可以像给 Agent“装备”能力一样灵活配置，而非被框架束缚。
- **原生 HTTP 集成**：Agent 可作为 Web 服务的一部分部署，开箱即用地支持路由和请求处理，简化了从开发到上线的流程。
- **TypeScript 原生支持**：充分利用 TypeScript 的类型系统和模块化现代 JavaScript 特性，提供良好的开发体验和类型安全保障。

## 相关链接

- [GitHub 仓库](https://github.com/withastro/flue)
- 官方文档与更详细的示例，请参考仓库 `README` 及相关文档目录。
