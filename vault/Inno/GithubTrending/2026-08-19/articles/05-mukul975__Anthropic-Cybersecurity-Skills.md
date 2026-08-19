---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-08-19
language: Python
stars_total: 29270
stars_today: 730
---
## 项目概述

Anthropic-Cybersecurity-Skills 是一个面向 AI 代理的开源网络安全技能库，由社区开发者 mukul975 创建并维护。该项目汇集了 817 个结构化网络安全技能，覆盖 29 个安全领域，是目前规模最大的同类开源资源库。需要特别说明的是，尽管项目名称中包含 "Anthropic"，但它是一个独立的社区项目，与 Anthropic PBC 公司没有任何官方隶属关系。

该项目的核心价值在于将网络安全领域的专业知识转化为 AI 代理可以直接理解和执行的标准化技能模块。这些技能按照 agentskills.io 标准进行结构化组织，使得 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多种主流 AI 开发工具能够直接调用。项目采用 Apache 2.0 许可证，完全开源免费，主要面向安全工程师、DevOps 团队、AI 应用开发者以及安全研究人员。

## 核心功能

- **多框架映射**：所有技能均映射到 6 个主流安全框架，包括 MITRE ATT&CK（攻击技术）、NIST CSF 2.0（风险管理）、MITRE ATLAS（AI 威胁）、D3FEND（防御技术）、NIST AI RMF（AI 风险管理）以及 MITRE F3（反欺诈）。这种映射关系让使用者可以清晰地理解每项技能在行业标准体系中的定位。

- **29 个安全领域覆盖**：从网络渗透测试、恶意软件分析到云安全、身份认证、数据保护、事件响应等，几乎涵盖现代网络安全的全部关键领域。

- **标准化技能格式**：遵循 agentskills.io 标准，每项技能都包含清晰的触发条件、执行步骤、输入输出定义和预期结果，确保 AI 代理能够准确理解并执行。

- **多平台兼容**：支持 20 多种主流 AI 开发平台和工具，包括 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等，具有良好的跨平台迁移能力。

- **结构化分类体系**：技能按安全框架和领域双重维度组织，使用者可以通过框架映射或领域分类快速定位所需技能。

## 技术架构

项目的技术核心在于其标准化的技能描述语言。每项技能遵循 agentskills.io 规范，采用 YAML 或类似结构化格式定义，包含技能名称、描述、使用场景、所需参数、执行流程和输出格式等元数据。这种设计使得技能不依赖特定的 AI 模型或平台，任何支持该标准的工具都能识别和执行。

框架映射机制是项目的另一大技术亮点。项目团队将 MITRE ATT&CK、NIST CSF 2.0 等大型安全框架的条目逐一对应到具体的技能定义中，形成了一个覆盖攻击链全阶段的技能图谱。例如，一个针对 MITRE ATT&CK 中 "T1059 Command and Scripting Interpreter" 技术的技能，会包含检测命令注入、脚本执行监控、日志分析等具体操作步骤。

项目的底层使用 Python 构建，提供了完善的技能管理和调用接口。技能库的版本控制通过 Git 实现，便于社区协作和持续更新。

## 安装与使用

安装过程非常简单，只需将仓库克隆到本地即可：

```bash
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

在支持 agentskills.io 标准的 AI 工具（如 Claude Code）中，通过配置文件指定技能库路径，即可实现技能的自动加载和调用。假设你使用 Claude Code，可以在设置中添加：

```yaml
skills:
  - source: local
    path: ./Anthropic-Cybersecurity-Skills/skills
```

之后，向 AI 代理发出安全相关的自然语言指令，它将自动匹配并执行对应的技能。例如，当您提出"分析这份 pcap 文件中是否存在 SQL 注入特征"时，代理会调用网络流量分析技能和 SQL 注入检测技能进行协同处理，并按技能定义的格式返回结构化结果。

## 适用场景

- **安全自动化测试**：DevSecOps 团队可以借助该技能库，让 AI 代理自动执行漏洞扫描、配置核查、渗透测试等安全任务，显著提升 CI/CD 流水线中的安全自动化水平。

- **安全运营中心（SOC）增强**：安全分析师可以将日常告警处理、日志分析、威胁狩猎等任务委托给 AI 代理，通过技能库中标准化的响应流程提高工作效率和一致性。

- **安全培训与演练**：安全团队可以利用技能库中的红队/蓝队技能，构建真实的攻防对抗模拟环境，用于内部安全培训和应急响应演练。

- **AI 驱动的安全研究**：研究人员可以使用该技能库作为数据源，训练自己的安全专用 AI 模型，或者基于框架映射关系进行安全技术关联分析。

## 项目亮点

该项目的差异化优势主要体现在三个维度。首先是规模的全面性：817 个技能、29 个领域、6 个框架映射，使其成为目前最大的开源安全技能库，几乎可以覆盖各种常见的安全任务需求。其次是标准化程度高：严格遵循 agentskills.io 标准，确保技能可以在不同平台间无缝迁移，避免了技术架构锁定。最后是框架对齐的严谨性：项目将技能与 MITRE ATT&CK、NIST CSF 2.0 等权威框架逐一对应，让使用者能够清晰地知道每项技能在行业标准体系中的定位和适用边界，这在同类项目中十分罕见。

此外，项目还采用了双用途技术的合规化处理——虽然包含红队渗透等攻击性安全技能，但通过明确的法律授权声明和 Apache 2.0 许可约束，强调仅限授权与合法场景使用，体现了负责任的社区治理态度。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
