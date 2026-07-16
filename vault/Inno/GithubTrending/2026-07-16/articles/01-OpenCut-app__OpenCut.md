---
tags:
  - trending
  - article
repo: OpenCut-app/OpenCut
date: 2026-07-16
language: TypeScript
stars_total: 72392
stars_today: 1664
---
## 项目概述

OpenCut 是一款免费开源的视频编辑器，旨在成为 CapCut 的替代品。它支持在 Web、桌面和移动端运行，让用户无需依赖商业软件即可完成视频剪辑工作。项目当前正在从零开始重写，目标用户包括视频创作者、内容制作者、以及需要自动化视频处理的开发者。

## 核心功能

- **多平台支持**：一套代码库同时覆盖浏览器、桌面和移动端，基于 Rust 核心实现。
- **插件优先架构**：提供第一方第三方插件支持，通过插件 API 扩展编辑器能力。
- **编辑器 API**：允许外部程序调用编辑功能，便于集成到工作流中。
- **MCP 服务器**：支持 AI 代理通过协议与编辑器交互，实现智能剪辑。
- **无头模式**：支持自动化处理和批量渲染，无需图形界面。
- **脚本标签**：在编辑器内部集成脚本编写环境，方便用户自定义操作。

## 技术架构

OpenCut 采用 Rust 作为核心语言，确保高性能和跨平台一致性。前端使用 TypeScript 构建，通过统一的代码库实现 Web、桌面和移动端的同步迭代。项目采用单体仓库结构，使用 `moon` 工具管理多个子项目（`web`、`api`、`desktop`）。架构设计强调插件优先，使第三方开发者能轻松扩展功能。MCP 服务器支持 AI 代理接入，无头模式则允许通过命令行或脚本进行批量处理。

## 安装与使用

当前项目处于重写阶段，经典版本仍可通过以下方式使用：

1. **访问在线版**：直接打开 [opencut.app](https://opencut.app) 即可使用经典版本。
2. **本地开发**：
   - 安装 [proto](https://moonrepo.dev/proto) 工具：`bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)`
   - 在仓库根目录运行：`proto use` 安装依赖工具
   - 启动 Web 开发服务器：`moon run web:dev`（默认在 localhost:5173）
   - 启动 API 服务器：`moon run api:dev`（默认在 localhost:8787）
   - 桌面端启动请参考 `apps/desktop/README.md`

最小可用示例：启动 Web 服务后，在浏览器中即可拖入视频素材，进行基本的剪辑、添加效果和导出操作。

## 适用场景

- **个人视频创作**：Vlog、短视频、社交媒体内容的快速剪辑。
- **自动化视频生产**：通过无头模式和 MCP 服务器，实现批量渲染、AI 辅助编辑。
- **插件开发与扩展**：开发者可基于插件 API 构建自定义功能模块。
- **跨平台部署**：同一套代码同时支持 Web、桌面和移动端，适合需要多端触达的项目。

## 项目亮点

- **开源免费**：MIT 许可，无隐藏收费或功能限制。
- **Rust 核心**：提供接近原生的性能，同时保证多平台一致性。
- **插件优先**：从架构层面支持第三方扩展，生态可塑性强。
- **AI 友好**：通过 MCP 服务器直接集成人工智能代理，实现自动化编辑。
- **全栈覆盖**：单仓库管理 Web、API、桌面端，开发体验统一。

## 相关链接

- [GitHub 仓库](https://github.com/OpenCut-app/OpenCut)
- [经典版仓库](https://github.com/opencut-app/opencut-classic)
- [官方网站](https://opencut.app)
- [新版预览](https://new.opencut.app)
- [Discord 社区](https://discord.gg/zmR9N35cjK)
- [Twitter/X](https://x.com/opencutapp)
