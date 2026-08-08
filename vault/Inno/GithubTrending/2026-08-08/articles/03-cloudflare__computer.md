---
tags:
  - trending
  - article
repo: cloudflare/computer
date: 2026-08-08
language: TypeScript
stars_total: 5851
stars_today: 872
---
## 项目概述

Cloudflare Computer 是一个运行在 Cloudflare 边缘网络上的虚拟文件系统，由 Cloudflare 官方开发并开源。它将权威状态存储在 Durable Object 中，底层使用 SQLite 作为持久化引擎，并通过 `workspace.runtime` 暴露统一的执行接口。这个项目的核心目标是让开发者能够在 Cloudflare 的分布式基础设施上获得一个“有状态”的计算环境，解决传统 Serverless 平台在持久化文件系统、长时间运行任务和复杂运行时方面的不足。

项目面向的受众包括：需要在边缘环境运行真实 Linux 二进制文件的开发者、希望在 Serverless 架构中获得文件系统持久化能力的团队、以及对隔离执行环境（如容器、shell、JavaScript）有统一调用需求的平台工程师。

## 核心功能

- **多后端执行引擎**：通过 `workspace.runtime.exec(source, { backend })` 单一入口，支持三种执行后端——容器（Container）、隔离 Shell（Isolate shell）和隔离 JavaScript（Isolate JavaScript），后端按需惰性连接。
- **SQLite 权威存储**：所有文件系统状态由 Durable Object 内的 SQLite 数据库权威持有，并通过多样后端映射到不同的执行环境，保证数据一致性和可恢复性。
- **容器 FUSE 挂载**：容器后端将 SQLite 状态投影为真实 FUSE 挂载点，通过沙箱侧守护进程 `computerd` 与云端同步，提供完整的 Linux 用户空间、真实二进制执行和真实网络访问能力。
- **无额外存储的 Shell 执行**：隔离 Shell 后端直接在 Dynamic Worker 中运行 just-bash，通过 Workers RPC 直达权威 Workspace，避免了额外的数据存储或同步往返。
- **JavaScript 模块执行**：隔离 JavaScript 后端支持 ECMAScript 模块运行，具备结构化输入/结果、持久化相对导入、可配置库，以及基于 Workspace 的 `node:fs/promises` 和受信任的 `ws:git`、`ws:artifacts` 模块。
- **无后端独立使用**：Workspace 可在不注册任何后端的情况下单独构建，调用方仅使用文件系统能力，适合存储密集型应用。

## 技术架构

Cloudflare Computer 采用分层设计，将状态层与执行层解耦。状态层由 Durable Object 承载 SQLite 数据库，所有文件元数据和内容均在此持久化；执行层通过 `workspace.runtime` 抽象出多个可插拔后端，每个后端都负责将权威状态投影到自身运行环境中。

容器后端选用 FUSE 文件系统作为桥接机制，`computerd` 守护进程在容器内部挂载状态，并通过 capnweb RPC 通道双向同步变更；隔离 Shell 后端依赖 Workers RPC，直接在 Dynamic Worker 中执行命令，消除中间层同步；隔离 JavaScript 后端则在全新的 Dynamic Worker 中运行模块，借助语言的模块系统和 Workers 生态实现代码隔离和依赖管理。

这种架构的优势在于：所有后端共享同一份权威状态，无需复制粘贴数据；后端可以独立演进，新增执行环境只需实现同一 `runtime` 接口；SQLite 的强一致性保证了并发访问下的可靠性。同时，所有执行环境都是临时的，仅在有调用时惰性创建，从而控制资源成本。

## 安装与使用

由于 Cloudflare Computer 目前以预览版形式发布，API 尚不稳定，建议通过 npm 安装并参考如下最小示例：

```bash
npm install @cloudflare/computer
```

创建一个 Workspace 实例，并执行一段容器后端命令：

```typescript
import { Workspace } from "@cloudflare/computer";

// 创建一个无后端的 Workspace
const ws = new Workspace();

// 注册容器后端（假设已配置 sandbox 参数）
const containerBackend = ws.registerBackend("container", { type: "container" });

// 在容器中执行命令
const result = await ws.runtime.exec("echo hello from cloudflare computer", {
  backend: "container",
});

console.log(result.stdout);
```

如需在容器内操作具体文件，需先通过 Workspace 的 API 写入文件，再在命令中引用挂载路径：

```typescript
await ws.writeFile("/hello.txt", "world");
const out = await ws.runtime.exec("cat /hello.txt", { backend: "container" });
```

## 适用场景

- **边缘计算与数据处理**：在靠近用户的边缘节点运行需要文件系统状态的计算任务，如日志聚合、图像处理或数据转换，减少回源延迟。
- **CI/CD 与构建流水线**：利用容器后端执行真实构建工具链，结合 SQLite 持久化构建缓存，加速重复构建过程。
- **多运行时服务编排**：同一份文件状态需要被 Shell 脚本、JavaScript 模块和容器程序共同操作的场景，统一通过 Workspace 进行读写。
- **原型验证与教学演示**：由于无需管理基础设施，开发者可以快速搭建一个带文件系统的在线代码执行环境，用于技术分享或教学。

## 项目亮点

- **统一状态，多样执行**：无论是容器、Shell 还是 JavaScript，都操作同一份 SQLite 权威数据，避免了多存储之间的同步问题，这是与大多数 Serverless 平台显著不同的设计思路。
- **真实的 Linux 环境**：容器后端提供完整的 FUSE 挂载和真实网络，可以直接运行传统 Unix 工具和第三方二进制，大幅扩展了 Serverless 的适用范围。
- **边缘原生**：基于 Durable Objects 和 Dynamic Workers，天然具备全球分布、快速启动和弹性伸缩的 Cloudflare 边缘网络能力。
- **模块化设计**：后端可插拔、按需创建，资源利用率高；同时预留扩展新执行后端的可能性。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/computer)
- [just-bash 项目](https://github.com/vercel-labs/just-bash)
