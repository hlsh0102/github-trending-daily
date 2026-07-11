---
tags:
  - trending
  - article
repo: microsoft/TypeScript
date: 2026-07-11
language: TypeScript
stars_total: 109807
stars_today: 177
---
## 项目概述

TypeScript 是由微软开发并维护的开源编程语言，它是 JavaScript 的一个超集，主要目标是为大规模 JavaScript 应用程序提供更好的开发体验。TypeScript 在保留 JavaScript 全部特性的基础上，加入了可选的静态类型系统，使得开发者能够在编码阶段就发现潜在错误，并借助强大的工具链提升代码的可维护性和可读性。编译后的 TypeScript 代码会生成纯净、可读的标准 JavaScript，可以在任何浏览器、任何主机、任何操作系统上运行。该项目适用于从个人开发者到大型企业团队的广泛用户群体，尤其适合需要长期维护、多人协作或代码规模较大的项目。

## 核心功能

- **静态类型检查**：TypeScript 允许为变量、函数参数、返回值等添加类型注解，在编译阶段即可捕获类型不匹配、空引用等常见错误。
- **类型推断**：即使不显式标注类型，TypeScript 也能根据上下文自动推断变量和表达式的类型，兼顾安全性与开发效率。
- **现代 JavaScript 特性支持**：支持 ES6+ 的语法，如箭头函数、解构赋值、异步/等待等，并能将其编译为指定版本的 JavaScript，确保兼容性。
- **丰富的类型工具**：提供接口、泛型、联合类型、交叉类型、条件类型等高级类型机制，能够精确建模复杂的数据结构和业务逻辑。
- **与 JavaScript 无缝集成**：TypeScript 是 JavaScript 的超集，任何合法的 JavaScript 代码都是合法的 TypeScript 代码，可逐步迁移现有项目。
- **强大的开发工具链**：内置语言服务，支持代码补全、导航、重构、错误提示等功能，在 VS Code 等主流编辑器中体验极佳。

## 技术架构

TypeScript 编译器采用分层架构设计，主要由以下几个部分组成：

- **扫描器/解析器**：将源代码转换为抽象语法树（AST），并执行初步的语法检查。
- **类型检查器**：核心组件，负责解析类型注解、进行类型推断和类型兼容性检查，是所有类型安全性的基础。
- **转换器**：将 TypeScript 特有的语法（如类型注解、枚举、装饰器等）抹除，生成纯净的 JavaScript AST。
- **发射器**：根据目标 ECMAScript 版本（如 ES5、ES6 等）、模块系统（CommonJS、ES Modules）等配置，输出最终的 JavaScript 代码。

类型检查与代码生成是分离的，这意味着即使代码中存在类型错误，TypeScript 默认仍会生成 JavaScript，开发者可以选择在各种严格级别之间平衡安全性与灵活性。编译器本身使用 TypeScript 编写，实现了自托管，这种设计有助于在开发过程中体验自身的类型系统。

## 安装与使用

安装 TypeScript 最常用的方式是通过 npm（Node.js 包管理器）。建议作为开发依赖安装到项目中：

```bash
npm install -D typescript
```

如需使用最新的夜间构建版本，可以执行：

```bash
npm install -D typescript@next
```

安装完成后，可以使用 `npx tsc` 命令编译 TypeScript 文件。创建一个简单的示例：

1. 新建一个 `greeter.ts` 文件，内容如下：

```typescript
function greeter(person: string) {
    return "Hello, " + person;
}

let user = "World";
console.log(greeter(user));
```

2. 在终端中运行编译命令：

```bash
npx tsc greeter.ts
```

3. 编译后会在同一目录下生成 `greeter.js` 文件，内容为：

```javascript
function greeter(person) {
    return "Hello, " + person;
}
var user = "World";
console.log(greeter(user));
```

对于项目级别的配置，运行 `npx tsc --init` 可以生成 `tsconfig.json` 配置文件，在其中设置编译选项、包含/排除的文件路径等。

## 适用场景

- **大型企业级 Web 应用**：当项目代码规模达到数万行甚至更多，多人协作频繁时，TypeScript 的类型系统能够显著减少运行时错误，提高代码的可维护性和可理解性。
- **库和框架开发**：为开源库或内部工具包添加类型定义，可以让使用者获得准确的代码提示和类型检查，提升开发体验。许多知名库如 React、Vue、Angular 等都提供了 TypeScript 类型支持。
- **团队协作项目**：类型注解作为代码的“活文档”，能够清晰表达接口契约和数据流，减少沟通成本，帮助新成员快速上手。
- **逐步迁移旧项目**：对于已有的 JavaScript 项目，TypeScript 允许逐步引入类型，可以将 `.js` 文件逐个或分模块地重命名为 `.ts`，并逐渐添加类型注解，降低迁移风险。

## 项目亮点

- **标准化与生态融合**：TypeScript 由微软主导开发，但始终保持与 ECMAScript 标准的同步演进，而非另起炉灶。它广泛支持流行的模块系统、框架和工具链，拥有繁荣的社区生态（DefinitelyTyped 库提供了数千个第三方库的类型定义）。
- **渐进式采用**：不同于一些要求全盘重写的语言，TypeScript 允许项目从零开始使用，也支持在现有 JavaScript 项目中逐步迁移。开发者可以按需开启严格模式，逐步提升安全级别。
- **强大的工具链**：基于语言服务的编辑器体验（如 VS Code、WebStorm）是 TypeScript 的核心优势之一。实时错误反馈、智能代码补全、重构功能等极大地提升了开发效率。
- **活跃的维护与演进**：项目保持频繁的更新节奏，每年发布多个大版本，不断引入新特性（如装饰器的标准化、模板字面量类型、Isolated Declarations 等），同时致力于提高编译速度和降低内存占用。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/TypeScript)
- [官方网站及 Playground](https://www.typescriptlang.org/)
- [官方博客](https://blogs.msdn.microsoft.com/typescript)
- [TypeScript 社区](https://www.typescriptlang.org/community/)
