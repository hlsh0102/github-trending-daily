---
tags:
  - trending
  - article
repo: akitaonrails/ai-memory
date: 2026-08-21
language: Rust
stars_total: 3674
stars_today: 332
---
## 项目概述

`ai-memory` 是一个为 AI 编码代理（Coding Agents）提供长期记忆能力的开源工具，使用 Rust 语言编写。它解决的核心问题是：当你在 Claude Code 中工作到一半，切换到 OpenAI Codex 继续同一目录下的任务时，新代理对项目的架构设计、已失败的尝试路径以及尚未解决的问题一无所知，需要从头开始重新解释。

`ai-memory` 充当了一个标准化的“记忆层”，它不关心你使用哪个代理供应商，而是将项目的上下文、决策历史和进行中的状态持久化存储，使得任何支持该工具的代理都能无缝接续他人或自己之前的工作。目标用户是重度依赖 AI 编程助手的开发者、团队以及需要在不同 AI 工具之间切换的技术人员。

## 核心功能

- **跨代理记忆持久化**：自动捕获当前工作目录下的项目上下文、架构决策和任务状态，并将其存储为结构化的记忆文件，供任何接入的代理读取和更新。
- **无侵入式钩子集成**：通过遵循各大 AI 代理（如 Claude Code、OpenAI Codex）的自定义钩子（Hook）规范，在任务开始、结束或特定事件时自动读写记忆，不需要修改代理本身。
- **动态上下文压缩**：实现了记忆的优先级和摘要机制，确保当对话长度超出模型窗口时，最关键的“长期事实”被保留，而不再引用过时的细节。
- **快速检索与注入**：采用高效的本地索引（基于 SQLite 和内存缓存），在每次会话初始化时将相关记忆以最简形式注入到系统提示词中，不显著增加 token 消耗。
- **多平台原生支持**：提供针对 macOS（Apple Silicon 与 Intel）、Linux（x86_64 与 arm64）的原生二进制分发，以及 Windows 下的 WSL2 和实验性原生支持。
- **黑盒加密与隐私**：支持可选的记忆库加密，确保记忆文件在磁盘上不是明文存储，适用于包含敏感代码库的环境。

## 技术架构

项目的技术核心是围绕“事件驱动 + 文件系统嗅探”设计的。

1.  **客户端-服务端模式**：`ai-memory` 提一个轻量级的守护进程（Daemon）模式。代理的钩子通过 CLI 命令向该守护进程发送 JSON-RPC 请求，守护进程负责记忆的读取、写入和索引更新。这种设计避免了多代理实例并发访问同一记忆文件时的锁竞争。

2.  **记忆分层模型**：记忆被划分为三个层次——**会话层**（当前对话的短期上下文）、**项目层**（跨会话的长期事实，如架构决策、模块关系、已知问题）、**用户全局层**（跨项目的偏好设置）。在每次任务切换时，工具会提取项目层记忆中最相关的部分（通过 TF-IDF 或简单的关键词匹配），与系统提示词合并。

3.  **自适应遗忘机制**：为了避免记忆库无限膨胀，工具会基于“最后访问时间”和“引用频率”对记忆条目进行衰减评分。低分条目会被自动摘要甚至归档，确保注入的上下文总是高信号密度的。

4.  **零依赖运行时**：除了可选的 `libsqlite3`，核心二进制没有外部运行时依赖，直接通过 GitHub Actions 构建发布，安装即为一个独立的可执行文件，这使其非常适合嵌入容器化的 CI/CD 环境。

## 安装与使用

安装非常简单，以 macOS 为例：

```bash
# 下载最新发布版本
curl -L -o ai-memory.tar.gz https://github.com/akitaonrails/ai-memory/releases/latest/download/ai-memory-macos-aarch64.tar.gz
tar -xzf ai-memory.tar.gz
sudo mv ai-memory /usr/local/bin/

# 初始化记忆库（会在当前目录生成 .ai-memory/ 文件夹）
ai-memory init
```

然后，只需要在代理的配置文件中添加钩子。以 Claude Code 为例，在 `settings.json` 中新增：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          { "type": "command", "command": "ai-memory hook pre_tool_use" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          { "type": "command", "command": "ai-memory hook post_tool_use" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "ai-memory hook session_end" }
        ]
      }
    ]
  }
}
```

配置完成后，当代理执行 Bash 命令时，`ai-memory` 会自动记录命令的输出摘要和文件变更，并在会话结束时生成一份结构化“简报”存储。下次任何支持该钩子的代理启动时，它会自动读取这份简报作为初始提示词的一部分。

## 适用场景

- **多代理协作工作流**：团队中部分人偏好 Claude Code 处理重构，部分人用 Codex 处理测试生成，通过 `ai-memory` 可以在同一个仓库上无缝交接，无需在对话中反复粘贴项目背景。
- **长期运行的大型重构**：一个持续数周的分阶段重构项目，每次代理会话结束后记录已迁移的模块和当前阻塞点，避免每次开始都重新分析全量代码。
- **CI/CD 中的自动修复代理**：在流水线失败时，由代理尝试修复。利用 `ai-memory` 存储之前的修复历史，防止代理重复尝试同样无效的修补策略。
- **敏感环境下的本地记忆**：在无法使用云端记忆服务的隔离开发环境中，提供一个完全本地的记忆方案，代码不出机器。

## 项目亮点

与现有的“上下文工程”方案（如直接导出聊天记录、或使用 MCP 服务器）相比，`ai-memory` 有几点显著的差异：

1.  **供应商中立性**：不绑定任何特定代理厂商的生态。它不依赖 Claude 的 Project Knowledge 或 Codex 的存储格式，而是提供一套基于标准钩子的协议，任何代理只要支持 shell 钩子即可接入。
2.  **以“状态机”而非“记录日志”为核心**：它不仅仅存储对话历史，还自动推导出“当前任务状态”和“失败的尝试”，将最重要的结论（而非过程）列入高优先级记忆，这使得注入的上下文简短且精准。
3.  **性能优先**：原生 Rust 实现确保钩子的执行开销在毫秒级，对代理的响应速度几乎无影响，而大多数基于 Python 或 Node.js 的替代方案会带来明显的延迟。
4.  **主动遗忘**：大多数工具只会无限堆积上下文，而 `ai-memory` 的衰减机制更像人类记忆，有时间维度和重要性排序，这能显著减少长周期项目中的 token 浪费。

## 相关链接

- [GitHub 仓库](https://github.com/akitaonrails/ai-memory)
- [macOS 安装指南](https://github.com/akitaonrails/ai-memory/blob/main/docs/macos.md)
- [GitHub Releases（下载页面）](https://github.com/akitaonrails/ai-memory/releases)
