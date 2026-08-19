---
tags:
  - trending
  - article
repo: akitaonrails/ai-memory
date: 2026-08-19
language: Rust
stars_total: 2803
stars_today: 648
---
## 项目概述

ai-memory 是一款面向 AI 编码代理（Agent）的长期记忆解决方案，旨在解决多代理协作场景下的上下文丢失问题。它允许开发者在任务中途退出 Claude Code，随后在同一目录下启动 OpenAI Codex，无需重新解释项目架构、失败尝试或待解决问题。该项目由 Rust 编写，采用 MIT 许可证，目前已在 GitHub 上获得超过 2800 星标，可见其切中了当下 AI 辅助编程的痛点。

目标用户是重度依赖 AI 编码代理的开发者、技术团队以及研究机构，尤其是那些需要跨工具切换、长时间维持项目上下文的场景。

## 核心功能

- **跨代理记忆持久化**：在工作目录中自动保存与项目相关的上下文信息，包括架构决策、失败路径、未解决问题等，实现从 Claude Code 到 Codex 等不同代理的无缝切换。
- **多平台支持**：官方支持 Linux（含 Docker 镜像）、macOS（原生二进制）、Windows（WSL2 及实验性原生支持），覆盖主流开发环境。
- **自动化上下文捕获**：通过代理的钩子（Hook）机制，在任务执行的关键节点自动提取并存储上下文，无需手动干预。
- **轻量级命令工具**：提供简洁的 CLI 接口，可快速查询、追加或清理记忆条目，与现有工作流自然集成。
- **结构化记忆存储**：以结构化格式（如 JSON 或 SQLite）持久化数据，支持按时间、主题或关联性检索，便于后续代理理解项目演进。
- **零配置启动**：在支持平台上，安装后即可自动启用，无需修改代理配置文件（若需自定义，可选用 Docker 包装器或源码构建）。

## 技术架构

ai-memory 采用 Rust 语言开发，充分利用了 Rust 在性能、内存安全和跨平台编译方面的优势。其架构核心是一个本地守护进程与 CLI 的二元结构：

- **核心存储引擎**：基于 Rust 编写，负责记忆数据的持久化、索引与查询。数据存储采用嵌入式数据库，支持事务性写入，确保多次钩子调用的数据一致性。
- **代理连接层**：通过标准输入输出（stdio）或文件系统监控与各类 AI 代理交互。它实现了针对不同代理解析的适配器，能够解析 Claude Code、Codex 等工具的钩子输出，提取有意义的上下文。
- **钩子调度机制**：利用各代理的钩子系统（如 Claude Code 的预/后命令钩子），在任务开始时加载相关记忆，在任务结束时写入新学到的信息，形成“记忆循环”。
- **平台抽象层**：通过条件编译和系统级抽象，统一了 macOS、Linux 和 Windows 的不同路径处理、进程管理和权限模型，尤其是处理了 Windows WSL2 与原生环境的差异。

设计上强调“目录即作用域”，记忆与当前工作目录绑定，这天然契合多项目并行开发的习惯，避免了全局状态污染。

## 安装与使用

**安装步骤**（以 macOS 推荐路径为例）：

1. 前往 [GitHub Releases](https://github.com/akitaonrails/ai-memory/releases/latest) 下载 `ai-memory-macos-aarch64.tar.gz`（Apple Silicon）或 `ai-memory-macos-x86_64.tar.gz`（Intel）。
2. 解压并将二进制文件移动到 `/usr/local/bin` 或添加到 `$PATH`。
3. 在项目根目录执行 `ai-memory init` 启动初始化（该命令会创建必要的配置目录）。

**最小可用示例**：

```bash
# 在项目目录中初始化
cd /path/to/your/project
ai-memory init

# 查看当前项目的记忆摘要
ai-memory recall

# 手动追加一条关键决策记录
ai-memory append "决定使用 PostgreSQL 而非 MySQL，因为需要 JSONB 支持"

# 在 Claude Code 中开始任务（自动加载已有记忆）
claude

# 任务完成一半，切换到 Codex
codex
# Codex 会自动感知到 ai-memory 的存在，并加载最新上下文
```

对于 Linux 用户，可直接使用 Docker 镜像（`docker pull ghcr.io/akitaonrails/ai-memory`）或从 AUR 安装（含 systemd 服务单元）。Windows 用户建议通过 WSL2 使用 Linux 安装路径。

## 适用场景

- **跨工具切换的长期开发**：团队成员使用不同的 AI 编辑工具（如 Claude Code、Codex、Copilot），共享项目记忆可减少重复解释，提升协作效率。
- **长时间运行的项目维护**：当项目周期较长、任务间隔较大时，AI 代理可以通过记忆快速恢复对代码库的“理解”，避免因上下文过期导致的错误建议。
- **自动化代码审查与重构**：在复杂的重构任务中，代理可以记录每一步的推理过程和受阻点，即便中断也能在后续会话中无缝续接。
- **研究性项目验证**：研究人员在尝试多种实验方案时，可用记忆功能记录各方案的优劣和组合逻辑，便于总结经验。

## 项目亮点

与在终端之间手动复制粘贴上下文或使用单一厂商的云同步方案相比，ai-memory 具备以下差异化优势：

- **供应商无关（Vendor-Agnostic）**：不是某一家 AI 工具的私有扩展，而是开放协议，支持主流代理，避免被单一厂商绑定。
- **本地优先与隐私友好**：所有数据保留在本地文件系统，不依赖云服务，适合处理敏感代码和内部架构信息。
- **极低侵入性**：基于钩子的无头设计，不必更改代理的主配置文件，使用原生系统资源，对性能影响极小。
- **跨平台一致性**：无论团队使用 macOS、Linux 还是 WSL2 环境，其行为保持一致，降低了团队间的沟通成本。
- **精准的辅助而非替代**：专注于提供“记忆”这一核心增能点，不试图重造 IDE 或代理框架，保持了工具的简洁性。

## 相关链接

- [GitHub 仓库](https://github.com/akitaonrails/ai-memory)
- [最新版本下载](https://github.com/akitaonrails/ai-memory/releases/latest)
- [macOS 使用指南](https://github.com/akitaonrails/ai-memory/blob/main/docs/macos.md)
