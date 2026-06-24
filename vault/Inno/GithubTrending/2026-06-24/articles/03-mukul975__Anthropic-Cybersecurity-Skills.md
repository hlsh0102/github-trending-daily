---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-06-24
language: Python
stars_total: 19997
stars_today: 1041
---
## 项目概述

Anthropic Cybersecurity Skills 是目前最大的开源网络安全技能库，专为 AI 智能体设计。该项目提供了 817 个结构化的网络安全技能，覆盖 29 个安全领域，并映射到 6 个主流安全框架。目标用户包括安全分析师、AI 开发者、DevSecOps 工程师，以及任何希望通过 AI 智能体自动化网络安全工作流的团队。项目遵循 agentskills.io 标准，兼容 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多个 AI 平台。

## 核心功能

- **817 个生产级安全技能**：每个技能都是结构化的、可执行的指令，覆盖从威胁狩猎到事件响应的全链条安全操作
- **6 框架映射**：技能同时映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 和 MITRE F3（反欺诈）框架，便于与现有安全控制框架集成
- **29 个安全领域全覆盖**：包括端点安全、网络分析、日志分析、云安全、AI 安全、逆向工程、恶意软件分析、取证分析、漏洞研究、红队操作等
- **跨平台兼容**：支持 20+ 个 AI 开发平台和 CLI 工具，包括 Claude CLI、GitHub Copilot CLI、Codex CLI、Gemini CLI、Cursor 等
- **结构化技能描述**：每个技能包含场景说明、输入输出格式、执行步骤和预期结果，降低 AI 智能体执行安全任务的门槛
- **Apache 2.0 开源许可**：完全开源，可自由使用、修改和分发，适合企业内部分发和商业化集成

## 技术架构

项目采用以技能为中心的架构设计。核心是 agentskills.io 标准定义的技能描述格式，每个技能是一个包含以下要素的结构化文本块：技能名称、适用场景、输入参数、执行步骤、预期输出、相关框架映射和风险说明。技能以 YAML 或 JSON 格式存储，便于解析和动态加载。

设计上遵循模块化和可组合原则——单一技能专注于一个原子安全操作，多个技能可以通过 AI 智能体的推理能力组合成复杂的工工作流。例如，“检测异常 PowerShell 执行”技能可以与“提取内存取证数据”技能串联，形成完整的攻击链分析能力。

项目本身不依赖特定运行时或语言，但推荐使用 Python 3.9+ 进行技能库的管理、验证和自定义开发。技能库的版本控制通过 Git 管理，每次更新都保持与最新框架版本的同步。

## 安装与使用

### 安装

```bash
# 克隆仓库
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills

# （可选）安装 Python 依赖，用于技能验证和工具辅助
pip install -r requirements.txt
```

### 最小可用示例

1. 将技能库加载到你的 AI 智能体配置中。以 Claude Code 为例：

```bash
# 将技能目录添加到 Claude Code 的工具上下文
claude code --tools ./skills/
```

2. 使用一个简单技能。例如，查找与“日志分析”相关的技能：

```bash
# 通过 CLI 查询技能库
python scripts/search_skills.py --domain "log_analysis"
```

3. 在 AI 对话中直接引用技能：

```
用户：请使用 `skills/edr/suspicious_process_creation.yaml` 技能分析以下进程列表...
```

更详细的使用示例请参考 `examples/` 目录和项目的 `QUICK_START.md`。

## 适用场景

- **自动威胁狩猎**：安全运营团队可以将技能库集成到 SIEM 或 SOAR 系统中，让 AI 智能体自动执行 MITRE ATT&CK 覆盖的 800+ 种攻击检测和分析任务，减少人工分析时间
- **AI 驱动的安全开发**：DevSecOps 工程师使用技能库指导 AI 代码助手（如 GitHub Copilot）在开发过程中识别安全漏洞、生成安全补丁、检查配置错误
- **红蓝队演练自动化**：红队使用技能库自动化攻击模拟和渗透测试步骤，蓝队则利用技能库自动执行防御措施验证和事件响应流程
- **AI 安全研究**：研究人员可以利用技能库快速对比不同框架（如 NIST CSF 与 MITRE ATT&CK）对同一安全能力的定义差异，或测试不同 AI 智能体在安全任务上的表现

## 项目亮点

- **规模最大**：817 个技能是目前公开可用的最大结构化网络安全技能库，覆盖范围远超同类项目
- **框架对齐**：同时对齐 6 个主流安全框架，这是独一无二的设计——一个技能库可同时满足合规、审计和运营多种需求
- **平台无关**：不绑定特定 AI 平台或安全工具，用户可以在任何支持 agentskills.io 标准的环境中自由切换
- **社区驱动**：作为社区项目，持续接收贡献，保持与最新威胁情报和框架更新的同步，同时也保持独立性和中立性

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
- [项目贡献指南](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md)
