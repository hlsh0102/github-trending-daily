---
tags:
  - trending
  - article
repo: openai/plugins
date: 2026-09-10
language: JavaScript
stars_total: 6294
stars_today: 498
---
## 项目概述

`openai/plugins` 是 OpenAI 官方维护的 Codex 插件示例集合仓库。它解决的问题是：Codex 作为编程智能体，其能力扩展过去缺乏统一的组织规范与可复用的示例参考。该仓库通过提供一批经过整理、结构规范的插件样例，展示了如何为 Codex 定义技能（skills）、命令（commands）、MCP 服务、代理（agents）以及钩子（hooks）等扩展点。

目标用户主要是三类人群：一是希望为自身工作流定制 Codex 能力的开发者；二是需要将第三方服务（如 Figma、Notion、Netlify）接入 Codex 的工具团队；三是想了解 Codex 插件规范与最佳实践的技术决策者。仓库中每个插件都放在 `plugins/<name>/` 目录下，便于逐个研究或直接复用。

## 核心功能

- **标准化插件清单**：每个插件必须包含 `.codex-plugin/plugin.json` 清单文件，统一声明插件的元信息、入口与依赖，降低集成成本。
- **多扩展面支持**：插件可附带 `skills/`、`agents/`、`commands/`、`hooks.json`、`.app.json`、`.mcp.json`、`assets/` 等多种伴随目录与文件，覆盖从提示词技能到外部进程调用的完整链路。
- **市场（Marketplace）机制**：默认市场位于 `.agents/plugins/marketplace.json`，指向标准 `plugins/` 目录；API key 登录用户则使用独立的 `.agents/plugins/api_marketplace.json`，实现不同认证模式的插件分发隔离。
- **丰富的示例插件**：包含 Figma、Notion、build-ios-apps、build-macos-apps、build-web-apps、Expo、Netlify、Remotion、Google Slides 等，覆盖设计协作、知识管理、移动端与 Web 开发、部署与媒体生成等场景。
- **技能与 MCP 结合**：部分插件（如 netlify、remotion、google-slides）同时提供技能与 MCP 后端支持，展示如何将本地能力与远程服务组合使用。

## 技术架构

仓库以 JavaScript 为主要语言，但插件的核心抽象并不绑定具体运行时。整体设计围绕“清单驱动 + 伴随资源”展开：`.codex-plugin/plugin.json` 作为单一事实来源描述插件身份与结构，其余目录按需提供具体能力。

`skills/` 承载可复用的提示词与工具封装；`agents/` 与 `commands/` 用于定义交互式代理与可调用命令；`hooks.json` 用于在特定生命周期事件上挂载行为；`.mcp.json` 则用于声明 Model Context Protocol 服务，使插件能够接入外部进程或远端 API。市场文件 `.agents/plugins/marketplace.json` 与 `.agents/plugins/api_marketplace.json` 采用两级分发设计，区分普通登录与 API key 登录两类用户，避免插件可见性与认证方式冲突。

这种架构的取舍在于：将大部分复杂性下沉到文件约定，而不是运行时框架，因此插件作者只需按目录结构组织资源，即可被 Codex 识别与加载。

## 安装与使用

该仓库本身是示例集合，通常不需要“安装”整个仓库，而是按需取用某个插件。基本流程如下：

1. 克隆仓库：

   ```
   git clone https://github.com/openai/plugins.git
   ```

2. 进入目标插件目录查看清单，例如：

   ```
   cd plugins/figma
   cat .codex-plugin/plugin.json
   ```

3. 根据清单声明的依赖与伴随文件，将插件纳入你的 Codex 工作区或市场配置中。若插件依赖 MCP 服务，需按 `.mcp.json` 的声明配置对应服务端。

最小可用示例可参考 `plugins/figma` 或 `plugins/notion`：阅读其 `plugin.json` 了解入口，再查看 `skills/` 下的技能定义与 `commands/` 中的命令，即可理解一个插件从声明到行为落地的完整路径。API key 用户则应参照 `.agents/plugins/api_marketplace.json` 的结构配置自己的市场文件。

## 适用场景

- **为 Codex 定制专属工作流**：团队可基于示例结构，将内部工具与规范封装成私有插件，统一在 Codex 中调用。
- **第三方 SaaS 集成**：通过 Figma、Notion、Netlify 等示例，学习如何将设计、文档、部署类服务接入智能体。
- **跨平台应用开发辅助**：build-ios-apps、build-macos-apps、build-web-apps、Expo 等插件展示了针对特定技术栈的构建、调试与打包工作流。
- **插件规范研究与教学**：作为官方示例集，适合用于理解 Codex 插件清单、市场与多扩展面的组织方式。

## 项目亮点

与社区零散的插件项目相比，该仓库的差异化优势在于官方背书与规范性：所有示例都遵循同一套清单与目录约定，且同时覆盖技能、命令、代理、钩子与 MCP 多种扩展面，形成较完整的参考矩阵。市场文件对普通登录与 API key 登录用户做区分，体现了对认证差异的考虑。此外，示例选型偏向真实产品（Figma、Notion、Netlify 等），可直接映射到实际工作流，而非玩具样例。仓库当前的关注度也说明其已成为 Codex 插件生态的重要参考入口。

## 相关链接

- [GitHub 仓库](https://github.com/openai/plugins)
