---
tags:
  - trending
  - article
repo: Tencent/teamai-cli
date: 2026-09-11
language: TypeScript
stars_total: 3991
stars_today: 841
---
## 项目概述

TeamAI 是由腾讯开源的一款命令行工具，托管于 GitHub 的 Tencent/teamai-cli 仓库。项目的核心目标是帮助研发团队将日常使用的各类 AI 编程助手统一管理起来，实现 "Make Every Team AI Native" 的愿景。

随着 Claude Code、Codex、CodeBuddy、WorkBuddy、OpenCode、Cursor 等 AI Agent 在团队中的普及，一个现实问题逐渐凸显：每个成员各自维护提示词、规则、技能和 MCP 配置，经验难以沉淀，配置无法复用，新人上手成本高。TeamAI 通过一个集中的仓库来管理团队的技能（Skills）、规则（Rules）、MCP 配置以及知识库，并把这些资源同步到上述各类 AI Agent 中，从而让整个团队共享一套经过验证的 AI 使用方式。其目标用户主要为研发团队、团队技术负责人，以及希望统一 AI 编程体验的个人开发者。

## 核心功能

- **跨 Agent 资源分发**：将团队定义好的技能、规则、MCP 配置和知识同步到 Claude Code、Codex、CodeBuddy、WorkBuddy、OpenCode、Cursor 等主流 AI Agent，避免逐一手工配置。
- **共享经验仓库**：借助 Git 托管平台（GitHub、GitLab、GitCode、CNB、TGit 或私有 Git 服务）作为团队知识的载体，团队成员通过拉取获得统一更新。
- **项目级与用户级安装**：通过 `teamai init` 支持将资源安装到项目目录（project scope）或用户环境，满足不同粒度的使用需求。
- **模板化起步**：官方提供 teamai-hub 组织下的模板仓库，预置了生产级别的技能、规则与审查 Agent，可直接 "Use this template" 后初始化使用。
- **团队权限协作**：通过给团队成员授予仓库写权限，让优秀的提示词与经验可以被持续贡献和迭代。

## 技术架构

TeamAI 使用 TypeScript 编写，通过 npm 以全局命令行工具的形式发布（`teamai-cli`），保证跨平台可用。其整体设计围绕“以 Git 仓库为单一事实源（Single Source of Truth）”展开：团队将技能、规则、MCP 配置和知识以约定的目录结构存放在仓库中，CLI 负责解析这些内容，并按照目标 Agent 的规范进行转换与安装。

这种设计把版本管理、权限控制和协作流程都交给成熟的 Git 生态承载，CLI 本身只需专注资源分发与适配。项目内置了持续集成（通过 GitHub Actions 中的 ci.yml 工作流），并借助 npm 完成分发，降低了安装门槛。仓库同时提供中英文文档，便于不同背景的团队使用。

## 安装与使用

基本安装通过 npm 全局完成：

```bash
npm install -g teamai-cli
```

对于团队管理员或独立使用者，先在一个 Git 托管平台（如 GitHub、GitLab、GitCode、CNB、TGit 或私有 Git 服务）上创建一个用于共享经验的仓库，并为团队成员授予写权限，然后执行：

```bash
teamai init https://github.com/yourorg/yourrepo
```

如果尚未准备好团队仓库，可以从 teamai-hub 组织下的模板仓库入手，点击 "Use this template" 生成自己的仓库后再执行 `teamai init`。

对于团队成员，根据希望安装资源的位置选择初始化方式。默认的项目级初始化会将资源安装到当前项目目录下：

```bash
teamai init
```

以上为最小可用路径，实际参数与更多选项可参考仓库文档。

## 适用场景

- **研发团队统一 AI 编程规范**：将团队的编码规范、审查规则和常用提示词集中管理，并同步到所有成员使用的 AI Agent。
- **规模化推广 AI 编程助手**：在企业内部推行 Claude Code、Cursor 等工具时，通过中心化仓库降低配置和培训成本。
- **新成员快速上手**：新人加入后只需执行初始化命令，即可获得与团队一致的技能与规则环境。
- **跨 Agent 混合使用环境**：团队成员使用不同 AI 工具时，仍能共享同一套知识与实践。

## 项目亮点

与单一 Agent 内置的配置管理相比，TeamAI 的差异化优势在于其**跨 Agent 的中立性与统一性**——它并不绑定某一种工具，而是把团队的 AI 资产抽象出来，再分发到多种主流 Agent 中。同时，它**以 Git 仓库为协作基础**，让提示词、技能和规则像代码一样被版本化、评审和复用。加之腾讯开源背景与活跃的社区贡献（仓库星标数较高、有持续的贡献者），项目在工程化和可维护性方面具备一定基础。

## 相关链接

- [GitHub 仓库](https://github.com/Tencent/teamai-cli)
- [npm 包](https://www.npmjs.com/package/teamai-cli)
- [模板仓库团队 teamai-hub](https://github.com/teamai-hub)
