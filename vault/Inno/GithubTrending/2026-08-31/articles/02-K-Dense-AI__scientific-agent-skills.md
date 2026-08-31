---
tags:
  - trending
  - article
repo: K-Dense-AI/scientific-agent-skills
date: 2026-08-31
language: Python
stars_total: 40047
stars_today: 1114
---
## 项目概述

Scientific Agent Skills 是一个开源的 Agent Skills 库，旨在将任何 AI 代理转变为具备专业科学能力的“AI 科学家”。该项目由 K-Dense AI 团队开发，目前已被全球超过 190,000 名科学家使用，是同类库中规模最大、覆盖最广的生态之一。

项目解决了科研人员在大模型应用中的核心痛点：通用 AI 代理缺乏科学领域的专业工具、数据源和验证流程。通过提供 165 个经过验证的即用型技能（Skills）以及 100+ 科学数据库的接入能力，Scientific Agent Skills 让研究者无需从零构建工具链，即可在对话中直接完成文献分析、分子设计、实验规划等复杂任务。

项目的目标用户包括生物学家、化学家、医学研究人员、药物发现从业者，以及所有希望在科研流程中引入 AI 辅助的开发者。它兼容 Cursor、Claude Code、Codex、Pi、Antigravity 等主流代理框架，并遵循开放 Agent Skills 标准（agentskills.io），避免了厂商锁定问题。

## 核心功能

- **165 个科学技能库**：涵盖实验设计、数据解析、统计分析、文献综述、分子性质预测等具体操作，每个技能都通过自动化测试验证其输出质量。
- **100+ 科学数据库集成**：内置对 PubChem、ChEMBL、UniProt、蛋白质数据库（PDB）、临床试验注册库等常用资源的统一接口，支持跨库检索与数据聚合。
- **多代理兼容**：基于开放 Agent Skills 标准构建，可直接安装到支持该标准的任何 AI 代理中，包括 Cursor、Claude Code、Codex、Pi 和 Antigravity。
- **即插即用的配置**：技能以标准目录结构组织（含 SKILL.md 定义文件），通过简单命令即可添加至现有代理环境，无需修改核心代码。
- **与研究工具链深度集成**：支持 Python 生态（NumPy、Pandas、RDKit、Biopython 等），并可作为 MCP（Model Context Protocol）服务运行，方便嵌入自定义工作流。
- **持续验证与更新**：项目通过 GitHub Actions 对每个技能执行单元测试和安全扫描，确保技能在各类模型和环境中保持稳定。

## 技术架构

Scientific Agent Skills 采用了一套轻量且标准化的架构。其核心是遵循开放 Agent Skills 规范定义的技能包：每个技能都是一个独立目录，其中包含一个 `SKILL.md` 文件（描述技能用途、输入输出和调用方式）以及配套的脚本或文档。这种设计使得技能可以被任何兼容代理动态加载和调用。

项目底层使用 Python 作为主要实现语言，充分利用了科学计算生态的成熟库。技能内部通过统一的 API 层访问外部数据库，该层封装了不同数据源的身份验证、请求限流和数据格式转换，确保代理能够稳定地获取结构化信息。

架构上特别强调“去中心化”和“可移植性”。它不绑定任何特定模型或代理，而是通过标准协议进行交互——技能既可以被本地脚本调用，也可以通过 MCP 暴露为远程服务。此外，项目采用面向过程的技能划分方式，每个技能聚焦单一科研任务（如“SMILES 规范化”或“蛋白质序列比对”），降低了耦合度，也便于社区贡献新技能。

对于有更高算力需求的场景，项目提供了可选的云扩展方案（例如通过 Modal 平台调度重型计算任务），而本地安装则保证数据隐私和处理速度。

## 安装与使用

### 环境要求

- Python 3.9 或更高版本（仅运行核心库时可选）
- 主流的 AI 代理环境（如 Cursor、Claude Code 或 Codex），或支持开放 Agent Skills 标准的运行时

### 安装步骤

1. 克隆仓库至本地：

   ```bash
   git clone https://github.com/K-Dense-AI/scientific-agent-skills.git
   cd scientific-agent-skills
   ```

2. 将技能目录链接到你的代理环境。以 Claude Code 为例，可以将 `skills` 文件夹复制到代理的工作目录，或通过代理的插件机制引用。

3. 运行技能验证（可选但推荐）：

   ```bash
   python -m pytest tests/ -v
   ```

### 最小可用示例

在支持 Agent Skills 的代理中（如 Cursor），安装后将技能库路径配置好，即可通过自然语言调用技能。以下是一个典型交互：

```text
用户请求：“请查找与 BRAF V600E 突变相关的临床试验数据。”
代理响应：调用 `search_clinical_trials` 技能，该技能自动查询 ClinicalTrials.gov 数据库，返回结构化结果，并附带数据质量检查和引用信息。
```

对于开发者，也可以通过 Python 直接调用技能函数：

```python
from scientific_agent_skills import search_pubchem

results = search_pubchem(query="aspirin", fields=["CID", "IUPACName"])
print(results)
```

## 适用场景

- **学术文献综述**：科研人员利用技能库自动检索多个数据库（如 PubMed、ChemRxiv），提取关键信息并生成结构化摘要，将文献整理时间从数天缩短至数小时。
- **药物早期发现**：计算化学家通过分子性质预测、ADMET（吸收、分布、代谢、排泄和毒性）评估和虚拟筛选技能，快速筛选候选化合物，减少湿实验前的盲目尝试。
- **实验数据质量控制**：实验室人员使用数据解析和异常检测技能，自动清洗来自不同仪器的原始数据，生成标准化报告，确保可复现性。
- **医学临床研究辅助**：医生和医学研究者利用循证医学技能快速收集诊疗指南、药物相互作用和临床试验信息，辅助制定研究方案或临床决策。

## 项目亮点

- **规模与覆盖面**：165 个经过测试的技能和 100+ 数据库接入，是目前公开可用的最大科学技能库，几乎覆盖了从分子到临床的完整科研链条。
- **真正的跨平台兼容**：放弃专有格式，完全拥抱开放 Agent Skills 标准。用户可以在底层代理变化时无缝迁移技能资产，避免重复投资。
- **企业级验证保障**：每个技能都附带自动化测试和安全扫描，在数百种模型组合上进行过验证，减少了生产环境中“技能失效”的风险。
- **社区活跃度高**：项目在 GitHub 上拥有超过 40,000 星标，24 小时内新增约 1,000 星，且提供官方 Discord 和定期社区会议，反馈循环快速。
- **开源且可扩展**：采用 MIT 许可证，允许商业使用和二次开发。同时提供详细的贡献指南（CONTRIBUTING.md），鼓励领域专家提交新技能。

## 相关链接

- [GitHub 仓库](https://github.com/K-Dense-AI/scientific-agent-skills)
- [开放 Agent Skills 标准](https://agentskills.io/)
- [K-Dense BYOK 桌面版工具](https://github.com/K-Dense-AI/k-dense-byok)
- [官方文档](https://agent-plugins.org/)
