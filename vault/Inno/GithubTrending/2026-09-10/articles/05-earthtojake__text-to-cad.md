---
tags:
  - trending
  - article
repo: earthtojake/text-to-cad
date: 2026-09-10
language: Python
stars_total: 15197
stars_today: 124
---
## 项目概述

text-to-cad 是一个面向 CAD、CAE 与 CAM 工作流的**智能体技能库（agent skills library）**。它将自然语言或本地工程文件作为输入，通过可组合的"技能"驱动智能体完成几何建模、检查、外部资源检索、切片以及向机器人描述文件的分发等任务。项目托管在 GitHub，采用 MIT 许可证，主语言为 Python。目标用户是需要将 AI 智能体能力引入机械设计、仿真与制造流程的工程师、机器人研究者以及构建工程 Copilot 类产品的开发者。

与传统的 CAD 自动化脚本相比，text-to-cad 并非提供单一 API，而是将 CAD / CAE / CAM 相关的操作拆解为若干带明确输入输出的技能模块，使其可被不同的智能体框架（如 Anthropic 的 Agent Skills 规范）直接调用。

## 核心功能

- **CAD 几何生成与预览**：从文本描述或项目文件生成参数化几何，并在内置的 CAD Viewer 中实时渲染，便于迭代验证。
- **模型检查与诊断**：对已有 CAD 文件进行结构检查，识别拓扑、尺寸或实体层面的问题。
- **资源来源检索（sourcing）**：对接标准件库或在线资源，为装配体补充可用的零部件。
- **切片与制造准备（slicing）**：将三维模型转换为可打印/可加工的切片数据，衔接增材制造流程。
- **机器人描述文件支持**：内置 URDF、SDF、SRDF 技能，将 CAD 成果导出为机器人仿真与运动规划所需的描述格式。
- **技能化交付（handoff）**：将上述各类产物以结构化方式交由下游智能体或流水线继续处理。

## 技术架构

项目以 **Python 包 + 技能清单（SKILL.md）** 的形式组织，每个技能目录（如 `skills/cad`、`skills/urdf`、`skills/sdf`、`skills/srdf`）都包含：

1. 一份描述技能能力、输入输出与使用约束的 `SKILL.md` 元文档；
2. 一个独立的 `requirements.txt`，用于声明该技能独有的依赖；
3. 实现该技能的 Python 代码。

这种"按技能隔离依赖"的设计使 CAD、URDF、SDF 等模块可独立安装、升级或替换，避免了整体式工具链常见的依赖冲突。整套库遵循 Agent Skills 规范，因此能被支持该规范的智能体运行时直接发现与调用。渲染与可视化部分依托几何内核完成，并通过本地 Viewer 呈现结果。仓库使用 GitHub Actions 进行持续测试。

## 安装与使用

基本安装流程如下（Python 3.10+）：

```bash
# 克隆仓库
git clone https://github.com/earthtojake/text-to-cad.git
cd text-to-cad

# 安装 CAD 技能的依赖（按需选择技能目录）
pip install -r skills/cad/requirements.txt
```

最小可用示例（示意）：

```python
from text_to_cad.skills.cad import CadSkill

skill = CadSkill(workspace="./output")
result = skill.generate("一个 40x40x10 mm 的底座，四角带 M3 沉孔")
print(result.file_path)
```

具体 API 与调用方式请以 `skills/cad/SKILL.md` 及各技能目录中的说明为准。官方文档站提供了完整的技能列表与示例。

## 适用场景

- **AI 辅助机械设计**：在设计早期用自然语言快速生成概念几何并迭代。
- **机器人仿真建模**：从 CAD 模型批量导出 URDF / SDF / SRDF，用于运动规划与仿真环境搭建。
- **增材制造流程**：对模型进行检查与切片，直接对接 3D 打印准备。
- **工程 Copilot 产品开发**：将技能库集成到自研智能体中，作为 CAD/CAE/CAM 领域的能力插件。

## 项目亮点

- **技能粒度清晰**：CAD、URDF、SDF、SRDF 各自成模块，支持按需加载，避免全量依赖。
- **面向智能体规范而非单一框架**：遵循 Agent Skills 约定，便于跨运行时复用。
- **覆盖设计到制造的完整链路**：从生成、检查、检索到切片与描述文件导出，形成端到端闭环。
- **工程化程度较高**：每个技能独立声明依赖，配合 CI 测试，便于在真实项目中维护。

## 相关链接

- [GitHub 仓库](https://github.com/earthtojake/text-to-cad)
- [官方文档](https://www.texttocad.dev)
- [Discord 社区](https://discord.gg/5FGB9DwJYU)
