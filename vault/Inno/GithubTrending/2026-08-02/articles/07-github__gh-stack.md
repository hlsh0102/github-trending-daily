---
tags:
  - trending
  - article
repo: github/gh-stack
date: 2026-08-02
language: Go
stars_total: 854
stars_today: 46
---
## 项目概述

GitHub Stacked PRs（`gh-stack`）是一个 GitHub CLI 扩展，专为管理堆叠分支（stacked branches）和堆叠拉取请求（stacked pull requests）而设计。在大型代码变更中，传统的单一 PR 往往体积庞大、难以审查，而堆叠 PR 通过将大改动拆解为一串相互依赖的小型 PR，让每个 PR 都能独立审查、合并和演进。

该项目由 GitHub 官方发布，旨在消除堆叠工作流中的重复性操作——包括分支创建、变基维护、PR 基础分支设置以及各层级间的跳转。目标用户是需要在复杂功能开发中维持代码可审查性的个人开发者，以及依赖 AI 编码代理辅助开发、需要明确堆叠操作规范的团队。

## 核心功能

- **堆栈初始化与管理**：`gh stack init` 一键创建堆栈起始分支；`gh stack add` 在当前分支之上添加新层级，自动处理分支间的继承关系。
- **批量推送与提交**：`gh stack push` 一次性推送堆栈中所有分支，避免手动逐个执行 `git push` 的繁琐操作。
- **可视化堆栈视图**：`gh stack view` 以树状或列表形式展示当前堆栈的结构，清晰呈现各分支的层级顺序与关联 PR 状态。
- **自动化 PR 提交**：`gh stack submit` 根据堆栈层级自动创建一系列 PR，并正确设置每个 PR 的基础分支（base branch），确保依赖关系准确无误。
- **AI 代理技能集成**：通过 `gh skill install github/gh-stack` 安装官方技能，使 AI 编码代理能够理解堆栈语义并正确调用 CLI 命令。
- **底层变基维护**：自动处理分支间的变基操作，当底层分支更新时，上层分支能够被同步维护，减少合并冲突。

## 技术架构

`gh-stack` 采用 Go 语言开发，作为 GitHub CLI 的扩展插件运行。它通过调用 `gh` 命令行工具以及 Git 底层命令，实现对本地分支和远程 PR 的编排控制。

项目的核心设计思路是**以分支链为抽象单元**。每条堆栈（stack）被定义为一个有序分支列表，底部（bottom）基于主干分支（如 `main`），顶部（top）是距离主干最远的分支。每个分支的 PR 都以其下方紧邻分支为基础，形成一条清晰的依赖链。CLI 内部维护状态信息，记录当前堆栈中各分支的父子关系，从而在执行 `push`、`submit` 等操作时能够获取完整的拓扑结构。

这种设计使得操作既简单又安全：用户无需手动记忆分支间的依赖关系，也不用担心设置错误的 base 分支导致 PR 出现意外的文件变更。所有与堆栈相关的元数据均保存在本地 Git 配置中，便于团队协作时的信息同步。

## 安装与使用

**前置条件**：需安装 [GitHub CLI](https://cli.github.com/)（`gh`）v2.0 或更高版本。

**安装扩展**：

```sh
gh extension install github/gh-stack
```

**安装 AI 技能（可选）**：

```sh
gh skill install github/gh-stack
```

**最小使用示例**：

```sh
# 1. 初始化堆栈，创建第一个分支并切换过去
gh stack init

# 2. 在第一个分支上进行提交
git add .
git commit -m "feat: add authentication layer"

# 3. 在现有分支上叠加油端点分支
gh stack add api-endpoints
# 进行新的提交...
git commit -am "feat: implement API endpoints"

# 4. 推送堆栈中所有分支到远端
gh stack push

# 5. 查看当前堆栈结构
gh stack view

# 6. 为堆栈中的每个分支创建 PR（自动设置 base 分支）
gh stack submit
```

执行 `gh stack submit` 后，系统会为每个分支创建独立的 PR，并将 PR 的 base 分支设置为该分支的下一级分支，形成一条完整的 PR 链。

## 适用场景

- **大型功能拆分**：当一个功能涉及多个模块或跨越较长时间开发时，将代码分解为多个有逻辑顺序的 PR，每个 PR 控制在可轻松审查的规模。
- **代码审查优化**：希望让审查者关注特定层级的逻辑，而不用面对一次性提交的大量文件变更，提升审查效率和反馈质量。
- **AI 辅助开发治理**：团队中 AI 编码代理生成代码补丁时，通过技能文件约束其遵循堆栈操作规范，避免代理随意创建分支或错误设置 PR 依赖。
- **回滚与多版本并行**：当新功能的多个阶段需要独立测试或回滚时，堆栈中各层级的独立性允许分别追溯和调整。

## 项目亮点

- **官方出品，与 GitHub CLI 无缝集成**：作为 GitHub 官方发布的扩展，其在命令规范、错误提示和 GitHub API 交互层面保持了高度一致性，避免了第三方工具可能存在的兼容性问题。
- **零配置的自动化**：从分支创建到 PR 提交，用户几乎不需要手动指定 base 分支或远端信息，CLI 自动推断堆栈结构并执行所有派生操作。
- **面向未来 AI 工作流的原生支持**：通过 `gh skill` 机制为 AI 代理提供标准化操作指令，这是当前许多同类工具尚未覆盖的新兴领域。
- **MIT 协议开源**：代码完全开放，允许自由使用、修改和二次分发，适合团队内部定制或学习研究。
- **活跃维护与社区反馈**：项目在 GitHub 上拥有超过 850 颗 Star，近期增长迅速，用户反馈的 issue 得到及时处理，持续改进迭代。

## 相关链接

- [GitHub 仓库](https://github.com/github/gh-stack)
- [GitHub CLI 安装指南](https://cli.github.com/)
