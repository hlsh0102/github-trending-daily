---
tags:
  - trending
  - article
repo: apache/ossie
date: 2026-07-17
language: Python
stars_total: 984
stars_today: 60
---
## 项目概述

Apache Ossie（孵化中）是一项由 Apache 软件基金会主导的行业级标准化规范，旨在解决数据分析、人工智能与商业智能生态系统中语义元数据交换的碎片化问题。该项目原名 **Open Semantic Interchange (OSI)**，致力于建立一套通用的、厂商中立的语义模型规范，成为数据定义与价值的单一真实来源。

随着数据工具链日益复杂，同一关键绩效指标在各平台间定义不一致，团队人工协调定义消耗大量精力，AI 代理因底层业务逻辑不统一而产生不可靠的产出——这些问题已成为数据驱动决策的核心瓶颈。Apache Ossie 通过统一的 JSON 与 YAML 规范，让任何工具都能读写同一份语义元数据，从根本上消除跨工具间的定义不一致性。项目面向数据工程师、分析平台开发者、AI 应用构建者以及任何需要确保语义一致性的团队。

## 核心功能

- **单一语义规范**：提供基于 JSON 与 YAML 的标准化语义模型定义，涵盖指标、维度、实体及其关系的完整描述，支持跨工具无缝交换。
- **机器可读 Schema**：内置 `osi-schema.json` 与 `spec.yaml` 两种格式的机器可读规范，便于自动化验证与工具集成。
- **参考转换器**：在 `converters/` 目录下提供将 Ossie 规范与其他语义格式（如 dbt metrics、LookML 等）互转的参考实现，降低迁移成本。
- **平台无关性**：规范本身不绑定任何特定数据库、分析引擎或编程语言，可通过 HTTP、文件系统或消息队列等任意方式传输。
- **可扩展描述能力**：支持嵌套定义、多语言标签、时序属性与血缘关系映射，适应现代数据场景中复杂的业务语义。

## 技术架构

Apache Ossie 采用**以规范为核心、转换器为辅助**的架构设计：

- **核心规范层**：位于 `core-spec/` 目录，包含人类可读的规范文档 `spec.md`，以及两份机器可读的 Schema 定义——`spec.yaml`（YAML 版本）与 `osi-schema.json`（JSON Schema 版本）。所有语义模型均遵循此规范，确保不同工具间的一致性。
- **格式转换层**：`converters/` 目录下的参考转换器实现了 Ossie 规范与其他流行语义格式（如 dbt、Metabase 自定义指标、Tableau 语义层）的互相转换。这些转换器可作为独立库使用，也可作为其他工具集成的参考实现。
- **协议无关传输**：规范本身不定义传输协议，任何能够传递 JSON/YAML 内容的机制（REST API、消息队列、文件共享）均可承载语义元数据交换。
- **验证工具**：项目计划提供标准化的规范验证器，允许用户检查其语义模型是否严格符合 Ossie 规范，确保互操作性。

整体采用 Python 语言实现转换器与配套工具，保持低依赖与高可移植性，便于嵌入各类数据基础设施。

## 安装与使用

Apache Ossie 目前处于孵化阶段，核心规范已在 `core-spec/` 目录下稳定。要开始使用：

1. **获取规范**：从仓库 `core-spec/spec.md` 阅读完整规范文档，从 `core-spec/spec.yaml` 或 `osi-schema.json` 获取机器可读 Schema。
2. **安装转换器**：克隆仓库后，在 `converters/` 目录下运行：
   ```bash
   pip install -r requirements.txt
   ```
3. **创建语义模型**：按照规范编写 `.osi.yaml` 或 `.osi.json` 文件，例如一个简单指标定义：
   ```yaml
   version: "1.0"
   metrics:
     - name: revenue
       description: Total revenue from orders
       expression: SUM(orders.amount)
       dimensions:
         - date
         - region
   ```
4. **转换现有格式**：使用转换器将已有的 dbt metrics、Metabase 指标等转换为 Ossie 格式：
   ```bash
   python converters/dbt_to_ossie.py --input metrics.yml --output output.osi.json
   ```

## 适用场景

- **统一企业级语义层**：大型组织中不同团队使用 Power BI、Tableau、Looker 等多种 BI 工具时，确保同一指标（如“月活跃用户”）在各工具中定义完全相同。
- **AI 代理语义 grounding**：为 AI 查询代理提供一致的业务定义，避免因不同工具间语义冲突导致的输出不可靠，例如让 LLM 根据统一规范生成 SQL 查询。
- **数据产品交换**：数据市场或数据云平台需要交换跨组织的语义模型时，使用 Ossie 作为交换格式，无需强制双方使用同一工具。
- **工具迁移与异构集成**：从一种分析平台迁移至另一种时，保留原有的业务语义定义，无需重新手动定义所有指标。

## 项目亮点

- **行业级统一规范**：由 Apache 孵化器主导，旨在成为跨平台、跨厂商的行业标准，而非某个单一工具的私有扩展。
- **极简依赖**：核心规范仅依赖 JSON/YAML，转换器保持 Python 低依赖，可轻松嵌入任何技术栈。
- **聚焦语义本身**：不定义数据存储、计算引擎或可视化方式，只关注“业务含义是如何定义的”，与现有工具解耦。
- **社区驱动演进**：作为开放标准，规范与转换器均接受来自任何组织的贡献，确保其通用性与前瞻性。
- **消除重复工作**：从根本上解决团队因同一指标在各工具中定义不同而导致的维护成本与数据信任问题。

## 相关链接

- [GitHub 仓库](https://github.com/apache/ossie)
- 项目文档与规范：参照仓库 `core-spec/spec.md` 及 `docs/` 目录（孵化中）
