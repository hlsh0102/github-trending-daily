---
tags:
  - trending
  - article
repo: OpenCut-app/OpenCut
date: 2026-07-17
language: TypeScript
stars_total: 74214
stars_today: 3537
---
## 项目概述

OpenCut 是一款免费开源的视频编辑器，旨在成为 CapCut 的替代品。该项目支持 Web、桌面和移动端，让用户无需付费即可获得专业级的视频编辑体验。OpenCut 面向所有需要视频编辑功能的用户，无论是内容创作者、教育工作者，还是普通用户，都可以自由使用、修改和分发这款软件。

目前，OpenCut 正在进行从零开始的全面重写，新版本将带来更强大的功能集和更好的跨平台体验。旧版本依然可用，可以通过 [opencut-app/opencut-classic](https://github.com/opencut-app/opencut-classic) 访问。

## 核心功能

- **跨平台支持**：同一代码库同时支持 Web、桌面和移动端，基于 Rust 核心构建，确保性能和一致性。
- **编辑器 API**：提供编程接口，允许开发者通过代码控制视频编辑流程，实现自动化操作。
- **插件系统**：采用插件优先架构，第三方开发者可以轻松创建和分享扩展功能，丰富编辑器的能力。
- **MCP 服务器**：为 AI 代理提供交互接口，支持通过人工智能进行视频编辑任务。
- **无头模式**：支持自动化渲染和批量处理，适合服务器端或后台运行。
- **脚本标签**：编辑器内直接集成脚本编写界面，用户可以编写 JavaScript 或 TypeScript 脚本来自定义编辑逻辑。

## 技术架构

OpenCut 采用现代技术栈构建，核心部分使用 Rust 语言，利用其高性能和安全性优势。Rust 核心使得同一代码库能够编译为 WebAssembly 运行在浏览器中，也能编译为原生应用运行在桌面和移动设备上。

前端部分使用 TypeScript 开发，结合 Vue 或 React 等现代框架（具体取决于版本），提供流畅的用户界面。项目使用 [moonrepo](https://moonrepo.dev) 作为构建工具链，通过 `proto` 工具管理运行时环境，确保开发一致性。

架构设计上，OpenCut 强调模块化和可扩展性。编辑器核心与 UI 层分离，使得核心功能可以独立于界面进行测试和扩展。新的插件架构允许第三方功能以独立模块形式加载，不影响主程序的稳定性和性能。

## 安装与使用

### 环境准备

OpenCut 使用 [proto](https://moonrepo.dev/proto) 管理开发工具链。首次使用需要安装 proto：

```sh
bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)
```

### 克隆并启动项目

```sh
git clone https://github.com/OpenCut-app/OpenCut.git
cd OpenCut
proto use  # 安装 .prototools 中锁定的工具
# 启动 Web 版本
moon run web:dev  # 访问 localhost:5173
# 启动 API 服务
moon run api:dev  # 访问 localhost:8787
# 启动桌面版本（具体请参考 apps/desktop/README.md）
moon run desktop:dev
```

对于普通用户，可以直接访问 [opencut.app](https://opencut.app) 使用在线版本，无需安装。新版本预览可通过 [new.opencut.app](https://new.opencut.app) 访问。

## 适用场景

- **内容创作**：视频博主、短视频创作者可以使用 OpenCut 进行剪辑、添加特效和字幕，完全免费且没有水印限制。
- **教育培训**：教育机构可以基于 OpenCut 定制视频编辑工具，用于教学视频制作和多媒体课程开发。
- **自动化工作流**：利用无头模式和编辑器 API，实现批量视频处理、自动生成片头片尾、定时渲染等任务，适合内容工厂和媒体公司。
- **开发集成**：开发者可以借助插件系统和脚本标签，为特定行业（如游戏、教育、电商）构建垂直化的视频编辑解决方案。

## 项目亮点

- **完全免费开源**：采用 MIT 许可证，用户可以自由使用、修改和分发，无需担心商业限制或隐藏费用。
- **跨平台一致性**：基于 Rust 核心的多平台支持意味着用户在浏览器、Windows、macOS、Linux 和移动设备上获得一致的编辑体验。
- **AI 就绪**：内置 MCP 服务器使得 AI 代理可以直接与编辑器交互，为未来基于人工智能的视频编辑铺平道路。
- **插件优先架构**：从设计之初就考虑可扩展性，第三方开发者可以轻松贡献功能，形成丰富的生态。
- **活跃的社区**：项目在 GitHub 上拥有超过 74,000 颗星，社区活跃度高，问题响应和版本迭代速度快。

## 相关链接

- [GitHub 仓库](https://github.com/OpenCut-app/OpenCut)
- [OpenCut 官网](https://opencut.app)
- [新版本预览](https://new.opencut.app)
- [Discord 社区](https://discord.gg/zmR9N35cjK)
- [X (Twitter) 账号](https://x.com/opencutapp)
