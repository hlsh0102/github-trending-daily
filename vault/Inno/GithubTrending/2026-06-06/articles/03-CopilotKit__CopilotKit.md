---
tags:
  - trending
  - article
repo: CopilotKit/CopilotKit
date: 2026-06-06
language: TypeScript
stars_total: 32801
stars_today: 366
---
## 项目概述

CopilotKit 是一个为智能体（Agent）和生成式 UI 打造的完整前端技术栈。它解决了在现有前端应用中集成智能助手和 AI 生成界面的核心难题——开发者无需从零构建对话架构、状态管理或 UI 渲染引擎，即可快速为 React、Angular、Vue 等框架的应用添加“AI 副驾驶”能力。目标是让任何 Web 应用拥有类似于 Copilot 的智能交互体验，让前端开发者能够像搭建普通组件一样集成 AI 功能。

## 核心功能

- **生成式 UI（Generative UI）**：AI 不仅输出文本，还能动态生成可交互的 UI 组件（如表格、图表、表单），并嵌入到应用界面中
- **共享状态**：智能体与应用前端共享状态，AI 能读取和修改应用的数据层，实现真正的“镶嵌式”交互
- **人机协同工作流（Human-in-the-Loop）**：支持 AI 在执行关键操作前请求用户确认，或由用户修改 AI 建议的步骤后再执行
- **多框架支持**：提供 React、Angular、Vue、React Native 的官方集成，并可通过 AG-UI 协议扩展到其他平台
- **开箱即用的对话界面**：内置可定制的聊天组件，支持流式响应、上下文记忆和富媒体交互
- **云服务与自托管双模式**：既可使用 CopilotKit 云服务快速部署，也支持自托管后端，满足数据隐私需求

## 技术架构

CopilotKit 采用分层架构设计，核心分为三个层面：

1. **运行时（Runtime）层**：管理智能体与前端之间的通信协议（AG-UI 协议），处理对话状态、流式数据推送和动作分发。这是整个框架的骨架，不依赖具体 UI 框架
2. **前端集成层**：为 React、Angular、Vue 等框架提供 SDK。每个 SDK 封装了运行时接口，以组件化（如 `<CopilotKit>`）或 Hooks 的形式暴露给开发者，自动处理数据绑定和生命周期
3. **UI 组件库**：提供默认的聊天窗口、气泡、输入框等可复用组件，并支持完全自定义样式和交互逻辑

项目使用 TypeScript 编写，强调类型安全。设计上遵循“约定优于配置”原则：开发者只需将应用状态（如 Redux Store、React State）通过适配器暴露给 CopilotKit 运行时，AI 即可自动感知并操作这些状态。与后端 LLM 的通信通过标准 HTTP/SSE 流完成，可对接 OpenAI、Anthropic 等模型，也支持自建模型服务。

## 安装与使用

### 安装（以 React 为例）

```bash
npm install @copilotkit/react-core @copilotkit/react-ui
```

### 最小可用示例

在 React 应用中添加一个基本的 AI 聊天助手：

```jsx
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

// 包裹应用根组件
function App() {
  return (
    <CopilotKit runtimeUrl="/api/copilotkit">
      <MyApp />
      <CopilotChat /> {/* 自动出现在右下角 */}
    </CopilotKit>
  );
}
```

然后启动一个兼容 CopilotKit 的后端（如使用 OpenAI 的 Node.js 服务），即可获得一个完整的对话助手，支持流式回答和上下文记忆。

## 适用场景

- **SaaS 应用内置 AI 助手**：为 CRM、项目管理、数据仪表盘等产品添加一个能理解当前页面上下文、辅助操作的新手引导或数据分析助手
- **自动化工作流编排**：结合人机协同，让 AI 分析业务数据后生成操作步骤，用户确认后再执行（如批量邮件发送、账单处理）
- **非技术用户的交互界面**：动态生成表单、图表等 UI 组件，通过自然语言完成复杂操作（如“生成过去三个月的销售趋势图”）
- **教育和文档工具**：嵌入交互式教程，AI 可以根据用户提问实时生成代码示例或操作演示

## 项目亮点

- **前端原生智能体**：不同于传统 AI 聊天框只输出文本，CopilotKit 的智能体能够直接操作前端状态和 UI，使 AI 像“同事”一样与应用共同工作
- **框架无关化设计**：通过 AG-UI 协议解耦运行时与 UI 层，在 React 之外也支持 Angular、Vue，甚至非浏览器环境
- **开发者体验优先**：零配置接入，只需几行代码即可获得完整对话界面，且完全可定制；附带的文档和示例仓库覆盖了从入门到高级的所有场景
- **人机协同的深度支持**：内置确认、修改、暂停等交互模式，确保 AI 不能随意执行危险操作，兼顾效率与安全
- **生态成熟**：MIT 许可证，社区活跃（Discord 数千人），持续贡献新的功能组件和可复用工具包

## 相关链接

- [GitHub 仓库](https://github.com/CopilotKit/CopilotKit)
- [官方文档](https://docs.copilotkit.ai/?ref=github_readme)
- [示例与演示](https://www.copilotkit.ai/examples)
- [Discord 社区](https://discord.gg/6dffbvGU3D?ref=github_readme)
