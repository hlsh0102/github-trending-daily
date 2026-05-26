---
tags:
  - trending
  - article
repo: anthropics/knowledge-work-plugins
date: 2026-05-26
language: Python
stars_total: 15980
stars_today: 1441
---
## 项目概述

Knowledge Work Plugins 是 Anthropic 开源的一套插件集合，旨在将 Claude Cowork 转化为特定角色、团队和公司的专家。项目主要面向知识工作者，帮助他们通过预设的技能、工具连接器、斜杠命令和子代理，让 Claude 更加理解用户的工作方式、偏好和关键工作流程。

该项目解决了知识工作中常见的“重复配置”痛点——每次使用 AI 助手时都需要重新描述工作背景、工具偏好和流程要求。通过插件化的工作流封装，用户只需一次配置，即可让 Claude 始终按照团队熟悉的术语、工具和流程来交付工作成果。

目标用户包括产品经理、销售代表、软件工程师、项目经理、市场专员等各类知识工作者，以及希望统一团队 AI 使用标准的团队管理者。

## 核心功能

- **角色专精化**：为不同岗位提供预设的技能包，例如销售插件包含客户研究、竞争分析和管道管理能力；产品插件则聚焦需求梳理和路线图制定。
- **工具连接器（Connectors）**：预置与主流 SaaS 工具的集成，涵盖 Slack、Notion、Asana、Linear、Jira、HubSpot 等 30+ 第三方服务，使 Claude 能够直接读写企业已有数据。
- **斜杠命令系统**：支持自定义 `/` 命令，例如在销售插件中可使用 `/prospect` 快速调取客户信息，在产品插件中使用 `/roadmap` 查看当前版本计划。
- **子代理编排**：每个插件内可包含多个子代理，分别负责不同子任务（如数据收集、分析、生成报告），由 Claude 根据用户指令自动调度。
- **团队流程定制**：允许用户修改插件内的术语定义、输出格式、审批环节等，使 AI 行为适配公司特有的 SOP（标准操作流程）。
- **跨工具工作流**：支持一次指令跨多个工具执行任务，例如“从 Linear 拉取本周新任务，更新到 Notion 项目看板，并在 Slack 通知相关人员”。

## 技术架构

项目基于 Python 开发，采用插件化架构设计。每个插件都是一个独立的 Python 包，包含以下核心组件：

- **MCP（Model Context Protocol）服务器**：负责处理 Claude 与外部工具之间的双向通信。插件通过 MCP 暴露可调用的工具函数和资源端点，接收 Claude 的推理请求并返回结构化数据。
- **工具定义文件**：使用 JSON Schema 描述每个工具的输入输出参数，确保 Claude 能准确理解如何调用。
- **提示模板**：包含角色上下文、工作流程描述和输出格式要求，作为系统提示词注入到对话中，指导 Claude 的行为风格。
- **认证模块**：处理各 SaaS 工具的 OAuth 或 API Key 认证，实现安全的第三方连接。

架构设计上强调可组合性：用户可以根据需要自由启用、禁用或组合多个插件。例如，一位技术产品经理可以同时加载“产品”和“工程”插件，让 Claude 同时理解两边的工作上下文。

## 安装与使用

**前提条件**：需要一个 Claude Cowork 账户（或兼容的 Claude API）。

**基本安装步骤**：

1. 克隆项目仓库：
```bash
git clone https://github.com/anthropics/knowledge-work-plugins.git
cd knowledge-work-plugins
```

2. 选择需要的插件目录，例如销售插件：
```bash
cd sales
pip install -r requirements.txt
```

3. 配置工具连接：根据插件内的 `.env.example` 文件，填写对应服务的 API Key 或 OAuth 凭据。

4. 启动插件服务器：
```bash
python main.py
```

5. 在 Claude Cowork 中添加该插件作为 MCP 服务器地址。

**最小可用示例**：

以“生产力”插件为例，连接成功后可在 Claude 中输入：

```
/startday 请检查我今天的日历事件，并从 Notion 拉取今天待办任务，在前端格式化展示。
```

Claude 将会依次调用日历连接器和 Notion 连接器，返回整理好的今日工作清单。

## 适用场景

- **销售跟进流程标准化**：销售团队可配置销售插件，使其在每次客户会议前自动从 HubSpot 拉取客户历史记录，调用 ZoomInfo 补充公司背景，生成会议议程草案。
- **跨职能项目管理**：产品经理可使用产品插件，通过一条指令从 Jira 拉取待办项、从 Figma 获取原型链接、从 Confluence 获取技术设计文档，整合为项目周报。
- **团队 onboarding 加速**：新员工可自动加载团队预设的插件配置，无需手动熟悉每个工具的 API 和查询语法，直接通过自然语言完成日常操作。
- **个人知识管理**：独立知识工作者可自定义个人生产力插件，集成自己的笔记应用、待办清单和日历，实现“用自然语言管理所有数字工作流”。

## 项目亮点

与市面上其他 AI 工具接入方案（如直接使用 Copilot、手工编写 API 脚本）相比，Knowledge Work Plugins 的差异化优势在于：

- **即用型插件市场**：项目开源了 11 个预构建的角色插件，覆盖了最常见的知识工作职能，用户无需从零开始搭建就能获得专业级的功能。
- **支持多工具组合工作流**：不同于单个工具的独立对接（如“只连接 Jira”或“只连接 Slack”），插件允许 Claude 在一次交互中跨工具执行多步骤任务。
- **团队级可定制性**：每个插件都可以修改提示词、工具列表和输出模板，适应不同公司的业务术语和流程要求，而非通用的“万能”方案。
- **与官方产品无缝集成**：专为 Claude Cowork 和 Claude Code 设计，避免了第三方插件的兼容性问题和安全审计顾虑。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/knowledge-work-plugins)
- [Claude Cowork](https://claude.com/product/cowork)
- [Claude Code](https://claude.com/product/claude-code)
