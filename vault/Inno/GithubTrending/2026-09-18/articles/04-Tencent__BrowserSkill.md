---
tags:
  - trending
  - article
repo: Tencent/BrowserSkill
date: 2026-09-18
language: TypeScript
stars_total: 4624
stars_today: 1302
---
## 项目概述

BrowserSkill 是由腾讯开源的一款浏览器自动化工具，定位为连接 AI Agent 与用户真实浏览器的桥梁。它由 CLI 工具与浏览器扩展两部分组成，核心目标是让 AI Agent 直接操作用户已经登录的浏览器，而无需为自动化任务单独准备测试账号或隔离环境。

传统浏览器自动化方案（如 Playwright、Puppeteer）通常需要启动一个全新的无痕浏览器实例，这意味着所有登录态、Cookie、会话信息都不复存在，Agent 必须重新走一遍登录流程，遇到验证码、双因素认证时往往直接卡死。BrowserSkill 换了一个思路：它并不新建浏览器，而是以“借用标签页”的方式接入用户当前的浏览器会话。Agent 需要操作某个已打开的标签页时，必须显式借入，任务结束后归还，其余标签页不受影响。

目标用户是已经在使用 Cursor、Claude Code、Codex、OpenClaw、CodeBuddy、WorkBuddy、Pi、Hermes Agent、DeepSeek Harness 等 AI 编码或通用 Agent 的开发者。只要 Agent 具备执行 shell 命令的能力，就能通过 `bsk` 命令驱动浏览器。

## 核心功能

- **复用真实登录状态**：Agent 直接使用用户已登录的站点，不需要额外创建测试账号或反复输入凭据，对内部系统、需登录后台等场景尤为实用。
- **不打断用户工作**：浏览器任务运行在独立的、可见的 Agent Window 中，用户可以在同一浏览器内继续自己的操作，两边互不干扰。
- **跨 Agent 通用**：通过 `bsk` CLI 暴露能力，任何能调用 shell 的 Agent 都可以接入，不绑定特定模型、Agent 框架或运行环境。
- **内置 Human-in-the-loop**：当任务遇到验证码、登录、确认弹窗等只能由人完成的步骤时，Agent 可以请求用户接管，用户处理完成后 Agent 继续执行后续流程。
- **显式标签页借用机制**：Agent 必须明确借入某个标签页，任务结束归还，避免越权操作其它页面。
- **整页截图与页面输出**：支持通过 Quick actions 或 `bsk screenshot --session <id> --full-page --out page.png` 等方式抓取整页截图，便于 Agent 获取完整页面视觉信息。

## 技术架构

项目使用 TypeScript 编写，整体分为三个层次：

1. **浏览器扩展**：运行在用户已登录的浏览器中，负责管理标签页的借入与归还、在独立 Agent Window 中执行操作，以及向用户呈现需要人工介入的提示。
2. **`bsk` CLI**：作为 Agent 与扩展之间的通信入口，提供截图、会话管理等命令。Agent 通过 shell 调用 CLI，CLI 再与扩展建立连接，从而间接控制浏览器。
3. **会话模型**：每个任务对应一个 session，Agent 在会话上下文中借用标签页；任务结束后会话释放，标签页回到用户控制。

这种分层的设计使得 Agent 侧不需要理解浏览器协议的细节，只需要按 CLI 约定发起命令即可；同时扩展层保留了可见性与用户接管能力，符合“人在回路”的自动化原则。

## 安装与使用

基本步骤通常如下（具体命令以仓库文档为准）：

1. 从 GitHub 仓库安装 `bsk` CLI（例如通过 npm 或仓库提供的安装脚本）。
2. 在浏览器中安装对应的 BrowserSkill 扩展。
3. 确认扩展已与 CLI 建立连接。

最小可用示例：让 Agent 对一个已登录的页面执行整页截图。

```bash
bsk screenshot --session <id> --full-page --out page.png
```

Agent 侧的典型流程是：先请求借入一个标签页，得到 session id；在 session 内执行导航、点击、截图等操作；完成后归还标签页。遇到验证码或登录确认时，扩展会提示用户接管，用户处理完毕后 Agent 继续执行。

## 适用场景

- **需登录后台的自动化**：企业内部管理系统、CRM、运营后台等无法用测试账号覆盖的场景，直接用已登录会话操作。
- **需要人工介入的流程**：例如触发短信验证码、图形验证码、二次确认的操作，交给用户处理后再继续。
- **边工作边自动化的并行场景**：用户在同一浏览器中处理自己的工作，Agent 在独立 Agent Window 中执行任务，互不抢占。
- **页面信息抓取与截图归档**：Agent 抓取完整页面截图或读取页面状态，用于生成报告、调试或记录。

## 项目亮点

与 Playwright、Puppeteer 这类需要在全新浏览器实例中重建上下文的方案相比，BrowserSkill 的核心差异在于**复用真实登录态**和**非侵入式借用**：它不要求用户为自动化单独维护一套账号体系，也不强制打断当前浏览行为。同时，通过 CLI 抽象，它避免了与特定 Agent 框架的强绑定，只要 Agent 能跑 shell 就能接入。内置的 human-in-the-loop 机制则弥补了自动化在验证码、登录等环节的天然短板，让 Agent 能在真实环境下更完整地完成任务链路。

## 相关链接

- [GitHub 仓库](https://github.com/Tencent/BrowserSkill)
- [项目 Banner 与演示视频](https://github.com/Tencent/BrowserSkill#readme)
