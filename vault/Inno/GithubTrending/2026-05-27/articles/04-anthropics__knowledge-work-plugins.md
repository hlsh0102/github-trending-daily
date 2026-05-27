---
tags:
  - trending
  - article
repo: anthropics/knowledge-work-plugins
date: 2026-05-27
language: Python
stars_total: 16764
stars_today: 1718
---
## 项目概述

Knowledge Work Plugins 是一个由 Anthropic 开源的插件集合，专为知识工作者设计，用于将 Claude 打造为贴合其角色、团队和公司的专属专家。该项目主要面向 Claude Cowork 用户，同时也兼容 Claude Code。通过这些插件，用户可以让 Claude 掌握特定的工作风格、数据源、关键工作流和快捷命令，从而在团队中实现更高效、更一致的工作成果。项目采用 Apache-2.0 许可协议，使用 Python 开发，目前已在 GitHub 上获得超过 1.6 万颗星。

## 核心功能

- **角色专属技能包**：每个插件针对特定岗位职责封装了技能、连接器、斜杠命令和子代理，使 Claude 能够精准理解并执行该角色的典型任务。
- **公司级定制化**：支持用户根据自身公司的工具、术语和流程对插件进行深度定制，让 Claude 的行为如同专为团队构建的内部助手。
- **多种工作流集成**：内置与主流生产力和业务工具的连接器，包括 Slack、Notion、Asana、Linear、Jira、HubSpot、ZoomInfo 等，实现数据源的自动化整合。
- **斜杠命令系统**：提供可暴露的快捷命令，团队成员可通过简单的斜杠操作快速触发常见工作流程。
- **子代理协作**：支持在插件内创建和配置子代理，处理更复杂的任务分解与协同作业。
- **模块化插件架构**：每个插件相互独立，用户可根据需要单独安装、启用或禁用特定插件。

## 技术架构

Knowledge Work Plugins 构建于 Claude 的扩展机制之上，采用了模块化设计。每个插件本质上是一个包含配置、技能定义、连接器规范和子代理策略的包。项目主要使用 Python 编写，这与其与 Claude 后端服务的对接方式一致。插件的核心设计思路是将“角色知识”结构化——包括该角色的信息检索模式、输出格式偏好、数据源访问权限以及决策边界。这种架构使得插件既可以开箱即用，也允许深度定制：高级用户可以通过修改配置文件和添加自定义连接器来调整插件行为。此外，项目遵循无状态、可扩展的原则，确保多个插件之间不会相互干扰。

## 安装与使用

基本使用方式如下：

1. **环境准备**：确保你拥有 Claude Cowork 或 Claude Code 的访问权限。
2. **获取插件**：从 GitHub 仓库克隆或下载所需的插件目录。
3. **配置集成**：在插件配置文件中指定需要连接的工具（如添加 Slack Token、Notion API Key 等）。
4. **加载插件**：在 Claude 的环境中加载插件包，通常通过设置环境变量或导入配置完成。

以下是一个最小可用示例（以 productivity 插件为例）：

```python
# 假设你已经将 productivity 插件放在指定路径
from knowledge_work_plugins.productivity import ProductivityPlugin

# 初始化插件
plugin = ProductivityPlugin(
    slack_token="your_slack_token",
    notion_token="your_notion_token",
    calendar_provider="microsoft365"
)

# 在 Claude 会话中启用
plugin.enable()
```

## 适用场景

- **个人效率提升**：知识工作者通过 productivity 插件管理日程、任务和待办事项，减少重复性操作，提升日常工作效率。
- **销售团队赋能**：销售团队使用 sales 插件进行客户调研、通话准备、渠道评审和竞争情报分析，从而优化销售流程。
- **跨工具数据整合**：需要同时操作多个 SaaS 工具的用户，可通过插件实现数据的自动拉取和统一展示，减少上下文切换。
- **新成员快速上手**：团队利用公司的定制化插件，让新员工在面对特定工作流程时获得一致的指导和支持。

## 项目亮点

- **真正的角色适配**：不同于通用型 AI 助手，该插件集合专注于模拟特定工作岗位的专业行为，而非提供泛化答案。
- **深度的企业定制性**：用户不仅能使用现有插件，还能将其改造为完全匹配公司内部规范的工具，这在进行团队级部署时具有显著优势。
- **开源与可审计**：Apache-2.0 许可保证了透明度和可修改性，企业可以自行审查代码、添加功能而不受厂商锁定。
- **丰富的预构建连接器**：开箱即提供多达 11 种主流工具集成，覆盖了知识工作者常用的绝大多数场景。
- **社区与生态潜力**：作为开源项目，未来其他组织和开发者可以贡献更多角色插件的可能性使得生态持续扩充。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/knowledge-work-plugins)
- [Claude Cowork 产品页面](https://claude.com/product/cowork)
- [Claude Code 产品页面](https://claude.com/product/claude-code)
