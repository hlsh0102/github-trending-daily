---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-06-23
language: Python
stars_total: 18944
stars_today: 956
---
## 项目概述

Anthropic Cybersecurity Skills 是一个为 AI 代理（AI Agent）提供结构化网络安全技能的开源项目，包含 817 条经过生产环境验证的技能指令。该项目由社区创建，独立于 Anthropic PBC，旨在让任何 AI 代理都能具备资深安全分析师级别的专业知识。项目以 agentskills.io 标准为基准，适用于 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 以及 20 多个主流 AI 平台。

该项目解决的核心问题是：如何让通用 AI 代理在网络安全领域具备可靠、准确且可复用的专业能力。通过将安全分析师多年的经验、工具使用方法和框架知识结构化为标准指令，任何 AI 代理都可以立即获得这些能力，无需从零开始学习或训练。

## 核心功能

- **817 条生产级技能指令**：每条技能都经过精心设计，覆盖从漏洞分析到事件响应、从恶意软件逆向到合规审计的完整安全操作流程。
- **6 大安全框架映射**：所有技能均映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 和 MITRE F3（Fight Fraud）等主流框架，方便用户按框架组织工作流。
- **29 个安全领域覆盖**：包括威胁情报、取证分析、红队操作、漏洞管理、云安全、AI 安全、欺诈检测等完整领域。
- **跨平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Curson、Gemini CLI 等 20+ 主流 AI 平台，一次导入即可使用。
- **agentskills.io 标准格式**：遵循行业标准指令格式，确保技能在不同代理之间具有一致的行为和输出质量。
- **Apache 2.0 开源许可**：完全免费使用，允许商业集成和二次开发。

## 技术架构

项目基于 YAML 文件组织技能定义，每条技能包含唯一标识符、描述、输入参数、输出格式和关联框架。核心技术特点包括：

- **模块化技能设计**：每条技能独立，包含完整的上下文上下文和约束条件，确保 AI 代理在调用时能够准确理解任务边界。
- **框架映射层**：每条技能关联多个框架的战术和技术 ID，支持跨框架检索和组合，例如一个技能可以同时映射到 MITRE ATT&CK 的某个技术和 NIST CSF 的某个函数。
- **平台适配层**：提供统一的技能接口，底层适配不同 AI 平台的调用方式（如 Anthropic 的 tools API、OpenAI 的 function calling 等），用户无需关心平台差异。
- **版本控制与贡献机制**：项目采用 Git flow 管理技能迭代，社区贡献者可以提交新技能或优化现有技能，经过评审后合并到主干。

## 安装与使用

### 快速开始

1. 克隆仓库：
```bash
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

2. 查看技能目录：
```bash
ls skills/
# 输出示例：threat_intel/ forensics/ red_team/ cloud_security/ ai_security/ ...
```

3. 在 AI 代理中加载技能：
```python
# 示例：使用 Python 加载并调用一个威胁情报技能
from anthropic import Anthropic

with open("skills/threat_intel/ip_reputation.yaml") as f:
    skill_yaml = f.read()

client = Anthropic()
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    tools=[{"type": "yaml", "content": skill_yaml}],
    messages=[{"role": "user", "content": "分析 IP 地址 8.8.8.8 的威胁情报"}]
)
```

4. 在 Claude Code 中使用：
```bash
# 直接引用技能路径
claude code --skills ./skills/forensics/volatility_analyze.yaml
```

### 最小可用示例

以恶意软件分析技能为例：
- 技能文件：`skills/malware_analysis/static_analyze.yaml`
- 功能：对 PE 文件进行静态分析，提取导入表、字符串、资源等
- 调用后 AI 代理会自动输出格式化的分析报告，包含 IOCs 和建议

## 适用场景

- **安全运维自动化**：在 SOC（安全运营中心）中，AI 代理可以自动处理告警、执行取证、生成事件响应建议，大幅减少分析师重复劳动。
- **红队演练与渗透测试**：红队成员可以快速调用特定攻击技术模拟、漏洞验证或权限提升技能，提高工作效率和准确性。
- **安全培训与考核**：安全团队可以基于这些技能构建交互式培训场景，让新人在 AI 引导下完成实际安全操作任务。
- **合规审计与报告**：自动调用 NIST CSF 或 MITRE ATT&CK 映射的技能，生成组织安全态势评估报告和合规性证据。

## 项目亮点

- **最大开源网络安全技能库**：817 条技能是同类项目中规模最大的，且全部经过生产环境验证。
- **多框架兼容性**：同时映射 6 个主流框架，覆盖传统安全、AI 安全和反欺诈领域，这是许多单框架项目无法比拟的。
- **平台无关性**：不绑定特定 AI 平台或工具，真正实现“一种技能，随处可用”。
- **社区驱动**：项目活跃维护，接受社区贡献，用户可以直接参与技能优化和扩展。
- **易用性优先**：技能以标准化 YAML 文件提供，任何开发者都可以理解和使用，无需学习自定义 DSL。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
- [MITRE ATT&CK 框架](https://attack.mitre.org/)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
