---
tags:
  - trending
  - article
repo: kunchenguid/no-mistakes
date: 2026-06-27
language: Go
stars_total: 3552
stars_today: 398
---
## 项目概述

`no-mistakes` 是一个轻量级的本地 Git 代理工具，旨在帮助开发者在推送到远程仓库之前自动进行代码质量检查。它通过在本地创建一个代理层，将原本直接推送到 `origin` 的操作改为先推送到 `no-mistakes`，后者会启动一个临时的 worktree，运行 AI 驱动的验证流水线，只有在所有检查通过后才会将分支转发到真正的远程仓库，并自动创建 Pull Request。

该项目主要解决开发者在推送代码时因疏忽导致的问题，例如遗漏测试、代码风格不一致、潜在的安全风险或逻辑错误。目标用户是所有使用 Git 进行协作开发的软件工程师，尤其是那些希望自动化代码审查流程、减少审查者负担的团队。

## 核心功能

- **本地 Git 代理**：在本地创建一个代理仓库，开发者只需将推送目标改为 `no-mistakes` 即可自动触发验证流程。
- **AI 驱动验证**：利用 AI 模型对代码变更进行智能分析，检查潜在的错误、风格问题、安全漏洞和逻辑缺陷。
- **临时 Worktree**：每次推送都会创建一个独立的临时工作目录，用于运行验证流水线，不影响主工作区。
- **自动转发与 PR 创建**：验证通过后自动将分支推送到配置的远程仓库，并打开 Pull Request。
- **跨平台支持**：支持 macOS、Linux 和 Windows 三大主流操作系统。
- **轻量级集成**：无需修改现有 Git 工作流，只需安装并配置代理即可。

## 技术架构

项目使用 Go 语言开发，充分利用了 Go 的跨平台编译能力和高性能。核心架构分为三个层次：

1. **代理层**：在本地实现一个轻量级的 Git 远程仓库，接收来自 `git push` 的数据。
2. **验证引擎**：集成了 AI 模型接口，对代码变更进行审查。验证流程包括代码解析、模式匹配、静态分析和 AI 推理。
3. **转发层**：验证通过后，使用 Git 原生命令将分支推送到配置的远程仓库，并调用平台 API 创建 Pull Request。

设计上强调可扩展性：验证规则可以通过配置文件自定义，AI 模型可以替换为本地或远程的不同服务。整个流程完全在本地执行（除了 AI 推理可能需要远程 API），确保代码安全性。

## 安装与使用

### 安装方式

**macOS（Homebrew）**：
```bash
brew install no-mistakes
```

**Linux / macOS（脚本安装）**：
```bash
curl -fsSL https://raw.githubusercontent.com/kunchenguid/no-mistakes/main/install.sh | bash
```

**Windows（Scoop）**：
```bash
scoop bucket add no-mistakes https://github.com/kunchenguid/no-mistakes.git
scoop install no-mistakes
```

**手动安装**：从 [GitHub Releases 页面](https://github.com/kunchenguid/no-mistakes/releases) 下载对应平台的可执行文件并放入 PATH。

### 基本用法

1. 在项目根目录初始化 `no-mistakes`：
   ```bash
   no-mistakes init
   ```

2. 推送时使用 `no-mistakes` 替代 `origin`：
   ```bash
   git push no-mistakes main
   ```

3. 观察控制台输出，等待验证结果。如果所有检查通过，分支将自动转发到 `origin` 并创建 PR。

## 适用场景

- **日常代码提交**：在推送任何分支之前自动检查代码质量，减少低质量提交。
- **团队协作审核**：为代码审查环节增加自动化前置检查，减少审查者处理明显问题的时间。
- **CI/CD 预检**：在进入正式 CI 流水线之前，快速过滤掉有明显问题的推送，节省 CI 资源。
- **新成员入职引导**：帮助新开发者自动学习团队的代码规范和最佳实践。

## 项目亮点

相比于传统的 Pre-commit hooks 或 CI 检查，`no-mistakes` 的优势在于：

- **无需手动配置**：传统方案需要开发者在仓库或全局配置各种 hook，维护成本高；`no-mistakes` 只需安装后一句命令即可。
- **AI 智能分析**：不依赖固定的规则集，而是通过 AI 理解代码上下文，发现静态分析难以捕获的语义问题。
- **不影响现有工作流**：只需改变推送目标，不需要修改 Git 配置或 CI 模板。
- **临时隔离环境**：使用 disposable worktree 运行检查，不会影响当前开发状态。
- **跨平台一致性**：无论使用何种操作系统，体验与效果完全一致。

## 相关链接

- [GitHub 仓库](https://github.com/kunchenguid/no-mistakes)
- [Discord 社区](https://discord.gg/Wsy2NpnZDu)
- [作者 X 账号](https://x.com/kunchenguid)
