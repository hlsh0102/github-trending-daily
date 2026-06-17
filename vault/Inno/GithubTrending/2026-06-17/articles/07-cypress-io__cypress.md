---
tags:
  - trending
  - article
repo: cypress-io/cypress
date: 2026-06-17
language: TypeScript
stars_total: 50274
stars_today: 13
---
## 项目概述

Cypress 是一个基于 JavaScript 的前端测试工具，专为现代 Web 应用设计，旨在提供快速、简单且可靠的浏览器端测试体验。与传统的 Selenium 或 Puppeteer 等工具不同，Cypress 采用全新的架构设计，以解决开发者在编写和运行端到端（E2E）测试时遇到的常见痛点，如速度慢、调试困难、环境不稳定等问题。

Cypress 的目标用户包括前端工程师、QA 工程师以及需要确保应用在浏览器中表现正确的任何开发者。无论是编写单元测试、集成测试还是完整的端到端测试，Cypress 都能提供一致且高效的体验。该项目采用 MIT 许可证，开源免费。

## 核心功能

- **实时重载与热模块替换**：在测试文件保存后，Cypress 会自动重新运行测试，并立即呈现最新结果，极大提升开发效率。
- **内置时间旅行（Time Travel）**：测试运行时，Cypress 会记录每一步的快照，开发者可以随时回溯到任意一步，查看当时的 DOM 状态和控制台输出。
- **自动等待与断言**：Cypress 会自动等待元素出现、动画完成或网络请求结束，无需手动添加 `sleep` 或 `wait` 语句，简化测试逻辑。
- **全面的网络控制**：支持拦截、修改和模拟网络请求（XHR / Fetch），可轻松测试加载状态、错误处理及 API 响应。
- **跨浏览器测试**：支持 Chrome、Electron、Firefox 和 Edge 等主流浏览器，且提供一致的 API 行为。
- **丰富的调试与截图/视频录制**：测试失败时会自动生成截图或录屏，并附带详细的错误栈与 DOM 快照，方便定位问题。

## 技术架构

Cypress 的核心架构与传统测试工具截然不同。它直接运行在浏览器内部，通过一个由 Node.js 进程和浏览器进程协同工作的代理架构来实现操控。具体来说：

- **Node.js 后端**：负责管理测试运行器、与文件系统交互、启动浏览器、处理网络代理等任务。
- **浏览器前端**：通过注入到页面中的脚本，Cypress 可以实时访问 DOM、控制事件触发、拦截网络请求，并且与测试代码处于同一事件循环内。
- **实时双向通信**：测试代码与浏览器页面之间通过 WebSocket 保持同步，使得 Cypress 能够即时响应页面变化，实现自动等待和时间旅行。

这种架构使得 Cypress 拥有比传统 WebDriver 协议更快的执行速度和更精细的控制能力，能够解决测试中常见的竞态条件和不稳定性问题。

## 安装与使用

### 安装

Cypress 可以通过 npm 直接安装，推荐作为项目的开发依赖：

```bash
npm install cypress --save-dev
```

或者全局安装（不推荐生产使用）：

```bash
npm install -g cypress
```

安装完成后，可以通过以下命令首次打开 Cypress 测试运行器：

```bash
npx cypress open
```

首次运行会在项目根目录创建 `cypress` 文件夹，包含示例测试文件和配置文件。

### 最小可用示例

在 `cypress/e2e` 目录下创建一个测试文件 `example.spec.cy.js`：

```javascript
describe('我的第一个测试', () => {
  it('访问浏览器', () => {
    cy.visit('https://www.example.com');
    cy.contains('Example Domain').should('be.visible');
  });
});
```

然后执行 `npx cypress run`（无头模式）或再次使用 `npx cypress open` 在交互界面中运行该测试。

## 适用场景

- **端到端（E2E）测试**：模拟用户操作整个应用流程，验证关键路径如登录、注册、购物结账等功能正常运行。
- **组件测试**：Cypress 也支持测试独立的 UI 组件（如 React、Vue、Angular 组件），配合 `cypress/vue` 或 `cypress/react` 插件，可快速验证组件状态和行为。
- **集成测试**：测试前后端交互，验证 API 调用结果、数据渲染以及错误边界的处理逻辑。
- **回归测试**：在持续集成（CI）环境中自动化运行，确保每次代码提交不会破坏已有功能。

## 项目亮点

- **极致的开发体验**：实时重载、时间旅行、自动等待等功能让测试编写和调试变得非常流畅，大幅降低了测试门槛。
- **原生浏览器兼容**：无需 WebDriver 或 Selenium Server，直接控制浏览器，减少环境配置的复杂度。
- **强大的网络控制**：内置对 HTTP 请求、响应、超时和错误场景的模拟，方便构造复杂的测试用例。
- **活跃的开源社区**：拥有超过 5 万颗星标，配套文档完善，官方 Discord 社区响应迅速，第三方插件生态丰富（如 `cypress-image-snapshot`、`cypress-real-events` 等）。

与 Puppeteer 或 Playwright 相比，Cypress 更侧重于测试运行的直观性和调试便利性，尤其适合需要快速上手的前端团队。不过，其目前不支持跨域多标签页操作，但已在路线图中考虑。

## 相关链接

- [GitHub 仓库](https://github.com/cypress-io/cypress)
- [官方文档](https://on.cypress.io)
- [更新日志](https://on.cypress.io/changelog)
- [路线图](https://on.cypress.io/roadmap)
- [Discord 社区](https://on.cypress.io/discord)
