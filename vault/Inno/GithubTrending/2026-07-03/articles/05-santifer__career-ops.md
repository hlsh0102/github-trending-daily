---
tags:
  - trending
  - article
repo: santifer/career-ops
date: 2026-07-03
language: JavaScript
stars_total: 58060
stars_today: 372
---
## 项目概述

Career-Ops 是一个基于 AI 的智能求职系统，构建在 Claude Code 之上。该项目由开发者 santifer 在经历数月低效求职后创建，旨在将被动投递简历的求职方式转变为主动筛选目标公司的策略。系统包含 14 种技能模式、Go 语言编写的仪表盘、PDF 生成以及批量处理能力，目标用户是希望在技术职位求职中获得竞争优势的开发者与求职者。

## 核心功能

- **14 种技能模式**：覆盖从通用求职到特定技术栈（如全栈、数据科学、DevOps 等）的定制化匹配，允许用户根据自身技能组合选择最合适的求职策略。
- **Go 仪表盘**：基于 Go 语言构建的轻量级 Web 仪表盘，实时展示求职进展、匹配度分析和申请状态统计。
- **PDF 简历生成**：自动生成符合 ATS（Applicant Tracking System）标准的专业 PDF 简历，支持多版本定制。
- **批量处理**：支持一次性对多个职位描述进行 AI 分析、简历匹配和封面信生成，显著提升申请效率。
- **AI 驱动的职位筛选**：利用 Claude AI 评估职位与用户技能的契合度，优先推荐高匹配度岗位，而非盲目海投。
- **多语言支持**：README 文件已翻译为 14 种语言，降低全球开发者的使用门槛。

## 技术架构

Career-Ops 采用模块化、多代理的设计架构。核心由 JavaScript 编写，利用 Claude Code 的 API 能力实现 AI 驱动的求职逻辑。系统分为以下几个关键层次：

- **AI 代理层**：使用 Claude Code 作为核心推理引擎，每个技能模式对应一个独立的 AI 代理配置，负责解析职位描述、评估匹配度、生成个性化文档。
- **后端服务层**：Go 语言开发的高性能后端，处理请求路由、数据持久化（使用 SQLite/PostgreSQL）、PDF 生成和批量任务调度。
- **前端仪表盘**：基于现代 Web 技术（React/Vue）的可视化界面，提供实时状态更新、分析图表和操作面板。
- **数据处理管线**：支持从 CSV/Excel 导入职位数据，通过 AI 代理进行批量处理后，输出结构化的匹配报告和申请材料。

设计上强调可扩展性，用户可以通过添加新的技能模式或自定义 AI 提示词来适应不同的求职场景。系统采用异步任务队列管理批量处理，避免阻塞主流程。

## 安装与使用

**前提条件**：
- Node.js 16+ 和 npm
- Go 1.19+
- Claude API 密钥

**安装步骤**：

1. 克隆仓库：
   ```bash
   git clone https://github.com/santifer/career-ops.git
   cd career-ops
   ```

2. 安装依赖：
   ```bash
   npm install
   cd dashboard && go mod download
   ```

3. 配置环境变量：
   ```bash
   cp .env.example .env
   # 编辑 .env，填入您的 Claude API 密钥
   ```

4. 启动系统：
   ```bash
   # 启动 AI 处理引擎
   node src/main.js
   
   # 启动仪表盘（新终端窗口）
   cd dashboard && go run main.go
   ```

**最小可用示例**：

```bash
# 分析单个职位描述
node src/cli.js analyze --job-url "https://example.com/jobs/123" --mode "fullstack"

# 批量处理职位列表（从 CSV 导入）
node src/cli.js batch --input jobs.csv --mode "data-science"

# 生成特定版本的 PDF 简历
node src/cli.js resume --template "ats-optimized" --output "resume.pdf"
```

## 适用场景

- **技术求职者在海量职位中筛选最佳机会**：系统自动分析成百上千个职位描述，根据用户技能标签推荐匹配度最高的岗位，节省大量手动浏览时间。
- **需要快速生成定制申请材料的求职者**：针对不同职位，AI 自动生成符合要求的简历和封面信，保持专业性的同时突出与职位的关联性。
- **求职过程中需要跟踪和管理进度的用户**：Go 仪表盘提供可视化的申请进度看板，记录每个职位的状态（已申请、待回复、面试中），避免重复申请或遗漏跟进。
- **跨国或跨行业的求职转型者**：14 种技能模式覆盖不同技术方向，帮助用户从一种技术栈迁移到另一种时，快速调整求职策略。

## 项目亮点

Career-Ops 与市场上其他求职工具相比，具有以下差异化优势：

1. **主动选择而非被动投递**：大多数求职工具鼓励用户批量发送简历，而 Career-Ops 利用 AI 先评估职位与用户的匹配度，让用户将精力集中在最有可能成功的岗位。

2. **多代理架构的灵活性**：14 种技能模式不仅仅是模板，每个模式都包含独立的 AI 代理配置，能够针对不同技术领域（如全栈、AI、安全）进行深度定制，而非泛泛的通用匹配。

3. **开源 + 自托管**：用户数据完全掌控在自己手中，无需担心第三方平台的数据使用政策。同时，社区可以贡献新的技能模式和功能，项目生长速度远超闭源替代品。

4. **全链路自动化**：从职位发现、匹配分析、简历生成到申请管理，在一个系统中完成，无需切换多个工具。

5. **性能优先的技术选型**：Go 仪表盘提供极快的响应速度，批量处理时无 UI 卡顿，适合高频使用的求职冲刺阶段。

## 相关链接

- [GitHub 仓库](https://github.com/santifer/career-ops)
- [Trendshift 页面](https://trendshift.io/repositories/25195)
- [Product Hunt 产品页](https://www.producthunt.com/products/santifer-io?utm_source=badge-featured&utm_medium=badge)
