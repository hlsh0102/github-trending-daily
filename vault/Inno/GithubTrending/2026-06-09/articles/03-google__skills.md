---
tags:
  - trending
  - article
repo: google/skills
date: 2026-06-09
language: Python
stars_total: 12616
stars_today: 461
---
## 项目概述

Agent Skills 是由 Google 官方维护的开源仓库，旨在为 AI Agent 提供直接、可复用的技能模块，使其能够高效调用 Google 产品和技术的能力。该项目解决了当前 AI Agent 在集成复杂云服务时面临的配置繁琐、接口不统一、知识门槛高等问题。目标用户包括 AI 应用开发者、云平台运维工程师、以及希望通过智能体自动化 Google Cloud 工作流程的团队。

## 核心功能

- **即装即用的 Agent 技能包**：通过 `npx skills add google/skills` 命令即可快速安装，自动集成到 Agent 的运行环境中。
- **覆盖核心 Google Cloud 服务**：提供对 Gemini API、BigQuery、Cloud Run、Cloud SQL、Firebase、GKE 等主流服务的标准化技能模块。
- **预置最佳实践配方**：包含如“Google Cloud 新手上路”、“身份认证”、“网络可观测性”等高级配方（Recipe），一键指导 Agent 完成复杂场景。
- **支持 Well-Architected 框架**：提供安全、可靠性等框架下的技能模块，帮助 Agent 遵循云架构最佳规范。
- **模块化设计与按需安装**：用户可在 `npx install` 时自由勾选所需技能，避免冗余依赖。
- **开放扩展**：仓库遵循 Agent Skills 协议，允许社区贡献新的技能模块。

## 技术架构

该项目基于 Python 开发，但安装方式采用 Node 生态的 `npx`，体现了跨语言、跨平台的包容性。每个技能（Skill）被定义为一个独立的子目录，包含描述文件 (`README.md`)、Agent 可执行的指令脚本 (`skill.yaml` 或类似配置)、以及必要的参考文档。技能之间通过标准化的接口与 Agent 框架交互，底层依赖 Google Cloud 官方 SDK，确保与云端 API 的兼容性与安全性。设计上遵循“零配置优先”原则——技能包内置了默认的参数和回退逻辑，使 Agent 即使没有详细配置也能快速启动并执行常见操作。

## 安装与使用

**前提条件**：确保已安装 Node.js 20+ 和 npm（用于运行 `npx` 命令），并拥有有效的 Google Cloud 项目及相应服务权限。

**安装全部技能**：
```bash
npx skills add google/skills
```

**选择性安装**：执行上述命令后，按照提示勾选所需技能（例如 `Gemini API`、`BigQuery Basics` 等）。

**最小可用示例**（以 Gemini API 技能为例）：
1. 安装完成后，唤醒你的 Agent（例如基于 `agentskills.io` 的框架）。
2. 对 Agent 说出指令：“请使用 Gemini API 技能，生成一段关于旅游景点的描述。”
3. Agent 会自动加载技能包，调用 Gemini API 并返回结果。

若需运行复杂流程，可使用预置的“Recipe”技能。例如安装 `Recipe: Onboarding to Google Cloud` 后，Agent 能引导用户完成项目创建、身份认证、开通服务等步骤。

## 适用场景

- **智能运维与云资源管理**：通过 Agent 执行 BigQuery 查询、管理 Cloud SQL 实例、监控 GKE 集群，减少运维人员的手动操作。
- **AI 辅助应用开发**：Agent 调用 Gemini API 生成代码建议，或利用 `Cloud Run Basics` 技能一键部署无服务器应用。
- **多云环境自动化**：配合 Agent 框架，将 Google Cloud 技能与其他厂商的技能无缝组合，实现跨云工作流编排。
- **新员工培训与知识传承**：Agent 根据 Well-Architected 框架技能，为团队新人提供逐步指导，确保遵循安全、成本优化等最佳实践。

## 项目亮点

与同类项目（如各大云厂商的 SDK 封装库或 ChatGPT 插件）相比，Google Agent Skills 的差异化优势明显：

- **官方维护与深度集成**：由 Google 第一方团队开发，与云服务 API 保持同步更新，避免第三方适配滞后问题。
- **专注于 Agent 原生交互**：并非简单的 API 包装器，而是按照 Agent 认知模型设计的“技能”，支持对话式执行、错误重试和上下文记忆。
- **开源协同生态**：基于 Apache-2.0 许可证，社区可自由提交新技能，审核机制确保质量，形成良性循环。
- **轻量级安装与使用**：无需复杂的环境配置，通过 `npx` 一行命令部署，大幅降低入门门槛。

## 相关链接

- [GitHub 仓库](https://github.com/google/skills)
- [Agent Skills 官网](https://agentskills.io/home)
- [技能列表文档](https://github.com/google/skills/tree/main/skills)
