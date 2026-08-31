---
tags:
  - trending
  - article
repo: tt-a1i/archify
date: 2026-08-31
language: JavaScript
stars_total: 36259
stars_today: 3722
---
## 项目概述

Archify 是一个面向 AI 编程助手的 Node.js 渲染与验证系统，支持 Cursor、Claude Code、Codex CLI 和 OpenCode 等主流工具。它的核心使命是让 AI 智能体能够将代码库或系统描述直接转化为精美、可验证的交互式系统图谱——覆盖架构图、工作流程图、时序图、数据流图和生命周期图五种类型。

在传统工作流中，架构图往往需要人工手动绘制，且与代码实际结构容易脱节。Archify 改变了这一模式：AI 智能体生成类型化的 JSON 中间表示（IR），Archify 以确定性的方式将其编译为自包含的 HTML/SVG 文件。这意味着每次生成的图表都是可预测、可复现的，而非随机的产物。对于工程师、技术负责人和文档维护者而言，这意味着他们可以在对话中直接获得可用于评审、分享和演示的高质量图表，无需离开当前的开发环境。

## 核心功能

- **五种图表类型与四种预设**：覆盖架构、工作流、时序、数据流和生命周期图，每种类型均提供多种视觉预设，适配不同汇报场合。
- **变更对比（Before / Delta / After）**：支持对两个已验证的快照进行精确对比，清晰标注新增、移除、修改、移动和重路由等拓扑变更事实，方便在合并前审查架构演化。
- **交互式探索**：内置节点搜索，可与版本控制的源代码建立关联并验证其来源；支持上游/下游可达性追踪、精确路由查看、角色对比以及引导式故事播放，所有交互均基于真实拓扑，杜绝模型幻觉。
- **单一文件输出与多格式导出**：生成的自包含 HTML 文件可直接打开使用，同时支持导出 PNG、SVG、WebM 动图以及 1200×630 的分享卡片，适配文档、演示和社交媒体传播。
- **确定性验证机制**：通过类型化 JSON IR 与确定性检查，确保每次生成的图表在结构和内容上严格可控，适合自动化和团队协作场景。
- **品牌标识内置**：内置多种知名技术品牌的图标样式，可直接用于生成带有品牌印记的架构图。

## 技术架构

Archify 采用典型的编译器分层设计思路，分为前端、中间表示和后端渲染三层。

**前端（Agent 适配层）**：针对不同的 AI 编程助手（Cursor、Claude Code、Codex CLI、OpenCode）提供了统一的接口封装。各 Agent 通过自然语言理解系统描述或直接分析代码库，产出符合规范的类型化 JSON IR。该 IR 是架构事实的中间载体，不绑定任何具体渲染引擎。

**中间表示（Typed JSON IR）**：IR 的设计强调严格的可验证性。每个节点、边、分组和路由都以类型化的方式定义，并附带必要的属性（如坐标约束、层级关系、语义标签等）。Archify 的核心验证引擎会逐一检查 IR 的完整性、连通性和语义合法性，确保任何输入在进入渲染阶段前都是可信的。

**后端渲染（Deterministic Compiler）**：验证通过后，编译器依照预设的布局算法和主题模板，将 IR 确定性地映射为 SVG 元素和交互逻辑。由于渲染过程不依赖运行时随机性，同一份 IR 在不同时间或机器上生成的结果完全一致，这为版本间对比和自动化测试提供了坚实基础。最终产物是一个自包含的 HTML 文件，JavaScript、CSS 和 SVG 全部内嵌，无需外部依赖即可运行，并且支持无头模式导出静态图片和视频。

Archify 的设计哲学是“事实在先，渲染在后”。所有交互能力（如搜索、路径追踪、角色比较）都构建在已验证的拓扑数据之上，而不是通过视觉元素的摆布来模拟逻辑，这从架构上保证了图表的可信度。

## 安装与使用

Archify 通过 npm 分发，支持全局或项目局部安装。整体使用流程通常包含以下步骤：

1. **准备环境**：确保已安装 Node.js（推荐 v18 或以上版本），并在本地初始化 npm 项目（若尚未存在）。
2. **安装 Archify**：
   ```bash
   npm install -g archify   # 全局安装
   # 或
   npm install archify      # 项目内安装
   ```
3. **在 Agent 中调用**：在 Cursor、Claude Code 或 Codex CLI 中，将 Archify 配置为 Agent 技能（Skill）。使用自然语言指令描述目标系统，例如：
   ```
   请分析当前项目的微服务架构，并生成一张架构图。要求显示服务间调用关系和数据流。
   ```
4. **自动生成与导出**：Agent 内部会生成 JSON IR 并调用 Archify 编译器，产出 `architecture.html` 文件。随后可通过命令行工具导出不同格式：
   ```bash
   archify export architecture.html --format png
   archify export architecture.html --format svg
   archify export architecture.html --format webm
   ```

一个最小化的编程式调用示例如下（Node.js）：

```javascript
import { render } from 'archify';

const ir = {
  type: 'architecture',
  nodes: [
    { id: 'web', label: 'Web App', kind: 'frontend' },
    { id: 'api', label: 'API Server', kind: 'backend' },
    { id: 'db', label: 'Database', kind: 'storage' }
  ],
  edges: [
    { source: 'web', target: 'api', label: 'REST' },
    { source: 'api', target: 'db', label: 'SQL' }
  ]
};

const html = render(ir, { theme: 'dark', preset: 'default' });
// 将 html 写入文件即可获得自包含的交互式图表
```

## 适用场景

- **代码评审与架构治理**：在 Merge Request 评审阶段，自动生成本次改动带来的架构差异对比，帮助评审者快速聚焦于拓扑结构的变化，而不必逐行审查代码。
- **新人入职与技术文档**：为新成员快速生成系统全景图，并支持点击节点跳转至实际源码位置，缩短理解现有系统的时间。
- **技术汇报与对外路演**：生成带有品牌标识、动效和明暗主题的精美图表，直接用于发布会、技术分享或行业会议，且支持导出高清图片或视频。
- **AI Agent 系统辅助**：当 Agent 需要向用户解释其处理流程、数据流或决策链路时，Archify 可实时生成可验证的图表，增强输出内容的可信度。

## 项目亮点

- **确定性胜过随机**：不同于某些 Agent 直接生成 HTML 或 SVG 的方式（结果难以预料且不可维护），Archify 以验证过的 IR 作为唯一事实来源，确保任何输入都能得到一致、可靠的输出，并可在 CI/CD 流程中固化为测试资产。
- **事实型交互**：搜索、路径追踪、角色比较等交互功能均基于真实的拓扑数据，而非视觉近似，彻底消除模型在描述内部关系时可能产生的“胡编乱造”问题。
- **单一文件与多格式导出**：自包含 HTML 便于分发和归档，而 PNG/SVG/WebM 以及社交分享卡片的直接导出能力，使其无缝融入现有文档与协作工具链。
- **多 Agent 平台适配**：同一套 IR 和编译管线可服务于 Cursor、Claude Code、Codex CLI 和 OpenCode 等不同生态，降低了技术栈切换时的学习成本。

## 相关链接

- [GitHub 仓库](https://github.com/tt-a1i/archify)
- [项目主页](https://archify.dev)（此处为示例占位，请以实际页面链接为准）
- [更新日志](https://github.com/tt-a1i/archify/CHANGELOG.md)
