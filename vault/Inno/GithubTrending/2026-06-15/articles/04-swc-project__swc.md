---
tags:
  - trending
  - article
repo: swc-project/swc
date: 2026-06-15
language: Rust
stars_total: 33838
stars_today: 163
---
## 项目概述

SWC（全称 Speedy Web Compiler）是一个基于 Rust 语言构建的超高速 Web 平台编译器。它主要用于将 JavaScript 和 TypeScript 代码进行转译、打包和优化，旨在显著提升 Web 开发过程中的编译速度。SWC 的核心目标是“让 Web 开发更快”——通过利用 Rust 的系统级性能优势，它能够将传统 JavaScript 工具链（如 Babel）的编译速度提升数十倍甚至上百倍。项目面向所有现代 Web 开发者，特别是在大型代码库中受困于缓慢构建流程的团队，以及追求极致开发体验的前端工程师。

## 核心功能

- **超高速转译**：SWC 能够以极快的速度将 TypeScript、JSX 等现代 JavaScript 语法转译为兼容性更好的 ES5 或 ES6 代码，通常比 Babel 快 20 倍以上。
- **内置支持 TypeScript**：全面支持 TypeScript 语法解析与类型擦除，可直接作为 TypeScript 编译器的高性能替代方案。
- **模块打包能力**：提供 `@swc/plugin` 插件系统和 `swcpack` 打包器，支持 CommonJS、ESM 等模块格式的转换与打包。
- **代码压缩与优化**：内置 `swc_compress` 模块，能够对 JavaScript 代码进行高效压缩，生成体积更小、性能更优的输出。
- **AST 转换与插件系统**：基于成熟的 AST（抽象语法树）架构，允许开发者通过编写 Rust 或 WASM 插件来自定义代码转换逻辑。
- **多种使用方式**：提供 Node.js API、CLI 命令行工具以及 Vite/Webpack 等主流构建工具的集成插件，适配不同开发流程。

## 技术架构

SWC 采用 Rust 语言作为核心开发语言，这奠定了其高性能的基础。其架构主要分为以下几个关键层次：

- **解析器（Parser）**：使用 Rust 重写的 ECMAScript 解析器 `swc_ecma_parser`，基于 `swc_atoms` 和 `swc_common` 等基础库，能够快速生成符合规范的高质量 AST。
- **AST 与遍历器**：AST 结构设计轻量高效，配合 `swc_visit` 和 `swc_macros` 宏系统，实现了不产生额外内存开销的零成本抽象遍历机制。
- **转换器（Transformer）**：将 Babel 插件生态中的常用转换（如 `@babel/preset-env` 中的 polyfill 注入、装饰器转换）用 Rust 重写，确保每次转换都保持高性能。
- **代码生成器（Code Generator）**：负责从 AST 生成最终文本代码，支持多种输出格式（如 ESM、CommonJS），并可选集成代码压缩逻辑。
- **插件系统**：支持通过 Rust 编译为 WASM 的方式加载第三方插件，使得核心编译器保持轻量，同时允许社区贡献自定义功能。

整个项目采用模块化、松耦合的设计，核心编译器与打包器分离，既可作为独立工具使用，也能嵌入到其他构建系统中。

## 安装与使用

SWC 的安装和基本使用非常简单。首先需要 Node.js 环境（建议 v14 以上），通过 npm 或 yarn 安装：

```bash
npm install --save-dev @swc/core @swc/cli
```

或者全局安装 CLI：

```bash
npm install -g @swc/cli
```

一个最小可用的示例：假设有一个 `input.ts` 文件包含 TypeScript 代码：

```typescript
const greet = (name: string): string => `Hello, ${name}!`;
console.log(greet('World'));
```

直接使用 CLI 编译：

```bash
swc input.ts -o output.js
```

生成的 `output.js` 将是纯 JavaScript 代码（默认输出 ES6）。若要配置更详细的转译行为，可以在项目根目录创建 `.swcrc` 文件，例如：

```json
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": false
    },
    "target": "es2020"
  },
  "module": {
    "type": "commonjs"
  }
}
```

然后运行 `swc input.ts -o output.js` 即可得到转译为 CommonJS 模块的 ES2020 兼容代码。

## 适用场景

- **大型项目构建加速**：当使用 Webpack、Vite 等构建工具编译包含数千个模块的庞大前端项目时，用 SWC 替代 Babel 加载器可大幅减少每次保存后的热更新和全量编译耗时。
- **TypeScript 编译优化**：在需要频繁编译 TypeScript 代码的 CI/CD 流水线中，使用 SWC 作为实时编译器，能显著缩短构建时间，提升部署效率。
- **库与底层工具开发**：编写 Rust 或 WASM 插件以扩展 SWC 功能，用于语法分析、代码转换或自定义 lint 规则，适合需要定制化编译管线的团队。
- **服务端渲染优化**：在 Node.js 服务端使用 SWC 编译 JSX 或 TypeScript，加速 SSR 中的代码热替换和初次渲染速度。

## 项目亮点

与同类项目（如 Babel、esbuild）相比，SWC 的主要差异化优势包括：

- **兼容性优先**：虽然 esbuild 也很快，但 SWC 更加注重与 Babel 插件生态的兼容性，许多 Babel 插件的功能已用 Rust 重写实现，迁移成本更低。
- **插件扩展性强**：不同于 esbuild 的封闭生态，SWC 通过 WASM 插件机制允许开发者用 Rust 编写任意转换，同时保持了核心性能。
- **综合能力全面**：SWC 不仅提供转译，还内置了代码压缩和模块打包功能，而 Babel 需要额外配合工具（如 Webpack、Rollup）才能完成这些工作。
- **活跃的社区支持**：项目拥有 Discord 社区、GitHub 超 3.3 万星标，且 npm 包月下载量超过千万，生态快速发展。
- **持续优化与迭代**：核心团队持续关注 Web 标准演进，快速支持新的 JavaScript 语法特性，并不断优化 Rust 实现的内存和 CPU 效率。

## 相关链接

- [GitHub 仓库](https://github.com/swc-project/swc)
- [官方网站与文档](https://swc.rs/)
- [npm 包：@swc/core](https://www.npmjs.com/package/@swc/core)
- [Discord 社区](https://discord.com/invite/GnHbXTdZz6)
