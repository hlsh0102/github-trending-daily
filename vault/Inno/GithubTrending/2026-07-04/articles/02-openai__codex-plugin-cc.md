---
tags:
  - trending
  - article
repo: openai/codex-plugin-cc
date: 2026-07-04
language: JavaScript
stars_total: 23378
stars_today: 634
---
## 项目概述

Codex plugin for Claude Code 是一个将 OpenAI Codex 直接集成到 Claude Code 工作流中的插件项目。它由 OpenAI 官方维护，旨在让 Claude Code 用户能够便捷地调用 Codex 的能力，包括代码审查、任务委派等。目标用户是已经使用 Claude Code 进行开发、但希望结合 Codex 的审查和自动化能力来提升效率的开发者。通过简单的斜杠命令，用户无需离开熟悉的 Claude Code 界面，即可启动 Codex 的代码审查或后台任务管理。

## 核心功能

- **`/codex:review`**：执行标准的只读代码审查，快速获取 Codex 对代码的反馈。
- **`/codex:adversarial-review`**：进行可引导的挑战性审查，模拟对抗性场景，深入检查代码的潜在缺陷。
- **`/codex:rescue`**：将当前任务委派给 Codex，允许将复杂或耗时的操作交由 Codex 在后台处理。
- **`/codex:transfer`**：将会话或任务移交到 Codex，实现工作流的无缝切换。
- **`/codex:status` 和 `/codex:result`**：查询后台 Codex 任务的状态和获取最终结果。
- **`/codex:cancel`**：取消正在运行的后台 Codex 任务。

## 技术架构

该项目基于 JavaScript 构建，作为 Claude Code 的插件运行。其核心设计是利用 Claude Code 的插件系统（通过 `/plugin` 命令管理），在 Claude Code 环境中注册一系列自定义的斜杠命令和一个名为 `codex:codex-rescue` 的子代理。这些命令和代理通过调用本地安装的 Codex CLI 工具（`@openai/codex`）与 OpenAI 的 Codex 服务进行交互。插件本身不直接处理复杂的业务逻辑，而是充当桥梁，将用户在 Claude Code 中的请求转换为 Codex 命令，并将结果返回给用户。这种设计保持了架构的简洁性，同时充分利用了 Codex 和 Claude Code 各自的优势能力。

## 安装与使用

**前提条件**：需要有效的 ChatGPT 订阅（包括免费版）或 OpenAI API 密钥，以及 Node.js 18.18 或更高版本。

**安装步骤**：

1. 在 Claude Code 中，先添加插件市场：
   ```bash
   /plugin marketplace add openai/codex-plugin-cc
   ```

2. 安装插件：
   ```bash
   /plugin install codex@openai-codex
   ```

3. 重新加载插件：
   ```bash
   /reload-plugins
   ```

4. 运行设置命令以验证环境：
   ```bash
   /codex:setup
   ```
   如果系统检测到 Codex 未安装但 npm 可用，它会提示自动安装。也可以手动安装 Codex：
   ```bash
   npm install -g @openai/codex
   ```

5. 如果 Codex 已安装但未登录，运行登录命令：
   ```bash
   !codex login
   ```

安装成功后，可以看到注册的斜杠命令列表以及子代理 `codex:codex-rescue`。

## 适用场景

- **代码审查流程优化**：开发者在提交 PR 或合并代码前，可以通过 `/codex:review` 或 `/codex:adversarial-review` 快速获得 Codex 的专业审查意见，无需切换到其他工具。
- **异步任务委派**：在开发过程中，遇到需要较长时间处理的分析任务（例如重构建议、日志分析），可以使用 `/codex:rescue` 将任务交给 Codex 后台执行，随后通过 `/codex:status` 和 `/codex:result` 获取结果。
- **多工具协同开发**：开发者习惯使用 Claude Code 进行日常编码和对话式代码理解，但同时需要 Codex 的深度审查能力时，该插件提供了无缝的集成体验，避免了在多个 CLI 工具之间来回切换。

## 项目亮点

- **官方维护与深度集成**：由 OpenAI 官方开发，与 Codex 和 Claude Code 的兼容性有保障，且持续更新。
- **零额外配置**：安装后即可通过直观的斜杠命令使用，无需学习新的 CLI 语法或配置复杂的集成。
- **后台任务管理**：`/codex:rescue` 和 `/codex:cancel` 等命令让开发者能够将任务异步化，在等待 Codex 处理的同时继续在 Claude Code 中工作，提升效率。
- **丰富的工作流支持**：不仅支持常见的代码审查，还支持会话转移、任务状态跟踪等高级功能，满足从简单审查到复杂任务委派的多种需求。

## 相关链接

- [GitHub 仓库](https://github.com/openai/codex-plugin-cc)
- [OpenAI Codex 定价](https://developers.openai.com/codex/pricing)
