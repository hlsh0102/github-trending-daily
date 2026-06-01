---
tags:
  - trending
  - article
repo: nesquena/hermes-webui
date: 2026-06-01
language: Python
stars_total: 10257
stars_today: 357
---
## 项目概述

Hermes WebUI 是一个轻量级、暗色主题的网页界面，为 [Hermes Agent](https://hermes-agent.nousresearch.com/) 提供浏览器端的交互入口。Hermes Agent 是一个运行在服务器上的自主智能体，它能够通过终端或即时通讯应用进行访问，并具备记忆和学习能力，运行时间越长能力越强。Hermes WebUI 的目标是让用户在浏览器中获得与命令行终端完全一致的使用体验，无需安装额外工具即可随时随地管理 Hermes Agent。该界面采用纯 Python 后端与原生 JavaScript 前端构建，无构建步骤、无框架、无打包工具，追求极致的简洁与性能。

## 核心功能

- **完整的 CLI 功能对应**：支持 Hermes Agent 所有终端操作，包括会话管理、模型调用、文件操作等，实现零功能损失的 Web 转移。
- **三面板布局**：左侧边栏用于会话列表和导航，中央区域用于对话交互，右侧面板用于工作区文件浏览。
- **Composer 底部栏**：模型选择、个人资料切换、工作区控制等核心操作始终可见，方便在编写消息时快速调整。
- **圆形上下文环**：直观显示当前对话的 token 使用情况，帮助用户控制成本与上下文窗口。
- **Hermes 控制中心**：通过侧边栏底部启动器访问，集中管理所有设置、会话工具和配置项。
- **多主题支持**：内置暗色与亮色主题，并支持完整的个人资料配置，适应不同使用环境。

## 技术架构

Hermes WebUI 的技术设计遵循极简主义原则：

- **后端**：使用 Python 构建，直接与 Hermes Agent 的核心服务通信，无需额外的中间件或消息队列。
- **前端**：采用原生 JavaScript（Vanilla JS），不依赖 React、Vue 等现代框架，也不使用 WebPack 等构建工具，实现零编译、零依赖的快速加载。
- **通信协议**：通过轻量级的 HTTP/WebSocket 与 Hermes Agent 进行实时双向通信，确保低延迟的对话体验。
- **状态管理**：会话状态和用户配置直接保存在浏览器本地存储或服务端会话文件中，无需数据库支持，降低部署复杂度。
- **文件系统集成**：右侧面板直接映射到服务器工作区目录，支持文件浏览、查看和简单编辑，无需额外文件同步机制。

这种架构选择使得项目具备极高的可移植性和易部署性，任何支持 Python 3 的环境都能直接运行。

## 安装与使用

### 安装步骤

1. **确保 Hermes Agent 已运行**：首先需要部署并运行 [Hermes Agent](https://hermes-agent.nousresearch.com/)，确保其 API 或 WebSocket 接口可用。

2. **克隆仓库**：
   ```bash
   git clone https://github.com/nesquena/hermes-webui.git
   cd hermes-webui
   ```

3. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

4. **启动 WebUI**：
   ```bash
   python app.py
   ```

5. **访问界面**：在浏览器中打开 `http://localhost:5000` 即可使用。

### 最小可用示例

假设 Hermes Agent 运行在 `localhost:8000`，只需在启动 WebUI 前设置环境变量或修改配置文件：
```bash
export HERMES_API_URL=http://localhost:8000
python app.py
```
启动后即可在浏览器中创建新会话、选择模型、发送消息，并实时看到智能体的回复。右侧面板能直接浏览和管理服务器上的工作区文件。

## 适用场景

- **远程管理智能体**：当开发者无法通过 SSH 或终端访问服务器时，使用手机或平板的浏览器即可管理 Hermes Agent，查看对话历史、调整模型参数。
- **团队协作**：同一服务器上的多个用户可通过 WebUI 共享同一个 Hermes Agent 实例，各自维护独立的会话记录，适用于团队内部的知识库查询或自动化任务。
- **快速原型与调试**：无需安装任何客户端工具，仅需浏览器即可快速测试 Hermes Agent 的能力，适合在演示或临时实验环境中使用。
- **无头服务器运维**：对于没有图形界面的云服务器，WebUI 提供了直观的交互方式，运维人员可以通过任意设备轻松与智能体对话。

## 项目亮点

- **零配置部署**：无需 Node.js、npm、Webpack 等前端工具链，仅需 Python 和浏览器即可运行，降低入门门槛。
- **完整的 CLI 替代方案**：与 Hermes Agent 的终端接口完全一致，不牺牲任何功能，提供无缝迁移体验。
- **极简性能**：不依赖重框架，页面加载快，交互响应迅速，即使在低端设备或弱网环境下也能流畅使用。
- **深色主题设计**：默认暗色界面减少眼睛疲劳，同时提供亮色模式，满足不同喜好和使用场景。
- **开源与社区驱动**：基于 MIT 许可证发布，代码完全透明，社区可以自由贡献、修改和扩展。

## 相关链接

- [GitHub 仓库](https://github.com/nesquena/hermes-webui)
- [Hermes Agent 官网](https://hermes-agent.nousresearch.com/)
