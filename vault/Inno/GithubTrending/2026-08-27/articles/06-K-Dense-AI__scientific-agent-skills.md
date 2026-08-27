---
tags:
  - trending
  - article
repo: K-Dense-AI/scientific-agent-skills
date: 2026-08-27
language: Python
stars_total: 35021
stars_today: 494
---
## 项目概述

Scientific Agent Skills 是一个开源的 Agent Skills 库，旨在将任意 AI Agent 转变为具备专业科学能力的 AI 科学家。该项目由 K-Dense AI 团队开发维护，目前已获得全球超过 175,000 名科研工作者的使用，是当前规模最大的科学领域 Agent Skills 库。

在科研工作中，研究人员经常需要在多个专业数据库之间切换，处理大量的生物、化学、医学数据，并执行复杂的分析流程。传统 AI 助手缺乏对科学数据库的标准化访问能力和专业领域知识的深度集成，导致工作效率低下。Scientific Agent Skills 通过提供 163 个经过验证的预置技能和 100+ 科学数据库的接入能力，有效解决了这一问题。

该项目适用于生物学家、化学家、医学研究人员、药物发现专家以及所有需要在日常工作中处理科学数据的技术人员。无论您使用的是 Cursor、Claude Code、Codex、Pi、Antigravity 还是遵循开放 Agent Skills 标准的其他工具，都可以无缝集成这些科学技能。

## 核心功能

- **163 个已验证的科学技能**：覆盖从基因序列分析、蛋白质结构预测到化合物性质查询的完整科研工作流，每个技能均经过严格验证，确保输出结果的可靠性。

- **100+ 科学数据库接入**：内置对主流生物、化学、医学数据库的标准接口，包括但不限于 NCBI、UniProt、PDB、ChEMBL 等，免去繁琐的 API 对接工作。

- **跨平台兼容性**：基于开放 Agent Skills 标准构建，支持 Cursor、Claude Code、Codex、Pi、Antigravity 等主流 AI Agent 平台，实现一次集成、处处使用。

- **多学科广度覆盖**：技能库横跨生物学、化学、医学和药物发现四大核心领域，满足跨学科研究需求。

- **持续更新与验证**：项目通过自动化安全扫描和技能测试，确保每个技能在最新版本中保持可用性和准确性。

- **K-Dense BYOK 桌面应用**：配套的免费开源 AI 协同科学家桌面工具，支持自带 API 密钥，可本地运行全部 161 个技能，并可选通过 Modal 扩展到云端计算。

## 技术架构

Scientific Agent Skills 采用模块化的技能定义架构，每个技能本质上是一个遵循开放 Agent Skills 标准的指令包，包含明确的输入输出规范、参数定义和执行逻辑。这种设计使得技能可以被任何支持该标准的 AI Agent 动态加载和调用。

项目使用 Python 作为主要实现语言，通过 pyproject.toml 进行依赖管理和构建配置。技能库的组织遵循领域分层原则，将生物学、化学、医学和药物发现相关的技能分类存放，便于用户按需引入。

在数据访问层面，项目封装了统一的数据库查询接口，屏蔽了不同科学数据库之间的协议差异。这种抽象层设计不仅简化了技能开发流程，还使得新增数据库时无需修改已有技能逻辑。同时，项目通过 GitHub Actions 实现了持续集成测试和安全隐患扫描，确保每个技能在各类环境中都能稳定运行。

值得注意的是，该项目前身为 Claude Scientific Skills，经过架构调整后更名为 Scientific Agent Skills，将兼容性从单一平台扩展到所有支持开放标准的 AI Agent。这种开放策略避免了厂商锁定，使用户可以根据实际需求自由选择运行环境。

## 安装与使用

### 环境要求

- Python 3.9 或更高版本
- 支持 Agent Skills 标准的 AI Agent 客户端

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git

# 进入项目目录
cd scientific-agent-skills

# 安装依赖
pip install -e .
```

### 最小使用示例

以查询蛋白质序列为例，您可以按照以下方式在支持 Agent Skills 的客户端中调用：

1. 在您的 AI Agent 配置中，将本仓库的 `skills` 目录添加为技能源。
2. 直接使用自然语言请求，例如：“请从 UniProt 数据库中获取人类 TP53 蛋白的氨基酸序列。”
3. Agent 将自动匹配并执行 `uniprot_sequence_query` 技能，返回结构化结果。

对于需要多个数据库操作的复杂任务，如“查找与 BRAF V600E 突变相关的上市药物”，Agent 会自动串联相应技能，组合完成查询和分析流程。

## 适用场景

- **学术研究**：生物医学领域的研究人员可以快速检索文献相关数据、分析基因表达谱、进行蛋白质结构比对，大幅缩短数据收集和预处理时间。

- **药物发现**：药物研发团队能够高效查询化合物活性、毒性数据，结合 ChEMBL 和 PubChem 等数据库进行先导化合物筛选和评估。

- **临床决策支持**：医学工作者可快速获取药物相互作用信息、基因突变与疾病关联数据，辅助诊断和治疗方案制定。

- **跨学科教学**：教育学场景中，教师可向学生演示如何利用 AI 工具进行科学数据查询和分析，培养计算思维。

## 项目亮点

与其他 AI Agent 技能库相比，Scientific Agent Skills 具有以下差异化优势：

- **深度领域知识**：并非简单的通用工具封装，而是针对科研工作流进行了深度优化，技能设计贴近实际研究过程中的操作逻辑。

- **广泛的生态合作**：项目已获得全球顶尖 AI 工具链的支持，覆盖 175,000+ 科学家用户，形成了活跃的社区反馈和改进循环。

- **开放标准倡导**：率先采纳开放 Agent Skills 标准，推动行业互操作性，避免用户被单一平台锁定。

- **本地优先的数据安全**：配套的 BYOK 工具实现了完全本地化的数据处理，满足科研数据隐私和合规要求，同时支持按需扩展到云端计算。

- **活跃的更新节奏**：项目持续迭代，每日不断增长的 star 数量和频繁的安全扫描验证，体现了项目的生命力和可靠性。

## 相关链接

- [GitHub 仓库](https://github.com/K-Dense-AI/scientific-agent-skills)
- [Agent Skills 开放标准](https://agentskills.io/)
- [Agent Plugins 社区](https://agent-plugins.org/)
- [K-Dense BYOK 桌面工具](https://github.com/K-Dense-AI/k-dense-byok)
