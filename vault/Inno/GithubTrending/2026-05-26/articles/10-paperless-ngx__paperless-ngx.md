---
tags:
  - trending
  - article
repo: paperless-ngx/paperless-ngx
date: 2026-05-26
language: Python
stars_total: 41453
stars_today: 176
---
## 项目概述

Paperless-ngx 是一个由社区驱动的开源文档管理系统，旨在帮助用户将纸质文档转化为可搜索的在线档案，从而减少实体纸张的依赖。它基于 Python 构建，是原 Paperless 和 Paperless-ng 项目的官方继任者，由核心开发团队共同维护。该项目特别适合需要高效管理大量纸质文档的个人用户、小型办公室或家庭用户，尤其适用于处理各类收据、合同、账单、发票等日常生活或工作中产生的文件。

## 核心功能

- **自动文档扫描与索引**：支持通过自动分类、OCR（光学字符识别）和智能标签功能，将扫描件直接转换为可搜索的电子档案。
- **全文搜索与归档**：对所有文档内容进行 OCR 识别，实现全文搜索，并支持按日期、标签、文档类型等多种维度进行归档整理。
- **Docker 化部署**：提供完整的 Docker Compose 部署方案，可轻松在 Linux、Windows 或 NAS 设备上运行，支持一键启动。
- **RESTful API 支持**：提供 RESTful API 接口，便于与第三方应用（如扫描仪驱动、自动化工作流工具）集成。
- **多用户与权限管理**：支持多用户使用，可以设置管理员、编辑者和只读用户角色，控制不同用户的访问权限。
- **文档生命周期管理**：支持文档的导入、导出、重分类、合并、删除等完整操作，并保留操作历史记录。

## 技术架构

Paperless-ngx 采用前后端分离的设计理念。后端基于 Python 的 Django 框架构建，负责文档解析、OCR 处理、标签分类、数据库管理等核心逻辑。前端使用 Angular 框架开发，提供现代化的 Web 界面。OCR 功能依赖 Tesseract OCR 引擎，支持 100 多种语言的文字识别。项目使用 PostgreSQL 数据库存储元数据，并将文档文件存储于本地文件系统或云存储中。整体架构采用 Docker 容器化部署，利用 Celery 实现异步任务队列处理，确保文档批量处理时系统响应流畅。

## 安装与使用

### 基本安装步骤（Docker 方式）

1. **准备环境**：确保系统已安装 Docker 和 Docker Compose（v2 或更高版本）。
2. **克隆仓库并配置环境变量**：
   ```bash
   git clone https://github.com/paperless-ngx/paperless-ngx.git
   cd paperless-ngx
   cp docker-compose.env.example docker-compose.env
   ```
   编辑 `docker-compose.env` 文件，设置 `PAPERLESS_SECRET_KEY` 和 `PAPERLESS_URL` 等必要参数。
3. **启动服务**：
   ```bash
   docker compose up -d
   ```
   等待容器初始化完成（首次启动可能需要几分钟以更新数据库和执行迁移）。
4. **访问管理界面**：在浏览器中打开 `http://<服务器IP>:8000`，使用默认管理员账户（admin/admin）登录后即可开始使用。

### 最小可用示例

1. 在 Web 界面中点击“上传文档”，选择一张扫描好的 PDF 或图片。
2. 系统自动识别文本内容，并建议标签（如“发票”、“合同”）和文档类型。
3. 确认后保存，文档即可通过关键词或标签被快速检索到。

## 适用场景

- **个人文档归档**：管理护照复印件、银行对账单、医疗记录、保险单据等，告别纸质文件柜。
- **小型企业办公**：处理发票、合同、工资单、收据等，便于财务审计和客户信息查询。
- **会员组织管理**：社团或协会用于存档会议记录、会员资料、活动通知，提升内部管理效率。
- **家庭生活管理**：存储保修卡、使用说明书、包装清单等，方便快速查找和维护家电信息。

## 项目亮点

与同类文档管理系统相比，Paperless-ngx 具有以下差异化优势：

- **社区驱动**：作为继任项目，继承了原 Paperless 和 Paperless-ng 的生态积累，社区活跃度高，问题响应迅速。
- **强大的 OCR 能力**：内置支持多种语言的离线 OCR，无需依赖云服务，保障数据隐私安全。
- **灵活的自定义机制**：支持自定义标签、文档类型、对应方、存储路径规则，可深度适配个人或组织的工作流。
- **完整的自动化集成**：通过 API、邮件管道、消费目录等方式，与扫描仪、手机应用等外部系统无缝对接。
- **现代化用户界面**：基于 Angular 构建，响应式设计，支持移动端访问，操作体验流畅。

## 相关链接

- [GitHub 仓库](https://github.com/paperless-ngx/paperless-ngx)
- [官方文档](https://docs.paperless-ngx.com/)
- [在线演示](https://demo.paperless-ngx.com/)（用户名：demo，密码：demo）
- [社区讨论（Matrix）](https://matrix.to/#/%23paperlessngx%3Amatrix.org)
