---
tags:
  - trending
  - article
repo: anthropics/skills
date: 2026-09-05
language: Python
stars_total: 174242
stars_today: 511
---
## 项目概述

anthropics/skills 是 Anthropic 官方发布的公开仓库，用于承载 Claude 的 Agent Skills 实现。Agent Skills 是一种以文件夹为单位的轻量级扩展机制，将指令、脚本和资源打包在一起，使 Claude 能够按需加载，从而在特定任务上获得更专业的表现。该仓库不仅提供了技能系统本身的参考实现，还收录了大量由 Anthropic 团队开发的高质量技能示例，覆盖创意设计、技术开发、企业运营等多个领域。

对于任何希望在 Claude 生态中构建可复用工作流的开发者、企业团队或是个人用户，这个仓库都是一个重要的起点。它既帮助用户理解技能系统的工作原理，也为自定义技能的开发提供了从规范到实践的全套参考。

## 核心功能

- **技能即文件夹**：每个技能都被设计为一个自包含的目录，核心是一个 `SKILL.md` 文件，其中包含技能的名称、描述、使用说明和必要的元数据，使 Claude 能够理解何时以及如何调用该技能。

- **丰富的官方技能示例**：仓库内置了多个开箱即用的技能，例如创意写作、图像生成、音乐编排、Web 应用测试、MCP 服务器生成，以及面向企业场景的品牌沟通和合规文档生成等，用户可以直接导入使用。

- **按需动态加载**：与固定上下文不同，技能由 Claude 根据当前任务需求自动判断并加载，不影响默认交互的轻量性和响应速度。

- **开放协同**：这是一个公开仓库，接收来自社区的贡献，用户可以浏览、借鉴乃至提交自己的技能实现，推动 Agent Skills 生态的发展。

- **版本化与可移植性**：每个技能内容均可追溯、可复刻，便于团队在统一标准下管理和分发内部技能资产。

- **与 Claude 产品深度集成**：所有技能均遵循 Anthropic 官方规范，能够无缝应用于 Claude 桌面端、移动端和 API 环境中。

## 技术架构

Agent Skills 的核心设计理念是"轻量、按需、可扩展"。在实现上，每个技能是一个标准化的文件夹，内部至少包含一个 `SKILL.md` 文件。该文件使用 Markdown 格式进行书写，头部嵌入 YAML frontmatter，用于声明技能的名称（name）和描述（description）。描述部分被设计为语义化的触发条件——当 Claude 判断当前用户请求与该描述匹配时，就会自动读取该技能文件，并将其中的指令注入到上下文中。

这种架构与传统的工具调用或 API 集成有明显区别。技能不需要预先注册到模型中，也不依赖外部服务，而是一种随取随用的"上下文附加包"。为了帮助 Claude 在合适的时机选用正确的技能，仓库中提供了关于技能描述撰写的最佳实践指南。此外，技能文件夹中除了 `SKILL.md`，还可以包含脚本代码、提示词模板、参考文档及其他静态资源，这些文件通过相对路径被主文件引用。

在官方实现中，技能被设计为不依赖特定的编程语言或框架，标准本身与运行时无关。仓库中的代码示例以 Python 为主，但在技能内部使用什么语言编写脚本，完全取决于任务本身的需求，这极大地降低了技能开发的门槛。

## 安装与使用

要使用该仓库中的技能，通常有以下两种路径：

**1. 在 Claude 产品中直接使用**

确保你使用的是支持 Agent Skills 的 Claude 版本，然后从仓库中下载你感兴趣的技能文件夹，放置在 Claude 应用指定的技能目录下（具体路径请参阅官方文档中的"使用技能"指南）。此后，当你在对话中提出相关任务需求时，Claude 会自动检测并加载对应技能。

**2. 在 API 或自定义 Agent 中集成**

```python
# 以 Anthropic API 为例，简化展示如何将技能用于自定义 Agent
import anthropic

client = anthropic.Anthropic()

# 假设技能内容已读取为字符串
with open("path_to_skill/SKILL.md", "r") as f:
    skill_content = f.read()

response = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=4096,
    system=[
        {
            "type": "text",
            "text": skill_content
        }
    ],
    messages=[
        {"role": "user", "content": "请根据公司品牌规范撰写一封客户回信。"}
    ]
)

print(response.content[0].text)
```

在上述示例中，关键步骤是将技能文件中的指令内容注入到系统提示词中。在实际开发中，你可以先通过代码判断任务类型，再选择性地注入对应技能。

**创建自定义技能时**，你只需新建一个文件夹，编写 `SKILL.md` 文件，填入名称和描述，并准备好所需的脚本与资源即可。仓库内的技能示例是最好的学习模板。

## 适用场景

- **企业内部知识沉淀**：将公司品牌规范、文案风格要求、合规审查标准等包装为技能，让 Claude 在撰写对外材料时自动遵循企业标准，减少人工校对成本。

- **研发效率提升**：例如将 Web 应用测试流程、MCP 服务器生成规范、代码风格检查等变为技能，使 Claude 在软件开发生命周期的各个阶段提供更为专业的辅助。

- **个人自动化工作流**：将邮件草拟、日程总结、报告生成等重复性任务定义成技能，让 Claude 以一个"专属助手"的方式完成日常高频操作。

- **教育与研究**：利用公开技能作为教学案例，向开发者展示如何设计一套以模型为中心的高效指令系统。

## 项目亮点

- **官方权威性**：作为 Anthropic 的官方仓库，它直接反映了 Agent Skills 的最新标准与最佳实践，消除了社区猜测和碎片化实现的困扰。

- **低姿态扩展**：相比微调模型或构建复杂插件系统，技能系统仅需自然语言指令加少量配套文件，即可实现能力拓展，学习曲线平缓。

- **高度可组合**：在复杂任务中，多个技能可以依据上下文分别触发，协同完成一条完整的工作流，而不必事先设计为一个庞然大物。

- **社区与生态双驱动**：仓库开放的贡献模式加上超过 17 万星标的关注度，使其成为 Agent 能力扩展领域中最具活力的公共资源之一。

- **真实可用而非演示性质**：仓库中展示的技能致力于贴近实际业务，反映了 Anthropic 在将大模型应用于真实工程与企业环境中的方法论。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/skills)
- [Agent Skills 标准信息](http://agentskills.io)
- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Claude 中使用技能](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [创建自定义技能指南](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Anthropic 工程博客：用 Agent Skills 装备智能体](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
