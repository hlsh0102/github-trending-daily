---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-08-18
language: Python
stars_total: 28515
stars_today: 198
---
## 项目概述

Anthropic-Cybersecurity-Skills 是一个面向 AI 代理的开源网络安全技能库，目前收录了 817 个生产级网络安全技能，覆盖 29 个安全领域。该项目由独立开发者 mukul975 创建，并明确声明与 Anthropic 官方无任何关联，是一个社区驱动的独立项目。

项目旨在解决当前 AI 代理在网络安全任务中缺乏标准化、可复用技能组件的问题。它将复杂的网络安全知识体系拆解为结构化的、机器可读的技能单元，使 Claude Code、GitHub Copilot、Codex CLI 等 AI 编程助手能够直接调用这些技能来执行渗透测试、威胁建模、漏洞分析等安全任务。目标用户包括安全工程师、DevOps 团队、AI 应用开发者以及网络安全研究人员。

## 核心功能

- **817 个结构化技能**：每个技能按照 agentskills.io 标准格式定义，包含明确的输入输出描述、执行步骤和预期结果，便于 AI 代理理解与调用。
- **六大框架映射**：技能与 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF、MITRE F3（反欺诈）六个主流安全框架一一对应，帮助用户按框架维度检索和使用技能。
- **29 个安全领域覆盖**：从网络渗透、Web 应用安全、云安全到 AI 安全、欺诈检测、数字取证等，几乎涵盖网络安全的所有重要分支。
- **多平台兼容**：已适配 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 26 个以上的 AI 平台，用户可以在熟悉的开发环境中直接使用。
- **开源与可扩展**：项目采用 Apache 2.0 许可证，完全开源，支持社区贡献新技能和优化现有技能。

## 技术架构

项目以 Python 为主要语言，核心设计理念是"技能即代码"——每个安全技能被定义为一个结构化的、自包含的可执行单元，遵循 agentskills.io 行业标准。这种设计使得技能既可以被 AI 代理动态加载和调用，也可以被人类安全分析师阅读和理解。

在架构层面，项目采用了两层设计：底层是技能库本身，包含按领域和框架分类的 JSON/Markdown 格式技能定义；上层是平台适配层，通过统一的接口协议与不同 AI 平台对接，屏蔽了各平台之间的 API 差异。这种解耦设计使得新增平台支持只需编写对应的适配器，而无需改动技能本体。

框架映射机制是项目的技术亮点之一。每个技能都通过元数据标签关联到一个或多个安全框架的具体战术、技术和流程条目，这使得用户能够基于框架合规需求快速筛选适用技能。技能的版本控制和审核流程也遵循开源社区的成熟实践，确保技能质量。

## 安装与使用

**安装步骤：**

1. 克隆仓库：
   ```bash
   git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
   cd Anthropic-Cybersecurity-Skills
   ```

2. 安装 Python 依赖（如需要）：
   ```bash
   pip install -r requirements.txt
   ```

3. 根据使用的 AI 平台，将技能库路径配置到对应平台的插件或技能目录中。例如在 Claude Code 中，可以将技能目录添加到其技能加载路径。

**最小可用示例：**

以调用一个 Web 漏洞扫描技能为例，在支持 agentskills.io 标准的 AI 代理中，只需通过自然语言指示代理加载对应技能：

```
请加载技能库中针对 OWASP Top 10 中 SQL 注入检测的技能，并对目标 URL https://example.com 执行漏洞扫描。
```

代理会自动查找并执行相匹配的技能定义，返回扫描结果和建议修复措施。用户也可以在支持界面中按框架（如 MITRE ATT&CK）浏览和手动选择技能。

## 适用场景

- **自动化渗透测试**：安全团队可以利用 AI 代理结合技能库，对内部应用和基础设施执行标准化的安全评估，减少人工重复劳动。
- **AI 驱动的安全代码审查**：开发者在提交代码前，让 AI 代理调用安全编码相关技能，自动检查代码中的安全缺陷和合规问题。
- **安全研究与教育**：研究人员和学生可以通过技能库系统性学习各安全框架下的技术与攻防手法，加速知识积累。
- **安全运营响应**：在事件响应过程中，安全分析师可使用代理调用取证分析、日志排查等技能，提升响应速度和准确性。

## 项目亮点

与同类项目相比，Anthropic-Cybersecurity-Skills 最显著的差异化优势在于其**规模与标准化**。817 个技能的体量在开源安全 AI 技能库中处于领先地位，且项目严格对齐 agentskills.io 标准，而非某个特定平台的私有格式，这保证了技能的可移植性和跨平台兼容性。其六大框架映射能力也相对罕见，特别是对 AI 安全（MITRE ATLAS 和 NIST AI RMF）和反欺诈（MITRE F3）的前瞻性覆盖，使其不仅适用于传统网络安全，也适用于 AI 系统安全和业务反欺诈场景。

此外，Apache 2.0 的宽松许可证降低了企业使用的法律门槛，社区的持续贡献机制则保障了技能库的更新活力。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
- [项目贡献指南](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md)
