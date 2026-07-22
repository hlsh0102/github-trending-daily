---
tags:
  - trending
  - article
repo: tradesdontlie/tradingview-mcp
date: 2026-07-22
language: JavaScript
stars_total: 4920
stars_today: 114
---
## 项目概述

TradingView MCP Bridge 是一个将 Claude Code 等 AI 助手与本地运行的 TradingView Desktop 应用程序相连接的工具。它通过 Chrome DevTools Protocol (CDP) 实现与 TradingView 图表的深度交互，为用户提供 AI 辅助的图表分析、Pine Script 开发和自动化工作流能力。

该项目旨在解决 TradingView Desktop 缺乏原生 AI 集成的问题。对于需要每日分析大量图表、编写和调试 Pine Script 策略、或希望将 AI 纳入交易决策流程的用户而言，TradingView MCP Bridge 提供了一条安全、高效的桥梁。目标用户包括量化交易者、技术分析师、Pine Script 开发者和自动化交易研究者。

## 核心功能

- **AI 驱动图表分析**：通过自然语言指令让 AI 助手读取当前图表的技术指标、K线形态、成交量等数据，并生成分析结论。
- **Pine Script 辅助开发**：AI 可读取图表上已有的 Pine Script 代码，协助调试、优化或生成新的策略与指标脚本。
- **图表状态控制**：支持 AI 更改时间周期、切换 K线类型、加载特定技术指标、修改指标参数等操作。
- **跨图表数据交互**：能够读取多窗口布局中不同图表的符号、周期与指标数值，支持组合分析。
- **工作流自动化**：可将重复性分析任务（如每日开盘检查多个交易品种的技术图形）编排为 AI 可执行的自动化流程。
- **本地安全处理**：所有与 TradingView 的数据交互均在用户本机完成，不经过外部服务器，保护交易数据和策略隐私。

## 技术架构

TradingView MCP Bridge 基于 Chrome DevTools Protocol (CDP) 构建，这是所有基于 Chromium/Electron 应用自带的标准调试接口。TradingView Desktop 本质是一个 Electron 应用程序，因此天然支持通过 CDP 进行外部控制。

项目采用 MCP (Model Context Protocol) 架构，这是一种开放标准，用于将 AI 模型与外部工具和数据源连接。具体而言：

- **连接层**：使用 CDP 客户端连接到本地 TradingView Desktop 的调试端口，获取对页面 JavaScript 上下文的完整访问权限。
- **桥接层**：将 TradingView 内部的 JavaScript API 暴露为 AI 可调用的工具函数，例如 `getCurrentChartSymbol()`、`setTimeframe('1D')`、`getPineScriptCode()` 等。
- **MCP 服务层**：以 MCP 服务器形式运行，提供符合标准协议的工具描述、输入参数和响应格式，使得 Claude Code、GitHub Copilot 等支持 MCP 的 AI 工具可以直接调用。
- **安全隔离**：工具的所有通信均限制在本地回环地址，不发起任何对外部网络的连接。AI 模型获得的权限被限定在工具预先定义的操作范围内。

设计上强调透明性和可控性：每个操作的日志都会被记录，用户可明确看到 AI 正在对 TradingView 执行哪些指令。此外，由于依赖 TradingView Desktop 内部未文档化的 API，项目建议用户锁定 TradingView 版本以维持稳定性。

## 安装与使用

**前提条件**：
- 已安装 Node.js（建议 v18 或更高版本）
- 已拥有有效的 TradingView 订阅并安装 TradingView Desktop 应用

**基本安装步骤**：

1. 克隆仓库并进入目录：
```bash
git clone https://github.com/tradesdontlie/tradingview-mcp.git
cd tradingview-mcp
```

2. 安装依赖：
```bash
npm install
```

3. 启动 TradingView Desktop，确保其运行在可调试模式。

4. 启动 MCP 桥接服务：
```bash
npm start
```

5. 在 Claude Code 或其他支持 MCP 的 AI 工具中配置该服务地址，即可开始使用。

**最小可用示例**：
- 在 Claude Code 中输入：“分析当前图表上的 BTCUSDT 日线走势，识别关键支撑阻力位。”
- AI 将通过工具调用获取图表数据并返回分析结果。
- 或者：“在 4 小时图表上添加 50 日均线和 RSI 指标，然后截图保存。”

## 适用场景

- **每日盘前分析**：交易者可在早晨让 AI 自动遍历关注的几个交易品种，检查关键技术位变动、均线交叉信号和成交量异常，生成一份简报。
- **策略开发与回测辅助**：Pine Script 开发者在编写策略时，可直接让 AI 读取当前代码、指出潜在逻辑问题、建议优化方向，并实时载入修改后的代码查看效果。
- **多时间周期分析**：针对同一交易品种，AI 可以按顺序切换日线、4小时、1小时等不同周期，综合评估趋势、阻力和震荡指标状态。
- **自动化监控面板**：结合脚本定时调用，可实现当特定技术信号出现时（如超买超卖、金叉死叉），由 AI 自动标记并通知用户。

## 项目亮点

与同类工具相比，TradingView MCP Bridge 具有以下差异化优势：

- **原生本地架构**：全部计算在本地完成，无需将 TradingView 数据上传至任何第三方 AI 服务，保障交易策略和持仓信息的隐私安全。
- **深度图表控制**：并非仅读取静态截图或 CSV 数据，而是能直接操作 TradingView 图表的完整交互能力，如同一个熟练的人类分析师在操作界面。
- **开放 MCP 协议**：基于标准 MCP 架构，不锁定用户到特定 AI 模型。无论使用 Claude Code、GitHub Copilot 或其他支持 MCP 的工具，均可无缝集成。
- **透明可审计**：所有 AI 对 TradingView 的操作均记录日志，用户可以随时回溯和审查每一步操作的合理性与安全性。
- **社区活跃度高**：仅 GitHub 上已获得 4900+ 星标，且每日新增约 100+ 星标，表明项目获得了大量实际用户的认可和关注。

## 相关链接

- [GitHub 仓库](https://github.com/tradesdontlie/tradingview-mcp)
