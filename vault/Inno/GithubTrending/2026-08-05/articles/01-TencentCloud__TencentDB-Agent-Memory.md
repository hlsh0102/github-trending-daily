---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-08-05
language: TypeScript
stars_total: 14044
stars_today: 1111
---
## 项目概述

TencentDB Agent Memory 是一个面向 AI Agent 的团队级内存中枢（Memory Hub），由腾讯云数据库团队开源。该项目致力于解决 AI Agent 在长期运行中面临的“记忆碎片化”问题——当多个 Agent 协作完成复杂任务时，每个 Agent 各自为战、上下文孤立，导致知识无法沉淀、经验无法复用。

该项目将对话、文档、代码等海量信息转化为四类可复用的记忆资产：Chat Memory（对话记忆）、Skill（技能）、LLM-Wiki（知识库）和 Code-Graph（代码图谱），并在此基础上提供统一的管理、共享与调用机制。通过这套体系，不同 Agent 之间可以实现“记忆互联”，让整个 Agent 团队像一个有组织的人类团队一样，不断积累经验、协同进化。

项目目标用户包括：AI 应用开发者、使用多 Agent 架构的团队、面向 Agent 场景的 DevOps 工程师，以及希望构建“一人公司”式自动化工作流的个人开发者。目前项目在 GitHub 上已获得超过 14,000 颗星，社区活跃度极高。

## 核心功能

- **四类记忆资产统一管理**：将对话记录、技能脚本、领域知识文档和代码结构统一建模为可检索、可版本化的记忆对象，避免信息孤岛。
- **跨 Agent 记忆共享**：通过 Memory Hub 实现多个 Agent 之间的记忆读写，支持按团队、项目或角色进行细粒度权限控制。
- **多框架无缝集成**：原生兼容目前主流的 Agent 框架，包括 OpenClaw、Hermes 等，提供标准化的接入接口，降低迁移成本。
- **一键部署全家桶**：项目提供 `memory-core`（核心存储）、`memory-hub`（共享中枢）和 `proxy`（代理服务）三个组件，可通过一条命令同时启动，开箱即用。
- **代码图谱生成**：自动分析代码仓库结构，生成函数调用关系、模块依赖等代码图谱，让 Agent 快速理解大型代码库。
- **基准测试支持**：内置 Benchmark 评测工具，帮助开发者量化验证记忆系统对 Agent 任务完成率的提升效果。

## 技术架构

TencentDB Agent Memory 采用三组件分层架构设计，各司其职且协同工作：

- **Memory Core（记忆核心）**：负责四类记忆资产的底层存储与索引，采用向量数据库与关系型数据库混合存储方案，兼顾语义检索与结构化查询的性能需求。
- **Memory Hub（记忆中枢）**：提供统一的 API 网关和记忆调度逻辑，支持记忆的写入、读取、更新、删除以及跨 Agent 的共享分发，是系统中的“记忆交换总线”。
- **Proxy（代理层）**：负责与各类 Agent 框架对接，将不同框架的上下文格式转换为标准的记忆接口调用，这一层使得系统具备极强的框架兼容性。

技术上基于 TypeScript 构建，充分利用其类型系统保证接口的可靠性。部署层面采用 Docker 容器化方案，所有服务可在本地或云端快速拉起。设计思路上，项目借鉴了人类团队协作的模式——每个 Agent 不再是孤立的个体，而是通过共享记忆形成“团队记忆”，从而提升整体协作效率。

## 安装与使用

安装过程极为简洁，只需以下几步：

```bash
# 1. 克隆仓库
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-imag

# 2. 启动全部三个服务（memory-core + memory-hub + proxy）
docker-compose up -d

# 3. 检查服务状态
docker-compose ps
```

启动成功后，系统默认会在本地暴露三个服务的访问端口。最小可用示例如下：

```typescript
// 通过 Memory Hub API 写入一条对话记忆
const response = await fetch('http://localhost:8080/api/v1/memories', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    type: 'chat',
    content: '用户偏好使用 Python 编写数据处理脚本',
    agent: 'data-assistant'
  })
});

// 在另一个 Agent 中读取共享记忆
const memories = await fetch('http://localhost:8080/api/v1/memories?type=chat&query=Python')
  .then(res => res.json());
```

## 适用场景

- **多 Agent 协作开发**：在大型软件项目中，多个 Agent 分别负责前端、后端、测试等任务，通过共享 Code-Graph 和 Chat Memory，快速对齐项目上下文，避免重复探索。
- **企业知识库问答**：将内部文档导入 LLM-Wiki，构建面向员工的智能问答助手，Agent 可实时查阅最新知识并回答跨部门问题。
- **自动化运维与排障**：运维 Agent 将历史故障处理流程沉淀为 Skill，当同类问题再次发生时，新 Agent 可直接调用既有技能快速响应。
- **个人自动化工作流**：个人开发者构建“一人公司”式的自动化系统，让多个 Agent 分别处理邮件、日程、代码任务，通过共享记忆保持整体一致性。

## 项目亮点

- **团队级记忆范式**：与市面上大多数单 Agent 记忆方案不同，本项目从设计之初就面向多 Agent 协作场景，提供记忆共享机制，这是本质性的差异化优势。
- **四维记忆资产模型**：将记忆细分为 Chat、Skill、Wiki、Code 四个维度，覆盖了 Agent 工作流中几乎所有关键信息类型，比单一的“对话历史”存储更加完备。
- **极低接入门槛**：借助 Proxy 层与主流框架无缝对接，开发者无需重写现有 Agent 逻辑，即可快速获得团队记忆能力，采用成本极低。
- **全栈可部署**：从本地开发到云端生产，一套代码即可完成部署，配合 Docker Compose 一条命令启动全部组件，运维体验顺畅。
- **社区与生态背书**：项目由腾讯云数据库团队维护，并已入选 GitHub Trend 榜，社区活跃度持续攀升，具有可靠的持续演进保障。

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [简体中文 README](https://github.com/TencentCloud/TencentDB-Agent-Memory/blob/main/README_CN.md)
- [npm 包地址](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [Discord 社区](https://discord.gg/dJQM6mKMF)
