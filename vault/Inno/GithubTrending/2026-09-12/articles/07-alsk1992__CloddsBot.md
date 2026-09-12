---
tags:
  - trending
  - article
repo: alsk1992/CloddsBot
date: 2026-09-12
language: TypeScript
stars_total: 2247
stars_today: 626
---
## 项目概述

CloddsBot 是一个开源的 AI 交易代理（trading agent），由开发者 alsk1992 构建并以 MIT 协议发布。它的核心思路是将大语言模型（Claude）的推理能力与多市场交易执行能力结合，让代理能够自主地在超过 1000 个市场中扫描交易机会、执行订单并管理风险。项目名称 "Clodds" 取自 "Claude" 与 "Odds"（赔率）的组合，点明了其定位：面向预测市场与加密资产市场的智能交易终端。

它主要解决的问题是：在预测市场（如 Polymarket、Kalshi）和加密市场（如 Binance、Hyperliquid、Solana DEX、多条 EVM 链）之间，价格与信息往往分散在不同平台，人工监控和跨市场套利效率低下。CloddsBot 通过统一的代理框架接入这些市场，自动完成信息扫描、信号评估与下单操作，从而降低人工盯盘成本。

目标用户包括：希望自动化交易策略的量化爱好者、跨市场套利交易者、对 AI 代理与 agent commerce 协议感兴趣的开发者，以及希望自托管交易工具、不愿将资金控制权交给第三方托管平台的用户。

## 核心功能

- **多市场接入与扫描**：覆盖 Polymarket、Kalshi、Binance、Hyperliquid、Solana DEX 以及 5 条 EVM 链，代理持续扫描超过 1000 个市场，寻找定价偏差与潜在 edge。
- **自主执行交易**：在识别到符合条件的信号后，代理可即时下单执行，无需人工确认，支持在用户设定的范围内自动运作。
- **风险管理**：内置风险控制机制，在代理运行期间对仓位、敞口和执行节奏进行约束，降低单笔或连环操作带来的损失。
- **Agent Commerce 协议**：提供机器对机器（machine-to-machine）的支付能力，使代理之间可以进行价值交换与协作。
- **自托管部署**：所有密钥、资金与策略运行在用户自己的环境中，不依赖中心化托管服务。
- **技能系统**：README 显示内置 121+ 个 skills，以模块化方式扩展代理可执行的操作类型。

## 技术架构

项目使用 TypeScript 编写，要求 Node.js 22 及以上版本，TypeScript 版本标注为 5.3，采用 MIT 许可证。整体架构围绕"代理 + 技能 + 市场适配器"的思路设计：

- **推理层**：基于 Claude，负责对市场信息进行判断、生成交易决策。代理并非简单规则触发，而是借助 LLM 的理解与推理能力评估信号。
- **技能层**：以 skills 的形式封装可执行动作，目前超过 121 个，便于按需组合和扩展。
- **市场适配层**：为不同交易所和链上协议提供统一接口，屏蔽各平台 API 差异，使代理能以一致方式访问 Polymarket、Kalshi、Binance、Hyperliquid、Solana DEX 和多条 EVM 链。
- **执行与风控层**：负责订单落地与风险约束，确保代理在预设边界内运作。
- **自托管设计**：强调用户自行部署与掌控私钥，减少对第三方服务的依赖。

从定位看，项目面向 Colosseum Agent Hackathon 构建，属于"AI 代理 + 加密金融"方向的开源实践。

## 安装与使用

以下为基于常见 Node.js 项目结构的概述性步骤，具体命令请以仓库文档为准：

1. 确认环境满足 Node.js >= 22。
2. 克隆仓库：

   ```bash
   git clone https://github.com/alsk1992/CloddsBot.git
   cd CloddsBot
   ```

3. 安装依赖：

   ```bash
   npm install
   ```

4. 配置环境变量，填入 Claude API 凭证以及各市场（如 Polymarket、Binance 等）所需的 API key 或钱包信息。
5. 启动代理：

   ```bash
   npm start
   ```

最小可用示例：完成上述配置后，代理会按默认策略开始扫描市场；用户可通过配置文件调整目标市场、风控参数和启用的 skills。由于涉及真实资金与密钥，建议先在测试网络或小额仓位下验证行为。具体配置项与命令请参考仓库中的 README 和文档。

## 适用场景

- **跨市场套利**：在预测市场与加密市场之间捕捉同类事件的定价差异。
- **预测市场自动交易**：在 Polymarket、Kalshi 上按策略持续扫描并自动执行。
- **加密资产交易自动化**：通过 Binance、Hyperliquid 及 Solana DEX、EVM 链执行策略。
- **AI 代理与 agent commerce 研究**：作为机器对机器支付的实验与开发平台。

## 项目亮点

与同类交易机器人相比，CloddsBot 的差异化主要体现在：接入市场的广度（预测市场 + 中心化交易所 + 多条链上 DEX）、以 Claude 为核心的推理式决策而非纯规则触发、121+ skills 的模块化扩展能力，以及面向机器对机器支付的 agent commerce 协议。同时项目坚持自托管，用户保留对密钥与资金的控制权。其在 GitHub 上已获得 2247 颗星（数据截至仓库描述所示时点），并进入 Trendshift 榜单。

## 相关链接

- [GitHub 仓库](https://github.com/alsk1992/CloddsBot)
- [最新 Release](https://github.com/alsk1992/CloddsBot/releases/latest)
