---
tags:
  - trending
  - article
repo: anthropics/claude-plugins-community
date: 2026-08-26
language: Python
stars_total: 1821
stars_today: 351
---
## 项目概述

`anthropics/claude-plugins-community` 是 Anthropic 官方维护的社区插件市场镜像仓库，为 Claude Cowork 和 Claude Code 提供社区贡献的插件分发服务。该仓库本质上是社区插件目录的**只读镜像**，其中的 `.claude-plugin/marketplace.json` 文件列出了所有可安装的社区插件，并每晚与 Anthropic 内部的审核流水线自动同步。

这一项目的核心价值在于为 Claude 用户建立一个安全、有序的插件分发通道。所有插件均需通过 [claude.ai](https://clau.de/plugin-directory-submission) 提交，经过自动化安全扫描并获准后方可进入此镜像。对于希望扩展 Claude 工具链能力的开发者、需要复用社区最佳实践的技术团队，以及想贡献自定义插件的创作者而言，这是官方认可的插件获取与分发渠道。

## 核心功能

- **插件市场镜像**：提供权威的社区插件目录，用户可通过标准命令直接安装，无需手动搜索或验证插件来源。
- **自动化安全把关**：所有插件在进入镜像前均经过自动化安全扫描和审核，降低了恶意或低质量插件的风险。
- **只读同步机制**：仓库内容由 Anthropic 内部审核流水线每晚同步，确保插件列表实时反映最新通过审核的版本。
- **多客户端支持**：同时适配 Claude Cowork 和 Claude Code 两大产品，用户可在不同工作环境中使用一致的插件管理方式。
- **简化提交流程**：插件作者通过单一入口提交申请，无需处理复杂的 Pull Request 流程，审核通过后自动进入市场。
- **开放协作生态**：与官方插件仓库、知识工作插件仓库形成互补，覆盖从通用型到领域专用的各类插件需求。

## 技术架构

该仓库采用轻量级设计，核心是一个符合 Claude 插件市场规范的 `marketplace.json` 清单文件。该文件遵循 Claude 插件标准的 JSON 结构，记录了每个插件的名称、版本、仓库地址、描述及校验信息等元数据。

从架构层面看，本项目体现了"审核管道 + 只读分发"的典型模式。Anthropic 内部维护着插件提交、安全扫描、人工审核的完整流水线，审核通过后的成果物通过自动化任务同步至 GitHub 仓库。由于仓库是只读的，社区用户无法直接修改插件列表，这从机制上避免了恶意篡改或未经验证的插件进入分发渠道。

对于客户端（Claude Code 等）而言，其通过 `claude plugin marketplace add` 命令将本仓库注册为插件源，随后按需拉取插件清单并安装。这种设计将"审核"与"分发"解耦，既保证了分发效率，又确保了安全合规。

## 安装与使用

**Claude Code 用户**使用以下命令添加社区插件市场：

```bash
claude plugin marketplace add anthropics/claude-plugins-community
```

添加后即可安装市场中的任意插件：

```bash
claude plugin install <plugin-name>@claude-community
```

**Claude Cowork 用户**无需命令行操作，直接访问 [claude.com/plugins](https://claude.com/plugins/) 即可浏览和安装社区插件。

**插件作者**如需提交新插件，请前往 [clau.de/plugin-directory-submission](https://clau.de/plugin-directory-submission) 填写提交表单。注意，直接对该仓库发起 Pull Request 会被系统自动关闭，所有变更均须通过内部审核管道流转。

## 适用场景

- **个人开发者扩展工具链**：在 Claude Code 中快速安装社区插件，为编码、调试、文档生成等工作流添加实用功能。
- **团队标准化插件管理**：技术团队可基于该市场统一安装经过审核的插件，避免成员各自寻找非官方来源带来的安全隐患。
- **插件开发者分发作品**：希望将自己的 Claude 插件分享给更广泛用户群的开发者，可通过提交入口进入官方分发渠道。
- **研究与学习参考**：前端开发者可浏览该仓库的插件清单，了解 Claude 插件生态的现状、技术规范与最佳实践。

## 项目亮点

- **官方背书的安全保障**：与第三方插件聚合站不同，本仓库由 Anthropic 直接维护，所有插件经过自动化安全扫描和人工审核，可信度显著更高。
- **零维护的消费体验**：作为用户仅需两条命令即可完成市场接入与插件安装，且市场内容自动同步刷新，无需手动跟踪更新。
- **严格的生态治理**：通过"只读镜像 + 单一提交入口"的设计，有效避免了开源仓库常见的质量良莠不齐、维护分散等问题，营造了可持续发展的插件生态。
- **低门槛的参与机制**：插件作者无需了解 GitHub 协作流程，通过网页表单即可提交作品，降低了贡献门槛，加速了生态扩张。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/claude-plugins-community)
- [Claude Cowork 产品页](https://claude.com/product/cowork)
- [Claude Code 产品页](https://claude.com/product/claude-code)
- [插件提交入口](https://clau.de/plugin-directory-submission)
- [官方插件仓库](https://github.com/anthropics/claude-plugins-official)
- [知识工作插件仓库](https://github.com/anthropics/knowledge-work-plugins)
