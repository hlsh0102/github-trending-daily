---
tags:
  - trending
  - article
repo: lfnovo/open-notebook
date: 2026-06-05
language: TypeScript
stars_total: 25310
stars_today: 212
---
## 项目概述

Open Notebook 是一个开源的、注重隐私的 Notebook LM 替代实现。它是对 Google Notebook LM 的完全开源复刻，同时提供了更高的灵活性和更丰富的功能。项目使用 TypeScript 开发，采用 MIT 许可证发布。

该项目的核心目标是提供一个不受厂商锁定、数据完全由用户掌控的笔记智能助手。无论是研究者、学生、内容创作者还是知识工作者，都可以使用 Open Notebook 来整理、分析和生成基于自有文档的智能内容。与 Google 的闭源方案不同，Open Notebook 允许用户在自己的基础设施上部署，确保敏感数据不会离开本地环境。

## 核心功能

- **多格式文档支持**：能够导入包括 PDF、Markdown、文本文件、网页链接等多种格式的文档，并自动解析内容
- **智能问答**：基于导入的文档内容，使用大语言模型提供精准的问答服务，支持多轮对话
- **自动笔记生成**：根据用户导入的文档自动生成摘要、关键点提取和结构化笔记
- **自定义工作流**：支持用户配置不同的 LLM 提供商和模型，灵活选择最适合使用场景的 AI 模型
- **多语言支持**：内置国际化和多语言界面，包括中文、英文、德文、法文、西班牙文等多语言支持
- **隐私保护**：支持完全本地部署，数据存储和 AI 调用均在用户控制的环境中进行

## 技术架构

Open Notebook 采用现代化的前端后端分离架构。前端使用 Next.js 框架构建，提供响应式的用户界面；后端基于 Node.js 和 TypeScript 开发，保证了代码的类型安全性和可维护性。

项目采用了模块化设计，核心功能包括文档处理引擎、向量存储系统、LLM 集成模块和用户管理系统。文档处理引擎支持多种文件格式的解析和文本提取；向量存储系统使用嵌入向量实现高效的语义检索；LLM 集成模块抽象了不同 AI 提供商的 API 差异，允许灵活切换底层模型。

数据库层面支持多种主流数据库系统，可以根据部署需求选择 SQLite、PostgreSQL 或 MySQL。项目还集成了 Redis 用于缓存和会话管理，提升了响应速度和并发处理能力。

## 安装与使用

### 基本安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/lfnovo/open-notebook.git
cd open-notebook
```

2. **安装依赖**
```bash
npm install
# 或使用 yarn
yarn install
```

3. **配置环境变量**
复制 `.env.example` 为 `.env`，并根据需要配置 LLM API 密钥、数据库连接等信息。

4. **启动开发服务器**
```bash
npm run dev
# 或
yarn dev
```

5. **构建生产版本**
```bash
npm run build
npm start
```

### 最小可用示例

使用 Docker Compose 进行一键部署：

```yaml
version: '3.8'
services:
  app:
    image: lfnovo/open-notebook:latest
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/open_notebook
      - LLM_API_KEY=your_api_key_here
    volumes:
      - ./data:/app/data
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=open_notebook
```

启动后访问 `http://localhost:3000` 即可开始使用。

## 适用场景

- **学术研究**：研究人员可以导入论文、报告等文档，快速获取关键信息、自动生成文献综述和论文大纲
- **项目管理**：产品经理和项目经理能够整理各类文档、会议记录，自动生成项目总结和待办事项清单
- **内容创作**：作家、博主可以收集参考资料，利用 AI 辅助生成文章大纲、草稿和修改建议
- **个人知识管理**：知识工作者可以建立个人知识库，实现高效的信息检索和知识沉淀

## 项目亮点

与 Google Notebook LM 和其他类似项目相比，Open Notebook 具有以下差异化优势：

- **完全开源**：代码透明可审计，社区驱动发展，不存在被商业公司突然关闭的风险
- **数据主权**：用户完全控制自己的数据，支持本地部署，避免敏感信息上传到第三方服务器
- **模型灵活性**：支持接入多种 LLM 提供商（如 OpenAI、Anthropic、本地模型等），不受单一模型限制
- **丰富的配置选项**：从数据库选择到 AI 模型配置，提供了高度定制化的部署能力
- **活跃的社区支持**：拥有 Discord 社区和详细的文档系统，包括入门指南、用户手册和核心概念说明
- **持续更新迭代**：项目保持活跃的开发状态，GitHub 上拥有超过 25000 星标，社区贡献活跃

## 相关链接

- [GitHub 仓库](https://github.com/lfnovo/open-notebook)
- [官方网站](https://www.open-notebook.ai)
- [入门指南](docs/0-START-HERE/index.md)
- [用户手册](docs/3-USER-GUIDE/index.md)
- [功能说明](docs/2-CORE-CONCEPTS/index.md)
- [部署文档](docs/1-INSTALLATION/index.md)
