---
tags:
  - trending
  - article
repo: coder/coder
date: 2026-09-20
language: Go
stars_total: 15729
stars_today: 402
---
## 项目概述

Coder 是一个可自托管的云开发环境（Cloud Development Environment，CDE）与 AI 编码代理平台。它试图解决的问题是：开发者本地机器的算力、配置和环境一致性长期受限，同时企业又需要对这些开发环境进行统一的权限、网络与合规管控。Coder 将这些开发环境从开发者的笔记本迁移到企业自有的基础设施上，用代码（Terraform）定义工作区，并通过安全隧道供开发者访问。

目标用户主要包括三类：需要为工程团队统一提供开发环境的基础设施或平台团队；对代码和密钥有合规要求、不能使用公有云托管开发环境的企业；以及希望在自己掌控的算力上运行 AI 编码代理的团队。项目采用 Go 编写，以 AGPL-3.0 许可证开源，目前在 GitHub 上拥有约 1.5 万颗星。

## 核心功能

- **基于 Terraform 的工作区定义**：每个工作区（Workspace）由 Terraform 模板描述，可运行在 AWS、GCP、Azure、Kubernetes 或裸金属等任意目标上，基础设施即代码的方式让环境可复现、可版本化。
- **安全隧道连接**：工作区通过 WireGuard® 隧道与控制平面连接，无需对外暴露入站端口，开发者可从任意位置安全访问。
- **自动关停闲置环境**：当工作区一段时间未被使用时自动关闭，降低云资源成本。
- **原生 AI 编码代理**：Coder Agents 在控制平面（部署于用户自有基础设施）中执行代理循环，避免将代码或凭据发送给第三方 API。
- **集中化的访问与权限管理**：提供统一的身份认证、角色与访问控制，便于企业对开发环境进行治理和审计。
- **多编辑器与工具集成**：支持 VS Code、JetBrains 等主流 IDE，以及浏览器内访问方式。

## 技术架构

Coder 的控制平面使用 Go 语言实现，采用典型的服务端 + 代理（Agent）架构。控制平面负责用户认证、工作区编排、模板管理和 API 服务；每个工作区内运行一个轻量代理进程，负责与主控建立隧道并上报状态。

关键设计点包括：

1. **Terraform 作为编排层**。Coder 本身不直接管理虚拟机或容器，而是生成 Terraform 配置并调用 Terraform 来创建工作区资源。这种设计让平台不绑定特定云厂商，也允许团队复用现有的 Terraform 模块和基础设施规范。
2. **WireGuard® 隧道**。控制平面与工作区代理之间通过加密隧道通信，避免开放公网入站端口，减少攻击面。
3. **控制平面承载 AI 代理循环**。与传统 IDE 插件式 AI 助手不同，Coder Agents 的执行循环运行在控制平面上，代码和上下文保留在自有基础设施内。

## 安装与使用

Coder 提供单二进制部署方式，可在 Linux 主机或 Kubernetes 集群中运行。

基本安装步骤大致如下：

1. 下载对应平台的发布包或使用官方安装脚本。
2. 启动 `coder server`，指定访问地址与数据库（默认使用内嵌 PostgreSQL）。
3. 首次启动时创建管理员账号。
4. 安装模板：通过 `coder templates init` 获取官方模板，或编写自定义 Terraform 模板后执行 `coder templates push`。
5. 开发者通过 `coder login` 登录后，使用 `coder create` 创建自己的工作区，并通过 CLI 或 Web UI 连接。

最小可用示例（概念性）：

```bash
# 启动服务端
coder server --postgres-url <url>

# 推送一个模板
coder templates init
coder templates push my-template

# 创建并连接工作区
coder create my-workspace --template my-template
coder ssh my-workspace
```

生产部署通常配合反向代理、TLS 证书和外部 PostgreSQL。具体参数以官方文档为准，不同版本可能存在差异。

## 适用场景

- **企业统一开发环境治理**：为整个工程团队提供标准化的开发环境，集中管理权限、网络策略和成本。
- **合规敏感型组织**：源代码和模型调用不能离开自有基础设施，需要 AI 编码代理在内网内运行。
- **弹性算力需求**：本地机器无法满足编译、训练或大规模测试的需求，需要按需申请高配工作区。
- **远程与外包协作**：向外部协作者提供受控的临时开发环境，任务结束即回收。

## 项目亮点

与 GitHub Codespaces、Gitpod 等托管型方案相比，Coder 的核心差异在于**自托管与基础设施无关**：控制平面和数据都留在用户自己的环境中，工作区可落在任意云或本地集群。与仅做容器化开发的工具相比，Coder 以 Terraform 为编排层，能够管理虚拟机、GPU 节点等更广泛的计算形态。

此外，将 AI 编码代理的执行循环放在控制平面、而非依赖第三方 API，是该项目在当前阶段的显著特征，适合对代码外流敏感的场景。自动关停与模板化定义也有助于控制长期运行带来的资源开销。

## 相关链接

- [GitHub 仓库](https://github.com/coder/coder)
- [官方网站](https://coder.com)
- [官方文档](https://coder.com/docs)
- [定价与版本对比](https://coder.com/pricing#compare-plans)
- [Go 包文档](https://pkg.go.dev/github.com/coder/coder)
