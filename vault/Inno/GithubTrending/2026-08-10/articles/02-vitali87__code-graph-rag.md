---
tags:
  - trending
  - article
repo: vitali87/code-graph-rag
date: 2026-08-10
language: Python
stars_total: 3128
stars_today: 96
---
## 项目概述

Code-Graph-RAG 是一个面向大型代码仓库（Monorepo）的检索增强生成（Retrieval-Augmented Generation, RAG）引擎。它旨在解决传统代码搜索工具和基础 LLM 在理解复杂、多语言代码库时面临的上下文缺失与准确性问题。通过将代码解析为知识图谱，并结合向量检索，该工具让开发者能够以自然语言查询、理解乃至编辑整个代码库。其目标用户是需要在单体仓库中进行跨模块、跨语言代码分析的中大型团队、DevOps 工程师以及 AI 辅助编程工具的开发者和研究者。

## 核心功能

- **多语言代码图谱构建**：自动解析 Python、TypeScript、Java、Go 等多种主流语言的源代码，提取类、函数、接口、调用关系等语义元素，构建成结构化的知识图谱。
- **混合检索策略**：融合基于知识图谱的符号检索和基于向量嵌入的语义检索，既保证查询的精确性（如查找特定函数定义），又能捕获语义层面的相似模式。
- **自然语言代码查询**：支持用日常英语（或中文）提问，例如“哪个模块处理用户认证流程？”，系统会定位到图谱中的相关子图并生成答案。
- **代码编辑建议**：在理解代码结构的基础上，提供基于上下文的修改建议或生成补丁，而不只是简单的代码片段搜索。
- **非侵入式 Cli 与 API**：提供命令行工具和 Python API，方便集成到现有 CI/CD 流程或 IDE 插件中。
- **增量索引**：支持对代码库的增量更新索引，仅重新处理变更文件，适用于频繁迭代的开发周期。

## 技术架构

Code-Graph-RAG 的核心架构遵循“索引-图谱-检索”三层分离设计：

1.  **索引层**：使用 Tree-sitter 之类的解析器生成具体语法树（CST），通过自定义分析器提取实体与引用，并计算符号的嵌入向量。
2.  **图谱层**：采用图数据库（如 Neo4j 或内存中的 NetworkX）存储实体节点（函数、类、文件）和关系边（调用、导入、继承）。图谱不仅保存结构信息，还挂载了每个节点的向量索引，实现图与向量的混合查询。
3.  **检索层**：采用两阶段检索。第一阶段从用户的查询中提取意图并生成候选实体（基于向量相似度），第二阶段利用图谱的遍历能力扩展上下文（例如，查找该函数的所有调用方或被依赖的对象）。最终将子图序列化为 LLM 可理解的文本上下文，供 GPT、Claude 等模型生成回答。

设计上，项目强调**可插拔性**：解析器、图存储、向量库和 LLM Provider 均通过抽象基类解耦，用户可以根据自身基础设施替换组件。同时，它将“细粒度符号检索”作为首要路径，避免了纯向量检索带来的幻觉问题。

## 安装与使用

安装可通过 pip 直接完成：

```bash
pip install code-graph-rag
```

**最小使用示例**：首先对代码库建立索引（以当前目录为例）：

```bash
code-graph-rag index --source ./my_monorepo --output ./graph_store
```

随后启动交互式查询界面：

```bash
code-graph-rag query --graph ./graph_store --question "How does the auth middleware interact with the user service?"
```

作为 Python 库集成：

```python
from code_graph_rag import CodeGraphRAG

# 使用已有的图谱索引；如果没有，可先构建
rag = CodeGraphRAG(graph_path="./graph_store")
answer = rag.query("Find the function that validates JWT tokens and list its callers.")
print(answer)
```

## 适用场景

- **大型单仓（Monorepo）重构**：当团队需要安全地重构数千个文件时，可以用该工具回答“哪些模块受 API 变更影响”，降低回归风险。
- **快速入职与知识传递**：新成员通过自然语言提问即可理解核心服务的架构，无需阅读大量文档或代码。
- **AI 辅助代码审查**：将工具集成到 PR 检查流程中，自动分析变更文件的影响面，并生成带参照的审查评论。
- **构建企业内部的代码助手**：作为底层引擎，为内部聊天机器人或 IDE 插件提供对私有代码库的智能问答能力。

## 项目亮点

与现有的 CodeQL、Grit 或纯向量 RAG 方案相比，Code-Graph-RAG 的差异化优势体现在：

- **图谱与 LLM 的深度耦合**：不是简单地用向量夹带代码片段，而是将结构化的关系路径（调用链、继承树）作为上下文注入提示词，大幅提升回答的推理深度。
- **高可扩展的解析架构**：支持新增语言只需实现一个解析器插件，已有对前端（TS/JS）、后端（Python/Go/Java）的覆盖。
- **对编辑任务的支持**：大多数 RAG 工具只读，该项目通过分析修改影响范围，可提供初步的编辑建议，打通了“查询-理解-修改”的闭环。
- **工程品质**：项目已上 CI 流水线、代码覆盖率与静态分析看板，并提供企业版支持，符合严肃工程项目的标准。

## 相关链接

- [GitHub 仓库](https://github.com/vitali87/code-graph-rag)
- [官网与文档](https://code-graph-rag.com)
- [PyPI 项目页](https://pypi.org/project/code-graph-rag/)
