---
tags:
  - trending
  - article
repo: infiniflow/ragflow
date: 2026-08-13
language: Go
stars_total: 87619
stars_today: 139
---
## 项目概述

RAGFlow 是一款领先的开源检索增强生成（Retrieval-Augmented Generation, RAG）引擎，旨在为大型语言模型（LLM）打造卓越的上下文层。它深度融合了前沿的 RAG 技术与 Agent 能力，解决了传统 RAG 系统在处理复杂文档、保障信息准确性和实现深度推理方面的不足。RAGFlow 的目标用户包括需要构建企业级知识库问答系统、智能客服、深度文档分析工具的开发者、数据科学家以及 AI 应用架构师。项目采用 Apache-2.0 许可证，在 GitHub 上拥有超过 8.7 万 Star，是目前最活跃的 RAG 开源项目之一。

## 核心功能

- **深度文档理解**：支持从 Word、PPT、Excel、PDF、图片及扫描件等 20 余种格式的文档中精准提取信息，内置 OCR 与版面分析能力，可解析复杂表格、公式与多栏排版，显著降低信息丢失率。
- **基于图识别的 RAG 引擎**：采用独特的“图”式文档结构解析方法，将文档片段以节点和关系组织，避免了传统分块（Chunking）导致的语义割裂，支持更精准的检索与引用。
- **可解释的引用溯源**：生成的每一个答案都强制附带文档引用来源，用户可一键回溯至原始文本或图片位置，有效解决大模型“幻觉”问题，大幅提升结果可信度。
- **集成 Agent 工作流**：内置 Agent 框架，支持将 RAG 检索与多步推理、工具调用、API 交互相结合，可编排诸如“多文档对比分析”或“数据驱动的动态报告”等复杂任务。
- **灵活的召回与重排**：提供混合检索（关键词 + 向量 + 图关系）与可配置的重排序策略，允许根据业务场景在“召回率”与“精准度”之间灵活权衡。
- **低代码可视化编排**：提供友好的 Web UI，通过拖拽式流程画布即可构建 RAG 应用，无需编写复杂代码，同时支持基于 HTTP 的完整 API 服务，方便集成至现有业务系统。

## 技术架构

RAGFlow 的技术架构体现了**数据-检索-生成**三层解耦与深度融合的设计理念。

- **核心语言与底层**：项目主体语言为 **Go**，这使得引擎具备高并发、低资源占用的特点，适合作为企业级后端服务部署。其底层充分吸收了 Elasticsearch 等成熟检索组件的能力，并结合自研的文档解析管线。
- **文档解析管线（DeepDoc）**：这是 RAGFlow 的基石。它利用深度学习模型（如 LayoutReader 等）对文档进行版面分析，识别标题、段落、表格、图片等元素，然后将文本块以**树形或图结构**进行索引，而非简单的顺序分割。
- **Agent 与执行引擎**：Agent 引擎基于有向无环图（DAG）设计，将“检索”、“重排”、“推理”、“生成”等步骤视为节点。每个节点均可独立调用（如调用 OpenAI、Claude 或本地模型 API），并支持 Python 脚本来扩展逻辑。这种设计使得流程具备高度可定制性，并能通过 Graph 模式实现多轮迭代推理，完成复杂任务。
- **双轨检索机制**：同时维护**全文倒排索引**与**向量索引**。在召回阶段，通过自研的 RARE 算法（Retrieval with Attention to Ranking and Evidence）结合图权重，优先返回具有“证据链”关联的文档片段，保证召回结果的语义连贯性。
- **接口与集成层**：采用前后端分离架构，前端使用 React 构建可视化工作台，后端提供 RESTful API 与 WebSocket 接口，支持 Token 认证，易于构建可观测、可编排的生产级系统。

## 安装与使用

RAGFlow 提供了两条主要安装路径，推荐使用 Docker Compose 快速部署：

1.  **前置要求**：确保系统已安装 Docker（版本 ≥ 17.05）与 Docker Compose（版本 ≥ v2.0），建议 CPU 至少 4 核，内存 16 GB 以上。

2.  **通过 Docker 快速启动**：
    ```bash
    # 克隆仓库
    git clone https://github.com/infiniflow/ragflow.git
    cd ragflow/docker

    # 复制并编辑环境变量配置（默认配置可直接使用）
    cp .env.example .env

    # 启动所有服务（内置 Elasticsearch、MySQL、MinIO 与 Redis）
    docker compose -f docker-compose.yml up -d
    ```

3.  **访问与使用**：
    服务启动后，浏览器访问 `http://localhost:80`。首次登录需注册管理员账号。登录后，通过以下最小步骤创建第一个 RAG 应用：
    - 在“知识库”中创建数据集，上传你的 PDF 或 Word 文档，系统将自动解析并建立索引。
    - 在“应用”中新建一个“聊天助手”应用，在“基础知识库”中选择刚才创建的数据集。
    - 在对话框中输入问题，即可获得带引用的答案。

    **最小 API 调用示例**（基于 Python Requests）：
    ```python
    import requests

    API_BASE = "http://localhost/api/v1"
    # 获取 API Key: 在界面的“API”页面生成
    headers = {"Authorization": "Bearer <your_api_key>"}
    payload = {
        "name": "my_new_chat",
        "dataset_ids": ["<your_dataset_id>"],
        "model": "gpt-3.5-turbo"  # 或你的本地模型
    }
    resp = requests.post(f"{API_BASE}/chats", json=payload, headers=headers)
    print(resp.json())
    ```

## 适用场景

- **企业私有知识库问答**：将内部规章制度、产品手册、技术文档导入 RAGFlow，构建安全可控的智能问答系统，员工可快速查询并直接定位原文出处。
- **深度研究报告与合规审查**：针对大量招股书、研报、合同进行多文档对比分析。通过 Agent 工作流，可自动抽取关键指标差异，并生成附有全文证据链的复核报告。
- **智能客服与工单处理**：对接企业售后知识库，通过混合检索能力理解用户长尾问题，配合 Agent 调用订单查询接口，实现自动化的复杂业务办理。
- **学术研究与辅助写作**：处理海量论文，通过图结构理解论文间的引用关系，辅助研究人员进行文献综述，并针对特定观点生成带有严格引用的综述段落。

## 项目亮点

- **精准度优先**：区别于其他仅做向量化的 RAG 框架，RAGFlow 通过“文档结构图”与“强制引用”机制，从根源上缓解了幻觉问题，在需要高度精确的知识密集型场景（如医疗、金融）具有显著优势。
- **Agent 融合的差异化定位**：许多项目将 RAG 与 Agent 分开构建，RAGFlow 将两者原生融合，允许通过可视化的 DAG 编排复杂的“检索 + 推理 + 行动”闭环，超越了单纯的知识问答范畴。
- **全栈自研与可扩展性**：从文档解析（DeepDoc）、索引引擎（基于 Go 与 ES）到 Agent 流程编排，核心组件均为自主研发，避免了拼接不同开源库带来的兼容性问题，并提供宽松的 Apache-2.0 许可，方便二次开发。
- **企业级部署友好**：提供了一键化的 Docker 部署方案，并内置了对象存储（MinIO）、向量检索（ES）等依赖，减少了系统集成与运维成本，不仅支持云端，也适合内网私有化部署。

## 相关链接

- [GitHub 仓库](https://github.com/infiniflow/ragflow)
- [官网](https://ragflow.io/)
- [云服务体验](https://cloud.ragflow.io/)
- [中文文档](https://ragflow.io/docs/dev/)
