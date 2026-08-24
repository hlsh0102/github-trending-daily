---
tags:
  - trending
  - article
repo: openai/codex
date: 2026-08-24
language: Rust
stars_total: 115623
stars_today: 2715
---
## 项目概述

Codex CLI 是 OpenAI 推出的官方命令行编码代理，以轻量级设计直接在终端环境中运行。它能够理解自然语言指令，并在你的本地开发环境中执行代码编写、文件修改、命令运行等任务，充当开发者身边的智能编程助手。该项目使用 Rust 语言编写，追求高性能与低资源占用，面向希望在不离开终端的情况下获得 AI 辅助编码体验的开发者。与 OpenAI 云端的 Codex Web 不同，Codex CLI 完全运行在本地，能够直接访问你的文件系统与开发工具链，同时将输出流式传输至 OpenAI 后端进行智能处理。

## 核心功能

- **自然语言驱动编码**：通过对话形式描述需求（如“修复登录页面的样式问题”），Codex CLI 自动解析并生成对应的代码修改方案。
- **本地文件系统深度集成**：可以直接读写项目目录中的文件，进行批量重构、缺陷修复或功能实现，无需手动复制粘贴代码。
- **终端命令自动执行**：Agent 能够识别并运行构建、测试、Git 操作等命令行指令，并在出错时自行迭代修正。
- **多平台支持**：提供 macOS、Linux 和 Windows 的安装脚本，并支持 Homebrew、npm 等主流包管理器安装。
- **会话恢复与并行管理**：支持暂停、恢复多个独立会话，方便切换上下文管理不同任务。
- **IDE 与桌面应用桥接**：虽为 CLI 工具，但无缝集成 VS Code、Cursor 等编辑器，并提供可选的桌面应用体验（通过 `codex app` 命令）。

## 技术架构

Codex CLI 采用 Rust 编写核心运行时，以获得出色的启动速度与内存效率。其架构设计遵循以下原则：

- **本地优先**：所有与文件系统、终端交互的操作均在本地执行，确保低延迟与数据隐私控制。
- **API 驱动**：通过 OpenAI 的 Responses API 与后端模型通信，支持模型自由度选择（如 GPT-5-Codex、GPT-5-Codex-Max 等），开发者可通过 `CODEX_MODEL` 环境变量自定义。
- **审批机制**：内置安全审批模式（`--dangerously-byposs-approvals-and-sandbox` 选项可跳过），在默认配置下，高风险操作（如删除文件、执行未知命令）会请求用户确认，降低误操作风险。
- **沙箱隔离**：后台执行的命令运行在临时沙箱环境中，限制对宿主系统的越权访问。
- **跨语言交互**：采用 Rust 的 FFI（外部函数接口）机制实现与系统 shell 的安全交互，确保命令传递的可靠性。

## 安装与使用

**快速安装（macOS / Linux）**：
```shell
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

**快速安装（Windows PowerShell）**：
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

**配置认证**：首次运行时，使用 `codex login` 登录你的 OpenAI 账号（需要订阅 ChatGPT Plus/Pro/Team 或 API 付费账户）。

**基础使用示例**：
1. 在项目根目录启动交互会话：`codex`
2. 输入自然语言指令，例如：“请将 `utils/date.ts` 中的所有时间格式化函数迁移到独立的 `utils/format.ts` 文件中”
3. 审查 Codex 提供的修改计划（默认会显示 diff 预览），确认后应用更改。

**非交互模式**：可通过管道传递指令执行一次性任务：
```shell
echo "Add error handling to the login API" | codex exec
```

## 适用场景

- **日常开发辅助**：快速实现小功能、生成单元测试、修复静态分析工具报告的缺陷，减少重复性劳动。
- **代码重构与迁移**：批量重命名变量、拆分大文件、调整项目结构，利用自然语言描述重构意图，避免手动逐行修改。
- **技术栈学习与探索**：在陌生框架中快速生成示例代码、解释复杂代码片段逻辑，作为交互式学习工具。
- **DevOps 自动化**：编写或修改 Dockerfile、CI/CD 配置文件（如 GitHub Actions），生成部署脚本并验证语法正确性。

## 项目亮点

- **原生终端体验**：无需额外图形界面，轻量启动，完美融入已有的开发工作流。
- **开源透明**：采用 Apache-2.0 许可证，代码完全开源，社区可审查、贡献代码，安全可信。
- **灵活模型选择**：支持在多个 OpenAI 模型间切换，平衡速度与能力。
- **安全默认**：内置审批与沙箱机制，在自动操作的同时保留人为控制权。
- **活跃社区与生态**：GitHub 星标超过 11.5 万，日增数千，拥有丰富的中文社区教程与插件扩展。

## 相关链接

- [GitHub 仓库](https://github.com/openai/codex)
- [OpenAI Codex 官方文档](https://developers.openai.com/codex/)
- [Codex Web（云端版本）](https://chatgpt.com/codex)
