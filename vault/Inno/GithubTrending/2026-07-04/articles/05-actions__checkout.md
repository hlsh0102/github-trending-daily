---
tags:
  - trending
  - article
repo: actions/checkout
date: 2026-07-04
language: TypeScript
stars_total: 8280
stars_today: 129
---
## 项目概述

`actions/checkout` 是 GitHub Actions 官方提供的一个核心操作，用于在 CI/CD 流水线中从 GitHub 仓库检出代码。它是绝大多数 GitHub Actions 工作流的第一步，解决了自动化构建、测试和部署场景下如何安全、高效地获取源码的问题。目标用户是所有使用 GitHub Actions 进行持续集成和持续部署的开发者、运维团队以及开源项目维护者。

无论项目是采用 Node.js、Python、Java 还是其他语言，只要需要在 Actions 运行环境中获取仓库代码，`checkout` 动作都是不可或缺的基础组件。

## 核心功能

- **快速检出仓库代码**：将指定仓库（默认是触发工作流的仓库）的代码克隆到 Actions 运行环境中，支持指定分支、标签或提交 SHA。
- **安全的分支处理**：默认禁止在 `pull_request_target` 和 `workflow_run` 触发器中检出 fork 仓库的代码，防止“pwn request”漏洞（即 PR 中的恶意代码利用基础仓库的权限）。
- **持久化 Git 凭据**：自动将 GitHub Token 写入凭证存储，使后续的 `git fetch`、`git push` 等操作无需额外配置即可通过身份验证，同时通过将凭据存储在临时文件而非 `.git/config` 中提升了安全性。
- **灵活的子模块支持**：支持递归检出 git 子模块，并允许验证子模块的 SSH 密钥。
- **自定义检出路径**：可将代码检出到工作目录之外的自定义路径。
- **轻量级与自动清理**：可配置只检出最新版本（`fetch-depth: 1`），并在作业结束后自动清理临时文件。

## 技术架构

该项目使用 TypeScript 编写，发布在 GitHub Actions Marketplace 上。其核心逻辑是将一系列 git 命令封装为可复用的 Action 步骤，通过输入参数（如 `repository`、`ref`、`token`）控制检出行为。

关键设计思路包括：
- **分层架构**：使用 `Runner` 工具类抽象与 GitHub Actions 运行时的交互，使用 `GitCommandManager` 类封装所有 git 操作，使代码逻辑清晰且易于测试。
- **安全优先**：在 7.x 版本中，专门引入 `allow-unsafe-pr-checkout` 开关，并要求工作流作者显式确认风险后才能在敏感触发器中检出 PR 代码，这是对开源社区常见安全问题的积极回应。
- **兼容性演进**：从 v5 的 node24 运行时升级到 v7 的 ESM 模块化，不仅利用新技术提升性能和安全，还保持了与旧版本的向后兼容性。

## 安装与使用

`actions/checkout` 无需单独安装，它作为 GitHub Actions 的一部分，可直接在工作流中引用。以下是典型的最小可用示例：

```yaml
steps:
  - name: Checkout repository code
    uses: actions/checkout@v4
    with:
      repository: ${{ github.repository }}
      ref: ${{ github.ref }}
      token: ${{ secrets.GITHUB_TOKEN }}
```

在大多数场景中，只需简单地写为：
```yaml
steps:
  - uses: actions/checkout@v4
```

如果想只检出最新一次提交（用于大型仓库加速）：
```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 1
```

如需在安全场景下检出 fork PR 的代码（谨慎使用）：
```yaml
- uses: actions/checkout@v4
  with:
    allow-unsafe-pr-checkout: true
```

## 适用场景

- **持续集成流水线**：在任何代码推送或合并请求触发时，先通过 `checkout` 获取代码，再执行构建、测试、代码检查等步骤。
- **自动化部署**：在发布工作流中，检出指定发布分支的代码，然后部署到云服务器或容器平台。
- **多仓库协作**：通过 `repository` 参数配合 `token`，在同一个工作流中检出多个不同仓库的代码，用于编译、打包或数据同步。
- **定时任务**：配合 `schedule` 触发器，定期检出并处理仓库中的最新变更。

## 项目亮点

- **行业标准**：作为 GitHub 官方维护的动作，拥有超过 8,200 星以及极高的使用率，经过大规模实际场景验证。
- **安全性强化**：v7 中对 fork PR 检出行为进行严格限制，主动防范了 GitHub Actions 生态中最常见的“pwn request”攻击。
- **凭据管理优化**：v6 中将 Git 凭据存储在临时目录中，避免了 `.git/config` 可能被不当暴露的风险，且无需用户修改工作流配置。
- **持续更新维护**：定期升级运行时环境（如 v5→v6→v7 的 node 版本升级），修复已知安全漏洞，紧跟技术发展趋势。

## 相关链接

- [GitHub 仓库](https://github.com/actions/checkout)
