---
tags:
  - trending
  - article
repo: agent-substrate/substrate
date: 2026-08-21
language: Go
stars_total: 1426
stars_today: 22
---
## 项目概述

Agent Substrate 是一个面向大规模智能体（Agent）部署的高性能运行时环境。该项目由 Google 工程师发起并维护，但并非 Google 官方支持产品。它解决的核心问题是：在真实业务场景中，大量智能体应用（如 AI Agent、自动化任务等）绝大多数时间处于空闲状态，直接为每个 Agent 分配独立计算资源会导致巨大的基础设施浪费。Agent Substrate 通过将大量「Actor」（即应用实例，例如 Agent）映射到少量准备好的「Worker」上，利用 Agent 类应用的空闲特性实现高密度复用，从而大幅降低运行成本。

该项目定位为低约束（low-opinion）系统：它不限定工作负载必须是 AI Agent，只要符合「长时间空闲、按需唤醒」特征的应用都可以运行在其上。同时，它也不是一个用于构建 Agent 的 SDK，而是一个用于在规模上运行 Agent 的基础设施层。目标用户包括需要部署大量 Agent 服务的平台工程师、后端开发者以及运维团队。

## 核心功能

- **完整的生命周期管理**：支持 Actor 的创建、销毁、挂起（suspend）和恢复（resume）操作，所有操作均通过统一的控制平面接口暴露。
- **亚秒级挂起/恢复**：针对 Agent 场景优化的快速启停能力，实测恢复时间可控制在数百毫秒级别，使 Agent 可以按需唤醒。
- **高密度资源复用**：支持在同一组计算基础设施上复用大量 Actor，显著提升机器利用率，降低单 Agent 运行成本。
- **多沙箱技术适配**：内置对 microVM 和 gVisor 等多种沙箱技术的支持，不同沙箱类型之间保持一致的运行与管理语义。
- **实时 Actor–Worker 调度**：根据当前负载和策略动态将 Actor 分配到合适的 Worker 上，并在运行过程中按需迁移。
- **流量路由**：将外部请求准确路由到对应的 Actor 实例，支持 Actor 被挂起时自动唤醒，保证服务可用性。

## 技术架构

Agent Substrate 的架构遵循控制平面与数据平面分离的设计原则。控制平面负责全局状态管理、调度决策和生命周期操作的协调；数据平面由一个或多个运行 Agent 的实际计算节点构成，节点上部署 Worker 进程，每个 Worker 可以承载多个 Actor 沙箱。

核心调度逻辑建立在「Actor 空闲假设」之上：系统假定大多数 Actor 在绝大多数时间内处于空闲状态，因此实际活跃的并发请求数远小于 Actor 总数，从而实现高密度复用。当请求到达时，调度器选择已挂起的 Actor 并通过快速的 sandbox 恢复流程将其唤醒，处理请求后再次挂起，整个过程对调用方透明。

在沙箱隔离方面，Agent Substrate 抽象了统一的沙箱接口，上层调用不感知底层实现细节。microVM 方案提供更完整的硬件虚拟化隔离，gVisor 方案则以轻量用户态内核换取更快的启动速度。两种方案共享相同的生命周期状态机，使得调度策略无需针对具体隔离机制分别编写。

项目采用 Go 语言开发，充分利用其高并发、低内存占用以及良好的系统编程支持。通信层基于 gRPC 构建，支持多节点间的状态同步与控制指令下发。

## 安装与使用

Agent Substrate 采用 Go 模块化管理，可直接通过标准 `go get` 方式获取源码构建。假设您已安装 Go 1.21 或更高版本：

```bash
git clone https://github.com/agent-substrate/substrate.git
cd substrate
make build
```

构建完成后，将在 `bin/` 目录下生成控制平面和节点组件的二进制文件。启动一个基础环境涉及两步：先启动控制平面，再在计算节点上注册 Worker。

以下为一个最小启动示例：

```bash
# 启动控制平面（默认监听 50051 端口）
./bin/substrate-controller --listen :50051 &

# 在本地启动一个 worker 并注册到控制平面
./bin/substrate-worker --controller localhost:50051 --sandbox gvisor &
```

随后可以通过控制平面暴露的 gRPC API 创建 Actor、挂起/恢复以及路由流量。具体 API 定义可参考仓库中的 `proto/` 目录。完整的配置说明和部署建议请参阅 [docs](https://github.com/agent-substrate/substrate/blob/main/docs)。

## 适用场景

- **大规模 AI Agent 服务**：部署成千上万个 LLM Agent，各 Agent 持有独立的上下文和会话状态，但只在用户交互时被唤醒，其余时间保持挂起状态。
- **定时任务与事件驱动工作负载**：适合那些以分钟、小时为周期触发一次，其余时间完全空闲的应用，如报表生成、数据同步、监控巡检等。
- **多租户 SaaS 平台**：为每个租户提供独立的运行沙箱实例，隔离租户之间数据与计算资源，同时通过复用降低总体基础设施成本。
- **测试环境批量管理**：在 CI/CD 流程中按需创建大量隔离测试环境，测试完成后迅速销毁，避免了常驻环境的资源浪费。

## 项目亮点

Agent Substrate 的差异化优势主要体现在三个维度：**性能**上，亚秒级的挂起/恢复操作使得按需唤醒策略成为现实，无需长期占有资源；**密度**上，通过在单台物理机或虚拟机内复用大量空闲 Actor，可以将基础设施成本降低一个数量级以上；**通用性**上，与特定 Agent 框架解耦，任何「空闲为主、突发为次」的应用都能在其上获得收益，并且对底层沙箱技术的透明抽象使得用户可以自由选择安全等级与性能的平衡点。

## 相关链接

- [GitHub 仓库](https://github.com/agent-substrate/substrate)
- [项目说明文档](https://github.com/agent-substrate/substrate/tree/main/docs)
