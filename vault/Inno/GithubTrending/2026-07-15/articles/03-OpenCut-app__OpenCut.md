---
tags:
  - trending
  - article
repo: OpenCut-app/OpenCut
date: 2026-07-15
language: TypeScript
stars_total: 69446
stars_today: 4276
---
## 项目概述

OpenCut 是一款完全免费开源的视频编辑软件，旨在成为 CapCut（剪映国际版）的开源替代方案。该项目支持 Web、桌面和移动端，让用户无需付费即可享受专业级的视频编辑体验。OpenCut 的目标用户包括视频创作者、内容生产者、教育工作者以及任何需要便捷、强大视频编辑工具的个人或团队。与 CapCut 等闭源工具不同，OpenCut 赋予用户完全的控制权和隐私保护，所有代码均以 MIT 许可证开源。

## 核心功能

- **多平台支持**：从单一代码库同时支持浏览器、桌面（Windows/macOS/Linux）和移动端（Android/iOS），用户可在任何设备上无缝编辑视频。
- **编辑器 API**：提供可编程的编辑器接口，允许开发者通过代码控制视频编辑流程，实现自动化操作。
- **第三方插件系统**：采用以插件优先的架构设计，支持第三方开发者创建和分享扩展，极大丰富编辑器的功能生态。
- **MCP 服务器**：内置 MCP（Model Control Protocol）服务器，使 AI 代理能够与编辑器交互，实现智能化的视频编辑辅助。
- **无头模式**：支持无图形界面的自动化模式，可用于批量渲染、脚本化处理和服务端视频生成。
- **内置脚本面板**：在编辑器中直接提供脚本编写和执行界面，用户可编写自定义脚本实现高级编辑逻辑。

## 技术架构

OpenCut 采用 Rust 作为核心开发语言，通过跨平台编译实现 Web、桌面和移动端的统一代码基础。前端使用 TypeScript 开发，确保类型安全性和开发效率。项目结构如下：

- **Rust 核心**：处理视频解码/编码、渲染管线、时间轴逻辑等性能敏感部分，通过 FFI 或 WebAssembly 与上层交互
- **Web 应用**：基于现代前端框架（如 React/Vue）构建，通过浏览器原生 API 或 WASM 调用 Rust 核心
- **桌面应用**：使用 Tauri 或 Electron 等技术封装，提供原生性能和系统集成能力
- **移动端**：通过跨平台框架（如 React Native）或 Rust 原生绑定实现

当前项目正在进行全面重写，目标是实现插件优先架构，为第三方开发者提供一流的扩展支持。新版本还将引入 Editor API，使程序化控制和自动化编辑成为可能。

## 安装与使用

**注意：当前稳定版本为 classic 分支，新版本正在开发中。以下指南适用于开发版。**

### 环境要求
- 安装 [proto](https://moonrepo.dev/proto) 工具管理器
- Node.js（推荐 v18+）
- Rust 工具链（用于编译核心库）

### 快速开始

```bash
# 安装 proto 工具管理器
bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)

# 克隆仓库
git clone https://github.com/OpenCut-app/OpenCut.git
cd OpenCut

# 安装项目所需工具
proto use

# 启动 Web 开发服务器
moon run web:dev   # 访问 http://localhost:5173

# 启动 API 服务器（可选，用于后端功能）
moon run api:dev   # 访问 http://localhost:8787

# 启动桌面应用（查看 apps/desktop/README.md 获取具体说明）
moon run desktop:dev
```

### 基本使用示例
- 打开 Web 版后，通过拖拽导入视频、音频和图片素材
- 在时间轴上剪辑片段、添加转场和效果
- 使用内置脚本面板执行自定义编辑逻辑（新版本特性）
- 通过 API 调用实现程序化渲染（适用于自动化场景）

## 适用场景

- **个人视频创作**：为 YouTuber、Vlog 创作者、短视频制作者提供免费且强大的编辑工具，避免订阅费用
- **教育与培训**：学校和培训机构可部署自有视频编辑环境，无需购买商业许可证，学生可随时访问
- **自动化视频生产**：企业通过无头模式和 API 实现批量视频生成，用于广告、社交媒体内容或数据可视化
- **AI 集成开发**：开发者利用 MCP 服务器和插件系统，为 AI 代理赋予视频编辑能力，构建智能内容工作流

## 项目亮点

- **真正开源免费**：以 MIT 许可证发布，无任何隐藏收费或限制，社区可自由修改和分发
- **跨平台统一体验**：从浏览器到桌面再到手机，使用同一套代码和功能，学习成本低
- **插件优先架构**：不同于大多数视频编辑器，OpenCut 将插件系统作为核心设计，鼓励社区贡献和生态建设
- **AI 友好设计**：内置 MCP 服务器和脚本面板，天然支持与 AI 代理和自动化工具集成
- **企业级可扩展性**：无头模式和编辑器 API 使其不仅适合个人使用，也能支撑团队协作和自动化流水线

## 相关链接

- [GitHub 仓库](https://github.com/OpenCut-app/OpenCut)
- [经典版仓库](https://github.com/opencut-app/opencut-classic)
- [官方网站](https://opencut.app)
- [新版本预览](https://new.opencut.app)
- [Discord 社区](https://discord.gg/zmR9N35cjK)
- [Twitter/X 账号](https://x.com/opencutapp)
