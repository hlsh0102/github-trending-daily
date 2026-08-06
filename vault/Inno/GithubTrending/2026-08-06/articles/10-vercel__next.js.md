---
tags:
  - trending
  - article
repo: vercel/next.js
date: 2026-08-06
language: JavaScript
stars_total: 141589
stars_today: 68
---
## 项目概述

Next.js 是由 Vercel 团队开发并维护的开源 React 框架，目前是 GitHub 上最活跃的前端项目之一，拥有超过 14 万颗星标。它旨在解决 React 应用开发中的几个核心痛点：服务端渲染（SSR）、静态站点生成（SSG）、路由管理以及全栈能力整合。通过扩展 React 的最新特性，Next.js 让开发者能够以统一的框架完成从构思到部署的完整流程，而无需为每个功能单独寻找并配置第三方库。

Next.js 适用于各类规模的项目——从个人博客、企业官网到复杂的电商平台和 SaaS 应用。它不仅服务于前端开发者，也因其内置的 API 路由和服务器功能，降低了全栈开发的入门门槛。

## 核心功能

- **文件系统路由**：基于 `pages` 或 `app` 目录结构自动生成路由，无需手动配置路由映射，并支持动态路由、嵌套布局和捕获所有路径。
- **混合渲染策略**：在同一个应用中灵活使用服务端渲染（SSR）、静态站点生成（SSG）和客户端渲染（CSR），针对每个页面选择最优的渲染方式以平衡性能与交互性。
- **内置 API 路由**：允许开发者在应用内直接创建后端 API 端点，无需额外搭建独立的服务器，便于构建全栈应用。
- **自动代码分割与优化**：Next.js 自动分析页面依赖，仅加载当前路由所需的 JavaScript，同时内置图像优化、字体优化等性能工具。
- **快速刷新（Fast Refresh）**：为 React 组件提供即时的热更新体验，保留组件状态，显著提升开发效率。
- **Rust 驱动的构建工具**：底层使用基于 Rust 的 Turbopack（开发模式）和 SWC（编译与压缩），大幅缩短构建时间和冷启动速度。

## 技术架构

Next.js 的核心设计思路是“约定优于配置”，通过规范化的目录结构和文件命名约定，减少配置文件的复杂度。它的架构分为几个关键层：

- **编译与打包层**：采用 SWC（Rust 编写的 JavaScript/TypeScript 编译器）进行代码转换和压缩，比传统 Babel 快数倍。在最新版本中，开发服务器使用 Turbopack 作为打包器，优化了模块热替换（HMR）的速度。
- **路由层**：支持两种路由模式——经典的 `pages` 路由和较新的 `app` 路由。`app` 路由基于 React Server Components，允许开发者在服务端和客户端之间精细划分组件的渲染职责，同时支持共享布局和加载/错误状态。
- **数据获取与缓存**：框架提供 `getServerSideProps`、`getStaticProps` 等数据获取方法（在 `pages` 中）以及 `fetch` 的扩展选项（在 `app` 中），支持按需重新验证（ISR）和静态缓存策略，兼顾动态内容与页面时效性。
- **服务端能力**：除了 API 路由，Next.js 还支持 Middleware（中间件）机制，允许在请求完成前执行认证、重定向、日志等逻辑，且运行在边缘网络，实现低延迟响应。

## 安装与使用

安装 Next.js 非常简单，只需使用 Node.js 环境（建议 18.17 或更高版本）运行以下命令，即可创建一个新的应用：

```bash
npx create-next-app@latest my-app
cd my-app
npm run dev
```

上述命令会生成一个包含基础目录结构的新项目，并在 `http://localhost:3000` 启动开发服务器。

一个最小可用的页面示例（`app/page.tsx` 或 `pages/index.js`）：

```javascript
export default function Home() {
  return (
    <div>
      <h1>欢迎使用 Next.js</h1>
      <p>这是一个极简页面。</p>
    </div>
  );
}
```

对于需要服务端数据获取的页面，可以导出异步函数（以 `pages` 路由为例）：

```javascript
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
}

export default function Page({ data }) {
  return <div>服务端数据: {JSON.stringify(data)}</div>;
}
```

## 适用场景

- **内容型网站与博客**：利用 SSG 或 ISR 生成静态页面，兼具 SEO 友好和快速加载优势，同时支持频繁的内容更新。
- **电商与营销站点**：需要出色的首屏加载速度和良好的搜索引擎排名，Next.js 的混合渲染让商品详情页可静态化，购物车和用户中心则保持动态。
- **全栈 SaaS 应用**：借助 API 路由和后端逻辑，开发者可以在同一代码库中构建完整的应用，简化部署与运维，尤其适合中小规模团队。
- **企业级门户与仪表盘**：通过 React Server Components 和布局系统，可以轻松管理复杂的权限控制和嵌套 UI，同时保持性能。

## 项目亮点

与 Create React App（CRA）或 Vite 等工具相比，Next.js 最大的优势在于其“零配置”地集成了服务端能力和 SEO 解决方案。CRA 仅提供客户端渲染，开发者需要自行搭建 SSR 框架和路由。而 Next.js 将这一切作为框架的一等公民，开箱即用。

得益于 Rust 工具链（SWC 和 Turbopack），Next.js 在构建速度和开发反馈循环上明显优于基于 Babel/Webpack 的旧式工具链。此外，`app` 路由引入的 React Server Components 让开发者能够将数据密集型逻辑留在服务端，从而大幅减少客户端 JavaScript 体积，提升应用性能。

另一个突出的亮点是 Vercel 提供的原生部署平台集成。与 GitHub 仓库直接关联后，每次 `git push` 都能自动触发构建和部署，并支持预览部署（Preview Deployments），让团队协作和代码评审流程更加高效。

## 相关链接

- [GitHub 仓库](https://github.com/vercel/next.js)
- [官方网站](https://nextjs.org)
- [学习课程与文档](https://nextjs.org/learn)
- [Next.js Showcase 展示案例](https://nextjs.org/showcase)
