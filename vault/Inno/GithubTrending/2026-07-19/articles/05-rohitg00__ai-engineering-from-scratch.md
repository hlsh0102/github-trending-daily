---
tags:
  - trending
  - article
repo: rohitg00/ai-engineering-from-scratch
date: 2026-07-19
language: Python
stars_total: 39203
stars_today: 191
---
## 项目概述

AI Engineering from Scratch 是一份面向 AI 工程师的完整学习路线图与实践指南，由 Agent Memory（#1 持久记忆库）作者 rohitg00 创建。该项目旨在帮助学习者从零开始系统掌握 AI 工程的核心技能，包括模型训练、部署、推理优化、工具链构建等，最终能够独立构建并交付面向他人的 AI 产品。

项目包含 503 节课程、20 个阶段，覆盖从基础理论到生产级工程实现的完整路径。无论你是刚入门 AI 的开发者，还是希望补齐工程能力的算法工程师，这个项目都能提供清晰的学习路径和可复现的代码示例。

## 核心功能

- **结构化学习路线**：将 AI 工程知识拆解为 20 个循序渐进的学习阶段，每个阶段包含若干课程和实践练习，帮助你避免学习路径上的迷茫。
- **完整工程示例**：每个概念都配有可运行的 Python 代码示例，覆盖数据预处理、模型训练、推理服务、API 封装等全流程。
- **从理论到部署**：不仅讲解算法原理，更强调工程落地——包括模型优化（量化、剪枝）、推理加速（vLLM、TensorRT）、容器化部署等生产级主题。
- **开放参考手册**：项目同时提供 Web 版本（aiengineeringfromscratch.com），可作为随时查阅的 AI 工程参考手册。
- **社区驱动迭代**：基于 500+ 课程内容持续更新，接受社区贡献和反馈，保持与行业实践同步。
- **与 Agent Memory 生态兼容**：项目中的工具和库设计上保持与 Agent Memory 等持久记忆方案的兼容性，方便构建具有长期记忆能力的 AI 代理。

## 技术架构

项目围绕“学-建-交付”三阶段设计，技术栈主要基于 Python 生态：

- **核心语言与框架**：以 Python 为主要实现语言，覆盖 PyTorch、Hugging Face Transformers、LangChain 等主流框架。
- **学习阶段划分**：每个阶段聚焦一个核心领域，如基础机器学习、深度学习、自然语言处理、强化学习、模型部署、AI 代理等。
- **代码即文档**：所有课程都配有可复现的 Jupyter Notebook 或 Python 脚本，便于动手实践。
- **生产级工具链**：涵盖 Docker、Kubernetes、MLflow、FastAPI 等工业级工具的使用方法。
- **模块化设计**：课程内容按主题独立组织，允许学习者根据自身需求选择性地学习特定阶段。
- **持续集成**：通过 GitHub Actions 维护代码质量和示例的可用性。

## 安装与使用

1. **克隆仓库**

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
```

2. **创建虚拟环境（推荐）**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **启动学习**

打开任意阶段的 Jupyter Notebook 或 Python 脚本开始学习。例如，从第一阶段的基础 ML 开始：

```bash
jupyter notebook phases/phase-01-basics/
```

5. **访问在线版本**

你也可以直接访问 [aiengineeringfromscratch.com](https://aiengineeringfromscratch.com) 阅读完整参考手册。

## 适用场景

- **AI 初学者转型**：从零基础开始，系统学习 AI 工程所必需的数学、编程和框架知识，适合希望成为 AI 工程师的开发者。
- **算法工程师补足工程能力**：已经掌握模型原理但缺乏部署、优化、监控等工程经验的算法人员，可以通过项目中的生产级主题补齐短板。
- **创业团队快速原型**：需要快速构建 AI 产品原型的团队，可以借鉴项目中的完整工程示例和最佳实践。
- **教育机构教学辅助**：作为 AI 工程课程的补充教材，提供标准化的学习路径和实践素材。

## 项目亮点

- **完整性与深度**：500+ 课程覆盖从线性回归到多模态 AI 代理的完整技术栈，是目前 GitHub 上最全面的 AI 工程学习资源之一。
- **实战导向**：每个知识点都配有可直接运行的代码，强调“即学即用”，而非仅停留在理论层面。
- **持续更新**：基于 AI 领域的最新进展（如 RAG、AI 代理、持久记忆）不断补充内容，保持与行业前沿同步。
- **高质量文档**：课程组织清晰，配有图表和实际案例，降低了学习曲线。
- **社区认可度高**：拥有 39k+ GitHub 星标，社区活跃，Issue 和 PR 响应积极。

## 相关链接

- [GitHub 仓库](https://github.com/rohitg00/ai-engineering-from-scratch)
- [官网/参考手册](https://aiengineeringfromscratch.com)
- [Agent Memory 项目](https://github.com/rohitg00/agentmemory)
