---
tags:
  - trending
  - article
repo: hasaneyldrm/exercises-dataset
date: 2026-07-02
language: HTML
stars_total: 8634
stars_today: 2470
---
## 项目概述

Exercises Dataset 是一个面向开发者的结构化健身动作数据集与项目脚手架工具。项目包含 **1,324 个健身动作**的详尽元数据，涵盖动作名称、类别、目标肌群、所需器械、分步指导等信息，并提供 **6 种语言**（英语、西班牙语、意大利语、土耳其语、俄语、中文）的指令翻译。该项目旨在帮助开发者快速搭建健身类应用的数据库结构、API 代码或 LLM 提示词模板，而无需从零收集和整理健身数据。

目标用户为健身应用开发者、后端工程师、数据科学家以及需要结构化健身数据用于机器学习或 demo 项目的技术爱好者。

## 核心功能

- **结构化数据集**：提供 1,324 条健身动作记录的 JSON 格式数据，每条记录包含名称、类别、目标肌群、器械、详细分步指导等字段。
- **多语言支持**：指令说明覆盖 6 种语言（EN, ES, IT, TR, RU, ZH），便于构建国际化应用。
- **元数据字段完整**：每条数据包含 `media_id`（原始媒体引用）、肌肉组、身体部位等关键标签，方便分类和检索。
- **开发者脚手架**：数据集设计可直接用于生成数据库 Schema、REST API 端点或作为 LLM 微调的种子数据。
- **开源且可自由使用**：基于 ExerciseDB v1 数据源，通过 Kaggle 二次加工而来，遵循开放数据协议。
- **明确的归属声明**：项目清晰标注了数据来源与版权归属，避免法律风险。

## 技术架构

项目以 **JSON 文件** 作为核心数据存储格式（`data/exercises.json`），数据结构遵循一致的 Schema 设计。每条记录包含以下关键字段：

- `id`：唯一标识符
- `name`：动作名称（英文）
- `category`：动作类别（如力量、拉伸、有氧）
- `bodyPart`：主要身体部位
- `equipment`：所需器械
- `target`：目标肌群
- `secondaryMuscles`：辅助肌群
- `instructions`：分步指导（仅英文原始版本）
- `instructions_{lang}`：多语言翻译版本
- `media_id`：原始 ExerciseDB 媒体引用 ID

项目本身采用 **静态数据仓库** 形态，不包含运行时环境或框架。开发者可将其直接克隆到本地，或通过 Git Submodule 集成到自己的项目中。数据集与脚手架代码分离，便于按需使用。

## 安装与使用

### 安装

```bash
git clone https://github.com/hasaneyldrm/exercises-dataset.git
cd exercises-dataset
```

### 使用示例

**1. 直接读取 JSON 数据**（Python 示例）：

```python
import json

with open('data/exercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# 遍历前5个动作
for exercise in exercises[:5]:
    print(exercise['name'], exercise['target'], exercise['instructions_zh'])
```

**2. 生成数据库 Schema**（SQLite 示例）：

```sql
CREATE TABLE exercises (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    body_part TEXT,
    equipment TEXT,
    target TEXT,
    instructions_zh TEXT,
    instructions_en TEXT
);
```

**3. 用于 LLM 提示词**：

```
以下是一个健身动作数据集，请根据用户需求推荐合适的动作：
用户询问：锻炼胸肌的动作有哪些？
数据示例：{JSON记录}
```

## 适用场景

- **健身应用后端开发**：快速搭建包含动作百科、训练计划推荐等功能的应用数据库。
- **多语言健身平台**：利用现成的 6 种语言翻译，节省本地化开发时间。
- **健身 AI 助手指令微调**：基于结构化数据训练或微调 LLM，实现智能动作推荐与指导。
- **数据分析与可视化**：分析各类动作的肌肉群分布、器械使用频率等，用于运动科学研究或内容规划。

## 项目亮点

- **数据量大且结构化**：1,324 个动作远超市面上多数免费数据集，每条记录字段完整，可直接投入生产。
- **多语言开箱即用**：无需额外翻译工作，降低国际化应用门槛。
- **清晰的版权声明**：主动说明媒体文件未包含的原因和归属，避免开发者误用侵权资源。
- **开发者友好设计**：数据集可直接作为数据库迁移文件、API 响应示例或前端状态管理的初始数据。
- **活跃的社区关注**：GitHub 获 8,600+ Stars，今日新增超 2,400，证明项目在开发者中的受欢迎程度。

## 相关链接

- [GitHub 仓库](https://github.com/hasaneyldrm/exercises-dataset)
- [原始数据源 ExerciseDB API 文档](https://oss.exercisedb.dev/docs)
- [Kaggle 数据集来源](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset)
