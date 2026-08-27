---
tags:
  - trending
  - article
repo: JetBrains/go-modern-guidelines
date: 2026-08-27
language: Go
stars_total: 1872
stars_today: 314
---
## 项目概述

JetBrains/go-modern-guidelines 是一个旨在帮助 AI 编码代理编写现代 Go 代码的指南项目。该项目由 JetBrains 维护，针对当前 AI 编码工具普遍生成过时 Go 代码的问题，提供了一套系统性的、版本感知的现代 Go 编写规范。

该项目的核心目标用户是使用 AI 编码助手（如 GitHub Copilot、JetBrains AI Assistant 等）进行 Go 开发的开发者，以及希望提升代码质量的 Go 团队。它通过为 AI 代理提供明确的现代 Go 特性参考，解决训练数据滞后和频率偏差两大核心问题，从而显著改善 AI 生成的 Go 代码质量。

## 核心功能

- **版本感知指导**：自动检测项目的 `go.mod` 文件中的 Go 版本，并指导 AI 代理仅使用该版本及之前可用的语言特性和标准库功能。
- **现代惯用法替代**：提供从 Go 1.0 到 Go 1.27 最有用的特性指南，覆盖 `modernize` 分析器涉及的全部内容，帮助代理将旧模式替换为现代惯用法。
- **标准库首选**：引导 AI 代理优先使用标准库中的现代函数，如 `slices.Contains` 替代手动循环、`cmp.Or` 替代多级 nil 检查链。
- **新版本特性支持**：涵盖最新版本的新增功能，例如 Go 1.26 中的 `new(42)` 创建指针和 `errors.AsType[T]` 类型安全错误匹配。
- **内联示例**：每个指南条目都配有具体的代码示例，帮助 AI 代理理解和应用正确的写法。

## 技术架构

项目采用基于 Markdown 的指南文件作为核心载体，通过 `plugin/skills/use-modern-go/SKILL.md` 文件向 AI 代理传递规则。这种设计具有极高的可移植性和可扩展性——指南文件可以被不同的 AI 代理框架加载，无论是基于提示工程的传统方法还是基于技能的现代代理架构。

架构上的关键设计决策是“版本感知动态适配”。与静态的编码规范不同，该指南要求 AI 代理首先读取项目的 `go.mod` 文件来确定目标 Go 版本，然后仅在该版本支持的特性范围内提供建议。这种机制确保了生成代码的兼容性，有效避免了因使用过高版本特性而导致的编译错误。

项目的技术深度体现在对 Go 语言演进历史的系统梳理上。从 Go 1.0 到 1.27，每个版本中值得推荐的新特性都被筛选和归档，形成一个结构化的知识库。这种体系化的整理方式远超一般编码规范的范围，使 AI 代理能够理解语言的演进脉络，在正确的场景中使用合适的特性。

## 安装与使用

该项目本身是规则集合，因此安装过程非常简单，只需将仓库克隆到本地或将其配置集成到 AI 编码代理的设置中。

基本使用步骤：

```bash
git clone https://github.com/JetBrains/go-modern-guidelines.git
```

或者将 `SKILL.md` 文件复制到你的 AI 工具配置目录中。对于使用支持技能的 AI 代理框架（如支持 Skills 的 IDE 插件），只需将 `plugin/skills/use-modern-go/` 目录链接到代理的技能目录。

配置完成后，当你的 AI 编码代理写入 Go 代码时，它会自动参考此指南：

```go
// 传统写法（不推荐）
var maxVal int
if a > b {
    maxVal = a
} else {
    maxVal = b
}

// 现代写法（AI 代理将自动采用）
maxVal := max(a, b)
```

```go
// 错误处理传统写法
var user *User
if err := findUser(id, &user); err == nil && user != nil && user.Name != "" {
    // 处理逻辑
}

// 现代写法
user, err := findUser(id)
name := cmp.Or(user.Name, "unknown")
```

## 适用场景

- **AI 辅助开发团队**：团队统一应用此指南后，AI 生成的所有 Go 代码将保持一致的现代风格，减少资深开发者审查和修改 AI 代码的负担。
- **大型 Go 项目现代化改造**：在维护较旧 Go 代码库时，使用该指南驱动 AI 代理解析并重构现有代码，逐步引入新特性。
- **Go 新手学习**：开发者在学习 Go 时，可以参照此指南了解当前推荐的最佳实践，避免从过时的教程中习得旧模式。
- **CI 代码审查辅助**：将指南内容集成到自动化审查工具中，用于检测提交代码中是否存在可以现代化的旧写法。

## 项目亮点

与一般 Go 编码规范相比，本项目最突出的差异化优势在于其“为 AI 代理量身定制”的设计哲学。传统规范依赖开发者的主动阅读和记忆，而本项目将最佳实践以精确、可操作的指令形式注入 AI 的生成流程，效果更加稳定一致。

其次，版本感知机制是同类项目中的独创。多数规范要么只覆盖稳定版特性，要么无差别地推广最新特性。本项目巧妙地通过 `go.mod` 检测，实现了不同项目间的自动适配，既保证了代码可运行性，又不失现代性。

最后，JetBrains 的品牌背书和开源许可证（Apache-2.0 协议）使其可以自由集成到任何商业工具中，这保证了项目的长期维护质量和生态影响力。

## 相关链接

- [GitHub 仓库](https://github.com/JetBrains/go-modern-guidelines)
- [使用指南（SKILL.md）](https://github.com/JetBrains/go-modern-guidelines/blob/main/plugin/skills/use-modern-go/SKILL.md)
