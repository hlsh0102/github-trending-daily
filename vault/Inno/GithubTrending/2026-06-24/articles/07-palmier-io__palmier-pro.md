---
tags:
  - trending
  - article
repo: palmier-io/palmier-pro
date: 2026-06-24
language: Swift
stars_total: 8572
stars_today: 1630
---
## 项目概述

Palmier Pro 是一款专为 AI 时代打造的 macOS 视频编辑器。与传统的视频编辑软件不同，Palmier Pro 将人工智能深度集成到编辑流程的每个环节，让创作者能够利用 AI 技术大幅提升视频制作的效率和质量。该项目由 Y Combinator S24 批次支持的团队开发，开源采用 GPL-3.0 许可证，旨在为视频创作者、AI 爱好者和开发者提供一个现代化、可扩展的编辑平台。

## 核心功能

- **AI 驱动的智能剪辑**：内置 AI 模型可自动识别视频中的关键场景和精彩片段，支持一键生成粗剪版本，大幅减少手动挑选素材的时间。
- **实时 AI 特效与滤镜**：集成多种 AI 处理管线，可实时对视频进行风格迁移、超分辨率增强、背景去除等高级操作，所有效果在编辑过程中实时预览。
- **智能字幕与翻译**：自动语音识别（ASR）生成时间轴字幕，支持多语言翻译，并允许用户手动校正和调整字幕样式。
- **非线性时间轴编辑**：提供专业级的多轨时间轴编辑器，支持无限图层、关键帧动画、速度调整、转场效果等核心编辑功能。
- **AI 辅助音频处理**：集成语音分离、噪声消除和自动音量均衡功能，可一键优化视频中的音频质量。
- **原生 macOS 性能**：基于 Swift 和 Apple Silicon 深度优化，充分利用 Metal 和 Core ML 框架，实现流畅的实时渲染体验。

## 技术架构

Palmier Pro 采用 Swift 作为主要开发语言，深度整合 macOS 平台的原生框架。核心架构围绕以下几个关键技术构建：

1. **Metal 加速渲染管线**：所有视频处理和特效渲染均基于 Metal 框架实现 GPU 加速，支持 4K、8K 等高分辨率视频的实时回放和编辑。
2. **Core ML 集成**：AI 模型通过 Apple 的 Core ML 框架运行，确保在 Apple Silicon 芯片上获得最佳性能。支持本地推理，无需联网即可使用大部分 AI 功能。
3. **插件化架构**：编辑器和 AI 功能采用模块化设计，开发者可通过公开的 API 扩展新的滤镜、转场和 AI 模型，社区可贡献自定义组件。
4. **FFmpeg 底层支持**：使用 FFmpeg 处理视频的编解码和格式转换，保证对不同视频格式的广泛兼容性。
5. **响应式 UI 框架**：采用 SwiftUI 构建用户界面，支持 macOS 的最新特性如 Stage Manager、多窗口和 Handoff。

## 安装与使用

**系统要求**：macOS 26 (Tahoe) 及以上版本，Apple Silicon 芯片（M 系列）。

**安装步骤**：

1. 前往 [GitHub Releases 页面](https://github.com/palmier-io/palmier-pro/releases) 下载最新的 `.dmg` 安装包。
2. 打开下载的磁盘映像，将 Palmier Pro 拖入“应用程序”文件夹。
3. 首次启动时，系统可能会提示安全验证，请在“系统设置>隐私与安全性”中允许打开。
4. 启动应用后，即可开始创建项目并导入视频素材。

**最小可用示例**：

```swift
// 创建一个新项目并导入视频
import PalmierCore

let project = Project(name: "My First AI Edit")
let videoClip = try VideoClip(url: URL(fileURLWithPath: "input.mp4"))
project.timeline.addClip(videoClip)

// 应用 AI 场景检测自动生成字幕
let sceneDetection = AISceneDetection()
let scenes = sceneDetection.detectScenes(in: videoClip)

// 导出最终视频
let exportConfig = ExportConfig(format: .mp4, resolution: .hd1080)
try project.export(to: URL(fileURLWithPath: "output.mp4"), config: exportConfig)
```

## 适用场景

- **内容创作者与视频博主**：利用 AI 智能剪辑功能，快速处理大量拍摄素材，自动生成吸引眼球的短视频和 Vlog。
- **影视后期从业者**：作为专业编辑流程的辅助工具，使用 AI 增强功能提高工作效率，如智能去噪、超分辨率修复老旧素材。
- **教育与企业培训**：自动为教学视频生成多语言字幕，并进行语音润色，便于国际化分发和远程学习。
- **AI 研究与原型开发**：基于 Palmier Pro 的插件化架构，开发者可以快速集成和测试新的视频 AI 模型，探索创意应用。

## 项目亮点

- **原生 AI 集成**：与其他视频编辑器不同，Palmier Pro 将 AI 作为核心编辑能力而非附加功能，所有 AI 处理均在本地完成，保护用户隐私。
- **极致性能优化**：专为 Apple Silicon 设计，充分利用 M 系列芯片的神经网络引擎和 GPU，实现毫秒级 AI 推理响应。
- **开源透明**：GPL-3.0 许可证保证了代码的开放性，社区可以审查 AI 模型的行为、贡献新的功能组件或定制自己的版本。
- **现代用户体验**：遵循 macOS 设计规范，提供直觉式操作界面和键盘快捷键，降低学习曲线，同时保留专业编辑所需的深度控制。

## 相关链接

- [GitHub 仓库](https://github.com/palmier-io/palmier-pro)
- [下载页面](https://github.com/palmier-io/palmier-pro/releases/latest/download/PalmierPro.dmg)
- [X（Twitter）官方账号](https://x.com/Palmier_io)
- [Discord 社区](https://discord.com/invite/SMVW6pKYmg)
