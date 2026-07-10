---
tags:
  - trending
  - article
repo: wonderwhy-er/DesktopCommanderMCP
date: 2026-07-10
language: TypeScript
stars_total: 6617
stars_today: 185
---
## 项目概述

Desktop Commander MCP 是一个为 Claude 设计的 MCP 服务器，它赋予 AI 强大的终端控制、文件系统搜索以及差异化文件编辑能力。该项目解决了传统 AI 编辑器在代码和文本操作上的局限性，让用户能够通过自然语言与计算机进行深度交互。目标用户包括开发者、系统管理员以及任何希望在 AI 辅助下更高效地处理文件、运行命令和自动化任务的用户。

## 核心功能

- **终端控制**：允许 AI 直接与终端交互，执行命令、启动进程、管理后台任务，实现真正的命令行自动化。
- **文件系统搜索**：支持在指定目录下进行快速、灵活的文件和文本内容搜索，帮助 AI 理解项目结构。
- **差异化文件编辑**：提供智能的文件编辑能力，可对文件进行精确的增量修改，而非简单覆盖，减少出错风险。
- **跨平台支持**：兼容 macOS 和 Windows 系统，确保在主流开发环境中均可稳定运行。
- **自动化任务编排**：支持通过终端脚本或 MCP 工具组合，实现从文件操作到流程运行的全链路自动化。
- **安全与权限控制**：提供可配置的终端执行策略和文件访问白名单，确保 AI 操作在可控范围内。

## 技术架构

项目采用 TypeScript 编写，基于 MCP（Model Context Protocol）协议实现与 Claude 等 AI 模型的通信。核心架构围绕“工具”和“资源”两个概念展开：

- **工具层**：将终端命令、文件操作、搜索等能力封装为 MCP 工具，AI 可像调用函数一样直接使用。
- **资源层**：提供文件系统资源访问接口，AI 能够读取和监控文件变化。
- **传输层**：使用标准输入输出（stdio）作为通信协议，轻量且高效，无需额外网络开销。

设计上强调模块化和可扩展性，每个功能模块独立解耦，便于用户根据需求自定义或扩展。同时，通过权限控制机制确保 AI 操作的安全边界，防止误操作或越权访问。

## 安装与使用

**环境要求**：Node.js 16+、npm/yarn、Claude Desktop 或其他支持 MCP 的客户端。

**安装步骤**：

1. 使用 npm 全局安装 Desktop Commander MCP：
   ```bash
   npm install -g @wonderwhy-er/desktop-commander
   ```

2. 在 Claude Desktop 中配置 MCP 服务器。编辑 `claude_desktop_config.json` 文件（通常位于 `~/.config/Claude/`），添加以下内容：
   ```json
   {
     "mcpServers": {
       "desktop-commander": {
         "command": "npx",
         "args": ["-y", "@wonderwhy-er/desktop-commander"]
       }
     }
   }
   ```

3. 重启 Claude Desktop，即可在对话中使用相关功能。

**最小使用示例**：

- 在 Claude 中输入：“列出当前目录下的所有文件”。
- 或：“创建一个名为 test.txt 的文件，内容为‘Hello World’”。
- 或：“在终端中运行 npm run build 并捕获输出”。

## 适用场景

- **开发环境管理**：AI 可协助创建、编辑项目文件，运行构建命令，自动修复编译错误。
- **自动化运维**：通过终端命令和脚本，AI 能执行批量文件处理、日志分析、系统监控等任务。
- **数据处理与清洗**：利用文件搜索和编辑功能，AI 可快速定位并修改批量数据文件。
- **学习与实验**：AI 可在隔离环境中执行命令并提供实时反馈，适合用于教学或技术验证。

## 项目亮点

- **超越传统 AI 编辑器**：通过终端控制能力，AI 能执行任意命令，而不仅仅是代码编辑，极大扩展了应用边界。
- **主机端订阅，无需额外 API 费用**：项目直接使用 Claude Desktop 的订阅，用户无需为 AI 调用支付额外令牌费用。
- **差异化编辑**：相比于整文件覆盖，增量编辑更安全、更高效，尤其适合大型项目。
- **生态丰富**：项目已上架 npm，并在多个 MCP 目录中收录，社区活跃，更新频繁。
- **可选桌面应用**：提供独立的 Desktop Commander 应用，支持更多 AI 模型和高级功能，满足进阶用户需求。

## 相关链接

- [GitHub 仓库](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- [npm 包](https://www.npmjs.com/package/@wonderwhy-er/desktop-commander)
- [Desktop Commander 应用官网](https://desktopcommander.app)
