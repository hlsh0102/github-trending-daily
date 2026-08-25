---
tags:
  - trending
  - article
repo: anthropics/claude-plugins-community
date: 2026-08-25
language: Python
stars_total: 1401
stars_today: 489
---
## 项目概述

Claude Plugins — Community 是 Anthropic 官方维护的社区插件市场仓库，为 Claude Cowork 和 Claude Code 提供由社区贡献的插件集合。该仓库以降级只读镜像的形式存在，其中 `.claude-plugin/marketplace.json` 文件记录了所有可供安装的社区插件列表，并通过每日夜间同步机制从 Anthropic 内部审核管线更新。

这个项目解决了 Claude 生态中插件分发和发现的核心问题：社区开发者需要安全、规范的渠道发布自己的插件，而用户需要一个可信赖的插件源来扩展 Claude 的能力。该仓库面向两类用户：一是希望通过插件扩展 Claude 功能的终端用户，二是希望将自研插件分享给更广泛受众的开发者。

## 核心功能

- **插件市场索引**：集中维护社区插件的元数据与安装信息，用户可通过标准命令直接安装
- **自动化安全审核**：所有插件在收录前均经过自动化安全扫描，确保代码质量与安全性
- **夜间同步更新**：仓库内容每晚自动从 Anthropic 内部审核管线同步，保证插件列表始终最新
- **跨产品支持**：同时兼容 Claude Cowork 与 Claude Code 两大产品线，提供统一安装体验
- **提交入口统一**：插件提交通过官方入口完成，避免无效 PR 干扰仓库维护
- **分类导航**：与官方插件仓库和知识工作插件仓库形成互补，方便用户按需选择

## 技术架构

该项目采用 Python 语言构建，核心是一个符合 Claude 插件市场规范的 JSON 索引文件（`marketplace.json`）。架构设计遵循"单一事实来源"原则：Anthropic 内部审核管线是唯一的数据源，公共仓库只是其定期镜像。

同步机制采用定时任务驱动，每天夜间将内部审核结果推送到 GitHub 仓库。这种设计有效避免了社区 PR 直接修改导致的供应链风险，确保所有插件都经过统一的安全审查流程。仓库中的 `marketplace.json` 遵循 Claude 插件协议，使得 Claude Cowork 和 Claude Code 客户端能够通过标准协议识别并安装插件。

技术栈精简，不依赖复杂的构建系统，GitHub Actions 即可完成同步任务。这种极简架构降低了维护成本，同时保证了系统的可靠性和可审计性。

## 安装与使用

### 在 Claude Code 中安装插件

```bash
# 1. 添加社区插件市场
claude plugin marketplace add anthropics/claude-plugins-community

# 2. 安装具体插件（将 <plugin-name> 替换为实际插件名）
claude plugin install <plugin-name>@claude-community
```

### 在 Claude Cowork 中使用插件

直接访问 [claude.com/plugins](https://claude.com/plugins/) 页面浏览并安装社区插件，无需命令行操作。

### 提交你自己的插件

访问 [clau.de/plugin-directory-submission](https://clau.de/plugin-directory-submission) 提交插件审核。值得注意的是，直接向本仓库发起 Pull Request 会被自动关闭，所有变更都源自内部审核管线，社区贡献者不应尝试绕过官方提交流程。

## 适用场景

- **功能扩展**：为 Claude Code 增加自定义工具、命令或工作流，满足特定业务场景需求
- **团队协作**：在团队内部统一安装经过审核的插件，确保开发环境一致性与安全性
- **生态分发**：开发者将自研插件通过官方审核后，借助社区市场触达更广泛的用户群体
- **能力发现**：用户浏览社区插件列表，发现其他开发者创造的有趣用途，激发新的使用思路

## 项目亮点

与其他插件分发机制相比，该项目最突出的优势在于 **安全与信任**。由于所有插件都经过 Anthropic 官方的自动化安全扫描和人工审核，用户在安装插件时无需担心恶意代码风险，这是独立插件仓库难以提供的保障。

其次，**同步机制的先进性**体现在其严格的写入控制上。通过将仓库设为只读镜像并关闭 PR 功能，Anthropic 从根源上杜绝了供应链攻击的可能性。这种"官方审核 + 公开镜像"的模式既保证了代码质量，又保持了社区开放性。

此外，**跨产品兼容性**让开发者只需一次提交即可同时覆盖 Claude Cowork 与 Claude Code 两大平台，显著降低了分发成本。配合官方插件仓库与知识工作插件仓库的分类，用户可以快速找到最适合自己需求的工具集。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/claude-plugins-community)
- [Claude Cowork 产品页面](https://claude.com/product/cowork)
- [Claude Code 产品页面](https://claude.com/product/claude-code)
- [插件提交入口](https://clau.de/plugin-directory-submission)
- [官方插件仓库](https://github.com/anthropics/claude-plugins-official)
- [知识工作插件仓库](https://github.com/anthropics/knowledge-work-plugins)
