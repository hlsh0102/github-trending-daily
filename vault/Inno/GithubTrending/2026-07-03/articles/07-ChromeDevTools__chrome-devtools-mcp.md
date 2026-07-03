---
tags:
  - trending
  - article
repo: ChromeDevTools/chrome-devtools-mcp
date: 2026-07-03
language: TypeScript
stars_total: 45176
stars_today: 104
---
## 项目概述

`chrome-devtools-mcp` 是 Chrome DevTools 官方团队开源的一个工具，它为 AI 编程代理（如 Antigravity、Claude、Cursor 或 Copilot）提供了直接控制与检查实时 Chrome 浏览器的能力。该项目作为一个 Model-Context-Protocol（MCP）服务器运行，使 AI 编程助手能够利用完整的 Chrome DevTools 功能，实现可靠的自动化操作、深入的调试以及性能分析。同时，它也提供了 CLI 工具，方便在没有 MCP 的环境中使用。

该项目解决了开发者在 AI 辅助编程中无法直接与浏览器交互的痛点。传统上，AI 编码助手只能通过文本描述理解问题，而 `chrome-devtools-mcp` 让它们能够直接“看到”浏览器中的实际表现，获取网络请求、控制台日志、性能追踪等关键信息。目标用户包括使用 AI 编码助手进行 Web 开发的软件工程师、前端开发者以及需要自动化浏览器调试的团队。

## 核心功能

- **性能洞察**：利用 Chrome DevTools 记录性能追踪（trace），并提取可操作的性能优化建议，帮助开发者发现页面渲染、脚本执行等方面的瓶颈。
- **高级浏览器调试**：支持分析网络请求、截取浏览器截图、检查浏览器控制台消息（包含 source-map 映射后的堆栈跟踪），提供全面的调试能力。
- **可靠自动化**：基于 Puppeteer 实现浏览器操作自动化，能够自动等待操作结果，确保自动化流程的稳定性和可预测性。
- **DevTools 面板操作**：允许 AI 代理直接访问和操作 Chrome DevTools 的各种面板，包括 Elements、Console、Network、Performance 等，实现与人工调试相似的能力。
- **上下文感知交互**：作为 MCP 服务器，它能够为 AI 代理提供当前浏览器状态的完整上下文，让 AI 更准确地理解问题并给出针对性建议。

## 技术架构

`chrome-devtools-mcp` 采用 TypeScript 编写，核心架构基于以下关键技术：

- **MCP 协议**：项目实现为 MCP（Model-Context-Protocol）服务器，这是一种标准化的协议，允许 AI 模型与外部工具和数据进行交互。通过 MCP，AI 代理可以以统一的方式调用各种浏览器操作和 DevTools 功能。
- **Puppeteer**：作为底层浏览器自动化引擎，Puppeteer 提供了对 Chrome 的完整控制能力，包括页面导航、元素操作、截图、网络拦截等。项目在此基础上封装了更高级的 DevTools 相关功能。
- **Chrome DevTools Frontend**：直接利用 Chrome DevTools 的前端代码库，获取性能追踪、网络记录、控制台日志等专业调试数据，保证了与真实开发工具的一致性。
- **模块化设计**：项目采用模块化架构，将不同功能（性能分析、网络调试、自动化控制等）组织为独立的模块，便于扩展和维护。

架构设计上，`chrome-devtools-mcp` 注重安全性和可控性。它通过 MCP 协议暴露浏览器内容给 AI 代理，但文档中明确提示用户避免分享敏感或个人信息。

## 安装与使用

### 安装

```bash
# 通过 npm 全局安装
npm install -g chrome-devtools-mcp

# 或使用 npx 直接运行
npx chrome-devtools-mcp
```

### 基本使用

1. **启动 MCP 服务器**：
```bash
chrome-devtools-mcp
```

2. **在 AI 编码助手（如 Claude Desktop、Cursor）中配置 MCP 服务器**：
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "chrome-devtools-mcp"
    }
  }
}
```

3. **使用 CLI 模式**（无需 MCP）：
```bash
# 截图示例
chrome-devtools-mcp screenshot --url https://example.com

# 性能分析
chrome-devtools-mcp trace --url https://example.com --output trace.json
```

### 最小可用示例

以下是一个简单的使用场景，让 AI 代理检查网页性能：

1. 启动 MCP 服务器。
2. 在 AI 编码助手界面中，发送指令：“打开 example.com，记录性能追踪，分析加载瓶颈”。
3. AI 代理会通过 MCP 调用相关工具，自动打开浏览器、记录性能数据、分析结果，并返回优化建议。

## 适用场景

- **性能优化工作流**：开发者在进行性能优化时，可以借助 AI 代理自动分析页面加载性能、识别长任务、发现渲染瓶颈，并获取具体的优化建议，大幅减少手动调试的时间。
- **自动化调试与排查**：当需要排查复杂的网络请求问题或 JavaScript 运行时错误时，AI 代理可以直接启动浏览器、复现问题、检查网络面板和控制台日志，快速定位问题根源。
- **端到端测试编写**：在编写端到端测试时，AI 代理可以通过 `chrome-devtools-mcp` 在真实浏览器中执行操作并验证结果，生成更准确、更接近实际用户行为的测试用例。
- **教学与代码审查**：用于演示前端技术的工作原理，或在代码审查过程中自动检查页面行为与代码变更的对应关系，帮助评审者理解影响范围。

## 项目亮点

`chrome-devtools-mcp` 与同类项目相比，具有以下差异化优势：

- **官方出品**：由 Chrome DevTools 团队维护，保证了与最新 Chrome 浏览器的兼容性，以及对 DevTools 功能的完整支持。
- **深度集成 DevTools**：不仅仅是简单的浏览器自动化，而是直接利用了 Chrome DevTools 的专业能力，性能分析、网络调试等功能的专业度远超一般自动化工具。
- **MCP 标准协议**：采用 MCP 协议使该项目能够与多种 AI 编码助手无缝集成，无需为每个平台单独适配。
- **开源与社区驱动**：基于 Apache-2.0 许可证开源，社区活跃度高（拥有超过 45,000 颗 Star），文档完善，有详细的故障排除指南和设计原则说明。

## 相关链接

- [GitHub 仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [工具参考文档](./docs/tool-reference.md)
- [故障排除指南](./docs/troubleshooting.md)
- [设计原则](./docs/design-principles.md)
