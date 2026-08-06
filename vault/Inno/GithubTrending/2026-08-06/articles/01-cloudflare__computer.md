---
tags:
  - trending
  - article
repo: cloudflare/computer
date: 2026-08-06
language: TypeScript
stars_total: 3527
stars_today: 891
---
## 项目概述

Cloudflare Computer 是一个运行在 Durable Object 内部的虚拟文件系统。它由 Cloudflare 官方推出，核心思路是将 SQLite 作为权威数据存储，通过可插拔的执行表面（`workspace.runtime`）为 AI 代理（Agent）提供一个完整的计算机环境。该项目解决了 AI 代理在执行复杂任务时缺乏持久化、可编程文件系统的问题，让代理能够像人类一样操作文件、运行命令、执行代码。目标用户是构建 AI 代理应用的开发者，尤其是需要在边缘环境（Edge）中运行可信代码并管理持久状态的团队。

## 核心功能

- **虚拟文件系统**：基于 SQLite 构建的权威文件系统，支持文件的增删改查、目录结构管理，可作为独立存储使用，无需绑定任何执行后端。
- **多后端执行表面**：通过 `workspace.runtime.exec(source, { backend })` 统一入口，支持三种后端——Container（FUSE 挂载的沙箱容器）、Isolate shell（基于 just-bash 的 Dynamic Worker）、Isolate JavaScript（ECMAScript 模块执行环境）。
- **Container 后端**：将 SQLite 状态投影为真实 FUSE 挂载，提供完整的 Linux 用户空间、真实二进制文件和网络访问。沙箱侧守护进程 `computerd` 负责挂载和通过 capnweb RPC 信道同步变更。
- **Isolate shell 后端**：在 Dynamic Worker 中运行 just-bash，通过 Workers RPC 直接连接权威 Workspace，无二次存储或同步往返，延迟极低。
- **Isolate JavaScript 后端**：在全新的 Dynamic Worker 中运行 ECMAScript 模块，支持结构化输入/结果、持久化相对导入、配置库、Workspace 驱动的 `node:fs/promises`，以及受信任的 `ws:git` 和 `ws:artifacts` 模块。
- **多后端注册与懒连接**：同一 Workspace 可注册多个后端，按稳定 ID 区分，后端在首次使用时才建立连接，节省资源。

## 技术架构

项目采用类型安全的 TypeScript 编写，核心架构围绕 Durable Object 展开：

- **权威状态存储**：所有文件系统状态存储在 Durable Object 绑定的 SQLite 中，保证数据的一致性和持久性，任何后端访问都通过同一状态源，避免了分布式系统常见的数据不一致问题。
- **可插拔后端抽象**：设计上通过 `workspace.runtime` 抽象出统一执行接口，使得不同后端（容器、shell、JS）可以无缝切换。这种插件式架构让开发者能根据任务需求选择最合适的执行环境，无需改动上层代码。
- **同步与通信机制**：Container 后端采用 FUSE + capnweb RPC 实现沙箱与权威状态的双向同步；Isolate 后端则直接利用 Workers RPC，减少了中间层，提升了性能。这种差异设计体现了对不同场景的针对性优化。
- **无后端模式**：Workspace 也可以完全脱离执行后端独立存在，仅提供文件系统访问，便于在不需要执行环境时复用存储能力。

## 安装与使用

由于项目处于预览阶段，安装步骤相对简单。首先确保你的环境已配置 Node.js 和 npm，然后安装：

```bash
npm install @cloudflare/computer
```

最小使用示例：

```typescript
import { Workspace } from "@cloudflare/computer";

// 创建无后端的 Workspace（仅文件系统）
const ws = new Workspace();

// 创建带后端后，执行 shell 命令
const wsWithShell = new Workspace({ backend: "isolate-shell" });
const result = await wsWithShell.runtime.exec("ls -la", { backend: "isolate-shell" });
console.log(result.stdout);

// 执行 JavaScript 模块
const jsResult = await wsWithShell.runtime.exec(
  `export default async function(ctx) { return await ctx.fs.readFile("/path/to/file", "utf8"); }`,
  { backend: "isolate-js" }
);
```

注意：由于 API 尚不稳定，建议参考仓库中的最新文档和示例代码进行开发。

## 适用场景

- **AI 代理工作流**：为代理提供持久化文件系统和代码执行能力，使其能够处理多步骤任务，如数据处理、文件转换、代码生成与测试。
- **边缘计算应用**：在 Cloudflare Workers 生态中构建需要本地文件系统状态和沙箱执行的环境，例如 Webhook 处理、自动化脚本运行。
- **多租户沙箱服务**：利用 Durable Object 的隔离性，为每个租户提供独立工作区，支持容器或 JS 后端，实现安全的多租户代码执行。
- **开发调试与原型验证**：快速搭建具有完整文件系统能力的开发环境，验证新想法或进行集成测试。

## 项目亮点

- **统一状态源**：所有后端共享同一个 SQLite 权威状态，消除了数据同步的复杂性，这一点与多数仅提供无状态执行环境的方案形成鲜明对比。
- **极低延迟的隔离执行**：Isolate 后端直接通过 Workers RPC 连接 Workspace，无需额外的存储或网络往返，性能优于常见的容器方案。
- **后端可插拔**：单一入口 `exec` 屏蔽了底层差异，让开发者可以灵活选择执行环境，且支持在同一个 Workspace 中混用多个后端。
- **持久化文件系统**：作为 Durable Object 的一部分，文件系统天然具备高可用和持久性，适合长期运行的代理任务。
- **活跃的社区关注**：项目上线即获得大量关注（当前已超 3500 星），说明其解决的实际问题和设计思路得到开发者认可。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/computer)
- [just-bash](https://github.com/vercel-labs/just-bash)（Isolate shell 后端依赖）
