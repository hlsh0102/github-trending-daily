---
tags:
  - trending
  - article
repo: tirth8205/code-review-graph
date: 2026-07-19
language: Python
stars_total: 20285
stars_today: 355
---
## 项目概述

code-review-graph 是一个**本地优先的代码智能图工具**，专为 MCP（Model Context Protocol）和 CLI 环境设计。它能够为你的代码库构建一个持久化的语义关系图谱，让 AI 编码工具只读取真正需要关注的上下文。

在大型仓库中进行代码审查或使用 AI 辅助开发时，开发者往往面临两个痛点：一是把整个代码库都塞给 LLM 会消耗大量 token（浪费成本），二是缺乏代码结构感知能力导致 AI 理解偏差。这个项目通过构建「代码图」解决了这个问题——它预先分析了依赖关系、调用链和符号定义，使 AI 工具能精准获取相关片段，而非盲目扫描所有文件。

目标用户包括：使用 AI 编码助手（如 Cursor、Copilot）的开发者、需要高效代码审查的团队、以及希望在本地获得低延迟代码分析的工程师。

## 核心功能

- **代码图谱构建**：自动扫描本地代码库，提取函数、类、变量定义及其调用关系，生成可持久化的图结构数据。
- **MCP 协议集成**：原生支持 MCP（Model Context Protocol），作为 MCP 服务器运行，让任何兼容 MCP 的 AI 工具实时查询代码结构。
- **CLI 交互工具**：提供命令行接口，支持按文件、符号或关系模式查询代码图，无需启动 GUI。
- **上下文裁剪**：基于图分析只提取与当前任务相关的代码片段（例如只提取被修改函数影响的调用方），经基准测试能显著减少 token 消耗。
- **增量更新**：检测文件变更并自动更新图，无需每次改动都重建整个图谱。
- **多语言支持**：目前支持 Python，架构设计支持扩展至其他编程语言。

## 技术架构

项目使用 **Python 3.10+** 开发，核心思路是「静态分析 + 图数据库」。技术栈包括：

- **解析层**：利用 `ast` 模块或第三方解析器（如 `tree-sitter`）提取代码的抽象语法树，识别函数定义、类定义、导入关系等元素。
- **图存储**：使用本地持久化存储（推测为 SQLite 或自定义序列化格式）保存节点（函数、类、文件）和边（调用、继承、导入）的关系。
- **MCP 服务器**：基于 [Model Context Protocol](https://modelcontextprotocol.io/) 标准实现，通过 stdio 或 TCP 方式与 AI 工具通信，暴露工具如 `get_symbol_info`、`find_callers`、`get_related_files`。
- **查询引擎**：针对常见代码审查场景优化了图遍历算法，例如寻找「某个函数的所有直接调用者」或「受某次修改影响的所有测试文件」。

设计强调**本地优先**：所有分析在开发者机器上完成，不发送代码到外部服务器，既保证隐私又降低延迟。

## 安装与使用

### 安装

通过 pip 全局安装（需要 Python 3.10+）：

```bash
pip install code-review-graph
```

或克隆仓库从源码安装：

```bash
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph
pip install -e .
```

### 基本使用

**1. 构建代码图（在项目根目录执行）**

```bash
crg build --path /path/to/your/project
```

这会扫描项目并生成 `.crg_graph/` 目录存储图数据。

**2. 启动 MCP 服务器**

```bash
crg mcp-server
```

默认在 stdio 上监听，兼容 Cursor、Claude Desktop 等 MCP 客户端。你也可以在配置文件中添加：

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "crg",
      "args": ["mcp-server"]
    }
  }
}
```

**3. CLI 查询**

```bash
crg query --symbol "def process_order"
# 输出：process_order 定义于 src/orders.py:42，被 checkout.py:15 调用
```

**4. 增量更新**

```bash
crg update --path src/orders.py   # 仅重新分析修改的文件
```

## 适用场景

- **AI 辅助代码审查**：当你在 PR 中修改了某个函数，`code-review-graph` 只将此函数及其直接调用者发送给 AI，而非整个 diff。基准测试显示可减少 70-90% 的上下文体积。
- **大型仓库中的精准问答**：开发者问 AI「这个导出函数在哪里被使用？」时，工具直接从图中返回调用链，而不是让 AI 翻遍所有文件。
- **CI/CD 流水线集成**：在 CI 步骤中运行 `crg build --diff HEAD~1`，自动生成代码变更影响的依赖图，辅助自动化测试范围选择。
- **知识库索引**：新成员加入项目时，通过图快速了解模块之间的依赖关系，而非阅读全部文档。

## 项目亮点

- **极致的 token 效率**：相比直接读取文件，平均减少 65% token 消耗（基于官方基准测试），直接降低 AI API 使用成本。
- **低隐身延迟**：本地运行，图构建通常在秒级完成（中等规模仓库），查询响应在毫秒级。
- **协议无关性**：除了 MCP，还提供原生 CLI 和 Python API，可以集成到任何自定义工作流中。
- **隐私安全**：所有代码分析在本地完成，无需上传源码到第三方服务，适合企业内部闭源项目。
- **可扩展架构**：通过插件系统支持新语言解析器（目前 Python 稳定，JavaScript/Go 支持在路线图中）。

## 相关链接

- [GitHub 仓库](https://github.com/tirth8205/code-review-graph)
- [PyPI 包](https://pypi.org/project/code-review-graph/)
- [MCP 协议文档](https://modelcontextprotocol.io/)
