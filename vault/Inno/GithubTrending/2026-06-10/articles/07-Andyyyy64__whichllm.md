---
tags:
  - trending
  - article
repo: Andyyyy64/whichllm
date: 2026-06-10
language: Python
stars_total: 4235
stars_today: 633
---
## 项目概述

`whichllm` 是一个轻量级命令行工具，旨在帮助用户快速找到能在本地硬件上实际运行且性能最佳的本地大语言模型。它自动检测用户系统的 GPU、CPU 和 RAM 信息，然后从 HuggingFace 上实时检索并排名适合该硬件的模型。该工具根据真实、具备时效性的基准评测结果进行排序，而不是依赖参数量等笼统指标。用户只需执行一条命令即可获得推荐结果，无需繁琐的项目配置。目标用户包括希望在本地部署 LLM 的开发者、机器学习爱好者、需要对比不同 GPU 升级方案的硬件采购人员，以及希望快速评估模型兼容性的研究人员。

## 核心功能

- **硬件自动检测与模型推荐**：自动识别当前机器的 GPU、CPU 和 RAM 配置，实时从 HuggingFace 检索并排名适合该硬件的模型，输出按性能、量化等级和社区评分排序的结果。
- **硬件模拟与升级对比**：支持指定任意 GPU 型号（如 `--gpu "RTX 4090"`）模拟其推理能力，方便在购买硬件前预览推荐模型；`upgrade` 子命令可同时对比多款显卡（如 `RTX 4090`、`RTX 5090`、`H100`）的推荐模型差异。
- **模型反向查询规划**：通过 `plan` 子命令，输入具体模型名称（如 `"llama 3 70b"`）即可反查需要什么样的硬件（GPU/RAM 规格）才能运行该模型。
- **一键运行与代码片段生成**：`run` 子命令可直接启动模型对话体验；`snippet` 子命令生成可直接复制粘贴的 Python 调用代码，便于集成到脚本或应用中。
- **JSON 输出与脚本友好**：支持 `--json` 标志和 `--top N` 参数，可直接输出结构化 JSON 结果，供自动化脚本或 CI/CD 流水线使用。

## 技术架构

`whichllm` 采用 Python 实现，核心架构围绕“硬件检测—模型匹配—实时排名”三个环节设计。硬件检测模块通过系统 API 读取 GPU 显存、CPU 内存及架构信息，在 Linux/macOS/Windows 上均能正常工作。模型匹配逻辑基于 HuggingFace 的 API 实时搜索，根据参数量、量化版本（如 GGUF Q5_K_M）和内存占用约束自动过滤不兼容项。排名算法融合了社区评分（如模型打分、下载量）与具备时效性的基准评测数据，而非简单依赖参数量。工具本身打包为 Python 包，支持通过 `uv` 一键运行（无需安装）、`pip` 安装或 Homebrew 安装，并将依赖局限在最小范围内（仅需 Python 3.10+ 和核心网络/HuggingFace 客户端库），确保启动速度快、占用空间小。

## 安装与使用

安装方式灵活，共支持四种方式：

```bash
# 方式一：无需安装，直接运行
uvx whichllm@latest

# 方式二：安装为本地工具（推荐频繁使用）
uv tool install whichllm
uv tool upgrade whichllm  # 更新已安装版本

# 方式三：Homebrew（macOS/Linux）
brew install andyyyy64/whichllm/whichllm

# 方式四：pip
pip install whichllm
```

安装后，可立即执行以下典型命令：

```bash
# 自动检测本机硬件并推荐最佳模型
whichllm

# 模拟使用 RTX 4090 时的推荐模型
whichllm --gpu "RTX 4090"

# 对比 RTX 4090、RTX 5090 和 H100 的推荐差异
whichllm upgrade "RTX 4090" "RTX 5090" "H100"

# 查询运行 llama 3 70B 所需的推荐硬件
whichllm plan "llama 3 70b"

# 直接启动与 qwen 2.5 1.5b GGUF 模型的对话
whichllm run "qwen 2.5 1.5b gguf"

# 为 qwen 7B 模型生成可复制的 Python 代码片段
whichllm snippet "qwen 7b"

# 返回前 1 个推荐模型的 JSON 格式结果（方便脚本解析）
whichllm --top 1 --json
```

## 适用场景

- **本机模型选型**：开发者或研究者希望快速找到能在自己本地计算机（如个人笔记本或工作站）上流畅运行的 LLM 模型，避免逐个下载测试。
- **硬件采购决策**：企业或个人在计划升级或采购 GPU（如 RTX 4090、H100）前，使用 `--gpu` 或 `upgrade` 子命令预估不同显卡的模型支持情况和性能差异，辅助预算分配。
- **模型部署前规划**：团队在部署特定模型（如 `llama 3 70b`）前，通过 `plan` 子命令了解所需的最低硬件规格，确保基础设施满足要求。
- **自动化 CI/CD 与脚本集成**：运维人员或 MLOps 工程师在构建自动化的模型部署流水线时，使用 `--json` 输出将推荐结果集成到监控、调度或自动化报告系统中。

## 项目亮点

- **真正的硬件适配**：许多同类工具仅按参数量粗略推荐，`whichllm` 结合显存/内存约束、推理框架兼容性以及社区实时评分，提供真正“能运行”且“性能好”的模型。
- **零配置一键启动**：无需安装、无需配置环境变量或项目结构，一条命令直接给出结果，大幅降低使用门槛。
- **硬件模拟与反向查询**：支持在无实际硬件的情况下模拟不同 GPU 的推荐结果，以及从模型反查所需硬件，将选型流程从单向变为双向，灵活性远超同类工具。
- **持续维护与社区活跃**：项目仓库目前收获了超过 4200 星标，社区活跃度高，支持多语言文档（中文、日文），并有持续的自动化测试保障质量。

## 相关链接

- [GitHub 仓库](https://github.com/Andyyyy64/whichllm)
- [PyPI 包](https://pypi.org/project/whichllm/)
- [日文版文档](https://github.com/Andyyyy64/whichllm/blob/main/docs/README.ja.md)
