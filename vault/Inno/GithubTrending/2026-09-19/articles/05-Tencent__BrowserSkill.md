---
tags:
  - trending
  - article
repo: Tencent/BrowserSkill
date: 2026-09-19
language: TypeScript
stars_total: 5482
stars_today: 1306
---
## 项目概述

BrowserSkill 是由腾讯开源的浏览器自动化工具，旨在让 AI Agent 直接复用用户已经登录的真实浏览器，而不是启动一个干净的、需要重新登录的无头实例。它由 CLI（`bsk`）与浏览器扩展两部分组成，任何能够调用 shell 的 AI Agent 都可以通过命令行接入。

项目解决的核心痛点有两个。其一，传统的浏览器自动化方案（如 Playwright、Puppeteer）通常需要独立配置账号、Cookie 和登录态，面对验证码、双因素认证时容易中断。其二，当 Agent 占用浏览器执行任务时，用户往往无法同时使用自己的浏览器，工作被迫中断。BrowserSkill 通过"借用标签页"的显式协议来规避这两个问题：Agent 必须明确声明要操作哪个已打开的标签页，任务完成后归还，其余标签页不受影响。

目标用户包括使用 Cursor、Claude Code、Codex、OpenClaw、CodeBuddy 等编码或通用 Agent 的开发者，以及希望将浏览器操作能力接入自有 Agent 框架的团队。

## 核心功能

- **复用真实登录态**：Agent 直接操作你已登录的站点，无需创建独立的测试账号或复制 Cookie。
- **任务隔离不打断工作**：浏览器操作在独立的可见 Agent Window 中执行，用户可以继续正常使用自己的浏览器。
- **跨 Agent 通用**：通过 `bsk` CLI 暴露能力，不绑定特定模型、Agent 框架或运行环境，只要 Agent 能执行 shell 命令即可调用。
- **内建 Human-in-the-loop**：遇到验证码、登录、确认弹窗等只有人类能完成的步骤时，Agent 可以请求用户接管，用户处理完毕后任务继续。
- **显式标签页借用协议**：Agent 必须显式借用标签页，并在完成后归还，避免对用户浏览器造成干扰。
- **全页截图等快捷操作**：支持通过 Quick actions 或 `bsk screenshot --session <id> --full-page --out page.png` 抓取整页截图。

## 技术架构

项目以 TypeScript 为主要开发语言，整体分为两层：

- **CLI 层（`bsk`）**：作为 Agent 与浏览器之间的命令接口，负责会话管理、标签页借用与归还、指令下发和结果回传。Agent 通过标准 shell 调用与之交互，因此天然具备跨语言、跨框架的兼容性。
- **浏览器扩展层**：注入到用户已登录的浏览器中，负责实际执行 DOM 操作、页面导航、截图等动作，并与 CLI 保持通信。

设计上强调"最小侵入"：Agent 的每个操作都以会话（session）为单位，且必须绑定到一个被显式借用的标签页。这种约束使得多个 Agent 任务与用户自身操作可以并存，而不会互相覆盖状态。Human-in-the-loop 机制则作为一类特殊的中断状态被纳入会话生命周期，Agent 检测到需要人工介入时暂停，用户完成后恢复执行，避免任务因验证码等原因彻底失败。

## 安装与使用

基本流程如下（具体命令以官方文档为准）：

1. 在浏览器中安装 BrowserSkill 扩展，并确认扩展处于启用状态。
2. 通过 npm 或官方提供的方式安装 CLI：

   ```bash
   npm install -g browserskill
   ```

3. 在 Agent 中调用 `bsk` 命令，例如借用标签页并访问目标站点：

   ```bash
   bsk open --url https://example.com
   ```

4. 需要整页截图时：

   ```bash
   bsk screenshot --session <id> --full-page --out page.png
   ```

5. 任务完成后归还标签页，结束会话。

最小可用示例是在 Cursor 或 Claude Code 中直接让 Agent 执行上述命令，观察浏览器中 Agent Window 的动作。若遇到登录或验证码，按提示在浏览器中手动完成即可。

## 适用场景

- **需要登录态的网页操作**：如从内部管理系统导出数据、在已登录的 SaaS 后台批量操作。
- **编码 Agent 辅助调试**：让 Cursor 或 Claude Code 打开本地开发页面，检查渲染结果或抓取截图。
- **自动化测试中的交互验证**：在真实登录环境而非全新会话中验证流程。
- **个人日常任务自动化**：如整理已登录邮箱、处理需要人工确认的表单提交。

## 项目亮点

与 Playwright、Puppeteer 等从零启动浏览器的方案相比，BrowserSkill 的差异化在于"借用而非接管"：它不复制登录态，也不创建新会话，而是以显式协议使用用户现有的浏览器上下文。与各类浏览器 MCP 服务相比，它不绑定特定模型或 Agent 框架，通过 CLI 实现了更广的适配面。Human-in-the-loop 被设计为一等公民，使得涉及验证码和人工确认的任务能够继续推进，而不是直接失败。此外，MIT 许可证和活跃的社区关注度（GitHub 星标已超 5000）也降低了采用门槛。

## 相关链接

- [GitHub 仓库](https://github.com/Tencent/BrowserSkill)
