---
tags:
  - trending
  - article
repo: tirth8205/code-review-graph
date: 2026-07-18
language: Python
stars_total: 19831
stars_today: 74
---
## 项目概述

code-review-graph 是一个本地优先的代码智能图工具，专为 MCP（Model Context Protocol）和 CLI 环境设计。它的核心目标是构建代码库的持久化地图，使 AI 编码工具在代码审查和大仓库工作流中只读取真正相关的部分。通过智能提取关键上下文，该项目在基准测试中实现了显著的上下文缩减效果，有效减少了 AI 工具的 token 消耗，解决了目前大语言模型在处理大型代码库时常见的上下文窗口限制问题。

项目主要面向使用 AI 辅助编码工具的开发者，特别是那些需要处理大型代码仓库、频繁进行代码审查的团队。无论你是使用 Cursor、Copilot 等 AI 编辑器，还是通过 CLI 进行代码审查，code-review-graph 都能帮助你更高效地与 AI 工具协作。

## 核心功能

- **代码智能图构建**：自动扫描代码库，建立文件、函数、类之间的依赖关系和引用网络，生成结构化的知识图谱
- **MCP 协议支持**：作为 MCP 服务器运行，与支持 MCP 的 AI 工具（如 Claude Desktop、Claude Code 等）原生集成
- **CLI 工具**：提供直观的命令行接口，支持代码库分析、图构建、查询和导出操作
- **智能上下文提取**：根据变更的文件列表或查询需求，自动提取出最相关的上下文信息，而非简单加载整个文件
- **持久化存储**：将构建的代码图持久化到本地磁盘，支持增量更新，无需每次都重新分析整个仓库
- **基准测试与报告**：内置 benchmark 工具，可测量上下文缩减效果，并提供详细的性能报告

## 技术架构

项目采用 Python 3.10+ 实现，遵循模块化设计原则。核心架构包含以下几个组件：

1. **图谱引擎**：使用图数据结构（基于 NetworkX 或自定义实现）存储代码实体及其关系，支持节点和边的属性标注
2. **静态分析器**：通过 AST 解析和符号表分析，提取源代码中的类、函数、变量定义及其引用关系
3. **MCP 服务器模块**：实现 MCP 协议规范，提供标准化的工具调用接口，支持 AI 工具通过协议进行查询和操作
4. **CLI 前端**：基于 Click 或 Argparse 构建的命令行界面，提供便捷的用户交互方式
5. **缓存与持久化层**：使用 SQLite 或 JSON 文件存储图数据，支持快速加载和增量更新

设计思路上，项目强调“本地优先”，所有分析都在开发者本地完成，不依赖外部 API 服务，确保代码安全性和隐私保护。同时，通过预计算和缓存机制，大幅降低重复分析的开销。

## 安装与使用

### 安装

```bash
# 使用 pip 安装
pip install code-review-graph

# 或从源码安装
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph
pip install -e .
```

### 基本使用

```bash
# 构建当前代码库的智能图
code-review-graph build

# 查看图的基本统计信息
code-review-graph info

# 在 MCP 模式下运行（用于 AI 工具集成）
code-review-graph serve

# 对指定文件进行上下文提取（用于代码审查）
code-review-graph context --files src/main.py src/utils.py

# 导出图的 JSON 格式
code-review-graph export --format json --output graph.json
```

### MCP 集成示例（以 Claude Desktop 为例）

在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "code-review-graph",
      "args": ["serve"]
    }
  }
}
```

## 适用场景

- **大型仓库代码审查**：在拥有数千个文件的微服务或单体应用中，AI 工具传统上需要加载大量上下文，导致 token 消耗巨大。code-review-graph 通过智能图提取，仅加载与变更直接相关的代码，实现 80% 以上的上下文缩减。
- **AI 辅助编程工作流**：将 code-review-graph 与 Cursor、Copilot 或 Claude Code 配合使用，让 AI 工具能更精准地理解代码依赖关系，生成更准确的建议和补全。
- **代码库重构与迁移**：在需要对大型代码库进行重构时，代码智能图可以帮助开发者快速理解代码间的依赖关系，规划重构路径，并通过 AI 工具获得有针对性的重构建议。
- **持续集成中的自动化审查**：将 code-review-graph 集成到 CI/CD 流水线中，在每次 PR 提交时自动构建变更影响图，生成高度浓缩的审查上下文，供 AI 审查工具使用。

## 项目亮点

与现有的代码分析工具相比，code-review-graph 的核心差异化优势在于：

1. **AI 原生设计**：从一开始就为 AI 工具的使用场景优化，而非传统代码分析工具的简单适配
2. **本地优先 + 隐私安全**：所有分析在本地完成，代码无需上传到第三方服务
3. **MCP 协议支持**：作为首批支持 MCP 的代码图工具，可与日益增长的 MCP 生态无缝集成
4. **可量化的性能提升**：提供内置的 benchmark 工具，让用户能直观看到 token 消耗和上下文缩减的实际效果
5. **增量更新**：支持对已有图结构进行增量更新，避免每次变更都全量重新扫描

## 相关链接

- [GitHub 仓库](https://github.com/tirth8205/code-review-graph)
- [PyPI 包](https://pypi.org/project/code-review-graph/)
- [MCP 协议文档](https://modelcontextprotocol.io/)
