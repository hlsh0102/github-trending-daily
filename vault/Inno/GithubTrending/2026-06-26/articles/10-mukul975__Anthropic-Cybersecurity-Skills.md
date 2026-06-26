---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-06-26
language: Python
stars_total: 21410
stars_today: 571
---
## 项目概述

Anthropic-Cybersecurity-Skills 是一个面向 AI 代理（Agent）的开源网络安全技能库，目前包含 817 个结构化技能。这些技能覆盖了 29 个安全领域，并映射到 6 个主流安全框架：MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 和 MITRE F3（反欺诈）。项目遵循 agentskills.io 标准，兼容 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多个 AI 平台。

该项目旨在解决一个核心问题：让通用型 AI 代理能够像一名资深安全分析师一样理解、执行和决策安全任务。普通安全分析师掌握的工具知识、战术技能和框架经验，通过本项目的结构化技能库，可以直接注入到 AI 代理的上下文中，从而显著提升 AI 在安全场景中的表现。

项目采用 Apache 2.0 许可证，是一个独立的社区项目，与 Anthropic 公司无官方关联。

## 核心功能

- **817 个结构化安全技能**：覆盖从基础到高级的完整技能链，每个技能都遵循 agentskills.io 标准化格式，可直接被 AI 代理理解和执行。
- **六框架映射**：技能同时映射至 MITRE ATT&CK（攻击行为识别）、NIST CSF 2.0（安全管理）、MITRE ATLAS（AI安全威胁）、D3FEND（防御技术）、NIST AI RMF（AI风险管理）和 MITRE F3（反欺诈）六大标准框架，确保技能的通用性和行业一致性。
- **29 个安全领域全覆盖**：包括威胁情报、漏洞分析、取证分析、安全架构评估、日志分析、云安全、反欺诈等核心领域。
- **多平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 26 种以上 AI 平台和工具链。
- **即用即集成**：无需复杂配置，直接将技能库引入 AI 代理的 prompting 系统即可生效，适合快速集成到现有工作流中。
- **开源可扩展**：遵循 Apache 2.0 开源协议，社区可自由贡献、修改和扩展新的技能。

## 技术架构

该项目本质上是一个**结构化的知识与指令库**，而非传统的软件应用。其核心架构由以下几层构成：

第一层是**技能本体层**，包含 817 个 JSON/YAML 格式化的技能定义文件。每个技能文件遵循 agentskills.io 标准，包含技能名称、描述、输入输出规范、所属安全领域、关联框架标签以及具体执行步骤。

第二层是**框架映射层**，每个技能都通过标签系统关联到上述六个安全框架的具体技术点或控制项。例如，一个关于“恶意软件内存取证”的技能可能在 MITRE ATT&CK 中映射到“T1003.001（凭据转储）”，同时在 D3FEND 中映射到“取证分析”。

第三层是**平台适配层**，项目提供针对不同 AI 代理平台（如 Claude Code、Copilot、Cursor 等）的提示词模板和集成指南，确保技能库能够在不同平台的 prompt 上下文中有效运转。

第四层是**持续更新层**，项目维护一个贡献指南（CONTRIBUTING.md），鼓励社区基于实际安全实践补充新的技能，持续扩展知识库的深度和广度。

项目的设计思路强调“知识即代码”（Knowledge-as-Code），将安全专家的隐性知识显式化、结构化，使其可被机器理解和重复使用。这与传统安全工具不同——不依赖特定运行环境，而是作为 AI 代理的上下文知识注入。

## 安装与使用

该项目无需传统意义上的安装。使用步骤非常简单：

1. 克隆或下载仓库到本地：
   ```bash
   git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
   cd Anthropic-Cybersecurity-Skills
   ```

2. 查看技能列表：进入技能文件夹，可直接浏览 JSON 或 YAML 格式的技能定义文件。

3. 集成到 AI 代理：
   - 对于 Claude Code：将相关技能文件的内容作为 system prompt 的一部分注入，或引用 agentskills.io 标准格式进行加载。
   - 对于 GitHub Copilot 或 Cursor：将技能库放置在项目根目录，或直接引用技能文件路径，AI 会自动索引并应用。
   - 对于其他平台：参考项目文档中“Compatible Platforms”部分，找到对应平台的集成指南。

4. 最小示例：
   假设需要 AI 代理执行“识别恶意进程”的任务，只需在 prompt 中引用对应的技能 ID（例如 `skill-malware-process-detection`），AI 即可按照技能定义的步骤执行：采集进程列表 → 比对已知恶意签名 → 分析异常行为 → 生成报告。

## 适用场景

1. **安全运营中心（SOC）自动化**：将技能库注入安全编排自动化响应（SOAR）系统或 AI 助手，实现自动化告警分析、分类和初步处置决策。

2. **红蓝对抗与渗透测试**：红队或蓝队使用 AI 代理结合技能库，快速生成攻击/防御策略，评估特定基础设施的安全性。

3. **安全培训与知识库**：作为安全新手的“AI 导师”，技能库将资深分析师的知识结构化，帮助初级人员快速掌握标准操作流程（SOP）。

4. **AI 安全评估**：结合 MITRE ATLAS 和 NIST AI RMF 映射的技能，用于评估 AI 系统本身在模型投毒、对抗攻击、数据泄露等方面的脆弱性。

## 项目亮点

- **规模最大**：目前 GitHub 上最大的开源网络安全技能库（817 个技能），覆盖面远超同类项目。
- **框架对齐**：将技能同时挂接到六个主流安全框架，保证了技能的国际标准合规性和广泛适用性，避免“闭门造车”。
- **即插即用**：不需要安装、不需要依赖、不需要修改现有系统，直接作为 AI 代理的上下文使用，集成成本极低。
- **社区驱动**：采用 Apache 2.0 许可证，鼓励社区贡献，确保技能库随着安全威胁生态的演变而持续更新。
- **超强兼容**：支持 26 种以上主流 AI 平台，是目前兼容性最好的安全技能库之一。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [Agentskills 标准](https://agentskills.io)
- [项目贡献指南](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/CONTRIBUTING.md)
