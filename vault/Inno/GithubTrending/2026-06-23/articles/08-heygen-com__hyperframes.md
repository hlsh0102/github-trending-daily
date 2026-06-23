---
tags:
  - trending
  - article
repo: heygen-com/hyperframes
date: 2026-06-23
language: TypeScript
stars_total: 30226
stars_today: 395
---
## 项目概述

HyperFrames 是一个由 HeyGen 团队开发的开源框架，其核心理念是“编写 HTML，渲染视频，为智能体而生”。它旨在弥合 Web 页面与动态视频生成之间的鸿沟，允许开发者使用熟悉的 HTML、CSS 和 JavaScript 技术栈来构建和渲染可编程的视频内容。该项目主要面向需要程序化生成高质量、可定制视频的开发者和 AI 智能体开发者，解决了传统视频编辑工具难以与代码工作流集成、且无法通过 API 或 AI 指令灵活控制的问题。通过 HyperFrames，用户可以像编写网页一样设计视频帧，并将其无缝转化为流畅的视频输出。

## 核心功能

- **HTML 驱动视频生成**：直接使用标准的 HTML、CSS 和 JavaScript 编写视频每一帧的内容和样式，无需学习复杂的视频编辑软件或专用格式。
- **智能体友好 API**：提供简洁的 API 接口，专为 AI 智能体、自动化工作流和脚本调用设计，支持从自然语言指令或结构化数据生成视频。
- **动态数据绑定**：支持将 JSON 数据动态注入到 HTML 模板中，实现基于数据变化的实时视频渲染，适合数据可视化、统计报告等场景。
- **内置动画与转场**：集成了标准的 CSS 动画和页面转场效果，开发者可以轻松实现帧与帧之间的平滑过渡，提升视频质量。
- **实时预览与迭代**：提供开发模式下的实时预览功能，以及在线 Playground，让用户在编写代码的同时即可看到视频效果，加速调试流程。
- **可扩展的组件库**：项目附带 Catalog，包含预置的图表、数据展示等视觉 Block，用户可以直接复用或自定义组件，加快开发速度。

## 技术架构

HyperFrames 基于 TypeScript 开发，运行依赖于 Node.js（版本 ≥22）。其核心设计思想是**将浏览器渲染管道与视频编码管线结合**。框架内部利用浏览器环境（如无头 Chromium）对用户提供的 HTML 文件进行渲染，然后逐帧捕获屏幕截图或动画输出，最终将这些静态或动态帧编码为视频文件。这种架构的优越性在于：开发者可以充分利用 Web 生态中丰富的 CSS 动画、Canvas 绘图、SVG 矢量图形等能力，而视频的生成过程则完全自动化。此外，整个框架通过抽象层屏蔽了底层渲染和编码细节，对外提供统一的 `hyperframes` 包接口，方便集成到各类前端或后端项目中。

## 安装与使用

**安装**：
通过 npm 或 yarn 安装 HyperFrames 包：
```bash
npm install hyperframes
# 或
yarn add hyperframes
```

**最小可用示例**：
创建一个简单的 HTML 文件 `hello.html`，内容如下：
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial; }
    .text { font-size: 48px; color: #333; }
  </style>
</head>
<body>
  <div class="text">Hello, HyperFrames!</div>
</body>
</html>
```

然后编写一个 Node.js 脚本 `generate.js`：
```javascript
import { render } from 'hyperframes';

await render({
  input: 'hello.html',
  output: 'hello.mp4',
  duration: 3, // 视频时长（秒）
  fps: 30,
});
```

运行脚本即可在目录下生成 `hello.mp4` 视频文件。

## 适用场景

- **数据驱动视频报告**：如企业季度报表、实时数据分析看板的自动视频化摘要，数据变化时无需人工干预即可生成新的视频内容。
- **AI 辅助内容创作**：结合大语言模型，将文本脚本或故事板自动转换为短视频，适用于社交媒体内容生产、教育说明视频等。
- **自动化营销素材生成**：为电商、广告行业提供批量视频生成能力，基于产品列表模板快速输出个性化宣传视频。
- **开发者工具与原型**：前端开发者可将 UI 原型、交互演示快速转为视频分享，或用于自动化测试中的视觉回归校验。

## 项目亮点

- **低门槛与高效率**：不需要专门的视频编码知识，前端开发者和 AI 智能体即可直接上手，大幅降低视频生成的技术门槛。
- **完全的程序化控制**：通过代码精确定义每一帧的内容、动画和时间轴，实现传统视频编辑无法达到的粒度和可重复性。
- **与 Web 生态无缝集成**：可复用现有 HTML/CSS 库、图表工具（如 D3.js）、字体和资源，最大化已有技术投资。
- **开源与社区驱动**：基于 Apache 2.0 许可证发布，拥有活跃的 Discord 社区和丰富的文档、示例及在线 Playground，确保持续迭代和支持。

## 相关链接

- [GitHub 仓库](https://github.com/heygen-com/hyperframes)
- [快速开始](https://hyperframes.heygen.com/quickstart)
- [在线 Playground](https://www.hyperframes.dev/)
- [组件 Catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart)
- [官方文档](https://hyperframes.heygen.com/introduction)
- [Discord 社区](https://discord.gg/EbK98HBPdk)
