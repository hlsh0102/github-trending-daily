---
tags:
  - trending
  - article
repo: humanlayer/skills
date: 2026-09-06
language: TypeScript
stars_total: 2824
stars_today: 442
---
## 项目概述

`humanlayer/skills` 是 HumanLayer 团队开源的一套 Claude Code 技能集合。它通过 `npx skills add` 命令快速安装，为开发者提供了一系列可直接调用的斜杠命令（如 `/improve-claude-md`），用于改善 Agent 对项目说明文件的遵循度、精简 React 组件属性类型、构建自动化的 Agent 迭代工作流等。该项目主要面向使用 Claude Code 进行开发、希望提升 AI 编码助手在真实代码库中表现质量的开发者与团队。

## 核心功能

- **improve-claude-md**：自动重写项目中的 `CLAUDE.md` 指令文件，利用 `<important if>` 条件块结构化组织指令，显著提升 Claude 对项目上下文的指令遵循率。
- **narrow-react-prop-types**：扫描 React 组件代码，将 prop types 收窄至实际活跃的代码路径，剔除仅存在于 Storybook、测试或 mock 中的冗余状态，减少类型误导。
- **build-iterated-agentic-loop**：在仓库内生成一套完整的“本地技能 + GitHub Actions 编码 Agent”工作流，包含提示词、记忆文件和参考模板，实现自动化的迭代编码循环。
- **design-control-loop**：通过交互式访谈，为你量身设计一个以“传感器–控制器–执行器–扰动”为框架的 Agent 控制循环方案，并将其实现为可本地运行的组件和定时任务工作流。
- **show-me**：快速解析当前代码主题，以简洁图表、代码形状草图和聚焦的 HTML 可视化片段清晰呈现复杂逻辑。

## 技术架构

该项目本身是 TypeScript 编写的技能管理生态，核心设计围绕 Claude Code 的扩展体系展开。每个技能本质上是一个封装了特定提示词、代码扫描逻辑与模板生成脚本的独立模块，通过标准化的 `npx skills add` 命令分发与安装。安装后，技能以斜杠命令的形式注入开发环境，在与 Claude 的交互中按需触发。

架构上的显著特点是**条件式指令生成**与**代码感知的静态分析结合**。例如，`improve-claude-md` 在重写指令时采用结构化条件块，允许 Claude 在运行时根据文件状态选择执行路径，而非笼统的静态指令；`narrow-react-prop-types` 则利用抽象语法树（AST）分析实际引用的 props，将分析结果与类型定义交叉比对，从而生成精准的收窄建议。`design-control-loop` 与 `build-iterated-agentic-loop` 则展示了将 Agent 编排模式（控制回路、迭代记忆）落地为仓库本地可执行资产的能力，体现了从“单一技能”向“可复用的自动化系统”演进的架构思路。

## 安装与使用

**前置条件**：已安装 Node.js 18+ 与 Claude Code CLI。

安装任意技能的命令格式统一，例如：

```bash
npx skills add humanlayer/skills --skill improve-claude-md
```

在除 `humanlayer/skills` 之外的任意项目目录执行上述命令后，技能即被注入当前项目的 Claude Code 环境中。

使用时，直接在 Claude Code 会话中键入对应斜杠命令：

```
/improve-claude-md
```

以 `improve-claude-md` 为例，Claude 会读取项目根目录下的 `CLAUDE.md`（若不存在则提示创建），生成一份使用 `<important if>` 块重写后的新指南，并要求你审阅确认后替换原文件。

若要同时安装全部技能，可执行：

```bash
npx skills add humanlayer/skills
```

## 适用场景

- **维护 AI 友好的项目文档**：当团队发现 Claude 无法稳定遵循 `CLAUDE.md` 中的工程规范（如提交消息格式、分支策略），但又不确定如何改进指令时，`improve-claude-md` 可自动重构协作指南，提升一致性。
- **收紧 React 代码库的类型契约**：在大型 React 应用中，当 Storybook 或测试文件中的 props 干扰了类型推断，导致智能提示与实际调用不符时，`narrow-react-prop-types` 能帮助清理类型定义。
- **搭建自动化编码 Agent 流水线**：如果你想在 GitHub Actions 中定期运行一个能够自我迭代、根据任务反馈持续修改代码的 Agent，`build-iterated-agentic-loop` 提供了开箱即用的参考实现与脚手架。
- **学习与设计 Agent 控制模式**：架构师或平台工程师在设计复杂 Agent 行为时，可通过 `design-control-loop` 的引导式访谈，梳理系统边界与控制信号，快速产出原型。

## 项目亮点

- **极低的接入成本**：项目将复杂的指令工程与代码分析逻辑封装为即插即用的斜杠命令，不要求使用者了解内部实现，两条命令即可完成安装与使用。
- **聚焦真实痛点**：相比于泛化的 Agent 调优讨论，每个技能针对一个具体的、高频的问题（如指令遵循、类型失真、CI 迭代效率）给出了直接可执行的解决方案。
- **设计理念领先**：通过对 React 类型、指令文件等静态资源进行程序化感知与修改，改变了“Agent 只能被动读取代码”的传统模式，使其能够积极参与到工程资产的重构中，且支持将整套 Agent 工作流回落到仓库内实现版本管理与复用。
- **开放与社区驱动**：项目采用 MIT 许可证，并在 GitHub 上保持较高活跃度，扩展生态的边际成本低，鼓励开发者贡献自定义技能。

## 相关链接

- [GitHub 仓库](https://github.com/humanlayer/skills)
- [HumanLayer 官网](https://humanlayer.dev)
