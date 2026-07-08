---
tags:
  - trending
  - article
repo: AhmadIbrahiim/Website-downloader
date: 2026-07-08
language: HTML
stars_total: 4192
stars_today: 140
---
## 项目概述

Complete Website Downloader 是一个基于 Node.js 的开源工具，旨在帮助用户一键下载任何网站的完整源代码，包括所有资产文件（如 JavaScript 脚本、CSS 样式表和图片）。该项目通过封装 `wget` 和 `archiver` 库，将网页抓取与文件压缩功能集成到统一的 Node.js 服务中，最终通过 Socket 通道将压缩包实时发送给用户。

对于需要离线保存网页、迁移网站内容、或研究前端构建方式的开发者、设计师和普通用户而言，这个项目提供了一个简单、高效的网页抓取解决方案。它解决了传统手动保存网页时无法批量下载完整资源（如依赖的字体、图片和脚本）的问题。

## 核心功能

- **全站镜像下载**：使用 `wget --mirror` 参数递归下载整个网站，保留原始目录结构。
- **链接转换**：自动将网页中的绝对链接转换为相对链接，确保离线浏览时样式和脚本正常加载。
- **文件扩展名修正**：根据文件的实际内容类型（如 HTML 或 CSS）自动添加或修正文件扩展名，避免缺失后缀。
- **页面必需资源抓取**：下载 CSS 样式表、图片、JavaScript 等页面渲染所必需的资源，确保离线版完整显示。
- **目录限制**：通过 `--no-parent` 参数限制递归范围，防止抓取超出目标网站范围的上级目录。
- **实时压缩交付**：抓取完成后使用 `archiver` 将所有文件打包为压缩包，并通过 WebSocket 实时推送下载链接。

## 技术架构

项目采用 Node.js 作为运行时环境，核心依赖为 `wget` 和 `archiver`。整体架构分为三个模块：

1. **任务接收层**：通过 Web 界面或 API 接口接收用户提交的网址。
2. **抓取执行层**：调用系统 `wget` 命令并传入预设参数（如 `--mirror`、`--convert-links`、`--adjust-extension`、`--page-requisites`、`--no-parent`），将目标网站镜像抓取到临时目录。
3. **压缩发送层**：抓取完成后，`archiver` 将临时目录中的所有文件压缩为 `.zip` 文件，然后通过 WebSocket 实时通知用户并提供下载。

设计上，项目采用 **任务队列 + 回调通知** 模式，支持异步处理大文件网站。前端界面采用简洁的输入框和进度条，后端通过进程管理和错误处理确保稳定性。此外，项目兼容多个云平台部署（如 Replit、Glitch、Railway、Cyclic、Koyeb），方便用户快速启动。

## 安装与使用

### 安装步骤

1. 确保系统中已安装 **Node.js**（v12 及以上）和 **wget**（Linux/macOS 通常自带，Windows 需安装或使用 WSL）。
2. 克隆仓库并安装依赖：
```bash
git clone https://github.com/AhmadIbrahiim/Website-downloader.git
cd Website-downloader
npm install
```
3. 启动服务：
```bash
npm start
```
4. 浏览器打开 `http://localhost:3000` 即可使用。

### 最小可用示例

1. 在页面的输入框内填写目标网址，例如 `https://example.com`。
2. 点击“Download”按钮。
3. 等待进度条显示完成，系统会返回包含所有资产文件（HTML、CSS、JS、图片等）的压缩包。
4. 下载并解压后，可直接双击 HTML 文件离线浏览。

## 适用场景

- **离线存档**：需要保存个人博客、技术文档或教程类网站，以便无网络时阅读。
- **网站迁移**：将旧网站静态内容迁移到本地或新服务器，无需逐页手动复制。
- **前端学习**：研究优秀网站的 HTML 结构、CSS 布局和 JS 交互逻辑，下载完整版便于本地调试。
- **内容备份**：对重要企业官网或项目展示页进行定期备份，防止原站突然下线。

## 项目亮点

- **全自动化流程**：用户只需输入网址，系统自动完成抓取、打包、交付全流程，无需任何技术操作。
- **基于成熟工具**：依托 `wget` 稳定的抓取能力（支持递归、链接转换等），同时用 `archiver` 实现高效压缩，可靠性高。
- **零配置部署**：支持一键部署到 Replit、Glitch、Railway 等主流云平台，无需复杂服务器配置。
- **实时反馈**：通过 WebSocket 实时显示下载进度，用户可清楚知道当前抓取状态和剩余时间。
- **开源免费**：采用 MIT 许可证，代码完全透明，可任意修改或集成到其他项目。

## 相关链接

- [GitHub 仓库](https://github.com/AhmadIbrahiim/Website-downloader)
- [在线演示](https://website-downloader.onrender.com)
