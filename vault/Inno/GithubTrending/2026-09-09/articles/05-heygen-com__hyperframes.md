---
tags:
  - trending
  - article
repo: heygen-com/hyperframes
date: 2026-09-09
language: TypeScript
stars_total: 48038
stars_today: 2627
---
## 项目概述

HyperFrames 是一个面向 AI Agent 的 HTML 视频渲染引擎，由 HeyGen 团队开源。它允许开发者将 HTML 内容直接渲染为高质量视频，提供了一套简洁的 TypeScript API 和渲染服务，使程序化生成动态视频变得像编写网页一样自然。该项目解决了传统视频生成中模板固定、定制成本高的问题，通过引入 HTML/CSS 表达力，让每一次视频生成都能拥有完全不同的视觉呈现。目标用户包括 AI 应用开发者、自动化内容生产者、前端工程师以及任何希望在 agent 工作流中加入动态视觉输出能力的团队和独立开发者。

## 核心功能

- **HTML 到视频的无缝转换**：直接接受含有 CSS 动画、过渡和交互的 HTML 内容，可通过 JavaScript SDK 或播放器 iframe 接口提交代码并返回最终渲染后的 MP4 视频文件。
- **面向 Agent 的原生设计**：提供专为自动化和程序化调用优化的组件，支持 llms.txt 规范以帮助大语言模型理解和调用 API，还提供用于结构化输出的响应 schema 校验。
- **模板块（Blocks）内容复用**：内置可复用的内容模板块系统，其中数据图表模板块支持直接生成数据驱动型可视化内容，方便在多个视频中保持一致的信息设计风格。
- **playground 可交互调试**：附带云端 playground 环境（hyperframes.dev），开发者可以在浏览器中即时编辑 HTML/CSS/JS 并查看渲染效果，极大降低实验和迭代成本。
- **本地快速开发与全球边缘渲染网络**：支持在本地开发环境中预览效果，而渲染任务由分布在全球的边缘节点执行，显著提升视频生成速度和可靠性。

## 技术架构

HyperFrames 的核心设计理念是“将浏览器能力转化服务”。底层利用了无头浏览器的渲染管线，通过服务器端运行的浏览器实例将定时器驱动的 CSS 动画转换为视频帧序列。项目采用客户端 SDK 与服务端渲染 API 相结合的架构：客户端 SDK 负责构建符合规范的请求、并在必要时执行生成器的生命周期函数；服务端则负责将 HTML 渲染为高质量的 MP4 视频。

项目特别针对 Agent 场景定义了核心的生命周期函数——`up`、`time` 和 `down`。`up` 用于帧序列激活前的准备（如网络请求），`time` 用于每帧更新画面（接受时间戳与元数据），`down` 用于清理资源。这使生成过程具备可预测性和可控制性，同时不需要面对传统视频渲染中的笨重状态管理。

在数据协议层面，项目定义了模板状态的协商逻辑，通过 `LLMContext` 将运行时动态数据注入模板并使用“生成器元数据”来控制时间。整个项目使用 TypeScript 编写，构建产物被编译为 ESM 及 CommonJS 双格式。并发渲染、负载均衡等技术细节均被封装在服务端，客户端无需关心具体资源部署。

## 安装与使用

HyperFrames 以 npm 包 `hyperframes` 形式发布，需要 Node.js 22 或更高版本。项目中针对不同的使用需求提供了三种使用模式：本地 CLI 快速验证、用于自定义工作流（在 Animate 应用场景中即可在目标服务器上运行）以及由 HeyGen 托管的渲染服务。

针对开发阶段，可以使用 npm 初始化一个项目：

```bash
npm install hyperframes
```

之后创建 `first.js` 文件并写入以下代码，在本地渲染第一个视频：

```js
import { HF } from "hyperframes";

const hf = new HF("您的API密钥");
const video = await hf.renderVideo(`
  <html>
    <body style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
      <h1>Hello HyperFrames</h1>
    </body>
  </html>
`);
await video.download("output");

// 如需本地预览，运行：
// npx hyperframes dev
```

生成并保存这一 MP4 文件只需 3-5 秒。项目还支持更复杂的时间驱动型动画，例如：

```js
window.hyperframes = (ctx) => ({
  up: async () => { /* 初始化资源 */ },
  time: async ({ video, duration, elapsed, frame }) => {
    document.getElementById('clock').textContent = (elapsed / 1000).toFixed(2) + 's';
  },
  down: async () => { /* 清理 */ }
});
```

在本地开发阶段也可以直接使用 `hyperframes dev` 启动开发服务器进行快速 Debug。

## 适用场景

- **AI Agent 自动内容生产**：在个人智能助理或自动化脚本中，将整理好的新闻摘要或数据报表实时渲染成短视频，可以直接发送至微信或抖音生态，无需二次人工剪辑。
- **数据驱动的动态视频仪表盘**：企业内可将实时运营数据生成可发布的动态视频报告，利用内置的“数据图表”模板块生成带图表动画的财经播报或项目汇报视频。
- **社交营销素材的规模化测试**：对于需要高频产出 A/B 测试素材的市场团队，通过编写不同配色版式文档的方式，可以在几分钟内完成上百套视频创意的渲染。
- **多语言视频与字幕制作**：利用高级字幕块（subtitles block），结合大模型翻译能力为同一份视频源自动生成多语言版本，拓展视频到达范围。

## 项目亮点

HyperFrames 与其他程序化视频生成项目的显著差异在于“从代码到像素”的路径是标准 Web 技术与现代渲染基础设施的结合。它避开了锁定在特定模板引擎的桎梏，让开发者回归使用自己已经掌握的 HTML/CSS 技能即可创造动态画面，这也是其星标增长惊人的主要原因。服务端渲染（API 即核心）配合开源 SDK，使得 Agent 接入视频能力的成本被大幅降低——一段可读性很强的 HTML 就能让模型直接上手。项目将“生成”的能力云服务化，没有把复杂度过早地抛给终端开发者在本地进行。

## 相关链接

- [GitHub 仓库](https://github.com/heygen-com/hyperframes)
- [在线 Docs 文档](https://hyperframes.heygen.com/introduction)
- [快速上手指南](https://hyperframes.heygen.com/quickstart)
- [效果展示页](https://hyperframes.heygen.com/showcase)
- [Playground 在线体验](https://www.hyperframes.dev/)
- [模板块目录](https://hyperframes.heygen.com/catalog/blocks/data-chart)
- [Discord 社区](https://discord.gg/EbK98HBPdk)
