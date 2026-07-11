---
tags:
  - trending
  - article
repo: oven-sh/bun
date: 2026-07-11
language: Rust
stars_total: 94338
stars_today: 209
---
## 项目概述

Bun 是一个专为 JavaScript 和 TypeScript 应用打造的一体化工具集，由 Oven 团队使用 Rust 语言开发。它以一个名为 `bun` 的单一可执行文件发布，旨在成为 Node.js 的直接替代品。Bun 从底层采用 JavaScriptCore 引擎（而非 Node.js 的 V8 引擎），并利用 Rust 语言的高性能特性，在启动速度、内存占用和执行效率上实现了显著提升。项目的目标用户是希望简化开发工具链、追求极致性能和现代开箱即用体验的前端与全栈开发者。

## 核心功能

- **极速 JavaScript 运行时**：作为 Node.js 的替代运行时，Bun 能在毫秒级启动，大幅减少脚本执行前的等待时间。开箱即用支持 TypeScript 和 JSX，无需额外配置。
- **内置打包器 (Bundler)**：Bun 包含一个高性能打包器，能够快速将多文件项目打包为单一输出文件。它兼容 Node.js 模块解析算法，可替代 Webpack、esbuild 等打包工具。
- **高速测试运行器**：Bun 集成了兼容 Jest API 的测试框架，无需安装 Jest 或 Mocha 即可运行单元测试。测试执行速度通常是 Jest 的数倍。
- **原生包管理器**：Bun 内置兼容 npm 生态的包管理器，可直接安装 npm 包。其安装速度是 npm 或 yarn 的数倍，采用全局锁文件来避免重复解析依赖。
- **Node.js API 兼容**：Bun 努力实现与 Node.js 核心模块（如 `fs`、`path`、`http`）的高度兼容，并支持 CommonJS 和 ES 模块混合使用，让现有 Node.js 项目平滑迁移。
- **环境变量与脚本管理**：通过 `bun run` 命令可直接执行 `package.json` 中的脚本，并自动加载 `.env` 文件，简化开发配置流程。

## 技术架构

Bun 的技术堆栈以 Rust 和 JavaScriptCore 为核心。JavaScriptCore 是 WebKit 浏览器的 JavaScript 引擎，其即时编译 (JIT) 策略与 V8 不同，在启动速度和内存开销上具有优势。Rust 语言则用于实现文件 I/O、网络请求、HTTP 解析等底层操作，借助其零成本抽象和内存安全特性，Bun 在大量场景下能达到接近原生编译代码的性能。

Bun 的设计思路是“一切内建”——将运行时、打包器、测试运行器和包管理器整合为同一个二进制文件，减少工具链的耦合与版本冲突。其包管理器采用基于文件系统的全局锁机制（如 `.bun.lockb`），一次性解析并缓存所有依赖，避免重复锁定操作。打包器则使用了与 esbuild 类似的并行工作架构，充分利用多核 CPU 进行并行编译。

## 安装与使用

Bun 的安装极其简单，支持 macOS、Linux 和 Windows（通过 WSL）。

**快速安装**：

```bash
# macOS / Linux
curl -fsSL https://bun.sh/install | bash

# 或使用 npm
npm install -g bun
```

**最小可用示例**：

1. 创建一个简单的 HTTP 服务器文件 `server.ts`：

```typescript
// 可以直接运行 TypeScript，无需先编译
Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Hello from Bun!");
  },
});
console.log("Server running at http://localhost:3000");
```

2. 使用 Bun 运行：

```bash
bun run server.ts
```

3. 运行测试（无需安装测试框架）：

```typescript
// test.ts
import { describe, expect, test } from "bun:test";

describe("math", () => {
  test("addition", () => {
    expect(1 + 1).toBe(2);
  });
});
```

```bash
bun test
```

## 适用场景

- **微服务与 API 服务器**：利用 Bun 极低的启动延迟和内置 HTTP 服务器，可快速部署轻量级 REST 或 GraphQL API 服务，尤其在需要频繁重启开发的场景下体验极佳。
- **CLI 工具开发**：Bun 的快速执行和原生 TypeScript 支持非常适合构建命令行工具，开发者无需经过复杂的构建配置即可编写和分发工具。
- **前端工程化**：使用 Bun 作为包管理器取代 npm/yarn 可大幅缩短 CI/CD 中的依赖安装时间。同时其内置打包器可用于小型项目的构建，简化前端工具链。
- **全栈应用原型设计**：从后端 API 到前端静态资源打包，Bun 提供了一站式解决方案，适合快速验证产品想法或编写教学演示代码。

## 项目亮点

- **极致的性能**：Bun 在常见的基准测试中，启动速度比 Node.js 快 4 倍以上，包安装速度比 npm 快 10 倍以上，测试执行速度也是 Jest 的数倍。这种性能优势源于 Rust 底层实现和 JavaScriptCore 引擎的协同优化。
- **工具链一体化**：大多数开发者需要在 Node.js 环境中同时使用 Webpack/esbuild、Jest/Mocha、npm/yarn 等工具。Bun 将这四个功能整合为一个可执行文件，消除了版本兼容问题与配置复杂度，极大地提高了开发效率。
- **开箱即用的现代特性**：无需安装 `ts-node`、`tsc` 或 `ts-jest`，Bun 原生支持 TypeScript 和 JSX。开发者可以直接编写和运行 `.tsx` 文件，测试框架也支持类型定义，降低了项目初始化的门槛。
- **活跃的社区与持续迭代**：Bun 在 GitHub 上拥有超过 94,000 个 star 和活跃的 Discord 社区。项目仍处于快速迭代期，每周都会发布新版本，不断改进 Node.js API 兼容性和新增功能。

## 相关链接

- [GitHub 仓库](https://github.com/oven-sh/bun)
- [官方文档](https://bun.com/docs)
- [Discord 社区](https://bun.com/discord)
- [项目路线图](https://github.com/oven-sh/bun/issues/159)
