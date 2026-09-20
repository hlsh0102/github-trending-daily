---
tags:
  - trending
  - article
repo: cloudflare/security-audit-skill
date: 2026-09-20
language: JavaScript
stars_total: 16984
stars_today: 3155
---
## 项目概述

`security-audit-skill` 是 Cloudflare 开源的一个编码代理（coding-agent）技能包，用于将通用 AI 编程代理转变为结构化安全审计工具。它解决的是一类常见问题：让代理单线程地"扫一遍代码、报告漏洞"往往会产生大量重复、无法复现、真假混合的发现，既难以验证也难以复用。该项目通过多阶段、多代理隔离协作的方式，把审计过程拆分为侦察、覆盖驱动的漏洞搜寻、候选验证、结构化输出、独立记录校验和面向目标无关的报告生成六个阶段，从而产出经过独立确认、机器可读的审计结果。

目标用户包括安全工程团队、希望在 CI 或本地流程中引入自动化审计的开发者，以及想借鉴多代理协作模式构建自有漏洞发现流水线的团队。项目源自 Cloudflare 的漏洞发现框架（Vulnerability Discovery Harness），该框架后来发展为覆盖全公司多仓库的多阶段系统，而本仓库正是其演进的单一仓库起点。

## 核心功能

- **六阶段审计流程**：将审计拆分为侦察、覆盖驱动搜寻、候选验证、结构化输出、独立记录验证和目标中立报告六个阶段，每个阶段有明确的输入输出产物。
- **覆盖台账（Coverage Ledger）**：在侦察阶段生成 `architecture.md` 与 `coverage-ledger.json`，把攻击面、信任边界、输入入口和既有证据映射为可追踪的工作单元，避免遗漏。
- **隔离式猎手与批判者**：基于台账单元分配独立的搜寻代理，并由"覆盖批判者"代理反向检查是否存在未被覆盖的盲区。
- **反证式候选验证**：每个唯一候选漏洞交由一个全新的验证代理尝试推翻，减少误报。
- **结构化发现输出**：将结果按照 `confirmed`、`needs_validation`、`rejected` 三类写入 `findings.json`，并使用 `report-schema.json` 进行模式校验。
- **独立记录复核与多格式报告**：由全新代理验证最终源码主张，并据此生成 `REPORT.md`、`FINDINGS-DETAIL.md` 和 `NEEDS-VALIDATION.md`。

## 技术架构

项目使用 JavaScript 实现，整体设计围绕"代理隔离"与"可验证性"两条主线。其核心思路是将一个模糊的安全审计任务分解为可独立执行的原子步骤，每一步由状态干净的新代理承担，避免上下文污染和确认偏误在同一个代理内累积。所有中间产物均落盘为文件（Markdown 与 JSON），使审计过程可重放、可审计、可 diff。

数据流上，侦察阶段产生架构与覆盖台账，搜寻阶段依据台账生成候选，验证阶段对候选做反证，随后写入符合 JSON Schema 的发现记录，再经过第二层独立复核，最后由报告生成阶段读取已确认记录派生人类可读文档。报告中不会硬编码特定目标信息，因此同一套产物可以适配不同仓库和不同报告模板。

## 安装与使用

由于项目以"技能"形式提供，通常需要放置于支持技能机制的编码代理环境中。一般流程如下：

```bash
git clone https://github.com/cloudflare/security-audit-skill.git
cd security-audit-skill
```

随后将技能目录注册到你的代理配置中（视代理实现不同，方式可能是复制到技能目录、在配置文件中声明路径，或作为子模块引入）。最小可用示例是让代理对目标仓库执行一次完整审计：

```text
使用 security-audit 技能，对当前仓库执行一次完整审计
```

代理会依次产出 `architecture.md`、`coverage-ledger.json`、`findings.json`、`REPORT.md`、`FINDINGS-DETAIL.md` 和 `NEEDS-VALIDATION.md`。建议在运行前确认代理拥有读取目标仓库源码的权限，并在审计后将 `findings.json` 与 `report-schema.json` 对照校验，以确保输出格式正确。

## 适用场景

- **开源或内部代码库的安全自检**：在合并前对关键模块执行结构化审计，获得可追踪的发现清单。
- **CI/CD 中的安全门禁**：将 `findings.json` 作为机器可读输入，接入流水线做自动判定。
- **构建自定义漏洞发现流水线**：作为多代理协作审计的最小可用参考实现，扩展到多仓库场景。
- **安全研究与教学**：用于演示覆盖驱动搜寻、反证式验证等审计方法论。

## 项目亮点

与常见的"让代理跑一遍扫描器"的做法相比，该项目的差异化在于将审计过程工程化：一是通过覆盖台账把"审计是否完整"变成可检查的问题；二是用全新代理对新候选进行反证，显著降低误报；三是对最终记录再做一层独立验证，形成双重校验链路；四是所有产物均为可落盘、可 schema 校验的结构化文件，便于自动化消费与审计追踪。此外，它来自 Cloudflare 实际运行的大规模漏洞发现框架，方法论经过生产环境检验，而非一次性演示脚本。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/security-audit-skill)
- [Build your own vulnerability harness（Cloudflare 博客）](https://blog.cloudflare.com/build-your-own-vulnerability-harness)
