---
tags:
  - trending
  - article
repo: cloudflare/security-audit-skill
date: 2026-09-18
language: JavaScript
stars_total: 11257
stars_today: 3607
---
## 项目概述

`security-audit-skill` 是 Cloudflare 开源的一个编码智能体技能（coding-agent skill），用于将通用编码智能体改造为具备多阶段流程的安全审计工具。它针对的核心问题是：直接让大模型"审查代码找漏洞"往往产出不可靠、不可复现、难以验证的结论，且缺乏对审计覆盖面的量化管理。本项目通过把安全审计拆解为六个相互隔离的阶段，并引入独立的记录校验环节，让每一条漏洞结论都能追溯到具体的代码证据与验证过程。

该技能最初用于构建 Cloudflare 内部的漏洞发现平台（vulnerability harness），后续演化为跨仓库、舰队级的多阶段系统，而本仓库保留的是其最初的单仓库形态。目标用户包括安全工程师、红队成员、代码审计人员，以及希望在 CI 或本地工作流中引入自动化安全审查的开发团队。

## 核心功能

- **六阶段结构化审计流程**：依次执行侦察、覆盖驱动的漏洞狩猎、候选验证、结构化输出、独立记录校验、目标无关报告生成，避免一次性"黑盒"扫描。
- **覆盖台账（coverage ledger）管理**：在侦察阶段生成 `coverage-ledger.json`，把系统拆解为独立的审计单元，并据此分派隔离的 hunter 智能体，减少重复与遗漏。
- **对抗式候选验证**：每一个候选漏洞都会交给一个全新的 verifier 智能体，其任务是尝试证伪该候选，而非确认它，从而过滤假阳性。
- **机器可读的结构化输出**：结果写入 `findings.json`，分为 `confirmed`、`needs_validation`、`rejected` 三类，并按 `report-schema.json` 进行模式校验。
- **独立记录校验**：由新的智能体核验最终记录中的源码引用，对被替换过的关键结论再派第二个独立验证者复核。
- **目标无关的报告生成**：从已校验的记录与覆盖数据自动派生 `REPORT.md`、`FINDINGS-DETAIL.md`、`NEEDS-VALIDATION.md`，不依赖特定项目结构。

## 技术架构

项目以 JavaScript 实现，本质上是一组供编码智能体调用的技能定义、阶段编排逻辑与 JSON Schema 规范，而非独立运行的扫描器。设计上遵循三条原则：

一是**隔离性**——狩猎、验证、记录校验分别由不同的智能体实例执行，避免同一上下文中的确认偏差相互污染；二是**可追溯性**——侦察阶段的架构描述、覆盖单元、候选记录、最终结论以文件形式逐层落盘，形成完整的证据链；三是**模式约束**——所有中间产物都有明确的文件格式（如 `architecture.md`、`coverage-ledger.json`、`findings.json`），并由 JSON Schema 强制校验，便于机器消费与后续集成。

整体架构可以理解为"编排器 + 阶段技能 + 校验规则"，编排器负责阶段推进与产物交接，各阶段技能负责具体工作，校验规则保证数据在阶段之间不失真。

## 安装与使用

典型使用方式是将本仓库作为技能目录挂载到支持技能的编码智能体（如 Claude Code 等）中。基本步骤：

1. 克隆仓库到本地：

   ```bash
   git clone https://github.com/cloudflare/security-audit-skill.git
   ```

2. 在智能体的技能配置中指向该目录，使其能够加载 `security-audit` 技能定义。

3. 在待审计的目标仓库中启动该技能，智能体会按顺序推进六个阶段，并在工作目录下生成 `architecture.md`、`coverage-ledger.json`、`findings.json`、`REPORT.md` 等文件。

4. 审计结束后，可直接读取 `findings.json` 做后续处理，例如导入缺陷跟踪系统；对 `needs_validation` 类别的记录，建议人工复核后再决定处置方式。

由于项目依赖智能体运行环境，具体命令与配置项请以仓库 README 与技能定义文件为准。

## 适用场景

- **多仓库/单体仓库的定期安全巡检**：通过覆盖台账确保每次审计的覆盖面可量化、可对比。
- **代码合并前的安全把关**：对涉及认证、输入解析、权限边界等高风险改动的模块做针对性审计。
- **漏洞发现流程的方法论落地**：团队希望把"确认—证伪—复核"的流程标准化，而非依赖个人经验。
- **安全研究中的证据留存**：需要机器可读、可追溯到具体源码位置的发现记录，用于报告或复现。

## 项目亮点

与常见的"让模型直接扫代码"或传统的静态分析工具相比，本项目的主要差异在于：验证环节采用**证伪导向**，由独立智能体主动尝试推翻候选结论；同时，最终记录会再经独立智能体核对源码，形成双重校验。此外，覆盖台账将审计完整性显式建模，弥补了黑盒扫描"找不到就等于没有"的盲区。项目由 Cloudflare 在生产环境中演化而来，具备真实的工程背景与方法论沉淀。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/security-audit-skill)
- [Build your own vulnerability harness（Cloudflare 博客）](https://blog.cloudflare.com/build-your-own-vulnerability-harness)
