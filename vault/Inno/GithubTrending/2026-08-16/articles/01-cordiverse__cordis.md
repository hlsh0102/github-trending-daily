---
tags:
  - trending
  - article
repo: cordiverse/cordis
date: 2026-08-16
language: TypeScript
stars_total: 4129
stars_today: 599
---
## 项目概述

Cordis 是一个面向时空组合性（Spatiotemporal Composability）的元框架（Meta-Framework），由 cordiverse 组织开发，使用 TypeScript 编写。它旨在解决分布式系统和复杂应用中，组件在时间和空间两个维度上的组合与编排难题。

传统的软件框架往往将时间和空间视为正交的维度，难以统一建模。例如，在微服务架构中，服务间的调用关系是空间上的拓扑结构，而异步事件、定时任务则引入了时间维度。Cordis 提出了一种新的编程范式，将时间和空间统一抽象，使得开发者能够以声明式的方式描述组件在何时、何地以及如何组合协作，从而构建出高内聚、低耦合、易于推理的复杂系统。

该项目目前处于积极开发阶段，API 尚未稳定，适合技术探索者和对前沿编程范式感兴趣的开发者。其核心思想源自学术论文《A Programming Paradigm for Spatiotemporal Composability》，并提供了配套的入门文档。

## 核心功能

- **统一的时空抽象**：提供一种统一的抽象模型，将时间维度（如事件触发、生命周期、调度）和空间维度（如服务发现、路由、分布式拓扑）统一建模，消除二者之间的割裂。
- **声明式组合编排**：开发者通过声明式配置或描述性代码，定义组件在特定时间和空间条件下的组合关系，而非编写命令式的胶水代码。
- **可组合性优先**：框架设计以组合性为第一原则，确保各个模块、服务或组件可以像积木一样灵活拼装，而无需修改内部实现。
- **类型安全的开发体验**：基于 TypeScript 构建，提供完善的类型推断和编译时检查，在开发阶段即可捕获大量因时空配置错误导致的问题。
- **元框架特性**：不局限于某一具体领域（如 Web 后端或数据处理），而是提供一种通用的范式，可以作为上层框架或特定领域框架的底层基础。
- **活跃的社区与前沿研究支撑**：背靠公开的学术论文，拥有清晰的理论基础，项目在 GitHub 上获得了 4000+ Star，社区关注度高。

## 技术架构

Cordis 的核心技术架构围绕“元框架”这一概念展开。它并不直接是一个 Web 框架或任务队列，而是一种描述组件间时空关系的“语言”和“运行环境”。

其底层核心可能包含以下几个关键设计：

1. **统一的时空类型系统**：定义了描述时间（如 `instant`、`interval`、`schedule`）和空间（如 `location`、`scope`、`region`）的基本类型和运算规则，为静态分析和类型安全提供基础。
2. **组合算子与运行时**：提供一系列组合子（Combinator），例如“顺序执行”、“并行执行”、“条件触发”、“基于位置的动态绑定”等。运行时负责解析这些组合关系，并调度底层资源（如事件循环、消息队列、网络 RPC）来执行。
3. **依赖注入与服务网格**：借助 TypeScript 的装饰器或元数据反射机制，实现依赖的自动管理和注入。在空间维度上，它可能内置或对接服务发现机制，使得组件可以动态地定位和连接彼此。
4. **基于图的执行引擎**：将应用抽象为一个有向无环图（DAG），节点是组件，边是时空依赖关系。执行引擎负责拓扑排序、并发控制以及时间约束的验证。

这种架构的显著特点是“逻辑与物理分离”。开发者专注于描述“该做什么”和“何时何地做”，而 Cordis 则负责决定“怎么做”和“在哪里的资源上做”，从而极大提升了系统的可移植性和可伸缩性。

## 安装与使用

由于项目处于早期阶段且 API 可能变化，使用前请务必查阅最新的官方文档。

**安装步骤（基于 npm 或 yarn）：**

1. 确保你的环境已安装 Node.js（>= 16）和 TypeScript（>= 4.5）。
2. 在你的项目中安装核心依赖：

```bash
npm install @cordis/core
# 或者使用 yarn
yarn add @cordis/core
```

**最小可用示例（伪代码/概念演示）：**

以下代码展示了如何声明一个简单的时空组合，其中 `fetchData` 和 `processData` 两个组件在时间上顺序执行，在空间上位于同一作用域。

```typescript
import { defineComponent, time, space } from '@cordis/core';

// 定义两个独立的、可组合的组件
const fetchData = defineComponent(async (ctx) => {
  const data = await ctx.http.get('/api/data');
  return data;
});

const processData = defineComponent(async (ctx, data: any) => {
  return transform(data);
});

// 在元框架中声明组合关系
const pipeline = space.scope('worker-node', () => {
  return time.sequence([
    fetchData,
    processData
  ]);
});

// 运行
pipeline.run().then(console.log);
```

**注意**：上述代码仅为展示 Cordis 核心思路的简化示例，并非真实可运行的 API。请务必参考 `cordis-primer` 文档获取最新的 API 用法。

## 适用场景

- **复杂分布式系统开发**：当系统需要跨越多个服务、多个地域，且涉及复杂的异步流程和事件驱动架构时，Cordis 的时空抽象可以显著降低系统的认知负担和协调复杂度。
- **实时数据处理流水线**：构建需要严格时序（如窗口聚合、事件时间处理）和数据分片路由（如地理位置路由）的流处理或批处理任务，可借助 Cordis 高效编排数据处理节点。
- **物联网与边缘计算**：在物联网场景中，设备和计算资源分布在不同的物理空间，且数据产生具有很强的时序性。Cordis 可以帮助定义设备数据的采集、上传、协同处理的时空策略。
- **科研与教学实验**：作为一篇学术论文的实践项目，Cordis 非常适合作为研究分布式系统理论、编程语言设计和软件架构的实验平台，用于验证新的架构理念。

## 项目亮点

- **理论先行，实践落地**：不同于多数仅从实践出发的框架，Cordis 拥有严谨的学术理论支撑，思路清晰，避免了盲目堆砌功能。
- **真正的时空统一**：多数框架要么仅关注时间（如响应式编程），要么仅关注空间（如服务网格），Cordis 首次在“元框架”层面将两者深度融合。
- **高度灵活的组合性**：其“元框架”的定位意味着它不绑定具体业务，可以嵌入到现有技术栈中，或作为新一代基础架构的基石，具有极高的战略价值。
- **前沿且社区关注度高**：在未正式发布稳定版的情况下获得了大量 Star，证明社区对这一创新范式的浓厚兴趣和期待。

## 相关链接

- [GitHub 仓库](https://github.com/cordiverse/cordis)
- [学术论文《A Programming Paradigm for Spatiotemporal Composability》](https://github.com/cordiverse/paper)
- [入门文档（cordis-primer）](https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer)
