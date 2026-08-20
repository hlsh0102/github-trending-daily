---
tags:
  - trending
  - article
repo: volcengine/OpenViking
date: 2026-08-20
language: Python
stars_total: 30327
stars_today: 804
---
## 项目概述

OpenViking 是由火山引擎（Volcengine）开源的一个面向 AI Agent 的**自进化上下文数据库**。它旨在解决当前大语言模型应用中一个核心痛点：Agent 的状态管理和知识管理是割裂的，开发者往往需要同时维护向量数据库、KV 存储、外部知识库和多套工具调用逻辑，导致系统复杂度高、上下文一致性差。

OpenViking 将 **Agent Memory（代理记忆）、Knowledge RAG（知识检索增强生成）和 Skills（技能/工具）** 统一到一个整体性的数据库中，让 AI Agent 能够像人类一样在会话过程中动态积累经验、检索相关知识，并逐步提升自身能力。项目采用 Python 编写，以 AGPL-3.0 协议开源，目前已在 GitHub 上获得超过 3 万 star，是当下 AI 基础设施领域最受关注的开源项目之一。

## 核心功能

- **统一上下文存储**：将短期对话记忆、长期用户画像、业务知识文档和技能定义整合为单一数据模型，避免了传统方案中需要拼接多个存储系统的繁琐过程。
- **自进化记忆机制**：Agent 在每次交互后能够自动提炼关键信息并写入记忆，同时定期对旧记忆进行摘要、合并或遗忘，实现记忆的自动维护与优化。
- **混合检索增强**：支持向量检索、全文检索与结构化查询的混合模式，并能根据查询意图自动选择最佳检索策略，显著提升 RAG 的准确率。
- **技能即数据**：把可复用的能力（如 API 调用模板、代码片段、工作流）沉淀为数据库中的一等公民，Agent 可以动态加载、调用甚至学习新技能。
- **内置状态管理**：提供会话级与跨会话的状态跟踪，使 Agent 在复杂多轮任务中能够保持上下文连贯性，避免“失忆”。
- **开发者友好 SDK**：仅需几行代码即可接入主流 Agent 框架，并提供直观的 Web Studio 进行可视化调试和数据管理。

## 技术架构

OpenViking 在架构设计上遵循“存储与计算分离、数据与逻辑统一”的原则。其底层采用可插拔的存储引擎，默认支持 PostgreSQL 与 pgvector，同时抽象出统一的存储接口以适配其他数据库。核心层是一套**上下文编排引擎**，负责将来自对话流程的原始信息流解析为可管理的实体（记忆单元、知识块、技能定义），并根据预定义或自适应的策略将它们写入持久化存储。

在检索方面，项目实现了一个两阶段管道：首先是轻量级的查询路由器，负责判断当前请求是否需要记忆回忆、知识检索或技能匹配；随后进入混合检索器，通过 Rerank 模型对多路召回结果进行融合排序，最终返回最相关的上下文片段。所有操作都通过 RESTful API 或 Python SDK 暴露，易于嵌入 LangChain、LlamaIndex 等主流生态。

值得关注的是其“自进化”能力，OpenViking 内置了后台异步任务，周期性地对记忆库进行一致性检查与重构，例如合并重复记忆、提炼高频主题、淘汰低价值数据，这一设计使系统在长期运行中不仅能保持性能，还能提升上下文的相关性。

## 安装与使用

安装 OpenViking 非常简单，推荐使用 Docker Compose 方式快速启动完整环境（包含数据库和 Studio 界面）：

```bash
git clone https://github.com/volcengine/OpenViking.git
cd OpenViking
docker compose up -d
```

启动后，Studio 管理界面默认运行在 `http://localhost:8080`。然后通过 pip 安装 Python SDK：

```bash
pip install openviking
```

以下是一个最小使用示例：创建一个 Agent 记忆存储并在对话中调用。

```python
from openviking import VikingClient

client = VikingClient(endpoint="http://localhost:8080")

# 创建 Agent 上下文空间
ctx = client.create_context("my-agent")

# 保存一条记忆
ctx.remember("用户偏好使用 Python 编写数据管道")

# 检索相关内容
results = ctx.query("该用户喜欢用什么语言？")
print(results)
```

若要启用知识 RAG，只需要将文档上传至同一上下文空间并设置索引策略，OpenViking 会自动完成分块、向量化与索引构建。

## 适用场景

- **智能客服与虚拟助手**：通过长期记忆识别并记住每个用户的偏好和历史诉求，结合知识库进行精准答疑，减少重复沟通。
- **自动化工作流 Agent**：在需要多步骤操作的场景（如数据分析、报表生成）中，Agent 可以依靠技能库调用合适的工具，并通过状态管理保持每一步的上下文。
- **企业内部知识管理**：将分散在 Wiki、工单、代码库中的信息统一入库，提供基于对话的智能问答接口，大幅降低信息检索成本。
- **个性化教育辅导**：记录学习者的知识盲区与进度，自适应调整讲解策略，并动态补充学习资料。

## 项目亮点

与 LangChain 的 Memory 模块、独立的向量数据库（如 Milvus、Weaviate）等方案相比，OpenViking 的最大差异化在于**“一体化”与“自进化”**。它并非简单的存储组件聚合，而是一个具备数据治理能力的上下文平台。具体亮点包括：

1. **真正意义上的“自进化”**，不只是存储数据，还会主动维护和优化数据，使 Agent 在长期运行中表现越发稳定和智能。
2. **统一数据模型**，将记忆、知识和技能三者打通，开发者无需为不同类型的数据设计各自的管理和检索逻辑。
3. **性能与扩展性兼顾**，基于成熟的 PostgreSQL 生态，既有 ACID 保证，又能通过扩展实现大规模部署。
4. **活跃的社区与产品支持**，依托火山引擎的开源生态，项目迭代迅速，并有官方文档和演示环境可供体验。

## 相关链接

- [GitHub 仓库](https://github.com/volcengine/OpenViking)
- [官方网站](https://www.openviking.ai)
- [在线演示](https://openviking.ai/studio)
- [技术文档](https://docs.openviking.ai/)
