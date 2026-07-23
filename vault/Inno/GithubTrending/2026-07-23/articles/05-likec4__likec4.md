---
tags:
  - trending
  - article
repo: likec4/likec4
date: 2026-07-23
language: TypeScript
stars_total: 4402
stars_today: 80
---
## 项目概述

LikeC4 是一个面向软件架构的建模语言及配套工具，旨在帮助团队以代码的方式描述、可视化并持续演进软件架构。它借鉴了 C4 模型 和 Structurizr DSL 的思想，但提供了更高的灵活性——你可以自定义或定义自己的符号、元素类型，以及任意数量的嵌套层级，完美贴合实际项目需求。目标用户是希望将架构文档与代码同步、实现“架构即代码”理念的软件开发者、架构师和团队。

## 核心功能

- **基于代码的架构模型**：通过简洁的 DSL 文件（如 `.c4` 文件）定义系统、容器、组件和关系，模型与代码同源，始终反映最新设计。
- **实时交互式图表生成**：运行 `npx likec4 start` 即可启动本地开发服务器，自动生成可缩放、可交互的架构图，支持高亮、导航和分层查看。
- **可自定义的符号与层级**：不局限于 C4 模型的固定层级，允许你扩展或重定义元素类型（如 `system`、`actor`、`queue`），并支持任意深度的嵌套，适应微服务、事件驱动等复杂架构。
- **Visual Studio Code 扩展**：提供专门的 VS Code 插件，支持语法高亮、自动补全、实时预览和错误检查，提升编写体验。
- **集成与导出**：支持导出为 SVG、PNG 等静态图片格式，也可嵌入到文档网站或作为 CI/CD 流程的一部分，确保架构图始终最新。
- **协作与版本管理**：所有架构定义以文本形式存储在 Git 仓库中，团队可以像管理代码一样进行审核、分支合并和版本回溯。

## 技术架构

LikeC4 使用 TypeScript 开发，核心分为三部分：
1. **DSL 解析器**：将 `.c4` 源文件解析为内存中的模型对象，支持语法校验和错误报告。
2. **布局引擎**：基于自动布局算法（如 Dagre 或自定义布局）将模型渲染为可视化图表，支持手动调整节点位置。
3. **前端渲染器**：使用 Web 技术（如 React 或 Canvas）生成响应式的交互式图表，支持缩放、拖拽和点击高亮。

设计上，LikeC4 强调**模型与视图分离**：DSL 定义纯模型（元素和关系），而视图（如系统上下文图、容器图）通过独立的视图声明控制展示方式和范围。这种设计使得同一个模型可以衍生出多个不同的图表视角，同时保持模型本身的一致性。

## 安装与使用

**安装 CLI**：
```bash
npm install -g likec4
```

**创建项目**：
```bash
mkdir my-architecture
cd my-architecture
likec4 init
```

**编写架构定义**（在 `src/` 目录下创建 `model.c4`）：
```c4
workspace "My System" {
    model {
        user = person "用户"
        system = softwareSystem "我的系统" {
            webApp = container "Web 应用" {
                this.tags "frontend"
            }
            api = container "API 服务" {
                this.tags "backend"
            }
        }
        user -> webApp "使用"
        webApp -> api "调用"
    }
    views {
        systemContext view "系统上下文" {
            include *
            autoLayout
        }
    }
}
```

**启动预览**：
```bash
npx likec4 start
```
浏览器自动打开 `http://localhost:5173`，实时显示可交互的架构图。

## 适用场景

- **微服务架构文档化**：在拥有几十个微服务的项目中，用 LikeC4 描述服务边界、通信方式和依赖关系，保持文档与实际部署同步。
- **技术债务治理**：通过架构模型识别模块间的循环依赖、过度耦合或缺少抽象层，为重构提供依据。
- **新成员入职文档**：为新加入的开发者提供清晰、可浏览的系统地图，加速理解业务模块和技术栈划分。
- **架构评审与决策记录**：在架构决策记录（ADR）中嵌入 LikeC4 图表，使评审过程直观且可追溯。

## 项目亮点

与 Structurizr DSL 等同类工具相比，LikeC4 的核心差异化在于：
- **灵活性极高**：不强制使用固定的 C4 层级，允许自定义元素类型和任意嵌套层数，适用于 Event Storming、领域驱动设计（DDD）等不同方法论的建模需求。
- **零配置上手**：使用 `npx likec4 start` 即可启动交互式预览，无需安装 Docker 或配置数据库，适合快速原型和集成到现有项目。
- **实时反馈**：配合 VS Code 扩展，编辑 DSL 时图表自动更新，大幅降低调整模型的心智负担。
- **轻量级与可嵌入**：生成纯静态的 HTML/SVG 文件，可轻松集成到文档站点（如 Docusaurus、VitePress）或 CI 流程中。
- **社区与模板**：提供官方模板仓库和 Playground，让新用户能立即体验并快速创建项目。

## 相关链接

- [GitHub 仓库](https://github.com/likec4/likec4)
- [官方文档](https://likec4.dev)
- [在线 Playground](https://playground.likec4.dev)
- [模板仓库](https://template.likec4.dev/view/index)
- [VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=likec4.likec4-vscode)
