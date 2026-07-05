---
tags:
  - trending
  - article
repo: openai/codex-plugin-cc
date: 2026-07-05
language: JavaScript
stars_total: 24763
stars_today: 718
---
## 项目概述

Codex for Claude Code 是一个将 OpenAI Codex 与 Anthropic 的 Claude Code 深度集成的插件项目。它解决了开发者在已有 Claude Code 工作流中需要同时利用 Codex 进行代码审查和任务委派的痛点。目标用户是那些已经习惯使用 Claude Code 进行开发、但又希望在不切换工具的前提下获得 Codex 强大能力的工程师和团队。通过这个插件，用户可以在 Claude Code 界面内直接调用 Codex 的各种功能，实现无缝协作。

## 核心功能

- **代码审查（`/codex:review`）**：对指定代码进行只读审查，提供专业建议和潜在问题分析。
- **对抗性审查（`/codex:adversarial-review`）**：进行可引导的挑战性审查，主动寻找代码中的漏洞和缺陷。
- **任务委派（`/codex:rescue`）**：将复杂或耗时任务移交给 Codex 在后台异步处理。
- **会话转移（`/codex:transfer`）**：将当前工作会话无缝移交给 Codex 继续执行。
- **后台任务管理**：包括查询状态（`/codex:status`）、获取结果（`/codex:result`）和取消任务（`/codex:cancel`）等完整生命周期管理。

## 技术架构

项目采用插件架构设计，通过 Claude Code 的插件系统进行集成。核心机制是定义一组自定义斜杠命令（slash commands），这些命令在 Claude Code 环境中由 JavaScript 实现驱动。插件内部通过 Node.js 18.18+ 运行时调用本地安装的 Codex CLI 工具，实现与 OpenAI Codex 的通信。设计上强调低侵入性——仅作为对现有工作流的扩展，而非替代方案。插件会将 Codex 作为子代理（sub-agent）注册到 Claude Code 的代理系统中，使得用户可以在 `/agents` 视图中直接看到 `codex:codex-rescue` 等子代理条目。

## 安装与使用

安装过程分为三个步骤：

1. 在 Claude Code 中添加插件市场：
```bash
/plugin marketplace add openai/codex-plugin-cc
```

2. 安装插件：
```bash
/plugin install codex@openai-codex
```

3. 加载插件并运行初始化设置：
```bash
/reload-plugins
/codex:setup
```

`/codex:setup` 命令会自动检测当前环境是否已安装 Codex，如果未安装且系统中有 npm，它会引导安装 `@openai/codex`。你也可以手动安装：
```bash
npm install -g @openai/codex
```

如果 Codex 已安装但未登录，执行：
```bash
!codex login
```

安装完成后，即可直接使用 `/codex:review` 等命令完成代码审查或任务委派。

## 适用场景

- **代码审查工作流**：开发者在 Claude Code 中完成编码后，直接调用 Codex 进行多角度代码审查，无需切换到其他工具。
- **复杂任务分解**：遇到需要大量上下文分析或耗时较长的任务时，使用 `/codex:rescue` 将任务交给后台处理，自身可继续其他工作。
- **团队协作场景**：通过会话转移功能，在团队成员之间或与 AI 助手之间灵活切换工作上下文，提升协作效率。
- **安全审计**：利用对抗性审查模式，在开发阶段主动发现安全漏洞和逻辑缺陷，增强代码质量。

## 项目亮点

与独立的 Codex 使用方式相比，该插件的核心优势在于**零切换集成**。开发者无需离开 Claude Code 的交互环境就能调用 Codex 的全部能力，大幅减少了上下文切换的成本。此外，插件提供的多种命令覆盖了从实时审查到后台任务管理的完整使用场景，特别是对抗性审查和安全引导功能，为代码质量保障提供了独特的增值。项目遵循 Apache-2.0 开源协议，对开发者友好，且支持 ChatGPT 订阅（包括免费用户）和 OpenAI API 密钥两种接入方式，降低了使用门槛。

## 相关链接

- [GitHub 仓库](https://github.com/openai/codex-plugin-cc)
- [了解更多 Codex 定价信息](https://developers.openai.com/codex/pricing)
