---
tags:
  - trending
  - article
repo: microsoft/TypeScript
date: 2026-08-22
language: Go
stars_total: 110395
stars_today: 65
---
## 项目概述

TypeScript 是微软开发并维护的一种开源编程语言，作为 JavaScript 的超集，它通过添加可选的静态类型系统，将 JavaScript 从一门脚本语言提升为适合大规模应用开发的企业级语言。TypeScript 代码经过编译后生成干净、可读、符合标准的 JavaScript 代码，可以在任何浏览器、任何主机、任何操作系统上运行。该项目主要面向需要构建和维护大型复杂 Web 应用的前端团队、全栈开发者、开源库作者以及希望在 JavaScript 工程中获得更强类型保障和工具支持的开发者。

## 核心功能

- **静态类型检查**：支持变量、函数参数、返回值、对象属性等位置的类型标注，在编译阶段捕获常见错误，包括空值引用、拼写错误、类型不匹配等问题。
- **类型推断与高级类型**：在无显式标注时自动推断类型，并提供联合类型、交叉类型、泛型、类型守卫、映射类型、条件类型等丰富的类型工具，支持构建精确且灵活的类型模型。
- **现代 JavaScript 语法编译**：支持最新的 ECMAScript 提案语法（如可选链、空值合并、装饰器、类字段等），并可将代码编译至指定目标版本（如 ES5、ES2015、ES2020 等），兼容不同运行环境。
- **结构化类型系统**：采用结构化类型（即鸭子类型）而非名义类型，允许两个具有相同形状的对象互相赋值，这与 JavaScript 的原生行为自然契合，降低了迁移成本。
- **丰富的编辑器集成**：为 Visual Studio Code 等主流编辑器提供一流的语言服务，包括自动补全、代码导航、重构、快速修复、类型悬停提示等功能。
- **声明文件（.d.ts）**：允许为现有 JavaScript 库编写类型声明，使第三方代码也能获得类型检查和编辑器智能感知，支持类型生态的扩充与共享。

## 技术架构

TypeScript 本身由 TypeScript 语言编写，编译器后端编译为 JavaScript 执行。其核心架构包含以下关键部分：

- **编译器管线**：第一步是扫描器（Scanner）将源码拆分为 Token 流；解析器（Parser）根据语法规则构建抽象语法树（AST）；绑定器（Binder）关联符号声明与引用，建立符号表；检查器（Checker）基于类型信息对 AST 进行语义分析和类型验证；最终发射器（Emitter）将验证通过的 AST 生成 JavaScript 代码、声明文件和 source map。
- **语言服务层**：在编译器内核之上，TypeScript 提供语言服务平台，为编辑器提供增量编译、语义诊断、智能补全、签名帮助、快速修复等能力，实现即时响应式开发体验。
- **模块系统**：完整支持 ES Modules、CommonJS、AMD、UMD 等模块格式，并允许通过 `moduleResolution` 配置模块解析策略。
- **配置驱动**：通过 `tsconfig.json` 文件统一管理编译选项，支持项目引用、增量编译（`--incremental`）、构建模式（`--build`）等，支持大型代码库的工程化构建与缓存。
- **设计原则**：TypeScript 严格遵循 JavaScript 语义，力求不改变现有 JS 代码运行时行为，仅在编译期增加类型约束。所有类型信息在编译后被擦除，不产生额外运行时开销。

## 安装与使用

**安装最新稳定版**：

```bash
npm install -D typescript
```

**安装 nightly 构建**：

```bash
npm install -D typescript@next
```

安装完成后，可以通过命令行调用编译器，或创建 `tsconfig.json` 配置文件管理项目。

**最小使用示例**：

1. 创建一个名为 `greeter.ts` 的文件：

```typescript
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const user = "World";
console.log(greet(user));
```

2. 在终端编译：

```bash
npx tsc greeter.ts
```

3. 运行生成的 `greeter.js`：

```bash
node greeter.js
```

**项目化配置**（推荐）：

```bash
npx tsc --init
```

该命令会在当前目录生成 `tsconfig.json`，之后只需运行 `npx tsc` 即可按照配置编译整个项目。

## 适用场景

- **大型前端应用开发**：当项目规模增长到数百个模块、数十位开发者协作时，静态类型系统能够显著降低重构风险、提升代码可维护性，并帮助新成员更快理解代码结构。
- **Node.js 后端服务**：TypeScript 可无缝应用于服务端开发，借助类型定义对数据库查询结果、API 响应、配置对象等进行约束，减少运行时错误。
- **开源库与工具链开发**：库作者使用 TypeScript 编写源码，可同时产出高品质的类型声明文件，为用户提供开箱即用的类型体验，提升库的工程质量与使用体验。
- **大型团队协作与代码迁移**：对于从 JavaScript 逐步迁移至有类型约束体系的项目，TypeScript 允许渐进式引入类型标注，并能与现有 JS 代码共存，降低迁移风险。

## 项目亮点

- **与 JavaScript 原生兼容**：TypeScript 的语法是 JavaScript 的超集，现有的 JS 代码无需修改即可作为 TypeScript 文件使用，迁移过程平滑无感。
- **成熟的企业级采用**：由微软主导开发，拥有稳定的版本发布周期、完善的长期支持策略（LTS）和庞大的社区生态。无数知名项目（如 Angular、Vue 3、VS Code、Slack 桌面版）使用 TypeScript 构建。
- **强大的类型系统深度**：提供表达力极强的类型工具，能够建模复杂的数据结构和 API 形状，在类型层面实现运行时的部分逻辑验证，这在同类静态类型语言中独具特色。
- **工具链完备且性能优秀**：编译器性能经过持续优化，支持 `tsc --watch` 和 `--build` 增量模式；语言服务在大型代码库中表现流畅。配合 Prettier、ESLint 等工具，拥有完整的代码质量保障体系。
- **活跃的社区与文档**：官方文档详实易懂，提供交互式 Playground 和设计理念说明；StackOverflow 上有大量高质量问答，社区贡献活跃，版本迭代中持续吸收社区反馈。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/TypeScript)
- [官方网站](https://www.typescriptlang.org/)
- [在线 Playground](https://www.typescriptlang.org/play/)
- [官方博客](https://devblogs.microsoft.com/typescript/)
- [社区页面](https://www.typescriptlang.org/community/)
