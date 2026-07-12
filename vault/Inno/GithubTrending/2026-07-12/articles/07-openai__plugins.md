---
tags:
  - trending
  - article
repo: openai/plugins
date: 2026-07-12
language: JavaScript
stars_total: 4458
stars_today: 29
---
## 项目概述

OpenAI Plugins 是一个由 OpenAI 官方维护的 Codex 插件示例集合仓库。该项目旨在为开发者提供一套结构化的、可直接参考的插件开发范例，帮助用户快速理解和构建基于 Codex 平台的扩展功能。目标用户主要是希望利用 OpenAI 的 Codex 模型来增强或自动化工作流的开发者、技术团队以及 AI 应用构建者。

该仓库解决了插件开发中缺乏标准化模板和最佳实践的问题，通过提供从简单到丰富的多个示例，让开发者能够快速上手，并理解插件与 Codex 交互的标准方式。

## 核心功能

- **标准化的插件结构**：每个插件都遵循统一的目录组织方式，包含必需的 `plugin.json` 清单文件以及可选的附属组件（如 `skills/`、`commands/` 等）。
- **丰富的示例生态**：内置了多个高质量生产级插件示例，涵盖 Figma、Notion、iOS/Android/macOS 应用构建、Web 开发、Expo 等多个领域。
- **多层级扩展能力**：支持技能（skills）、命令（commands）、代理（agents）、MCP 端点、钩子（hooks）等多种扩展点，允许插件实现复杂的工作流。
- **内置市场机制**：提供默认市场和 API 密钥用户专属市场两个配置入口，便于插件的发现与分发。
- **即开即用的示例**：示例插件包含完整的功能实现代码和配置，开发者可直接运行或作为起点进行二次开发。

## 技术架构

该项目基于 JavaScript 构建，但插件本身可以支持多种语言和框架。其核心架构围绕以下设计原则：

1. **清单驱动**：每个插件的入口是 `.codex-plugin/plugin.json` 文件，定义了插件的基本信息、权限、技能（skills）和 MCP（Model Context Protocol）端点等。Codex 模型通过解析该清单来理解插件的功能边界。
2. **模块化组件**：插件功能被拆分为独立的模块，如 `skills/` 存放具体技能实现、`commands/` 存放命令行交互、`agents/` 存放子代理、`hooks.json` 定义生命周期钩子。这种设计便于维护和复用。
3. **MCP 支持**：部分插件（如 `plugins/netlify`）集成了 MCP 端点，允许插件通过标准协议与外部系统进行结构化数据交换，增强了插件的互操作性。
4. **多市场配置**：通过 `marketplace.json` 和 `api_marketplace.json` 两个配置文件，实现了普通用户与 API 用户的不同访问权限控制，体现了对安全性和访问控制的考量。

## 安装与使用

1. **克隆仓库**：
   ```bash
   git clone https://github.com/openai/plugins.git
   cd plugins
   ```

2. **选择目标插件**：
   进入 `plugins/` 目录，选择一个感兴趣的示例，例如：
   ```bash
   cd plugins/notion
   ```

3. **查看清单文件**：
   检查 `.codex-plugin/plugin.json` 以了解该插件的功能和配置要求。

4. **配置环境**：
   根据具体插件的要求，可能需要设置 API 密钥或配置外部服务。例如，对于 `plugins/notion`，需要配置 Notion 集成密钥。

5. **加载插件到 Codex**：
   在 Codex 环境中，通过指定插件路径或使用插件市场功能加载插件。对于本地开发，可以直接在 `marketplace.json` 中添加插件路径。

**最小可用示例**：以 `plugins/hello-world`（假设存在）为例，启动 Codex 后，加载该插件并调用插件定义的技能，即可看到插件响应。

## 适用场景

- **AI 辅助设计开发**：利用 `plugins/figma` 示例，从 Figma 设计稿直接生成代码、创建代码连接（Code Connect）或应用设计系统规则。
- **智能项目管理**：基于 `plugins/notion` 示例，构建用于项目规划、会议记录、研究资料收集和知识管理的 AI 助手。
- **跨平台应用开发**：参考 `plugins/build-ios-apps`、`plugins/build-macos-apps` 和 `plugins/expo`，实现 SwiftUI 应用、macOS 桌面软件或 React Native 移动项目的开发、调试和构建自动化。
- **全栈 Web 开发**：使用 `plugins/build-web-apps` 和 `plugins/netlify`，自动化部署、UI 开发、支付集成和数据库操作等工作流。

## 项目亮点

- **官方维护与背书**：由 OpenAI 官方发布和维护，确保了示例的最佳实践和代码质量。
- **覆盖广泛领域**：从创意设计到应用开发，从移动端到 Web 端，提供了多领域的完整插件范例。
- **高度可扩展性**：MCP、技能、命令、代理等多层次扩展机制，让插件不仅能做简单动作，还可以编排复杂工作流。
- **降低学习曲线**：统一的目录结构和清单规范，使开发者能够快速迁移经验，从理解一个插件到创建新插件的成本极低。

与同类项目相比，该仓库不仅是代码集合，更是一套完整的插件开发标准和生态系统参考，对 Codex 平台的深度使用者尤其有价值。

## 相关链接

- [GitHub 仓库](https://github.com/openai/plugins)
