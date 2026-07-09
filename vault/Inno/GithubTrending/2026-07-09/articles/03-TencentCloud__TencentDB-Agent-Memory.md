---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-07-09
language: TypeScript
stars_total: 7808
stars_today: 318
---
## 项目概述

TencentDB Agent Memory 是一个为 AI Agent 提供完全本地化长期记忆能力的开源项目，由腾讯云数据库团队开发。该项目通过独创的四层渐进式管道架构，在不依赖任何外部 API 的情况下，为 AI Agent 赋予高效、持久的记忆能力。

在实际应用中，AI Agent 常常面临两个痛点：一是对话历史过长导致 token 消耗巨大，二是缺乏有效的长期记忆机制导致任务连贯性差。TencentDB Agent Memory 正是为了解决这些问题而生，其目标用户包括 AI 应用开发者、大模型研究人员、以及任何希望为自己的 Agent 系统添加强大记忆能力的团队。

## 核心功能

- **符号化短期记忆**：将冗长的工具调用日志压缩为紧凑的 Mermaid 符号表示，大幅减少 token 消耗，同时提升任务成功率
- **分层长期记忆**：摒弃传统的平面向量存储方案，采用人格与场景的结构化记忆分层设计，让碎片化的对话转化为有组织的知识
- **渐进式四层管道**：从符号化、压缩、结构化到持久化，构建完整的记忆处理流水线
- **零外部依赖**：所有记忆处理均在本地完成，无需调用任何第三方 API，确保数据安全与隐私
- **与 OpenClaw 深度集成**：开箱即用，针对 OpenClaw 框架进行了专门优化
- **性能显著提升**：在基准测试中，token 消耗最多降低 61.38%，任务通过率提升 51.52%

## 技术架构

TencentDB Agent Memory 的核心设计理念是“拒绝平面存储，拥抱分层与符号化”。其技术架构主要包含四个层次：

1. **符号化层**：将 Agent 产生的原始工具日志、对话记录等，转化为结构化的符号表示（如 Mermaid 图表），这是实现高效压缩的基础
2. **压缩层**：在保持语义完整性的前提下，对符号化后的记忆进行智能压缩，去除冗余信息
3. **结构化层**：将压缩后的记忆片段根据内容类型（如人格特征、场景上下文）进行分类和结构化，形成可检索的知识体系
4. **持久化层**：将结构化的记忆写入本地存储，使用 TencentDB 技术栈保证读写性能和可靠性

整个架构使用 TypeScript 实现，基于 Node.js 运行时，采用模块化设计，允许开发者按需启用不同层级的记忆功能。与传统方案依赖外部向量数据库不同，TencentDB Agent Memory 将整个记忆管道本地化，既降低了延迟，也提升了隐私性。

## 安装与使用

### 安装

```bash
npm install @tencentdb-agent-memory/memory-tencentdb
```

### 最小可用示例

```typescript
import { MemoryAgent } from '@tencentdb-agent-memory/memory-tencentdb';

// 初始化记忆代理
const agent = new MemoryAgent({
  mode: 'long-term', // 使用长期记忆模式
  storagePath: './memories' // 本地存储路径
});

// 记录一条对话
await agent.remember({
  role: 'user',
  content: '我是一名律师，近期在研究人工智能法律问题。'
});

// 检索相关记忆
const relevantMemories = await agent.recall({
  query: '用户的职业',
  topK: 3
});

console.log(relevantMemories);
// 输出: 包含用户身份背景的结构化记忆
```

## 适用场景

- **智能客服系统**：为客服 Agent 提供持续的用户画像记忆，让每次对话都能基于历史交互做出更个性化的响应，减少重复询问
- **个人 AI 助手**：帮助个人助手记住用户的偏好、日程和兴趣，实现更自然的长对话体验
- **知识管理工具**：作为团队知识库的记忆引擎，自动组织和检索项目文档、会议记录等信息
- **复杂任务编排**：在需要多步骤推理的 Agent 工作流中，通过短期记忆追踪任务状态，通过长期记忆积累领域知识

## 项目亮点

与现存的 Agent 记忆方案相比，TencentDB Agent Memory 的差异化优势非常明显：

1. **完全本地化**：无需调用任何外部 API，所有数据处理都在本地完成，这是当前许多云依赖方案无法比拟的
2. **独特的符号化与分层设计**：不是简单的向量存储，而是通过符号化压缩减少了大量的 token 消耗，同时通过分层长期记忆解决了传统平面存储的语义丢失问题
3. **量化的性能提升**：有详细基准测试数据支撑——token 消耗降低 61.38%，任务通过率提升 51.52%，人格记忆准确率从 48% 提升至 76%
4. **轻量级集成**：作为 npm 包发布，可通过简单几行代码快速集成到现有 Agent 系统中，特别是与 OpenClaw 框架的深度适配

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [NPM 包](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
- [OpenClaw 框架](https://github.com/openclaw/openclaw)
- [Hermes Agent 文档](https://hermes-agent.nousresearch.com/docs/)
