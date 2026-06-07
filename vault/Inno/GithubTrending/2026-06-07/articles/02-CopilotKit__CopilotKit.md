---
tags:
  - trending
  - article
repo: CopilotKit/CopilotKit
date: 2026-06-07
language: TypeScript
stars_total: 33367
stars_today: 631
---
## 项目概述

CopilotKit 是一套专为构建“代理原生（Agent-Native）”应用而设计的前端技术栈。它解决了传统前端应用难以与 AI 智能体（Agent）深度集成的问题——开发者往往需要自己处理状态同步、流式渲染、人工审核等复杂逻辑。CopilotKit 提供了开箱即用的生成式 UI 组件、共享状态管理以及人机协作工作流，让开发者能够在 React、Angular、Vue、React Native 等主流框架上快速搭建具备 AI 交互能力的应用。

目标用户包括前端开发者、全栈工程师以及希望将 AI 智能体嵌入到现有产品中的团队，尤其适合那些需要构建聊天界面、表单自动化、数据问答系统或复杂工作流审批的应用场景。

## 核心功能

- **框架无关的前端集成**：支持 React、Angular、Vue、React Native 以及 Slack、移动端等多平台，无需后端改造即可嵌入 AI 交互层。
- **生成式 UI 组件**：智能体可以动态生成并嵌入自定义 UI 组件，例如表格、图表、表单或按钮，实现真正的“AI 驱动界面”而非纯文本对话。
- **共享状态管理**：AI 智能体可以读取和修改前端应用中的状态（如表单字段、列表数据），实现双向实时同步，无需手动对接 API。
- **人机协作工作流**：内置 Human-in-the-Loop（人机回环）支持，智能体生成的响应可配置为“需要用户确认后执行”，适用于审批、编辑等场景。
- **流式响应与分步渲染**：支持 AI 输出的逐步渲染，用户可实时看到思考过程和中间结果，提升交互透明度和体验。
- **AG-UI 协议**：作为项目核心理念，定义了一套标准化的接口，使智能体能够以统一方式操作前端 UI，降低集成成本。

## 技术架构

CopilotKit 的核心是一套基于 TypeScript 开发的前端运行时（Runtime），它抽象了与 AI 后端的通信协议，并通过插件化架构适配不同框架。技术特点包括：

- **协议驱动设计**：采用 AG-UI 协议，将智能体的操作请求封装为结构化指令（如“更新表格行”、“显示确认对话框”），前端组件根据指令渲染对应 UI，实现解耦。
- **状态同步层**：通过 React 的 Context 或 Vue 的 Provide/Inject 机制，将 AI 可操作的状态暴露给智能体，同时监听状态变化并自动推送，保证前端与 AI 逻辑的一致性。
- **组件注册系统**：开发者可以注册自定义 UI 组件，智能体通过组件名称和参数动态调用，支持复杂嵌套布局。
- **流式渲染引擎**：基于 JavaScript 事件循环与异步迭代器，将 AI 输出的数据流分片解析并递进渲染，避免阻塞主线程。

## 安装与使用

以 React 项目为例，安装基础包：

```bash
npm install @copilotkit/react-core @copilotkit/react-ui
```

在应用入口处配置 CopilotKit 提供者：

```jsx
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

function App() {
  return (
    <CopilotKit runtimeUrl="https://your-ai-api.com">
      <CopilotSidebar>
        <YourMainApp />
      </CopilotSidebar>
    </CopilotKit>
  );
}
```

在需要 AI 访问状态的组件中，使用 `useCopilotAction` 定义可被智能体调用的操作：

```jsx
import { useCopilotAction } from "@copilotkit/react-core";

function TaskList() {
  useCopilotAction({
    name: "addTask",
    description: "添加一个新任务",
    parameters: [
      { name: "title", type: "string", description: "任务标题" },
    ],
    handler: async ({ title }) => {
      // 添加任务到本地状态
    },
  });

  return <div>...</div>;
}
```

之后用户即可通过对话窗口向 AI 发出指令，AI 将自动调用注册的操作并更新 UI。

## 适用场景

- **智能表单与数据录入**：用户通过自然语言填写复杂表单（如保险申请、调查问卷），AI 自动映射字段并实时校验，减少手动操作。
- **AI 驱动的管理后台**：在仪表盘或 CRUD 应用中，用户可直接对 AI 说“显示上个月销售额最高的产品”，AI 查询数据后以图表形式动态渲染。
- **工作流审批系统**：员工提交申请后，AI 自动生成审批意见并推送给管理者，管理者可在对话中直接修改或驳回，所有操作同步回后台。
- **聊天机器人升级为应用智能体**：将传统问答机器人扩展为能直接操作电商购物车、银行转账、订票系统等真实业务的智能助手。

## 项目亮点

- **多框架统一封装**：与仅支持单一框架的类似项目不同，CopilotKit 提供了标准化的 API 适配层，允许同一套 AI 逻辑运行在 Web、移动端甚至 Slack 中。
- **状态共享而非仅对话框**：多数工具仅提供聊天 UI，而 CopilotKit 让 AI 能直接操作应用内部状态，实现真正的“嵌入式智能体”。
- **灵活的人机回环**：可精细控制哪些操作需要人工确认、哪些可以自动执行，平衡效率与安全。
- **活跃的社区与开源生态**：GitHub 3.3 万+ Star，MIT 许可，且已形成多个贡献者驱动的插件和示例。

## 相关链接

- [GitHub 仓库](https://github.com/CopilotKit/CopilotKit)
- [官方文档](https://docs.copilotkit.ai/?ref=github_readme)
- [示例项目](https://www.copilotkit.ai/examples)
- [Discord 社区](https://discord.gg/6dffbvGU3D?ref=github_readme)
