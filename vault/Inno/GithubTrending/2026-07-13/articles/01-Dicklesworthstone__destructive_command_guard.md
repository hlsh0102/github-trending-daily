---
tags:
  - trending
  - article
repo: Dicklesworthstone/destructive_command_guard
date: 2026-07-13
language: Rust
stars_total: 3197
stars_today: 444
---
## 项目概述

`dcg`（Destructive Command Guard）是一个高性能的守护程序，专门为 AI 编程代理设计，用于在执行破坏性命令之前进行拦截和阻止。随着 Claude Code、Codex CLI、Cursor 等 AI 编程工具在日常开发中的广泛使用，AI 代理在生成代码时偶尔会误执行 `rm -rf`、`git reset --hard`、`git push --force` 等危险命令，导致工作区文件被意外删除或仓库历史被破坏。dcg 在系统层面充当一个轻量级代理，实时监控并拦截这些高风险命令，在命令真正执行前提示用户确认或直接拒绝。项目面向所有使用 AI 编程代理的开发者，尤其适合高价值仓库、多人协作项目以及需要严格保护生产环境的团队。

## 核心功能

- **命令拦截与放行**：自动识别超过 30 种高风险 shell 命令和 git 命令，包括 `rm`、`dd`、`chmod`、`git reset`、`git push --force`、`git clean` 等，在执行前弹出实时确认提示，用户可选择阻止或放行当前命令。
- **智能白名单机制**：支持对特定命令、参数组合或目标路径添加白名单。例如，允许在指定项目目录下执行 `git push --force`，但拒绝在根目录执行。白名单支持通配符和正则表达式。
- **深度命令解析**：不依赖简单的字符串匹配，而是真正解析 shell 命令的 AST（抽象语法树），能有效识别被别名、变量、字符串拼接或嵌套子命令隐藏的危险操作，避免被 AI 代理的欺骗性提示绕过。
- **高性能与低开销**：使用 Rust 编写，内存占用极低（空闲时 < 1 MB），命令检查延迟 < 50 微秒，几乎不影响开发工具的启动和响应速度。
- **多平台支持**：原生支持 macOS（Apple Silicon 和 Intel）、Linux（x86_64 和 aarch64），并提供 Windows 版本的实验性支持。
- **一键安装与集成**：通过 `dcg install` 命令自动检测当前系统上已安装的 AI 编程工具（Claude Code、Codex CLI、Cursor 等），并配置对应的 hook。支持核心引导二进制文件，无需手动修改配置文件。

## 技术架构

dcg 采用客户—服务器（client-server）架构。核心守护进程 `dcgd` 以后台进程运行，监听来自前端 hook 的命令查询请求。前端 hook 是由 AI 编程工具在每次执行 shell 命令时调用的轻量级二进制文件（通常体积 < 100 KB），它将当前要执行的命令及其上下文（工作目录、环境变量）序列化后发送给 `dcgd`。守护进程内部维护一个经过编译的规则引擎，规则引擎加载白名单配置和内置危险命令库，执行快速的模式匹配和 AST 解析。如果命令被判定为危险且不在白名单内，守护进程返回阻止信号，hook 进程阻止命令执行。通信采用基于 Unix 域套接字（macOS/Linux）或命名管道（Windows）的零拷贝协议，确保极低的延迟。配置存储在 `~/.config/dcg/config.toml` 文件中，支持热重载，无需重启守护进程。

## 安装与使用

**安装步骤：**

1. **通过包管理器（推荐）：**
   ```bash
   # macOS (Homebrew)
   brew install destructive-command-guard/tap/dcg

   # Linux (使用 cargo)
   cargo install dcg
   ```

2. **配置与激活：**
   ```bash
   # 启动守护进程
   dcgd start

   # 自动检测并安装 hook 到所有已发现的 AI 工具
   dcg install --all

   # 检查当前系统状态
   dcg status
   ```

**最小可用示例：**

安装后，当你使用 Claude Code 或 Codex CLI 时，任何疑似危险的命令都会触发拦截提示。例如，在 Claude Code 中尝试让 AI 执行 `rm -rf /tmp/test`，dcg 会弹出一个终端提示：
```
⚠️ Destructive Command Guard 已拦截：
  命令: rm -rf /tmp/test
  来源: Claude Code (PID 12345)
  是否允许？ [y/N] 
```

你可以选择允许本次执行，或仅忽略此命令的告警一次。

**手动添加白名单示例：**

在 `~/.config/dcg/config.toml` 中添加：
```toml
[whitelist]
commands = [
  { pattern = "git push --force", path = "/path/to/your/project" },
  { pattern = "rm -rf /tmp/.*" }
]
```

## 适用场景

- **AI 辅助开发的安全护栏**：任何使用 AI 编程代理进行日常开发的团队或个人，可以放心让代理执行代码重构、文件移动等操作，而无需担忧误删除关键文件或破坏 git 历史。
- **CI/CD 流水线上的防御层**：在 CI/CD 环境中，AI 代理如 Codex CLI 或 Grok CLI 被用来自动修复代码或执行部署脚本。dcg 可作为最后一道防线，拦截因模型幻觉或错误上下文导致的破坏性命令。
- **共享开发环境与教学场景**：在多用户共享的开发服务器上，可以配置全局 dcg 规则，防止新手开发者误用危险命令损坏公共资源，同时保留教育意义（提示内容会解释为何该命令危险）。
- **高价值仓库的保护**：对于拥有大量未推送更改或包含敏感数据的仓库，dcg 可以阻止 `git clean -fd` 或 `git checkout -- .` 等不可逆操作，确保只有经过用户明确同意后才可以执行。

## 项目亮点

- **真正理解命令语义**：不同于简单的字符串模糊匹配，dcg 通过解析 AST 识别复杂构造下的危险操作，极大降低了误拦率和漏拦率。许多同类项目仅依赖正则表达式，容易被 `r m -rf /` 这类空格变形绕过。
- **零配置的即插即用**：安装后只需一条 `dcg install --all` 命令，即可自动配置当前机器上所有主流 AI 工具的 hook。无需手动编写 shell 脚本或修改工具配置文件，降低了使用门槛。
- **守护进程的持久化与热重载**：独立的后台进程支持实时日志记录和统计查看，配置变更无需重启，适合持续使用 AI 代理的日常开发流程。部分同类方案仅在每次会话启动时加载配置，效率较低。
- **活跃维护与广泛兼容**：项目在发布首周即获得大量社区关注，并持续适配新出现的 AI 编程工具（如 Antigravity CLI、OpenCode、Pi 等），支持官方 hook 和社区插件，生态覆盖全面。

## 相关链接

- [GitHub 仓库](https://github.com/Dicklesworthstone/destructive_command_guard)
- [Pi 集成教程](https://github.com/Dicklesworthstone/destructive_command_guard/blob/main/docs/pi-integration.md)
