---
tags:
  - trending
  - article
repo: google/skills
date: 2026-08-10
language: Python
stars_total: 17321
stars_today: 528
---
## 项目概述

google/skills 是一个由 Google 官方维护的开源仓库，专门为 Google 产品和技术提供 **Agent Skills**（代理技能）。Agent Skills 是一种可复用的能力模块，能够赋予 AI 代理（Agent）执行特定任务的知识和工具集。该仓库旨在解决开发者在构建 AI 代理时面临的“技能碎片化”问题——以往开发者需要为每个代理单独编写与 Google Cloud 交互的代码，而 Skills 将这些交互封装为标准化的、可插拔的模块，大幅降低了开发门槛。项目主要面向 AI 应用开发者、云架构师以及数据科学团队，帮助他们快速构建能够与 Google Cloud 服务无缝协作的智能代理。目前仓库处于积极开发阶段，Star 数已超过 1.7 万，社区关注度极高。

## 核心功能

- **标准化技能安装**：通过 `npx skills add google/skills` 命令，开发者可以交互式选择并安装所需技能，无需手动复制代码或处理依赖关系。
- **Google Cloud 认证封装**：提供开箱即用的认证技能，支持多种 Google Cloud 身份验证方式，简化代理访问云资源的安全配置流程。
- **云基础架构引导**：包含“Foundation Builder”和“Onboarding”技能，帮助代理理解并操作云资源目录、IAM 权限等基础架构元素。
- **多产品解决方案技能**：覆盖从数据科学工作流到实时多模态流媒体的完整解决方案，例如将 Spark、Knowledge Catalog 等大数据组件封装为代理可调用的技能。
- **架构设计工作流**：提供“Solution Architecture”技能，使代理能够遵循 Google Cloud 最佳实践进行架构方案设计。
- **跨云数据分析**：支持代理在 AWS、Azure、GCP 等多云环境中执行分析任务，突破单一云平台的限制。

## 技术架构

该仓库采用 **“技能即代码”** 的设计理念，每个技能都是一个独立的、遵循统一接口规范的模块。核心架构特点包括：

1. **声明式接口**：每个技能通过元数据文件（如 `SKILL.md`）描述其功能、输入参数和调用方式，使代理能够动态发现和理解技能用途。
2. **模块化设计**：技能之间相互独立，按产品领域（Cloud、AI、Data）分类存放，并通过命名约定（`recipe-`、`solution-`）区分基础操作和完整解决方案。
3. **Python 原生实现**：底层使用 Python 编写，与主流的 AI 代理框架（如 LangChain、CrewAI）天然兼容，同时通过 `npx` 命令提供 JavaScript/TypeScript 生态的接入入口。
4. **版本化管理**：依托 Git 仓库作为分发渠道，每次安装都会拉取特定版本的技能，保证环境可复现性。
5. **可组合性**：技能可以被链式调用，例如“认证 → 数据查询 → 架构建议”是常见的组合模式，系统设计时已考虑上下文传递。

## 安装与使用

### 环境要求
- Node.js 16+（用于 `npx` 命令）
- Python 3.9+
- 一个活跃的 AI 代理运行时（如 Claude、Gemini 或开源 LLM 框架）
- Google Cloud 账号（用于访问云服务）

### 安装步骤

```bash
# 1. 在项目目录中初始化技能
npx skills add google/skills

# 2. 根据提示选择需要安装的技能（例如：google-cloud-recipe-auth）
# 3. 技能文件将被复制到 ./skills/ 目录

# 4. 在代理配置中声明技能引用
# 在代理的配置文件（如 agent.yaml）中添加：
# skills:
#   - path: ./skills/google-cloud-recipe-auth
```

### 最小使用示例

以“认证技能”为例，在 Python 代理中调用：

```python
from skills.google_cloud_recipe_auth import authenticate

# 自动获取当前环境凭据
credentials = authenticate()

# 使用凭据调用 Google Cloud API
from google.cloud import storage
client = storage.Client(credentials=credentials)
buckets = list(client.list_buckets())
```

对于需要完整工作流的场景，可以直接调用“解决方案技能”：

```bash
# 安装解决方案技能
npx skills add google/skills --select google-cloud-solution-agentic-analytics-spark-knowledge-catalog

# 随后代理即可通过自然语言指令驱动数据分析流水线
```

## 适用场景

1. **企业级 AI 助手开发**：为内部知识管理或客服系统构建能查询 BigQuery、操作 Cloud Storage 的智能助手。
2. **云资源自动化运维**：通过代理自动执行云环境巡检、成本分析、配置优化等运维任务。
3. **数据科学流程加速**：将数据采集、清洗、建模、部署的完整流程封装为代理技能，支持非专家用户进行数据分析。
4. **多云架构研究**：利用跨云分析技能，在统一代理框架下对比不同云厂商的服务性能与成本。

## 项目亮点

- **官方背书与质量保障**：由 Google 团队维护，技能与 Google Cloud 最新 API 保持同步，避免了社区项目普遍存在的版本滞后问题。
- **低代码接入体验**：相比从零编写云服务调用代码，安装技能可将开发周期从数天压缩至数小时，且无需深入理解底层云 API 细节。
- **全栈解决方案覆盖**：不局限于单一 API 封装，而是提供了从认证、基础运维到复杂架构设计的完整技能生态。
- **开放的贡献机制**：采用 Apache 2.0 协议，允许企业定制私有技能，同时官方鼓励社区提交新技能，形成良性生态循环。
- **跨框架兼容性**：通过标准化 Skill 描述格式，兼容当前主流的代理框架（包括自主开发的和开源的），降低了锁定风险。

## 相关链接

- [GitHub 仓库](https://github.com/google/skills)
- [官方技能目录](https://skills.sh/google/skills)
- [Agent Skills 标准文档](https://agentskills.io/home)
