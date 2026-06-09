---
tags:
  - trending
  - article
repo: Andyyyy64/whichllm
date: 2026-06-09
language: Python
stars_total: 3630
stars_today: 143
---
## 项目概述

`whichllm` 是一款为本地硬件量身定制的大语言模型推荐工具。你只需要执行一条命令，它就能自动检测系统的 GPU/CPU/RAM 信息，从 HuggingFace 上数以万计的模型中，筛选出那些真正能在你机器上运行的、且综合表现最优的模型，并根据实时更新的性能基准进行排名。它的目标用户是希望在本地部署 LLM 的开发者、研究人员和 AI 爱好者，帮助用户摆脱靠参数数量判断模型好坏的旧习惯，用真实跑分数据做出选择。

## 核心功能

- **一键推荐**：无需任何配置，运行命令即可获得当前硬件上最佳的本地 LLM 推荐列表。
- **硬件自动检测**：自动识别 GPU 型号、CPU 核心数、可用显存和系统 RAM，确保推荐的模型能实际运行。
- **硬件模拟**：可指定任意 GPU 型号（如 `--gpu "RTX 4090"`），提前评估升级硬件后的模型选择空间。
- **模型规划**：通过 `whichllm plan` 命令，反向查询运行特定模型（如 “llama 3 70b”）所需的最低 GPU 配置。
- **即时运行**：`whichllm run` 支持直接启动所选模型的聊天会话，无需额外配置。
- **脚本集成**：提供 `--json` 输出模式，方便 CI/CD 或其他自动化脚本调用；`whichllm snippet` 可生成可直接粘贴使用的 Python 代码片段。

## 技术架构

`whichllm` 采用 Python 实现，核心设计思路是“一次扫描、实时排名”。运行时会执行以下步骤：

1. **硬件探测**：使用 `pynvml` 和 `psutil` 等库，配合系统工具，采集 GPU 显存、CUDA 核心数、CPU 线程数、可用 RAM 等信息。
2. **约束过滤**：从 HuggingFace 的公开模型元数据中，根据模型大小、量化格式（GGUF / GPTQ / AWQ）和许可类型，筛选出满足用户硬件约束的候选模型。
3. **基准排名**：拉取 Open LLM Leaderboard 或其他时效性强的基准评测数据，对候选模型按实际性能（如 MMLU、HumanEval 得分）进行排序，而非仅依据参数量。
4. **用户交互**：通过 Rich 库实现精美终端表格输出，支持颜色高亮和分页显示。

架构上强调“零配置”和“即时使用”，所有依赖通过 `uv` 或 `pip` 一次性安装，运行时无需连接外部依赖（除 HuggingFace API 外）。

## 安装与使用

**安装方式（任选其一）**：

```bash
# 推荐：使用 uv 一次性运行
uvx whichllm@latest

# 安装到系统（便于频繁使用）
uv tool install whichllm
# 或
pip install whichllm
# 或
brew install andyyyy64/whichllm/whichllm
```

**最小可用示例**：

```bash
# 直接获取当前硬件的推荐列表
$ whichllm
```

输出示例（假设机器配备 RTX 4090）：

```text
#1  Qwen/Qwen3.6-27B     27.8B  Q5_K_M   score: 0.92
#2  Mistral-7B-Instruct   7.0B   Q4_K_M   score: 0.88
#3  Llama-3-8B            8.0B   Q6_K     score: 0.86
```

其他常用命令：

```bash
# 模拟指定 GPU
whichllm --gpu "RTX 4090"

# 查看升级方案对比
whichllm upgrade "RTX 4090" "RTX 5090"

# 寻找运行某模型所需硬件
whichllm plan "llama 3 70b"

# 直接聊天
whichllm run "qwen 2.5 1.5b gguf"

# 生成 Python 代码片段
whichllm snippet "qwen 7b"
```

## 适用场景

- **硬件选购前的评估**：计划购买 GPU 时，用 `--gpu` 参数模拟不同显卡，提前了解哪些模型能跑、跑得有多快。
- **自有设备模型选型**：在现有笔记本或工作站上，快速找到兼顾性能与显存占用（如量化版本）的最佳模型。
- **CI/CD 自动化部署**：在模型部署流水线中，使用 `--json` 模式获取推荐结果，自动选择适合生产环境的模型。
- **教育与研究对比**：对比不同量化格式（GGUF vs GPTQ）在相同硬件上的效果差异，或验证新模型的实际可用性。

## 项目亮点

- **时效性驱动**：排名基于实时更新的开源基准评测数据，而非静态的参数量表。即使用户的硬件与某个模型理论兼容，但如果该模型的新版本性能下降，也会自动排到后面。
- **零配置原则**：相比手动翻查 HuggingFace 列表、手动计算显存占用，`whichllm` 只需一条命令，降低了本地 LLM 的使用门槛。
- **硬件模拟能力**：支持通过参数模拟任意 GPU 配置，这是其他同类工具（如单纯的 HuggingFace 模型浏览器）不具备的实用功能。
- **全流程覆盖**：从推荐、规划、比较到实际运行，一个工具完成从选型到对话的完整链路，不必在多个工具间切换。
- **活跃社区维护**：项目在 GitHub 上已获得 3600+ Stars，每日新增约 100+ Star，更新频率高，问题响应快。

## 相关链接

- [GitHub 仓库](https://github.com/Andyyyy64/whichllm)
- [PyPI 包页面](https://pypi.org/project/whichllm/)
