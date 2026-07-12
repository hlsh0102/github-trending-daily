---
tags:
  - trending
  - article
repo: wonderwhy-er/DesktopCommanderMCP
date: 2026-07-12
language: TypeScript
stars_total: 7817
stars_today: 909
---
## 项目概述

Desktop Commander MCP 是一个为 Claude 等 AI 助手提供终端控制、文件系统搜索和差异化文件编辑能力的 MCP（Model Context Protocol）服务器。该项目解决了 AI 模型无法直接操作本地计算机文件系统和执行终端命令的痛点，使 AI 能够像人类开发者一样浏览、编辑文件并运行命令。主要面向使用 Claude Desktop 及其他 MCP 客户端的开发者、技术写作者和自动化工作者，帮助他们在 AI 辅助下更高效地完成编码、文本处理、任务自动化等工作。

## 核心功能

- **终端控制**：允许 AI 直接在本地终端中执行命令，包括运行脚本、编译代码、启动服务等，并实时获取输出结果
- **文件系统搜索**：支持按文件名、内容、模式等方式快速搜索本地文件，帮助 AI 定位和理解项目结构
- **差异化文件编辑**：提供智能的文件编辑能力，AI 可以精确修改文件中的特定行或段落，而非覆盖整个文件，减少误改风险
- **多文件管理**：支持同时打开、读取、编辑多个文件，便于进行跨文件的重构和修改
- **安全控制**：提供可配置的命令白名单/黑名单，限制 AI 可以执行的终端操作，保障系统安全
- **实时反馈**：AI 执行操作后即时获得结果和状态更新，支持迭代调试和逐步改进

## 技术架构

该项目基于 TypeScript 开发，遵循 MCP（Model Context Protocol）标准协议。MCP 是 Anthropic 提出的一种用于 AI 模型与外部工具交互的开放协议，遵循客户端-服务器架构：Claude Desktop 作为 MCP 客户端，Desktop Commander MCP 作为服务端提供工具接口。

核心技术特点包括：
- 使用标准输入输出（stdio）或 HTTP 协议与客户端通信，支持灵活的部署方式
- 采用模块化设计，将终端控制、文件搜索、文件编辑等功能封装为独立的工具模块
- 实现了安全的命令执行沙箱，通过白名单机制防止恶意命令执行
- 支持文件差异比较和智能合并，在编辑时自动备份原始文件，支持回滚

## 安装与使用

### 前提条件
- Node.js 18.0 或更高版本
- npm 或 yarn 包管理器
- Claude Desktop 或其他支持 MCP 的客户端

### 安装步骤

1. **全局安装 MCP 服务器**：
```bash
npm install -g @wonderwhy-er/desktop-commander
```

2. **配置 Claude Desktop**：
在 Claude Desktop 的配置文件（通常位于 `~/.claude/claude_desktop_config.json`）中添加：
```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["@wonderwhy-er/desktop-commander"]
    }
  }
}
```

3. **重启 Claude Desktop**，即可在对话中让 AI 直接操作你的文件系统和终端。

### 最小可用示例

安装并配置后，你可以直接对 Claude 说：
- "搜索当前目录下所有包含'API_KEY'的配置文件"
- "打开 `src/main.ts`，在第42行后添加日志输出"
- "运行 `npm test` 并告诉我测试结果"

AI 将自动调用相应的 MCP 工具完成操作，并将结果反馈给你。

## 适用场景

- **代码开发与调试**：开发者可以让 AI 直接读取项目文件、修改代码、运行测试命令，实现真正的 AI 辅助编程，无需手动复制粘贴代码
- **系统管理与维护**：IT 运维人员可以通过 AI 执行服务器检查、日志分析、配置修改等操作，提升例行工作的效率
- **文档与内容创作**：技术写作者可让 AI 搜索项目文件、提取代码示例、自动生成文档内容，并直接写入文件系统
- **自动化工作流**：结合其他 MCP 工具（如数据库、API 等），构建复杂的自动化任务，如数据抓取、文件转换、报告生成等

## 项目亮点

- **原生终端集成**：与其他 AI 编程工具（如 Copilot）不同，Desktop Commander MCP 让 AI 拥有真正的终端执行能力，而不仅仅是代码补全或建议
- **零 API 成本**：使用 Claude Desktop 订阅制，不按 API 调用计费，适合高频使用的开发者
- **开源透明**：MIT 许可证，代码完全可见，无后门风险，用户可以自行审计安全实现
- **灵活可扩展**：基于 MCP 标准协议，可与其他 MCP 工具和 AI 模型组合使用，不受限于特定平台
- **社区活跃**：项目拥有超过 7800+ 星标，更新频繁，社区提供丰富的使用案例和问题解答

## 相关链接

- [GitHub 仓库](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- [NPM 包](https://www.npmjs.com/package/@wonderwhy-er/desktop-commander)
- [Agent Audit 目录](https://agentaudit.dev/skills/desktop-commander)
- [MCP 目录](https://archestra.ai/mcp-catalog/wonderwhy-er__desktopcommandermcp)
- [Smithery 安装](https://smithery.ai/server/@wonderwhy-er/desktop-commander)
- [桌面版应用（Beta）](https://desktopcommander.app)
- [Discord 社区](https://discord.gg/kQ27sNnZr7)
