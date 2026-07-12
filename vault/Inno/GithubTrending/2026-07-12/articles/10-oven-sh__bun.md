---
tags:
  - trending
  - article
repo: oven-sh/bun
date: 2026-07-12
language: Rust
stars_total: 94592
stars_today: 658
---
## 项目概述

Bun 是一个面向 JavaScript 和 TypeScript 应用的全能工具集，由 Oven 团队使用 Rust 语言开发。它以一个名为 `bun` 的单一可执行文件形式交付，集 JavaScript 运行时、打包器、测试运行器和包管理器于一身。Bun 旨在成为 Node.js 的即用替代品，显著缩短启动时间并降低内存消耗，尤其适合追求高性能和简洁开发体验的开发者。该项目在 GitHub 上拥有超过 94,000 颗星，反映了社区对其速度和集成度的认可。

## 核心功能

- **高速 JavaScript 运行时**：基于 Rust 和 JavaScriptCore 引擎打造，启动速度远超 Node.js，支持 TypeScript 和 JSX 开箱即用，无需额外配置。
- **内置包管理器**：原生支持 npm 包安装，速度比 npm 和 Yarn 快数倍，兼容现有的 `package.json` 和 `node_modules` 结构。
- **一体化打包器**：提供类似于 Webpack 或 esbuild 的打包能力，可直接将 JavaScript/TypeScript 应用打包为单文件，简化构建流程。
- **内置测试运行器**：支持 Jest 兼容的 API，能直接运行测试文件，无需单独安装 Jest 或其他测试框架。
- **跨平台支持**：支持 macOS、Linux 和 Windows（通过 WSL），并提供单一执行文件安装，降低部署复杂度。

## 技术架构

Bun 的核心设计理念是“一体化”，即用一个工具替代 Node.js、npm、yarn、webpack、jest 等多个独立工具。其技术实现主要依赖以下亮点：

- **JavaScriptCore 引擎**：Bun 使用 WebKit 的 JavaScriptCore 作为底层运行时，而非 Node.js 常用的 V8 引擎。JavaScriptCore 在启动速度和内存管理上具有优势，使得 Bun 的冷启动时间通常比 Node.js 快 4 倍以上。
- **Rust 语言开发**：整个工具链使用 Rust 编写，避免了 C++ 带来的内存安全和并发问题，同时保证了接近原生代码的性能。Rust 的零成本抽象特性，让 Bun 在文件 I/O、网络请求等场景下表现出色。
- **原生 Node.js 兼容性**：Bun 实现了对 Node.js API 的全面兼容，包括 `fs`、`http`、`path` 等核心模块。大部分 npm 包无需修改即可在 Bun 中运行，降低了迁移成本。
- **优化的包安装算法**：Bun 的包管理器采用全局锁和并行下载策略，减少了网络请求和磁盘写入开销。在测试中，安装一个中等规模项目的依赖项，Bun 的速度可达 npm 的 10 倍以上。

## 安装与使用

Bun 提供多种安装方式，推荐使用官方安装脚本：

```bash
# macOS 和 Linux
curl -fsSL https://bun.sh/install | bash

# 通过 npm（需要 Node.js 16+）
npm install -g bun

# 通过 Homebrew（macOS）
brew tap oven-sh/bun
brew install bun
```

安装完成后，验证是否成功：

```bash
bun --version
```

最小可用示例：创建一个简单的 HTTP 服务器，支持 TypeScript。

创建一个 `server.ts` 文件：

```typescript
// server.ts
Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Hello, Bun!");
  },
});

console.log("Server running on http://localhost:3000");
```

运行：

```bash
bun run server.ts
```

使用内置包管理器安装依赖：

```bash
bun add express
```

使用内置测试运行器：

```bash
# 创建一个测试文件 test.test.js
import { describe, expect, test } from "bun:test";

describe("数学运算", () => {
  test("加法", () => {
    expect(1 + 1).toBe(2);
  });
});

# 运行测试
bun test
```

## 适用场景

- **快速原型开发**：Bun 的即时启动和 TypeScript/JSX 原生支持，让开发者能快速验证想法，无需等待构建工具启动。
- **全栈 JavaScript 应用开发**：从后端 API 到前端打包，Bun 提供一站式解决方案，减少工具链碎片化问题，特别适合初创团队或小型项目。
- **高性能微服务**：由于启动快、内存占用低，Bun 非常适合部署在云函数或容器化微服务中，能快速响应请求并降低资源成本。
- **持续集成/持续部署管道**：在 CI 环境中，Bun 的快速安装和测试执行能显著缩短流水线时间，提升开发效率。

## 项目亮点

Bun 与 Node.js、Deno、esbuild 和 Jest 等传统工具相比，具有以下差异化优势：

- **极致的集大成**：Bun 不是单纯的运行时，而是将运行、打包、测试、包管理四种功能融为一体。一个 `bun` 命令即可覆盖开发全流程，消除了不同工具间的版本冲突和配置开销。
- **无与伦比的速度**：在基准测试中，Bun 的启动速度是 Node.js 的 4 倍，包安装速度是 npm 的 10 倍，测试执行速度接近 Jest 的 2 倍。这些性能优势来源于 Rust 和 JavaScriptCore 的底层技术选型。
- **零配置体验**：开发者无需安装 TypeScript 编译器、Webpack 配置或 Babel 插件，即可直接运行 `.ts` 和 `.jsx` 文件。这种“开箱即用”的设计大幅降低了入门门槛。
- **活跃的社区和生态系统**：Bun 拥有不断增长的 npm 包兼容性，贡献者社区积极解决兼容性问题。官方 Discord 频道和 GitHub Issues 提供快速反馈渠道，Roadmap 清晰透明。

## 相关链接

- [GitHub 仓库](https://github.com/oven-sh/bun)
- [官方文档](https://bun.sh/docs)
- [Discord 社区](https://bun.sh/discord)
- [项目路线图](https://github.com/oven-sh/bun/issues/159)
