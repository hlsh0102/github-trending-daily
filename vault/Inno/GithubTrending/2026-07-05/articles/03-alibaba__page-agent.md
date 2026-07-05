---
tags:
  - trending
  - article
repo: alibaba/page-agent
date: 2026-07-05
language: TypeScript
stars_total: 23282
stars_today: 742
---
## 项目概述

Page Agent 是一个轻量级的 JavaScript 页面内 GUI Agent 工具，允许用户通过自然语言直接控制网页界面。该项目由阿里巴巴开源，旨在解决传统 Web 自动化工具（如 Selenium、Puppeteer）集成复杂、依赖重型浏览器环境或 Python 运行时的问题。它的目标用户包括前端开发者、自动化测试工程师、以及希望快速构建 AI 驱动的 Web 交互应用的团队。Page Agent 的核心价值在于：无需安装浏览器扩展、无需启动无头浏览器、无需依赖多模态大模型，仅通过一行 JavaScript 代码即可让网页听懂“人话”。

## 核心功能

- **自然语言驱动交互**：用户可以直接输入“点击登录按钮”或“填写表单”等指令，Page Agent 会自动解析并执行对应的 DOM 操作。
- **纯文本 DOM 操控**：不依赖截图或图像识别，仅基于页面 HTML 结构和文本内容进行元素定位与操作，避免了对多模态 LLM 或特殊权限的需求。
- **自带大模型支持**：允许用户接入自己的 LLM（如 GPT-4、Claude 等），通过 API 将自然语言指令转化为结构化操作序列。
- **极简集成**：无需安装浏览器扩展、Python 环境或无头浏览器，只需在网页中引入一个 JavaScript 文件即可运行。
- **可选 Chrome 扩展**：针对跨页面任务（如多标签页操作），提供可选的 Chrome 扩展支持，扩展核心能力而无需改变常规使用方式。
- **开源与 MIT 许可**：代码完全开源，可自由修改和商用，降低使用门槛。

## 技术架构

Page Agent 的核心技术架构基于**纯前端 JavaScript 运行环境**。它通过以下方式实现轻量级 GUI 自动化：

1. **DOM 解析与意图映射**：当用户输入自然语言指令后，Page Agent 会调用用户提供的 LLM API，将指令解析为具体的 DOM 操作意图（如 `click`、`type`、`scroll` 等）。然后，它利用浏览器的 `document.querySelector` 和 DOM 遍历能力，结合指令中的文本关键词，定位目标元素。
2. **文本优先的策略**：与传统方案不同，Page Agent 不使用截图或 canvas 渲染。它仅依赖页面的 DOM 树结构和元素的文本内容。这意味着它不需要额外的图像预处理模块，也避免了多模态模型的高昂成本。
3. **事件模拟层**：定位到元素后，Page Agent 会触发浏览器原生事件（如 `click`、`input`），确保与真实用户操作行为一致。
4. **无状态设计**：所有操作均基于当前页面状态。对于跨页面任务，通过 Chrome 扩展维护一个轻量级的上下文状态，但仍保持核心逻辑的轻量化。
5. **模块解耦**：代码采用 TypeScript 编写，核心逻辑封装为独立模块，便于扩展和替换（例如替换 LLM 服务商或更改操作解析策略）。

## 安装与使用

### 安装步骤

1. **通过 npm 安装**（推荐）：
   ```bash
   npm install page-agent
   ```

2. **或通过 CDN 直接引入**：
   ```html
   <script src="https://unpkg.com/page-agent"></script>
   ```

### 最小可用示例

```javascript
import PageAgent from 'page-agent';

// 初始化，传入你的 LLM API 密钥
const agent = new PageAgent({
  llm: {
    apiKey: 'your-api-key',
    model: 'gpt-4',
  },
});

// 执行自然语言指令
await agent.execute('点击页面上的“登录”按钮');

// 更复杂的指令
await agent.execute('在搜索框中输入“JavaScript”并点击搜索');
```

对于不需要 coding 的场景，也可以直接通过 Chrome 扩展（可选）安装后，在浏览器的开发者工具中使用。

## 适用场景

- **前端自动化测试**：快速编写测试用例，无需学习 Selenium 或 Cypress 的复杂 API，直接使用自然语言描述场景，例如“点击导航栏中的‘关于我们’”。
- **AI 驱动的网页助手**：为在线客服、表单填写、数据抓取等场景提供对话式界面，用户只需“告诉”页面想做什么。
- **无障碍辅助工具**：为行动不便的用户提供语音或文本控制网页的桥梁，降低操作门槛。
- **原型验证与演示**：快速展示交互流程，无需编写大量 DOM 操作代码，直接通过自然语言模拟用户行为。

## 项目亮点

- **极致简化的集成**：与其他 GUI Agent 方案相比，Page Agent 不需要安装浏览器扩展、Python 运行时或 headless 浏览器。一个 JavaScript 文件即可运行，这大大降低了嵌入门槛。
- **纯文本高效路线**：摒弃截图和多模态 LLM，仅依赖文本解析。这带来了两个优势：一是显著降低了 API 调用成本和延迟；二是避免了截图可能导致的隐私和安全问题（如敏感页面内容泄露）。
- **自带 LLM 的灵活性**：用户可以选择自己喜欢的 LLM 服务商（如 OpenAI、Anthropic 等），不绑定特定 AI 平台，也方便本地部署或私有化模型。
- **基于真实浏览器事件**：操作触发的是浏览器原生事件，而非模拟指令，这意味着它能兼容绝大多数 Web 应用（包括单页面应用和复杂框架），行为与真实用户操作一致。

## 相关链接

- [GitHub 仓库](https://github.com/alibaba/page-agent)
- [在线 Demo](https://alibaba.github.io/page-agent/)
- [官方文档](https://alibaba.github.io/page-agent/docs/introduction/overview)
- [Chrome 扩展说明](https://alibaba.github.io/page-agent/docs/features/chrome-extension)
