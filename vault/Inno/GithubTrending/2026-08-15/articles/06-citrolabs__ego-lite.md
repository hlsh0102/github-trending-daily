---
tags:
  - trending
  - article
repo: citrolabs/ego-lite
date: 2026-08-15
language: JavaScript
stars_total: 10406
stars_today: 165
---
## 项目概述

ego-lite 是一款专为 AI 代理设计的极速浏览器，旨在解决 AI 代理在执行浏览器自动化任务时的核心痛点：登录态共享与性能开销。当前，像 Codex、Claude Code 这样的编程代理在需要访问网页时，往往面临两种困境——要么通过浏览器自动化框架从零开始处理登录流程，频繁遭遇验证码、双因素认证等障碍；要么依赖云端浏览器，不仅成本高昂，还需将敏感凭证托管到第三方服务。

ego-lite 提供了一种零成本、零配置的本地解决方案：它将你日常使用的浏览器状态（包括登录会话、Cookie、本地存储等）直接共享给 AI 代理，让代理可以像你本人一样直接访问已登录的网站，全程无需打扰你的正常操作，也无需任何额外的付费服务。项目采用 MIT 许可证开源，自发布以来迅速获得超过 10000 颗 Star，成为 AI 代理工具链中备受关注的基础设施组件。

## 核心功能

- **登录态无缝共享**：自动将你当前浏览器中的会话信息传递给 AI 代理，代理可直接访问 Gmail、GitHub、Notion 等需要认证的服务，无需重复登录。
- **零配置启动**：安装后无需任何设置即可使用，代理环境变量配置完成后即可开始自动化任务，省去复杂的 WebDriver 或 CDP 连接配置。
- **极致性能表现**：针对 AI 代理的调用模式做了专门优化，启动速度和页面加载速度均显著优于通用浏览器，减少代理每次操作间的等待时间。
- **无打扰运行**：浏览器在后台静默运行，不会弹出窗口、不会抢占焦点，你可以在前台继续自己的工作，互不干扰。
- **本地数据存储**：所有会话数据均保存在本机，不经过任何云端服务器，确保账号安全和隐私可控。
- **多代理兼容**：支持 Codex、Claude Code 等主流 CLI 编程代理，通过标准环境变量即可接入。

## 技术架构

ego-lite 基于 JavaScript/TypeScript 构建，核心设计思路是"最小化浏览器引擎 + 会话共享机制"。项目并未采用传统浏览器的完整庞杂架构，而是专注于 AI 代理所需的自动化执行环境，剥离了用户界面、扩展系统等非必要组件，从而获得显著的性能提升。

在会话共享方面，ego-lite 利用了 Chromium 系的用户数据目录（user-data-dir）机制。当你日常使用的 Chrome/Edge 浏览器关闭后，ego-lite 会以相同的用户数据目录启动自己的浏览器实例，从而继承所有已登录的会话状态。这一设计巧妙地绕开了 Cookie 手动导出的局限，也避免了 Selenium 等工具中常见的登录态丢失问题。

此外，项目提供了轻量级的 HTTP 控制接口，AI 代理可通过标准的 CDP（Chrome DevTools Protocol）或自定义的简化 API 与其通信。代码库保持了高度的模块化，核心引擎与代理适配层分离，使得未来扩展更多 AI 工具支持变得容易。

## 安装与使用

**安装步骤**：

1. 前往 [Releases 页面](https://github.com/citrolabs/ego-lite/releases) 下载对应平台（Apple Silicon 或 Intel）的 dmg 安装包。
2. 拖拽安装到 Applications 文件夹，首次打开时在系统设置中允许来自 unidentified developer 的应用运行。
3. （可选）保持你日常使用的 Chrome 登录状态，然后完全退出 Chrome 浏览器。

**与 AI 代理集成**：

在 Codex 或 Claude Code 的项目配置中，添加以下环境变量指向 ego-lite 的可执行文件：

```bash
export EGO_LITE_PATH=/Applications/ego-lite.app/Contents/MacOS/ego-lite
```

然后直接调用浏览器工具即可。例如在 Codex 中：

```bash
codex "打开 GitHub 仓库页面，将 star 数截图保存"
```

ego-lite 会自动启动，使用你已登录的 GitHub 会话完成操作，并将结果返回给代理。整个过程无需输入密码或处理验证码。

## 适用场景

- **日常开发自动化**：开发者在本地使用 Codex 或 Claude Code 编写代码时，需要让代理查询内部文档、提交 Issue、操作测试环境，ego-lite 能让代理直接使用你的公司 SSO 登录态完成这些操作。
- **数据采集与监控**：针对需要登录才能访问的数据源（如社交媒体后台、金融账户），ego-lite 可帮助 AI 代理稳定地抓取数据，避免因会话过期导致的任务中断。
- **零成本 RPA 替代**：个人用户希望自动化一些重复的网页操作（如自动签到、表单填写），却不想为云端 RPA 服务付费，ego-lite 提供了一条完全本地、无订阅费用的路径。

## 项目亮点

- **真正的零成本**：不同于 Playwright 云服务或 Browserless 等按量计费方案，ego-lite 完全免费且开源自托管，无任何隐藏费用。
- **极低的学习曲线**：没有复杂的 YAML 配置，没有需要管理的 Docker 容器，下载即用，集成到现有代理工具链只需一行环境变量。
- **性能代差**：在 AI 代理多轮对话的场景下，ego-lite 的启动时间和响应速度带来质的提升，减少 token 消耗和等待时间。
- **隐私友好架构**：所有数据本地处理，不经过第三方中继服务器，适合处理敏感业务数据的场景。
- **社区活跃度高**：项目在 Trendshift 上排名靠前，Discord 社区活跃，迭代速度快，能够及时适配新的 AI 代理工具。

## 相关链接

- [GitHub 仓库](https://github.com/citrolabs/ego-lite)
- [官方文档](https://lite.ego.app/document/)
- [Discord 社区](https://discord.gg/5eGZVvHbTq)
- [关注 X / Twitter](https://x.com/ego_agent)
