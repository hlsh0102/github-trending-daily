---
tags:
  - trending
  - article
repo: PrefectHQ/prefect
date: 2026-07-13
language: Python
stars_total: 23228
stars_today: 66
---
## 项目概述

Prefect 是一个基于 Python 的工作流编排框架，旨在帮助开发者构建具有弹性的数据管道。无论是简单的 ETL 流程还是复杂的机器学习工作流，Prefect 通过提供声明式的任务定义、自动重试机制、可视化监控面板以及灵活的事件驱动调度，让数据管道的开发、部署和维护变得更加可靠和高效。目标用户包括数据工程师、数据科学家、MLOps 工程师以及任何需要编排异步或批处理任务的开发者。

## 核心功能

- **声明式工作流定义**：使用 Python 装饰器（如 `@flow` 和 `@task`）来定义任务与流程，代码即工作流定义，无需额外的 YAML 或 DSL 文件。
- **自动重试与错误处理**：为每个任务配置重试策略、超时时间以及状态回调，当任务失败时可自动重试或触发降级逻辑，大幅提升管道韧性。
- **内置调度器与事件驱动**：支持 Cron 表达式定时触发，同时可通过 Webhook 或外部事件来动态启动工作流，实现全自动编排。
- **实时监控与 UI 仪表盘**：提供 Web UI 查看所有流程的运行历史、任务状态、日志输出和运行耗时，便于定位瓶颈与排查故障。
- **灵活的执行后端**：支持本地进程、线程池、Dask 分布式集群或 Kubernetes 作为任务执行环境，可根据工作负载弹性扩展。
- **状态与结果持久化**：自动将每个任务的状态、返回值和元数据存储到数据库或云存储中，支持断点续跑与审计追溯。

## 技术架构

Prefect 采用“客户端-服务器”模型设计。核心组件包括：

- **Prefect Client**：用户编写的 Python 脚本通过 SDK 注册工作流，并负责执行任务逻辑。
- **Prefect Server**：一个基于 FastAPI 构建的后端服务，提供 REST API 接口来管理流程、存储运行记录、管理状态机。
- **Prefect UI**：基于 React 构建的 Web 用户界面，用于可视化监控和分析。
- **任务引擎**：支持多种执行器（Executor），如 `SequentialExecutor`、`ThreadPoolExecutor`、`DaskExecutor` 等，用户可根据工作负载选择同步或并发执行。
- **存储与状态管理**：利用 SQL 数据库（如 PostgreSQL）持久化所有运行数据，并通过事件订阅机制（Webhooks/Subscriptions）实现实时通知。

架构设计上强调“可观察性”和“弹性”：每个任务运行时都会上报其状态（Pending、Running、Success、Failed 等），Server 端持续跟踪并允许用户通过 API 或 UI 实时查询。同时，Prefect 内置了“重试-退避”策略，避免大量失败请求冲击下游系统。

## 安装与使用

安装 Prefect 非常简单，只需执行 pip 命令即可：

```bash
pip install prefect
```

之后，你可以启动 Prefect 的本地服务器与 UI（用于开发和测试）：

```bash
prefect server start
```

下面是一个最小可用的示例，展示如何定义一个简单的流程并执行它：

```python
from prefect import flow, task

@task
def greet(name: str) -> str:
    return f"Hello, {name}!"

@flow
def hello_flow(name: str = "World"):
    result = greet(name)
    print(result)

if __name__ == "__main__":
    hello_flow()
```

运行该脚本后，你可以在 Prefect UI（通常位于 `http://localhost:4200`）中看到这次运行记录。如需调度此流程每天运行，可以添加装饰器参数：

```python
@flow(cron="0 8 * * *")
def scheduled_hello_flow(name="World"):
    ...
```

对于更复杂的分布式场景，你可以配置执行器改为 Dask 或 Kubernetes：

```python
@flow(executor="dask")
def distributed_flow():
    ...
```

## 适用场景

1. **数据 ETL/ELT 管道**：定时从多个源（数据库、API、文件存储）提取数据，进行清洗转换后加载到目标仓库。Prefect 的重试和状态跟踪可确保数据不丢失、不重复。
2. **机器学习训练与部署工作流**：将数据预处理、特征工程、模型训练、评估、部署和监控串联成一个自动化流程，支持按条件分支（例如模型准确率低于阈值时触发 retrain）。
3. **微服务编排与事件响应**：当 Kafka 消息、Webhook 或数据库变更事件到达时，触发一系列业务逻辑处理，例如用户注册后自动发送欢迎邮件、更新 CRM 并记录审计日志。
4. **批处理与夜间任务**：对大量文件进行批量处理、生成日报表、数据归档或清理任务，借助调度器实现全自动无人值守运行。

## 项目亮点

- **纯 Python 原生体验**：相比 Airflow 需要使用 DAG 文件定义任务依赖，Prefect 的装饰器设计允许开发者在任何 Python 脚本中内嵌工作流，降低了学习门槛。
- **断路器与自适应重试**：当连续失败次数达到阈值时，Prefect 会自动暂停重试（断路器模式），避免无效资源消耗，待系统恢复后自动恢复执行。
- **强大的动态工作流支持**：可以在运行时动态生成任务、根据数据量调整并行度，非常适合数据量不确定的场景（如每天处理不同数量的文件）。
- **开源核心 + 云托管可选**：Prefect 的核心功能完全开源（Apache 2.0），同时提供 Prefect Cloud 托管服务提供团队协作、高级监控和零运维节点，灵活满足不同规模团队的需求。

## 相关链接

- [GitHub 仓库](https://github.com/PrefectHQ/prefect)
- [官方文档](https://docs.prefect.io/)
- [社区 Slack](https://prefect.io/slack)
- [YouTube 频道](https://www.youtube.com/c/PrefectIO/)
