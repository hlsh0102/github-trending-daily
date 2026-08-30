---
tags:
  - trending
  - article
repo: bigskysoftware/htmx
date: 2026-08-30
language: JavaScript
stars_total: 49183
stars_today: 32
---
## 项目概述

htmx 是一个轻量级、无依赖的 JavaScript 库，旨在通过直接在 HTML 中使用属性来访问 AJAX、CSS 过渡、WebSocket 和 Server Sent Events 等现代 Web 功能。它的核心理念是“high power tools for HTML”——即用最简单的超文本方式构建现代化的用户界面。

传统的前端开发往往需要编写大量 JavaScript 代码来实现页面交互，而 htmx 将这一过程简化为在 HTML 标签上添加 `hx-get`、`hx-post`、`hx-swap` 等属性。它的目标用户是那些希望保持后端渲染架构（如 Django、Rails、Laravel、Spring MVC 等）的开发者，以及认同 HATEOAS（超媒体作为应用状态引擎）和 REST 架构风格的工程师。通过 htmx，你可以摆脱复杂的 SPA 框架（如 React、Vue）带来的构建工具链和状态管理负担，回归 Web 的原始简约之美。

## 核心功能

- **AJAX 请求增强**：允许任意 HTML 元素发起 AJAX 请求，不再局限于 `<a>` 和 `<form>`。支持 `hx-get`、`hx-post`、`hx-put`、`hx-delete` 等属性，且支持 GET、POST、PUT、PATCH、DELETE 全部 HTTP 方法。
- **事件触发控制**：不再局限于 `click` 和 `submit` 事件。你可以通过 `hx-trigger` 指定鼠标、键盘、触摸甚至自定义事件来触发请求，还能添加节流或延迟（如 `every 1s`、`click delay:500ms`）。
- **局部页面替换**：通过 `hx-swap` 属性精确控制服务器响应更新 DOM 的方式，支持 `innerHTML`、`outerHTML`、`beforebegin`、`afterend` 等多种策略，不再只能替换整个页面。
- **CSS 过渡动画**：内置支持 CSS 过渡，当页面内容被替换时，可以自动应用进入和退出动画效果，无需额外编写 JavaScript。
- **扩展机制**：提供强大的扩展系统（Extensions），官方和社区开发了丰富的扩展，如 WebSocket 和 Server Sent Events 支持、客户端模板渲染、数据缓存、表单验证等。
- **事件与 WebSocket 集成**：通过扩展轻松接入 WebSocket 和 SSE，实现服务端推送功能，同时支持事件化编程（hx-on）和事件触发处理。

## 技术架构

htmx 的技术设计遵循渐进增强和 HTML 优先的理念。整个库是一个独立的 JavaScript 文件，大小仅为约 14KB（min.gz'd），且没有任何运行时依赖。它的核心工作流是：解析 DOM 中的 `hx-*` 属性，监听相应的触发事件，代发 AJAX 请求，接收响应后按照 `hx-swap` 指定的方式更新页面。

其架构具有以下显著特点：

1. **声明式设计**：所有逻辑都通过 HTML 属性声明，保持 Markup 与行为的高度内聚，符合 HATEOAS 架构风格。
2. **可组合性**：htmx 允许在同一个元素上组合多个属性，构建复杂交互，例如同时定义 `hx-get`、`hx-trigger` 和 `hx-target`。
3. **事件驱动**：htmx 内置了丰富的事件机制，如 `htmx:beforeRequest`、`htmx:afterSwap` 等，便于开发者介入请求生命周期。
4. **服务端无关**：它只关心 HTTP 请求与 HTML 响应，不关心服务端技术栈，因此与任何后端语言都能无缝协作。

## 安装与使用

安装 htmx 非常简单，只需在 HTML 中引入一个 `<script>` 标签即可：

```html
<script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.10/dist/htmx.min.js"></script>
```

也可以通过 npm 安装，用于模块化项目：

```bash
npm install htmx.org
```

以下是一个最小可用的示例：当点击按钮时，向服务器发起 GET 请求，并将响应内容替换到指定容器中。

```html
<div id="result">点击按钮加载数据</div>
<button hx-get="/api/data" hx-target="#result" hx-swap="innerHTML">
  加载数据
</button>
```

当用户点击按钮，htmx 会向 `/api/data` 发送一个 GET 请求，服务器的响应内容会替换 `#result` 元素的 `innerHTML`。如果服务端返回一段 HTML 片段，页面局部更新即刻完成，无需刷新。若需要自动触发，可将 `hx-trigger` 设为 `load`，页面加载即自动请求。

## 适用场景

- **服务端渲染应用的交互增强**：使用 Django、Rails、Laravel 等技术栈的团队，无需重写前端框架，即可为现有页面增加动态更新、表单提交等交互，大幅提升用户体验。
- **快速原型与内部工具**：对于快速迭代的管理后台、数据仪表盘或内部工具，使用 htmx 可以显著减少开发时间，保持代码库简洁。
- **渐进增强的 Web 页面**：在保留基础 HTML 功能的前提下，为浏览器环境较好的用户提供 AJAX 增强，构建不依赖 JavaScript 也能正常工作的页面。
- **教学与学习场景**：作为理解超媒体架构和 REST 概念的极佳工具，也适合初学者探索 Web 开发，避开复杂的工程栈。

## 项目亮点

htmx 与传统 SPA 框架和纯 jQuery 方案相比，具有鲜明的差异化优势：

- **极简体积与零依赖**：约 14KB 的压缩体积，不引入任何第三方库，加载和渲染性能极高。
- **回归 HTML 本质**：遵循 HATEOAS 与 REST 架构，让后端掌握应用状态，保持前端逻辑的简单与透明。
- **范式转换思维**：它不只是一个工具，而是一种思想——将超文本的力量重新带回 Web 开发，挑战复杂的 JavaScript 前端生态。
- **蓬勃的生态与社区**：拥有活跃的 Discord 社区和丰富的第三方扩展，可无缝集成 WebSocket、客户端模板、缓存等高级功能。
- **可测试性与可维护性**：服务端返回的 HTML 片段可以直接复用模板，测试覆盖更简单，浏览器兼容性良好。

## 相关链接

- [GitHub 仓库](https://github.com/bigskysoftware/htmx)
- [官方网站与文档](https://htmx.org/docs)
- [实用示例集](https://htmx.org/examples)
- [扩展生态](https://htmx.org/extensions)
- [WebSocket 扩展](https://htmx.org/extensions/ws/)
- [Server Sent Events 扩展](https://htmx.org/extensions/sse/)
