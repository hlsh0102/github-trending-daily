---
tags:
  - trending
  - article
repo: MemPalace/mempalace
date: 2026-06-07
language: Python
stars_total: 54410
stars_today: 446
---
## 项目概述

MemPalace 是一个本地优先的 AI 记忆系统，旨在为 AI 对话提供持久化、可检索的会话历史存储。它解决了当前 AI 对话系统缺乏长期记忆、会话窗口有限、依赖云端 API 的核心痛点。项目以 96.6% 的 R@5 原始得分在 LongMemEval 基准测试中表现优异，且完全开源、免费使用。目标用户包括 AI 开发者、对话系统构建者、需要长期记忆支持的 Claude Code/Slack AI 等工具的用户，以及任何希望为 AI 应用添加可靠记忆功能的技术团队。

## 核心功能

- **逐字存储**：不进行摘要、提取或改写，完整保留对话原始文本，确保信息零失真。
- **可插拔后端**：支持多种存储后端，用户可根据需求选择本地文件系统、数据库或云存储方案。
- **语义检索**：基于语义相似度的高效搜索，能够在大量历史记录中快速定位相关内容。
- **层级组织架构**：将人与项目映射为“wing”，主题映射为“room”，原始内容存储在“drawer”中，支持限定范围的精确搜索。
- **本地优先**：默认所有数据存储在本地，无需依赖第三方 API 或远程服务，保障数据隐私和访问速度。
- **Claude Code 集成**：提供专属的会话保留设置清单，支持与 Claude Code 环境无缝对接，防止 30 天会话过期。

## 技术架构

MemPalace 采用 Python 编写，核心设计遵循本地优先原则。其架构包含三个主要层次：

1. **存储层**：负责原始文本的持久化，支持多种后端实现（如 SQLite、文件系统等），通过统一接口切换。
2. **索引层**：构建基于语义向量的搜索索引，采用高效嵌入模型（无需外部 API 调用即实现 96.6% R@5 性能），支持按 wing/room/drawer 层级限域检索。
3. **查询层**：提供简洁的 Python API 和命令行接口，支持自然语言搜索、范围过滤和排序。

项目的关键设计决策包括：不进行任何信息提炼或压缩以确保忠实性；使用结构化索引而非扁平化存储以提升搜索精度；所有操作在本地完成以避免隐私泄露和 API 依赖。

## 安装与使用

**安装要求**：Python 3.9+

**安装**：

```bash
pip install mempalace
```

**最小可用示例**：

```python
from mempalace import MemPalace

# 初始化记忆宫殿
palace = MemPalace(storage_backend="local", path="./my_memory")

# 存储对话
palace.store("user: What is the capital of France?\nassistant: Paris.", meta={"session": "geo_101"})

# 搜索相关内容
results = palace.search("France capital", top_k=3)
for r in results:
    print(f"Score: {r.score:.4f}, Text: {r.text[:100]}")
```

**Claude Code 快速集成**：

1. 安装 MemPalace
2. 参照官方指南配置启动/恢复钩子
3. 使用 `mempalace save` 和 `mempalace search` 命令管理会话记忆

## 适用场景

- **长期 AI 会话管理**：为 Claude Code 等工具提供超越会话窗口限制的持久记忆，避免 30 天过期后丢失上下文。
- **个人知识库检索**：作为个人笔记、研究资料的本地搜索引擎，支持语义查询且不依赖云端。
- **客户支持系统**：存储历史工单和客户对话，帮助客服人员快速回溯过往交互记录。
- **AI Agent 记忆组件**：作为多轮推理 Agent 的外部记忆模块，提供高保真的历史信息检索能力。

## 项目亮点

- **基准测试领先**：在 LongMemEval 上取得 96.6% R@5 原始得分，是目前公开性能最优的 AI 记忆系统之一。
- **零 API 依赖**：完全本地运行，无需调用任何外部服务或付费 API，成本可控且无网络要求。
- **忠实存储**：不同于其他摘要式记忆系统，MemPalace 保留原文，避免信息丢失和失真。
- **结构化索引**：wing/room/drawer 的层级设计让搜索可限域，提升准确性和效率。
- **MIT 开源许可证**：完全免费，允许商业使用、修改和分发。
- **庞大的社区验证**：超过 54,000 个 GitHub Star，每日新增 400+，社区活跃度高。

## 相关链接

- [GitHub 仓库](https://github.com/MemPalace/mempalace)
- [官方文档](https://mempalaceofficial.com)
- [PyPI 包](https://pypi.org/project/mempalace/)
- [Claude Code 保留设置指南](https://mempalaceofficial.com/guide/claude-code-retention.html)
