---
tags:
  - trending
  - article
repo: ruvnet/ruflo
date: 2026-09-07
language: TypeScript
stars_total: 71111
stars_today: 276
---
## 项目概述

Ruflo 是一个面向 Claude Code 和 Codex 的智能体元框架（Agent Meta-Harness），旨在为 AI 编程助手提供完整的执行层能力。项目的核心理念是 "Agent = Model + Harness"——模型负责生成内容，而框架负责赋予模型工具、记忆、循环控制、沙箱环境和安全防护，使其能够真正独立完成复杂工作。

Ruflo 解决了当前 AI 编程工具面临的核心痛点：单一 Agent 会话缺乏长期记忆、无法自主协调多步骤任务、难以在多机器间安全协作。通过 `npx ruflo init` 一条命令，开发者即可为 Claude Code 和 Codex 注入"神经系统"，让 Agent 具备自我组织、群体协作和跨会话学习的能力。

项目主要面向使用 AI 辅助开发的软件工程师、DevOps 团队以及构建复杂对话式 AI 系统的开发者，特别适合需要多 Agent 协作处理工作流的场景。

## 核心功能

- **100+ 专业 Agent 库**：内置涵盖代码审查、测试生成、重构、文档编写等场景的专用 Agent，按需调用。
- **自适应记忆系统**：Agent 能够从每次交互中学习，跨会话保留关键上下文，无需人工重复说明项目背景。
- **多 Agent 群体编排**：支持将多个 Agent 组织为"群体"（Swarm），自动分配任务角色并协调执行顺序。
- **自我学习与优化**：系统会记录任务执行效果，持续调整 Agent 行为策略以提升后续任务的完成质量。
- **RAG 集成**：内置检索增强生成能力，Agent 可无缝接入外部知识库，提升回答的准确性和时效性。
- **跨机器联邦通信**：通过安全通道实现不同机器上的 Agent 之间通信，支持分布式协作而不泄露敏感数据。
- **原生适配主流 CLI**：深度集成 Claude Code、Codex 和 Hermes，同时提供 MCP（Model Context Protocol）接口。

## 技术架构

Ruflo 采用分层架构设计，其核心执行流程如下：

```
用户 → Ruflo（CLI/MCP）→ 路由器 → 群体管理器 → 专业 Agent → 记忆系统 → LLM 提供商
```

其中，**路由器**负责任务分发，根据输入内容判断应由哪个 Agent 或群体处理；**群体管理器**负责协调多个 Agent 的执行顺序和数据传递；**记忆系统**采用向量数据库持久化存储交互历史，支持语义检索；底层通过统一的 LLM Provider 层对接不同模型提供商。

技术栈方面，Ruflo 使用 TypeScript 开发，充分利用其类型系统确保 Agent 间接口的类型安全。项目的关键设计特点包括：

- **模块化解耦**：CLI、Agent 库、记忆系统、通信层均为独立模块，可按需启用。
- **安全沙箱**：联邦通信采用经过认证的加密通道，确保跨机器数据传输安全。
- **元框架定位**：并非替代 Claude Code 或 Codex，而是作为其上的编排层，最大化兼容已有工具链。
- **可扩展插件机制**：社区可以贡献自定义 Agent 和工具，丰富生态。

## 安装与使用

### 安装要求

- Node.js 16+
- Claude Code 或 Codex CLI（任选其一）
- 对应的 LLM API 密钥

### 快速开始

```bash
# 1. 在项目目录中初始化 Ruflo
npx ruflo init

# 2. 检查当前配置并列出可用 Agent
npx ruflo agents list

# 3. 启动交互式群体会话
npx ruflo swarm --task "审查当前代码库中的潜在安全问题"

# 4. 在 MCP 客户端中加载 Ruflo（可选）
# 在 Claude Desktop 或类似 MCP 客户端中添加 Ruflo 作为 MCP 服务器
```

最小可用示例——创建一个带记忆能力的简单 Agent：

```typescript
import { Ruflo } from 'ruflo';

const app = await Ruflo.create({
  agents: ['./agents/custom-reviewer'],
  providers: { claude: { model: 'claude-sonnet-4-20250514' } }
});

const result = await app.run({
  task: '请对 src/utils.ts 中的 error handling 逻辑进行代码审查并给出改进建议',
  mode: 'single', // 或 'swarm' 进行多 Agent 协作
  remember: true // 将本次任务记录到长期记忆
});
```

## 适用场景

1. **大型代码库自动化审查与优化**：团队可利用多个 Agent 分别执行代码规范检查、性能瓶颈定位和重构建议生成，显著提升代码质量评审效率。

2. **多项目知识共享与协作**：不同机器上的开发者通过联邦通信共享 Agent 学习到的项目特定知识，减少低效沟通成本。

3. **复杂工作流自动化编排**：例如从需求理解、任务拆解到测试生成与验证的整套敏捷开发流程，可通过群体模式自动推进。

4. **对话式 AI 系统构建与运维**：利用 Ruflo 的记忆与 RAG 能力，构建具备上下文感知的客服或内部支持机器人。

## 项目亮点

Ruflo 与同类 Agent 编排工具相比具有以下差异化优势：

- **原生集成体验**：直接构建于 Claude Code 和 Codex 之上，无需放弃现有工作流即可增强 Agent 能力。
- **开箱即用 Agent 生态**：100+ 预置 Agent 覆盖主流开发场景，避免从零搭建的重复劳动。
- **真正的自学习能力**：具备跨会话记忆持久化，能够积累项目级知识——这是多数替代方案所缺失的关键能力。
- **安全优先的联邦通信**：分布式场景下基于企业级安全隔离设计，可信执行环境保障数据不泄露。
- **单命令初始化**：`npx ruflo init` 即可获得完整能力，大幅降低入门门槛。
- **无锁定供应商**：支持 Claude、Codex 等多模型后端，并提供开放 MCP 接口对接任意兼容工具。

## 相关链接

- [GitHub 仓库](https://github.com/ruvnet/ruflo)
- [官方文档站点](https://flo.ruv.io/)
- [npm 包页面](https://www.npmjs.com/package/ruflo)
- [底层联邦通信参考实现](https://github.com/ruvnet/ruvector)
- [Ruflo Goal 规划页面](https://goal.ruv.io/)
