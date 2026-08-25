---
tags:
  - trending
  - article
repo: Alishahryar1/free-claude-code
date: 2026-08-25
language: Python
stars_total: 49105
stars_today: 891
---
## 项目概述

Free Claude Code（FCC）是一个开源的命令行工具，旨在让开发者免费使用 Claude Code、Codex、Pi 和 OpenCode 等主流 AI 编程助手，无需承担高昂的订阅费用。该项目聚合了超过 50 家符合服务条款（ToS）的模型提供商，每月可提供高达 13 亿以上的免费 Token，使用户能够在终端、IDE、应用甚至手机上，通过统一的界面访问免费、付费、订阅及本地模型。

该项目目前已在 GitHub 上获得超过 49,000 颗星标，活跃度极高。它由独立开发者维护，与 Anthropic 官方无任何关联，但完全兼容 Anthropic 官方 Claude Code 工具链。项目采用 MIT 许可证，完全免费开源。

## 核心功能

- **多模型统一访问**：在一个简洁的命令行界面中，统一搜索并调用来自 50+ 提供商的模型，涵盖免费、付费、订阅和本地推理模型，无需切换多个工具。
- **多智能体支持**：原生支持 9 种主流编码智能体，包括 Claude Code、OpenAI Codex、Pi、OpenCode、Cline、Hermes 等，用户可根据任务需求选择最合适的智能体。
- **Voice 语音支持**：内置语音交互能力，允许用户通过语音指令驱动编码助手，提升无障碍性和操作效率。
- **服务条款友好**：项目严格遵循各模型提供商的条款，自动移除不再被允许的集成，确保用户账号安全，避免因滥用服务而面临封禁风险。
- **跨平台接入**：不仅支持桌面终端，还提供 API 接口和移动端适配，用户可通过 IDE 插件或手机远程调用同一套模型目录。
- **统一模型目录**：提供可搜索的模型库，支持按提供商、模型类型、价格和上下文长度等条件筛选，方便用户快速定位最佳模型。

## 技术架构

Free Claude Code 基于 Python 构建，充分利用了 Python 生态系统中的高效工具链。项目的核心设计理念是“适配器模式”与“统一抽象层”：

- **提供商适配层**：每个模型提供商都实现为一个独立的适配器模块，负责处理认证、速率限制、格式转换等细节。新增提供商只需实现标准接口，无需修改核心逻辑。
- **智能体桥接层**：通过专门设计的桥接协议，将不同编码智能体（如 Claude Code 与 Codex）的 API 差异封装起来，向上提供统一的调用接口。
- **CLI 与 TUI 分离**：核心逻辑与命令行界面解耦，便于嵌入到 IDE（如 VS Code、JetBrains）或通过 REST API 暴露给其他应用。
- **依赖管理**：使用 `uv`（极速 Python 包管理器）进行依赖安装和虚拟环境管理，结合 `ruff` 进行代码规范检查，`pytest` 用于自动化测试，确保项目质量。
- **日志与监控**：采用 `loguru` 库提供清晰的日志输出，便于开发者诊断连接问题或排查 Token 消耗异常。

## 安装与使用

Free Claude Code 的安装过程非常简单，推荐使用 Python 3.10+ 环境。最快捷的方式是通过 `uv` 工具：

```bash
# 安装 uv（若未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 使用 uv 直接运行 FCC
uvx free-claude-code
```

或者通过 pip 安装：

```bash
pip install free-claude-code
fcc --install
```

安装完成后，首次运行需要选择一个模型提供商并配置 API 密钥。FCC 提供了交互式向导：

```bash
# 启动交互式配置
fcc setup

# 选择一个免费提供商（如 Groq、Cerebras 等）
# 按照提示粘贴你的 API Key

# 连接 Claude Code
fcc connect claude-code
```

最小可用示例：配置完成后，直接在终端运行编码智能体：

```bash
# 使用 Claude Code
fcc run claude-code "帮我写一个 Python 快速排序函数"

# 使用 Codex CLI
fcc run codex "解释一下这段代码的复杂度"

# 使用语音输入
fcc --voice "重构这个项目中的数据库连接池"
```

## 适用场景

- **个人开发者高频使用**：在预算有限的情况下，开发者可以充分利用每月 13 亿+ 免费 Token 进行日常编码、代码审查、单元测试生成等，大幅降低工具成本。
- **多模型对比与切换**：AI 研究者和提示工程师需要频繁对比不同模型（如 Claude 与 GPT-4o）的输出效果。FCC 的统一界面让比较变得极其高效。
- **离线与私有部署环境**：在企业内网或隐私敏感环境中，用户可以通过 FCC 连接本地推理服务器（如 Ollama），享受本地模型的隐私优势，同时保留统一的 CLI 体验。
- **移动端与远程开发**：通过 API 接口，用户可以在手机 SSH 到远程开发机，结合语音功能，在通勤途中或不便打字时完成简单的编码任务和问题排查。

## 项目亮点

与同类工具相比，Free Claude Code 的差异化优势显著：

1. **真正的免费额度**：许多“免费”工具依靠按次广告或限制速度，而 FCC 聚合的是各大云厂商的真实免费层（如 Groq、OpenRouter 等），每月 Token 额度充裕且可持续。
2. **ToS 优先的安全设计**：项目主动关注条款变更，一旦某个提供商不再允许免费使用，会立即移除并推荐替代品。这种对用户账号安全的重视在同类项目中非常罕见。
3. **语音原生支持**：不是简单的第三方语音插件，而是深度集成语音到命令的转换，支持自然语言操作多个智能体，显著降低使用门槛。
4. **极低的使用门槛**：得益于 `uv` 的一键安装和交互式配置向导，从零到可以运行 Claude Code 的时间不超过两分钟，无需手动管理多个 Python 环境。

## 相关链接

- [GitHub 仓库](https://github.com/Alishahryar1/free-claude-code)
- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [OpenCode 项目主页](https://github.com/anomalyco/opencode)
