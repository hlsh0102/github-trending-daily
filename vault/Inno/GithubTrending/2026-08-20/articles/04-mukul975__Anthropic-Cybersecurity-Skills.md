---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-08-20
language: Python
stars_total: 29901
stars_today: 766
---
## 项目概述

Anthropic-Cybersecurity-Skills 是目前开源社区中规模最大的、专为 AI Agent 设计的网络安全技能库。该项目由独立开发者 mukul975 创建，包含 **817 个生产级网络安全技能**，覆盖 29 个安全领域，并系统性地映射到 6 个主流安全框架。尽管项目名称中含有 "Anthropic"，但这是一个完全独立的社区项目，与 Anthropic PBC 公司无任何关联。

该项目解决的核心问题是：AI 编程助手（如 Claude Code、GitHub Copilot）在安全领域的应用中，缺乏结构化的专业知识库。开发者或安全分析师虽然可以使用 AI 辅助进行安全分析，但 AI 模型本身并不内置完整的攻防知识体系。这个技能库以 `agentskills.io` 标准格式封装了从威胁检测到漏洞修复、从红队操作到合规审计的全链路技能，使 AI Agent 能够调用这些技能来执行具体的安全任务。

项目目标用户包括安全工程师、DevSecOps 团队、红队/蓝队成员、安全研究员，以及所有希望借助 AI 提升安全工作效率的开发者。

## 核心功能

- **29 个安全领域全覆盖**：涵盖网络威胁情报、漏洞分析、恶意软件研究、事件响应、数字取证、安全配置审计、身份与访问管理、云安全、应用安全等方向，每个领域包含数十个细粒度技能。
- **6 大安全框架映射**：技能分别对应 MITRE ATT&CK（攻击战术知识）、NIST CSF 2.0（网络安全框架）、MITRE ATLAS（AI 系统威胁）、D3FEND（防御对抗）、NIST AI RMF（AI 风险管理）和 MITRE F3（反欺诈），便于安全团队将技能与既有合规要求对齐。
- **多平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20+ 主流 AI 编程平台，技能以标准格式打包，即插即用。
- **生产级技能质量**：每个技能均经过结构化设计，包含明确的输入参数、执行流程和输出格式，而非简单的提示词模板，可直接用于自动化安全任务。
- **Apache 2.0 开源许可**：完全免费商用，允许自由修改和分发，企业可基于此构建私有安全知识库。

## 技术架构

项目采用基于 `agentskills.io` 标准格式的技能定义方式。每个技能是一个独立的文件夹，内部包含 `SKILL.md` 标记文件，该文件遵循特定的 YAML frontmatter 结构和自然语言指令描述。这种设计使得技能既可以被 AI 模型的系统提示解析，也可以被外部工具链读取。

技能库的组织方式采用双层分类结构：第一层按安全领域（如 `incident-response`、`threat-intel`）划分，第二层在领域内按具体任务切分。每个技能文件内不仅有操作步骤，还嵌入了与 MITRE ATT&CK 等技术图谱的映射关系，例如某个钓鱼邮件分析技能会标注其对应的 ATT&CK 战术 ID（如 TA0001 Initial Access）和 D3FEND 对抗技术（如 Email Analysis）。

鉴于项目使用 Python 生态，其工具链也以 Python 为主，提供技能校验脚本和元数据生成器，用于确保所有技能文件符合 agentskills.io schema 规范。技能本身为纯文本/标记文件，不依赖运行时环境，因此可以在任意支持文件读取的 AI Agent 中运行。

## 安装与使用

**安装步骤：**

1. 克隆仓库：
   ```bash
   git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
   cd Anthropic-Cybersecurity-Skills
   ```

2. 查看技能目录结构：
   ```bash
   ls skills/
   # 输出示例：appsec/  cloud-security/  forensics/  threat-intel/  ...
   ```

3. 将技能目录路径告知你的 AI Agent。以 Claude Code 为例，在配置中指定技能路径：
   ```bash
   claude --skills-path ./skills
   ```

**最小可用示例：**

假设你希望 AI 辅助分析一份可疑的 PCAP 文件。在支持技能加载的 Cursor 或 Codex 中，只需在对话中触发：

```
请使用 network-traffic-analysis 技能分析 sample.pcap，提取可疑的 C2 通信特征。
```

AI 将从技能库中匹配对应的技能文件夹（如 `skills/network-traffic-analysis/SKILL.md`），自动加载其中定义的分步分析流程、所需工具（如 tshark、Zeek）以及输出模板，然后执行并返回结构化报告。

## 适用场景

- **红队与渗透测试**：安全测试人员可让 AI 基于 MITRE ATT&CK 映射的技能，快速生成针对特定目标的攻击路径枚举、payload 构造建议，并输出符合规范的测试报告。
- **安全运营中心（SOC）事件响应**：当发生安全告警时，分析师可利用 `incident-response` 领域技能，让 AI 按照 NIST CSF 2.0 Respond 阶段的标准流程执行日志分析、威胁定性、遏制建议，缩短平均响应时间。
- **AI 安全的合规审计**：面向使用大模型的企业，项目中的 MITRE ATLAS 与 NIST AI RMF 映射技能，可用于指导 AI 系统上线前的安全评估、对抗性攻击测试（提示注入、模型窃取等），辅助完成合规文档编写。
- **安全产品开发中的知识注入**：开发者可将技能库作为微调数据集或 RAG 检索源，为自己的安全产品（如 SIEM 查询生成器、漏洞扫描器）注入专家级决策逻辑。

## 项目亮点

与同类开源项目（如单个安全工具的提示词集合或小型 skill 库）相比，该项目的差异化优势显著：

1. **规模与系统性**：817 个技能远超同类仓库，且不是零散文件的堆砌，而是经过结构化设计、按领域分类、并横向映射到 6 个权威框架的系统工程。
2. **标准驱动的互操作性**：遵循 agentskills.io 通用标准，而非绑定特定 AI 厂商的私有格式，这意味着技能库可以跨平台复用，不因工具迁移而失效。
3. **合规对齐的实用性**：MITRE ATT&CK 与 NIST CSF 的映射并非标签式点缀，而是深入到技能执行步骤的每个环节，真正帮助安全团队将 AI 能力纳入现有的合规管理体系中。
4. **活跃的社区生态**：项目拥有近 3 万 Star 且日增数百，充分验证了社区对高质量安全知识库的强烈需求，持续贡献机制也保证了技能的时效性。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准文档](https://agentskills.io)
- [MITRE 官方欺诈框架（F3）](https://ctid.mitre.org/fraud/)
