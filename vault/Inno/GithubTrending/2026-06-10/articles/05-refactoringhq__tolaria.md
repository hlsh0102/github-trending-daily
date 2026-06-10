---
tags:
  - trending
  - article
repo: refactoringhq/tolaria
date: 2026-06-10
language: TypeScript
stars_total: 14500
stars_today: 829
---
## 项目概述

Tolaria 是一款跨平台桌面应用（支持 macOS、Windows 和 Linux），专为管理 Markdown 知识库而设计。它将自己定位为一种“文件优先”和“Git 优先”的知识管理工具，旨在解决传统笔记应用数据锁定、不可移植的痛点。

核心用户群体包括：希望建立“第二大脑”和个人知识库的个人用户、需要为 AI 语境组织公司文档的团队，以及使用 OpenClaw 等助手类工具管理和存储记忆与流程的用户。项目作者 Luca 本人使用 Tolaria 管理包含超过 10,000 条笔记的工作空间，涵盖工作笔记、个人日志和第二大脑系统。

## 核心功能

- **原生 Markdown 支持**：所有笔记以纯 Markdown 文件形式存储，无需专有格式或导出步骤，保证数据的可移植性。
- **基于 Git 的版本控制**：每个知识库（Vault）都是一个 Git 仓库，天然支持文件的变更历史、分支管理和团队协作。
- **多平台桌面客户端**：提供 macOS、Windows 和 Linux 的原生桌面应用体验，而非基于网页的伪桌面应用。
- **强大知识库组织能力**：支持大规模笔记库（如作者本人 10,000+ 条笔记）的高效浏览与管理。
- **灵活的导入导出**：作为文件优先的工具，可以轻松与其他编辑器（如 VS Code、Neovim）配合使用。
- **开源与社区驱动**：采用 AGPL-3.0 许可证，代码完全开放，用户可自行审查、修改和扩展功能。

## 技术架构

Tolaria 基于 TypeScript 开发，充分利用了其类型安全和生态丰富的特点。核心技术选择包括：

1. **前端框架**：采用 Electron 或类似技术实现跨平台桌面应用，结合 React 或类似 UI 库构建用户界面。
2. **文件系统集成**：借助 Node.js 的文件系统 API 实现对本地 Markdown 文件的直接读写，确保低延迟和高性能。
3. **Git 集成**：内置 Git 客户端功能，可自动检测和操作 Vault 目录下的 Git 仓库，提供可视化的提交、分支和合并操作。
4. **渲染引擎**：使用 Markdown 解析库（如 unified/remark）实现实时预览和富文本编辑。
5. **状态管理**：采用响应式状态管理方案，确保大规模笔记库下界面流畅更新。

架构设计的核心理念是“极简依赖”——不依赖云服务、专有数据库或服务器端组件，所有数据都在本地处理和存储。

## 安装与使用

### 安装步骤

1. 访问 [Tolaria GitHub 发布页面](https://github.com/refactoringhq/tolaria/releases) 下载对应操作系统的安装包。
2. macOS 用户：下载 `.dmg` 文件并拖拽到 Applications 文件夹。
3. Windows 用户：运行安装程序 `.exe` 或 `.msi`。
4. Linux 用户：下载 AppImage 或 Snap 包，赋予执行权限后运行。

### 快速入门

```bash
# 1. 创建或克隆一个 Markdown 知识库
git init my-knowledge-base
# 或克隆现有仓库
git clone git@github.com:your-username/your-knowledge-base.git

# 2. 启动 Tolaria，选择上述目录作为 Vault

# 3. 开始创建笔记
```

**最小使用示例**：

1. 打开 Tolaria，点击“打开 Vault”按钮。
2. 选择一个包含 Markdown 文件的文件夹，或新建一个空文件夹。
3. 在左侧导航栏右键选择“新建笔记”，输入标题保存后即可开始编辑。
4. 修改自动保存在本地文件系统中，无需手动保存。
5. 在底栏中可查看当前 Git 状态，点击“提交”按钮即可记录变更。

## 适用场景

- **个人知识管理（第二大脑）**：用于记录学习笔记、读书摘要、日记和灵感，配合 Git 实现版本回溯，避免内容丢失。
- **团队文档协作**：团队成员可将公司文档以 Markdown 形式存储在 Git 仓库中，结合 Tolaria 获得可视化浏览体验，同时保留代码级协作能力。
- **AI 工具集成**：为 AI 助手（如 OpenClaw）提供结构化的上下文知识库，便于 AI 理解业务背景和流程规范。
- **长期项目归档**：大型项目的技术文档、架构决策记录（ADR）等可以结构化存储在 Vault 中，通过 Git 历史追溯变更原因。

## 项目亮点

- **真正的数据所有权**：与 Notion、Roam Research 等封闭平台不同，Tolaria 不锁定用户数据。笔记是普通文件，可以随时用任何文本编辑器打开。
- **原生 Git 集成**：将所有 Vault 视为 Git 仓库并非简单包装，而是深度集成了版本控制工作流，在桌面应用中提供分支管理、差异比较等功能。
- **无后端依赖**：所有操作离线完成，无需 SaaS 订阅或云同步服务，用户只需自行管理 Git 远程仓库（GitHub、GitLab 等）即可。
- **极致的性能**：针对万级笔记库进行了优化，对比同类工具如 Obsidian 在加载大型知识库时的卡顿问题，Tolaria 提供了更流畅的体验。
- **简洁的设计理念**：不过度封装，忠实呈现 Markdown 文件的实际内容，避免让用户陷入复杂的文件夹和标签管理系统。

## 相关链接

- [GitHub 仓库](https://github.com/refactoringhq/tolaria)
- [如何组织我的 Tolaria 工作空间](https://www.loom.com/share/bb3aaffa238b4be0bd62e4464bca2528)
- [我的收件箱工作流](https://www.loom.com/share/dffda263317b4fa8b47b59cdf9330571)
- [如何将网页资源保存到 Tolaria](https://www.loom.com/share/8a3c1776f801402ebbf4d7b0f31e9882)
