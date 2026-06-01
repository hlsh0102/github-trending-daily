---
tags:
  - trending
  - article
repo: supermemoryai/supermemory
date: 2026-06-01
language: TypeScript
stars_total: 23526
stars_today: 264
---
## 项目概述

Supermemory 是一个面向 AI 时代的记忆引擎与上下文管理应用，旨在解决当前大语言模型普遍存在的“记忆缺失”问题。无论是个人的知识管理，还是企业级 AI 应用中的上下文连续性，Supermemory 提供了一个极速、可扩展的记忆层。其目标用户包括 AI 开发者、知识工作者以及需要将长期记忆集成到 AI 工作流中的团队。项目在 LongMemEval、LoCoMo 和 ConvoMem 三大主流 AI 记忆基准测试中均排名第一，证明了其在记忆建模与检索方面的顶尖性能。

## 核心功能

- **多源记忆摄取**：支持从网页、文档、笔记、对话等多种来源自动提取和存储信息，构建统一的知识图谱。
- **语义上下文检索**：基于向量的语义搜索，能够从海量记忆库中精准找到与当前问题最相关的上下文片段，而非仅仅依赖关键词匹配。
- **实时记忆更新**：支持增量式记忆写入和更新，无需全量重建索引，确保系统在高频交互中依然保持低延迟。
- **多级记忆管理**：区分短期记忆（会话内）与长期记忆（跨会话），支持手动或自动将重要内容提升至长期存储，并允许遗忘或修正。
- **开发者友好 API**：提供 RESTful API 和 SDK（支持 TypeScript 和 Python），让开发者可以轻松将记忆层嵌入自己的 AI 应用、聊天机器人或自动化流程。
- **可扩展的存储后端**：底层支持 PostgreSQL、Redis、向量数据库（如 Pinecone、Weaviate）等多种存储方案，用户可根据规模与成本灵活配置。

## 技术架构

Supermemory 采用模块化的微服务架构，核心由三部分组成：**摄取管道**、**记忆存储层**和**检索引擎**。摄取管道使用事件驱动架构（基于 RabbitMQ 或 Kafka），支持异步处理海量数据源——例如将网页内容抓取、分块、嵌入向量化等任务离线完成。记忆存储层采用混合存储策略：元数据关系存储在 PostgreSQL 中，语义向量存储在专用向量数据库，而热数据（最近交互）则放在 Redis 缓存中以实现毫秒级响应。检索引擎实现了多阶段召回——先通过 BM25 关键词匹配和向量相似度计算进行初筛，再经由重排序模型（如 Cohere Rerank）精排，最终返回最相关的 5-10 条结果。

项目完全用 TypeScript 编写，这意味着天然具备类型安全与全栈同构能力。前端（Next.js）与后端（NestJS）共享相同的类型定义与部分工具函数，减轻了上下文切换成本。此外，Supermemory 设计了嵌入无关性（embedding-agnostic）接口，允许用户自由切换 OpenAI、Cohere、Hugging Face 等嵌入模型，甚至使用本地模型保持数据私密。

## 安装与使用

### 快速开始（本地开发）

1. **克隆仓库**：
   ```bash
   git clone https://github.com/supermemoryai/supermemory.git
   cd supermemory
   ```

2. **安装依赖**：
   ```bash
   # 使用 pnpm（推荐）
   pnpm install
   # 或使用 npm
   npm install
   ```

3. **配置环境变量**：根据 `.env.example` 创建 `.env` 文件，至少设置：
   ```env
   DATABASE_URL=postgresql://...
   VECTOR_DB_URL=...
   OPENAI_API_KEY=sk-...
   ```

4. **初始化数据库**：
   ```bash
   pnpm db:migrate
   pnpm db:seed   # 可选，插入示例数据
   ```

5. **启动开发服务器**：
   ```bash
   pnpm dev
   ```
   访问 `http://localhost:3000` 即可看到仪表盘。

### 最小可用示例（API 调用）

```python
import supermemory

client = supermemory.Client(api_key="your-key")

# 存入一段记忆
client.memory.save(
    content="今天学习了如何用 LangChain 构建 RAG 应用",
    source="笔记",
    metadata={"project": "rag-tutorial"}
)

# 检索相关记忆
results = client.memory.query("什么是 RAG？", top_k=5)
for r in results:
    print(r.content)
```

## 适用场景

- **个人知识助手**：作为私有知识库，自动记录阅读过的文章、笔记、聊天内容，当再次提问时能回忆起之前讨论过的细节，避免重复询问。
- **企业 AI 客服**：将客户历史工单、产品文档、FAQ 整合为记忆库，使 AI 客服在对话中能够引用前几次交流的上下文，提供连贯的服务。
- **研究论文阅读**：自动抓取并存储论文摘要、关键图表、个人批注，当撰写新论文或做综述时，快速检索到相关文献和自己的思考。
- **AI 工作流编排**：在复杂自动化（如多步工具调用、代码生成）中保持状态记忆，使 AI Agent 能记住上一步的操作结果并基于此决策。

## 项目亮点

与同类项目（如 MemGPT、mem0、LangChain 的记忆模块）相比，Supermemory 的核心优势在于 **极致的性能与基准验证**。在 LongMemEval、LoCoMo、ConvoMem 三个权威评测中均位列第一，这意味着它的记忆 recall 准确率和上下文保持能力经过严格检验。其次，项目是**开源且可自托管**的，不依赖特定云服务，用户可以完全掌控数据隐私。此外，Supermemory 的 **多租户架构** 天生支持团队协作场景，每个用户或组织拥有隔离的记忆空间，同时允许跨租户共享特定知识库。最后，通过提供 TypeScript 和 Python 双语言 SDK，它降低了前后端开发者集成记忆能力的门槛。

## 相关链接

- [GitHub 仓库](https://github.com/supermemoryai/supermemory)
- [官方文档](https://supermemory.ai/docs)
- [快速入门指南](https://supermemory.ai/docs/quickstart)
- [控制台（Dashboard）](https://console.supermemory.ai)
- [Discord 社区](https://supermemory.link/discord)
- [npm 包](https://www.npmjs.com/package/supermemory)
- [PyPI 包](https://pypi.org/project/supermemory/)
