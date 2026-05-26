---
tags:
  - trending
  - article
repo: rohitg00/ai-engineering-from-scratch
date: 2026-05-26
language: Python
stars_total: 19356
stars_today: 3154
---
## 项目概述

AI Engineering from Scratch 是一套面向 AI 工程师的完整自学课程体系，包含 435 节课程、20 个阶段，总学习时长约 320 小时。该项目旨在解决当前 AI 教育中的核心矛盾：84% 的学生已经使用 AI 工具，但仅 18% 感到有能力在专业环境中正确使用它们。

项目覆盖 Python、TypeScript、Rust、Julia 四种编程语言，内容从基础概念延伸到生产级工程实践。与大多数只讲解理论或只展示 demo 的课程不同，这套课程的一个核心理念是：每一节课都必须交付一个可复用的制品——可能是一个提示词、一个技能、一个智能体，或一个 MCP 服务器。你不仅学习 AI，你亲手构建它，端到端，从头做起。

该项目完全免费、开源，采用 MIT 许可协议，允许任意商业使用和二次分发。

## 核心功能

- **系统化课程规划**：435 节课被组织为 20 个递进阶段，从基础知识到前沿技术，覆盖 AI 工程的全链路。
- **多语言实践**：课程同时使用 Python、TypeScript、Rust 和 Julia，帮助学习者掌握不同生态下的 AI 工程最佳实践。
- **可复用制品输出**：每节课都交付一个可直接使用的产物，包括提示词库、可复用的功能模块、智能体壳或完整的 MCP 服务。
- **生产级工程视角**：内容的组织方式强调工程落地，而非单纯的学术推导，包含部署、测试、监控和迭代方法。
- **社区驱动发展**：项目拥有详细的路线图（ROADMAP.md），社区可以通过 issue 和 PR 参与内容改进和扩展。
- **配套官方网站**：项目不仅托管在 GitHub，还拥有独立站点 aiengineeringfromscratch.com，提供更有结构化的阅读体验。

## 技术架构

项目以“从零构建”为设计哲学，内容结构围绕四个维度展开：

**基础层（阶段 1–5）**：首先构建对机器学习、神经网络核心概念的理解，采用 Python 和 Jupyter Notebook 作为主要教学工具。学习者会手动实现简单的感知机、前馈网络和反向传播算法，而非直接调用库函数。

**框架层（阶段 6–10）**：引入主流 AI 框架和工具链，包括 PyTorch、LangChain、Hugging Face Transformers 等。此阶段开始引入 TypeScript，用于构建与大语言模型交互的前端应用。

**工程层（阶段 11–15）**：转向生产环境关注的服务化部署、API 设计、模型序列化与分发。Rust 在此阶段登场，用于构建低延迟的推理服务和工具链。

**前沿层（阶段 16–20）**：涵盖多模态模型、强化学习微调、MCP 协议实现、智能体内核开发。Julia 被用于高性能计算和实验性场景。

项目的本质不是一个框架或库，而是一套结构化的知识图谱，每个知识点都通过实际编码转化为可运行的代码。仓库使用 modular structure 组织，每个阶段的目录下包含课程说明（Lesson.md）、代码实现（code/）、以及可运行的测试和示例（examples/）。

## 安装与使用

1. **克隆仓库**

   ```bash
   git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
   cd ai-engineering-from-scratch
   ```

2. **阅读指南**

   从仓库根目录的 README.md 或访问 [官网](https://aiengineeringfromscratch.com/) 了解课程整体结构和推荐学习顺序。

3. **选择阶段**

   根据你的当前水平选择起始阶段。建议初学者从阶段 1 开始；有经验的工程师可以直接跳转到阶段 11 之后的工程实践章节。

4. **运行代码示例**

   每个阶段的 code/ 目录下通常包含 requirements.txt 或 pyproject.toml。安装依赖后按课程说明逐步运行代码：

   ```bash
   cd phase-01/lessons/01-perceptron/code/
   pip install -r requirements.txt
   python perceptron.py
   ```

5. **提交你的制品**

   每节课的交付物可以存入你自己的分支或派生仓库。项目鼓励 fork 后进行个性化扩展。

## 适用场景

- **自学 AI 工程的系统路径**：适合希望从零开始、有步骤地掌握 AI 工程全流程的个人学习者。课程结构清晰，可自定进度。
- **企业内部培训素材**：公司的 AI 团队或新员工 onboarding 可以直接使用该课程作为参考手册或实验场地，节省从头设计培训材料的时间。
- **高校辅助教材**：计算机科学、数据科学或人工智能方向的课程可以使用这套内容作为课外实践或项目制学习的补充材料。
- **AI 工具开发者参考**：希望了解 MCP 服务器、智能体框架、多模态模型部署等前沿技术的工程师，可以直接参考项目中相关章节的完整实现。

## 项目亮点

与其他 AI 学习资源相比，该项目具有以下差异化优势：

- **完整覆盖而非碎片化**：大部分开源课程只覆盖一个方面（如仅 Prompt Engineering 或仅 Fine-tuning），本项目试图提供一条完整的、从理论到生产的工程路径。
- **每课必出成果**：大多数课堂只讲知识，但这门课要求每一节都交付一个可独立运行的“零件”。这极大地提升了学习者的成就感和知识转化率。
- **多语言实战**：同时使用四种语言不是噱头，而是基于工程实际：Python 用于快速原型，TypeScript 用于 Web 交互，Rust 用于高性能服务，Julia 用于科学计算。学习者在完成课程后将具备跨语言工程能力。
- **社区活跃与持续更新**：项目已获得超过 1.9 万星标（并保持每日数千的增长），显示社区认可其价值。路线图和 issue 区保持活跃，内容不断扩充。
- **极低门槛，超高回报**：完全免费、MIT 许可，无需任何付费或授权。任何人都可以从任何地方开始学习。

## 相关链接

- [GitHub 仓库](https://github.com/rohitg00/ai-engineering-from-scratch)
- [官方网站](https://aiengineeringfromscratch.com/)
- [项目路线图](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/ROADMAP.md)
