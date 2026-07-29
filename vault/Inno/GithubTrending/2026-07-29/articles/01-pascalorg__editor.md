---
tags:
  - trending
  - article
repo: pascalorg/editor
date: 2026-07-29
language: TypeScript
stars_total: 18923
stars_today: 341
---
## 项目概述

Pascal Editor 是一个基于 Web 构建的 3D 建筑编辑器，专注于让用户能够快速创建和分享 3D 建筑项目。该项目采用 TypeScript 开发，底层依赖 React Three Fiber 和 WebGPU 技术栈，实现了在浏览器中运行的高性能 3D 编辑体验。它解决了传统 3D 建筑设计工具安装复杂、协作困难、分享门槛高的问题，目标是面向建筑设计师、3D 建模爱好者、教育工作者以及需要在线展示建筑方案的团队。

## 核心功能

- **实时 3D 编辑**：基于 WebGPU 渲染，支持在浏览器中流畅地创建、修改和查看 3D 建筑模型，无需安装任何本地软件。
- **节点化设计系统**：采用节点化架构，用户可以通过组合预定义的建筑节点（如墙体、门窗、楼梯等）来构建复杂的建筑结构。
- **一键分享**：完成项目后，可以通过链接直接分享给他人，无需导出文件或部署额外服务，降低协作与展示成本。
- **插件扩展机制**：内置插件系统，支持加载社区或第三方开发的节点包，扩展编辑器功能边界。
- **包化发布**：核心功能、渲染引擎、编辑工具和节点库分别以独立的 npm 包形式发布，开发者可以按需集成到自己的应用中。
- **React 生态集成**：基于 React Three Fiber 构建，与 React 应用无缝集成，便于前端开发者定制和二次开发。

## 技术架构

Pascal Editor 采用 Turborepo 构建的 monorepo 架构，整个项目包含四个核心运行时包和若干辅助包，层次清晰，职责分明：

- **@pascal-app/core**：定义核心的数据 schema、场景状态管理以及插件注册表合约，是整个编辑器的底层基础设施。
- **@pascal-app/viewer**：3D 渲染运行时，负责场景的渲染循环、光照、相机控制等通用渲染系统，基于 React Three Fiber 和 WebGPU 实现高效渲染。
- **@pascal-app/editor**：包含编辑工具和 UI 组件，如拾取、变换、属性面板等，提供交互式编辑能力。
- **@pascal-app/nodes**：内置的节点定义、渲染器和系统，预置了常见的建筑构件，用户可直接拖拽使用。
- **@pascal-app/ui**：共享的 UI 组件库，为各个包提供一致的界面元素。

这种设计遵循了关注点分离原则，核心包不依赖具体编辑器的 UI 实现，渲染包不关心节点业务逻辑，使得各部分可以独立演进和维护。同时，WebGPU 的运用带来了比传统 WebGL 更优的渲染性能和更低的功耗，为复杂 3D 场景的实时编辑提供了技术基础。

## 安装与使用

Pascal Editor 提供了按需集成的 npm 包，开发者可以快速在自己的项目中嵌入 3D 建筑查看或编辑能力。

**基础安装步骤：**

1. 安装核心包和查看器包：
```bash
npm install @pascal-app/core @pascal-app/viewer @pascal-app/editor @pascal-app/nodes
```

2. 在应用入口加载内置节点插件：
```typescript
import { loadPlugin } from '@pascal-app/core'
import { builtinPlugin } from '@pascal-app/nodes'

await loadPlugin(builtinPlugin)
```

3. 在 React 组件中使用 `<Viewer>` 渲染场景：
```tsx
import { Viewer } from '@pascal-app/viewer'

function App() {
  return <Viewer />
}
```

更详细的 React 示例和配置可参考 `@pascal-app/viewer` 包中的 `README.md` 文件。

## 适用场景

- **建筑方案在线展示**：设计师完成方案后，分享给甲方或团队成员在线查看，支持自由旋转和缩放，提升沟通效率。
- **教育课堂互动硬件**：在建筑学或室内设计课程中，学生可直接在浏览器中搭建模型，无需部署本地环境，降低教学门槛。
- **轻量级产品原型**：中小团队在设计初期快速构建 3D 概念模型，并制作交互式演示链接，用于内部评审或客户提案。
- **开发者工具集成**：前端开发者可将 Pascal Editor 的渲染或编辑能力嵌入到自己的产品中，如在线家装设计平台、建筑咨询网站等。

## 项目亮点

与同类 Web 3D 编辑器相比，Pascal Editor 的核心差异在于：

- **前端技术栈原生**：基于 React Three Fiber 构建，对 React 开发者友好，可复用现有组件生态，定制和扩展成本低。
- **WebGPU 基础设施**：采用下一代 Web 图形 API，相比传统 WebGL 渲染效率更高，支持更复杂的场景和更流畅的编辑体验。
- **模块化发布**：核心、查看器、编辑器、节点库彼此独立，开发者只需按需安装，避免臃肿的全量引入。
- **开放插件机制**：通过 `loadPlugin` 接口允许任意节点库接入，社区可以贡献专用节点包，形成生态。

## 相关链接

- [GitHub 仓库](https://github.com/pascalorg/editor)
- [@pascal-app/viewer 快速开始](https://github.com/pascalorg/editor/blob/main/packages/viewer/README.md#usage)
- [Discord 社区](https://discord.gg/SaBRA9t2)
- [X (Twitter) 官方账号](https://x.com/pascal_app)
