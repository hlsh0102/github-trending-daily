---
tags:
  - trending
  - article
repo: alirezarezvani/claude-skills
date: 2026-07-07
language: Python
stars_total: 21302
stars_today: 610
---
## 项目概述

Claude Skills & Plugins 是一个开源的、面向 AI 编码代理的技能与插件库。该项目提供了 355 个生产级技能，涵盖工程、DevOps、营销、安全、合规、高管咨询、生产力、学术研究、企业研究运营等多个领域。它不仅适用于 Claude Code，还兼容 OpenAI Codex、Gemini CLI、Cursor、Aider、Windsurf 等 13 种主流 AI 编码工具，是目前最全面的开源技术与业务代理技能集合。

目标是让使用者无需重复编写提示词或配置规则，就能直接获得一个经过实战检验的“AI 编码助手技能库”，覆盖从日常开发到高管决策支持的广阔场景。

## 核心功能

- **丰富的预置技能集合（355+）**：包含 30 多个专用代理、70 多条自定义命令、330 多个可复用技能，以及可自定义的参考文档与脚本，覆盖技术与非技术场景。
- **多代理适配**：项目技能全部遵循统一的 SKILL.md 与 agentskills.io 规范。原生适配 Claude Code、Codex、Gemini CLI 等工具，对于 Hermes Agent、Mistral Vibe 等工具提供“BYO-sync”同步机制，无需格式转换即可使用。
- **多维角色与命令**：包含 10 组高管顾问角色（CFO、CMO、CRO、CPO、COO、CHRO、CISO、GC、CDO、CAIO、CCO、VPE），提供 21 条 `/cs:*` 斜杠命令，例如 `/cs:founder-finance`、`/cs:growth-advice`、`/cs:compliance-review`。
- **高效提示系统**：内置多种提示策略，例如“一次性生成所有测试”、“无限循环保护”、“进度条反馈”、“清晰的行内错误信息”等，提升开发效率与交互体验。
- **实用脚本支持**：提供 python 脚本用于技能目录的自动同步与部署，同时支持灵活的自定义参考文档引用，满足团队协作需求。

## 技术架构

项目以 **agentskills.io SKILL.md 标准**作为核心规范，所有技能均以独立的 Markdown 文件形式存放于 `skills/` 目录下，并通过分层的目录结构（如 `skills/engineering/`、`skills/marketing/`、`skills/compliance/`、`skills/c-suite/` 等）实现分类管理。

- **适配器层**：项目为不同的 AI 编码工具实现了适配逻辑。原生工具（Claude Code、Codex、Cursor 等）可自动识别技能目录；对于需要手动同步的工具（如 Hermes Agent、Mistral Vibe），项目提供了预生成的技能树及一键同步脚本，例如 `scripts/sync-hermes-skills.py`，避免用户手动处理格式对齐。
- **设计决策**：优先采用“一次编写，多处运行”的理念，确保相同技能在不同工具下行为一致。同时提供丰富的可配置 `config.json` 与自定义引用机制，让用户能在不修改技能核心文件的前提下调整参数。
- **性能与可扩展**：项目本身以 Python 编写，脚本依赖标准库，跨平台兼容。技能数量虽多但采用扁平化文件结构，加载效率高，易于贡献者添加新技能。

## 安装与使用

**前提条件**：确保您已安装 Python 3.8 或更高版本，并拥有了可用的 AI 编码工具（如 Claude Code CLI 或 Codex CLI 等代理）。

**安装步骤**:

1. **克隆仓库**：
   ```bash
   git clone https://github.com/alirezarezvani/claude-skills.git
   cd claude-skills
   ```

2. **安装技能（以 Claude Code 为例）**：
   将 `skills/` 目录中的内容复制到 Claude Code 的扩展目录（`~/.claude/skills/`）下：
   ```bash
   mkdir -p ~/.claude/skills
   cp -r skills/* ~/.claude/skills/
   ```

   或者，为支持通过脚本自动同步，可运行：
   ```bash
   python scripts/install-skills.py
   ```

3. **使用技能**：
   启动您的 AI 编码代理（例如 CLI 对话），即可直接通过提示词引用技能名称（如 `/cs:devops-audit` 或 `[skill:engineering-code-review]`）。

**最小可用示例**：

运行一个简单的工程代码审查技能：
```bash
claude-code
# 在与代理的对话中输入:
# 使用技能 [skill:engineering-code-review] 审查当前项目代码中的安全问题。
# 代理会自动加载对应技能文件，并指导审查流程。
```
更丰富的场景可以通过 `/cs:*` 系列斜杠命令直接调用高管顾问角色。

## 适用场景

- **工程团队日常与代码开发**：开发者可快速调用代码审查、安全扫描、架构建议等 80+ 技能，提升编码质量和效率，尤其适合多人协作项目及 CI/CD 流程中的自动化审查。
- **营销与 AEO（答案引擎优化）**：营销人员可借助专门的 AEO 技能（技能列表中有标注 `marketing-aeo`），针对大型语言模型（LLM）的引用机制优化内容，提升品牌在 AI 回答中的可见性。
- **高管决策支持与合规审查**：CEO/CFO 等角色可使用 `/cs:founder-finance` 等命令，快速获取财务模型建议、合规风险评估、组织架构优化等顾问级别的分析。适合创业者、高级管理者在无顾问团队时使用。
- **学术研究与企业研究运营**：研究团队可使用 litreview、grants、patent、dossier、pulse 等技能，系统化地管理文献综述、项目申请、专利查新、产品脉冲调研，并通过 hybrid router 智能路由到最合适的技能模块。

## 项目亮点

- **技能规模与覆盖广度**：目前是 GitHub 上最全面的 AI 编码代理技能库（355+），覆盖从开发到商业战略的完整链条，远超同类项目通常只聚焦技术或某一领域。
- **标准化与多工具兼容**：所有技能严格遵循 SKILL.md 规范，无需改造即可在 13 种不同 AI 编码工具之间无缝迁移，极大降低了用户切换工具时的学习成本。
- **生产级与实用主义设计**：技能均为生产级，经过真实场景测试。例如“无限循环保护”、“进度条反馈”、“行内错误信息”等设计，直接解决日常编码中常见的痛点问题，而非停留在理论概念。
- **持续更新与社区贡献驱动**：项目仍在活跃更新（包含 v2.9.0 等版本），且通过 MIT 许可鼓励社区贡献。用户可以直接从 GitHub Issues 或 Discussions 中提出需求或提交新技能。

## 相关链接

- [GitHub 仓库](https://github.com/alirezarezvani/claude-skills)
- [agentskills.io 标准](https://agentskills.io)
