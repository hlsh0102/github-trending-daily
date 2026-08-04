---
tags:
  - trending
  - article
repo: TencentCloud/TencentDB-Agent-Memory
date: 2026-08-04
language: TypeScript
stars_total: 12377
stars_today: 1090
---
## 项目概述

TencentDB Agent Memory 是腾讯云推出的一款团队级 AI Agent 记忆中枢，旨在解决多 Agent 协作场景下知识碎片化、记忆不共享的核心痛点。随着 AI Agent 从单机对话走向复杂的多智能体协作，如何让不同 Agent 之间共享经验、复用技能、统一知识库成为实际落地中的关键挑战。该项目将对话记录、文档资料、代码逻辑等原始数据，转化为四类结构化记忆资产——Chat Memory（对话记忆）、Skill（技能）、LLM-Wiki（知识库）、Code-Graph（代码图谱），并在此基础上提供治理、共享和跨框架调用能力。项目面向 AI 应用开发者、Agent 框架维护者以及需要构建"一人公司"式自动化团队的独立开发者，帮助他们摆脱重复训练和提示词堆砌的困境，让 Agent 团队真正具备积累与进化的能力。项目采用 TypeScript 开发，目前在 GitHub 上已获得超过 1.2 万 Star，展现出强劲的社区关注度。

## 核心功能

- **四类记忆资产统一管理**：将对话、文档、代码三类原始输入，自动转化为 Chat Memory、Skill、LLM-Wiki 和 Code-Graph 四类标准化记忆资产，每类资产均有明确的存储格式和检索接口，便于 Agent 按需调用。
- **团队级记忆共享**：支持在多 Agent 之间共享记忆资产，避免每个 Agent 各自维护孤立的知识库，实现一次沉淀、全员复用，显著降低重复建设成本。
- **权限与治理机制**：内置资产管理功能，支持对记忆资产进行版本控制、访问权限设置和生命周期管理，确保团队协作中知识的安全性与一致性。
- **跨框架兼容**：提供框架无关的接入方式，可无缝对接 OpenClaw、Hermes 等主流 Agent 框架，也支持自定义集成，降低迁移成本。
- **一键部署的完整服务栈**：通过 `memory-core`、`memory-hub` 和 `proxy` 三个服务组件的协同工作，提供开箱即用的完整记忆服务，无需复杂配置即可快速启动。
- **智能场景增强**：基于记忆资产，帮助 Agent 在代码生成、任务规划、问题解答等场景中引用历史经验和团队知识，提升输出质量与一致性。

## 技术架构

TencentDB Agent Memory 采用三层服务架构设计。底层为 `memory-core` 服务，负责记忆资产的持久化存储与索引构建，基于高性能数据库实现数据可靠性保障。中间层为 `memory-hub` 服务，承担记忆资产的分类、标注、关联和检索逻辑，是知识加工与分发的中枢。上层为 `proxy` 服务，面向外部 Agent 框架提供统一的 API 接口，屏蔽底层存储细节，使不同框架可以通过标准协议接入记忆服务。

在数据流层面，系统通过解析管道将原始输入（对话、文档、代码仓库）进行结构化拆解：对话记录经过摘要与槽位提取生成 Chat Memory；可复用的操作序列被封装为 Skill；文档知识经过向量化和索引构建进入 LLM-Wiki；代码文件则通过语法分析和依赖解析生成 Code-Graph 图谱。四类记忆资产间保留交叉引用关系，便于 Agent 在检索时发现知识关联。

项目采用 TypeScript 作为主要开发语言，利用其类型系统保障服务间接口的稳定性。部署层面提供全局镜像方案，支持通过 Docker Compose 或云服务快速拉起整套环境。此外，项目强调"即插即用"的设计哲学，尽可能降低与具体 Agent 框架的耦合度，开发者可以通过简单的 REST 调用或 SDK 接入即可获得记忆能力。

## 安装与使用

安装过程简洁，克隆仓库后启动三个服务即可：

```bash
git clone https://github.com/Tencent/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-imag
# 按 README 指引启动 memory-core、memory-hub、proxy 三个服务
```

启动服务后，开发者可以通过以下方式接入 Agent：

```typescript
// 示例：通过 HTTP API 将对话记录写入记忆
const response = await fetch('http://localhost:8080/memory/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    agent: 'support-bot',
    conversation: [...]
  })
});

// 示例：检索与问题相关的 Skill
const skills = await fetch('http://localhost:8080/memory/skill/search?q=payment+refund');
```

对于深度集成，项目提供 SDK 封装，支持在 Agent 框架初始化时注入记忆客户端，并在对话循环中自动调用保存和检索接口。

## 适用场景

- **多 Agent 协作团队**：在客服、运营、开发等多角色 Agent 共存的系统中，共享客户历史、话术模板和排障流程，提升整体协作效率。
- **开源项目自动化维护**：为代码评审 Agent、Issue 管理 Agent 和文档生成 Agent 提供统一的代码图谱与项目知识，实现自动化维护的闭环。
- **个人知识助手**：作为"一人公司"的运营中枢，让个人助手 Agent 记住用户偏好、历史项目和常用工作流，提供越来越个性化的服务。
- **企业知识库问答**：将内部文档转换为 LLM-Wiki 资产，结合 Chat Memory 中的历史问答，构建智能化的企业知识问答系统。

## 项目亮点

与同类 Agent 记忆方案相比，TencentDB Agent Memory 的差异化优势体现在三个方面：其一，它并非单一的记忆存储，而是提供了完整的多类记忆资产体系（对话、技能、知识、代码），覆盖 AI Agent 工作流的全链路知识需求；其二，它强调"团队级"而非"单机级"记忆，通过 Hub 架构实现多 Agent 之间的记忆共享与治理，这是多数开源方案尚未完善的领域；其三，项目背靠腾讯云的基础设施能力，在数据可靠性、性能优化和部署便捷性方面具备企业级水准，同时保持开源开放的态度，支持社区自定义扩展。此外，项目保持了活跃的迭代节奏，并提供了清晰的基准测试（Benchmark），便于开发者评估其在真实场景中的表现。

## 相关链接

- [GitHub 仓库](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- [中文说明文档](./README_CN.md)
- [Discord 社区](https://discord.gg/dJQM6mKMF)
