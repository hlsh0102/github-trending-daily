---
tags:
  - trending
  - article
repo: anthropics/claude-plugins-official
date: 2026-06-24
language: Python
stars_total: 30930
stars_today: 77
---
## 项目概述

Claude Code Plugins Directory 是一个由 Anthropic 官方维护的高质量 Claude Code 插件目录。该项目旨在为 Claude Code 用户提供一个集中化的插件发现和安装平台，解决了用户在众多插件中难以找到可靠、高质量插件的痛点。目标用户包括所有使用 Claude Code 的开发者，尤其是希望通过插件扩展 Claude Code 功能的用户。

该目录包含两大类插件：由 Anthropic 团队开发和维护的内部插件（位于 `/plugins` 目录下），以及来自合作伙伴和社区的第三方插件（位于 `/external_plugins` 目录下）。这种分类方式让用户能够清晰区分官方支持与社区贡献的插件来源。

## 核心功能

- **集中化插件发现**：用户可以通过插件目录浏览和搜索所有可用的插件，无需在分散的仓库中寻找。
- **一站式安装**：支持通过 Claude Code 的插件系统直接安装插件，支持 `/plugin install {plugin-name}@claude-plugins-official` 命令或在 `/plugin > Discover` 界面浏览安装。
- **安全提醒机制**：项目明确提醒用户在安装、更新或使用插件前需要确保对插件的信任，并声明 Anthropic 不控制插件中包含的 MCP 服务器、文件或其他软件。
- **标准化插件结构**：每个插件遵循统一的结构规范，包括 `.claude-plugin/plugin.json`（必需）和可选的 `.mcp.json` 配置文件，以及 `commands/` 目录等。
- **贡献与提交流程**：为内部插件和第三方插件提供了不同的提交路径，外部插件需要满足质量和安全标准才能被收录。
- **开源与社区驱动**：项目基于 Apache-2.0 开源许可，鼓励社区贡献和第三方开发。

## 技术架构

项目的技术架构围绕插件目录的结构设计和 Claude Code 的插件系统展开。核心设计思路是：

1. **目录即市场（Directory as Marketplace）**：将一个 Git 仓库设计为可扩展的插件注册表，用户通过 Claude Code 客户端直接与仓库交互，实现插件的发现、安装和更新。

2. **标准化元数据**：每个插件必须包含 `.claude-plugin/plugin.json` 文件，用于声明插件名称、描述、版本、作者等元数据。这种标准化的描述方式使得客户端能够自动解析和呈现插件信息。

3. **MCP 集成**：插件可选的 `.mcp.json` 文件用于配置 MCP（Model Context Protocol）服务器，这是 Claude Code 与外部工具交互的标准协议，允许插件通过标准化的接口集成各种外部服务。

4. **分类隔离**：通过 `/plugins`（内部）和 `/external_plugins`（第三方）两个物理目录实现来源隔离，便于管理和权限控制。

5. **安全模型**：采用明确告知、用户自主决断的安全策略，不强制执行代码审查，而是通过提示和更新机制让用户做出信任决策。

## 安装与使用

安装插件的基本步骤：

1. **确保已安装 Claude Code**：用户需要先安装并配置好 Claude Code 客户端。

2. **使用命令行安装**：在 Claude Code 环境中执行以下命令：
   ```
   /plugin install {plugin-name}@claude-plugins-official
   ```
   将 `{plugin-name}` 替换为具体插件名称。

3. **通过用户界面安装**：在 Claude Code 中打开 `/plugin > Discover` 界面，浏览可用的插件列表，选择需要的插件进行安装。

4. **更新插件**：当插件有更新时，Claude Code 的插件系统会提示用户进行更新。

对于开发者贡献插件：

1. 内部插件：按照 `/plugins/example-plugin` 的参考实现创建插件。
2. 外部插件：通过 [plugin directory submission form](https://clau.de/plugin-directory-submission) 提交申请。
3. 确保插件包含 `.claude-plugin/plugin.json` 等必要文件。

## 适用场景

- **功能扩展**：开发者为 Claude Code 添加特定领域的功能，例如数据库查询、API 调用、代码分析等。
- **工作流集成**：团队将 Claude Code 集成到现有的开发工作流中，通过插件连接 CI/CD 工具、项目管理平台等。
- **企业内部工具**：企业为 Claude Code 开发和管理内部专用的插件，实现私有功能的扩展。
- **社区共建**：开源社区围绕 Claude Code 生态共建插件市场，推动生态发展。

## 项目亮点

与同类项目相比，Claude Code Plugins Directory 的差异化优势包括：

1. **官方背书**：由 Anthropic 官方直接管理和维护，权威性和可靠性更高。
2. **来源透明**：明确区分官方插件和第三方插件，用户能够清晰了解插件来源和可信度。
3. **标准化接入**：基于 MCP（Model Context Protocol）标准，插件能够以统一的方式集成各种外部能力。
4. **安全优先**：虽不强制审查，但通过清晰的安全警告和更新机制，让用户能够做出明智的信任决策。
5. **社区友好**：为第三方贡献提供了清晰的流程和标准，降低了参与门槛。

## 相关链接

- [GitHub 仓库](https://github.com/anthropic/claude-plugins-official)
- [插件提交表单](https://clau.de/plugin-directory-submission)
