---
tags:
  - trending
  - article
repo: pascalorg/editor
date: 2026-09-10
language: TypeScript
stars_total: 23116
stars_today: 107
---
## 项目概述

Pascal Editor 是一个开源的本地优先（local-first）三维建筑编辑器，使用 React Three Fiber 与 WebGPU 构建，代码主要由 TypeScript 编写。它同时面向两类用户：需要快速搭建、查看和调整建筑体块与室内布局的人类设计师，以及希望通过 MCP（Model Context Protocol）协议驱动编辑操作的 AI 代理。

项目要解决的核心问题是三维建筑编辑工具通常依赖云端、难以脚本化、且对 AI 代理不友好。Pascal Editor 将编辑器本体、CLI 和 MCP 服务都放在本地运行，数据存储于本机 SQLite 数据库，不需要克隆仓库即可启动，也便于把编辑能力嵌入自动化流程。

## 核心功能

- 浏览器与 CLI 双入口：既可以在浏览器中交互式编辑三维场景，也可以通过命令行启动本地编辑器服务，适配不同的工作习惯。
- 本地持久化存储：项目数据写入 `~/.pascal/data/pascal.db`，无需注册账号或依赖远程服务。
- 内置 MCP 服务：CLI 启动时会在后台运行带鉴权的 MCP 服务，供 AI 代理连接并调用编辑工具。
- 冲突规避的端口选择：自动挑选无冲突的环回（loopback）端口，减少本地多实例运行时的配置负担。
- 面向代理的工作流：README 提到仓库版本包含只读的家具候选检查（read-only furniture candidate check）以及托管代理的 claim/status 命令，用于支持 AI 代理参与设计流程。
- 模块化 npm 包：拆分为 `@pascal-app/core`、`@pascal-app/viewer`、`@pascal-app/cli` 等包，便于按需引用。

## 技术架构

项目采用以 React Three Fiber 为基础的声明式三维渲染管线，底层图形能力由 WebGPU 提供，因此在支持 WebGPU 的现代浏览器中可以获得更好的渲染性能。整体是"本地优先"架构：编辑器的运行时、数据存储和 MCP 服务都运行在用户机器上，不依赖中心化后端。

职责划分上，`core` 承担编辑器核心逻辑与数据模型，`viewer` 负责三维查看与渲染，`cli` 负责启动、端口管理、项目管理和 MCP 服务编排。CLI 启动编辑器时会一并拉起经过鉴权的 MCP 服务，AI 代理通过 `pascal mcp connect` 接入，从而以工具调用的方式操作编辑会话。数据层面使用 SQLite 文件持久化，路径固定，便于备份和迁移。

## 安装与使用

运行环境要求 Node.js 22.13 或更高版本。无需克隆仓库，直接用 npx 创建持久化的本地安装：

```bash
npx @pascal-app/cli editor
```

该命令会启动编辑器，并在后台运行带鉴权的 MCP 服务，同时自动选择无冲突的环回端口，项目数据保存在 `~/.pascal/data/pascal.db`。若要让 AI 代理接入，将其配置为启动 `pascal mcp connect` 即可。项目文档还提供了基于 pnpm 或 Bun 的命令、项目管理、MCP 配置、更新、存储路径与故障排查说明。

需要注意版本差异：npm 的 `beta` 标签当前指向 `@pascal-app/cli@1.0.0-beta.1`，该版本早于仓库中新增的只读家具候选输入和托管代理 claim/status 命令。如果需要使用这些能力，应改用仓库中经过验证的 GitHub 预览版本。

## 适用场景

- 建筑与室内方案的快速体块推敲：在浏览器中交互调整空间布局，结果本地保存。
- AI 辅助设计流程：通过 MCP 让代理读取场景、执行编辑或做候选检查，把自然语言需求落到具体几何操作上。
- 自动化脚本与集成：借助 CLI 和 npm 包，把编辑器嵌入构建、批处理或自建工具链。
- 本地离线工作：数据不出本机，适合对隐私和网络独立性有要求的团队或个人。

## 项目亮点

与常见云端三维设计工具相比，Pascal Editor 的差异点在于"本地优先 + 代理友好"的组合：编辑器、存储、MCP 服务全部在本地运行，同时又为 AI 代理提供了标准的工具接入方式。WebGPU 渲染配合 React Three Fiber 的声明式写法，降低了扩展和二次开发的成本；CLI 一键启动并自动处理端口与持久化，减少了环境配置摩擦。MIT 许可证也让它在商业与内部项目中都较易采用。

## 相关链接

- [GitHub 仓库](https://github.com/pascalorg/editor)
- [本地运行文档](https://editor.pascal.app/docs/developers/local-editor)
- [@pascal-app/core](https://www.npmjs.com/package/@pascal-app/core)
- [@pascal-app/viewer](https://www.npmjs.com/package/@pascal-app/viewer)
- [@pascal-app/cli](https://www.npmjs.com/package/@pascal-app/cli)
- [Discord 社区](https://discord.gg/XRKsDcpqgS)
