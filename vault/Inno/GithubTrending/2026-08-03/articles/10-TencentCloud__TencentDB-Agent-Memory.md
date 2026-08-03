---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-08-03
language: TypeScript
stars_total: 11356
stars_today: 602
---
## 项目概述

TencentDB Agent Memory 是一个面向 AI Agent 的团队级记忆中心（Team-level Memory Hub），由腾讯云数据库团队开源。该项目旨在解决 AI Agent 在长期运行和团队协作中面临的“记忆碎片化”问题——单个 Agent 的上下文窗口有限，且不同会话、不同 Agent 之间的知识难以共享和沉淀。

通过将对话记录、文档资料和代码片段转化为四种可复用的记忆资产（Chat Memory、Skill、LLM-Wiki、Code-Graph），该项目让 AI Agent 不仅“记住”过去，更能像人类团队一样积累经验、分工协作。其目标用户包括：使用 AI Agent 进行复杂任务开发的工程师、需要构建多 Agent 协作系统的技术团队，以及希望将 AI 能力深度集成到业务流程中的组织。

项目采用 TypeScript 编写，当前在 GitHub 上已获得超过 11000 颗星，并处于快速迭代的 Beta 阶段，被 Trendshift 社区收录。

## 核心功能

- **Chat Memory（对话记忆）**：自动记录 Agent 与用户、Agent 与 Agent 之间的多轮对话，支持按时间、主题或参与者进行检索，让 Agent 在长时间跨度内保持上下文连贯。

- **Skill（技能沉淀）**：将从对话中提炼出的可执行流程、工具调用序列或问题解决模式固化为标准化的“技能”，可被团队内其他 Agent 按需调用，避免重复试错。

- **LLM-Wiki（知识库）**：将文档、FAQ、内部规范等非结构化文本转化为结构化的向量化知识条目，支持语义检索，帮助 Agent 在回答问题时引用最新、最准确的知识。

- **Code-Graph（代码图谱）**：对代码仓库进行解析，建立函数、类、模块之间的依赖关系图，使 Agent 在代码生成、重构或 Bug 修复时能理解全局结构，而非只看到孤立片段。

- **统一管控与共享**：所有记忆资产均支持权限管理、版本控制和跨 Agent 共享，团队管理员可以精细化控制谁能读取、谁可修改。

- **多框架兼容**：提供与主流 Agent 框架（如 OpenClaw、NousResearch Hermes 等）的适配层，无须重写现有 Agent 即可接入记忆能力。

## 技术架构

TencentDB Agent Memory 采用“三服务一中心”的微服务架构，整体设计围绕“记忆接入 — 处理 — 存储 — 分发”的生命周期展开：

- **memory-core（记忆核心）**：负责接收来自各类 Agent 框架的原始数据流（对话、文档、代码改动），执行预处理、实体抽取、向量化嵌入等操作，并将结果写入统一的存储层。该服务实现了多租户隔离，不同团队的数据在逻辑上完全隔离。

- **memory-hub（记忆中枢）**：作为记忆资产的统一管理面，提供 RESTful API 和 GraphQL 接口，承载元数据管理、权限校验、资产检索和版本控制。它内部维护了四类记忆资产的索引结构，其中 Code-Graph 采用图数据库存储以支持复杂关系查询。

- **proxy（代理服务）**：充当 Agent 与 memory-hub 之间的轻量网关，自动处理认证、限流、协议转换和缓存。代理层支持热插拔，可以适配不同的 Agent 框架而不影响核心服务。

- **统一存储**：底层依赖腾讯云数据库能力（如 TDSQL、TencentDB for Redis 等），但也兼容本地文件系统或外部对象存储，便于开发者本地部署测试。

记忆写入采用异步流水线设计：Agent 产生数据后立即返回，后端异步完成嵌入和索引更新，避免阻塞 Agent 推理流程。检索时则通过向量相似度和关键词混合召回，并支持按时间衰减因子调整记忆权重，确保近期信息优先。

## 安装与使用

项目提供了快速部署脚本，通过 Docker Compose 一键启动全部三个服务：

```bash
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-imag
docker-compose up -d   # 启动 memory-core、memory-hub、proxy
```

启动完成后，使用 REST API 接入你的 Agent：

```typescript
import { MemoryClient } from '@tencentdb-agent-memory/memory-tencentdb';

const client = new MemoryClient({
  endpoint: 'http://localhost:8080',
  apiKey: 'your-team-key'
});

// 向记忆库写入一条对话
await client.chatMemory.add({
  sessionId: 'session-123',
  role: 'user',
  content: '如何优化这个查询性能？'
});

// 检索相关记忆
const results = await client.llmWiki.search({
  query: '查询性能优化',
  topK: 5
});

// 获取可复用的技能
const skills = await client.skill.list({ tags: ['database'] });
```

对于非 TypeScript 项目，也可直接调用 HTTP 接口。详细的配置项（如向量维度、存储后端）可在 `config.yaml` 中调整。

## 适用场景

1. **长周期项目助手**：在持续数月的软件开发项目中，Agent 通过 Chat Memory 与 Code-Graph 记住每个迭代的决策过程和代码结构，随时回答“上周我们为什么这样设计”类问题。

2. **多 Agent 团队协作**：在自动运维或智能客服体系中，不同职能的 Agent（如告警分析、故障处理、知识检索）通过共享 Skill 和 LLM-Wiki 形成合力，一个 Agent 发现的解决方案可即时被其他 Agent 复用。

3. **企业内部知识管理**：将员工手册、政策文档、产品说明导入 LLM-Wiki，让公司内部问答机器人基于统一的、版本可控的知识库提供准确回复，而非各自维护私有知识。

4. **代码库智能化**：针对大型遗留系统，Code-Graph 帮助 Agent 快速理解模块依赖和调用链，辅助新人培训、代码审查和重构风险评估。

## 项目亮点

- **完整的记忆资产分类**：不同于传统方案仅提供“对话缓存”，该项目将记忆细分为四种类型，分别对应不同的检索模式和生命周期管理，更贴合实际开发需求。

- **团队级共享设计**：记忆不再是单 Agent 的私有数据，而是可以作为团队资产被治理、授权和共享，真正支持“团队 Agent”的构建。

- **低侵入接入**：通过 proxy 层和官方 SDK，已有 Agent 框架只需少量代码即可接入，不必从零构建记忆系统。

- **生产级部署友好**：基于腾讯云数据库能力构建，天然具备高可用、弹性扩容和备份恢复能力，同时也支持本地部署用于测试。

- **活跃社区驱动**：项目处于 Beta 快速迭代期，GitHub 社区提交频繁，官方提供 Discord 支持渠道，用户反馈能快速进入产品路线图。

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [npm 包页面](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [项目技术文档（README）](https://github.com/TencentCloud/TencentDB-Agent-Memory/blob/main/README_CN.md)
- [社区讨论（Discord）](https://discord.gg/dJQM6mKMF)
