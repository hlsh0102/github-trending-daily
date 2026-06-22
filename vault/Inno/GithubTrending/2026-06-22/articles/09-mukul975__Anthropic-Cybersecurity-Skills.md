---
tags:
  - trending
  - article
repo: mukul975/Anthropic-Cybersecurity-Skills
date: 2026-06-22
language: Python
stars_total: 17971
stars_today: 361
---
## 项目概述

Anthropic Cybersecurity Skills 是一个开源项目，旨在为 AI 代理提供一套结构化、生产级的网络安全技能库。该项目包含 **754 个精心设计的技能项**，覆盖 26 个安全领域，并映射到 5 个主流网络安全框架：MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 以及 NIST AI RMF。

项目解决了两个核心问题：一是 AI 代理在网络安全场景中缺乏标准化的技能描述，无法系统性地执行安全任务；二是安全团队难以将 AI 能力与现有框架和流程对齐。通过提供结构化的技能库，项目让任何 AI 代理（如 Claude Code、GitHub Copilot、Codex CLI、Cursor 等）都能具备相当于高级安全分析师的操作能力。

目标用户包括安全运营工程师、渗透测试人员、AI 安全研究员以及希望在安全工作流中集成 AI 代理的开发团队。

## 核心功能

- **754 个生产级技能项**：覆盖从日志分析到攻防演练的完整安全生命周期，每个技能都包含精确的操作描述和参数规范
- **5 框架映射**：技能与 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 显式关联，便于管理层审计和合规对齐
- **26 个安全领域全覆盖**：包括威胁狩猎、数字取证、恶意软件分析、云安全、容器安全、AI 安全等关键领域
- **多平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 26 余种 AI 平台的技能加载和执行
- **可扩展性设计**：遵循 agentskills.io 标准格式，用户可直接使用或基于现有技能进行修改定制
- **Apache 2.0 开源许可**：完全开源，允许商业使用和二次开发

## 技术架构

项目以 Python 为主要实现语言，采用**技能即代码（Skills as Code）**的核心设计思路。每个技能项被编码为结构化 JSON/YAML 格式，包含以下关键字段：

- 技能名称与唯一标识符
- 适用的框架映射（如 MITRE ATT&CK 技术 ID）
- 操作描述与预期输出
- 参数约束与平台兼容性标记
- 前序/后置条件（便于编排）

架构上采用**分层设计**：底层是独立技能项，顶层是框架映射层和平台适配层。这种设计允许技能在保持标准化的同时，通过简单的适配器层接入不同 AI 代理的运行环境。

项目不依赖任何特定的 AI 引擎或云服务，技能数据以纯文本形式存储，因此可以嵌入到任何支持工具调用（Tool Calling）或函数调用（Function Calling）的 AI 系统中。

## 安装与使用

### 快速开始

```bash
# 克隆仓库
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills

# 查看技能库结构
ls skills/

# 以 JSON 格式输出所有技能（示例）
python scripts/export_skills.py --format json --output skills.json
```

### 在 Claude Code 中使用

将仓库中的技能文件作为上下文提供给 Claude Code：

```bash
# 在 Claude Code 项目中加载技能目录
claude code --skills-dir ./skills/
```

### 在 GitHub Copilot 中使用

将技能文件中的 JSON 定义作为 Codex 工具的上下文参考，Copilot 将基于技能库中的模式生成安全相关的代码。

### 自定义技能

```json
{
  "skill_id": "memory_forensics_volatility3",
  "name": "Volatility3 内存取证分析",
  "framework": ["mitre_attack", "nist_csf"],
  "description": "使用 Volatility3 的 linux.malfind 插件扫描可疑内存区域",
  "parameters": {
    "image_path": "string",
    "output_dir": "string"
  },
  "platforms": ["claude_code", "copilot", "cursor"]
}
```

## 适用场景

- **安全运营自动化**：在 SOC 中部署 AI 代理，自动执行日志解析、告警分类、初步取证等重复性任务，将分析时间从小时级缩短到分钟级
- **红蓝对抗模拟**：训练 AI 代理基于 MITRE ATT&CK 框架的技能库，自动化执行渗透测试步骤或检测规则验证
- **安全培训与技能评估**：将技能库作为学习路径，帮助安全新人系统化掌握框架映射关系，评测 AI 代理的安全能力覆盖度
- **合规审计支持**：利用 NIST CSF 2.0 和 NIST AI RMF 映射的技能项，快速生成与合规要求对齐的控制措施列表

## 项目亮点

- **规模最大**：754 个技能项是目前开源社区中最大的 AI 安全技能库，远超同类项目的技能覆盖度
- **框架中立但全面兼容**：不同于仅绑定单一框架的项目（如只支持 MITRE ATT&CK），该项目兼顾了 5 个主流框架，更符合企业实际的安全治理需求
- **跨平台设计**：技能库不依赖特定 AI 平台，可以无缝迁移到 Claude、Copilot、Cursor 等工具，避免了平台锁定
- **可审计性与可追溯性**：每个技能都标明映射的框架 ID，安全负责人可以清晰追踪某个自动化操作对应的行业标准要求
- **活跃的社区贡献**：项目采用 agentskills.io 标准，社区可以提交新的技能或修正现有映射，持续演进

## 相关链接

- [GitHub 仓库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [agentskills.io 标准](https://agentskills.io)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [D3FEND](https://d3fend.mitre.org/)
- [NIST AI RMF](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence)
