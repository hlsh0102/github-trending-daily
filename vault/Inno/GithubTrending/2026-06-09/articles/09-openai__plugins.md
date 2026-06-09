---
tags:
  - trending
  - article
repo: openai/plugins
date: 2026-06-09
language: JavaScript
stars_total: 2385
stars_today: 296
---
## 项目概述

OpenAI Plugins 是一个由 OpenAI 官方维护的 Codex 插件集合仓库，旨在为开发者提供可复用、可扩展的插件示例库。该项目解决了 Codex 生态系统中缺乏标准化插件模板和最佳实践的问题，帮助开发者快速集成工具、自动化工作流和增强 AI 编码助手的能力。目标用户包括使用 Codex、Cursor、GitHub Copilot 等 AI 编程工具的开发者，以及希望为特定框架或平台构建智能辅助工具的工程师。

## 核心功能

- **结构化插件框架**：每个插件遵循统一的目录结构，包含 `.codex-plugin/plugin.json` 清单文件和可选配置，支持 `skills/`、`agents/`、`commands/` 等模块化扩展。
- **预构建丰富示例**：提供 Figma、Notion、iOS 构建、macOS 构建、Web 应用构建、Expo、Netlify 等场景的完整插件实现，可直接参考或修改使用。
- **多表面集成**：插件可包含 `.mcp.json`（MCP 模型上下文协议配置）、`.app.json`（应用配置）、`hooks.json`（钩子）等，实现与外部工具和环境的深度集成。
- **设计系统与代码规则**：例如 Figma 插件包含设计令牌、组件映射和代码生成规则，帮助保持设计一致性和代码质量。
- **工作流自动化**：如 Notion 插件支持会议记录、研究整理、知识捕获等任务自动化，减少重复性操作。
- **跨平台兼容**：支持 Web、iOS、macOS、Expo/React Native 等多种平台，覆盖主流开发场景。

## 技术架构

项目基于 Codex 插件规范构建，核心设计思路是“清单驱动”的模块化架构。每个插件由一个 `plugin.json` 定义元数据（名称、描述、触发条件），并通过目录结构组织功能组件。关键技术包括：

- **JavaScript 生态**：使用 Node.js 编写插件逻辑，支持 npm 依赖管理和 ES Modules 模块系统。
- **MCP（模型上下文协议）**：通过 `.mcp.json` 文件定义与外部系统（如文件系统、数据库、API）的交互协议，实现安全的上下文传输。
- **技能系统**：`skills/` 目录定义可复用的 AI 技能，例如代码转换、调试、部署等，每个技能对应一个独立的 prompt 或 action。
- **Agent 与 Hook**：`agents/` 提供自动化代理逻辑，`hooks.json` 定义生命周期钩子（如 pre-commit、post-build），实现事件驱动的编程辅助。
- **资源与资产管理**：`assets/` 目录存储静态资源（图标、模板文件），通过 `assets/` 引用路径实现插件内的资源隔离。

这种架构的设计特点在于“可组合性”——开发者可以像搭积木一样组合不同插件、技能和代理，快速构建复杂的开发工作流，同时保持插件的独立性和可维护性。

## 安装与使用

使用 OpenAI Plugins 前，需要确保你的开发环境满足以下条件：

- 安装 Node.js 18+ 和 npm 8+
- 拥有 Codex 兼容的 IDE（如 Cursor、VS Code 插件）
- 基本的命令行操作经验

安装步骤：

1. **克隆仓库**：
   ```bash
   git clone https://github.com/openai/plugins.git
   cd plugins
   ```

2. **进入插件目录**（以 Figma 插件为例）：
   ```bash
   cd plugins/figma
   ```

3. **安装依赖**：
   ```bash
   npm install
   ```

4. **配置插件**：编辑 `plugin.json` 中的 `name`、`description` 和 `skills` 字段，确保与你的开发环境匹配。

5. **激活插件**：将插件目录注册到 Codex 插件的配置文件中（如 `~/.codex/config.json`），或使用 IDE 的插件管理界面加载。

最小可用示例（创建一个简单插件的流程）：

```bash
mkdir -p my-plugin/.codex-plugin
cat > my-plugin/.codex-plugin/plugin.json << EOF
{
  "name": "my-plugin",
  "description": "自定义示例插件",
  "version": "1.0.0",
  "skills": {
    "hello": "打印欢迎消息"
  }
}
EOF
```

然后在 Codex 中加载该插件，并调用 `hello` 技能。

## 适用场景

- **设计到代码的自动转换**：设计师在 Figma 中修改组件后，通过 Figma 插件自动同步到代码库中的组件定义，减少人工比对工作量。
- **项目脚手架搭建**：使用 `build-ios-apps` 或 `build-web-apps` 插件快速生成具备最佳实践的初始项目结构，包括 linter 配置、CI/CD 脚本和状态管理方案。
- **团队协作知识管理**：Notion 插件可自动整理开发会议笔记、关联任务并生成周报，适合有文档化需求的敏捷团队。
- **跨平台应用开发**：Expo 插件帮助 React Native 开发者管理 EAS 构建、版本升级和 Codex 运行，简化移动端开发流程。

## 项目亮点

与普通的插件集合不同，OpenAI Plugins 的最大优势在于“生态一致性”和“深度集成”：

- **标准化格式**：所有插件遵循统一的清单文件结构，降低理解成本，便于社区贡献和工具链自动化处理。
- **官方维护**：由 OpenAI 团队直接管理，确保示例的质量、兼容性和安全性，避免第三方插件的碎片化问题。
- **从实际场景提炼**：每个插件都来自真实开发痛点（如 Figma 的设计系统维护、Notion 的知识管理），而非纯粹的技术演示。
- **可扩展性**：通过 `MCP` 和 `hooks` 支持任意外部系统集成，理论上可以覆盖任何开发工作流，而不仅限于 OpenAI 自身产品。

## 相关链接

- [GitHub 仓库](https://github.com/openai/plugins)
