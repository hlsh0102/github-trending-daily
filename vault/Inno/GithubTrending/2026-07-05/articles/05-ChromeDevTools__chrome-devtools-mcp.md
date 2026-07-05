---
tags:
  - trending
  - article
repo: ChromeDevTools/chrome-devtools-mcp
date: 2026-07-05
language: TypeScript
stars_total: 45843
stars_today: 304
---
## 项目概述

`chrome-devtools-mcp` 是 Chrome DevTools 团队官方推出的一款开源工具，它通过模型上下文协议，让您的 AI 编码助手（如 Antigravity、Claude、Cursor 或 Copilot）能够直接控制并检视一个实时的 Chrome 浏览器实例。该项目本质上是一个 MCP 服务器，为 AI 工具赋予了完整的 Chrome DevTools 能力——包括可靠的浏览器自动化、深入的调试分析和性能剖析。同时，项目也提供了独立的 CLI 工具，方便没有 MCP 支持的环境使用。目标用户主要包括：希望利用 AI 辅助进行前端开发、网页性能优化、端到端自动化测试的开发者与测试人员。

## 核心功能

- **获取性能洞察**：借助 Chrome DevTools 前端，录制运行时性能轨迹，并提取可操作的性能优化建议，帮助开发者精准定位瓶颈。
- **高级浏览器调试**：支持分析网络请求、截取页面截图、检查浏览器控制台消息，并且控制台错误堆栈会自动进行源码映射，便于在开发环境中定位问题。
- **可靠的自动化操作**：基于 Puppeteer 驱动 Chrome 浏览器执行自动化操作，并能智能等待操作结果稳定后继续，避免竞态条件。
- **完整的 DevTools 面板接入**：通过 MCP 协议，AI 助手可以调用 DevTools 的各种底层能力，包括但不限于元素检查、样式修改、断点调试等。
- **灵活的运行模式**：既可作为 MCP 服务器集成到 Cursor、Claude 等支持 MCP 的 AI 工具中，也可通过独立 CLI 直接使用，满足不同工作流需求。
- **源码映射支持**：错误堆栈和工具提示自动关联到原始源码（而非编译后代码），极大降低调试心智负担。

## 技术架构

项目的核心是基于 Chrome DevTools 协议和 Puppeteer 构建的 MCP 服务器。设计上遵循了几个关键原则：首先，采用“等待结果稳定”的自动化策略，而非传统工具中的固定超时或轮询，这得益于 Puppeteer 对 Chrome DevTools 协议的深度集成。其次，性能分析功能直接复用 DevTools 前端的 Trace 录制与解析引擎，确保洞察的专业性与一致性。架构上，MCP 服务器作为中介层，将 AI 助手的自然语言请求转换为对 Chrome 实例的精准操作指令，并将 DevTools 返回的复杂结构化数据（如网络瀑布图、控制台日志、性能轨迹）格式化后返回给 AI。此外，项目提供了详细的工具参考文档和故障排除指南，降低了使用门槛。

## 安装与使用

**前提条件**：确保系统中已安装 Node.js（推荐 v18 及以上版本）和 Google Chrome 浏览器。

**基本安装**：
```bash
npm install chrome-devtools-mcp
```

**作为 MCP 服务器使用（以 Cursor 为例）**：
1. 启动 Chrome 浏览器并开启远程调试端口：
   ```bash
   google-chrome --remote-debugging-port=9222
   ```
2. 配置 Cursor 的 MCP 客户端连接到此端口。
3. 在 Cursor 的 AI 对话中直接发出指令，例如："分析当前页面的性能瓶颈" 或 "帮我调试这个网络请求失败的原因"。

**使用 CLI 模式**：
```bash
npx chrome-devtools-mcp --port 9222 # 连接到已启动的 Chrome 实例
```
之后可执行具体命令，例如截取截图或录制性能轨迹。

**最小可用示例**（CLI 模式）：
1. 打开一个终端，启动带远程调试的 Chrome：`chrome --remote-debugging-port=9222`
2. 在另一个终端运行：`npx chrome-devtools-mcp --port 9222 screenshot --url https://example.com --output screenshot.png`

## 适用场景

- **AI 辅助前端调试**：开发者直接在 AI 助手聊天框中描述问题（如“为什么这个按钮的点击事件没触发？”），AI 通过 MCP 自动打开 DevTools、查看事件监听器、检查控制台错误，并返回分析结果。
- **自动化性能审计**：将 `chrome-devtools-mcp` 集成到 CI/CD 流水线中，对每次构建的新版本进行自动化性能轨迹录制与指标提取，及时发现回归问题。
- **端到端测试增强**：传统 E2E 测试往往难以获取浏览器内部状态。结合此工具，AI 可以动态检查 DOM 结构、监听网络事件、分析错误日志，让用例更加智能和健壮。
- **无头浏览器远程协作**：团队成员可以共享同一个浏览器实例，AI 助手协助实时排查远程环境中的页面问题，尤其适合跨时区协作。

## 项目亮点

- **官方出品，生态兼容**：由 Chrome DevTools 团队直接维护，与 Chrome 浏览器的迭代高度同步，兼容性最佳。
- **深度对接 AI 工作流**：通过 MCP 标准化协议，无需额外适配即可接入主流的 AI 编码工具，降低了 AI 辅助开发的门槛。
- **源码映射提升效率**：DevTools 的原始报错信息经过自动源码映射，AI 能直接定位到开发者编写的 TypeScript/JSX 源码，而非编译产物。
- **智能等待机制**：不同于传统脚本中固定的 sleep 或轮询，Puppeteer 驱动的等待机制能感知页面状态变化，显著提升自动化场景的稳定性。

## 相关链接

- [GitHub 仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [工具参考文档](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md)
- [设计原则文档](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/design-principles.md)
- [故障排除指南](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md)
