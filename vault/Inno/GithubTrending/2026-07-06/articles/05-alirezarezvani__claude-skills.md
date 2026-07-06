---
tags:
  - trending
  - article
repo: alirezarezvani/claude-skills
date: 2026-07-06
language: Python
stars_total: 20758
stars_today: 392
---
## 项目概述

Claude Skills 是一个面向 AI 编码助手的开源技能库与插件集合，由开发者 Alireza Rezvani 维护。该项目目前包含 **355 个生产就绪的技能、插件和代理技能**，覆盖工程、DevOps、市场营销、安全、合规、C 级高管咨询、学术研究、企业运营、商业与财务以及日常生产力等领域的专业能力。

项目的核心目标是解决 AI 编码助手在特定领域任务中“泛而不精”的问题。通过提供预构建、可复用的“经验包”，开发者和团队可以将 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等 13 种主流编码代理快速武装成特定领域的专家，大幅减少重复提示词工程和时间成本，提升 AI 辅助编程的准确性与产出质量。

## 核心功能

- **355 个即用型技能**：涵盖 330+ 个独立技能，无需手动编写复杂的系统提示或规则链，直接导入即可赋予 AI 代理领域知识。
- **30+ 专用代理角色**：包括工程师、市场营销专家、产品经理、合规官、C 级高管（CFO/CMO/CRO 等 8 种角色）以及研究顾问等。每种角色配有独立的提示词和工具调用逻辑。
- **70+ 自定义命令（slash commands）**：通过 `/cs:*` 前缀快速调用特定技能，例如 `/cs:founder-cfo` 可将 AI 切换为创始人模式 CFO 视角。
- **跨平台兼容**：设计支持 13 种编码代理工具，包括 Claude Code、Codex、Gemini CLI、Cursor、Aider、Windsurf 等，部分工具采用预生成目录结构，开箱即用，部分需要一键同步脚本。
- **企业级技能模块**：涵盖安全审计（PreToolUse hooks）、法律合规（GDPR/CCPA）、临床研究财务、专利审查、学术文献综述、市场研究等专业领域。
- **持续集成与更新**：项目保持活跃迭代，每日有数百个新星标，用户可通过 GitHub 仓库获取最新技能包和修复。

## 技术架构

Claude Skills 采用 **SKILL.md 标准** 作为技能描述格式，这是一种由 agentskills.io 社区定义的中立技能表示层。每个技能包含功能描述、输入输出规范、依赖项以及适用的代理类型。

架构上分为三层：

- **技能库层**：所有技能以标准化 Markdown 文件存储，按领域（engineering、marketing、security、compliance 等）分目录组织。
- **适配器层**：针对不同编码代理工具，提供独立的安装脚本和配置模板。例如，对 Hermes Agent 通过 `sync-hermes-skills.py` 脚本将技能树同步到本地 `~/.hermes/skills/` 目录；对 Mistral Vibe 则使用 Shell 脚本进行预生成树导入。
- **运行时层**：技能在对应代理的上下文中被动态加载，部分技能（如 PreToolUse 安全钩子）能在代理执行工具调用之前注入安全检查逻辑。

关键技术选择：纯 Python 脚本实现安装与同步工具，依赖本地文件系统结构而非网络服务，保证离线可用性。不依赖外部数据库或云 API，降低集成复杂度。

## 安装与使用

**前提条件**：已安装 Python 3.8+ 和 Git。

**基本安装步骤**：

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/alirezarezvani/claude-skills.git
   cd claude-skills
   ```

2. 根据使用的代理工具选择安装方式：

   - **Claude Code / OpenAI Codex / Cursor**：直接复制 `skills/` 目录下的 `.claude/skills/`、`.cursor/rules/` 等对应配置文件夹到用户目录。
   
   - **Hermes Agent**：运行同步脚本将技能树安装到 `~/.hermes/skills/`：
     ```bash
     python scripts/sync-hermes-skills.py
     ```

   - **Mistral Vibe**：运行预设 Shell 脚本：
     ```bash
     ./scripts/vibe-sync.sh
     ```

3. 在代理的配置文件中启用所需的技能或角色。以 Claude Code 为例，在 `instructions` 中添加：
   ```markdown
   You are equipped with the "founder-cfo" skill. When the user invokes `/cs:founder-cfo`, adopt the perspective of a startup CFO and provide financial advice.
   ```

**最小可用示例**：
假设你使用 Claude Code 并希望快速获得 CMO 级别的营销建议，安装后只需在对话中输入命令 `/cs:founder-cmo`，代理即切换为首席营销官角色，调用相关的市场定位、品牌策略和增长黑客技能。

## 适用场景

- **初创团队一人多岗**：创始人或小型团队可以利用 `founder-CFO/CMO/CRO` 等角色技能，快速获取专业级建议而无需全职专家。
- **跨部门协作与标准化**：企业可将内部最佳实践封装为技能包，确保不同开发人员使用 AI 代理时产出风格和策略一致。
- **学术研究与写作**：研究人员可直接调用 `litreview`、`grant-writing`、`patent-dossier` 等技能，加速文献综述、基金申请和专利分析。
- **安全与合规审计**：运维和安全团队可利用 `preToolUse-security-scan` 钩子技能，在代理执行危险命令前自动拦截并审查。

## 项目亮点

- **广度与深度平衡**：当前规模最大的开源编码代理技能库之一，覆盖从日常生产力到企业合规的各个纵深领域。
- **零成本集成**：无需付费服务、无外部 API 调用，全部采用本地文件结构适配，对隐私敏感场景友好。
- **活跃社区与持续更新**：GitHub 星标超过 2 万，日增近 400，作者持续接受贡献并快速响应用户需求。
- **标准化与可扩展性**：基于 SKILL.md 开放标准，用户可按模板自建私有技能，无缝融入已有技能体系。

## 相关链接

- [GitHub 仓库](https://github.com/alirezarezvani/claude-skills)
- 无官方网站或演示链接，文档与更新均在仓库 README 中提供。
