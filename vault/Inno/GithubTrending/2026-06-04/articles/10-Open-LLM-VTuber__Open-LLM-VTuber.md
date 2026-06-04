---
tags:
  - trending
  - article
repo: Open-LLM-VTuber/Open-LLM-VTuber
date: 2026-06-04
language: Python
stars_total: 9138
stars_today: 693
---
## 项目概述

Open-LLM-VTuber 是一个开源项目，旨在让用户通过语音与任何大型语言模型（LLM）进行免提交互，同时配合 Live2D 虚拟角色进行面部表情和口型同步，所有计算均在本地完成。该项目解决了传统 AI 对话工具中需要手动输入、缺乏视觉反馈以及依赖云服务的问题，特别适合希望获得沉浸式、个性化 AI 交互体验的开发者、虚拟主播（VTuber）爱好者以及隐私敏感用户。它支持跨平台运行（Windows、macOS、Linux），并允许多人同时与同一 LLM 实例对话。

## 核心功能

- **免提语音交互**：用户可以通过语音与 LLM 进行对话，无需键盘或鼠标操作，支持多轮对话和即时响应。
- **语音打断**：在 LLM 回复过程中，用户可以随时语音打断，项目会自动停止当前输出并等待新输入，提供流畅的交互体验。
- **Live2D 角色集成**：支持加载自定义的 Live2D 模型，根据语音输入和 LLM 回复实时驱动角色的表情和口型同步，增强沉浸感。
- **本地运行**：所有核心组件（语音识别、LLM 推理、语音合成、Live2D 渲染）均在本地设备上运行，无需网络连接，保护用户隐私。
- **跨平台支持**：支持 Windows、macOS 和 Linux 系统，并提供了 Docker 镜像简化部署。
- **多用户并发**：支持多个用户同时与同一个 LLM 实例交互，适用于直播或多用户协作场景。

## 技术架构

项目采用模块化设计，主要组件包括：

- **语音识别**：基于 Vosk 或 Whisper 等本地语音识别引擎，将用户的语音输入转换为文本。
- **LLM 接口**：通过统一的 API 接口支持多种 LLM，如 Llama、Mistral、GPT（通过本地部署）等，用户可自由切换模型。
- **语音合成**：使用 Edge TTS 或 Coqui TTS 等本地合成引擎，将 LLM 的文本回复转换为语音。
- **Live2D 渲染**：集成 Cubism SDK 或 Live2D Web 引擎，在 OpenGL 或 Web 环境中实时渲染 Live2D 模型并同步动作。
- **音频流处理**：使用 PyAudio 或 PortAudio 库实现低延迟的音频输入输出，支持实时语音打断。
- **配置管理**：通过 YAML 文件或 GUI 界面配置各模块参数，包括 LLM 模型路径、语音引擎选择、Live2D 模型文件等。

架构特点在于各个模块松耦合，用户可以根据硬件性能和需求单独替换或升级组件。例如，低配机器可选用轻量级语音识别模型，高配机器则启用更强大的 LLM 和 TTS。

## 安装与使用

### 安装步骤

1. **克隆仓库**：
   ```bash
   git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber.git
   cd Open-LLM-VTuber
   ```

2. **安装依赖**：
   项目基于 Python 3.9+，建议使用虚拟环境：
   ```bash
   pip install -r requirements.txt
   ```

3. **下载 Live2D 模型**：
   默认模型可通过脚本下载：
   ```bash
   python download_model.py
   ```
   用户也可放置自己的 `.model3.json` 文件到 `models/` 目录。

4. **配置 LLM**：
   编辑 `config.yaml` 文件，设置 LLM 的路径或 API 地址（如使用 Ollama 或 llama.cpp 本地服务）。

5. **运行**：
   ```bash
   python main.py
   ```

### 最小可用示例

启动后，项目会打开 Live2D 窗口并开始监听麦克风。用户可直接对麦克风说话，系统会显示语音转文字结果，LLM 回复后，Live2D 角色会同步口型并播放合成语音。按 `Ctrl+C` 或关闭窗口退出。

如果需要测试语音打断，只需在 LLM 说话时再次说话，系统会自动停止当前回复并开始新的一轮对话。

## 适用场景

- **虚拟主播（VTuber）直播**：主播无需手动打字或切换屏幕，直接用语音与 AI 角色互动，提升直播趣味性和观众参与度。
- **个人 AI 助手**：在需要免提操作的场景中（如烹饪、驾驶），通过语音向 LLM 询问信息，Live2D 角色提供视觉反馈。
- **编程辅助**：开发者可通过语音向 LLM 提问代码问题，同时 Live2D 角色展示表情变化，提升工作愉悦感。
- **教育与训练**：用于语言学习或角色扮演训练，学生可以与 Live2D 角色进行口语对话练习。

## 项目亮点

与同类项目相比，Open-LLM-VTuber 具有以下差异化优势：

- **完全本地运行**：所有数据处理在本地完成，不依赖云服务，适合注重隐私的用户或离线环境。
- **多 LLM 兼容**：不锁定特定模型，用户可自由选择 Hugging Face 上任意 LLM，或通过 API 接入自部署的服务。
- **实时语音打断**：这是许多语音 AI 项目中缺失的功能，它让交互更自然，接近真人对话体验。
- **跨平台支持**：相比仅限 Windows 的 VTuber 工具，macOS 和 Linux 用户也能享受完整功能。
- **活跃的社区与开发路线**：项目正计划 v2.0 完全重写，社区在 Zulip 上定期讨论规划，用户可直接参与贡献。

## 相关链接

- [GitHub 仓库](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)
- [官方文档](https://open-llm-vtuber.github.io/docs/quick-start)
- [Docker 镜像](https://hub.docker.com/r/Open-LLM-VTuber/open-llm-vtuber)
- [Zulip 开发者社区](https://olv.zulipchat.com)
- [Discord 讨论组](https://discord.gg/3UDA8YFDXx)
