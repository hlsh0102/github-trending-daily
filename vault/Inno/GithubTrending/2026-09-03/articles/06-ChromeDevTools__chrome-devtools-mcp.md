---
tags:
  - trending
  - article
repo: ChromeDevTools/chrome-devtools-mcp
date: 2026-09-03
language: TypeScript
stars_total: 50742
stars_today: 148
---
## 项目概述

`chrome-devtools-mcp` 是 Chrome DevTools 团队官方推出的 Model-Context-Protocol（MCP）服务器，旨在为 AI 编程代理（如 Antigravity、Claude、Cursor、Copilot 等）提供对实时 Chrome 浏览器的完全控制与检查能力。该工具将 Chrome DevTools 的强大功能封装为 MCP 协议接口，使 AI 助手能够执行可靠的自动化操作、深入的调试分析和性能诊断。项目使用 TypeScript 编写，以 Apache-2.0 许可证开源，目前在 GitHub 上获得超过 5 万颗星，深受开发者社区欢迎。

对于使用 AI 辅助编程的开发者而言，该工具解决了智能代理在浏览器端操作能力受限的痛点。此前，AI 编程助手大多只能处理静态代码，无法观测或操控真实运行环境中的网页表现。通过接入 `chrome-devtools-mcp`，编码代理得以获得 `查看控制台日志`、`模拟用户操作`、`分析网络流量`、`记录性能轨迹` 等能力，极大拓展了 AI 在端到端开发、测试、排错等环节的应用边界。

## 核心功能

- **性能洞察**：借助 Chrome DevTools 前端框架，自动记录页面性能轨迹（trace），提取可操作的性能瓶颈信息，例如长时间任务、布局抖动、网络瀑布等。
- **高级浏览器调试**：支持审查网络请求详情（包括请求头、响应体、状态码）、捕获页面截图、读取浏览器控制台消息，堆叠信息经过源码映射（source-map）处理，便于定位到原始 TS/JS 代码而非压缩代码。
- **可靠的自动化操作**：底层通过 Puppeteer 库驱动 Chrome，自动化执行点击、输入、导航等操作，并能自动等待页面和元素达到预期状态后再返回结果，显著降低自动化脚本的脆弱性。
- **MCP 协议集成**：作为标准 MCP 服务器，可无缝接入各类支持 MCP 协议的 AI 客户端，实现统一接口调用。
- **轻量级 CLI**：提供基于命令行的独立工具，无需 MCP 环境也可独立使用，方便脚本集成或手动快速验证。

## 技术架构

`chrome-devtools-mcp` 核心采用 TypeScript 开发，设计上遵循 MCP 服务，将 DevTools 协议（Chrome DevTools Protocol，CDP）与 Puppeteer 的自动化能力桥接到 MCP 消息通道中：

- **CDP 层**：直接用 `devtools-frontend` 的组件递归追踪和性能分析的逻辑，而非简单封装命令行工具。
- **Puppeteer 调度层**：负责启动、连接、控制独立 Chrome 实例，并处理并发命令、页面生命周期管理等细节。
- **MCP 服务层**：定义各类功能 Tool 的输入输出 schema，支持结构化参数验证，确保 AI Agent 生成命令的合法性。
- **安全设计**：官方声明用户需注意——该服务会将浏览器内部数据暴露给 MCP 客户端，因此不应在含有敏感信息（如登录态、个人数据）的环境中使用。此外，项目明确官方支持 Google Chrome（对其他 Chromium 内核浏览器兼容性未做保证）。

架构上强调解耦与可扩展性，每一层都便于独立测试和替换。例如，性能分析模块可独立于自动化层升级，用户也可通过配置关闭不必要的 Tool 以降低安全风险。

## 安装与使用

**全局安装**

```bash
npm install -g chrome-devtools-mcp
```

**以 MCP 服务器方式运行**

在支持 MCP 的客户端（如 Claude Desktop、Cursor 等）中，将 `chrome-devtools-mcp` 作为外部服务器添加：

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

**使用 CLI（无需 MCP）**

```bash
chrome-devtools-mcp --cli
# 进入交互式命令行，可输入命令如：navigate <url>、screenshot、console-messages 等
```

**连接已有 Chrome 实例**

如果不希望工具自行启动一个新的浏览器进程，可通过 `--browserUrl` 参数连接已开启远程调试端口的 Chrome：

```bash
chrome-devtools-mcp --browserUrl http://localhost:9222
```

**最小可用示例**

启动后，在 MCP 客户端中发送自然语言指令，例如：  
_“打开 example.com，点击 body 上的按钮，然后截图，并告诉我控制台是否有报错。”_  
工具会自动映射到相应操作序列，并通过 Puppeteer 的等待逻辑确保操作可靠完成。

> 注意：正式使用前，请阅读官方文档中的 [Troubleshooting][troubleshooting] 和 [Design Principles][design-principles]，特别是了解缓存与浏览器实例复用原理，避免状态污染。

## 适用场景

- **AI 辅助前端调试**：当 AI 编码助手生成代码可能含有运行时错误时，让其自动打开浏览器，检查 console 报错与网络 404，从而快速定位问题并自主迭代修复。
- **视觉回归与交互验收测试**：在 CI 流水线中调用该工具，让代理 Agent 自动执行页面点击流，对比屏幕截图，并结合性能指标判断是否有明显退化，从而减少人工回归成本。
- **性能优化顾问**：开发者向 Agent 描述“首页加载慢”，Agent 利用 `chrome-devtools-mcp` 采集 tracing 数据，分析出阻塞渲染的脚本或未压缩的资源，并直接给出量化报告与修改建议。
- **爬虫与数据采集中的复杂交互**：在需要登录、翻页、滚动加载等复杂交互的爬虫中，结合 AI 规划步骤与工具的执行能力，提高防护严苛网站的采集成功率。

## 项目亮点

- **背靠官方能力**：Chrome DevTools 团队维护，直接复用 DevTools 内部的追踪与性能分析逻辑，功能深度与可靠性远超社区自研的简易封装。
- **源码映射栈追踪**：控制台错误信息自动带出原始源码位置，此特性在同类自动化工具中极为稀缺，可大幅减轻 AI 排障的认知负担。
- **自动化等待机制**：通过智能等待，显著减少了定时器随意 sleep 的需求，自动判断 action 完成时机，让 AI Agent 生成的脚本更贴近人工操作习惯。
- **双重接口形态**：同时提供标准 MCP 协议与命令行 CLI，既满足多智能体生态接入需求，也允许传统脚本进行轻量调用，覆盖更深层的用户群。
- **设计文档公开**：项目公开了设计原则文档，对安全性、浏览器生命周期处理等做出明确解释，为二次开发或企业内部分叉提供权威基准。

## 相关链接

- [GitHub 仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [工具参考文档](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool_reference.md)
- [变更日志](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/CHANGELOG.md)
- [贡献指南](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/CONTRIBUTING.md)
- [故障排查](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md)
- [设计原则](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/design-principles.md)
