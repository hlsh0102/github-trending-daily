---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-08-06
language: TypeScript
stars_total: 15285
stars_today: 1892
---
## 项目概述

TencentDB Agent Memory 是腾讯云推出的一款团队级 AI Agent 记忆中枢，旨在解决 Agent 在长期运行中“记忆缺失”和“知识孤岛”的问题。传统 AI Agent 每次对话都从零开始，无法积累经验，也难以在团队内部共享知识。该项目将对话记录、文档和代码转化为四种可复用的记忆资产——Chat Memory（对话记忆）、Skill（技能）、LLM-Wiki（大模型知识库）和 Code-Graph（代码图谱），并通过统一的治理、共享机制，让这些记忆资产在不同 Agent 和框架之间自由流通。

项目面向 AI 应用开发者、企业智能化团队以及独立开发者，尤其适合需要构建多 Agent 协作系统或长期运行 AI 服务的场景。通过 TencentDB Agent Memory，团队可以将分散的智能体经验沉淀为组织级资产，实现“ Agents remember. Humans innovate.”（智能体负责记忆，人类专注创新）的核心理念。

## 核心功能

- **多类型记忆资产管理**：支持四种记忆形态，对话记忆用于保留交互上下文，技能模块封装可复用的工具调用流程，LLM-Wiki 存储结构化的领域知识，代码图谱则梳理代码库的依赖关系与函数逻辑。
- **团队级共享与治理**：记忆不再局限于单个 Agent，而是通过 Memory Hub 实现团队内多智能体的共享访问，并提供权限管理和版本控制能力，确保数据安全与一致性。
- **跨框架兼容**：基于 TypeScript 构建，提供标准化的 SDK 和 API 接口，可与主流 Agent 框架（如 OpenClaw、Hermes）无缝集成，也支持自定义接入。
- **一键部署架构**：提供 `memory-core`（核心存储）、`memory-hub`（管理网关）和 `proxy`（代理服务）三个组件，通过 Docker Compose 可快速启动完整环境。
- **智能检索增强**：内置语义搜索和向量索引能力，Agent 可高效定位相关记忆，减少无效 token 消耗并提升响应质量。
- **持续进化机制**：系统会自动从新对话和新文档中提取知识，不断丰富记忆资产库，形成团队知识的正向循环。

## 技术架构

项目采用典型的三层服务设计。底层为 `memory-core`，负责记忆资产的持久化存储，支持多种数据库后端（包括腾讯云数据库 TencentDB 系列）；中间层为 `memory-hub`，作为记忆管理的控制平面，处理知识抽取、索引构建、权限校验和版本控制等逻辑；顶层为 `proxy`，负责与外部 AI Agent 框架通信，提供统一的 RESTful API 和 WebSocket 接口，屏蔽底层实现细节。

在技术选型上，项目充分利用 TypeScript 的静态类型系统，保证了代码的可维护性。知识抽取环节结合了 LLM 解析与规则引擎，能够从非结构化文本中提取实体、关系和操作流程。代码图谱的构建则采用抽象语法树（AST）分析技术，实现跨文件的依赖追踪。所有记忆资产均以标准化 JSON 格式存储，并生成向量嵌入以支持语义检索。

项目还设计了开放的数据模型，允许开发者自定义记忆类型和属性。部署层面，官方提供全局镜像仓库以及 Docker Compose 编排文件，用户可在 Kubernetes 或云服务器上自由扩展。基准测试覆盖了知识召回率、响应延迟等关键指标，为生产环境选型提供参考。

## 安装与使用

安装过程较为简单，前提是本地已安装 Docker 和 Docker Compose。通过以下命令即可一步启动所有服务：

```bash
git clone https://github.com/Tencent/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-image
docker-compose up -d
```

启动后，`memory-core` 默认监听 8080 端口，`memory-hub` 监听 8081 端口，`proxy` 暴露 8082 端口。开发者可通过 `proxy` 的接口进行最小化验证：

```bash
# 存储一条对话记忆
curl -X POST http://localhost:8082/v1/memories \
  -H "Content-Type: application/json" \
  -d '{"type": "chat", "content": "用户喜欢简洁的回复风格", "metadata": {"source": "support"}}'

# 查询相关记忆
curl -X GET "http://localhost:8082/v1/search?q=回复风格&limit=3"
```

对于 Node.js 项目，可直接安装 npm 包并初始化客户端：

```bash
npm install @tencentdb-agent-memory/memory-tencentdb
```

```javascript
import { MemoryClient } from '@tencentdb-agent-memory/memory-tencentdb';

const client = new MemoryClient({ endpoint: 'http://localhost:8082' });
const results = await client.search('如何部署微服务');
console.log(results);
```

## 适用场景

- **企业级客服机器人团队**：多个客服 Agent 共享用户历史记录和服务知识，确保不同会话间体验一致，并持续积累常见问题解决方案。
- **研发辅助智能体**：结合 Code-Graph 记忆，代码审查助手可以理解项目整体结构，新成员加入时也能快速获取代码库上下文。
- **个人知识管理 Agent**：作为“一人公司”的运营中枢，汇聚邮件、文档、会议记录等数据，为决策提供全面的信息支持。
- **多智能体协作平台**：在复杂任务中，规划 Agent、执行 Agent 和验证 Agent 通过共享记忆协作，避免重复劳动并保持目标对齐。

## 项目亮点

相较于 LangChain 的 Memory 模块或 VectorStore 类方案，TencentDB Agent Memory 的核心差异在于其**团队级**定位。多数方案只解决单 Agent 的状态管理，而本项目将记忆提升为组织级资源，引入 RBAC 权限控制和跨 Agent 共享机制，更适合企业级生产环境。

此外，项目开箱即用的一键部署体验降低了上手门槛，用户无需自行搭建向量数据库和知识抽取管道。其多类型记忆资产的划分也更为细致，尤其是 Code-Graph 将代码分析纳入记忆体系，这在同类开源项目中较为少见。项目在 GitHub 上已获得超过 1.5 万 Star，社区活跃度高，迭代迅速，提供了持续演进的保障。

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [NPM 包地址](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [OpenClaw Agent 框架](https://github.com/openclaw/openclaw)
