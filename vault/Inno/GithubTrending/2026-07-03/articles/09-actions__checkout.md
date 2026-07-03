---
tags:
  - trending
  - article
repo: actions/checkout
date: 2026-07-03
language: TypeScript
stars_total: 8190
stars_today: 26
---
## 项目概述

`actions/checkout` 是 GitHub Actions 生态中最核心的官方 Action 之一，用于在 CI/CD 工作流中自动将指定的 Git 仓库代码检出到运行器（Runner）的工作目录中。它的目标用户是所有使用 GitHub Actions 进行持续集成、持续部署或自动化测试的开发者。

该项目解决了在自动化流程中手动配置 Git 操作的繁琐问题。通过简单的 `uses: actions/checkout@v4` 一行配置，即可自动完成仓库的克隆、分支切换、认证配置等操作，为后续的构建、测试、部署步骤提供干净的代码环境。当前最新稳定版本为 v7。

## 核心功能

- **仓库检出**：支持按分支、标签或指定提交哈希检出代码，默认检出触发工作流的分支。
- **浅克隆优化**：支持设置 `fetch-depth` 参数来控制 Git 历史深度，显著加速大型仓库的检出速度，默认仅检出最近一次提交。
- **Token 自动处理**：使用 `GITHUB_TOKEN` 或自定义 PAT 进行认证，避免手动处理访问令牌。
- **子模块支持**：通过 `submodules` 参数自动初始化并拉取嵌套的子模块。
- **LFS 文件支持**：能够自动检出通过 Git LFS 管理的二进制文件。
- **路径自定义**：通过 `path` 参数指定检出到运行器上的自定义目录。
- **安全增强**：v7 版本引入更严格的 fork pull request 保护机制，默认阻止在 `pull_request_target` 和 `workflow_run` 触发条件下执行不安全代码。

## 技术架构

`actions/checkout` 是一个基于 TypeScript 开发的 GitHub Action，本质是一个运行在 Actions Runner 上的可执行脚本。其核心逻辑包括：

1. **环境感知**：自动识别 `GITHUB_REF`、`GITHUB_SHA`、`GITHUB_TOKEN` 等环境变量，确定需要检出的仓库、分支或提交。
2. **Git 操作封装**：通过调用系统自带的 Git 命令完成克隆、拉取、子模块初始化等操作，避免了重复造轮子。
3. **凭证安全存储**：从 v6 版本开始，`persist-credentials` 功能将凭证存储在 `$RUNNER_TEMP` 下的独立文件中，而非直接写入 `.git/config`，提高了安全性。
4. **事件驱动**：根据不同的 GitHub 事件（如 `push`、`pull_request`、`workflow_dispatch`）动态调整行为，例如 `pull_request_target` 事件下会启用更严格的检查。

项目架构呈现轻量级特点，依赖版本管理良好，每次大版本更新都会升级运行环境（如 node20、node24）以确保兼容性和性能。

## 安装与使用

由于 `actions/checkout` 是 GitHub 官方提供的 Action，无需单独安装。直接在 `.github/workflows/` 下的 YAML 工作流文件中使用即可。

**最小可用示例**：创建一个 `.github/workflows/checkout-demo.yml` 文件，内容如下：

```yaml
name: Checkout Demo
on: [push]

jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          repository: my-org/my-private-repo  # 可选，默认检出当前仓库
          ref: main                           # 可选，默认检出触发事件的分支
          fetch-depth: 0                      # 获取完整 Git 历史（默认仅最近一次提交）
      - name: List files
        run: ls -la
```

**进阶用法**（带子模块和自定义路径）：

```yaml
- name: Checkout with submodules
  uses: actions/checkout@v4
  with:
    submodules: 'true'
    path: my-custom-dir
```

建议固定使用 `v4` 或 `v7` 这样的主版本号标签，以避免不必要的破坏性更新。

## 适用场景

- **持续集成流水线**：每次代码推送后自动检出最新代码，运行单元测试、代码扫描或构建任务。
- **发布流程自动化**：基于标签检出指定版本代码，执行打包、签名、发布到包管理器的操作。
- **多仓库协作**：在一个工作流中多次调用 `actions/checkout`，分别检出主仓库和依赖库，用于集成测试。
- **安全审核场景**：当使用 `pull_request_target` 或 `workflow_run` 触发器时，配合 `allow-unsafe-pr-checkout: true` 进行可控的代码审查。

## 项目亮点

- **官方维护，生态标准**：由 GitHub 官方团队维护，与 GitHub Actions 深度集成，是社区中最广泛使用的 Action 之一（拥有超过 8000 颗 Star）。
- **安全优先的设计**：v7 版本的 fork PR 保护机制直接解决了“pwn request”漏洞，而 v6 改进的凭证存储方式降低了凭证泄露风险，体现了对安全问题的持续关注。
- **极简配置**：大多数场景下仅需一行 `uses: actions/checkout@v4` 即可工作，零配置启动。
- **细粒度控制**：虽然默认行为简单，但支持 20 多个可选参数（如 `fetch-depth`、`submodules`、`path`、`token` 等），满足复杂定制需求。
- **性能优化**：默认浅克隆深度为 1，适合快速 CI；设置 `fetch-depth: 0` 可获取完整历史；支持 Git LFS 和子模块，避免手动处理依赖。

## 相关链接

- [GitHub 仓库](https://github.com/actions/checkout)
- [官方文档 - GitHub Actions 工作流程语法](https://docs.github.com/zh/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsuses)
