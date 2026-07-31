---
tags:
  - trending
  - article
repo: pascalorg/editor
date: 2026-07-31
language: TypeScript
stars_total: 20218
stars_today: 625
---
## 项目概述

Pascal Editor 是一个基于 Web 的 3D 建筑编辑器，旨在让用户快速创建、编辑并分享三维建筑项目。该项目使用 React Three Fiber 和 WebGPU 技术构建，将复杂的 3D 建模能力带入浏览器，无需安装任何桌面软件即可完成建筑设计工作流。无论是建筑师、室内设计师、学生还是建筑爱好者，都可以通过直观的界面和可扩展的节点系统，将创意转化为可视化的三维模型，并通过链接轻松分享给他人。

## 核心功能

- **实时 3D 编辑**：基于 WebGPU 的高性能渲染管线，支持流畅的视角操作、对象变换和场景导航，提供接近原生应用的交互体验。
- **节点化建筑系统**：内置丰富的建筑节点定义（墙体、门窗、楼板、家具等），用户可像搭积木一样组合节点，快速搭建复杂建筑结构。
- **场景状态管理**：通过`@pascal-app/core`包提供规范化的场景数据模型，支持项目的保存、加载与版本管理，确保设计过程的连续性。
- **插件化扩展机制**：采用插件注册表架构，用户可自定义节点类型、渲染器和系统逻辑，突破内置功能限制，满足个性化设计需求。
- **跨平台分享**：生成的建筑项目可通过链接一键分享，查看者无需安装任何软件即可在浏览器中查看三维模型，支持团队协作与方案展示。
- **模块化包管理**：核心、查看器、编辑器和节点定义分离为独立 npm 包，开发者可按需引入，降低集成成本。

## 技术架构

Pascal Editor 采用 Turborepo 管理的 monorepo 结构，将关注点清晰分离至多个运行时包，形成分层清晰的架构体系：

- **核心层（@pascal-app/core）**：定义场景 Schema、状态管理逻辑和插件注册契约，是连接各包的"数据中枢"。该层不依赖任何渲染实现，确保数据模型的纯净性和可移植性。
- **渲染层（@pascal-app/viewer）**：负责 3D 场景的渲染运行时，基于 React Three Fiber 构建，封装了场景图管理、相机控制、光照系统与 WebGPU 渲染管线。查看器可独立于编辑器使用，仅需加载必要的插件即可嵌入任意 React 应用。
- **编辑层（@pascal-app/editor）**：提供创建和修改场景所需的工具集与 UI 组件，包括对象变换 gizmo、属性面板、图层管理等，与渲染层解耦，便于替换或扩展编辑交互方式。
- **节点语义层（@pascal-app/nodes）**：定义内置节点（墙、门、窗等）的数据结构、渲染器与对应系统行为。节点通过插件机制加载，可动态注册到核心注册表中，实现真正的鸭子类型扩展。
- **应用层（apps/editor）**：基于 Next.js 构建的完整编辑器应用，整合上述所有包，提供用户可直接访问的 Web 界面。

该架构的关键设计在于"插件即数据"的理念：节点定义、渲染器和系统均作为可注册实体，在运行时动态加载，而非硬编码编译。这使得第三方开发者能够以统一接口扩展编辑器能力，而无需修改核心代码。

## 安装与使用

### 使用发布包

若要单独使用查看器或开发自定义节点，可通过 npm 安装相关包：

```bash
npm install @pascal-app/core @pascal-app/viewer @pascal-app/editor @pascal-app/nodes
```

在 React 应用中加载内置节点插件：

```typescript
import { loadPlugin } from '@pascal-app/core'
import { builtinPlugin } from '@pascal-app/nodes'

await loadPlugin(builtinPlugin)
```

随后即可挂载`<Viewer>`组件用于场景展示。完整的 React 示例可参阅`@pascal-app/viewer`包的快速开始文档。

### 本地开发

克隆仓库并安装依赖：

```bash
git clone https://github.com/pascalorg/editor.git
cd editor
npm install
```

启动开发服务器：

```bash
npm run dev
```

默认会在本地启动 Next.js 编辑器应用，浏览器访问`http://localhost:3000`即可开始编辑。

## 适用场景

- **建筑方案快速推敲**：设计师可在几分钟内搭建建筑体块与空间关系，辅助前期概念方案的形体和功能推敲，替代传统草图或繁重的建模软件。
- **室内设计可视化**：利用内置的家具与材质节点，快速布置室内空间，并通过实时渲染检查光照和材质效果，生成客户可交互的预览链接。
- **教育实训与展示**：建筑类院校可将 Pascal Editor 作为教学工具，让学生在浏览器中直观理解三维空间构成，并通过分享功能提交作业成果。
- **轻量级协同评审**：项目成员通过分享的链接即可同时查看同一模型，无需安装专业软件，降低评审反馈的门槛，提升沟通效率。

## 项目亮点

- **纯 Web 技术栈**：基于 WebGPU 和 React Three Fiber，无需插件或桌面运行时，天然适配现代浏览器，大幅降低使用门槛。
- **插件优先架构**：与常见的单体编辑器不同，Pascal Editor 将核心、渲染和节点定义拆分，并采用运行时插件注册机制，使得扩展性成为第一等公民，开发者可围绕统一契约构建垂直领域解决方案。
- **语义化数据模型**：场景状态基于严谨的 Schema 定义，而非依赖图形化文件格式，这为程序化生成、AI 辅助设计和第三方工具互操作奠定了基础。
- **模块化消费友好**：各包可独立使用，例如仅用`@pascal-app/viewer`嵌入已有项目展示 3D 场景，或仅用`@pascal-app/core`处理场景数据，集成成本极低。

## 相关链接

- [GitHub 仓库](https://github.com/pascalorg/editor)
- [npm: @pascal-app/core](https://www.npmjs.com/package/@pascal-app/core)
- [npm: @pascal-app/viewer](https://www.npmjs.com/package/@pascal-app/viewer)
- [Discord 社区](https://discord.gg/SaBRA9t2)
- [X (Twitter)](https://x.com/pascal_app)
