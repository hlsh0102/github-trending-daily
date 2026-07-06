---
tags:
  - trending
  - article
repo: alibaba/page-agent
date: 2026-07-06
language: TypeScript
stars_total: 24182
stars_today: 805
---
## 项目概述

Page Agent 是一个基于 JavaScript 的页面内 GUI 代理工具，允许用户通过自然语言直接控制网页界面。该项目由阿里巴巴开源，主要解决了传统网页自动化工具依赖浏览器扩展、Python 环境或无头浏览器的痛点，将智能代理直接嵌入到网页中运行。目标用户包括前端开发者、自动化测试工程师、AI 应用开发者以及希望简化网页操作的普通用户。

## 核心功能

- **轻量集成**：无需安装浏览器扩展、Python 环境或无头浏览器，仅需引入一个 JavaScript 脚本即可在任意网页中运行。
- **文本驱动**：基于文本的 DOM 操作机制，不依赖屏幕截图或多模态大语言模型，因此不需要额外的视觉识别权限。
- **自定义 LLM**：支持用户自带大语言模型（LLM），可以选择 OpenAI、Anthropic 或其他兼容的 API 服务。
- **页面内操作**：所有交互在用户当前浏览的页面内完成，无需切换到后台或独立的控制面板。
- **可选扩展支持**：提供了 Chrome 扩展选项，用于处理需要跨页面或多标签页的复杂任务。
- **开源与模块化**：采用 TypeScript 开发，遵循 MIT 开源协议，代码结构清晰，便于二次开发和定制。

## 技术架构

Page Agent 的核心设计基于纯前端 JavaScript 运行环境，不依赖任何后端服务或浏览器原生 API 之外的能力。其技术特点包括：

- **DOM 代理层**：通过解析网页的 DOM 结构，构建一个可被 LLM 理解的文本表示，替代传统的截图+VLM（视觉语言模型）方案。
- **动作执行引擎**：将 LLM 返回的文本指令（如“点击提交按钮”“在搜索框输入关键词”）映射为标准的 DOM 操作方法，直接操作页面元素。
- **状态管理**：维护当前页面的上下文状态，支持多步骤操作的记忆与连贯执行。
- **适配器模式**：通过统一的 LLM 适配器接口，支持接入不同厂商的大语言模型服务，用户只需配置 API Key 和模型名称即可使用。

## 安装与使用

### 安装

通过 npm 安装：

```bash
npm install page-agent
```

或直接在 HTML 中引入 CDN 脚本：

```html
<script src="https://cdn.jsdelivr.net/npm/page-agent/dist/page-agent.min.js"></script>
```

### 最小可用示例

在浏览器控制台或脚本中初始化 Page Agent：

```javascript
import { PageAgent } from 'page-agent';

const agent = new PageAgent({
  llm: {
    provider: 'openai',  // 或 'anthropic' 等
    apiKey: 'your-api-key',
    model: 'gpt-4o-mini'
  }
});

// 用自然语言控制页面
await agent.execute('点击页面上的“登录”按钮');
await agent.execute('在用户名输入框输入 admin');
```

对于浏览器直接使用，Page Agent 会自动挂载到全局对象 `window.PageAgent`，无需额外配置构建工具。

## 适用场景

- **网页自动化测试**：开发者和 QA 工程师可以使用自然语言编写测试用例，代替复杂的 Selenium 或 Playwright 脚本。
- **RPA 场景**：在不需要安装专门软件的网页上执行重复操作，如批量数据录入、表单填写等。
- **AI 辅助工具**：为智能助手或聊天机器人提供网页操作能力，使其可以作为“行为代理”替用户完成网页操作。
- **快速原型验证**：在开发过程中快速测试页面交互逻辑，无需编写完整的代码实现。

## 项目亮点

Page Agent 与同类项目（如 Playwright、Puppeteer、Browser Use 等）相比，具有以下差异化优势：

- **零环境依赖**：不需要无头浏览器、Python 环境或浏览器扩展（可选），一个 `<script>` 标签即可启动。
- **无视觉模型依赖**：通过文本 DOM 操作而非截图识别，大幅降低推理成本（无需多模态模型），同时避免 CORS 或权限问题。
- **页面内运行**：用户无需切换到外部工具或后台进程，所有操作都在当前浏览页面上实时可见，便于调试和人工介入。
- **开源友好**：MIT 协议允许商业使用，TypeScript 全量类型定义，文档齐全且有在线 Demo 可直接体验。

## 相关链接

- [GitHub 仓库](https://github.com/alibaba/page-agent)
- [在线 Demo](https://alibaba.github.io/page-agent/)
- [官方文档](https://alibaba.github.io/page-agent/docs/introduction/overview)
- [Chrome 扩展文档](https://alibaba.github.io/page-agent/docs/features/chrome-extension)
