---
tags:
  - trending
  - article
repo: JuliusBrussee/caveman
date: 2026-07-05
language: JavaScript
stars_total: 84178
stars_today: 1089
---
## 项目概述

Caveman 是一个面向 AI 编码代理的语言优化插件，核心哲学可以用一句话概括：「why use many token when few token do trick」。该工具通过让 AI 代理以「原始人」风格回答问题，在保持回答质量不变的前提下，将输出 token 消耗降低约 **65%**。

项目由开发者 JuliusBrussee 创建，主要服务于使用 Claude Code、Codex、Gemini、Cursor、Windsurf、Cline、Copilot 等 30 多种 AI 编程助手的用户。无论你是在使用终端中的代理、IDE 插件还是对话式编码助手，Caveman 都能以极简安装步骤介入，让代理从滔滔不绝变为言简意赅。

## 核心功能

- **Token 削减 65%**：通过去芜存菁、去除多余填充词和冗长解释，在不牺牲答案准确性的前提下，大幅减少输出 token 数量，直接降低 API 调用成本。
- **保持答案质量**：去除的是修饰性语言和废话，保留核心技术内容。回答依然完整、正确、可执行，只是表达方式更直接。
- **简易安装**：仅需一条命令或导入一个配置文件，即可在支持的 30 多种代理上生效，无需修改原有工作流程。
- **多级别「原始化」**：提供不同激进程度的语言压缩等级（Grunt 级别），从轻微压缩到极度精简，用户可根据使用场景自行选择。
- **兼容主流编码代理**：覆盖 Claude Code、Codex、Gemini、Cursor、Windsurf、Copilot 等行业内常见工具，跨平台支持完善。
- **开源可审计**：基于 MIT 许可证发布，代码完全透明，用户可查看、自定义或贡献压缩逻辑。

## 技术架构

Caveman 本质上是一个**提示词（prompt）注入插件**。它的工作原理并非重新训练模型，而是在代理启动时通过系统提示或配置文件，注入一组经过设计的语言风格约束指令。

具体而言，Caveman 利用代理对系统提示的遵守能力，设定一系列语言规则：省略冠词、简化句子结构、用短词替换长词、减少废话和表示过渡的短语。例如，将「I think we should consider using async/await here because it would improve readability and prevent blocking」重写为「use async/await. no block. more read. good.」。

项目以 JavaScript 为主要实现语言，核心逻辑围绕提示词的生成和分发。它会根据不同代理的类型和环境（终端、插件、Web 客户端），生成适配的提示格式并注入到代理的上下文中。对于支持插件系统的代理，Caveman 以独立插件形式运行；对于不支持插件的环境，则通过配置文件或 Shell 别名进行挂载。

同时，Caveman 提供了多套预定义的语言压缩配置（Grunt 级别）。每个级别对应不同强度的压缩规则，用户可通过简单的参数选择所需的精简程度。这种设计让用户在「节省 token」和「保留可读性」之间拥有灵活选择空间。

## 安装与使用

安装 Caveman 的过程极为简单。以最常用的 Claude Code 为例，只需运行：

```
npx caveman install
```

若使用其他代理（如 Codex、Gemini 或 Cursor），可在项目所在目录运行对应的初始化命令，或直接手动将 Caveman 的提示模板粘贴到代理的系统提示词中。

使用示例：

1. **基本使用**：安装后，正常使用 Claude Code 编写代码或提问。例如问「优化这段 Python 代码」，原本长回答会被压缩为「用 list comprehension，去掉临时变量。快 2 倍。给你新版本：...」。

2. **选择级别**：安装时可通过参数指定 Grunt 级别，例如 `npx caveman install --grunt medium`，表示采用中等压缩强度。不指定则默认使用中等级别。

3. **移除插件**：如需恢复原始风格，运行 `npx caveman uninstall` 即可完全移除所有影响。

在 IDE 插件（如 Cursor 或 WindSurf）中，安装过程通常仅需在设置页面激活 Caveman 插件，或在项目配置中添加对应字段。

## 适用场景

- **高频 AI 编码交互**：对于日常重度依赖 AI 编码助手的开发者，Caveman 可显著减少每次对话的输出量，降低整体 API 费用，让反馈更快、更直接。
- **成本敏感的项目或团队**：当团队使用付费 API（如 Claude Code 或 GPT-4），且每日调用量较大时，减少 65% 的输出 token 带来的成本节约非常可观。
- **终端环境下的效率追求者**：在使用终端代理时，冗长的回答影响阅读效率。Caveman 有助于快速提取核心信息、代码块和建议，提升工作流紧凑度。
- **需要快速了解工具链结果的场景**：在 DevOps 流水线、CI/CD 环境或代码审查辅助中，短而直接的回答更容易被自动化流程或协作成员快速理解。

## 项目亮点

与其他 token 压缩方式相比，Caveman 有三个突出的差异点：

- **无需重新训练或微调模型**。许多优化方案需要基于特定模型进行微调或使用专门的小模型，而 Caveman 完全工作在 prompt 层，兼容现有所有主流代理，不需要改变底层模型，也无需额外硬件成本。
- **风格化压缩不减损信息**。大部分 token 节约工具通过截断回答或强迫模型输出更短内容来实现，可能导致信息丢失。Caveman 采用「语言风格修改」而非「内容丢弃」，结果同样是简洁，但核心内容——代码片段、逻辑解释、最佳实践——完整保留。
- **生态兼容性极强**。覆盖 30 多种编码代理，覆盖了当前主流开发场景。安装一次，随处可用。同时，MIT 许可证允许二次开发，使得用户可以针对特定代理或语言做出定制化修改，也便于集成到企业内部工具中。

## 相关链接

- [GitHub 仓库](https://github.com/JuliusBrussee/caveman)
- [安装指南 (INSTALL.md)](https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md)
- [Caveman 生态及更多信息](https://github.com/JuliusBrussee/caveman#the-whole-cave)
