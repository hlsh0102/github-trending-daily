---
tags:
  - trending
  - article
repo: cypress-io/cypress
date: 2026-08-05
language: TypeScript
stars_total: 50831
stars_today: 11
---
## 项目概述

Cypress 是一个面向现代 Web 的前端测试工具，专注于为浏览器中运行的任何内容提供快速、简单且可靠的测试体验。它解决了传统端到端测试工具长期存在的痛点：配置复杂、运行缓慢、调试困难。Cypress 的目标用户是前端开发者、测试工程师以及任何需要确保 Web 应用质量的技术团队。与依赖 Selenium WebDriver 的传统工具不同，Cypress 直接在浏览器内运行，提供了更快的执行速度、更稳定的测试结果和更直观的调试体验。

## 核心功能

- **实时重载与自动等待**：测试代码保存后自动重新运行，并内置智能等待机制，无需手动添加 `sleep` 或 `wait` 命令，有效消除时序竞争问题。
- **时间旅行调试**：Cypress 为每一步测试操作拍摄快照，支持鼠标悬停在命令日志上查看对应时刻的 DOM 状态，大幅降低错误定位成本。
- **网络流量控制**：可以自由 stub 或拦截 XHR、Fetch 请求，模拟各种网络响应（如超时、错误、慢速网络），无需修改应用代码。
- **原生访问与可编程控制**：通过 `cy.task` 和插件机制，可以在 Node.js 环境中执行诸如数据库操作、文件读写等底层任务，打破浏览器安全沙箱的限制。
- **一键并行测试**：内置 Dashboard 服务支持跨多台机器并行执行测试，显著缩短完整测试套件的运行时间。
- **完整的断言与截图/视频录制**：内置丰富的断言库（支持 BDD/TDD 风格），并在测试失败时自动截图、录制视频，为失败分析提供详实证据。

## 技术架构

Cypress 的架构设计颠覆了传统 WebDriver 模型。它由两个核心部分构成：运行在 Node.js 进程中的**服务端**和注入到浏览器中的**客户端**。两者通过 WebSocket 进行实时双向通信。

- **浏览器内执行**：测试命令并非通过外部协议发送，而是直接在浏览器上下文中运行，这使得 Cypress 可以轻松穿透 iframe 边界，并同步访问 DOM、网络请求等运行时信息。
- **命令队列与异步控制**：Cypress 的命令是异步的，但它们被组织为一个队列并按顺序执行。每个命令都会触发下一次浏览器重绘和事件循环，从而保证测试操作贴近真实用户行为。
- **进程隔离**：服务端负责解析测试文件、管理插件和与浏览器驱动交互，而客户端专注于执行命令和收集数据，这种分工保证了系统的稳定性和可扩展性。
- **依赖内置工具**：基于 Node.js 和 Chrome DevTools 协议，Cypress 无需额外安装浏览器驱动，内建了对 Chrome、Firefox、Edge 等主流浏览器的支持。

## 安装与使用

首先，在项目根目录安装 Cypress：

```bash
npm install cypress --save-dev
```

然后，打开 Cypress 的测试运行器：

```bash
npx cypress open
```

首次运行会生成默认的 `cypress` 文件夹，其中包含示例测试。一个最小可用的测试用例（`cypress/e2e/example.cy.js`）如下：

```javascript
describe('My First Test', () => {
  it('Visits the app and asserts content', () => {
    cy.visit('https://example.com');
    cy.contains('Example Domain').should('be.visible');
  });
});
```

在交互模式下，测试会实时运行并显示每个步骤的日志。如需以命令行方式运行所有测试（如 CI 环境），使用：

```bash
npx cypress run
```

此外，可以通过 `cypress.config.js` 文件配置基础 URL、环境变量、视口尺寸等选项，灵活适配不同项目的需求。

## 适用场景

- **端到端回归测试**：在每次代码提交或发布前，自动验证核心用户路径（如登录、注册、下单）是否正常。
- **前端组件验收**：结合 Component Testing 特性，对组件库中的独立组件进行交互和样式验证。
- **接口与 UI 集成验证**：通过拦截网络请求，断言前端逻辑是否正确处理成功、失败、异常等不同 API 响应。
- **可视化回归初筛**：虽然 Cypress 本身不提供图像对比，但可以结合截图功能与第三方工具（如 Percy）使用，快速捕获视觉偏差。

## 项目亮点

与同类工具（如 Selenium、Playwright）相比，Cypress 的差异化优势非常鲜明：

- **开发者体验优先**：内置调试器、时间旅行和自动等待让测试编写和排错变得异常顺畅，上手门槛极低。
- **架构创新**：无需 WebDriver，直接在浏览器内运行，从根本上规避了网络延迟和同步问题导致的脆弱测试。
- **一体化解决方案**：从测试编写、断言到报告生成、视频录制，甚至 CI 并行执行，Cypress 提供了开箱即用的全链路支持，无需拼装多个库。
- **社区与生态**：作为开源项目，拥有庞大的用户群、丰富的插件库（如 `cypress-cucumber-preprocessor`），以及活跃的 Discord 社区支持。

## 相关链接

- [GitHub 仓库](https://github.com/cypress-io/cypress)
- [官方文档](https://on.cypress.io)
- [变更日志](https://on.cypress.io/changelog)
- [路线图](https://on.cypress.io/roadmap)
