---
tags:
  - trending
  - article
repo: google-labs-code/stitch-skills
date: 2026-07-12
language: TypeScript
stars_total: 7130
stars_today: 340
---
## 项目概述

Stitch Design Skills 是一个为 Google Stitch 平台设计的 Agent Skills 技能库，遵循 [Agent Skills](https://agentskills.io) 开放标准。该项目旨在为各类编码智能体（如 Antigravity、Gemini CLI、Claude Code、Cursor 等）提供可直接调用的技能集合，帮助开发者更高效地在 Stitch 平台上进行设计、构建和开发工作。

项目主要解决以下问题：
- 标准化 Agent Skills 在 Stitch 平台上的实现方式
- 提供开箱即用的设计、构建和工具类技能
- 确保不同编码智能体之间的技能兼容性

目标用户包括使用 Stitch 平台的 UI/UX 设计师、前端开发者，以及依赖编码智能体进行自动化开发的工程师团队。

## 核心功能

- **Stitch Design 技能**：专注于设计领域的技能集合，包括 UI 组件创建、样式调整、布局优化等设计相关操作
- **Stitch Build 技能**：面向构建和组件开发，支持自动化生成代码片段、组件脚手架和项目模板
- **Stitch Utilities 技能**：提供通用的工具类技能，涵盖文件操作、数据转换、代码格式化等基础功能
- **插件市场集成**：支持通过 Codex 命令行或 UI 界面快速添加和安装插件市场
- **稀疏检出优化**：支持 `--sparse` 参数进行选择性代码检出，减少克隆体积，提升初始化速度

## 技术架构

项目采用 TypeScript 编写，遵循 Agent Skills 开放标准。其架构特点包括：

1. **插件化设计**：每个技能作为独立插件存在，支持按需安装组合，降低项目依赖复杂度
2. **Git 子集管理**：利用 Git 的稀疏检出功能，开发者可以只拉取所需的技能路径，避免下载整个仓库
3. **多平台兼容**：技能格式标准化，确保与主流编码智能体（Codex、Antigravity、Gemini CLI、Claude Code、Cursor）无缝协作
4. **模块化组织**：代码按功能领域划分为 `stitch-design`、`stitch-build`、`stitch-utilities` 等独立模块，便于维护和扩展

## 安装与使用

### 前提条件
- 安装 Codex CLI 或使用支持 Agent Skills 的编码智能体
- 具备 Git 基础操作能力

### 安装步骤

**方式一：命令行安装（推荐）**

```bash
# 添加插件市场
codex plugin marketplace add google-labs-code/stitch-skills --ref main \
  --sparse .agents/plugins \
  --sparse plugins/stitch-design \
  --sparse plugins/stitch-build \
  --sparse plugins/stitch-utilities
```

> 提示：`--sparse` 参数是可选的，用于限制检出范围以加快克隆速度。省略该参数将拉取整个仓库。

**方式二：UI 界面安装**
1. 导航至 Codex 设置 → Plugin Marketplaces → Add
2. 填写仓库地址：`https://github.com/google-labs-code/stitch-skills`
3. 指定 Git ref 为 `main`
4. （可选）设置稀疏路径：`.agents/plugins`, `plugins/stitch-design` 等

### 安装后使用
市场注册成功后，选择以下插件进行安装：
- `stitch-design`：设计相关技能
- `stitch-build`：构建和组件开发技能
- `stitch-utilities`：通用工具类技能

具体调用方式取决于所使用的编码智能体，技能将通过 Agent Skills 标准接口暴露给智能体调用。

## 适用场景

1. **UI 组件设计自动化**：设计师或开发者在 Stitch 平台上快速生成 UI 组件和设计稿，减少重复性工作
2. **编码智能体开发**：为基于 AI 的编码助手提供结构化技能支持，提升其在 Stitch 生态中的任务执行能力
3. **团队协作开发**：多个开发者使用不同编码智能体时，统一的技能标准确保协作一致性
4. **项目模板快速搭建**：利用 Stitch Build 技能自动生成项目和组件脚手架，加速开发启动

## 项目亮点

- **标准化先行**：严格遵循 Agent Skills 开放标准，确保技能在不同编码智能体间无缝迁移和复用
- **极简集成**：通过稀疏检出技术，开发者只需数秒即可完成插件市场注册和技能安装
- **按需组合**：技能按功能领域拆分，开发者可根据实际需求灵活选择安装组合
- **开源友好**：采用 Apache-2.0 许可证，鼓励社区贡献和二次开发

## 相关链接

- [GitHub 仓库](https://github.com/google-labs-code/stitch-skills)
- [Google Stitch 平台](https://stitch.withgoogle.com)
- [Agent Skills 开放标准](https://agentskills.io)
