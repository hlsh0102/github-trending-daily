---
tags:
  - trending
  - article
repo: google/skills
date: 2026-08-09
language: Python
stars_total: 16802
stars_today: 481
---
## 项目概述

`google/skills` 是 Google 官方发布的一个开源仓库，用于为 Google 产品和技术提供 **Agent Skills**（智能体技能）。Agent Skills 是一种可复用的、面向 AI 智能体的结构化能力模块，使智能体能够更高效地完成特定类型的任务，例如身份认证、云平台入门、解决方案架构设计等。该项目目前处于积极开发阶段，目标是帮助开发者快速为基于大语言模型（LLM）的智能体应用集成 Google Cloud 及其他 Google 技术的最佳实践。

该仓库主要面向两类用户：一是希望在自有 AI 应用中快速接入 Google Cloud 能力的开发者，二是需要标准化智能体工作流、减少重复开发的企业团队。通过 `skills` 模块，用户无需从头编写复杂的云交互逻辑，而是直接复用经过验证的方案。

## 核心功能

- **Google Cloud 认证技能**：提供 `Authenticating to Google Cloud` 技能，帮助智能体安全地处理身份认证流程，支持服务账号、OAuth 等场景。
- **云平台入门引导**：通过 `Onboarding to Google Cloud` 和 `Foundation Builder` 技能，智能体可以引导用户完成项目初始化、资源创建等基础配置。
- **解决方案架构工作流**：提供 `Google Cloud solution-architecture workflow` 技能，使智能体能够基于业务需求自动生成符合最佳实践的云架构方案。
- **多产品集成方案**：包含多个跨产品的综合技能，例如：
  - Agentic analytics（支持跨云厂商和数据类型的智能分析）
  - Borderless data lakehouse（开放性数据湖仓一体化 AI 系统）
  - Build and deploy AI agents（在 Google Cloud 上构建和部署智能体）
- **高级数据与 AI 工作流**：覆盖数据科学工作流、多模态实时流式智能体方案等前沿场景。
- **统一安装管理**：通过 `npx skills add google/skills` 一键选择和安装所需技能模块。

## 技术架构

该项目基于 **Agent Skills 规范** 构建，该规范定义了一种标准化的技能打包、描述和调用方式。每个技能模块通常包含：

- **描述文件**（如 `SKILL.md`）：以 Markdown 格式定义技能的名称、用途、输入输出参数和调用示例。
- **可执行代码**：Python 或 JavaScript 脚本，用于实际执行智能体请求的任务。
- **依赖管理**：技能内部可声明所需库或外部 API，并通过安装命令自动拉取。

设计上，`google/skills` 采用**模块化和组合式设计**：技能之间相互独立，可单独安装，也可组合成完整的工作流。例如，用户可以先安装“认证”技能，再搭配“架构设计”技能，形成一个从身份验证到方案输出的完整链路。这种架构使得智能体开发变得更加灵活，且能够充分利用 Google Cloud 的全栈能力。

此外，仓库遵循 **Apache-2.0** 开源协议，代码质量较高，且与 Google Cloud 官方 SDK 深度集成，确保与谷歌云生态的兼容性和稳定性。

## 安装与使用

### 安装

需要 Node.js 环境（推荐 v18 及以上）。在项目目录下运行：

```bash
npx skills add google/skills
```

执行后，CLI 会列出仓库中可用的技能清单，按提示选择安装即可。所有技能默认安装到本地 `skills` 目录。

### 最小使用示例

以安装“Authenticating to Google Cloud”技能为例：

```bash
npx skills add google/skills
# 在交互菜单中选择 google-cloud-recipe-auth
```

安装完成后，在智能体代码中引用技能：

```python
from skills.google_cloud_recipe_auth import authenticate

# 依照技能定义的接口调用
credentials = authenticate(service_account_path="path/to/key.json")
```

对于中文用户，建议在调用技能时传入明确的参数描述（如 `region="asia-east1"`），以便智能体更准确地执行任务。

## 适用场景

1. **企业云上云迁移与治理**：智能体可借助“Onboarding”和“Foundation Builder”技能，自动完成云端资源规划、权限配置和成本预估，降低上云门槛。
2. **AI 驱动的数据分析**：结合“Agentic analytics”技能，企业可以构建跨数据源（如 BigQuery、Spark）的智能分析助手，提供自然语言查询和自动报表生成。
3. **智能体应用快速开发**：对于需要构建客服、知识库问答等 LLM 应用的团队，可直接复用“Build and deploy AI agents”技能，加速后端服务与工具链的集成。
4. **实时多模态交互**：利用“Live bidirectional multimodal streaming”技能，开发适用于音视频交互场景的智能体，如实时语音助手或视频会议摘要机器人。

## 项目亮点

- **官方维护，可信赖**：由 Google 团队亲自维护，与 Google Cloud 服务同步更新，规避了第三方库兼容性风险。
- **覆盖全栈**：从底层认证到上层解决方案，技能矩阵覆盖云使用全生命周期，且持续扩充。
- **标准化交付**：遵循 Agent Skills 规范，技能可跨平台复用，不锁定特定 LLM 或框架。
- **社区活跃**：仓库 Star 数超过 16k，单日增长数百，反映出开发者社区的高度关注和快速迭代。

## 相关链接

- [GitHub 仓库](https://github.com/google/skills)
- [Agent Skills 官方首页](https://agentskills.io/home)
- [Google Cloud 官方文档](https://cloud.google.com/docs)
