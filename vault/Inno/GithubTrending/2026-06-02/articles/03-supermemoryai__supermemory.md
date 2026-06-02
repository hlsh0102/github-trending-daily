---
tags:
  - trending
  - article
repo: supermemoryai/supermemory
date: 2026-06-02
language: TypeScript
stars_total: 24166
stars_today: 647
---
## 项目概述

Supermemory 是一个为 AI 时代打造的高性能记忆引擎与应用。它解决了当前大语言模型（LLM）普遍存在的“金鱼记忆”问题——即模型无法在长对话或多次交互中有效保持上下文信息。无论是个人用户还是企业团队，都可以将 Supermemory 作为“第二大脑”，持久化存储、检索和利用任何历史对话、文档或知识片段。

项目在 LongMemEval、LoCoMo 和 ConvoMem 三大主流 AI 记忆基准测试中均取得第一名，证明了其记忆处理能力的业界领先地位。它既提供开箱即用的 Web 应用，也提供可独立集成的 npm 和 PyPI 包，覆盖从端侧到服务端的多种使用方式。

## 核心功能

- **超高速记忆存储与检索**：基于向量数据库和高效索引结构，实现毫秒级写入与精确语义检索，支持海量记忆片段的实时响应。
- **多模态记忆支持**：能够处理文本、代码、结构化数据等多种内容类型，并将其统一转化为可检索的向量表示。
- **长对话上下文管理**：在连续多轮对话中自动压缩、去重、摘要历史信息，显著降低 token 消耗的同时保持关键上下文完整。
- **记忆持久化与时间线**：所有记忆自动带时间戳，支持按时间范围、主题、重要性等维度进行过滤和回溯，形成完整的记忆时间线。
- **即用型 Web 应用**：提供开箱即用的图形界面（Dashboard），用户可直接在其中管理记忆、对话和知识库，无需额外开发。
- **开发者友好 SDK**：提供 TypeScript（npm）和 Python（PyPI）两种语言的官方 SDK，只需几行代码即可将记忆能力集成到现有 AI 应用、Chatbot 或工作流中。

## 技术架构

Supermemory 采用模块化、存储与检索分离的设计思路。核心架构包括以下几层：

- **记忆摄入层**：接收来自 Web 应用、SDK 调用或其他来源的输入。该层负责进行文本分块、实体抽取、摘要生成等预处理工作，将非结构化信息转化为结构化记忆单元。
- **向量化与索引层**：使用先进的嵌入模型将记忆单元转换为高维向量，并写入高性能向量数据库。支持多种索引策略（如 HNSW、IVF）以平衡速度与精度。
- **存储引擎**：采用分布式、可水平扩展的存储后端。除了向量索引外，还保存原始文本、元数据（时间、来源、相关性分数等），支持复杂的结构化查询与混合搜索（向量 + 关键词）。
- **检索与推理层**：提供多种记忆检索策略，包括精确语义检索、模糊匹配、重要性加权排序、时间衰减等。该层还负责在检索结果基础上进行推理压缩，只向 LLM 输入最相关的上下文。
- **API 与接入层**：通过 RESTful API 暴露所有能力，并提供 TypeScript 和 Python 的官方 SDK。SDK 封装了认证、错误重试、批量操作等细节，开发者只需调用 `store`、`retrieve`、`summarize` 等简洁接口。

整体设计强调性能与可扩展性，能够在单个节点处理百万级记忆条目，并支持通过添加节点实现线性扩展。

## 安装与使用

### 快速开始（Web 应用）
1. 访问 [supermemory.ai](https://supermemory.ai) 并注册。
2. 登录 Dashboard 后，即可在左侧面板添加文档、记录笔记或导入对话历史。
3. 在 AI 聊天界面中，Supermemory 会自动将相关记忆作为上下文提供给对话模型。

### 使用 SDK（Python 示例）
```python
import supermemory

# 初始化客户端（需在 Dashboard 获取 API Key）
client = supermemory.Client(api_key="your_api_key")

# 存储一段记忆
client.memory.store("客户张总喜欢打羽毛球，尤其是周日下午", tags=["客户信息", "张总"])

# 检索相关记忆
results = client.memory.retrieve("张总周末有什么爱好？", top_k=3)
for r in results:
    print(r.text, r.score)
```

### 使用 SDK（TypeScript 示例）
```typescript
import { Supermemory } from 'supermemory';

const client = new Supermemory({ apiKey: 'your_api_key' });

await client.memory.store({
  text: '项目需求变更：登陆页面增加 SSO 支持',
  tags: ['项目_A', '需求']
});

const memory = await client.memory.retrieve({
  query: '登陆页面变更内容',
  limit: 5
});
```

## 适用场景

- **个人知识管理**：将阅读笔记、会议记录、日常灵感等碎片化信息存入 Supermemory，后续通过自然语言提问即可快速找回。相当于一个永不遗忘的个人第二大脑。
- **客户支持系统**：集成到客服机器人的后台，存储客户历史对话、偏好、购买记录。当客户再次联系时，机器人能自动调取上下文，提供个性化且连贯的服务，减少客户重复陈述。
- **团队协作与项目管理**：存储项目文档、讨论记录、决策日志。团队成员可通过搜索或提问一键获取项目全貌，新成员可以快速了解项目历史和上下文。
- **AI Agent 长期记忆**：为基于 LLM 的 Agent 提供持久化记忆功能。Agent 可以在多次执行任务间保持对用户偏好、环境状态、历史错误等信息的记忆，显著提升任务执行的准确性和连贯性。

## 项目亮点

- **业界领先的基准成绩**：在 LongMemEval、LoCoMo、ConvoMem 三大顶级记忆评测中均排名第一，记忆准确率、召回率、长上下文处理能力均经过严格验证。
- **极致的性能与可扩展性**：专为大规模实时场景设计，写入和检索延迟均控制在毫秒级，支持从单机到分布式集群的弹性扩展。
- **开箱即用与高度灵活并存**：既提供完整的 Web 产品供非技术用户直接使用，也提供轻量级 SDK 供开发者深度集成，适合从个人到企业的不同需求。
- **多语言 SDK 支持**：原生支持 TypeScript 和 Python，覆盖前端、后端、数据科学等主流开发领域，降低集成门槛。
- **研究驱动**：团队具有深厚的研究背景，所有技术均源自前沿学术成果并经过产品化打磨，确保技术的先进性与实用性。

## 相关链接
- [GitHub 仓库](https://github.com/supermemoryai/supermemory)
- [官方文档](https://supermemory.ai/docs)
- [快速开始指南](https://supermemory.ai/docs/quickstart)
- [控制台/Dashboard](https://console.supermemory.ai)
- [Discord 社区](https://supermemory.link/discord)
