---
tags:
  - trending
  - article
repo: google/agents-cli
date: 2026-07-01
language: Python
stars_total: 4376
stars_today: 445
---
## 项目概述

`agents-cli` 是由 Google 开源的一款命令行工具和技能集，旨在帮助开发者通过自然语言驱动的编码助手，快速在 Google Cloud 的 Gemini Enterprise Agent Platform 上构建、评估和部署 AI Agent。它的核心目标是降低 Agent 开发的门槛，让开发者无需深入了解每一个 Google Cloud CLI 和服务细节，即可利用自己喜爱的编码助理（如 Antigravity CLI、Claude Code、Codex）完成从原型到生产的全流程。无论是初学者还是专业开发者，凡是在 Google Cloud 上构建 Agent 的团队或个人，都会从这个工具中受益。

## 核心功能

- **Agent 创建与原型设计**：通过简单的命令行交互，自动生成 Agent 骨架代码和配置，支持快速迭代和实验。
- **技能管理**：内置一系列预定义的“技能”，涵盖常见功能（如对话管理、知识检索、工具集成），并允许用户自定义扩展。
- **评估与优化**：提供标准化测试框架，可对 Agent 进行性能评估、错误分析和迭代改进建议。
- **部署与治理**：一键部署至 Google Cloud 生产环境，同时支持访问控制、日志监控和版本管理，确保企业级合规。
- **多平台兼容**：无缝对接主流编码助理（Antigravity CLI、Claude Code、Codex），并可作为独立的 CLI 工具使用。
- **本地开发与云端同步**：在本地进行开发和调试，通过 `agents-cli` 自动同步至 Google Cloud 环境，保持一致性。

## 技术架构

`agents-cli` 基于 Python 开发，充分利用了 Google Cloud SDK、Vertex AI 和 Gemini API 等底层服务。其设计遵循以下原则：

- **插件化技能系统**：核心 CLI 引擎负责路由命令和生命周期管理，而具体的 Agent 行为通过“技能”插件实现。这种架构使得功能扩展非常灵活，社区或企业可以按需添加新的技能模块。
- **模板引擎**：内置 Jinja2 等模板技术，用于生成 Agent 配置文件和代码骨架，支持用户自定义模板库。
- **事件驱动与异步处理**：在 Agent 交互和部署流程中采用异步 I/O，提升在复杂任务（如并行评估、大规模部署）下的性能。
- **与 Google Cloud 深度集成**：利用服务账户和 IAM 进行安全认证，通过 Cloud Storage 存储数据集和模型，使用 Cloud Functions 或 Cloud Run 运行 Agent 后端，实现完全托管。
- **开放标准**：内部使用 OpenAPI 规范定义工具接口，Agent 编排遵循通用的对话式 AI 标准（如 LangChain 兼容），降低迁移成本。

## 安装与使用

### 安装步骤

1. 确保您的系统已安装 Python 3.10 或更高版本，以及 pip 包管理器。
2. 通过 PyPI 安装：
   ```bash
   pip install google-agents-cli
   ```
3. 验证安装：
   ```bash
   agents --version
   ```
4. （可选）配置 Google Cloud 凭据：
   ```bash
   gcloud auth application-default login
   ```

### 最小可用示例

创建一个简单的问答 Agent：

1. 初始化项目：
   ```bash
   agents init my-agent --template simple-qna
   ```
2. 编辑生成的 `agent.yaml` 文件，配置知识库来源（如 Cloud Storage 或 BigQuery）。
3. 在本地测试：
   ```bash
   agents test my-agent --query "什么是 Gemini？"
   ```
4. 部署至 Google Cloud：
   ```bash
   agents deploy my-agent --project my-project --location us-central1
   ```
5. 通过 CLI 交互测试部署后的 Agent：
   ```bash
   agents chat my-agent --message "你好，介绍一下你自己"
   ```

## 适用场景

- **企业知识库问答系统**：将内部文档、数据库转换为智能问答 Agent，支持员工自助查询，减少 IT 支持压力。
- **客服自动化**：构建多轮对话的客服 Agent，可集成 CRM、订单系统等后端 API，处理常见咨询和简单工单。
- **开发原型快速验证**：产品经理或开发者快速生成 Agent 原型，评估可行性后无缝进入生产阶段。
- **AI Agent 教育与培训**：教学场景下，学生可通过命令行互动学习 Agent 构建流程，无需记忆复杂云服务命令。

## 项目亮点

- **零配置集成**：与主流编码助理原生兼容，无需编写额外适配代码，即可将 Agent 构建能力注入日常开发工作流。
- **企业级治理开箱即用**：从创建到部署，自动处理 IAM、监控、版本管理，符合 Google Cloud 的安全和合规要求。
- **标准化评估体系**：内置测试框架，支持基于真实数据的自动评估，帮助开发者量化 Agent 性能并持续优化。
- **活跃的社区与文档**：GitHub 上拥有超过 4376 星标，配套完善的文档网站和发布说明，更新迭代透明。

## 相关链接

- [GitHub 仓库](https://github.com/google/agents-cli)
- [官方文档](https://google.github.io/agents-cli/)
- [PyPI 包页面](https://pypi.org/project/google-agents-cli/)
- [发布说明](https://github.com/google/agents-cli/blob/main/RELEASE_NOTES.md)
- [问题反馈](https://github.com/google/agents-cli/issues)
