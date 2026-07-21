---
tags:
  - trending
  - article
repo: diegosouzapw/OmniRoute
date: 2026-07-21
language: TypeScript
stars_total: 22212
stars_today: 1107
---
## 项目概述

OmniRoute 是一个开源的 MIT 协议 AI 网关项目，旨在解决开发者在使用多个 AI 模型时面临的碎片化问题。通过一个统一的端点，OmniRoute 聚合了 268 家以上 AI 供应商（其中 50 家以上提供免费额度）、500 多种模型——覆盖 Claude、GPT、Gemini、Kimi K3、GLM、DeepSeek 等主流模型。项目由 500 多名贡献者共同构建，核心目标是让开发者“永不停止编码”，即通过自动回退、智能配额管理和流量压缩，避免因 API 调用失败或额度耗尽而中断工作流。

目标用户包括使用 Claude Code、Codex、Cursor、Cline 和 Copilot 等 AI 开发工具的开发者，以及需要在多个 AI 模型之间进行灵活路由和成本控制的应用开发者。

## 核心功能

- **统一端点**：单个 API 端点接入 268 多家供应商、500 多种模型，无需为每个供应商分别集成 SDK
- **智能自动回退**：配额感知的自动回退机制，当免费额度用尽或调用失败时自动切换备用供应商，避免中断
- **极致 Token 压缩**：同时应用 RTK（Recursive Tokenization Knowledge）和 Caveman 压缩技术，节省 15%–95% 的 Token 消耗（平均约 89%）
- **免费额度聚合与监控**：聚合 39 个供应商池 / 460 多个模型的有文档记录的免费额度，约 14 亿 Token/月，并通过仪表盘实时显示
- **多协议支持**：支持 MCP（Model Context Protocol）、A2A（Agent-to-Agent）、多模态输入，以及桌面端和 PWA 使用
- **18 种路由策略**：提供丰富的智能路由逻辑，可根据成本、速度、可用性等维度选择最优模型

## 技术架构

OmniRoute 采用 TypeScript 构建，架构设计强调高性能和灵活性：

- **网关模式**：作为单一入口点接收所有 API 请求，然后根据预设路由策略分发到后端供应商，客户端无需修改代码即可切换模型
- **配额感知引擎**：实时追踪每个供应商的配额消耗状态，结合自动回退逻辑，确保在高并发或个别供应商故障时仍能维持服务
- **双层压缩流水线**：首先通过 RTK 算法进行递归式 Token 重编码，再叠加 Caveman 压缩技术，在不损失语义质量的前提下大幅减少传输量
- **模块化路由层**：支持 18 种路由策略，包括成本优先、速度优先、随机、轮询、故障转移等，可通过配置文件动态调整
- **实时仪表盘**：基于 Web 的图形界面展示实时免费额度、调用统计、供应商状态等运营数据，帮助开发者掌握整体运行情况

## 安装与使用

### 安装方式

OmniRoute 支持多种部署方式，推荐 Docker 部署：

```bash
# Docker 一键启动
docker run -d --name omni-route -p 3000:3000 \
  -v ./config.yml:/app/config.yml \
  diegosouzapw/omniroute:latest
```

### 基本配置

创建一个 `config.yml` 文件，指定需要使用的供应商和路由策略：

```yaml
routes:
  - name: "default"
    strategy: "quota-aware-fallback"
    providers:
      - provider: "anthropic"
        api_key: "sk-ant-xxx"
        quota: 1000000
      - provider: "openai"
        api_key: "sk-xxx"
        quota: 500000
      - provider: "google"
        api_key: "AIza-xxx"
```

### 最小可用示例

以 Python 调用为例，只需指向 OmniRoute 端点：

```python
import requests

response = requests.post(
    "http://localhost:3000/v1/chat/completions",
    headers={"Content-Type": "application/json"},
    json={
        "model": "claude-3-opus",
        "messages": [{"role": "user", "content": "Hello! Write a hello world program."}]
    }
)
print(response.json())
```

## 适用场景

- **AI 开发工具集成**：将 Claude Code、Cursor、Cline、Copilot 等工具配置指向 OmniRoute，使其自动利用多个免费额度，避免在编码过程中出现中断
- **多模型 A/B 测试**：需要对比不同模型（如 GPT-4o、Claude 3.5 Sonnet、Gemini Ultra）在相同任务上的表现时，通过 OmniRoute 的路由策略快速切换
- **大规模批处理任务**：利用免费额度聚合和自动回退，以极低成本处理大量文本生成、分类或翻译任务，同时通过压缩技术进一步降低成本
- **研究或副业项目**：个人开发者或小团队通过聚合各供应商的免费额度（月均约 14 亿 Token），无需付费即可运行中型 AI 应用

## 项目亮点

- **免费额度透明度**：首创“诚实预算”计算方式，排除重复计数（如同一供应商池内的不同模型），标注了 15 家存在条款限制的供应商供用户自行判断——并非简单拼凑数字
- **Token 压缩业界领先**：RTK + Caveman 双层压缩实测平均节省 89% Token，远超单一压缩方法的效果
- **供应商覆盖面最广**：268 家供应商、500+ 模型，包括许多小型或地区性供应商，真正实现“一个端点覆盖全局”
- **社区驱动且完全开源**：超过 500 名贡献者，MIT 协议，无任何付费墙或企业版限制
- **与主流开发工具即插即用**：无需修改现有工具代码，只需更改 API 端点地址即可接入 Claude Code、Codex、Cursor、Cline 和 Copilot

## 相关链接

- [GitHub 仓库](https://github.com/diegosouzapw/OmniRoute)
