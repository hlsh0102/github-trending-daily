---
tags:
  - trending
  - article
repo: alsk1992/CloddsBot
date: 2026-09-13
language: TypeScript
stars_total: 2585
stars_today: 376
---
## 项目概述

CloddsBot 是一个开源的 AI 交易智能体（AI trading agent），能够跨多个市场自主执行交易与风险管理。项目名称来自 "Claude + Odds"，底层由 Anthropic 的 Claude 模型驱动，定位于预测市场、加密货币现货/永续合约以及链上 DEX 等场景。

它试图解决的问题是：在多市场环境下，交易者需要同时监控预测市场（Polymarket、Kalshi）、中心化交易所（Binance、Hyperliquid）和链上交易（Solana DEX、5 条 EVM 链）之间的定价偏差，而人工很难在 1000+ 市场中持续扫描并即时执行。CloddsBot 将这些市场统一接入一个智能体循环，自动寻找可交易的 edge、执行下单并托管风险，同时提供 agent commerce protocol 以支持机器对机器的支付。

目标用户包括：自托管的量化交易者、预测市场套利者、加密资产交易者，以及希望在此基础上构建自动化交易策略的开发者。

## 核心功能

- **跨市场 edge 扫描**：同时接入 1000+ 市场（Polymarket、Kalshi、Binance、Hyperliquid、Solana DEX 及 5 条 EVM 链），持续扫描价格错位与套利机会。
- **自主执行与风控**：在识别到机会后即时下单，并在后台持续管理仓位、止损与整体风险敞口。
- **Agent Commerce Protocol**：提供机器对机器的支付协议，允许 agent 之间进行价值交换与协作。
- **121+ 技能（Skills）体系**：内置 121 个以上可组合技能，覆盖行情读取、下单、风控、事件响应等原子操作。
- **自托管部署**：用户在自己的环境中运行全部组件，私钥与资金不经过托管方。
- **基于 Claude 的推理层**：使用 Claude 进行市场判断、策略选择与自然语言交互。

## 技术架构

项目使用 TypeScript 编写，要求 Node.js >= 22，采用 MIT 许可证。整体架构可理解为三层：

1. **市场接入层**：为每个交易场所（预测市场、CEX、DEX、EVM 链、Solana）提供适配器，统一成一致的订单与行情接口。
2. **Agent 推理层**：由 Claude 模型承担决策与编排，配合 121+ Skills 将高层意图拆解为可执行动作。
3. **执行与风控层**：负责下单、持仓跟踪、风险限额与自动平仓，并在需要时通过 agent commerce protocol 与其他智能体结算。

这种"统一适配器 + 模型推理 + 技能编排"的设计使新增市场只需实现对应适配器，而策略逻辑可通过技能组合复用，降低了扩展成本。

## 安装与使用

基本步骤（基于常见 Node.js 项目实践）：

1. 确保本机安装 Node.js 22 或更高版本。
2. 克隆仓库并安装依赖：

```bash
git clone https://github.com/alsk1992/CloddsBot.git
cd CloddsBot
npm install
```

3. 复制环境变量模板并填入所需配置，例如 Anthropic API Key、各交易所 API Key、RPC 端点等：

```bash
cp .env.example .env
```

4. 构建并启动：

```bash
npm run build
npm start
```

具体命令、环境变量名称与支持的技能列表以仓库 README 与 docs 目录为准。最小可用示例通常只需要配置一个市场（例如 Polymarket 或 Binance 测试网）与 Claude 的 API Key，即可让 agent 开始扫描。

## 适用场景

- **预测市场套利**：在 Polymarket 与 Kalshi 之间寻找同一事件定价差异并自动执行。
- **跨市场做市/对冲**：在 CEX 与链上 DEX 之间捕捉价差，同时对冲方向性风险。
- **无人值守交易**：配置完成后，agent 在夜间或离线时段持续监控与执行。
- **Agent 经济实验**：借助 agent commerce protocol 构建多智能体之间的机器支付与协作流程。

## 项目亮点

与常见的单市场交易机器人相比，CloddsBot 的主要差异在于：

- **市场覆盖广**：单个 agent 同时覆盖预测市场、CEX、永续合约、Solana DEX 与多条 EVM 链，而非局限于一个场所。
- **真正的自主性**：从扫描到执行再到风控形成闭环，不依赖人工触发下单。
- **技能化扩展**：121+ Skills 让策略组合与扩展具备模块化路径。
- **自托管 + 开源**：MIT 许可、代码公开，资金与密钥由用户掌握。
- **Agent 原生**：内置机器对机器支付协议，面向智能体经济场景而不仅是人类交易者。

## 相关链接

- [GitHub 仓库](https://github.com/alsk1992/CloddsBot)
- [官网](https://cloddsbot.com)
- [最新 Release](https://github.com/alsk1992/CloddsBot/releases/latest)
