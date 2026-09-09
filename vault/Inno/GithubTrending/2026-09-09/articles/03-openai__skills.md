---
tags:
  - trending
  - article
repo: openai/skills
date: 2026-09-09
language: Python
stars_total: 26661
stars_today: 490
---
## 项目概述

`openai/skills` 是 OpenAI 官方维护的 **Codex 技能目录仓库**。Agent Skills 是包含指令、脚本和资源的文件夹，AI 代理可以自主发现并使用这些技能来执行特定任务。该项目的核心理念是"一次编写，处处使用"（Write once, use everywhere），旨在将复杂任务的执行能力打包为可复用的标准化技能模块。

需要特别注意的是，**该仓库目前已标记为已弃用（deprecated）**。OpenAI 已将其功能迁移至 [OpenAI Plugins 仓库](https://github.com/openai/plugins)，新的 Codex 技能和插件示例均在后者中持续更新。不过，本仓库仍保留了完整的技能分类框架和历史示例，对理解 Codex 技能体系的发展脉络仍具参考价值。该项目面向的主要用户是希望通过预置能力快速扩展 Codex 功能的企业团队、使用 Codex 进行自动化任务的开发者，以及希望创建和分发自定义技能的个人开发者。

## 核心功能

- **技能分类体系**：仓库将技能划分为 `.system`（系统级）、`.curated`（精选级）和 `.experimental`（实验级）三大类，不同的分类对应不同的安装信任程度和适用场景。
- **自动安装系统级技能**：位于 `.system` 文件夹中的技能会随着最新版本的 Codex 自动安装，用户无需手动干预即可获得基础能力。
- **命令行式技能安装器**：通过内置的 `$skill-installer` 指令，用户可以在 Codex 内快速安装精选技能（按名称安装）或实验技能（指定文件夹路径）。
- **技能创建指南**：README 中明确引导开发者查阅 [Codex 文档](https://developers.openai.com/codex/skills/create-skill) 中的技能创建教程，支持自定义技能开发。
- **规范化技能打包**：技能被定义为"指令、脚本和资源的文件夹"，这种结构化打包方式保证了技能在多环境中的可移植性和可维护性。
- **开放标准共建**：项目连接至 [Agent Skills open standard](https://agentskills.io)，推动技能格式的标准化进程。

## 技术架构

该仓库的技术内核围绕"技能包"这一概念展开。每个技能本质上是一个遵循特定目录结构的文件夹，包含三类资源：**指令文件**（告诉代理如何执行任务的说明性文本）、**可执行脚本**（用于具体完成任务的代码，常见为 Python）以及**辅助资源**（可供运行时参考的附加文件）。

技能发现机制基于分类目录扫描。`.system` 目录中的技能被视为"内建能力"，与 Codex 发布版同步分发；`.curated` 目录中的技能经过官方质量评估，适合大部分任务场景；`.experimental` 目录则保留社区贡献尚未稳定验证的技能，需要用户显式指明路径安装，降低了误用风险。

设计上，该项目强调**解耦与复用**：技能与具体对话流程解绑，使同一技能可在不同任务中多次调用；技能是纯文件形态，天然支持 Git 版本管理，便于团队协同迭代。虽然仓库现已弃用，但其架构思路（分类分层、基于目录的文件组织、代理可发现性）被完整沿用到了后续的 OpenAI Plugins 项目中，并通过插件系统做了进一步扩展。

## 安装与使用

由于仓库已弃用，新用户建议直接参考 [OpenAI Plugins 仓库](https://github.com/openai/plugins)获取最新技能示例，或阅读 [Build plugins 指南](https://developers.openai.com/codex/plugins/build)学习创建 skill-only 插件。对于需要沿用旧示例的场景，可参考以下历史用法：

**步骤 1：确认 Codex 环境已更新至支持技能发现的最新版本。**

**步骤 2：安装精选技能（按名称）。** 在 Codex 会话中执行：

```
$skill-installer gh-address-comments
```

该命令默认从 `skills/.curated` 目录中寻找并安装对应技能。

**步骤 3：安装实验技能（显式指明来源）。** 例如：

```
$skill-installer install the create-plan skill from the .experimental folder
```

系统将解析文件夹路径并完成安装。

**最小可用示例**：以 `gh-address-comments` 技能为例（其功能为给 GitHub Issue 评论添加可寻址特性），安装后即可在 Codex 交互中下达相关指令，Codex 将自动加载技能包中的指令与脚本执行任务。用户无需关心技能内部实现细节。

## 适用场景

- **版本控制流程增强**：利用 `gh-address-comments` 等 GitHub 相关技能，改善 Issue 评论区中跨评论交互的定位方式。

- **规划与任务拆分**：使用 `create-plan` 等实验性技能，帮助 Codex 生成结构化执行计划，提升长任务的条理性与可执行性。

- **企业内 Codex 能力标准化**：团队可将内部沉淀的技能统一放入目录并通过 Git 分发，确保各成员在相同技能基准下工作。

- **技能开发学习与研究**：将本仓库作为 Craft Skills 的示例集，新手开发者可研读不同技能的文件结构，理解 OpenAI 推荐的技能组织方式，为后续在 OpenAI Plugins 中创作自定义技能打基础。

## 项目亮点

- **官方示范性**：作为 OpenAI 官方仓库，其技能分类与目录设计直观展示了 Agent Skills 规范的最佳实践，是理解"技能即文件夹"范式不可多得的案例。
- **分级信任模型**：通过 `system/curated/experimental` 三级目录区分技能成熟度，让用户在便捷性与风险控制之间自由平衡，这一设计理念在后续插件体系中得到继承。
- **零成本扩展机制**：安装技能不需要重新编译或复杂配置，只需一行 `$skill-installer` 指令即可完成，显著降低了 Codex 功能的扩展门槛。
- **清晰的弃用迁移路径**：项目公告页直接指明接续仓库（OpenAI Plugins）与官方开发指南链接，体现了良好的项目生命周期管理意识，减少用户因仓库停更而陷入的维护困境。

## 相关链接

- [GitHub 仓库（已弃用）](https://github.com/openai/skills)
- [OpenAI Plugins 仓库（当前维护版本）](https://github.com/openai/plugins)
- [Build plugins 开发指南](https://developers.openai.com/codex/plugins/build)
- [Codex 技能文档](https://developers.openai.com/codex/skills)
- [Agent Skills 开放标准](https://agentskills.io)
