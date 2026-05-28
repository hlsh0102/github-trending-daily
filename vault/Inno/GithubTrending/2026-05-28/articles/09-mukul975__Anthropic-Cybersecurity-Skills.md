---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-05-28
language: Python
stars_total: 11170
stars_today: 886
---
## 项目概述

Anthropic Cybersecurity Skills 是一个为 AI 智能体设计的、开源的结构化网络安全技能库。该项目提供了 754 个经过验证的网络安全技能，覆盖 26 个安全领域，并映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 和 NIST AI RMF 五大权威安全框架。主要解决当前 AI 智能体在网络安全任务中缺乏专业、结构化安全知识的问题，目标用户包括安全分析师、AI 开发者、DevOps 团队以及任何希望将 AI 驱动自动化引入安全运营的专业人员。

## 核心功能

*   **754 个生产级技能**：每个技能都是可直接应用于实际安全场景的结构化指令，涵盖从威胁检测到事件响应的全过程。
*   **五框架映射**：技能同时映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 和 NIST AI RMF，确保与主流安全标准兼容。
*   **26 个安全领域全覆盖**：覆盖端点安全、网络分析、云安全、恶意软件分析、数字取证、身份管理、漏洞研究、AI 安全等关键领域。
*   **多平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 26 个以上主流 AI 开发平台和工具。
*   **agentskills.io 标准格式**：采用标准化的技能描述格式，便于不同 AI 智能体理解和执行，降低集成门槛。
*   **Apache 2.0 开源许可**：完全开源，允许商业使用、修改和再分发，鼓励社区贡献和生态建设。

## 技术架构

项目采用模块化、框架对齐的设计思路。核心架构围绕“技能”这一基本单元构建，每个技能包含：技能 ID、所属领域、框架映射（如 MITRE ATT&CK 中的技术编号）、适用平台列表、结构化指令和示例提示。技能以 JSON 文件形式存储，便于程序化加载和处理。项目使用 Python 编写辅助工具，支持技能验证、格式转换和批量导入主流 AI 平台的工作流。设计上强调“即插即用”——用户无需深度修改 AI 智能体即可引入这些技能，降低了安全自动化的准入门槛。

## 安装与使用

**基本安装步骤：**

1.  克隆仓库：
    ```bash
    git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
    cd Anthropic-Cybersecurity-Skills
    ```

2.  查看可用技能列表（可选）：
    ```bash
    ls skills/
    ```

3.  将技能集成到你的 AI 工作流中：
    - 对于支持 agentskills.io 标准的平台（如 Claude Code），可直接将技能目录添加到平台配置中。
    - 对于自定义集成，可使用项目提供的 Python 脚本将技能解析为平台所需的格式。

**最小可用示例：**

假设你使用 Claude Code，可简单将仓库中的技能文件作为上下文附加：

```bash
claude-code --context skills/threat_detection/domain_analysis.json
```

之后，AI 智能体便能在对话中直接调用该技能描述的结构化知识和操作方法。

## 适用场景

*   **安全事件响应自动化**：AI 智能体在收到告警后，自动根据技能库中的响应预案执行取证、分析和处置步骤，大幅缩短 MTTR（平均修复时间）。
*   **威胁情报分析**：分析师可让 AI 智能体基于 MITRE ATT&CK 映射的技能，快速关联攻击技术、识别模式并生成报告。
*   **安全工具链集成与编排**：团队成员将技能库作为 SOAR（安全编排自动化与响应）平台的知识层，让 AI 智能体统一调度不同安全工具。
*   **安全培训与能力评估**：新人可通过浏览技能库快速掌握安全分析的标准流程，企业也可评估 AI 智能体在不同领域的安全能力覆盖情况。

## 项目亮点

与同类项目相比，Anthropic Cybersecurity Skills 的差异化优势在于：**规模最大**（754 个技能）、**框架最全**（同时覆盖五大权威框架）、**平台最广**（支持 26+ 主流 AI 平台），并且是完全开源、社区驱动的项目。它不是一个封闭的私有知识库，而是一个开放的标准，任何人都可以贡献、改进和扩展。项目还特别关注 AI 安全领域（NIST AI RMF、MITRE ATLAS），这是其他安全技能库普遍缺失的部分。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [项目官网 agentskills.io](https://agentskills.io)
- [贡献指南](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md)
