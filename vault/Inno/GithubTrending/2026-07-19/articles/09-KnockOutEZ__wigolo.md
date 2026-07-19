---
tags:
  - trending
  - article
repo: KnockOutEZ/wigolo
date: 2026-07-19
language: TypeScript
stars_total: 1330
stars_today: 203
---
## 项目概述

wigolo 是一个面向 AI 编程代理的本地优先网页情报工具套件。它通过 MCP（模型上下文协议）为 AI 代理提供搜索、抓取、爬取和研究等能力，且完全不需要 API 密钥、不依赖云端服务、没有按查询计费的限制。该项目目前处于公测阶段。

wigolo 解决了 AI 代理在获取网络信息时面临的核心痛点：现有方案要么依赖第三方 API 产生持续成本，要么需要复杂的云端基础设施。wigolo 让 AI 代理在本地即可完成所有网页相关操作，所有数据都存储在 `~/.wigolo/` 目录下，不向外发送任何信息。

目标用户包括使用 Claude Code、Cursor、Codex、Gemini CLI 等编码代理的开发者，构建 LangChain、CrewAI、LlamaIndex 等 AI 框架应用的开发者，以及任何需要为 AI 代理提供可靠网络访问能力的团队。

## 核心功能

- **搜索**：支持搜索引擎查询，无需 API 密钥即可获取搜索结果
- **抓取**：直接获取网页内容，支持多种内容类型
- **爬取**：递归爬取网站，提取结构化数据
- **缓存**：智能缓存机制，避免重复请求，提高效率
- **相似内容查找**：基于内容相似度发现相关页面
- **研究模式**：自主信息收集循环，可针对复杂问题自动探索多个来源

## 技术架构

wigolo 基于 TypeScript 开发，采用模块化架构设计：

- **MCP 服务器**：作为 MCP 服务器运行，可无缝集成到支持 MCP 协议的 AI 代理中，如 Claude Code、Cursor、VS Code 等
- **REST API**：也提供 REST 接口，方便与传统 Web 应用或自托管代理集成
- **SDK 嵌入**：可直接嵌入到自定义应用程序中，提供编程接口

核心设计理念是“本地优先”——所有操作都在用户本地环境完成，不依赖任何外部云服务。这不仅消除了 API 成本，也保证了数据隐私。缓存机制将结果存储在本地，减少重复网络请求，同时提升响应速度。

工具集通过统一的接口暴露，AI 代理可以根据需要组合使用多个工具，实现复杂的网页情报收集任务。

## 安装与使用

**安装**

```bash
npm install -g wigolo
```

或者使用 npx 直接运行：

```bash
npx wigolo
```

**配置**

配置存储在 `~/.wigolo/` 目录下，无需任何 API 密钥即可开始使用。

**基本使用**

以 MCP 服务器方式运行，供 Claude Code 等代理使用：

```bash
wigolo serve
```

然后配置 AI 代理连接到本地运行的 MCP 服务器。

以 REST API 方式运行：

```bash
wigolo serve --rest
```

通过 SDK 在代码中使用：

```typescript
import { wigolo } from 'wigolo';

// 搜索网页
const results = await wigolo.search('最新的 AI 技术趋势');
console.log(results);

// 抓取特定页面
const content = await wigolo.fetch('https://example.com');
console.log(content);
```

## 适用场景

1. **编码代理增强**：在 Claude Code、Cursor 等编码工具中，让 AI 代理能实时获取文档、搜索解决方案、抓取技术博客，显著提升代码生成质量

2. **自托管 AI 工作流**：在 n8n、Dify 等自托管平台中，集成 wigolo 让自动化工作流具备网络信息检索能力，无需额外付费

3. **研究和情报收集**：使用研究模式让 AI 代理自动探索多个来源，收集整理特定主题的最新信息，适用于竞品分析、技术调研等场景

4. **本地知识库构建**：爬取指定网站内容，结合缓存机制构建本地知识库，供 AI 代理后续查询使用

## 项目亮点

- **零成本运营**：完全不需要 API 密钥，没有按查询计费的模式，$0/query 是真实承诺。这对于需要大量网络访问的 AI 代理尤其重要
- **隐私保障**：所有操作在本地完成，数据不离开 `~/.wigolo/` 目录，适合处理敏感信息的场景
- **多协议支持**：同时支持 MCP 和 REST 协议，可适配各种 AI 代理框架和传统应用
- **工具全面**：从搜索到抓取、爬取、缓存、研究，提供完整的信息获取工具链
- **零基础设施**：不需要搭建云服务，不需要配置 API 网关，一条命令即可启动

## 相关链接

- [GitHub 仓库](https://github.com/KnockOutEZ/wigolo)
- [文档](docs/README.md)
- [示例](examples/README.md)
