---
tags:
  - trending
  - article
repo: danny-avila/LibreChat
date: 2026-09-16
language: TypeScript
stars_total: 43989
stars_today: 254
---
## 项目概述

LibreChat 是一个开源的 AI 对话平台，定位为“增强版 ChatGPT 克隆”。它并非简单地复刻 ChatGPT 的界面，而是在保留多轮对话体验的基础上，将当前主流的大模型服务、工具调用能力与多用户管理整合到一个可自托管的 Web 应用中。

该项目主要解决的问题是：在商业闭源聊天产品与模型 API 之间，用户往往缺乏一个中立、可自主部署、可自由切换模型的中间层。LibreChat 通过统一的前端交互与后端适配层，让个人开发者、团队乃至企业能够在一个界面中同时接入 OpenAI、Anthropic、Google、AWS Bedrock、Azure、Groq、Mistral、OpenRouter、DeepSeek、Vertex AI 等多家供应商，并按需切换。

其目标用户包括希望私有化部署 AI 助手的开发者、需要统一管理多模型访问权限的团队，以及希望基于现有生态做二次开发的技术人员。项目采用 MIT 协议，截至撰写时在 GitHub 上已获得约 44k Star，且处于持续活跃开发状态。

## 核心功能

- **多模型与多供应商切换**：内置对 OpenAI、Anthropic、Google Gemini、AWS Bedrock、Azure OpenAI、Groq、Mistral、OpenRouter、DeepSeek、Vertex AI 等服务的适配，同时支持 o1、GPT-5 等新模型及 Responses API，用户可在会话中随时切换模型。
- **Agents 与工具生态**：支持 Agents、MCP（Model Context Protocol）、Skills、Functions、OpenAPI Actions 等机制，使模型能够调用外部工具、执行代码或访问自定义接口，从而完成搜索、计算、数据获取等任务。
- **Artifacts 与代码解释器**：提供 Artifacts 面板用于展示和迭代生成的前端代码、文档等内容，并集成 Code Interpreter 与 DALL-E-3 图像生成，扩展对话之外的产出能力。
- **安全的多人认证体系**：内置多用户认证与权限管理，支持会话隔离、Presets 预设配置，适合团队或组织内部署使用。
- **消息检索与预设管理**：支持对历史消息进行搜索，并通过 Presets 保存常用的模型、参数与系统提示组合，减少重复配置。
- **自托管与部署友好**：提供 Docker 等部署方式，并可通过 Railway、Zeabur 等平台一键部署，降低运维门槛。

## 技术架构

LibreChat 以 TypeScript 为主要开发语言，整体采用前后端分离的 Web 架构。前端是基于 React 的单页应用，负责对话界面、模型切换、Artifacts 渲染与用户交互；后端提供 REST 与流式接口，集中处理认证、会话存储、模型请求转发与工具调用编排。

在模型接入层，项目通过统一的适配抽象屏蔽各家 API 的差异，使新增供应商或模型时无需改动前端逻辑。工具调用方面，LibreChat 结合 LangChain 等生态能力，支持 Functions、OpenAPI Actions 与 MCP，将模型输出与外部服务连接起来。数据层通常配合 MongoDB 存储用户、会话与消息，并支持通过环境变量配置的密钥管理方式区分不同供应商的凭证。

这种“统一前端 + 适配后端 + 可插拔工具”的设计，使 LibreChat 既能作为个人自用的聊天入口，也能作为团队级 AI 网关进行扩展。

## 安装与使用

LibreChat 官方推荐使用 Docker 进行部署。基本流程如下：先克隆仓库，进入项目目录后复制环境变量示例文件（如 `.env.example`）并填写所需模型供应商的 API Key、数据库连接等配置，随后通过 Docker Compose 启动服务。启动完成后，在浏览器访问对应端口即可进入注册/登录页面。

最小可用示例可概括为：

1. 准备一台安装有 Docker 与 Docker Compose 的机器。
2. 克隆仓库并配置 `.env`，至少填入一个模型供应商的密钥。
3. 执行 `docker compose up -d` 启动服务。
4. 打开浏览器访问本地服务地址，注册账号后即可开始对话，并在界面中切换模型或启用工具。

对于不具备自托管条件的用户，也可以通过官方提供的 Railway、Zeabur 模板进行一键部署。更详细的配置项与进阶用法可参考官方文档。

## 适用场景

- **个人自建 AI 助手**：希望在自己的服务器上统一管理多个模型 API，避免在多个官方界面之间来回切换。
- **团队内部 AI 平台**：需要多用户账号、会话隔离与统一密钥管理，同时保留模型选择自由度。
- **多模型对比与评测**：在同一会话环境中快速切换不同供应商与模型，比较输出质量与响应表现。
- **工具增强型应用开发**：借助 Agents、MCP、OpenAPI Actions 等能力，将模型与企业内部接口或第三方服务集成。

## 项目亮点

与多数单一模型的 ChatGPT 克隆项目相比，LibreChat 的差异化主要体现在三点。其一，供应商与模型覆盖范围广，且对新兴模型和 Responses API 等接口跟进较快；其二，工具生态完整，Agents、MCP、Skills、Code Interpreter、Artifacts 等能力集中在一个项目中，无需拼装多个独立服务；其三，强调生产可用性，内置多用户认证、Presets、消息搜索等面向真实使用的功能，并保持 MIT 开源协议，便于自托管与二次开发。

## 相关链接

- [GitHub 仓库](https://github.com/danny-avila/LibreChat)
- [官方网站](https://librechat.ai)
- [官方文档](https://docs.librechat.ai)
- [Discord 社区](https://discord.librechat.ai)
- [YouTube 频道](https://www.youtube.com/@LibreChat)
