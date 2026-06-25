---
tags:
  - trending
  - article
repo: interviewstreet/hiring-agent
date: 2026-06-25
language: Python
stars_total: 2414
stars_today: 203
---
## 项目概述

Hiring Agent 是一个开源的人工智能简历评估与打分系统。它从 PDF 格式的简历中提取结构化信息，结合 GitHub 上的开源贡献信号，生成公正、可解释的评分报告。项目旨在解决传统简历筛选过程中存在的主观性强、效率低下、信息片面等问题，特别适合需要批量处理大量简历的招聘团队、技术面试官以及求职者自评。项目基于 Python 3.11+ 开发，采用 MIT 许可证开源，目前已在 GitHub 上获得超过 2400 颗星。

## 核心功能

- **简历 PDF 解析**：自动将 PDF 格式的简历转换为结构化 Markdown 文本，支持多分区识别。
- **LLM 驱动的结构化提取**：使用本地或云端大型语言模型，从 Markdown 中提取 JSON 格式的简历信息，包括技能、工作经历、教育背景等。
- **GitHub 信号增强**：自动解析候选人提供的 GitHub 链接，获取仓库贡献、Star 数、项目活跃度等信号，作为评估的客观依据。
- **可解释的评分机制**：基于预设规则和 LLM 分析，输出包含类别分数、证据引用、加分项和扣分项的详细评分报告。
- **多模型与本地部署支持**：支持 Ollama 本地模型（完全离线运行）以及 OpenAI/Anthropic 等云端 API，适应不同隐私和成本要求。
- **命令行界面**：提供简洁的 CLI 工具，支持单文件或批量处理，输出 JSON 格式的评估结果。

## 技术架构

项目采用模块化流水线设计，主要包含四个核心阶段：

1. **PDF 转 Markdown**：利用 PyMuPDF 等库提取文本和格式信息，还原为接近原始布局的 Markdown 文档。
2. **Markdown 结构化**：调用 LLM（如 Ollama 上的 Mistral/Llama，或 GPT-4）将 Markdown 转化为预定义 JSON Schema，包含 `personal_info`、`skills`、`experience`、`education`、`projects` 等字段。
3. **GitHub 信号采集**：通过 GitHub REST API 获取候选人的公开仓库、提交记录、语言分布等信息，并计算活跃度、影响力等元指标。
4. **评分与解释**：结合结构化简历数据与 GitHub 信号，依据权重矩阵（如技能匹配度、经验年限、项目影响力）生成最终分数，同时提供每个分数的逻辑依据。

架构支持通过 `config.yaml` 灵活切换 LLM 提供商、调整评分规则、修改 GitHub API 限速策略。所有中间产物（Markdown、JSON 提取结果、原始评分数据）均保留在输出目录中，便于审计和调试。

## 安装与使用

### 前提条件
- Python 3.11+
- 建议使用虚拟环境
- 如使用本地模型，需安装 Ollama（可选）

### 安装步骤
```bash
pip install hiring-agent
```

### 快速使用示例
```bash
# 基本用法：评估一份简历
hiring-agent evaluate resume.pdf

# 指定输出目录
hiring-agent evaluate resume.pdf --output ./results

# 使用 Ollama 本地模型
hiring-agent evaluate resume.pdf --provider ollama --model llama3

# 批量处理多个简历
hiring-agent batch ./resumes/*.pdf

# 自定义 GitHub 信号权重
hiring-agent evaluate resume.pdf --github-weight 0.3
```

### 配置示例（config.yaml）
```yaml
llm:
  provider: openai  # ollama / openai / anthropic
  model: gpt-4
  api_key: ${OPENAI_API_KEY}
github:
  token: ${GITHUB_TOKEN}
  limit_requests: 100
scoring:
  weight_skill: 0.4
  weight_experience: 0.3
  weight_github: 0.3
```

## 适用场景

- **技术岗位招聘初筛**：帮助招聘团队快速评估大量简历，自动生成候选人得分和理由，减少人工筛选时间。
- **开源贡献者评估**：结合 GitHub 真实贡献数据，特别适用于需要验证开源项目经验的技术岗位（如 DevOps、后端开发）。
- **求职者自检优化**：个人可上传自己的简历，获取客观打分和改进建议，有针对性地提升简历质量。
- **内部人才盘点**：企业内部可用来对现有团队成员的简历进行标准化评估，用于晋升或跨部门调动参考。

## 项目亮点

- **端到端自动化**：从 PDF 解析到评分报告，全流程无需人工干预，支持完全离线运行（使用 Ollama）。
- **评分可解释性**：每项分数都配有具体证据（如“该候选人有 5 年 Python 经验”），拒绝“黑盒”打分，增强信任度。
- **GitHub 信号价值挖掘**：将原本难以量化的开源贡献转化为结构化评分项，比纯简历评估更全面。
- **灵活多提供商**：支持本地模型（Ollama）和多种云端模型（OpenAI、Anthropic），适应不同预算和隐私合规要求。
- **轻量且可扩展**：纯 Python 实现，模块化设计，方便集成到现有招聘系统或扩展自定义评分规则。

## 相关链接

- [GitHub 仓库](https://github.com/interviewstreet/hiring-agent)
