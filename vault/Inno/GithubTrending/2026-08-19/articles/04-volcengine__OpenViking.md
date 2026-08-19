---
tags:
  - trending
  - article
repo: volcengine/OpenViking
date: 2026-08-19
language: Python
stars_total: 29503
stars_today: 213
---
## 项目概述

OpenViking 是由字节跳动旗下火山引擎团队开源的一款面向 AI Agent 的自进化上下文数据库（Self-evolving Context Database）。它的核心目标是解决 AI Agent 在长时间运行和多任务处理中面临的上下文管理难题——传统方案通常将记忆、知识检索（RAG）和技能调用分散在不同的系统中，导致数据孤岛、上下文碎片化，难以支撑复杂任务的连续执行。

OpenViking 将 Agent Memory（代理记忆）、Knowledge RAG（知识检索增强）和 Skills（技能）统一到一个自进化系统中。所谓“自进化”，意味着系统能够根据 Agent 的交互历史和任务结果，自动优化存储结构、检索策略和技能编排，从而持续提升 Agent 的响应质量与任务完成效率。该项目主要面向 AI 应用开发者、大模型应用架构师以及对 Agent 技术有深度定制需求的研究人员，适合构建从原型到生产级的 Agent 应用。

## 核心功能

- **统一上下文存储**：将短期对话记忆、长期事实记忆、领域知识与可复用技能整合到单一数据模型中，消除多个系统间的数据拷贝与同步成本。
- **自进化索引与检索**：基于反馈信号（如任务成功率、用户评分）动态调整向量索引权重和混合检索策略（结合语义检索与关键词匹配），让最相关的上下文在需要时优先弹出。
- **技能注册与编排**：支持将外部工具、API 或代码片段注册为“技能”，Agent 可依据当前上下文自动选择并组合技能，完成多步骤操作。
- **时间感知记忆衰减**：内置记忆重要性评估机制，对陈旧或低价值的信息进行层级降级或归档，防止上下文窗口被无关历史占用。
- **RAG 流水线加速**：提供高性能的文档切片、向量化与索引更新管道，支持增量式知识库更新，无需全量重建。
- **多租户与可观测性**：支持项目级隔离，并提供详细的上下文检索日志，便于开发者调试 Agent 的“思考依据”。

## 技术架构

OpenViking 基于 Python 构建，核心设计遵循“存储-索引-执行”三层分离架构：

1. **存储层**：采用混合存储模式——热数据使用内存数据库或高并发 KV 存储（如 Redis），冷数据与历史归档使用磁盘型数据库（如 SQLite/PostgreSQL），向量索引默认采用 HNSW 算法，同时支持 FAISS 或 Milvus 作为可插拔后端。
2. **索引层**：该系统实现了独特的“语义-时效双通道索引”。语义通道负责内容相似度匹配，时效通道则结合记忆的创建时间、访问频率与任务重要性评分别计算动态权重，两层结果联合排序后输出给上层。
3. **执行层**：提供简洁的 Python API 和异步接口，Agent 仅需通过 `get_context(query)` 或 `save_memory(data)` 等方法调用，内部自动完成记忆提炼、去重和技能匹配。设计上强调“无侵入式”接入——开发者既可以将其作为独立服务运行（通过 RESTful API），也可以作为本地库嵌入现有 Agent 框架（如 LangChain 或自定义代码）。

架构上值得注意的一点是，OpenViking 在保存新信息时会执行轻量级的“信息提炼”步骤，使用 LLM 将原始交互内容压缩为结构化摘要（如实体、关系、结论），再存储为图结构关联，这使得多轮对话后的实体关系推理能力显著优于纯粹的向量存储。

## 安装与使用

项目需要 Python 3.9+ 环境。可以通过 pip 快速安装：

```bash
pip install openviking
```

也可以从源码构建：

```bash
git clone https://github.com/volcengine/OpenViking.git
cd OpenViking
pip install -e .
```

最小使用示例（本地模式）：

```python
from openviking import ContextDB

# 初始化数据库，指定存储目录
db = ContextDB.storage("./my_agent_data")

# 保存一段交互记忆
db.save_memory(
    user_id="user_123",
    content="用户偏好使用简洁的回复风格，对代码示例要求完整可运行。",
    metadata={"source": "chat_history", "importance": 0.8}
)

# 为后续任务检索相关上下文
context = db.get_context(
    query="如何回复用户关于 Python 代码的问题？",
    top_k=3,
    user_id="user_123"
)

# 注册一个技能
db.register_skill(
    name="exec_code",
    description="在沙箱中执行 Python 代码并返回结果",
    callable_func=my_sandbox_executor  # 自定义函数
)

# 进行带技能提示的上下文查询
response = db.get_context("运行用户的代码", include_skills=True)
```

若需启动独立服务，可运行 `openviking-server` 命令，并通过 HTTP 接口调用。

## 适用场景

- **复杂多轮对话 Agent**：需要持续追踪用户偏好、历史决策和未完成事项的个人助理或客服机器人。
- **企业内部知识问答**：结合私有文档库构建 RAG 系统，但要求系统能根据员工反馈自我调整答案的权重和引用来源。
- **自动化工作流编排**：Agent 需要调用多个外部工具（如邮件、日历、数据库）完成跨系统任务，且需要记住之前步骤的中间状态。
- **研究与实验平台**：用于验证稀疏记忆机制、图结构记忆或自进化策略对模型性能影响的学术项目。

## 项目亮点

与传统的“向量数据库 + 单独记忆模块”方案相比，OpenViking 的差异化优势体现在三个方面：

1. **真正的“自进化”闭环**：多数项目仅将记忆保存下来然后原样检索，而 OpenViking 在检索后收集任务结果作为反馈信号，反过来调整信息的权重和索引结构，形成一个持续的优化循环。
2. **记忆与技能的深度融合**：它不仅存储“事实”，还能将成功的行为路径抽象为可调用的“技能”。这种能力让 Agent 从“知道什么”进步为“知道怎么做”，极大减少了重复编码。
3. **企业级工程细节**：作为火山引擎开源项目，其在多租户隔离、性能调优、数据持久化方面提供了生产级保障，同时采用 AGPL-3.0 许可协议，适合内部部署或二次开发。

## 相关链接

- [GitHub 仓库](https://github.com/volcengine/OpenViking)
- [官方网站](https://openviking.ai/)
- [在线体验 Demo](https://openviking.ai/studio)
- [官方文档](https://docs.openviking.ai/)
