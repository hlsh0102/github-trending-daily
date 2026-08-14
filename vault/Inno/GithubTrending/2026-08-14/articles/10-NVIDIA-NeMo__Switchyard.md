---
tags:
  - trending
  - article
repo: NVIDIA-NeMo/Switchyard
date: 2026-08-14
language: Rust
stars_total: 1272
stars_today: 408
---
## 项目概述

Switchyard 是一个用 Rust 编写的 LLM 流量代理与路由库，旨在解决大语言模型应用在多模型、多提供商环境下的互联互通问题。它能够在 OpenAI 和 Anthropic 的 API 协议之间进行转换，同时支持将流量路由到 vLLM、NVIDIA NIM、Ollama 等任意 OpenAI 兼容端点。通过 Switchyard，开发者可以将原本绑定在特定 API 协议上的应用（如 Claude Code、Codex CLI）无缝指向开源模型或其他提供商的模型，而无需修改应用本身。

该项目目前处于 pre-alpha 阶段，API 和路由算法仍在快速迭代中，官方明确警告不适合生产环境使用。对于追求灵活模型选择、A/B 对比测试和成本优化的开发者而言，Switchyard 提供了一个极具潜力的基础设施层。

## 核心功能

- **协议转换**：在 OpenAI Chat、Anthropic Messages 和 OpenAI Responses 三种主流 API 格式之间自由转换，使基于任一协议开发的客户端能够透明地使用其他协议的模型服务。
- **多后端路由**：内置随机路由、LLM 作为分类器的智能路由、基于信号的分阶段路由等多种路由策略，同时支持开发者实现自定义路由算法。
- **运营监控**：集成 Prometheus 指标，覆盖请求量、错误率、延迟、Token 消耗以及路由开销等关键运营数据，为模型调优和成本控制提供数据支撑。
- **自定义算法扩展**：支持编写类型化、可组合的路由逻辑，允许用户根据业务需求定制流量分配策略。

## 技术架构

Switchyard 采用 Rust 作为主要开发语言，利用其内存安全和高性能特性构建网络代理层。其最核心的设计思路是将“协议解析/序列化”与“路由决策”解耦：上层应用发送的请求先被解析为内部统一的中间表示，再经过路由算法决定转发目标，最后序列化为目标提供商期望的协议格式发送出去。

这一架构带来了几个关键优势。首先，协议转换是双向且可组合的，不仅支持 OpenAI 到 Anthropic 的单向转换，还支持反向转换，意味着同一个代理可以服务不同协议偏好的客户端。其次，路由算法作为一个独立的抽象层，可以通过类型系统确保不同策略之间的组合安全性和可预测性。此外，因为整个代理是独立的可执行文件，它可以作为本地或远程服务部署，同时也可以作为库嵌入到更大的 Rust 应用中。

## 安装与使用

Switchyard 的安装和使用分为两个路径：**启动器路径（Launcher Mode）** 和 **服务器路径（Server Mode）**。

**启动器路径**适用于直接运行 Claude Code、Codex CLI 或 OpenClaw 等现有工具。基本流程如下：

1. 构建或下载 Switchyard 二进制文件。
2. 配置代理，指定需要转换的协议类型和后端模型端点。
3. 启动 Switchyard 作为本地代理，并将工具的 API 端点指向 Switchyard 监听的地址。
4. 工具发送请求后，Switchyard 负责转换协议并转发到目标模型。

例如，要将 Claude Code（原本使用 Anthropic API）指向一个 OpenAI 兼容的本地模型服务：

```bash
# 假设 Switchyard 监听在 localhost:8080
switchyard serve --openai-backend http://localhost:8000/v1 \
                 --listen 127.0.0.1:8080 \
                 --translate anthropic-to-openai

# 然后将 ANTHROPIC_BASE_URL 环境变量设置为 http://127.0.0.1:8080
export ANTHROPIC_BASE_URL=http://127.0.0.1:8080
claude
```

**服务器路径**则适合构建自定义应用，将 Switchyard 作为 Rust 库引入，在代码中创建路由算法并启动代理服务。

## 适用场景

- **模型迁移与替换**：当企业希望将应用从闭源模型（如 Claude）切换到开源模型（如 Llama 3）时，无需改动应用代码，仅通过 Switchyard 的协议转换即可平滑过渡。
- **多模型 A/B 测试**：在相同应用负载下，将流量按比例分配给不同模型，通过 Prometheus 指标对比各模型的响应质量、延迟和成本。
- **成本优化**：根据请求复杂度或用户等级动态路由到不同价位模型，例如简单任务走便宜的小模型，复杂推理走高性能大模型。
- **本地开发与测试**：开发者可以直接将依赖云 API 的工具链指向本地运行的模型（如 Ollama），加快迭代速度并避免不必要的 API 费用。

## 项目亮点

Switchyard 最显著的特点是**协议无关性**与**路由能力**的深度结合。目前市面上大部分工具仅支持单一协议转换或简单的负载均衡，而 Switchyard 同时支持 OpenAI Chat、Anthropic Messages 和 OpenAI Responses 三种格式的双向转换，并提供了丰富的路由算法组合。这使它成为连接闭源与开源模型生态的桥梁。

此外，项目使用 Rust 实现，在性能和内存安全上有天然优势。它不仅是成熟的独立代理，也可以作为库嵌入到其他 Rust 项目中，为构建复杂 LLM 应用提供了底层基础设施。项目虽处于早期阶段，但社区活跃度较高（发布当日即获得超过 400 星标），也反映出用户对这种能力的强烈需求。

## 相关链接

- [GitHub 仓库](https://github.com/NVIDIA-NeMo/Switchyard)
