---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-05-26
language: Python
stars_total: 9687
stars_today: 1004
---
## 项目概述

Anthropic-Cybersecurity-Skills 是一个开源知识库，为 AI 代理（如 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等）提供 754 个结构化的网络安全技能。该项目遵循 [agentskills.io](https://agentskills.io) 标准，将这些技能映射至 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 和 NIST AI RMF 五大主流安全框架，覆盖 26 个安全领域。

项目旨在解决 AI 代理在网络安全任务中缺乏系统化、标准化技能指引的问题——传统安全工具依赖人工操作或硬编码脚本，而 AI 代理需要明确的知识边界和框架对齐才能有效执行检测、分析、防护等任务。目标用户包括安全工程师、AI 开发人员、红蓝队成员、合规分析师以及任何希望利用 AI 代理提升安全运营效率的团队。

## 核心功能

- **框架映射**：754 项技能全部映射至 MITRE ATT&CK（入侵检测）、NIST CSF 2.0（网络安全框架）、MITRE ATLAS（AI 系统威胁）、D3FEND（防御对抗）及 NIST AI RMF（AI 风险管理）五大框架，用户可基于任意框架快速定位所需技能。
- **多平台兼容**：技能定义遵循 agentskills.io 标准，可无缝集成至 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多个主流 AI 代理平台。
- **领域全覆盖**：涵盖 26 个安全领域，包括威胁情报、漏洞管理、事件响应、恶意软件分析、云安全、身份与访问管理、数据加密、网络分段、安全审计、零信任架构等。
- **结构化知识表示**：每项技能包含唯一标识符、描述、输入/输出参数、关联框架标签、依赖关系以及预期耗时，便于 AI 代理解析与执行。
- **可扩展性**：基于 Apache 2.0 开源协议，用户可自由提交新技能、自定义框架映射或集成至专有系统。
- **实时更新追踪**：仓库频繁更新（近期单日增长 1004 星），社区持续提交新技能和框架对齐修正，保持与最新威胁情报和标准同步。

## 技术架构

项目以 Python 为主要实现语言，采用以下关键技术设计：

- **YAML/JSON 描述文件**：每个技能以结构化数据文件存储，包含属性：`skill_id`（唯一 ID）、`name`（名称）、`description`（描述）、`domain`（安全领域）、`frameworks`（关联框架标签列表）、`input_schema`（输入参数定义）、`output_schema`（输出格式）、`dependencies`（依赖技能）、`estimated_time`（预期执行时间）。这种格式便于机器解析和版本控制。
- **技能图谱**：通过 `dependencies` 字段构建技能间的依赖关系图，AI 代理可按需触发前置技能，避免重复初始化。
- **框架对齐引擎**：内置交叉引用表，将每个技能映射至 MITRE ATT&CK 的 tactic/technique 节点、NIST CSF 2.0 的 function/category/subcategory、MITRE ATLAS 的 attack flow、D3FEND 的防御措施以及 NIST AI RMF 的风险管理步骤。该映射允许用户从任意框架入口检索技能。
- **模块化设计**：技能按安全领域分包组织（如 `threat_intel/`、`vuln_management/`、`incident_response/`），每个包内部独立，外部通过标准接口调用。
- **平台适配层**：提供轻量级 SDK，将技能描述转换为各平台（Claude Code、Copilot 等）的 Action/Function 定义，无需手动适配。
- **自动验证脚本**：持续集成（CI）中运行 Python 脚本检查技能格式、依赖循环、框架标签有效性，确保仓库一致性。

## 安装与使用

### 安装步骤

1. **克隆仓库**：
   ```bash
   git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
   cd Anthropic-Cybersecurity-Skills
   ```

2. **安装 Python 依赖**（如需要本地验证或集成 SDK）：
   ```bash
   pip install -r requirements.txt
   ```

3. **选择平台适配器**：根据你的 AI 代理选择对应适配器。例如，若使用 Claude Code，将技能文件导入其 Actions 目录：
   ```bash
   cp -r skills/* /path/to/claude/actions/
   ```

### 最小可用示例

以下演示如何在 Claude Code 中调用一个“检测 MITRE ATT&CK 技术 T1059（命令和脚本解释器）”的技能：

1. 确保技能文件 `skills/detection/t1059_command_scripting.yaml` 已导入。
2. 在 Claude Code 聊天界面中输入：
   ```
   /use-skill t1059_command_scripting
   ```
3. AI 代理将解析技能参数（如 `target_system`、`log_source`），自动提示用户输入所需信息，并返回检测结果及关联框架分析。

若使用 GitHub Copilot，可将技能定义为 Copilot Extensions 的 Function，在提示词中通过 `@skill-name` 调用。

## 适用场景

- **AI 驱动的安全运营中心（SOC）**：AI 代理自动执行日常告警分析、威胁狩猎、日志审查，基于技能库逐步完成从检测到响应的完整流程，减少分析师手动工作量。
- **红蓝队自动化测试**：红队利用技能库快速生成 MITRE ATT&CK 攻击模拟，蓝队根据 D3FEND 技能启动对应防御措施，双方在统一框架下协作演练。
- **AI 风险合规审计**：映射至 NIST CSF 2.0 和 NIST AI RMF 的技能允许 AI 代理自动检查系统配置、权限策略、AI 模型可信度，生成合规报告。
- **教育训练与技能评估**：安全新手可浏览技能库了解 26 个领域的实操要求，AI 代理随后根据缺失技能生成个性化学习路径。

## 项目亮点

- **唯一多重框架对齐**：绝大多数网络安全技能库仅映射单一框架（如仅 MITRE ATT&CK），本项目五框架对齐能力使其成为跨合规、攻击模拟、防御加固的全能工具。
- **即插即用的平台兼容性**：支持 20+ AI 代理平台，无需为各平台单独编写技能描述，大幅降低集成成本。
- **社区驱动与高频迭代**：单日增长超 1000 星说明社区活跃度极高，技能库持续随新威胁（如 AI 对抗攻击）和框架版本更新。
- **开源+标准化**：遵循 agentskills.io 标准，并基于 Apache 2.0 协议，企业可直接整合至内部系统或二次开发。
- **粒度均衡**：754 项技能覆盖 26 个领域，平均每个领域约 29 项技能，避免过粗（无法指导具体操作）或过细（管理成本高）的极端。

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准主页](https://agentskills.io)
