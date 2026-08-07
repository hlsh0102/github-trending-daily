---
tags:
  - trending
  - article
repo: tirth8205/code-review-graph
date: 2026-08-07
language: Python
stars_total: 29118
stars_today: 237
---
## 项目概述

code-review-graph 是一个本地优先的代码智能图谱工具，专为 MCP（Model Context Protocol）和 CLI 环境设计。它的核心目标是解决 AI 编程工具在处理大型代码库时面临的上下文过载问题——当 AI 需要理解整个代码库才能完成代码评审或重构时，往往会消耗大量 token，且响应缓慢。

该项目通过构建代码库的持久化图谱（包含文件依赖、符号引用、调用关系等结构信息），让 AI 工具能够按需读取最相关的代码片段，而不是扫描整个仓库。对于使用 Claude、GPT 等模型的开发者而言，这意味着显著降低 token 消耗、加快响应速度，同时保持对代码全局结构的准确理解。项目面向使用 AI 辅助编码的开发者、技术团队以及所有希望优化 CI/CD 流程中代码评审效率的工程实践者。

## 核心功能

- **持久化代码图谱构建**：自动扫描代码库，建立文件、类、函数、变量之间的结构化关系图谱，并缓存到本地，后续使用无需重新分析。
- **MCP 原生集成**：作为 MCP 服务器运行，允许 Claude Desktop、Cline 等支持 MCP 的 AI 工具通过标准协议直接查询图谱信息。
- **智能上下文选取**：根据评审请求或用户指令，从图谱中筛选出最相关的代码片段（如变更影响的函数、依赖模块），而非盲目传递整个仓库内容。
- **CLI 查询接口**：提供命令行工具，支持快速检索符号定义、查找调用链、分析文件依赖等操作，便于人类开发者或脚本调用。
- **基准化报告**：内置上下文缩减率的基准测试工具，量化显示在典型评审场景下的 token 节省比例，方便团队评估收益。
- **多语言支持**：支持 Python、JavaScript、TypeScript 等主流语言的语法分析和图谱构建（基于 Tree-sitter），并持续扩展语言覆盖面。

## 技术架构

项目采用 Python 实现，核心架构分为三层：

**1. 解析层**：基于 Tree-sitter 实现对源代码的语法树解析，提取符号定义（函数、类、变量）和引用关系。Tree-sitter 的增量解析特性使得图谱在文件变更后能够快速更新，无需全量重建。

**2. 图谱存储层**：使用持久化图数据库（Neo4j 或轻量级的 SQLite 加自定义图模型）存储节点（文件、符号）和边（调用、导入、继承）。图谱以本地文件形式缓存，支持跨会话复用。设计上要求离线优先，不依赖云服务。

**3. 服务层**：提供 MCP 服务器实现（基于 FastMCP 框架）和 CLI 工具（基于 Typer）。MCP 服务器暴露查询端点，如 `get_symbol_definition`、`find_impacted_code` 等；CLI 则封装相同的逻辑，支持管道和脚本化调用。

架构的关键设计选择是**“读取时剪枝”**——图谱本身保持完整，但 AI 工具请求上下文时，系统基于图遍历算法（如最短路径、影响集计算）动态选取子图返回。这避免了静态切片可能遗漏全局依赖的问题。此外，项目支持增量更新，Git 事件监听器可自动触发受影响的图谱更新，确保信息时效性。

## 安装与使用

**安装**（需要 Python 3.9+）：

```bash
pip install code-review-graph
```

**启动 MCP 服务器**：

```bash
code-review-graph serve --repo /path/to/your/project
```

服务器默认在本地端口监听 MCP 请求，支持添加到 Claude Desktop 的 MCP 配置中。

**CLI 基本用法**：

```bash
# 构建或更新图谱
crg index --repo /path/to/your/project

# 查找某个函数的定义
crg definition --name "parse_user_input"

# 查看修改文件影响的代码范围
crg impact --file src/utils.py --repo /path/to/your/project
```

**与 Cline 集成**（示例 `settings.json`）：

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "code-review-graph",
      "args": ["serve", "--repo", "${workspaceFolder}"]
    }
  }
}
```

连接后，AI 即可自动调用图谱查询接口获取评审所需的上下文，而无需手动加载整个代码库。

## 适用场景

- **大型仓库 AI 代码评审**：当 pull request 涉及的变更横跨多个模块时，AI 需要理解全局影响。code-review-graph 可以精确提取变更相关的依赖链，让评审既全面又高效。
- **持续集成中的自动化检查**：在 CI 流水线中，结合代码图谱进行静态分析或 AI 辅助的代码质量检查，减少不必要的全量编译或 Lint 扫描耗时。
- **遗留代码库的 AI 重构**：接手不熟悉的旧项目时，AI 助手可以借助图谱快速定位核心逻辑和耦合点，生成更安全的重构方案。
- **跨语言项目协作**：对于多语言混合的仓库，图谱提供统一的关系视图，帮助团队理解不同语言模块之间的交互，降低沟通成本。

## 项目亮点

与同类工具（如依赖分析器、代码索引器）相比，code-review-graph 的差异化优势集中在以下三点：

- **面向 AI 优化**：不是简单的代码索引器，而是深耕 MCP 协议，提供 AI 友好的查询接口和上下文剪枝策略，直接对接当前主流的 AI 编程工作流。
- **可量化的性价比**：项目通过基准测试明确展示上下文缩减率（提供实测数据），让用户直观看到 token 成本节省，而非只提供抽象概念。
- **本地优先、轻量集成**：不依赖远程服务，所有数据在本地处理，保护代码隐私；安装只需一条 pip 命令，配置简单，适合个人开发和团队快速试点。

## 相关链接

- [GitHub 仓库](https://github.com/tirth8205/code-review-graph)
- [PyPI 发布页面](https://pypi.org/project/code-review-graph/)
- [项目趋势页面](https://trendshift.io/repositories/23329)
