---
tags:
  - trending
  - article
repo: aws/agent-toolkit-for-aws
date: 2026-06-26
language: Python
stars_total: 1194
stars_today: 47
---
## 项目概述

Agent Toolkit for AWS 是由亚马逊云服务（AWS）官方维护的开源工具包，旨在帮助 AI 编码代理在 AWS 平台上高效地构建、部署和管理应用程序。随着大语言模型驱动的 AI 编码代理（如 Claude Code、Codex、Cursor 和 Kiro）的普及，开发者在使用这些代理进行 AWS 开发时面临工具链碎片化、权限管理和最佳实践缺失等问题。该项目正是为了解决这一痛点而生：它提供了一套官方支持的 MCP 服务器、技能和插件，为 AI 代理赋予与 AWS 服务交互的能力，目标用户是使用 AI 编码代理进行 AWS 开发和运维的开发者与团队。

## 核心功能

- **官方支持的 MCP 插件集合**：提供多个预配置的 MCP 插件，覆盖不同的 AWS 使用场景，如 `aws-core`、`aws-agents`、`aws-data-analytics` 和 `aws-agents-for-devsecops`。
- **服务选择与最佳实践指引**：`aws-core` 插件帮助 AI 代理理解 AWS 服务的选择逻辑，并遵循 AWS 官方推荐的最佳实践进行开发、部署和运维。
- **基础设施即代码支持**：支持通过 CDK 和 CloudFormation 进行基础设施的声明式管理和部署。
- **无服务器与容器化支持**：涵盖 Serverless 应用、容器化部署、存储服务、可观测性、账单管理和 SDK 使用等常见开发需求。
- **AI 代理构建支持**：`aws-agents` 插件专门针对在 Amazon Bedrock 和 AgentCore 上构建 AI 代理的场景，简化了代理的开发流程。
- **数据与分析工作流集成**：`aws-data-analytics` 插件支持数据湖、分析和 ETL 工作流，与 S3 Tables、AWS Glue 和 Athena 等服务无缝集成。
- **DevSecOps 集成**：`aws-agents-for-devsecops` 插件专注于安全运维场景，帮助 AI 代理进行事件调查、代码审查和合规检查。

## 技术架构

该项目基于 MCP（Model Context Protocol）协议构建，这是一种允许 AI 代理与外部工具和服务进行交互的行业标准协议。Agent Toolkit for AWS 将 AWS 服务的能力封装为标准的 MCP 服务器和工具，使得任何支持 MCP 的 AI 编码代理都可以无缝调用。项目采用 Python 作为主要实现语言，确保了与 AWS SDK 的天然兼容性。其架构设计遵循“插件化”原则，不同的 AWS 使用场景被封装为独立的插件（如 `aws-core`、`aws-agents` 等），用户可以按需安装，降低了资源占用和复杂度。此外，由于是 AWS 官方维护，这些插件内置了安全监控、IAM 权限最小化和最佳实践检查的能力，为 AI 代理在云环境中的安全运行提供了可控的“护栏”。

## 安装与使用

Agent Toolkit for AWS 的使用非常便捷，尤其对于已经安装了 Claude Code 的用户。以下是典型的安装步骤：

1. **确保环境就绪**：确保你已经安装了 Claude Code 或其他兼容的 AI 编码代理工具。
2. **安装主插件**：在 Claude Code 的终端中使用 `/plugin install` 命令安装所需插件。例如，安装核心插件：
   ```
   /plugin install aws-core@claude-plugins-official
   ```
3. **更新插件索引**：如果遇到 “Plugin not found” 错误，请先更新本地插件市场索引：
   ```
   /plugin marketplace update claude-plugins-official
   ```
4. **安装其他插件**：根据需求安装其他插件，例如：
   - 安装 AI 代理构建支持：`/plugin install aws-agents@claude-plugins-official`
   - 安装数据分析支持：`/plugin install aws-data-analytics@claude-plugins-official`
   - 安装 DevSecOps 支持：`/plugin install aws-agents-for-devsecops@claude-plugins-official`
5. **开始使用**：安装完成后，AI 编码代理便拥有了操作 AWS 服务的能力。你可以直接通过自然语言向其下达 AWS 相关的任务，例如“帮我创建一个 S3 存储桶并配置生命周期策略”。

**最小可用示例**：安装 `aws-core` 插件后，在 Claude Code 中输入：“使用 CloudFormation 部署一个包含 Lambda 函数和 API Gateway 的无服务器 API”。

## 适用场景

- **AI 辅助的 AWS 开发**：开发者使用 AI 编码代理编写 AWS 应用代码时，插件能让代理直接理解并操作 AWS 资源，提升开发效率。
- **基础设施即代码管理**：团队可以用自然语言通过 AI 代理来管理 CDK 或 CloudFormation 模板，实现基础设施的快速创建、更新和删除。
- **安全运维与事件响应**：安全团队可以借助 `aws-agents-for-devsecops` 插件，让 AI 代理辅助进行安全事件调查、代码审查和合规检查自动化。
- **数据工程工作流编排**：数据工程师可以利用 AI 代理和 `aws-data-analytics` 插件，快速搭建和维护数据湖、ETL 流程和分析管道。

## 项目亮点

- **官方维护，可靠可信**：由 AWS 官方团队维护和更新，确保与 AWS 服务的最新功能和安全最佳实践保持同步，避免第三方工具带来的风险。
- **即装即用，生态兼容**：紧密集成 Claude Code 等主流 AI 编码代理的插件市场，安装过程仅需一行命令，无需额外配置。
- **模块化设计，按需选择**：不同场景的插件相互独立，用户无需安装全套工具，只选择当前工作流需要的即可。
- **内置安全护栏**：插件内置安全监控和权限控制机制，为 AI 代理在云环境中的操作提供了可审计、可控制的执行边界。
- **持续更新，社区活跃**：项目在 GitHub 上拥有超过 1100 颗星标，每日新增关注度高，社区活跃，问题反馈和功能请求响应及时。

## 相关链接

- [GitHub 仓库](https://github.com/aws/agent-toolkit-for-aws)
