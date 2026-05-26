---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-05-26
language: Python
stars_total: 9518
stars_today: 1004
---
## 项目概述

Anthropic Cybersecurity Skills 是目前开源社区中规模最大的 AI 智能体网络安全技能库。项目包含 754 个结构化、可直接投入生产的网络安全技能，并已映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 和 NIST AI RMF 五大权威安全框架。它解决了当前 AI 安全助手在实际应用中缺乏标准化安全知识、无法按框架执行任务的问题。目标用户包括安全分析师、DevSecOps 工程师、AI 开发者以及任何希望为 AI 智能体赋予专业安全能力的团队或个人。

## 核心功能

- **754 个结构化安全技能**：覆盖从内存取证、日志分析到云安全配置等全流程安全操作，每个技能都包含明确的指令和上下文。
- **五大框架映射**：技能与 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 精准对齐，便于合规审计和标准化任务。
- **26 个安全领域覆盖**：涉及恶意软件分析、网络监控、身份与访问管理、漏洞研究、云安全等多个专业方向。
- **跨平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多种主流 AI 开发平台和代理工具。
- **agentskills.io 标准**：遵循开源 agentskills.io 技能格式，确保技能可被不同 AI 代理系统一致理解和执行。
- **Apache 2.0 开源许可**：完全免费商用，社区可自由贡献和扩展。

## 技术架构

项目采用模块化 YAML 文件结构存储每个技能。每个技能文件包含三个核心部分：元数据（技能 ID、名称、所属框架和领域）、触发条件（描述何种情境下该技能应被调用）和执行步骤（具体操作指令或脚本引用）。这种设计使得 AI 智能体可以基于自然语言输入自动匹配最相关的技能并执行。技能库与代理平台解耦，通过 agentskills.io 标准接口实现即插即用——无论底层是 Claude、GPT 还是 Gemini，技能都能以相同方式工作。映射到五大框架的逻辑通过预定义的标签系统实现，每个技能至少关联一个框架 ID 和攻击/防御阶段。Python 语言主要用于技能验证脚本和自动化生成工具，确保技能格式正确且可被解析。

## 安装与使用

### 快速开始

```bash
# 克隆仓库
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

将技能目录注册到你的 AI 代理平台中。以 Claude Code 为例：

```bash
# 在 Claude Code 中使用技能路径
claude config --skill-path ./skills
```

然后向 AI 输入实际安全任务，例如：“分析这个内存镜像并查找潜在的恶意进程”。AI 会自动检索匹配的技能（如 Volatility3 分析技能），并执行对应步骤。

### 最小可用示例

直接使用任何与 AI 平台的集成方式，将仓库中的 `skills/` 目录作为技能源。例如在 GitHub Copilot 的 `settings.json` 中：

```json
{
  "github.copilot.advanced": {
    "skillDirectories": ["path/to/Anthropic-Cybersecurity-Skills/skills"]
  }
}
```

然后打开一个安全相关文件（如 `.pcap` 或日志文件），Copilot 将自动根据框架映射提供上下文相关的技能建议。

## 适用场景

- **安全运营中心（SOC）自动化**：7×24 小时监控日志、事件响应，AI 代理根据 MITRE ATT&CK 框架自动执行分析、取证和阻断操作。
- **渗透测试与红队演练**：AI 代理在授权环境下自动执行漏洞扫描、利用和报告生成，技能映射确保步骤可追溯。
- **合规与安全审计**：基于 NIST CSF 2.0 框架的自动评估，AI 代理核对控制项并生成差距分析报告。
- **AI 安全培训与辅助**：安全分析师新人通过向 AI 询问“如何检测横向移动”，即可获得框架对齐的标准化操作步骤。

## 项目亮点

与同类项目相比，Anthropic Cybersecurity Skills 最显著的优势在于规模与标准化：754 个技能是目前最大规模的开源安全技能库，且全部对齐五大权威框架。许多竞品只覆盖单一框架（如只做 MITRE ATT&CK）或技能数量不足 200 个。此外，项目采用跨平台设计，不锁定任何 AI 供应商，用户可以在不同代理工具间无缝迁移技能。agentskills.io 标准确保了技能的互操作性，而 Apache 2.0 许可降低了企业商用门槛。最后，项目持续社区驱动，24 小时内获得超 1000 星标，反映出安全从业者在 AI 辅助工作流中对标准化技能库的迫切需求。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
