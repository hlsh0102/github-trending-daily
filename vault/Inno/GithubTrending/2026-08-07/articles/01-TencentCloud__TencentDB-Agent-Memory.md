---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-08-07
language: TypeScript
stars_total: 16634
stars_today: 1057
---
## 项目概述

TencentDB Agent Memory 是腾讯云推出的团队级 AI Agent 记忆中枢，旨在解决当前 AI 智能体在长期协作中面临的记忆碎片化、知识无法复用、团队经验难以沉淀等核心痛点。项目将对话记录、文档资料和代码片段转化为四种可复用的记忆资产——Chat Memory（对话记忆）、Skill（技能）、LLM-Wiki（大模型知识库）和 Code-Graph（代码图谱），并为这些记忆资产提供统一的治理、共享和装配能力，使其能够跨智能体和框架流转使用。

该项目面向三类核心用户：一是希望构建可持续进化智能体的个人开发者，二是需要将多个 Agent 协同编排的团队，三是关注企业级 AI 应用落地、需要知识资产沉淀的技术团队。通过将记忆从单个 Agent 的私有状态中解放出来，TencentDB Agent Memory 让“智能体团队”成为可能——每个 Agent 不再是孤立的信息孤岛，而是共享同一个不断生长的记忆体系。

## 核心功能

- **四种记忆资产模型**：将原始交互数据提炼为 Chat Memory（对话上下文）、Skill（可执行技能）、LLM-Wiki（结构化知识文档）和 Code-Graph（代码依赖关系图），覆盖智能体工作所需的大部分知识形态。
- **团队级记忆共享**：记忆资产不再局限于单个 Agent 的会话窗口，而是存储于中央化的 memory-hub，支持多个 Agent、多个框架同时读写，实现真正意义上的团队记忆。
- **开放框架适配**：与 openclaw、Hermes 等主流 Agent 框架深度集成，同时也提供标准化 API，可以便捷地接入任何自定义 Agent 系统。
- **一键部署体验**：通过 docker-compose 启动 memory-core（核心存储）、memory-hub（记忆管理服务）和 proxy（代理层）三个服务，即可在几分钟内搭建完整的记忆基础设施。
- **记忆治理能力**：提供记忆的版本管理、权限控制和生命周期管理，确保记忆资产的准确性、安全性和时效性。

## 技术架构

TencentDB Agent Memory 采用三层解耦的服务化架构：

**memory-core** 负责记忆的底层存储，基于腾讯云数据库 TencentDB 构建，支持结构化与非结构化数据的混合存储，并针对向量检索和关系查询做了专门的索引优化。

**memory-hub** 是记忆管理的中枢服务，封装了记忆的写入、提取、更新和删除逻辑。它负责将原始对话流通过语义分析、摘要抽取和关联建模，转化为高质量的四种记忆资产。该服务采用事件驱动的异步处理架构，能够实时响应用户交互并持续更新记忆状态。

**proxy** 层则作为标准化的接入网关，向上游 Agent 框架提供统一的 RESTful API。这一层设计使得底层存储和记忆算法的变更对于上层应用完全透明，不同框架的 Agent 可以通过同一套接口访问共享记忆。

在记忆组织层面，项目引入了 Team Memory 的设计理念。每个团队（Team）拥有独立的命名空间，团队内的所有 Agent 共享该命名空间的记忆资产。这种组织方式与企业在现实世界中的组织结构高度对应，使得记忆的权限边界和管理粒度更加清晰。

## 安装与使用

安装过程非常简便，只需几步即可启动全部服务：

```bash
# 1. 克隆仓库
git clone https://github.com/Tencent/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory

# 2. 进入部署目录
cd deploy/global-imag

# 3. 使用 docker-compose 一键启动（包含 memory-core、memory-hub、proxy）
docker-compose up -d
```

三个服务启动后，memory-hub 默认会监听本地端口。以下是最小可用示例，展示如何通过 proxy 将一段对话写入记忆，并从中检索相关内容：

```bash
# 向记忆库写入一条对话记录
curl -X POST http://localhost:8080/v1/memory \
  -H "Content-Type: application/json" \
  -d '{
    "team": "my-team",
    "type": "chat",
    "content": "用户反馈登录页面加载超时，建议检查 CDN 缓存配置"
  }'

# 检索与“登录”相关的历史记忆
curl -X GET "http://localhost:8080/v1/memory/search?team=my-team&query=登录&top_k=5"
```

对于已经使用 openclaw 或 Hermes 框架的开发者，可以在框架配置中直接指定 proxy 的地址作为记忆后端，无需编写额外代码即可启用团队级记忆能力。

## 适用场景

**多智能体协作编排**：当一个复杂任务需要多个 Agent 分工完成时，TencentDB Agent Memory 充当它们之间的信息交换枢纽。例如，一个 Agent 负责收集需求，另一个负责生成代码，第三个负责测试，它们可以通过共享记忆无缝传递上下文，避免重复沟通和上下文丢失。

**个人智能体团队的长期进化**：开发者可以围绕自己的工作流程创建多个专业 Agent（如代码审查 Agent、文档撰写 Agent、数据分析 Agent），这些 Agent 共享同一个记忆库。随着时间推移，它们对用户偏好、项目背景、历史决策的理解不断加深，真正实现“越用越懂你”。

**企业知识资产管理**：将团队的业务文档、技术方案、客户沟通记录全部导入记忆体系，通过 LLM-Wiki 模块将其转化为结构化的知识资产。新成员加入时，可以快速从记忆库中获取团队的隐性知识，显著缩短融入期。

## 项目亮点

- **团队级而非单机级记忆**：大多数 Agent 框架只提供会话级或用户级的记忆管理，TencentDB Agent Memory 将记忆提升到团队维度，这解决了多 Agent 协作中信息不同步的根本问题。
- **四种记忆资产的体系化设计**：不同于简单地存储原始对话记录，项目通过智能提炼将信息划分为对话、技能、知识和代码四个维度，每种资产都有针对性的存取和更新策略，记忆的利用效率远高于单一类型的存储方案。
- **底层依赖腾讯云数据库能力**：依托 TencentDB 的高可用、可扩展和生态工具链，记忆服务天然具备企业级的数据可靠性和性能保障，而非实验室级的玩具方案。
- **开放集成而非封闭绑定**：项目刻意设计了 proxy 抽象层来兼容不同 Agent 框架，而不是强制开发者绑定某一家生态，这极大地降低了采用门槛。

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [Trendshift 页面](https://trendshift.io/repositories/29310)
- [OpenClaw 集成文档](https://github.com/openclaw/openclaw)
- [Hermes Agent 文档](https://hermes-agent.nousresearch.com/docs/)
