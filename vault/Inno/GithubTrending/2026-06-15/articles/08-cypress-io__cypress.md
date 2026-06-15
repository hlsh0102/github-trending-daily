---
tags:
  - trending
  - article
repo: cypress-io/cypress
date: 2026-06-15
language: TypeScript
stars_total: 50052
stars_today: 39
---
## 项目概述

Cypress 是一个快速、简单且可靠的前端测试工具，专为在浏览器中运行的任何内容设计。它解决了传统端到端测试工具在安装配置复杂、运行速度慢、调试困难等方面的痛点。Cypress 的目标用户包括前端开发工程师、测试工程师以及任何需要为 Web 应用编写自动化测试的人员。与传统基于 Selenium 的测试框架不同，Cypress 采用全新的架构设计，与浏览器运行在同一事件循环中，从而实现了更快的执行速度和更稳定的测试结果。该项目在 GitHub 上拥有超过 50,000 颗星，是当下最受欢迎的前端测试框架之一，采用 MIT 开源许可证。

## 核心功能

- **实时重载与自动等待**：Cypress 在测试运行时自动等待元素出现、命令完成，消除了手动添加 `sleep` 或 `wait` 的繁琐操作，同时支持代码更改后的即时刷新。
- **时间旅行式调试**：每次命令执行时，Cypress 都会自动拍摄快照，开发者可以在测试运行过程中回溯到任意命令的执行状态，查看当时的 DOM 状态和控制台输出，极大简化调试流程。
- **内置契约测试与网络控制**：原生支持对 HTTP 请求进行拦截、模拟和存根（stub），无需额外的 mock 库即可轻松测试前后端交互、错误处理和网络延迟场景。
- **跨浏览器测试**：支持 Chrome、Firefox、Edge 和 Electron 等主流浏览器，并提供一致的测试体验。Cypress Cloud 进一步支持并行执行和跨浏览器结果聚合。
- **端到端测试与组件测试一体化**：不仅支持完整的页面端到端测试，还支持独立的组件测试模式，开发者可在隔离环境中测试 React、Vue、Angular 等框架的单个组件，显著提升开发效率。
- **可视化测试运行器**：提供具有图形界面的测试运行器，可直观展示测试进度、代码覆盖率，并支持录屏、截图等高级功能，方便团队协作与问题复现。

## 技术架构

Cypress 的核心设计理念是“运行在浏览器中，与应用程序在同一进程中执行”。与 Selenium 等传统工具通过远程命令驱动浏览器不同，Cypress 使用 Node.js 进程管理测试逻辑，并通过 WebSocket 直接与浏览器实例通信。这种同构架构带来了几个关键优势：首先，测试代码可以直接访问 DOM 和应用程序上下文，无需通过序列化/反序列化传递数据；其次，Cypress 可以监听浏览器内部事件（如页面加载、网络请求），实现精确的自动等待；最后，由于没有网络层的额外开销，测试执行速度相比传统方案提升了数倍。在实现层面，Cypress 主要使用 TypeScript 编写，底层依赖 Chrome DevTools Protocol 和 Electron 实现浏览器控制，配套的 Dashboard 服务（Cypress Cloud）则提供云端并行执行和结果分析能力。

## 安装与使用

**安装要求**：Node.js 12 或更高版本。Cypress 通过 npm 或 yarn 即可安装。

```bash
# 安装 Cypress 作为开发依赖
npm install cypress --save-dev

# 或使用 yarn
yarn add cypress --dev
```

安装完成后，可通过以下命令打开 Cypress 测试运行器：

```bash
npx cypress open
```

首次启动时，Cypress 会自动生成示例测试文件和配置文件。以下是一个最小的端到端测试示例：

```javascript
// cypress/e2e/spec.cy.js
describe('我的第一个测试', () => {
  it('访问百度并搜索', () => {
    cy.visit('https://www.baidu.com')
    cy.get('input[name="wd"]').type('Cypress 测试')
    cy.get('input[type="submit"]').click()
    cy.contains('Cypress').should('be.visible')
  })
})
```

如果需要在无头模式下运行所有测试（例如在 CI/CD 环境中）：

```bash
npx cypress run
```

组件测试还需要额外配置，在 Cypress 配置文件中指定框架（如 React、Vue）后即可运行。

## 适用场景

- **持续集成/持续部署（CI/CD）流水线**：Cypress 可以无缝集成到 GitHub Actions、Jenkins、CircleCI 等 CI 工具中，在每次代码提交后自动运行端到端测试，确保主干代码质量。
- **前端组件库开发**：组件测试模式允许开发者在独立环境中测试 UI 组件的各个状态（加载态、空态、错误态），配合 Storybook 使用可显著提升组件开发迭代效率。
- **回归测试**：对于频繁迭代的 Web 应用，Cypress 的自动等待和快照功能可以快速覆盖核心业务流程，在引入新功能时有效防止已有功能被破坏。
- **API 与 UI 联调测试**：利用网络拦截功能，开发者可以在不搭建后端服务的情况下，模拟各种 API 响应来测试前端界面显示和异常处理逻辑。

## 项目亮点

- **开发体验优先**：Cypress 提供了传统测试工具所不具备的现代化开发体验，如实时重载、时间旅行调试和可视化命令日志，使得编写和调试测试如同开发 Web 应用本身一样流畅。
- **无需额外依赖**：内置了断言库（Chai）、Mock/Stub 功能（Sinon）以及截图/录屏功能，无需像 Selenium 那样需要额外集成 TestNG、Junit 或各类 mock 库。
- **社区生态活跃**：作为 GitHub 明星项目，Cypress 拥有庞大的社区和丰富的插件生态（如 cypress-axe 可访问性测试、cypress-code-coverage 覆盖率报告），遇到问题时能快速获得支持。
- **适合现代前端工作流**：深度适配 React、Vue、Angular 等现代框架，并支持 TypeScript 开箱即用，与前端开发团队的技术栈完美契合。

## 相关链接

- [GitHub 仓库](https://github.com/cypress-io/cypress)
- [官方文档](https://on.cypress.io)
- [更新日志](https://on.cypress.io/changelog)
- [路线图](https://on.cypress.io/roadmap)
- [Discord 社区](https://on.cypress.io/discord)
