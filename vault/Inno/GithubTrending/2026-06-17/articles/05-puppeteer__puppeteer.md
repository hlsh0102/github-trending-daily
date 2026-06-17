---
tags:
  - trending
  - article
repo: puppeteer/puppeteer
date: 2026-06-17
language: TypeScript
stars_total: 94961
stars_today: 56
---
## 项目概述

Puppeteer 是一个由 Google 维护的 JavaScript 库，提供了一套高级 API 来控制 Chrome 或 Firefox 浏览器。它基于 DevTools 协议或 WebDriver BiDi 协议，默认在无界面（headless）模式下运行。该项目主要面向 Web 开发者、测试工程师和自动化运维人员，帮助他们通过代码直接操作浏览器行为，从而简化自动化测试、网页抓取、页面截图和性能监控等任务。Puppeteer 自发布以来已成为 Node.js 生态中最受欢迎的浏览器自动化工具之一，目前在 GitHub 上拥有超过 94000 颗星。

## 核心功能

- **浏览器自动化控制**：以编程方式启动、关闭浏览器，创建和切换标签页，模拟用户点击、输入、导航等交互行为。
- **页面截图与 PDF 生成**：对网页进行完整截图（包括滚动区域），或生成精确布局的 PDF 文件，支持自定义视口大小和输出格式。
- **网络请求拦截与修改**：拦截页面发出的所有网络请求，可修改请求头、响应内容，或模拟离线状态、限制网络速度。
- **JavaScript 执行注入**：在页面上下文中执行任意 JavaScript 代码，读取或修改 DOM 元素、获取运行时数据。
- **性能追踪与分析**：通过 Chrome DevTools 协议捕获性能指标、控制台日志、网络活动时间线，辅助页面性能优化。
- **多浏览器支持**：不仅支持 Chrome/Chromium，还通过 WebDriver BiDi 协议支持 Firefox，扩展了自动化测试的覆盖范围。

## 技术架构

Puppeteer 采用客户端-服务器架构设计。核心库通过 WebSocket 或管道与浏览器实例通信，使用 Chrome DevTools Protocol（CDP）或 WebDriver BiDi 协议发送指令并接收事件。其设计以 Node.js 事件驱动模型为基础，所有操作通过 Promise 异步执行，避免阻塞主线程。项目分为两个 npm 包：`puppeteer` 会自动下载兼容版本的 Chromium 浏览器，适合开箱即用的场景；`puppeteer-core` 仅包含库本身，需要用户自行提供浏览器，适合已有浏览器环境的部署。库内部维护了一个浏览器实例池，支持并发控制，同时提供 `Page`、`ElementHandle`、`Frame` 等抽象对象，让开发者以接近 DOM 编程的方式操作浏览器。此外，Puppeteer 通过可插拔的传输层设计，未来可扩展支持更多浏览器和协议。

## 安装与使用

安装 Puppeteer 最快捷的方式是使用 npm：

```bash
npm i puppeteer
```

该命令会在安装过程中自动下载兼容的 Chromium 浏览器。如果只需要库本身而不需要浏览器，可安装 core 版本：

```bash
npm i puppeteer-core
```

最低可用示例——打开百度首页并截图：

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.baidu.com');
  await page.screenshot({ path: 'baidu.png' });
  await browser.close();
})();
```

对于企业环境或 CI 系统，如果安装脚本被包管理器拦截，可手动下载浏览器：

```bash
npx puppeteer browsers install
```

## 适用场景

- **端到端自动化测试**：配合 Jest、Mocha 等测试框架，编写模拟用户完整流程的测试脚本，覆盖表单提交、页面跳转、异步加载等场景。
- **网页抓取与数据提取**：对需要 JavaScript 渲染的 SPA 网站进行抓取，获取动态加载的内容，或执行登录、翻页等复杂操作后提取数据。
- **网页性能监控**：定期捕获关键页面的加载时间、资源大小、首次绘制时间等指标，生成性能趋势报告，辅助前端性能优化。
- **自动化运维与报告生成**：定时生成业务仪表盘的截图或 PDF 报告，用于邮件发送或存档，或监控页面变化并触发告警。

## 项目亮点

- **浏览器生态的高度兼容**：由 Chrome 团队维护，对 Chromium 的支持最及时、最完整，能第一时间适配新特性。
- **丰富的 API 覆盖**：从基本的页面操作到高级的网络拦截、注入脚本、性能分析，API 设计直观且文档详尽。
- **异步驱动与性能优化**：基于 Promise 的异步架构，支持并发操作，配合浏览器无头模式，可在服务器端高效运行。
- **活跃的社区与生态**：拥有庞大的用户基础和海量教程、插件、集成工具（如与 Jest/Puppeteer 结合的测试框架），遇到问题容易找到解决方案。
- **灵活的浏览器管理**：内置浏览器下载机制，开箱即用；core 版本则适合自定义浏览器路径或进行集群管理。

## 相关链接

- [GitHub 仓库](https://github.com/puppeteer/puppeteer)
- [官方文档](https://pptr.dev/docs)
- [API 参考](https://pptr.dev/api)
- [常见问题解答](https://pptr.dev/faq)
