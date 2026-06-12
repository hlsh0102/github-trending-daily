---
tags:
  - trending
  - article
repo: NVIDIA/SkillSpector
date: 2026-06-12
language: Python
stars_total: 2905
stars_today: 319
---
## 项目概述

SkillSpector 是一款专门针对 AI 智能体技能（Skills）的安全扫描工具。随着 Claude Code、Codex CLI、Gemini CLI 等 AI 编程助手的普及，用户可以从社区安装各种技能来增强这些助手的能力。然而，这些技能往往以隐式信任的方式运行，缺乏有效的安全检查机制。研究表明，**26.1% 的 AI 技能存在安全漏洞**，**5.2% 的技能表现出潜在的恶意意图**。SkillSpector 旨在回答一个关键问题："这个技能安装安全吗？"

该项目由 NVIDIA 开源，目标用户包括 AI 开发人员、安全工程师、DevOps 团队以及任何需要安装或使用 AI 智能体技能的个人或组织。通过自动化的安全分析，SkillSpector 帮助用户在安装技能前识别潜在风险，降低供应链攻击和数据泄露的风险。

## 核心功能

- **多格式输入支持**：支持扫描 Git 仓库、URL 链接、ZIP 压缩包、本地目录或单个文件，灵活适配不同使用场景
- **64 种漏洞模式检测**：覆盖 16 大安全类别，包括提示注入（Prompt Injection）、数据泄露（Data Exfiltration）、权限提升（Privilege Escalation）、供应链风险（Supply Chain）、过度代理（Excessive Agency）、输出处理（Output Handling）、系统提示泄露（System Prompt Leakage）、内存污染（Memory Poisoning）、工具误用（Tool Misuse）、流氓代理（Rogue Agent）、触发器滥用（Trigger Abuse）、危险代码（Dangerous Code via AST）、污点跟踪（Taint Tracking）、YARA 签名（YARA Signatures）、MCP 最小权限（MCP Least Privilege）以及 MCP 工具污染（MCP Tool Poisoning）
- **两阶段分析流程**：快速静态分析 + 可选的 LLM 语义评估，兼顾速度与深度
- **实时漏洞查询**：集成 SC4 模块，通过 OSV.dev 实时查询 CVE 数据，并自动离线回退
- **多种输出格式**：支持终端、JSON、Markdown 和 SARIF 报告，便于集成到 CI/CD 流程
- **风险评分系统**：0-100 分的量化评分，附带严重级别标签和明确的安全建议

## 技术架构

SkillSpector 采用模块化的两阶段分析架构。第一阶段为静态分析，通过抽象语法树（AST）解析、YARA 规则匹配和模式识别引擎，快速扫描技能代码中的已知漏洞模式和恶意行为特征。这一阶段的速度极快，适合大规模批量扫描。

第二阶段为可选的 LLM 语义评估，当静态分析发现可疑但难以认定的代码时，可以调用大语言模型进行更深入的上下文理解，判断代码的真实意图。这种"静态分析 + LLM 辅助"的设计平衡了效率与准确性。

项目基于 Python 开发，代码结构清晰，遵循标准的包布局。开发者可以根据[开发指南](docs/DEVELOPMENT.md)扩展分析管道，添加新的检测规则或支持新的技能格式。内置的 SC4 漏洞查询模块采用双模式设计：优先查询在线 OSV 数据库获取最新 CVE 数据，在网络不可用时自动切换至本地离线数据库，确保在任何环境下都能稳定工作。

## 安装与使用

SkillSpector 通过 pip 安装：

```bash
pip install skillspector
```

基本扫描命令：

```bash
# 扫描本地目录
skillspector scan /path/to/skill/directory

# 扫描 Git 仓库
skillspector scan https://github.com/example/malicious-skill.git

# 生成 JSON 格式报告
skillspector scan ./skill.zip --format json --output report.json

# 启用 LLM 语义分析（需要配置 API 密钥）
skillspector scan ./skill --llm --llm-provider openai
```

高级用法示例：

```bash
# 组合多种输出格式
skillspector scan ./skill --format terminal --format markdown --output result.md

# 指定风险阈值，低于阈值的技能视为安全
skillspector scan ./skill --threshold 30

# 扫描并生成 SARIF 报告，用于 CI/CD 集成
skillspector scan ./skill --format sarif --output scan.sarif
```

## 适用场景

- **CI/CD 流水线安全检查**：在自动化构建流程中集成 SkillSpector，每次安装或更新 AI 技能前自动执行安全扫描，阻断恶意技能的部署。
- **AI 技能市场审核**：技能开发者或平台运营方使用 SkillSpector 对上传的技能进行安全审查，确保上架技能不包含已知漏洞或恶意代码。
- **企业内部安全审计**：安全团队定期扫描公司内部使用的所有 AI 技能，生成风险报告，及时发现并修复安全缺口。
- **个人开发者安全验证**：从社区安装 Claude Code 或 Codex CLI 技能前，用 SkillSpector 快速评估风险，避免信任未知来源的代码。

## 项目亮点

与通用安全扫描工具相比，SkillSpector 专为 AI 智能体技能这一新兴攻击面设计，覆盖了提示注入、MCP 工具污染等 AI 特有的安全威胁。其 64 种检测模式覆盖了当前已知的绝大多数技能安全风险类别，且通过分阶段分析架构实现了速度与精度的平衡。

项目集成了实时漏洞数据库查询功能，能够获取最新的 CVE 信息，这在快速演变的 AI 生态中尤为重要。多格式输出支持（尤其是 SARIF 格式）使其能够无缝集成到现有的 DevSecOps 工作流程中。此外，SkillSpector 是完全开源的 Apache-2.0 许可证项目，社区可以自由审计、修改和扩展检测规则。

## 相关链接

- [GitHub 仓库](https://github.com/NVIDIA/SkillSpector)
- [开发指南](docs/DEVELOPMENT.md)
- [OSV.dev 漏洞数据库](https://osv.dev)
