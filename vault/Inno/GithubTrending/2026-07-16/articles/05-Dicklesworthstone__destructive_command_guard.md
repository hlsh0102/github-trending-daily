---
tags:
  - trending
  - article
repo: Dicklesworthstone/destructive_command_guard
date: 2026-07-16
language: Rust
stars_total: 4840
stars_today: 471
---
## 项目概述

Destructive Command Guard（简称 dcg）是一个用 Rust 编写的高性能守护程序，专门用于拦截 AI 编码代理执行的危险 git 和 shell 命令。在 AI 辅助编程日益普及的今天，AI 代理在生成代码、执行命令时可能会意外触发 `git reset --hard`、`rm -rf /` 等破坏性操作，导致代码丢失或环境损坏。dcg 通过在命令执行前进行实时检查，有效阻止这类风险，保护开发者的工作成果。项目主要面向使用 Claude Code、Codex CLI、Gemini CLI、Copilot CLI、Cursor 等 AI 编码工具的开发者和团队。

## 核心功能

- **命令拦截与审查**：在 AI 代理执行命令前，dcg 会检查命令是否涉及危险操作（如强制删除、重置、覆盖等），并根据规则决定放行或拒绝。
- **多层防护策略**：支持黑名单（禁止特定命令）、白名单（仅允许安全命令）和模式匹配（基于正则表达式识别风险）三种防护模式，可灵活配置。
- **多工具兼容**：原生支持 Claude Code、Codex CLI、Gemini CLI、GitHub Copilot CLI、VS Code Copilot Chat、Cursor IDE、Hermes Agent、Grok (xAI) 等主流 AI 编码工具，并提供统一的集成接口。
- **透明审计日志**：所有被拦截的危险命令都会记录到日志中，包括执行时间、命令内容、发起代理等信息，便于事后审查。
- **轻量级性能**：采用 Rust 编写，执行效率高，对开发流程的延迟影响极小（通常在微秒级别）。
- **可定制规则**：用户可以根据自身需求添加、修改或禁用特定的危险命令规则，支持 YAML/JSON 配置文件。

## 技术架构

dcg 采用客户端-守护进程架构设计。核心是一个用 Rust 编写的高性能守护进程，通过 Unix 域套接字（或命名管道）与各 AI 编码工具的钩子系统通信。当 AI 代理准备执行命令时，工具会调用 dcg 的钩子脚本，该脚本向守护进程发送命令内容并等待裁决。守护进程的裁决引擎基于有限状态自动机（FSA）和模式匹配，能快速识别预定义的危险模式。整个设计遵循以下原则：

- **非侵入性**：作为钩子运行，不需要修改 AI 工具本身。
- **原子化裁决**：每个命令的检查是独立且原子的，不会影响工具的正常工作流。
- **低耦合**：通过标准输入输出（stdin/stdout）和轻量级协议与外部工具交互，便于扩展支持更多工具。
- **安全性优先**：守护进程以最小权限运行，且不支持远程访问，避免成为新的攻击面。

## 安装与使用

### 安装

dcg 提供预编译的二进制包，支持 macOS、Linux 和 Windows（WSL）。最简单的安装方式是通过包管理器：

```bash
# macOS (Homebrew)
brew install Dicklesworthstone/tap/dcg

# 或使用 Cargo 直接编译
cargo install dcg
```

安装后，运行 `dcg init` 会在当前用户的配置目录中生成默认配置文件，并自动检测已安装的 AI 编码工具。

### 基本使用

1. **启动守护进程**：
   ```bash
   dcg daemon &
   ```

2. **激活防护**：
   针对特定工具启用防护。例如，为 Claude Code 启用：
   ```bash
   dcg enable claude-code
   ```

3. **运行测试**：
   尝试执行一个危险命令，检查是否被拦截：
   ```bash
   git reset --hard HEAD~1
   # 如果命令被拦截，会输出类似：
   # [dcg] Dangerous command blocked: git reset --hard HEAD~1
   ```

4. **查看日志**：
   ```bash
   dcg logs
   ```

### 配置示例

创建一个 `~/.config/dcg/rules.yaml` 文件来定制规则：

```yaml
rules:
  - action: block
    pattern: "^git reset --hard"
  - action: warn
    pattern: "^rm -rf "
  - action: allow
    pattern: "^git commit"
```

## 适用场景

- **AI 辅助开发**：在使用 Claude Code、Copilot CLI 等工具时，防止 AI 代理误执行破坏性 git 操作或系统命令。
- **CI/CD 流水线**：在自动化部署流程中，额外增加一层安全防护，确保 AI 生成的脚本不会意外破坏生产环境。
- **团队协作开发**：对于多人协作的项目，统一配置危险命令规则，防止个别成员的 AI 工具误操作影响整个仓库。
- **教学与培训**：在编程教学环境中，允许学员使用 AI 辅助工具，同时通过 dcg 避免因误操作导致的代码丢失。

## 项目亮点

- **极致性能**：Rust 实现的守护进程在命令检查时仅消耗毫秒级资源，远低于同类 Python/Node.js 实现的工具。
- **广泛的工具生态支持**：覆盖了当前几乎所有主流 AI 编码工具，并且提供统一的集成接口，方便新增支持。
- **零误报策略**：默认规则经过精心设计，只拦截高度危险的命令，避免对正常开发流程造成干扰。
- **开源透明**：所有规则和代码均开源，用户可以审查、修改安全策略，确保没有后门或潜在的隐私泄露风险。

## 相关链接

- [GitHub 仓库](https://github.com/Dicklesworthstone/destructive_command_guard)
