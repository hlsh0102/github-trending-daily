---
tags:
  - trending
  - article
repo: ChromeDevTools/chrome-devtools-mcp
date: 2026-07-04
language: TypeScript
stars_total: 45544
stars_today: 405
---
## 项目概述

`chrome-devtools-mcp` 是一个开源项目，它将 Chrome DevTools 的强大功能通过 Model-Context-Protocol (MCP) 服务器暴露给 AI 编码助手。这意味着像 Claude、Cursor、Copilot 或 Antigravity 这样的 AI 工具，现在可以直接控制并检查一个正在运行的 Chrome 浏览器实例，进行可靠的自动化操作、深度调试和性能分析。

项目解决了 AI 编码助手“只能看代码，不能看运行结果”的痛点。以往 AI 助手只能基于静态代码生成建议，而通过 `chrome-devtools-mcp`，AI 可以实时观察页面的运行状态、捕获性能痕迹、分析网络请求、检查控制台日志，从而给出更准确、更具上下文的代码修改建议。目标用户是所有使用 AI 编码助手进行 Web 开发的前端工程师、测试工程师以及性能优化专家。

## 核心功能

- **获取性能洞察**：利用 Chrome DevTools 记录性能轨迹，从中提取可操作的性能优化建议，帮助 AI 助手针对性地生成优化代码。
- **高级浏览器调试**：能够分析网络请求详情、截取页面截图、查看浏览器控制台消息（包括经过源码映射的堆栈追踪），让 AI 助手全面了解运行时状态。
- **可靠的自动化**：基于 Puppeteer 驱动 Chrome 浏览器，自动等待操作结果，确保自动化流程的稳定性和准确性，避免因竞态条件导致的误判。
- **丰富的调试工具套件**：支持元素检查、样式查看、JS 断点调试等多种 DevTools 核心功能，AI 助手可以像人类开发者一样与页面交互。
- **灵活的使用方式**：除了作为 MCP 服务器运行外，还提供了一个独立的 CLI 工具，方便在没有 MCP 客户端的场景下直接使用。

## 技术架构

`chrome-devtools-mcp` 的技术架构围绕 MCP 协议展开。MCP 是一种开放协议，用于在 AI 编码助手和外部工具或数据源之间建立标准化的通信通道。该项目实现了一个 MCP 服务器，将 Chrome DevTools 的各种能力封装成一系列可供 AI 调用的工具。

具体来说，项目内部使用了 **Puppeteer** 来控制 Chrome 浏览器的实例，并通过 Chrome DevTools Protocol (CDP) 与 DevTools 前端进行深度交互。这意味着 AI 助手发出的指令，会通过 MCP 协议被转换成对 Chrome 浏览器的精确操作，从而实现对页面状态、网络、性能等各个维度的检查与控制。

这种架构设计的好处在于：它将复杂的浏览器自动化、DevTools 协议细节完全封装起来，对 AI 助手暴露的是一套简洁、功能强大的 API。AI 助手无需理解底层实现，就能执行“录制性能轨迹”或“分析网络请求”这样复杂的任务。

## 安装与使用

安装 `chrome-devtools-mcp` 非常简单，推荐使用 npm 进行全局安装：

```bash
npm install -g chrome-devtools-mcp
```

安装完成后，你可以通过以下几种方式启动服务：

**方式一：作为 MCP 服务器（推荐）**
在你的 AI 编码助手（如 Claude for Desktop、Cursor 等）的配置文件中，添加 MCP 服务器配置：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "chrome-devtools-mcp",
      "args": []
    }
  }
}
```

配置完成后，AI 助手就能自动发现并使用这个 MCP 服务器提供的所有工具。

**方式二：使用 CLI 工具**
如果你希望在没有 MCP 客户端的场景下使用，可以直接运行 CLI 命令：

```bash
chrome-devtools-mcp --headless
```

该命令会启动一个无头 Chrome 浏览器，并在控制台输出其状态信息。你可以在代码中通过编程方式与之交互。

**最小可用示例**：启动服务后，向 AI 助手提问“请打开百度首页，并检查页面加载性能”。AI 助手就会自动通过 MCP 服务器启动 Chrome、打开指定页面、录制性能轨迹，并返回分析结果。

## 适用场景

- **性能优化辅助**：AI 编码助手可以主动对当前开发的页面进行性能审计，识别出导致页面卡顿的 JavaScript 执行瓶颈或内存泄漏，并给出具体的优化建议和代码修改。
- **端到端测试编写**：AI 可以根据用户提供的测试需求，自动启动浏览器、执行一系列操作、截取特定状态下的截图，并验证页面元素是否符合预期，从而自动生成可靠的端到端测试用例。
- **Bug 自动复现与定位**：当收到用户提交的 Bug 报告时，AI 助手可以打开指定页面、模拟用户操作、复现 Bug，并分析控制台中的错误堆栈和网络请求，直接定位到源码中的问题位置。
- **代码生成验证**：AI 在生成复杂的 UI 组件或交互逻辑后，可以立即启动浏览器验证渲染结果，确保生成的代码能够正确运行，避免了“生成-手动测试-反复修改”的低效循环。

## 项目亮点

与其他自动化测试或调试工具相比，`chrome-devtools-mcp` 的独特优势在于：

- **原生 MCP 集成**：它是专门为 AI 编码助手设计的，采用了 MCP 标准协议，实现了与主流 AI 工具的无缝集成，无需额外的适配工作。
- **完整的 DevTools 能力**：不只是简单的浏览器操作，它能够调用 Chrome DevTools 的全部功能，包括性能分析、网络监控、源码映射堆栈等，这是普通 Puppeteer 脚本难以比拟的。
- **开箱即用**：安装即用，配置简单，AI 助手可以零额外学习成本地开始使用，大大提升了开发效率。
- **社区活跃**：由 ChromeDevTools 官方团队维护，拥有大量用户基础和活跃社区支持，项目持续迭代，紧跟 AI 编码助手的发展趋势。

## 相关链接

- [GitHub 仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [开发文档](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md)
