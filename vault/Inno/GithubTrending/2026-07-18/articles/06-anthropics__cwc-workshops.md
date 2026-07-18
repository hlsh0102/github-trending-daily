---
tags:
  - trending
  - article
repo: anthropics/cwc-workshops
date: 2026-07-18
language: TypeScript
stars_total: 1619
stars_today: 45
---
## 项目概述

`cwc-workshops` 是 Anthropic 官方出品的 **Code with Claude** 系列工作坊材料集合。该项目包含了多个动手实践的 workshop，旨在帮助开发者学习如何有效利用 Claude 进行 AI 辅助编程、构建多智能体系统以及优化模型选择。目标用户是对 Claude API、Agent 开发感兴趣的中高级开发者。

## 核心功能

- **模型选择与评估**：通过名为 `rightmodel` 的工作坊，学习如何使用 Claude Code SKILL 审计 LLM 评估套件，跨模型和推理参数（如扩展思考、effort）进行扫描，找到最佳的质量-价格和质量-时间配置。
- **多智能体系统构建**：在 `agent-decomposition` 中，演示如何将 400 行提示词的单体库存代理分解为 Skill、代码执行和可调用智能体的组合，每个分解步骤都有评估验证。
- **AI 辅助产品工作流**：`how-we-claude-code` 提供了一个三阶段的产品开发演示——从访谈需求到规格说明，生成四种不同方案的原型 HTML，最终构建出可被 AI 自动验证的 Vite + React 应用。
- **托管代理部署**：`ship-your-first-managed-agent` 是一个 Streamlit 构建的故障仪表盘应用，通过实现 `agent.py` 中的 7 个小函数，让 SRE 代理能够在沙箱中搜索 7 万行日志、调用本地工具并定位问题提交。
- **代理对战竞赛**：`agent-battle` 设计了一个 45 分钟的竞赛活动，挑战参与者配置 Claude 代理进行对决。

## 技术架构

项目采用 TypeScript 和 Python 作为主要开发语言，每个 workshop 都是独立的自包含项目。核心设计思路包括：

- **渐进式复杂度**：从基础的模型选择到复杂的多代理系统，逐步引导学习者深入。
- **可验证性**：每个 workshop 都强调使用评估（evals）来验证每个步骤的正确性，确保代码质量。
- **模块化设计**：Skill、MCP（Model Context Protocol）、Callable Agent 等概念被拆解为可复用的模块，便于理解和独立使用。
- **沙箱执行**：Managed Agents 运行在隔离的沙箱环境中，保证安全性的同时提供文件系统访问能力。

## 安装与使用

以 `ship-your-first-managed-agent` 为例的基本使用流程：

1. 克隆仓库并进入对应工作坊目录：
```bash
git clone https://github.com/anthropics/cwc-workshops.git
cd cwc-workshops/ship-your-first-managed-agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt  # 或 npm install
```

3. 配置 Claude API 密钥：
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

4. 启动应用：
```bash
streamlit run app.py
```

5. 按照 workshop 指南，逐步实现 `agent.py` 中的 7 个函数，每个函数调用一次 Claude Managed Agents API，直到代理能够正确搜索日志并定位问题。

对于其他 workshop，通常遵循类似的步骤：进入对应目录，安装依赖，配置 API 密钥，然后按照 README 中的步骤完成练习。

## 适用场景

- **AI 开发培训**：企业内部或在线课程中，用于教学如何高效使用 Claude 进行开发。
- **模型选型决策**：开发团队需要评估不同模型及其参数配置，找到适合特定任务的最佳性价比方案。
- **多代理系统设计**：需要将复杂的单代理任务拆解为多代理协作系统的项目。
- **开发者个人进阶**：希望从简单的提示词工程升级到完整的 Agent 系统构建的独立开发者。

## 项目亮点

- **官方出品**：由 Anthropic 团队维护，内容与最新的 Claude API 功能保持同步，具有权威性。
- **实战导向**：每个 workshop 都基于真实业务场景设计，强调可操作的技能而非理论说教。
- **模块化拆解**：特别是 `agent-decomposition` workshop，提供了一套将提示词工程升级为多代理系统的方法论，对大型项目架构设计极具参考价值。
- **完整的评估体系**：强调“没有评估就没有验证”的理念，帮助开发者建立质量意识。
- **零贡献声明**：明确声明不接受贡献，保证了材料的一致性和维护的确定性，避免版本混乱。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/cwc-workshops)
