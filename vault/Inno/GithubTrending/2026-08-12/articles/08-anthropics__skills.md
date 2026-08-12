---
tags:
  - trending
  - article
repo: anthropics/skills
date: 2026-08-12
language: Python
stars_total: 168239
stars_today: 485
---
## 项目概述

anthropics/skills 是 Anthropic 官方维护的公开仓库，集中展示了 Claude 的 Agent Skills 功能。Skills 本质上是包含指令、脚本和资源的文件夹，Claude 会在执行特定任务时动态加载这些内容，从而在专业领域提升表现。无论是按照公司品牌规范创建文档、遵循组织特定工作流分析数据，还是自动化个人任务，Skills 都能让 Claude 以可重复的方式完成这些工作。

该仓库面向所有 Claude 用户，包括开发者、企业团队以及个人爱好者。对于开发者而言，它是学习如何构建自定义 Skills 的最佳参考实现；对于企业用户，仓库中的技能模板可以直接用于梳理内部工作流；对于普通用户，这里提供了大量即插即用的技能，能够显著拓展 Claude 的能力边界。

## 核心功能

- **官方参考实现**：仓库包含 Anthropic 内部对 Skills 系统的实现，是理解该标准的最佳起点。每个技能独立成文件夹，内含 `SKILL.md` 文件，该文件用 Markdown 格式编写指令和元数据，Claude 能自动解析并加载。

- **多元技能目录**：技能覆盖范围广泛，从创意应用（艺术、音乐、设计）到技术任务（Web 应用测试、MCP 服务器生成），再到企业工作流（沟通、品牌建设）均有收录。每个技能都是自包含的，便于单独查看和使用。

- **开源与社区共建**：通过 GitHub 公开分发，任何人都可以浏览、fork 和贡献技能。这种开放模式促进了技能生态的快速生长，让最佳实践能够被社区共享和迭代。

- **简化技能分发**：仓库与技能的在线索引（如 skills.sh）兼容，用户可以通过简单链接直接在 Claude 中引用并加载技能，无需手动复制文件夹。

- **文档与指南集成**：仓库 README 中提供了多个官方链接，涵盖什么是技能、如何在 Claude 中使用、如何创建自定义技能，以及 Anthropic 关于 Agent Skills 的技术博客，形成完整的知识闭环。

## 技术架构

Skills 的设计遵循"约定优于配置"原则。每个技能是一个标准文件夹，核心文件 `SKILL.md` 采用 Markdown 格式，通过 YAML frontmatter 声明技能的名称、描述、所需环境等元数据，正文部分则包含详细的任务说明和操作指引。这种设计使得 Claude 无需额外解析逻辑即可理解技能的用途和调用方式。

配套的脚本和资源文件放置在同一文件夹中，形成自包含的单元。Claude 在运行时动态加载这些文件，因此技能可以携带任意复杂的辅助代码（如 Python 脚本），而不会污染全局环境。这种动态加载机制确保了技能之间的隔离性，也降低了部署复杂度。

从生态角度看，Anthropic 将 Skills 定义为一种开放标准（见 agentskills.io），而本仓库则是这一标准的官方实现之一。这意味着除了 Claude 之外，其他兼容该标准的 AI 工具也能复用这些技能，从而避免了锁定风险。

## 安装与使用

**安装步骤**：

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/anthropics/skills.git
   ```
2. 浏览 `skills` 目录，选择需要的技能文件夹（例如 `skills/art`）。
3. 在 Claude 客户端中（如 Claude Desktop 或 API），通过引用技能文件夹路径或对应的在线索引链接来加载技能。

**最小可用示例**：

假设你想使用仓库中的技能来分析一份数据文件。首先将技能文件夹复制到你的项目环境中，然后在对话中明确要求 Claude 使用该技能：

```
请使用 "data-analysis" 技能分析当前目录下的 sales.csv 文件，生成一份趋势摘要。
```

Claude 会识别技能声明，自动加载 `SKILL.md` 中描述的工作流和脚本，并按步骤执行任务。

如果希望分享自定义技能，只需将技能文件夹推送到任意 Git 仓库，并将仓库地址关联到 agentskills.io 索引，其他用户即可通过链接直接调用。

## 适用场景

- **企业品牌内容生产**：将公司品牌指南、语气规范打包为技能，让 Claude 在撰写对客邮件、营销文案时自动遵循统一标准。
- **专业数据分析流程**：将组织内部的数据处理逻辑、常用代码片段固化为技能，让 Claude 以一致的方式完成数据清洗、可视化和报告生成。
- **个人自动化助手**：将日常重复性任务（如整理会议纪要、生成周报、批量处理文件）封装为技能，实现"一次编写，随时复用"。
- **开发者效率工具**：将 MCP 服务器生成、单元测试编写、代码审查等开发任务标准化为技能，简化 AI 辅助开发的落地成本。

## 项目亮点

- **权威性**：由 Anthropic 官方维护，是 Agent Skills 标准的"第一方实现"，消除了社区版本可能存在的兼容性疑虑。
- **生态开放**：技能采用开放的文件格式和分发协议，不绑定特定平台，未来可迁移至其他兼容环境。
- **工程实践导向**：仓库中的技能并非玩具示例，而是涵盖真实业务场景（如企业沟通、Web 测试）的成熟模板，可用于生产环境。
- **低上手门槛**：`SKILL.md` 基于 Markdown 编写，任何拥有基本写作能力的人都能理解并创建技能，无需编程背景。
- **社区活跃度**：仓库当前拥有超过 16.8 万 Star 且持续增长，验证了其在开发者社区中的高认可度和实用价值。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/skills)
- [Agent Skills 标准官网](http://agentskills.io)
- [Skill 在线索引](https://skills.sh/anthropics/skills)
- [什么是 Skills？(Claude 官方文档)](https://support.claude.com/en/articles/12512176-what-are-skills)
- [创建自定义 Skills 指南](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Anthropic 技术博客：用 Agent Skills 装备真实世界的智能体](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
