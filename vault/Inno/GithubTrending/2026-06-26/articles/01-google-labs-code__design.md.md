---
tags:
  - trending
  - article
repo: google-labs-code/design.md
date: 2026-06-26
language: TypeScript
stars_total: 19797
stars_today: 1475
---
## 项目概述

DESIGN.md 是一个用于向编码代理（coding agents）描述视觉标识的格式规范。在 AI 辅助编程日益普及的当下，开发者经常需要让 AI 理解并保持一致的设计风格。传统的做法往往是通过零散的提示词或复杂的配置，效果不稳定且难以维护。DESIGN.md 解决了这一问题：它提供了一种结构化、标准化的方式，将设计系统的核心信息以机器可读的形式写入文件，让 AI 代理能够持久、准确地理解并应用你的设计语言。

该项目目标用户广泛，包括前端开发者、UX 设计师、产品经理以及所有使用 AI 编码工具（如 GitHub Copilot、Cursor 等）构建用户界面的团队。无论是独立项目、设计系统维护，还是需要在多个 AI 工具间保持视觉一致性，DESIGN.md 都能提供清晰的指导。

## 核心功能

- **机器可读设计令牌（YAML 前置元数据）**：通过 YAML 格式定义颜色、字体、圆角、间距等设计令牌，为 AI 代理提供精确的数值。代理可以直接读取这些数值并应用到生成的代码中，避免颜色偏差或字体错位。
- **人类可读设计说明（Markdown 正文）**：在 YAML 令牌之后，支持用 Markdown 书写设计理念、使用规则和上下文说明。这部分内容告诉 AI 代理“为什么这样设计”，而不仅仅是“是什么”。例如，解释某个颜色代表“严谨”或某个字体风格匹配“科技感”。
- **结构化且渐进式**：规格从最基本的颜色和字体开始，逐步扩展到布局、间距、阴影等复杂属性。这种渐进式结构让 AI 代理可以快速理解核心部分，同时为更精细的定制留出空间。
- **单一文件，全局一致**：所有设计信息集中在一个 `DESIGN.md` 文件中，避免了多个配置文件的碎片化问题。无论是开发者手动编写，还是由设计工具自动导出，都能保持一致性。
- **对 AI 代理透明**：文件格式直观，AI 代理无需额外训练即可解析。YAML 部分直接提供数值，Markdown 部分提供语境，两者结合让代理的生成结果更符合预期。
- **易于版本控制**：作为普通文本文件，DESIGN.md 可以完全纳入 Git 版本管理。设计系统的每次变更都能被追踪、回滚，并与团队协作流程无缝集成。

## 技术架构

DESIGN.md 的设计核心在于“双重可读性”——同时面向人和机器。技术上，它采用以下分层架构：

1.  **YAML 前置元数据层**：位于文件顶部，用三连短线 (`---`) 包裹。这部分使用标准 YAML 格式，包含 `name`（设计系统名称）、`colors`（颜色映射）、`typography`（排版定义）、`rounded`（圆角值）、`spacing`（间距值）等键值。AI 代理可以像解析 JSON 或 YAML 配置一样直接提取这些结构化数据，用于生成准确的 CSS 变量、Tailwind 配置或颜色常量。

2.  **Markdown 正文层**：YAML 之后是标准的 Markdown 文本。这里可以包含设计概览、颜色规则、排版原理、组件使用约束等。Markdown 的富文本能力（标题、列表、代码块、强调）使得人类开发者可以自然书写，而 AI 代理则通过自然语言处理理解上下文。

3.  **解析与生成机制**：工具链可以读取此文件，将其转换为多种输出格式。例如，提取 YAML 生成 CSS 自定义属性（`--color-primary: #1A1C1E`）、Tailwind 配置（`theme: { extend: { colors: {...} } }`）或设计令牌 JSON。AI 代理则直接解析文件内容，结合 YAML 数值和 Markdown 说明，在代码生成时应用设计规则。

这种架构的优势在于：不需要复杂的 DSL，不依赖特定框架，是一个纯粹的、可移植的规范。任何支持 YAML 和 Markdown 的解析器都能处理它。

## 安装与使用

DESIGN.md 本质上是一个规范，不需要传统的“安装”步骤。你只需在项目根目录（或任意合适的路径）创建一个 `DESIGN.md` 文件，按照规范撰写内容即可。

**最小可用示例：**

1.  在项目根目录创建 `DESIGN.md` 文件。
2.  写入以下内容：

```markdown
---
name: MyApp
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  accent: "#B8422E"
  background: "#F7F5F2"
typography:
  body:
    fontFamily: Inter
    fontSize: 1rem
  heading:
    fontFamily: Inter
    fontSize: 2rem
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 8px
  md: 16px
---

## Overview

Minimalist and clean design for a modern web application.

## Colors

- **Primary (#1A1C1E):** Used for all heading and body text.
- **Secondary (#6C7278):** Used for borders, dividers, and secondary text.
- **Accent (#B8422E):** Applied to primary buttons, links, and interactive elements.
- **Background (#F7F5F2):** Page background color.
```

3.  在你的 AI 编码工具中，引用此文件或将其路径告知代理。例如，在对话中提示：“请参考项目中的 `DESIGN.md` 文件来生成用户界面。” AI 代理将自动解析并应用这些设计规范。

对于更复杂的项目，可以扩展规格，加入 `shadows`（阴影）、`breakpoints`（断点）、`animation`（动画）等属性。

## 适用场景

- **AI 辅助前端开发**：使用 GitHub Copilot、Cursor、Codeium 等 AI 工具开发 UI 时，通过 `DESIGN.md` 让 AI 生成风格一致的组件代码，减少重复的“调整样式”指令。
- **设计系统标准化**：团队维护多个项目或设计系统时，用 `DESIGN.md` 统一描述，确保所有 AI 工具和新成员快速理解视觉规范。
- **设计交付与开发衔接**：设计师将设计令牌和说明写入 `DESIGN.md`，开发者或 AI 可直接取用，消除设计与开发之间的信息落差。
- **跨工具协作**：同一个 `DESIGN.md` 文件可以被 VSCode 插件、Figma 插件、自动化构建脚本等多种工具解析使用，实现视觉规范的一次定义、多处消费。

## 项目亮点

- **反直觉的简洁性**：在众多设计令牌规范（如 Design Tokens Format Module）和工具链中，DESIGN.md 选择了最朴素的方案——一个 Markdown 文件。这种简洁意味着零学习曲线、零依赖、零构建步骤。
- **人和 AI 的接口**：它不像纯 YAML/JSON 文件那样冰冷，而是保留了可读性极佳的 Markdown 说明部分。这让人类设计师可以随时书写设计思考，而 AI 同样可以深入理解。
- **与现有工作流无缝集成**：不是取代任何现有工具，而是作为它们的补充。你可以继续使用 Tailwind、Styled Components 或任何框架，`DESIGN.md` 只负责给 AI 提供设计蓝图。
- **社区驱动的进化**：项目在 GitHub 上开源（Apache-2.0 许可），规格本身也预留了扩展点。开发者社区可以贡献新的令牌类型、解析器工具或最佳实践案例。

## 相关链接

- [GitHub 仓库](https://github.com/google-labs-code/design.md)
- [DESIGN.md 规范官方文档](https://design.md/)
