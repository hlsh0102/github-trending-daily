---
tags:
  - trending
  - article
repo: cordiverse/cordis
date: 2026-08-18
language: TypeScript
stars_total: 5689
stars_today: 957
---
## 项目概述

Cordis 是一个面向时空组合性的元框架（Meta-Framework），旨在解决现代分布式系统中日益复杂的时空协调问题。它由 cordiverse 组织开发，采用 TypeScript 编写，并遵循 MIT 开源协议。

在传统编程模型中，时间和空间维度通常被割裂处理——时间上的调度（如定时任务）与空间上的部署（如微服务拓扑）往往由不同的工具和范式管理。Cordis 提出了一种全新的编程范式，将时间和空间作为一等公民统一建模，使开发者能够更自然、更高效地构建具有时空约束的分布式应用。项目当前处于活跃开发阶段，API 尚未稳定，适合对前沿编程范式感兴趣的开发者、研究者和早期采用者。

## 核心功能

- **统一时空抽象**：Cordis 提供统一的抽象层来描述事件的时间属性（如顺序、并发、时序关系）和空间属性（如位置、拓扑、路由），避免使用不同机制拼凑解决方案。

- **声明式组合语法**：通过声明式语法定义组件之间的时空关系，框架自动处理底层调度、通信和同步逻辑，显著降低心智负担。

- **可插拔运行时**：支持多种后端运行环境（如 Node.js、边缘计算节点），开发者可以编写一次逻辑，在不同时空基础设施上运行，无需修改业务代码。

- **时空感知的调度引擎**：内置智能调度引擎，能够根据时间和空间约束自动排序、分配和迁移任务，优化资源利用率与响应延迟。

- **形式化验证支持**：基于项目论文提出的数学基础，提供工具链对关键时空逻辑进行静态检查和形式化验证，增强系统可靠性。

- **OpenTelemetry 集成**：原生支持 OpenTelemetry 标准，方便对跨时空调用链进行分布式追踪和性能监控。

## 技术架构

Cordis 的核心设计围绕“时空组合子”（Spatiotemporal Combinators）展开，这是一种参考函数式编程中组合子思想的新型抽象。它将时间轴与空间拓扑编码为代数结构，通过组合子之间的运算关系推导出复杂系统的行为。

架构上分为三层：**核心层**（Core）实现了时空原语和组合子逻辑，不依赖任何运行时；**适配层**（Adapter）负责将抽象映射到具体运行时（如 Node.js 的事件循环、Web Worker 的隔离环境）；**工具层**（Tooling）提供开发者工具，包括类型推导、可视化调试和验证工具。

TypeScript 的类型系统在项目中扮演关键角色。Cordis 利用高阶类型和条件类型，在编译期对时空关系的合法性进行大量检查，让许多潜在错误在编码阶段即被暴露。项目的论文《A Programming Paradigm for Spatiotemporal Composability》详细阐述了其理论依据，为关注形式化方法的读者提供了深入的阅读材料。

## 安装与使用

由于项目仍在快速迭代中，建议使用包管理工具直接从 GitHub 安装最新开发版本：

```bash
npm install cordiverse/cordis
# 或
yarn add cordiverse/cordis
```

以下是一个最小示例，演示如何定义一个简单的时空组合：在两个位置之间按顺序执行两个事件。

```typescript
import { cordis, at, after } from '@cordis/core';

// 定义两个位置
const nodeA = { id: 'a', region: 'cn-east' };
const nodeB = { id: 'b', region: 'cn-west' };

// 在 A 执行任务，等待 100ms 后在 B 执行任务
const workflow = cordis(
  after(100, at(nodeA, () => console.log('Task A done'))),
  at(nodeB, () => console.log('Task B done'))
);

// 运行工作流
workflow.run().then(() => console.log('All tasks completed'));
```

更完整的入门教程可以参考官方文档 [cordis-primer](https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer)。

## 适用场景

- **边缘计算编排**：在多个边缘节点之间协调任务，要求考虑节点位置、网络延迟和本地时间差异，Cordis 可以自然建模链路延迟与执行顺序。

- **分布式事件驱动系统**：对于需要严格保证跨服务事件顺序（如金融交易、日志流水）的系统，Cordis 的时序原语提供了比传统消息队列更精细的控制。

- **物联网与机器人协调**：多个设备在物理空间中协同工作，需要同时处理移动轨迹（空间）与同步时序（时间），Cordis 为这类问题提供了统一的表达方式。

- **科学工作流调度**：在分布式计算集群上运行多阶段科学实验，各阶段间存在数据处理时间和地点依赖性，Cordis 可简化依赖编排。

## 项目亮点

Cordis 的差异化优势主要体现在三个层面。首先，**开创性的理论框架**——它是首个将时空组合性作为第一原则的编程模型，背后有完整学术论文支撑，而非工程上的临时拼凑。其次，**类型安全**——利用 TypeScript 的编译期检查捕获时空逻辑错误，这在现有分布式框架中极为少见。最后，**轻量而优雅**——核心库体积极小、无侵入，可以渐进式集成到现有项目中，与其他框架共存。

## 相关链接

- [GitHub 仓库](https://github.com/cordiverse/cordis)
- [学术论文：A Programming Paradigm for Spatiotemporal Composability](https://github.com/cordiverse/paper)
- [文档：cordis-primer](https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer)
