---
tags:
  - trending
  - article
repo: uber/ADR
date: 2026-08-05
language: Python
stars_total: 760
stars_today: 148
---
## 项目概述

ADR（Agentic AI Detection and Response）是 Uber 开源的一套企业级 AI 代理安全防护系统，专门用于保护组织内部面向员工和客户的 AI 代理。随着 Cursor、Claude Code、Codex 等 AI 编程工具以及各类 AI 客服代理的普及，组织面临的 AI 安全风险急剧上升——这些代理可以自主执行操作、访问敏感数据，但传统安全工具无法观测和防护这类新型攻击面。

ADR 解决了三个核心问题：企业无法完整观测 AI 代理的行为、缺乏针对 AI 代理攻击的防御能力评测基准、难以在攻击造成损失前进行有效检测。该项目已在 Uber 生产环境部署，相关论文被 MLSys 2026 接收，开源版本采用 Apache-2.0 许可证。

## 核心功能

ADR 通过四项互补能力构建完整的 AI 代理安全防线：

- **观测（Observability）**：在 macOS、Linux 和 Windows 平台上捕获 7 种以上 AI 编程工具（如 Cursor、Claude Code、Codex）的代理意图、工具调用和执行轨迹，同时支持内部自动化代理和客户支持代理的观测。
- **基准测试（Benchmark）**：提供 ADR-Bench 安全评测集，包含 300 多个测试任务、133 个 MCP（Model Context Protocol）服务器，完整覆盖 17 种代理攻击技术，帮助组织评估自身 AI 代理环境的安全态势。
- **威胁检测（Detection）**：采用两级检测架构——第一级通过高召回率快速分诊所有代理会话，第二级针对可疑会话进行更深层次的代理推理分析，在保证检出率的同时控制计算成本。
- **防护（Prevention）**：在 unsafe 操作造成实际损害前进行阻断。该模块暂未包含在当前开源版本中，官方表示将持续推出。

## 技术架构

ADR 的设计体现了几个关键架构决策：

首先是**跨平台代理观测层**，通过统一的遥测采集接口适配 macOS、Linux、Windows 三种操作系统，以及多样化的 AI 代理工具。采集的数据不仅包括常规的工具调用日志，还包括代理的“意图”信息，这使得安全团队能够理解代理为什么执行某项操作，而非仅仅看到操作结果。

其次是**两阶段检测流水线**。第一阶段使用轻量级、高召回率的分类模型对每个会话进行快速分诊，标记可能存在的风险；第二阶段仅对标记的会话调用大语言模型进行推理式分析，模拟安全分析师的思维过程来判断是否确实存在威胁。这种设计平衡了检测准确率和推理成本，使大规模生产部署成为可能。

第三是**安全基准即基础设施**。ADR-Bench 并非简单的测试集，而是包含真实 MCP 服务器和可复现攻击场景的评测环境，覆盖全部已收录的代理攻击技术分类。这使安全团队能够持续测试新出现的防御策略。

## 安装与使用

以下是一个基于 Python 环境的基本使用流程：

```bash
# 克隆仓库
git clone https://github.com/uber/ADR.git
cd ADR

# 安装依赖
pip install -r requirements.txt
```

**最小观测示例：**

```python
from adr.observability import ADRObserver

# 初始化观测器（以 macOS 上的 Cursor 为例）
observer = ADRObserver(tool="cursor", platform="macos")
observer.start()

# 读取捕获的代理执行事件
for event in observer.poll_events():
    print(event.tool_call, event.intent, event.timestamp)
```

**运行安全基准测试：**

```bash
# 运行 ADR-Bench 中的全部测试
python -m adr.benchmark run --full

# 运行指定攻击技术类别的测试
python -m adr.benchmark run --technique prompt-injection
```

具体配置和 API 细节请参考仓库内 README 与 `docs/` 目录下的论文和演示材料。

## 适用场景

- **企业 AI 开发工具安全治理**：对员工使用的 Cursor、Claude Code、Codex 等编程代理进行行为审计和越权操作检测，防止敏感代码泄露或未经授权的仓库修改。
- **客户支持 AI 代理防护**：观测面向用户的 AI 客服代理，检测提示注入攻击、数据越权访问或恶意指令执行，保护客户隐私和企业服务稳定性。
- **AI 安全能力评估与合规**：利用 ADR-Bench 对组织的 AI 代理环境进行安全基线评测，并为安全团队提供可量化的防御效果指标。
- **安全运营中心（SOC）扩展**：将 ADR 的检测结果接入现有 SIEM 或 SOAR 平台，让安全分析人员获得 AI 代理维度的威胁可见性。

## 项目亮点

与其他 AI 安全工具相比，ADR 的主要差异化优势体现在：

- **生产验证**：已在 Uber 大规模生产环境部署，非实验室原型。MLSys 2026 论文提供了架构思路和部署经验的系统总结。
- **全类型代理覆盖**：同时支持员工侧（编程工具）和客户侧（支持代理）两类常见的 AI 代理，覆盖面广。
- **可量化的评测基准**：完整的 17 种攻击技术覆盖和 300+ 任务的 ADR-Bench，使安全团队能够用统一标准衡量不同防御方案的效果。
- **成本可控的两级检测架构**：通过分诊与深度推理的分离，在有限推理预算下实现高检出率，这对生产环境的可扩展性至关重要。
- **全平台支持**：macOS、Linux、Windows 三平台覆盖，适配多样化的企业终端环境。

## 相关链接

- [GitHub 仓库](https://github.com/uber/ADR)
- [论文 PDF](docs/adr-paper.pdf)
- [MLSys 2026 演示材料](docs/adr-mlsys-2026-slides.pdf)
