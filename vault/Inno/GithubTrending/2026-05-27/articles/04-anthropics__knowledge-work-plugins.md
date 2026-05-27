---
tags:
  - trending
  - article
repo: anthropics/knowledge-work-plugins
date: 2026-05-27
language: Python
stars_total: 16833
stars_today: 1718
---
## 项目概述

Knowledge Work Plugins 是一个由 Anthropic 开源的插件集合，旨在将 Claude（Anthropic 开发的大语言模型）转变为特定角色、团队和公司的专属专家。该项目主要面向知识工作者，帮助他们在日常工作中更高效地完成任务。插件基于 Claude Cowork（Claude 的协作工具）构建，同时也兼容 Claude Code。通过预置的技能、连接器、斜杠命令和子代理，这些插件让 Claude 能够理解团队的工作方式、接入所需的工具和数据、处理关键工作流，并提供一致的输出结果。

该项目解决了知识工作者面临的典型痛点：重复性任务、信息分散在不同工具中、缺少标准化工作流程。用户不再需要反复向 AI 解释自己的偏好和流程，而是通过插件赋予 Claude 基于角色和公司特有的上下文认知。

## 核心功能

- **角色专属插件**：提供针对不同岗位的预制插件，包括产品经理、销售、客户支持、工程、设计、营销、法务、财务、人力资源、数据科学等，每个插件都包含了该角色的典型工作技能和工具连接。
- **工具连接器**：每个插件内置与常用 SaaS 工具的连接器，如 Slack、Notion、Jira、Linear、Asana、HubSpot、ZoomInfo、Fireflies 等，实现数据源的自动对接。
- **斜杠命令系统**：提供即用的斜杠命令，用户可以快速触发特定操作，如“/summarize 会议”、“/create 任务”等，减少与 AI 交互的摩擦。
- **自定义能力**：插件可针对公司内部术语、流程和工具进行深度定制，使 Claude 的行为更贴合团队实际需求。
- **多插件组合**：不同角色插件可以组合使用，覆盖跨职能协作场景，例如销售与产品团队的信息同步。
- **开源社区贡献**：项目采用 Apache-2.0 许可证，鼓励用户基于自身经验提出改进或贡献新的插件。

## 技术架构

Knowledge Work Plugins 基于 Python 开发，采用模块化的插件架构。每个插件是一个独立的目录，包含以下核心组件：

- **技能集（Skills）**：定义 Claude 在该角色下能完成的具体任务，如“研究潜客”、“撰写外联邮件”等。
- **连接器（Connectors）**：与外部 API 进行交互的接口模块，负责数据的读写操作。
- **斜杠命令（Slash Commands）**：预定义的命令映射，方便用户通过自然语言或预定义短语触发操作。
- **子代理（Sub-agents）**：针对复杂任务拆分的轻量级 AI 代理，可以在特定上下文中独立运行。

设计上，这些插件与 Claude Cowork 和 Claude Code 通过统一 API 进行集成。插件不依赖特定的后端基础设施，可以部署在用户的本地环境或云端。Anthropic 在项目中提供了大量基于真实工作经验的参考实现，方便用户直接使用或作为起点进行二次开发。

## 安装与使用

### 安装步骤（以 Claude Cowork 为例）

1. **克隆仓库**
   ```bash
   git clone https://github.com/anthropics/knowledge-work-plugins.git
   cd knowledge-work-plugins
   ```

2. **选择需要的插件**（例如 `productivity` 或 `sales`）
   ```bash
   cd productivity
   ```

3. **配置环境变量**
   在插件目录下复制 `.env.example` 为 `.env`，填入相关 API Key 和连接信息（如 Slack Token、Notion API Key 等）。

4. **运行插件**
   按照插件目录中的 `README` 说明执行启动命令。通常需要安装依赖（`pip install -r requirements.txt`）并运行入口脚本。

### 最小可用示例

假设你需要使用 `sales` 插件进行潜客调研，安装配置完成后：

```
$ python run.py

> 斜杠命令: /research_lead --company "Acme Corp" --industry "SaaS"
```

Claude 将根据配置的连接器，自动从 HubSpot、ZoomInfo 或 Clay 拉取相关数据，生成一份包含公司概况、关键决策人、近期动态的调研报告。整个过程无需手动切换工具。

## 适用场景

- **销售团队**：销售人员可以在一个界面中完成潜客调研、撰写外联邮件、查看 Pipeline 状态、生成竞争对比分析。插件自动同步 HubSpot 和 ZoomInfo 的数据，减少在多个浏览器标签页间切换的耗时。
- **产品经理**：PM 可以使用 `product` 插件快速查看用户反馈（来自 Slack、Jira）、生成需求文档、规划产品路线图。斜杠命令如 `/create_feature_request` 可自动创建 Jira Issue。
- **客户支持团队**：支持人员可以结合 `support` 插件创建知识库文章、生成工单回复、关联常见问题，所有操作基于来自 Zendesk 或 Notion 的实际数据进行。
- **跨职能协作**：不同角色的插件可以组合使用，例如销售与产品团队通过共享的 Slack 连接器，实时同步客户反馈和产品功能请求。

## 项目亮点

- **角色驱动而非通用**：与大多数 AI 工具提供通用助手不同，该项目聚焦于特定角色的专业知识和工作流，降低了学习成本和使用摩擦。
- **即装即用与可定制并重**：预置插件足够完成常见任务，同时所有配置文件和技能集均可修改，用户可以根据公司特有的工具和流程进行适配。
- **开源社区共创**：采用 Apache-2.0 许可证，鼓励用户提交自己优化的插件或技能集，形成一个持续演进的插件生态。
- **与 Anthropic 生态深度集成**：插件原生支持 Claude Cowork 和 Claude Code，这意味着用户能够利用 Claude 的上下文理解、推理和代码能力，而不仅仅是简单的文本生成。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/knowledge-work-plugins)
- [Claude Cowork 产品页面](https://claude.com/product/cowork)
- [Claude Code 产品页面](https://claude.com/product/claude-code)
