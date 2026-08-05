---
tags:
  - trending
  - article
repo: microsoft/generative-ai-for-beginners
date: 2026-08-05
language: Jupyter Notebook
stars_total: 116387
stars_today: 783
---
## 项目概述

[Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) 是微软开源的一套面向初学者的生成式人工智能学习课程，由 21 节独立课程组成，旨在帮助完全没有或仅有少量 AI 基础的学习者快速上手构建生成式 AI 应用。项目以 Jupyter Notebook 为主要载体，结合理论讲解与动手实践，覆盖从大语言模型（LLM）基础概念到实际应用开发的完整路径。目标用户包括希望转型 AI 领域的软件开发者、产品经理、数据爱好者以及任何对生成式 AI 感兴趣并希望通过动手实践来学习的个人。该项目采用 MIT 许可证，完全免费，且支持多种语言（包括简体中文、繁体中文、阿拉伯语等），是目前 GitHub 上最受欢迎的学习型 AI 仓库之一，拥有超过 11.6 万颗 Star。

## 核心功能

- **21 节结构化课程**：按主题分为六个部分，涵盖生成式 AI 与 LLM 入门、提示工程基础、文本生成应用、聊天应用、图像生成应用以及低代码 AI 工具（如 Copilot 和 Azure OpenAI）。
- **理论与动手相结合**：每节课都包含清晰的概念讲解、代码示例以及可运行的 Jupyter Notebook 实验，学习者可以在本地或云端直接运行代码，加深理解。
- **多语言支持**：通过 GitHub Action 自动维护翻译，提供包括简体中文、繁体中文、日文、韩文、法文等在内的多种语言版本，降低了非英语学习者的门槛。
- **配套教学资源**：每节课都附有知识检查（quiz）和作业（assignment），方便自学者检验学习效果，也适合教育者作为课程素材使用。
- **技术栈丰富**：课程中使用了 OpenAI API、Azure OpenAI Service、Hugging Face Transformers、LangChain、Semantic Kernel 等当前主流的 AI 开发框架和工具。
- **社区驱动**：项目鼓励学习者通过 GitHub Issues 和 Discussions 提问、交流，并有官方 Discord 社区供全球学习者互动。

## 技术架构

项目的技术架构以“课程内容 + 交互式笔记本”为核心。所有课程内容以 Markdown 编写，并嵌入 Python 代码示例，主要运行在 Jupyter Notebook 环境中。课程设计遵循“由浅入深、螺旋上升”的原则：首先介绍提示工程和上下文学习，然后过渡到使用 LangChain 构建文本生成与聊天应用，接着探讨图像生成模型的原理与调用方式，最后介绍低代码/无代码开发工具。

从技术栈来看，项目紧密结合微软 Azure 生态，尤其是 Azure OpenAI Service，同时也完全兼容 OpenAI 官方 API，确保学习者可以自由切换。课程代码采用模块化设计，每个 Notebook 独立可运行，减少依赖冲突。此外，项目使用 GitHub Actions 实现多语言 README 的自动翻译和同步，保证了文档的实时更新。对于希望深入底层原理的学习者，课程中还包含了 Transformer 架构、注意力机制、向量数据库、RAG（检索增强生成）模式等高级主题的介绍，帮助建立完整的技术图谱。

## 安装与使用

要使用本课程，建议先准备 Python 3.8+ 环境，并安装 Jupyter Notebook 或 Visual Studio Code（配合 Python 扩展）。推荐使用 Anaconda 或 venv 创建独立环境，并安装课程所需的依赖包，例如：

```bash
pip install openai langchain python-dotenv
```

安装完成后，克隆仓库并在本地启动 Notebook：

```bash
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners
jupyter notebook
```

接下来，需要准备 API 密钥。课程中的示例主要使用 OpenAI API 或 Azure OpenAI Service。在项目根目录创建一个 `.env` 文件，填入你的密钥：

```
OPENAI_API_KEY=your_openai_api_key
```

或者对于 Azure OpenAI：

```
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_KEY=your_key
```

然后选择你感兴趣的课程，打开对应的 Notebook，依次运行代码单元格即可。每一课的开头都会有学习目标和前置知识说明，建议按照顺序学习，以获得最佳效果。

## 适用场景

- **个人开发者自学**：如果你是一名软件工程师，希望系统性地学习生成式 AI 开发，本课程提供了从零到一的完整路径，涵盖提示工程、API 调用、应用构建等核心技能。
- **高校与企业培训**：教师或培训师可以直接使用本课程的章节和练习题设计教学计划，配合课程中的知识检查来评估学员掌握程度。
- **产品经理与技术决策者**：对于需要了解生成式 AI 能力边界、评估技术选型的非工程人员，课程中的理论与案例部分提供了很好的背景知识，尤其是关于低代码工具的章节。
- **技术社区活动与黑客松**：课程中的实战练习非常适合作为黑客松的参考资料，参与者可以基于其中的聊天应用或图像生成模板快速构建原型。

## 项目亮点

与市面上其他生成式 AI 学习资源相比，本项目有几个显著的差异化优势：

- **系统性与全面性兼具**：大多数在线教程只聚焦单一框架或单一功能，而本项目用 21 个课时构建了完整的学习路径，覆盖从基础概念到高级模式（如 RAG）的方方面面。
- **官方背书与持续维护**：由微软官方维护，资料质量高，且随着技术演进持续更新，保证了内容的时效性。项目还提供了官方的翻译自动化流程，确保非英语用户也能获得最新内容。
- **实践导向，低门槛**：每节课都有可立即运行的代码，并且提供了详细的错误排查和配置指引，极大降低了初学者的上手难度。
- **与 Azure 生态深度集成**：尽管也兼容 OpenAI API，但课程对 Azure OpenAI Service 的使用讲解深入，对于计划在企业级环境中部署 AI 应用的开发者尤具价值。
- **活跃的社区生态**：依托 GitHub 庞大的开发者社区和 Discord 专属频道，学习者可以获得即时帮助，同时也能看到大量由社区衍生的实践案例。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/generative-ai-for-beginners)
- [简体中文翻译版](https://github.com/microsoft/generative-ai-for-beginners/blob/main/translations/zh-CN/README.md)
- [Discord 社区](https://discord.gg/nTYy5BXMWG)
