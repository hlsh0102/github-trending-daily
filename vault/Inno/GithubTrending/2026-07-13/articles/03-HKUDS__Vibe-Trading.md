---
tags:
  - trending
  - article
repo: HKUDS/Vibe-Trading
date: 2026-07-13
language: Python
stars_total: 20820
stars_today: 768
---
## 项目概述

Vibe-Trading 是一个开源的个人交易智能体项目，由香港大学数据科学实验室（HKUDS）开发。该项目旨在通过一条命令即可让用户拥有一个具备全面交易能力的智能助手。它解决了个人投资者在复杂多变的金融市场中缺乏高效、自动化交易工具的问题，让没有专业编程背景的用户也能轻松部署和使用自己的交易机器人。目标用户包括加密货币和传统金融市场的个人交易者、量化交易爱好者以及希望探索自动化交易策略的研究人员。

## 核心功能

- **全自动化交易执行**：支持基于预设策略自动执行买卖操作，覆盖加密货币市场和传统金融品种。
- **多交易所对接**：内置对主流交易平台（如Binance、Bybit等）的API支持，用户只需配置密钥即可接入。
- **智能策略引擎**：提供多种内置交易策略模板，包括趋势跟踪、网格交易、均值回归等，同时支持用户自定义策略脚本。
- **实时市场监控与通知**：持续追踪市场行情变化，通过Telegram、邮件或Webhook推送交易信号和账户异动提醒。
- **可视化仪表盘**：基于React构建的前端界面，实时展示持仓、盈亏、交易历史和策略绩效指标。
- **回测与模拟交易**：支持历史数据回测以评估策略表现，并提供模拟盘环境供用户无风险测试。

## 技术架构

Vibe-Trading 采用前后端分离的微服务架构。后端基于 **FastAPI** 构建，提供高性能的RESTful API和WebSocket接口，负责策略调度、订单管理和行情数据处理。数据存储层使用 **PostgreSQL** 记录交易日志和用户配置，搭配 **Redis** 作为缓存和消息队列。前端使用 **React 19** 开发，通过图表库（如 ECharts）绘制实时K线和资金曲线。

核心设计思路是“即开即用”与“可扩展”的平衡。系统通过 **YAML配置文件** 管理交易所连接、策略参数和风控规则，用户无需编码即可完成基础设置。同时，策略插件采用 **Python脚本热加载机制**，允许高级用户编写自定义策略并动态注入运行环境。项目还集成了 **LangChain** 框架，可利用大语言模型解析自然语言交易指令，实现“智能对话式交易”。

## 安装与使用

### 前置条件
- Python 3.11+
- Node.js 18+（仅前端）

### 安装步骤
1. **克隆仓库**
   ```bash
   git clone https://github.com/HKUDS/Vibe-Trading.git
   cd Vibe-Trading
   ```

2. **安装后端依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **安装前端依赖（可选，仅使用API则可跳过）**
   ```bash
   cd frontend
   npm install
   ```

4. **配置环境变量**
   复制 `.env.example` 为 `.env`，填写交易所API密钥、数据库连接等参数。

5. **启动服务**
   ```bash
   # 启动后端
   uvicorn main:app --host 0.0.0.0 --port 8000
   
   # 启动前端（可选）
   cd frontend && npm start
   ```

### 最小可用示例
```python
# 快速运行内置的网格交易策略
from vibe_trading import VibeAgent

agent = VibeAgent(
    exchange="binance",
    strategy="grid",
    symbol="BTC/USDT",
    config={"upper_price": 50000, "lower_price": 40000, "grids": 10}
)
agent.run()  # 开始自动交易
```

## 适用场景

- **个人量化投资**：普通投资者使用内置策略进行加密货币或股票自动化交易，省去盯盘时间。
- **策略研究与回测**：量化爱好者基于历史数据验证新策略的有效性，快速迭代优化参数。
- **交易信号辅助**：将Vibe-Trading作为信号生成器，与外部交易系统通过Webhook联动。
- **教育学习**：Python学习者通过阅读项目源码和修改策略脚本，深入理解交易系统设计。

## 项目亮点

- **极低的准入门槛**：相比于其他量化交易框架（如CCXT、Backtrader），Vibe-Trading将复杂的API调用和事件循环封装为一条命令，用户无需编写任何代码即可开始交易。
- **一体化解决方案**：集成了行情采集、策略执行、风控、回测和可视化面板，用户无需拼凑多个工具。
- **全球化社区支持**：项目README已翻译为中、日、韩、阿拉伯等多种语言，降低了非英语用户的使用障碍。
- **高校背景与持续维护**：由香港大学实验室主导开发，代码质量高，依赖管理透明，且定期更新以适配交易所API变动。

## 相关链接

- [GitHub 仓库](https://github.com/HKUDS/Vibe-Trading)
- [Python 包 pypi](https://pypi.org/project/vibe-trading-ai/)
