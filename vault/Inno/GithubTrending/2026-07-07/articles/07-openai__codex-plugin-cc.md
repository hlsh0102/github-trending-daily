---
tags:
  - trending
  - article
repo: openai/codex-plugin-cc
date: 2026-07-07
language: JavaScript
stars_total: 26402
stars_today: 906
---
## 项目概述

Codex Plugin for Claude Code 是一个专为 Claude Code 用户设计的插件，它让你能够在 Claude Code 的工作流中直接调用 OpenAI Codex 进行代码审查或任务委派。该项目解决了跨 AI 工具协作的痛点：许多开发者希望同时利用 Claude Code 的交互式开发体验和 Codex 的深度代码分析能力，但不得不在两个工具之间来回切换。通过这个插件，你可以直接在 Claude Code 中使用 `slash commands` 触发 Codex 的各项功能，无需离开当前会话。目标用户是正在使用 Claude Code 且需要 Codex 高级代码审查或异步任务执行能力的开发者。

## 核心功能

- **代码审查**：使用 `/codex:review` 命令启动只读的 Codex 代码审查，快速获得代码质量、安全性和最佳实践方面的反馈。
- **对抗性审查**：通过 `/codex:adversarial-review` 启动可引导的挑战式审查，Codex 会主动寻找代码中的潜在问题或漏洞，模拟攻击者视角。
- **任务委派**：使用 `/codex:rescue` 将复杂或耗时的任务委托给 Codex 在后台执行，释放 Claude Code 的前端资源。
- **会话转移**：使用 `/codex:transfer` 将当前对话或工作上下文无缝移交给 Codex，实现协作模式切换。
- **后台作业管理**：通过 `/codex:status` 查看任务状态、`/codex:result` 获取结果、`/codex:cancel` 取消正在运行的后台任务。

## 技术架构

该项目本质上是一个 Claude Code 插件，使用 JavaScript 编写，遵循 Claude Code 的插件开发规范。其核心设计思路是在 Claude Code 的事件循环中注入自定义的 `slash commands`，这些命令通过系统调用或与本地安装的 Codex CLI 交互来执行相应操作。技术要点包括：

- **Node.js 18.18+**：所有命令运行在 Node.js 环境中，利用其子进程管理能力调用 Codex。
- **外部依赖**：依赖于本地安装的 `@openai/codex` npm 包，插件本身不包含 Codex 核心逻辑，而是作为桥接层。
- **会话与状态管理**：通过文件系统或临时存储管理后台任务的状态，确保 `/codex:status` 和 `/codex:result` 能准确报告执行进度。
- **可扩展命令架构**：插件定义了统一的命令注册和解析机制，便于后续添加更多与 Codex 交互的指令。

## 安装与使用

**安装步骤：**

1. 确保已安装 Node.js 18.18 或更高版本。
2. 在 Claude Code 中添加插件市场并安装插件：
   ```
   /plugin marketplace add openai/codex-plugin-cc
   /plugin install codex@openai-codex
   /reload-plugins
   ```
3. 运行初始化命令，检查 Codex 是否就绪：
   ```
   /codex:setup
   ```
4. 如果提示 Codex 缺失，可自动安装或手动执行：`npm install -g @openai/codex`
5. 若需要登录，运行：`!codex login`

**最小可用示例：**

完成安装后，你可以在 Claude Code 中直接运行：

```
/codex:review --file src/main.js
```

该命令会要求 Codex 对指定文件进行只读审查，并将结果返回到当前会话。你也可以使用类似 `npm install` 这样的自然语言指令，结合插件自动识别逻辑来触发 Codex 任务。

## 适用场景

- **代码审查工作流**：团队在 Claude Code 中协作开发时，快速调用 Codex 进行独立的代码质量审查，避免人为盲点。
- **复杂任务并行处理**：当涉及大量文件的重构或批量修复时，使用 `/codex:rescue` 在后台运行 Codex，同时继续在 Claude Code 中进行其他开发工作。
- **安全审计**：利用对抗性审查模式，让 Codex 从安全角度审视代码，发现潜在的 SQL 注入、XSS 或其他漏洞。
- **培训与辅助学习**：新手开发者可以通过 `/codex:review` 获得代码改进建议，学习最佳实践。

## 项目亮点

- **零切换成本**：无需离开 Claude Code 即可使用 Codex 的所有核心能力，极大提升开发效率。
- **异步执行**：支持后台任务，避免阻塞当前工作流，适合需要长时间分析的大型代码库。
- **灵活的会话管理**：从简单的代码审查到完整的任务委派和会话转移，提供了多种协作模式。
- **开源透明**：采用 Apache-2.0 许可证，代码完全开放，允许开发者根据需求自定义和扩展。

## 相关链接

- [GitHub 仓库](https://github.com/openai/codex-plugin-cc)
- [Codex 定价说明](https://developers.openai.com/codex/pricing)
