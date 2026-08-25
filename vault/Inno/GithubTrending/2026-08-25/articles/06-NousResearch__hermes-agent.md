---
tags:
  - trending
  - article
repo: NousResearch/hermes-agent
date: 2026-08-25
language: Python
stars_total: 235886
stars_today: 896
---
## 项目概述

Hermes Agent 是由 Nous Research 开发的一款开源自进化 AI 智能体。项目的核心理念是“与你一同成长”——它不只是一个固定的工具，而是一个具备内置学习循环的智能体，能够在与用户的交互过程中不断创建新技能、优化自身能力。与传统 AI 助手不同，Hermes Agent 能够在运行时自主地生成和整合新的技能模块，从而逐步扩展自身的功能边界。

该项目主要面向开发者、研究人员以及需要高度定制化 AI 助手的进阶用户。无论你是希望快速搭建个人 AI 工作流，还是想要研究智能体自进化机制，Hermes Agent 都提供了一个灵活且强大的基础框架。

## 核心功能

- **自进化学习循环**：智能体在执行任务过程中可自主创建新技能，并将其持久化到技能库中供后续复用，形成持续改进的闭环。
- **多模态交互**：支持文本、图像、音频等多种输入形式，能够处理复杂的混合任务。
- **可扩展技能系统**：用户可以通过简单的 API 接口定义和追加自定义技能，系统会自动管理技能的加载与调度。
- **本地优先架构**：支持完全本地部署，保障数据隐私的同时提供离线运行能力。
- **桌面端应用**：提供跨平台桌面图形界面（Hermes Desktop），可用鼠标点击操作而非仅依赖命令行。
- **组合式工作流**：支持将多个技能串联成复杂的工作流，实现端到端的自动化任务处理。

## 技术架构

Hermes Agent 基于 Python 构建，采用了模块化的设计架构。其核心是一个事件驱动的运行时引擎，负责协调技能调度、上下文管理和学习循环的执行。

关键技术组成部分包括：

- **技能注册表**：一个统一的技能存储与索引机制，支持插拔式技能扩展。技能可以是一段 Python 脚本、一个 API 调用模板或一个多步骤过程定义。
- **学习模块**：负责分析当前任务执行过程中暴露出的能力缺口，并利用底层语言模型生成新技能的代码与描述，经验证后写入技能库。
- **上下文管理系统**：维护多轮交互中的状态信息和知识记忆，使智能体在长对话中保持连贯性。
- **运行时沙箱**：为技能执行提供隔离环境，确保自定义代码的安全性，不会影响主程序的稳定性。

整体架构设计强调“轻量核心 + 可插拔扩展”，使得 Hermes Agent 既适合嵌入式部署，也能在云端大规模运行。

## 安装与使用

**安装要求**：Python 3.10 及以上版本，建议使用虚拟环境。

```bash
# 创建并激活虚拟环境（可选但推荐）
python -m venv venv
source venv/bin/activate  # Windows 下使用 venv\Scripts\activate

# 安装 Hermes Agent
pip install hermes-agent
```

**最小可用示例**：

```python
from hermes_agent import Agent

# 初始化智能体
agent = Agent()

# 执行一个简单任务
response = agent.run("列出当前目录下的所有 Python 文件")
print(response)

# 创建并添加一个自定义技能
skill_code = """
def list_py_files(directory='.'):
    import os
    return [f for f in os.listdir(directory) if f.endswith('.py')]
"""
agent.learn_skill("list_py_files", skill_code)

# 使用新技能
agent.run("用 list_py_files 技能查看根目录的 Python 文件")
```

如需使用桌面应用，可访问 [Hermes Desktop](https://hermes-agent.nousresearch.com/) 获取对应平台的安装包，安装后启动应用即可通过图形界面操作。

## 适用场景

1. **个人知识管理与自动化助手**：构建个性化的工作流，例如自动整理邮件、生成会议纪要、管理文件系统，且随着使用时间增加，智能体会针对你的习惯不断优化。

2. **研究实验平台**：用于探索大语言模型的自主学习和技能涌现现象，开发者可以基于其学习循环机制进行二次研究和扩展。

3. **企业内部业务机器人**：根据企业特有的业务流程定制技能，部署于内网环境，处理合同审查、客户问答、数据报表生成等重复性工作。

4. **教育与技术原型开发**：作为学习 AI Agent 架构的参考实现，也可快速搭建面向特定课程或实验室场景的智能助手原型。

## 项目亮点

- **唯一内置学习循环的智能体**：与大多数静态提示工程方案不同，Hermes Agent 能通过代码生成动态扩展自身能力，而非依赖预定义的插件集。
- **真正的本地部署选项**：核心推理和技能执行完全离线可运行，适合对数据安全有严格要求的场景。
- **MIT 开源许可**：宽松的商业使用限制，方便企业集成和二次开发。
- **高活跃度社区**：项目在 GitHub 上拥有超过 23 万 Star，日增近千，拥有活跃的 Discord 社区和多种语言文档，生态支持完善。
- **由 Nous Research 主导**：该团队在开源 LLM 领域有深厚积累，项目后续演变有清晰的技术路线支撑。

## 相关链接

- [GitHub 仓库](https://github.com/NousResearch/hermes-agent)
- [官方文档](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Desktop](https://hermes-agent.nousresearch.com/)
- [Discord 社区](https://discord.gg/NousResearch)
