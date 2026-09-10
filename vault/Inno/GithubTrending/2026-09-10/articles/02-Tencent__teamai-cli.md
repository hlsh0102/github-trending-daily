---
tags:
  - trending
  - article
repo: Tencent/teamai-cli
date: 2026-09-10
language: TypeScript
stars_total: 3289
stars_today: 556
---
## 项目概述

TeamAI 是腾讯开源的一个命令行工具，用于在团队内部统一管理 AI 编码代理所需的技能（Skills）、规则（Rules）、MCP 配置以及知识库。它面向的问题十分具体：当团队中的成员分别使用 Claude Code、Codex、CodeBuddy、WorkBuddy、OpenCode、Cursor 等不同 AI 代理时，各自的提示词、规则与工具配置往往散落在本地，难以共享、同步和版本化管理。TeamAI 通过一个受版本控制的 Git 仓库作为团队经验的唯一来源，让不同代理、不同成员之间的 AI 配置保持一致。

目标用户主要是希望推动“团队 AI 原生化”的研发团队，包括需要统一团队 AI 使用规范的团队管理员、希望快速获得团队既有经验的普通开发者，以及单独使用多个 AI 代理的个人用户。

## 核心功能

- **多代理统一管理**：同时支持 Claude Code、Codex、CodeBuddy、WorkBuddy、OpenCode、Cursor 等主流 AI 编码代理，屏蔽不同代理之间配置格式的差异。
- **技能与规则共享**：将团队沉淀的 Skills、Rules、MCP 服务器配置和知识文档集中存放在 Git 仓库中，成员通过初始化命令一键拉取。
- **项目级与用户级安装**：支持将资源安装到项目目录（默认作用域）或用户全局目录，适配不同团队的协作方式。
- **基于 Git 的分发机制**：以 Git 仓库作为后端，天然具备版本历史、权限控制和审计能力，可托管在 GitHub、GitLab、GitCode、CNB、TGit 或私有 Git 服务上。
- **模板化起步**：提供 teamai-hub 组织下的模板仓库，内置生产可用的技能、规则与代码审查代理，团队可直接复制模板快速落地。

## 技术架构

项目使用 TypeScript 编写，以 npm 包形式发布，通过 `npm install -g teamai-cli` 全局安装后提供 CLI 命令。其核心设计思路是“配置即代码”：团队的 AI 能力（技能、规则、MCP 配置、知识）以文件形式存放在 Git 仓库中，由 CLI 负责从仓库拉取并转换、分发到各个 AI 代理所要求的目录与格式。

这种架构将团队经验的沉淀与具体代理解耦，避免了为每个代理单独维护一套配置。借助 Git 本身的分支、权限与历史记录能力，团队可以对 AI 经验的演进进行追踪和回滚。CLI 通过 init 等命令完成仓库绑定与资源安装，并区分项目作用域与用户作用域，从而在多个项目之间灵活复用。

## 安装与使用

全局安装：

```bash
npm install -g teamai-cli
```

团队管理员或单人用户需要先在 Git 托管平台上创建一个存放共享经验的仓库（GitHub、GitLab、GitCode、CNB、TGit 或私有服务均可），并授予团队成员写权限，然后执行：

```bash
teamai init https://github.com/yourorg/yourrepo
```

如果团队还没有现成的仓库，可以从 [teamai-hub](https://github.com/teamai-hub) 组织下的模板仓库入手，点击 “Use this template” 生成自己的仓库后再执行初始化。

团队成员则根据资源希望安装的位置选择作用域：默认使用项目级初始化，将资源安装到当前项目目录下；如需在多个项目间共享，也可选择用户级安装。初始化完成后，团队定义的技能、规则、MCP 与知识即可在受支持的 AI 代理中生效。

## 适用场景

- **多代理混合团队**：团队成员使用不同的 AI 编码代理，需要一套共享的规则与技能配置，避免各自为战。
- **团队经验沉淀**：将资深成员总结的提示词、代码审查规则、最佳实践固化为仓库中的技能，供新成员直接复用。
- **规范统一与合规**：在受管控的私有 Git 服务上集中维护 AI 配置，便于审计、权限管理与版本追溯。
- **个人多机多项目同步**：单个开发者在多台设备或多个项目间保持一致的个人 AI 配置。

## 项目亮点

与针对单一 AI 代理的配置管理工具不同，TeamAI 的差异化在于跨代理能力：它把 Claude Code、Codex、CodeBuddy、Cursor 等异构代理统一到同一套配置源之下，这是同类工具较少覆盖的场景。同时，选择以 Git 仓库为分发载体而非自建服务，使团队无需引入额外的中心化系统，即可获得版本控制、权限模型和历史记录。

此外，模板仓库的提供降低了启动成本，团队不必从零编写技能与规则即可获得一套可用的基础配置。项目目前在 GitHub 上已获得三千余颗星，并在持续接受社区贡献。

## 相关链接

- [GitHub 仓库](https://github.com/Tencent/teamai-cli)
- [npm 包](https://www.npmjs.com/package/teamai-cli)
- [模板仓库组织 teamai-hub](https://github.com/teamai-hub)
- [贡献者列表](https://github.com/Tencent/teamai-cli/graphs/contributors)
