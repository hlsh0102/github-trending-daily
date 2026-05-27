---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-05-27
language: Python
stars_total: 10216
stars_today: 880
---
## 项目概述

Anthropic Cybersecurity Skills 是一个开源项目，旨在为 AI 代理（Agent）提供结构化、生产级的网络安全技能库。项目包含 **754 个经过精心整理的网络安全技能**，覆盖 **26 个安全领域**，并映射到五个业界主流安全框架。目标用户包括安全分析师、AI/ML 工程师、DevSecOps 从业者以及任何希望利用 AI 代理执行安全任务的开发者。

该项目的核心价值在于：将人类安全专家的知识和经验转化为可被 AI 代理理解和执行的标准化技能，从而显著降低安全自动化门槛，提升安全团队的效率和响应能力。无论你使用 Claude Code、GitHub Copilot、Cursor 还是其他支持代理式交互的 AI 平台，都可以直接调用这些技能。

## 核心功能

- **754 个结构化的安全技能**：涵盖从漏洞扫描、日志分析到威胁狩猎的全领域技能，每个技能均包含清晰的指令和预期输出格式。
- **五框架映射**：技能内容映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 以及 NIST AI RMF 五大框架，确保与行业标准对齐。
- **26 个安全领域全覆盖**：包括但不限于网络取证、恶意软件分析、云安全配置审计、身份与访问管理、容器安全等。
- **跨平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20+ 主流 AI 代理平台。
- **标准化的 agentskills.io 格式**：遵循 agentskills.io 标准，便于社区贡献和技能复用。
- **Apache 2.0 开源许可**：完全免费使用和二次开发，无商业使用限制。

## 技术架构

项目以 Python 为主要实现语言，核心架构围绕“技能定义-框架映射-平台适配”三层设计：

1. **技能定义层**：每个技能是一个 YAML/Markdown 文件，包含技能名称、描述、输入参数（如 IP 地址、哈希值）、执行步骤、预期输出和参考框架映射。这种结构化设计使 AI 代理能够准确理解任务上下文并正确执行。

2. **框架映射层**：通过一套预定义的标签系统，将每个技能关联到 MITRE ATT&CK 的技术类别（Technique ID）、NIST CSF 的功能类别（Identify/Protect/Detect/Respond/Recover）等。映射关系存储在 JSON 索引文件中，便于程序化查询。

3. **平台适配层**：项目提供了 CLI 工具和 API，可将技能库动态注入到不同 AI 代理平台的工作流中。例如，针对 Claude Code 的提示模板会自动包含当前任务所需的安全技能上下文。

设计思路上，该项目强调“可组合性”和“渐进式采用”——用户可以从简单技能（如“检查单个日志条目”）开始使用，逐步组合成复杂的自动化工作流。此外，技能库默认使用 agentskills.io 标准，允许社区贡献的技能无缝集成到任何支持该标准的系统中。

## 安装与使用

### 前提条件
- Python 3.9 或更高版本
- 一个支持本项目的 AI 代理平台（如 Claude Code、GitHub Copilot 等）

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills

# 安装依赖（可选，用于技能管理工具）
pip install -r requirements.txt
```

### 最小可用示例

将技能库引入 Claude Code 会话：

```bash
# 直接将技能目录作为上下文提供给 AI 代理
claude code --context skills/
```

然后在聊天中下达指令：

```
请使用 MITRE ATT&CK T1078（有效账户）相关的技能，检查当前系统是否存在可疑的管理员账户登录行为。输出格式参考该技能的预期输出模板。
```

AI 代理会自动加载技能库中的相关知识，按照结构化步骤执行检查，并输出符合预期的报告。

对于 GitHub Copilot，可以在 `README.md` 或 `.github/copilot-instructions.md` 中添加指向技能库的参考链接，Copilot 在代码编写时会自动参考这些技能上下文。

## 适用场景

1. **安全运营中心（SOC）自动化**：将重复性的告警分析、日志审查任务委托给 AI 代理，代理利用技能库中的标准流程执行操作，减少分析师的手动工作量。

2. **威胁狩猎与取证分析**：安全分析师可以在 AI 代理的帮助下，快速组合多个技能（如内存镜像分析 + 网络流量分析 + YARA 规则扫描）来调查复杂攻击链。

3. **DevSecOps 集成**：在 CI/CD 管道中集成 AI 代理，使用技能库中的安全审计技能自动扫描容器镜像、Kubernetes 配置和基础设施即代码文件，前置发现安全问题。

4. **安全培训与能力测试**：新入职的安全团队成员可以通过技能库了解标准安全操作流程，同时团队可以将技能库作为红蓝对抗或渗透测试的参考工具集。

## 项目亮点

- **规模最大**：目前开源的 AI 代理安全技能库中，754 个技能的覆盖面在最广泛的之列，且通过 5 个框架的映射确保内容的权威性和实用性。
- **框架中立性**：同时支持 MITRE、NIST、D3FEND 多个框架，避免了对单一框架的依赖，适用于不同合规和审计需求的组织。
- **社区驱动**：遵循 agentskills.io 标准，鼓励社区贡献和技能互认，预计随着贡献者增加，技能数量和质量将持续提升。
- **低摩擦接入**：无需复杂的 API 集成，只需将技能库文件提供给 AI 代理即可使用，适合短期项目或概念验证。
- **全方位覆盖**：从基础操作（如 Ping 测试）到高级领域（如 OT 安全、AI 安全审计）均有对应技能，适应不同成熟度的安全团队。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
- [项目官网](https://agentskills.io)
