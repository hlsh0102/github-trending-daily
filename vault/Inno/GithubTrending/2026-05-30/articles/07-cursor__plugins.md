---
tags:
  - trending
  - article
repo: cursor/plugins
date: 2026-05-30
language: TypeScript
stars_total: 1331
stars_today: 134
---
## 项目概述

Cursor Plugins 是 Cursor 编辑器官方维护的插件规范与参考实现仓库。该项目为开发者提供了一套标准化的插件开发框架，并发布了多个官方插件，覆盖从代码审查到持续学习等开发工作流中的关键环节。目标用户是 Cursor 编辑器的使用者、插件开发者以及希望通过自动化工具提升团队开发效率的工程团队。

## 核心功能

- **标准化插件清单**：每个插件以独立目录形式存在，根目录包含 `.cursor-plugin/plugin.json` 文件，明确定义插件的名称、作者、类别和描述等元信息
- **团队协作套件 (Cursor Team Kit)**：提供 Cursor 内部团队使用的完整工作流插件，涵盖 CI 集成、代码审查、本地自动化与验证等环节
- **深度代码审查 (Thermos)**：实现“热核级”分支审查，支持安全合规性审计、代码质量评分、并行子代理审查以及自动化 PR 流程
- **持续学习插件 (Continual Learning)**：通过增量式对话记录驱动 `AGENTS.md` 的记忆更新，仅保留高信号度的关键点，实现代理知识的渐进式积累
- **插件脚手架工具 (Create Plugin)**：提供 CLI 工具用于快速搭建和校验新插件，降低插件开发门槛
- **兼容性扫描 (Agent Compatibility)**：基于 CLI 的仓库兼容性扫描器，结合 Cursor 代理自动审计启动流程、验证环节与文档一致性

## 技术架构

项目基于 TypeScript 开发，采用模块化目录结构。每个插件独立打包，通过 `plugin.json` 清单文件与 Cursor 编辑器交互。设计上强调：

- **声明式配置**：插件的行为和依赖通过 JSON 清单描述，编辑器可自动识别和加载
- **CLI 优先**：多数插件提供命令行接口，便于代理程序稳定调用，而非依赖 GUI 交互
- **可组合性**：插件之间通过标准输入输出和文件系统通信，可编排为复杂工作流

## 安装与使用

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/cursor/plugins.git
   ```

2. 进入所需插件目录（例如 `cursor-team-kit`）：
   ```bash
   cd plugins/cursor-team-kit
   ```

3. 按照各插件目录下的 README 进行安装配置。通常步骤包括：
   - 安装依赖（`npm install` 或 `pnpm install`）
   - 配置环境变量或认证令牌
   - 将插件目录链接至 Cursor 的插件目录，或通过 Cursor 插件管理器直接加载

最小示例（使用 Create Plugin 脚手架）：
```bash
npx @cursor/create-plugin my-plugin
cd my-plugin
cursor . # 在 Cursor 中打开开发目录
```

## 适用场景

- **大型团队代码审查**：使用 Thermos 插件并行执行安全审计、质量评分和合并请求自动化，显著缩短审查周期
- **持续集成与交付**：通过 Cursor Team Kit 中的 CI 集成插件，将代码审查、自动化测试和部署流程无缝嵌入 Cursor 工作流
- **知识管理**：借助 Continual Learning 插件，让代理自动从对话中提取关键决策和技术点，维护动态更新的知识库
- **插件开发教学**：使用 Create Plugin 插件快速创建标准插件项目，参考官方插件实现理解最佳实践

## 项目亮点

与同类编辑器插件市场相比，Cursor Plugins 的差异化优势在于：

- **官方背书与一致性**：所有插件均由 Cursor 团队维护，确保与编辑器核心功能的深度兼容和及时更新
- **工作流导向**：不提供零散功能，而是围绕开发流程（审查、CI、学习）构建完整解决方案
- **代理友好设计**：CLI 优先的架构使得编码代理能够稳定调用插件，而非依赖图形界面操作
- **开源透明**：整个规范与实现公开，开发者可参与改进或 Fork 自定义版本

## 相关链接

- [GitHub 仓库](https://github.com/cursor/plugins)
- [Cursor 编辑器官网](https://cursor.sh)
