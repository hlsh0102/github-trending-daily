---
tags:
  - trending
  - article
repo: anthropics/claude-plugins-official
date: 2026-08-27
language: Python
stars_total: 34504
stars_today: 290
---
## 项目概述

`anthropics/claude-plugins-official` 是 Anthropic 官方维护的 Claude Code 插件目录。该项目为开发者提供了一个集中、经过筛选的高质量插件集合，这些插件能够显著扩展 Claude Code 的功能边界。无论是自动化日常开发任务、集成外部服务，还是增强 Claude 的代码理解能力，这个目录都扮演着插件生态系统中“应用商店”的角色。

该项目的核心目标用户包括：使用 Claude Code 进行日常开发的软件工程师、希望将 Claude 接入自有工作流的团队，以及有意向 Claude 生态贡献插件的第三方开发者。通过提供统一的管理和分发机制，它降低了插件发现、安装和更新的复杂度。

## 核心功能

- **官方与第三方插件聚合**：项目内部划分了 `/plugins`（Anthropic 内部开发维护）和 `/external_plugins`（来自合作伙伴与社区的第三方插件）两个独立区域，清晰地区分了插件来源与维护责任。
- **一键安装与发现**：用户可通过 Claude Code 内置的 `/plugin install {plugin-name}@claude-plugins-official` 命令直接安装，或通过 `/plugin > Discover` 浏览界面发现可用插件，无需手动处理依赖或配置文件。
- **标准化的插件结构**：每个插件遵循统一的目录规范（包含 `.claude-plugin/plugin.json` 元数据文件、可选的 `.mcp.json` MCP 服务器配置、`commands/` 斜杠命令目录等），这保证了插件在 Claude Code 中的行为一致性和可预测性。
- **社区提交与审核机制**：为外部开发者提供了正式的提交表单，第三方插件需要满足质量和安全标准才能被收录，这为整个插件生态设定了基线门槛。
- **信任与安全警示**：项目在 README 中强调了安全使用原则，明确声明 Anthropic 无法验证第三方插件内容的可靠性，引导用户在安装前审慎评估来源。

## 技术架构

该项目本质上是围绕 Claude Code 插件系统构建的元仓库，其技术架构体现了“规范驱动”的设计思路：

- **插件元数据规范**：`.claude-plugin/plugin.json` 是每个插件的必需组件，它定义了插件的名称、版本、描述等关键信息，Claude Code 通过读取此文件来识别和加载插件。
- **MCP（Model Context Protocol）集成**：可选的 `.mcp.json` 文件允许插件携带 MCP 服务器配置，使 Claude Code 能够与外部工具和数据源进行标准化交互，这是实现复杂插件功能（如数据库查询、API 调用）的基础。
- **目录与代码隔离**：通过物理上分离内部插件与外部插件目录，项目在保障官方插件稳定性的同时，也为社区创新提供了开放入口，这种架构减少了不同来源插件之间的潜在冲突。
- **基于 Claude Code 插件系统**：项目没有自行实现运行时环境，而是完全依赖 Claude Code 内置的插件系统来执行和管理插件，这大大简化了分发逻辑，使得安装过程对用户透明。

## 安装与使用

**前置条件**：确保已安装最新版本的 Claude Code 并完成身份验证。

**安装插件**：

1. 打开终端并启动 Claude Code。
2. 执行以下命令之一：
   - 指定安装：`/plugin install {plugin-name}@claude-plugins-official`
   - 交互式浏览：在 Claude Code 中输入 `/plugin`，然后选择 `Discover` 选项，从列表中挑选插件。
3. 等待安装完成，Claude Code 会自动处理依赖和配置。

**最小使用示例**：

假设你想安装某个名为 `example-plugin` 的插件，它提供 `/example` 斜杠命令用于生成测试用例：

```
# 在 Claude Code 会话中
/plugin install example-plugin@claude-plugins-official

# 安装成功后直接使用该插件的命令
/example build --module user-service --output ./tests
```

插件安装后通常无须额外配置即可使用。若插件依赖 MCP 服务器，则对应的 `.mcp.json` 配置会被自动加载。

## 适用场景

- **日常开发效率提升**：开发者可以安装代码格式化、静态分析、日志解析等插件，将重复性工作交给 Claude Code 处理。
- **特定技术栈集成**：针对特定框架（如 React、Django）或云服务（如 AWS、GCP）的插件，可以让 Claude 更好地理解和操作相关代码或资源。
- **团队标准化工具集**：团队可以统一使用官方推荐或内部开发的插件，确保所有成员的开发环境具备一致的工具能力。
- **快速原型与自动化**：借助插件提供的预构建命令，可以快速执行代码碎片化任务，例如自动生成 API 文档或重构代码结构。

## 项目亮点

- **官方权威性**：由 Anthropic 亲自维护，这意味着插件目录的规范性、更新及时性以及兼容性都更有保障，开发者可以放心地将其集成到核心工作流中。
- **生态分级管理**：内部与外部插件的明确区分，既保证了官方插件的质量，又为社区贡献提供了清晰路径，这种“官方核心 + 社区扩展”的模式兼顾了稳定性和创新性。
- **低门槛发现与安装**：相比手动从 GitHub 克隆和配置插件，该目录提供了一致的安装接口，大幅降低了使用门槛。
- **安全透明机制**：通过明确的安全警示和提交审核流程，项目在开放的生态中建立了必要的信任边界，这对企业级用户尤为重要。

## 相关链接

- [GitHub 仓库](https://github.com/anthropics/claude-plugins-official)
- [插件目录提交表单](https://clau.de/plugin-directory-submission)
- [Claude Code 官方文档](https://claude.com/zh/docs/claude-code)
