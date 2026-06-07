---
tags:
  - trending
  - article
repo: aquasecurity/trivy
date: 2026-06-07
language: Go
stars_total: 36031
stars_today: 159
---
## 项目概述

Trivy 是一款由 Aqua Security 开发的开源全功能安全扫描器，旨在帮助开发者和安全团队快速、全面地发现各类安全风险。该项目解决了容器镜像、文件系统、Git 仓库、虚拟机镜像和 Kubernetes 环境中的已知漏洞、错误配置、敏感信息泄露、软件物料清单（SBOM）生成以及软件许可证合规性问题。目标用户涵盖开发人员、DevOps 工程师、安全工程师以及任何需要将安全扫描集成到 CI/CD 管道中的团队。Trivy 以其易用性、全面的覆盖范围和低误报率而闻名，已成为云原生安全领域最受欢迎的工具之一。

## 核心功能

- **多目标扫描**：支持对容器镜像、本地文件系统、远程 Git 仓库、虚拟机镜像及 Kubernetes 集群进行统一扫描，覆盖应用生命周期的各个环节。
- **综合性检测能力**：内置多个扫描器，可同时检测操作系统级和应用程序级的已知漏洞（CVEs）、基础设施即代码（IaC）错误配置、硬编码密钥与敏感信息，以及软件许可证风险。
- **SBOM 生成**：能够输出软件物料清单（Software Bill of Materials），帮助用户清晰了解所有依赖组件的来源、版本及许可证信息，满足供应链安全需求。
- **广泛的语言与平台支持**：支持大多数主流编程语言（如 Java、Python、Node.js、Go、Ruby、Rust 等）的依赖库分析，并涵盖多个操作系统（如 Alpine、Debian、Ubuntu、CentOS、Red Hat）的漏洞数据库。
- **快速安装与集成**：提供 Homebrew、Docker、二进制文件下载、rpm/deb 包等多种安装方式，并可直接嵌入 GitHub Actions、GitLab CI、Jenkins 等 CI/CD 流水线，实现自动化安全扫描。
- **详细的报告与导出**：扫描结果支持 JSON、SARIF、HTML 等多种格式输出，便于集成到安全仪表板或告警系统中。

## 技术架构

Trivy 使用 Go 语言开发，具有轻量、跨平台和高并发的特性。其核心架构基于一个可扩展的扫描引擎，该引擎将“扫描目标”（如容器镜像层、文件系统路径）与“扫描器”解耦。扫描器各自独立处理漏洞数据库匹配、模式匹配（用于密钥检测）和配置规则评估。漏洞数据依赖于一个持续更新的本地缓存，该缓存从 NVD、RedHat、Debian、Ubuntu 等多个权威源同步。Trivy 支持通过自定义策略（如 Rego 语言编写的规则）扩展 IaC 扫描能力。设计中强调性能优化：通过层缓存、并行处理和增量更新机制，实现秒级扫描能力，尤其适合大规模仓库和 CI 场景。

## 安装与使用

### 安装

Trivy 提供多种安装方式，以下是几个常见示例：

**macOS（使用 Homebrew）**：
```bash
brew install trivy
```

**Docker**：
```bash
docker pull aquasec/trivy:latest
```

**Linux**（通过 RPM 或 DEB 包）：
```bash
# 以 Ubuntu/Debian 为例
sudo apt-get install trivy
```

### 最小可用示例

扫描一个容器镜像的漏洞：
```bash
trivy image nginx:latest
```

扫描当前文件系统目录中的错误配置和密钥：
```bash
trivy fs .
```

扫描远程 Git 仓库的漏洞：
```bash
trivy repo https://github.com/aquasecurity/trivy-ci-test
```

生成 SBOM 并输出为 JSON 格式：
```bash
trivy image --format cyclonedx --output result.json nginx:latest
```

所有扫描器默认同时启用，也可通过 `--scanners` 参数指定（如 `--scanners vuln,secret,config`）进行针对性检测。

## 适用场景

- **CI/CD 流水线集成**：在代码提交或构建阶段自动扫描容器镜像，阻止包含高危漏洞的镜像进入生产环境。
- **基础设施代码审计**：在部署前扫描 Terraform、CloudFormation、Kubernetes YAML 等 IaC 文件，发现错误配置（如开放的 S3 存储桶、非安全的 RBAC 设置）。
- **供应链安全审查**：定期生成并跟踪 SBOM，确保第三方依赖库中没有已知漏洞或被禁止的许可证，满足合规要求。
- **云端与本地环境巡检**：扫描运行中的 Kubernetes 集群或虚拟机镜像，识别已部署应用中的新漏洞和敏感信息泄露。

## 项目亮点

- **一站式扫描**：将漏洞、错误配置、密钥、许可证和 SBOM 生成整合在一个工具中，无需组合多个专有扫描器，降低工具链复杂度和维护成本。
- **极高的易用性**：默认零配置即可进行全功能扫描，命令行接口直观，输出结果清晰易懂，新手也能快速上手。
- **主动更新与社区活跃**：漏洞数据库每日多次更新，GitHub 星数超过 3.6 万，拥有活跃的贡献者社区和丰富的文档资源，问题响应及时。
- **低误报与高准确率**：针对每种编程语言和操作系统精心定制了扫描规则，并通过大量实际测试减少误报，减轻了人工审核负担。
- **企业级兼容性**：支持多种输出格式，可与主流 SIEM、告警平台及安全仪表板集成，同时支持自定义策略和忽略项，灵活满足企业安全策略需求。

## 相关链接

- [GitHub 仓库](https://github.com/aquasecurity/trivy)
- [Trivy 官方文档](https://aquasecurity.github.io/trivy/v0.46/)
- [Trivy 首页](https://trivy.dev/)
- [安装指南](https://aquasecurity.github.io/trivy/v0.46/getting-started/installation/)
