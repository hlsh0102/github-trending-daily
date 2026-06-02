---
tags:
  - trending
  - article
repo: nesquena/hermes-webui
date: 2026-06-02
language: Python
stars_total: 11705
stars_today: 945
---
## 项目概述

Hermes WebUI 是一个轻量级的网页用户界面，专为 Hermes Agent 设计。Hermes Agent 是由 Nous Research 开发的智能自主代理，它运行在用户的服务器上，可通过终端或消息应用进行访问。该代理具有持续学习的能力——它会记住学到的知识，运行时间越长，能力就越强。

Hermes WebUI 解决了 Hermes Agent 仅通过终端交互的不便，为用户提供了一个美观、易用的浏览器界面。无论是桌面电脑还是手机，用户都能通过这个暗色主题的 Web 应用，完整地操控 Hermes Agent。目标用户包括对自主 AI Agent 感兴趣的开发者、研究人员，以及任何希望在浏览器中便捷管理 AI 助手的用户。

## 核心功能

- **三栏式布局**：左侧边栏用于会话列表和导航，中央区域进行聊天对话，右侧面板浏览工作区文件，一目了然。
- **完整的 CLI 功能对等**：无需记住命令，通过 WebUI 可完成终端中的所有操作，包括模型选择、配置文件管理和工作区文件操作。
- **Composer 底部栏**：模型切换、配置文件选择和 workspace 控制始终可见，方便在编辑消息时快速调整。
- **上下文环（Context Ring）**：圆形视觉指示器，实时展示当前会话的 Token 使用情况，帮助控制上下文窗口。
- **Hermes 控制中心（Hermes Control Center）**：位于左侧边栏底部的启动器，可访问所有设置、会话管理工具和其他高级功能。
- **双主题支持**：除了默认的暗色主题，还提供完整的亮色模式，适应不同使用环境。

## 技术架构

Hermes WebUI 的设计哲学是极简且高效：**无需构建步骤、无需前端框架、无需打包工具**。整个项目仅由 Python 后端和原生的 Vanilla JS 前端构成。

- **后端**：使用 Python 构建的 HTTP 服务器，负责与 Hermes Agent 通信，处理会话管理、文件操作和设置持久化。
- **前端**：纯手工编写的原生 JavaScript 和 CSS，不依赖 React、Vue 等现代框架，确保了极快的加载速度和极小的体积。
- **通信协议**：通过 REST API 或 WebSocket 实现前后端通信，实时推送代理执行结果和状态更新。
- **部署方式**：可直接作为 Python 脚本运行，无需 Docker 或复杂的配置，适合在开发环境或生产服务器上快速启动。

## 安装与使用

安装 Hermes WebUI 非常简单，仅需几步：

1. **克隆仓库**：
   ```bash
   git clone https://github.com/nesquena/hermes-webui.git
   cd hermes-webui
   ```

2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **配置 Hermes Agent**：确保本地已经安装并运行了 Hermes Agent，并获取其 API 端口（默认为 8080）。

4. **启动 WebUI**：
   ```bash
   python server.py
   ```

5. **访问界面**：打开浏览器，访问 `http://localhost:5000`（或根据终端提示的地址）。

**最小可用示例**：启动后，你在左侧边栏可以创建新的会话，在中央聊天区输入消息，Hermes Agent 会以自主代理的模式进行响应。右侧面板可浏览工作区中的文件，点击即可查看或编辑。底部的 Composer 栏让你随时调整模型版本，上下文环则显示 Token 使用进度。

## 适用场景

- **远程 AI 助手管理**：在手机或平板上通过浏览器访问，随时随地与 Hermes Agent 交互，无需 SSH 或终端模拟器。
- **多模型实验**：在 WebUI 中快速切换不同模型配置，比较 Hermes Agent 在多种参数下的行为和输出质量。
- **工作区文件协作**：利用右侧文件浏览器，直接在会话中引用、编辑或创建工作区内的文件，适合一边聊天一边完成编程或写作任务。
- **教育与演示**：将 Hermes WebUI 部署在展示环境，让团队成员或学生体验自主 AI Agent 的能力，无需学习复杂的命令行操作。

## 项目亮点

与同类项目相比，Hermes WebUI 的差异化优势十分明显：

- **零构建流程**：不需要 Node.js、npm、webpack 等繁琐的工具链。安装完 Python 依赖就能运行，对运维极其友好。
- **完整功能对等**：不是 CLI 的简化版或阉割版，所有 Hermes Agent 的功能都能在 WebUI 中执行，包括高级会话管理、配置文件选择和工作区操作。
- **移动端友好**：暗色主题和响应式布局让手机浏览器也能获得良好体验，适合随时随地使用。
- **极简代码体积**：仅由 Python 和原生 JS 构成，没有臃肿的第三方框架依赖，易于定制和贡献。
- **实时 Token 监控**：独特的上下文环设计，将抽象的技术指标转化为直观的视觉反馈，帮助用户更好地控制成本和质量。

## 相关链接

- [GitHub 仓库](https://github.com/nesquena/hermes-webui)
- [Hermes Agent 官方网站](https://hermes-agent.nousresearch.com/)
