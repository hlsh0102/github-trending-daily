---
tags:
  - trending
  - article
repo: tirth8205/code-review-graph
date: 2026-07-21
language: Python
stars_total: 23622
stars_today: 1833
---
## 项目概述

**code-review-graph** 是一个本地优先的代码智能图谱工具，专为 MCP（Model Context Protocol）和 CLI 环境设计。它自动构建并持久化代码库的结构地图——包括函数、类、文件依赖和符号引用关系，使 AI 辅助编码工具（如 Cursor、Copilot、Claude Code 等）只读取真正相关的上下文，而非全量代码。

该工具针对代码审查和大型仓库工作流进行了深度优化，经基准测试可显著降低上下文消耗（最高减少 90% 以上）。核心解决两大痛点：一是 AI 工具在处理大型仓库时因输入上下文过长导致的性能下降与成本飙升；二是代码审查中因缺乏结构理解而导致的误判和遗漏。

目标用户包括：使用 AI 辅助编程的开发者、负责代码审查的团队成员、维护大型微服务或多语言仓的 DevOps 工程师，以及追求 AI 工具效率最大化的技术团队。

## 核心功能

- **代码图谱自动构建**：扫描项目目录，自动识别 Python、JavaScript、TypeScript、Go、Java、Rust、C/C++ 等主流语言的符号定义与引用关系，生成持久化的邻接表或图结构。
- **差分感知上下文筛选**：仅向 MCP 客户端或 CLI 输出与当前修改文件直接关联的函数/类/模块，避免无关代码干扰 AI 判断，实测可以将每次 AI 请求的 token 消耗降低 60–95%。
- **MCP 服务器集成**：作为 MCP 工具提供，兼容 Cursor、Windsurf、Claude Desktop 等支持 MCP 的编辑器/助手，无需修改工作流即可获得智能上下文。
- **CLI 命令支持**：提供 `crg` 命令行工具，支持 `analyze`、`graph`、`diff`、`review` 等子命令，适用于 CI/CD 流水线或本地快速分析。
- **多格式输出**：支持输出 JSON、Dot（Graphviz）、Mermaid 流程图等格式，便于可视化或二次处理。
- **增量式更新**：仅分析变更文件及其直接依赖，避免全量重建图谱，适合持续开发场景。

## 技术架构

项目基于 Python 实现，核心设计遵循以下原则：

- **静态分析引擎**：利用 `tree-sitter` 和 `jedi` 解析代码语法树。tree-sitter 提供快速的多语言 AST 解析，jedi 用于 Python 的动态类型推断和引用查找，降低误报。
- **图数据库后端**：默认使用 SQLite 持久化图谱数据，支持 `NetworkX` 内存图模式。图谱以节点（符号）和边（引用/继承/调用）的形式存储，支持高效双向检索。
- **上下文裁剪算法**：从修改文件出发，执行限定深度的 BFS/DFS 搜索（默认深度 2–3 层），结合 call-graph 和 import-graph 过滤无关路径。可配置白名单/黑名单文件模式。
- **模块化设计**：分为 `core`（解析引擎）、`graph`（图谱构建与查询）、`mcp`（MCP 协议适配）、`cli`（命令行接口）、`cache`（增量缓存）五个核心模块，便于扩展与其他语言支持。
- **零外部依赖选择**（核心模式）：除 tree-sitter 的语言包外，核心图操作不依赖大型框架，保持轻量和高性能。

## 安装与使用

**安装**：

```bash
# 通过 pip 安装
pip install code-review-graph

# 或使用 pipx（推荐隔离环境）
pipx install code-review-graph
```

**最小可用示例**：

```bash
# 1. 分析当前目录代码，输出图谱
crg analyze ./my-project

# 2. 查看与某个文件直接相关的上下文
crg diff src/main.py --depth 2

# 3. 作为 MCP 服务器启动（配置后编辑器自动识别）
crg mcp --path /path/to/project
```

**MCP 配置示例（以 Claude Desktop 为例）**：

在 `claude_desktop_config.json` 中添加：
```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "crg",
      "args": ["mcp", "--path", "/absolute/path/to/project"]
    }
  }
}
```

之后在对话中直接询问“这段修改涉及哪些函数？”或“帮我审查最近三个 commit”，MCP 工具会自动提供精准上下文。

## 适用场景

- **代码审查中的上下文补全**：在 PR 审查中，AI 助手通常只能看到更改的文件内容，而无法理解调用链和依赖关系。使用 code-review-graph 后，AI 能自动获取修改函数的所有调用者与被调用者，显著提升评审深度和准确性。
- **大型仓库的 AI 编码**：维护超过 1000 个文件的仓库时，AI 工具的上下文窗口极易被打满。code-review-graph 通过精确定位相关符号，让 AI 专注于关键代码，减少“幻觉”和无关建议。
- **跨语言依赖分析**：微服务架构中常常混合多种语言。该工具支持跨语言图谱，可帮助 AI 理解前端调用后端 API 时的完整链路，或定位接口变更的影响范围。
- **CI/CD 自动文档生成**：基于图谱变化，可以自动生成变更影响报告、调用链更新文档，降低团队维护开销。

## 项目亮点

与同类项目（如 `codesmithy`、`aider` 的 repo-map、`claude-code` 内置上下文）相比，突出优势如下：

- **本地优先与隐私安全**：所有代码分析在本地完成，不向云端传输任何代码片段或图谱数据，适合企业级保密要求高的项目。
- **基准性能优势**：作者公布的基准测试显示，在 Monorepo 场景中，上下文 token 量减少 92% 的同时保持了 96% 以上的评审准确率，远超同类工具的典型表现。
- **轻量级部署**：单文件 CLI + MCP 服务器，无数据库服务依赖，安装即用，适合集成到轻量级 CI 流水线。
- **主动维护与社区活跃**：GitHub 星数超 23000，日增 1800+，更新频率高，文档完善，支持中/英/日/韩/印多语言 README。
- **可编程性与可观测性**：提供 Python API 与 JSON 输出接口，可方便接入自定义分析流程或 Grafana 等可视化系统。

## 相关链接

- [GitHub 仓库](https://github.com/tirth8205/code-review-graph)
- [PyPI 项目页](https://pypi.org/project/code-review-graph/)
- [English README](https://github.com/tirth8205/code-review-graph/blob/main/README.md)
