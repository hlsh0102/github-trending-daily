---
tags:
  - trending
  - article
repo: openai/plugins
date: 2026-06-07
language: JavaScript
stars_total: 1834
stars_today: 213
---
## 项目概述

OpenAI Plugins 是一个精选的 Codex 插件示例集合，由 OpenAI 官方维护。该项目旨在为开发者提供可直接使用或参考的插件实现模板，帮助用户快速理解 Codex 插件系统的架构和开发模式。每个插件包含必要的 manifest 清单文件以及可选的辅助表面（如 skills/、.app.json、.mcp.json 等），覆盖从设计协作到应用开发的多种场景。目标用户包括希望扩展 Codex 能力的开发者、需要与外部服务集成的团队，以及希望学习插件化开发最佳实践的技术人员。

## 核心功能

- **设计系统集成**：Figma 插件支持 use_figma 命令、Code to Canvas 转换、Code Connect 双向同步以及设计系统规则定义，实现设计与代码的深度打通。
- **知识管理**：Notion 插件涵盖计划制定、研究记录、会议管理和知识捕获功能，将项目管理工具与 AI 开发工作流结合。
- **iOS 应用开发**：SwiftUI 应用构建插件提供实现、重构、性能分析和调试支持，针对 iOS 平台优化开发体验。
- **macOS 应用开发**：macOS 开发插件整合 SwiftUI/AppKit 工作流、构建/运行/调试循环以及打包指南，覆盖桌面应用全生命周期。
- **Web 应用构建**：一站式插件支持部署、UI 开发、支付集成和数据库工作流，简化现代 Web 应用的构建过程。
- **跨平台移动开发**：Expo 插件专门针对 React Native 和 Expo 应用，提供 SDK 升级、EAS 工作流和 Codex Run 操作支持。
- **额外工具集成**：Netlify 部署、Remotion 视频渲染和 Google Slides 演示插件，扩展了 Codex 在媒体与部署领域的能力。

## 技术架构

项目采用模块化插件架构，每个插件独立存放于 `plugins/<name>/` 目录下。核心强制文件为 `.codex-plugin/plugin.json` 清单，它定义了插件的元数据、入口点和权限声明。可选的 companion surfaces 包括：

- `skills/`：定义特定领域能力集
- `.app.json`：应用级配置
- `.mcp.json`：MCP（Model Context Protocol）集成描述
- `agents/`：自定义 AI Agent 逻辑
- `commands/`：命令行接口扩展
- `hooks.json`：事件钩子机制
- `assets/`：资源文件目录

这种分层设计使得插件既保持轻量（只需清单文件即可工作），又具备高度可扩展性。技术栈以 JavaScript 为主（根据仓库语言标识），与 Codex 运行环境自然集成。MCP 协议的使用允许插件声明式地定义与外部工具的交互方式，而 hooks 机制则提供了异步事件驱动能力。

## 安装与使用

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/openai/plugins.git
   ```

2. 选择感兴趣的插件目录，例如 Figma 插件：
   ```bash
   cd plugins/figma
   ```

3. 查看 `.codex-plugin/plugin.json` 文件确认基本配置，并根据需要调整。

4. 将插件目录放置到 Codex 环境可识别的路径，或在 Codex 配置中指定插件路径。

5. 最小可用示例——创建自定义插件：
   - 新建目录 `plugins/my-plugin/`
   - 创建 `.codex-plugin/plugin.json`，内容如下：
     ```json
     {
       "name": "my-plugin",
       "description": "一个简单的自定义插件",
       "skills": ["summary", "translate"]
     }
     ```
   - 可选添加 `skills/` 目录，放入具体的 skill 定义文件。

## 适用场景

- **设计师与开发协作**：当设计团队使用 Figma、开发团队使用 Codex 时，Figma 插件可确保设计变更加速到代码实现，减少沟通成本。
- **全栈 Web 应用开发**：需要快速构建包含前端 UI、支付、数据库后端的原型或 MVP 时，Web 应用构建插件提供一站式的部署和集成流程。
- **移动应用全生命周期管理**：对于使用 Expo 或原生 iOS/macOS 开发的项目，对应插件覆盖从初始化、开发、调试到发布的完整流程。
- **知识库与项目管理自动化**：团队使用 Notion 记录工作内容时，插件能将 AI 辅助的会议摘要、任务分解和知识检索直接融入日常工作流。

## 项目亮点

与独立的第三方插件集合相比，OpenAI Plugins 具备以下差异化优势：

- **官方维护与规范**：由 OpenAI 直接管理，所有示例遵循 Codex 插件的最新规范，避免兼容性问题。
- **丰富的最佳实践**：每个插件不仅是功能实现，更是架构模式的参考，展示了如何正确使用 manifest、skills、MCP 和 hooks 等机制。
- **覆盖广泛场景**：从设计工具（Figma）到云部署（Netlify），从视频创作（Remotion）到演示文档（Google Slides），一次性提供多种跨域集成范例。
- **轻量且可扩展**：最小化插件仅需一个 JSON 文件即可启动，但通过可选的 companion surfaces，能逐步增加复杂度而无须重构现有逻辑。
- **实时活跃维护**：仓库拥有超过 1800 星标，且近期每日保持高增长，说明社区反馈活跃，代码持续更新。

## 相关链接

- [GitHub 仓库](https://github.com/openai/plugins)
