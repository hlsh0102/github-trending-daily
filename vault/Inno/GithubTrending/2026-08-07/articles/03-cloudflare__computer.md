---
tags:
  - trending
  - article
repo: cloudflare/computer
date: 2026-08-07
language: TypeScript
stars_total: 4947
stars_today: 2802
---
## 项目概述

Cloudflare Computer 是一个运行在 Durable Object 内部的虚拟文件系统。它将权威状态保存在 SQLite 中，并通过 `workspace.runtime` 暴露一个可插拔的执行表面。简而言之，它让你的 Agent 拥有了一台"计算机"——一个持久化、可编程、可执行代码的虚拟工作空间。

这个项目解决了云原生应用中状态与执行分离的问题。传统方案要么将文件系统放在外部存储（如 S3 或网络卷），要么将执行环境与状态存储耦合在一起。Cloudflare Computer 将两者统一：SQLite 保存权威状态，而多种运行时后端（容器、隔离 Shell、隔离 JavaScript）可以自由地挂载或访问这个状态。目标用户是需要在边缘或 Worker 环境中运行复杂工作负载的开发者，尤其是构建 AI Agent、自动化流水线或需要持久化文件系统的应用开发者。

## 核心功能

- **多后端执行**：支持三种运行后端——容器（完整 Linux 用户空间）、隔离 Shell（基于 just-bash）、隔离 JavaScript（ECMAScript 模块）。每个后端通过 `workspace.runtime.exec` 统一入口调用，按需懒连接。
- **权威状态中心化**：所有文件系统操作都汇聚到 SQLite 中，任何后端看到的都是同一份数据，避免了多副本同步问题。
- **容器 FUSE 挂载**：容器后端将 SQLite 状态投影为真实文件系统挂载（FUSE），通过 `computerd` 守护进程和 capnweb RPC 通道同步变更。
- **零同步的 Shell 执行**：Isolate Shell 后端直接在 Dynamic Worker 中运行，通过 Workers RPC 直接访问权威 Workspace，无需额外的存储或同步往返。
- **Durable JavaScript 运行时**：支持结构化输入/输出、持久化相对导入、可配置库、Workspace 支持的 `node:fs/promises`、受信任的 `ws:git` 和 `ws:artifacts` 模块。
- **后端可注册与插拔**：Workspace 可以在稳定 ID 下注册多个后端，调用方自由选择执行环境。

## 技术架构

Cloudflare Computer 的核心架构围绕一个简单的理念：**文件系统即状态**。Durable Object 持有 SQLite 数据库作为不可变事实源，同时暴露一个 `workspace.runtime` 执行接口。代码调用的流程是：

1. `workspace.runtime.exec(source, { backend })` 被调用，`source` 可以是 Shell 命令或 ECMAScript 模块。
2. Durable Object 根据 `backend` 参数选择合适的执行后端。
3. 后端连接是懒加载的，首次使用时才建立通道。

**容器后端**：将 SQLite 中的文件系统通过 FUSE 投影到沙箱容器内。`computerd` 守护进程在沙箱侧挂载文件系统，并通过 capnweb RPC（Cloudflare 的 RPC 框架）将变更同步回 SQLite。这提供了完整的 Linux 用户空间体验——可以运行真实二进制、访问真实网络。

**Isolate Shell 后端**：直接在 Dynamic Worker 中运行 just-bash。它通过 Workers RPC 直接访问权威 Workspace，没有中间存储或同步步骤，非常适合快速迭代和命令执行。

**Isolate JavaScript 后端**：创建全新的 Dynamic Worker，运行 ECMAScript 模块。支持结构化输入/输出（JSON 序列化）、持久化相对导入（文件可以跨调用保留）、可配置库版本、Workspace 文件系统操作（通过 `node:fs/promises` 的适配层）以及受信任模块 `ws:git`（Git 操作）和 `ws:artifacts`（产物存储）。

架构上的关键设计包括：后端与状态完全解耦、执行入口单一、数据传输通过结构化协议（Cap'n Proto 或 RPC）而非原始文件流。Workspace 也可以完全无后端构建，仅作为纯文件系统 API 使用。

## 安装与使用

由于项目目前处于预览阶段（PREVIEW ONLY），API 不稳定。以下为基于 README 和常见模式的基本用法示例：

```bash
# 安装（假设已配置 Cloudflare Workers 环境）
npm install @cloudflare/computer
```

最小使用示例（JavaScript 环境）：

```typescript
import { Computer } from '@cloudflare/computer';

// 创建 Workspace（无后端，仅文件系统）
const ws = await Computer.create();

// 写入文件
await ws.fs.writeFile('/hello.txt', 'world');

// 注册后端（以 Isolate JavaScript 为例）
await ws.runtime.register('js', { type: 'javascript' });

// 执行隔离的 JavaScript 模块
const result = await ws.runtime.exec(`
  export default async function ({ fs }) {
    const content = await fs.readFile('/hello.txt', 'utf8');
    return { message: 'Hello ' + content };
  }
`, { backend: 'js' });

console.log(result); // { message: 'Hello world' }
```

对于容器后端，需要在沙箱环境配置 FUSE 挂载和 `computerd` 守护进程，具体部署细节需参考 Cloudflare 官方文档。

## 适用场景

- **AI Agent 工作区**：为 LLM Agent 提供持久化的文件系统，Agent 可以读写文件、执行 Shell 命令或运行 JavaScript 模块，跨多次对话保持状态。
- **云端开发环境**：将开发环境（包括文件、依赖、工具链）抽象为虚拟文件系统，在边缘动态创建和销毁。
- **自动化流水线**：在 CI/CD 或数据处理管道中，需要一个临时但持久的文件系统来暂存中间产物，同时支持多种执行语言。
- **多租户应用**：每个租户拥有独立的 Workspace，数据隔离在 SQLite 中，执行环境按需启动，资源利用率高。

## 项目亮点

- **状态与执行分离**：与其他方案（如直接挂载云存储）不同，Cloudflare Computer 将权威状态集中在 SQLite，执行后端只是视图，从根本上避免了分布式一致性问题。
- **异构后端统一接口**：容器、Shell、JavaScript 三种执行环境通过同一个 `runtime.exec` 接口访问，切换成本为零。
- **边缘原生**：基于 Durable Object 和 Dynamic Worker，充分利用 Cloudflare 的边缘网络，延迟低、扩展性好。
- **相对导入与持久化**：Isolate JavaScript 后端支持持久化相对导入，文件系统在多次执行之间保持不变，突破了传统无状态函数的限制。
- **活跃社区关注**：项目发布后迅速获得关注（发布当天新增约 2800 星），显示出开发者对云原生虚拟文件系统需求的强烈兴趣。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/computer)
- [just-bash](https://github.com/vercel-labs/just-bash)（Isolate Shell 后端依赖）
