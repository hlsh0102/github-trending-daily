---
tags:
  - trending
  - article
repo: openai/codex-plugin-cc
date: 2026-07-06
language: JavaScript
stars_total: 25754
stars_today: 1532
---
## 项目概述

Codex Plugin for Claude Code 是一个由 OpenAI 官方开发的插件，旨在让 Claude Code 用户能够直接在现有工作流中调用 Codex 进行代码审查或任务委托。该项目的核心价值在于打通了 Claude Code 与 Codex 之间的壁垒，让用户无需切换工具即可享受两种 AI 代码助手的协同能力。目标用户是已经习惯使用 Claude Code 进行编码和项目管理，同时希望利用 Codex 在代码评审、任务分包等方面的专项优势的开发者。

## 核心功能

- **代码审查**：提供 `/codex:review` 命令执行常规的只读代码审查，以及 `/codex:adversarial-review` 命令进行可引导性的挑战审查，后者允许开发者对审查方向进行干预和控制。
- **任务委托与工作交接**：通过 `/codex:rescue` 和 `/codex:transfer` 命令，可以将复杂任务或正在进行的工作委托给 Codex，实现跨工具的工作流接力。
- **后台任务管理**：支持通过 `/codex:status` 查询任务执行状态，`/codex:result` 获取最终结果，以及 `/codex:cancel` 取消正在运行的后台作业。
- **一站式环境配置**：提供 `/codex:setup` 命令自动检测 Codex 安装情况，并在必要时通过 npm 完成安装，简化用户的初始配置流程。
- **子代理集成**：安装后，`codex:codex-rescue` 子代理会自动注册到 Claude Code 的代理列表中，方便用户直接调用。

## 技术架构

该插件采用标准 Claude Code 插件架构，基于 JavaScript 开发，利用 Claude Code 的插件系统提供的钩子机制与 Codex 的命令行接口进行交互。其核心设计思路可以概括为“桥接模式”：插件本身不实现 Codex 的代码审查或任务调度逻辑，而是通过系统调用触发本地的 Codex CLI 进程，并将标准输入输出流映射为 Claude Code 中的对话式交互。这种设计使得插件轻量化且易于维护，同时也保持了对 Codex 最新功能的兼容性。

在部署方面，插件依赖于 Node.js 18.18 或更高版本运行环境，通过 npm 包管理器安装 Codex 本体。认证逻辑由 Codex 自身负责，用户在安装完成后需通过 `!codex login` 命令完成登录。整个架构确保了 Claude Code 终端中的每一次斜杠命令调用都能被透明地转换为对本地 Codex 实例的 API 调用，且不引入额外的中间服务。

## 安装与使用

安装过程分为三个步骤：

1. **添加插件市场**：
   ```bash
   /plugin marketplace add openai/codex-plugin-cc
   ```

2. **安装插件**：
   ```bash
   /plugin install codex@openai-codex
   ```

3. **重载插件并配置**：
   ```bash
   /reload-plugins
   /codex:setup
   ```

`/codex:setup` 命令会自动检测 Codex 是否可用，若检测到未安装且系统中有 npm，则会提示用户安装。用户也可以手动安装 Codex：

```bash
npm install -g @openai/codex
```

然后执行登录：

```bash
!codex login
```

完成上述步骤后，用户便可以在 Claude Code 中输入 `/codex:review` 等命令来使用 Codex 的功能。

## 适用场景

- **代码审查流水线**：开发团队在 Claude Code 中完成代码修改后，可直接发起 `/codex:review` 命令进行自动化审查，无需跳出当前编辑器窗口。
- **复杂任务的委托执行**：当 Claude Code 遇到超出其能力范围的特定任务（如需要专业算法优化），可通过 `/codex:rescue` 将任务转交给 Codex，之后通过 `/codex:status` 和 `/codex:result` 获取处理结果。
- **多工具协作开发**：在需要频繁切换 AI 助手的工作环境中，该插件为同时使用 Claude Code 和 Codex 的用户提供了统一的操作入口，缩短了上下文切换的时间成本。

## 项目亮点

与同类工具相比，该项目最显著的差异化优势在于其原生集成深度。它不是简单的“将代码粘贴到另一个窗口”，而是通过 Claude Code 的插件系统实现了会话级别的命令映射，允许用户在同一个终端环境中无缝切换两个不同的 AI 模型。此外，插件内置的任务生命周期管理（提交、查询、取消、取回结果）解决了跨工具协作中的常见痛点——用户不需要手动追踪 Codex 的后台作业，所有状态都可以在 Claude Code 中直接查看。

另一个突出点是 **adversarial review 模式**，该模式允许开发者主动引导审查方向，而非常规的被动接收反馈。这使得 Codex 不但可以作为代码质量的检查者，还能作为代码编写的协作伙伴。

## 相关链接

- [GitHub 仓库](https://github.com/openai/codex-plugin-cc)
- [Codex 定价信息](https://developers.openai.com/codex/pricing)
