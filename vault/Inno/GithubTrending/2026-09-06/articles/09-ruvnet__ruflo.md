---
tags:
  - trending
  - article
repo: ruvnet/ruflo
date: 2026-09-06
language: TypeScript
stars_total: 70761
stars_today: 136
---
## 项目概述

Ruflo 是一个面向 Claude Code 和 Codex 的智能体元框架（Agent Meta-Harness），旨在为 AI 编程助手提供完整的执行层能力。其核心设计理念是 **Agent = Model + Harness**——模型负责生成内容，而框架赋予模型工具调用、记忆管理、循环控制、沙箱环境和安全约束，使其能够真正完成复杂工作。

Ruflo 解决了当前 AI 智能体孤立运行、难以协作、缺乏持久记忆等核心痛点。通过一次性初始化，它即可为 Claude Code 和 Codex 赋予完整的“神经系统”：智能体可自主组织为多智能体群组、从每次任务中学习、跨会话保持记忆，并借助联邦通信机制实现跨机器的安全协作。该项目面向需要构建复杂 AI 工作流的开发者、AI 工程师团队以及希望将 Claude Code / Codex 集成到生产环境的企业开发者。

## 核心功能

- **100+ 专业智能体**：内置涵盖代码审查、架构设计、测试生成、文档编写等场景的专业智能体，可直接调用并支持自定义扩展。
- **协调式智能体群组**：智能体可动态组成“群组”（Swarm），按任务复杂度和目标自动分配角色，实现并行处理与协作。
- **自适应记忆系统**：支持跨会话的持久化记忆，智能体可从历史任务中学习偏好、编码风格和项目结构，持续优化后续行为。
- **RAG 集成**：内置检索增强生成能力，支持将项目文档、代码库或外部知识源接入智能体上下文，提升回答准确性和领域相关性。
- **联邦通信（Federation）**：通过加密通道实现不同机器上的智能体安全对话，无需共享原始数据即可协同完成分布式任务。
- **多模型/多工具兼容**：原生支持 Claude Code、Codex、Hermes 等多种模型后端，并提供 MCP（Model Context Protocol）接口，可灵活接入更多服务。

## 技术架构

Ruflo 采用模块化分层架构，核心数据流为：

```
User → Ruflo (CLI/MCP) → Router → Swarm → Agents → Memory → LLM Providers
```

- **接入层**：提供 CLI 和 MCP 双入口，开发者可通过命令行直接操作，也可将其嵌入 Cursor、VS Code 等支持 MCP 的 IDE 中。
- **路由与编排层**：Router 组件分析用户请求并分派至合适的智能体或群组；Swarm 管理器负责动态创建和销毁任务群组，平衡负载与上下文窗口。
- **智能体层**：每个 Agent 封装了特定角色、工具集和提示模板，可以独立运行或通过消息总线与其他 Agent 交互。
- **记忆与知识层**：Memory 模块采用分层结构，区分短期工作记忆与长期项目记忆，并自动执行记忆压缩和索引；RAG 引擎通过向量检索为智能体提供外部知识。
- **联邦层**：基于端到端加密通信协议，支持跨实例的智能体身份认证和消息路由，并确保敏感数据不出本地。
- **安全框架**：内置企业级防护栏，包括权限隔离、操作审计和可配置的 LLM 输出过滤规则。

项目使用 TypeScript 全程开发，保证了类型安全和模块可维护性。其架构设计强调“配置即声明”——通过简单的 YAML 或 TOML 配置即可构造复杂的工作流，而无需编写大量胶水代码。

## 安装与使用

Ruflo 可通过 npm 全局安装，并支持 Claude Code 和 Codex 两种主流编程智能体：

```bash
# 全局安装
npm install -g ruflo

# 或使用 npx 直接初始化（推荐）
npx ruflo init
```

执行 `npx ruflo init` 后，工具会自动检测环境中已有的 Claude Code 或 Codex 配置，并生成 `ruflo.config.ts` 配置文件及基础智能体模板。最小可用示例如下：

```typescript
// ruflo.config.ts
import { defineConfig } from 'ruflo'

export default defineConfig({
  model: {
    provider: 'anthropic',   // 或 'openai' / 'codex'
    model: 'claude-sonnet-4-20250514'
  },
  agents: {
    // 启用内置代码审查智能体，并自定义角色提示
    'code-reviewer': {
      role: '资深代码审查专家',
      tools: ['read', 'search', 'run-tests'],
      contextFiles: ['src/**/*.ts']
    }
  }
})
```

配置完成后，启动交互式 Ruflo 会话：

```bash
ruflo start
# 或直接以对话方式执行任务
ruflo run "重构 src/core 模块并编写单元测试"
```

若要创建并部署一个由多个智能体组成的群组以完成复杂任务，可在配置文件中声明群组关系，此后所有操作将由 Ruflo 自动编排。

## 适用场景

- **大型代码库维护与重构**：需要同时分析源码结构、编写重构方案、执行测试验证等多个任务时，可通过 Ruflo 组建多智能体并行作业。
- **跨团队知识管理**：利用自适应记忆和 RAG 集成能力，为开发团队构建可持续学习并沉淀经验的 AI 助手系统。
- **AI 产品原型研发**：快速搭建具备多轮对话、联网检索和工具调用能力的原型系统，测试智能体工作流的商业可行性。
- **分布式开发协作**：在本地和远程多台开发机上分别运行 Ruflo，通过联邦通信模块让智能体跨环境协同处理任务，保护核心数据不离开本地基础设施。

## 项目亮点

- **专注执行层的通用框架**：与多数聚焦模型调用的 Agent 框架不同，Ruflo 明确将重心落在执行层，为 Claude Code 和 Codex 这两大主流编码智能体提供了统一增强层。
- **开箱即用的协作和记忆能力**：其他框架往往需要自行搭建记忆和编排模块，而 Ruflo 通过一次初始化即可获得完整的自学习群组协作机制，大幅降低上手成本。
- **严格的安全与隐私设计**：联邦通信模块采用数据最小化原则，支持本地优先架构，允许企业在中控环境（如 VPC）中运行而无须将代码发送至公网模型。
- **活跃的开源生态**：项目在 GitHub 上拥有超过 7 万 Star，且日增活跃量可观，背后拥有强大的社区助力与持续迭代动力。

## 相关链接

- [GitHub 仓库](https://github.com/ruvnet/ruflo)
- [项目官网](https://flo.ruv.io/)
- [npm 包页面](https://www.npmjs.com/package/ruflo)
- [Agentic Engineering 文档](https://cognitum.one/agentic-engineering)
