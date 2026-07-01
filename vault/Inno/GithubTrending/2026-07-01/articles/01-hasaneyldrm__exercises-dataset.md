---
tags:
  - trending
  - article
repo: hasaneyldrm/exercises-dataset
date: 2026-07-01
language: HTML
stars_total: 7320
stars_today: 1343
---
## 项目概述

Exercises Dataset 是一个面向开发者的结构化健身运动数据集仓库，包含 1,324 项运动的结构化数据。每项运动都涵盖了分类、身体部位、目标肌群、所需器材、动作说明等核心信息，并提供了 6 种语言（英语、西班牙语、意大利语、土耳其语、俄语、中文）的逐步指导翻译。该项目旨在帮助开发者快速搭建健身类应用的后端基础，包括数据库 Schema、API 代码和 LLM 提示工程模板。仓库近期获得了显著关注（7,320 颗星，单日增长 1,343 颗）。

## 核心功能

- **广泛覆盖**：包含 1,324 项健身运动，涵盖多种分类和身体部位。
- **多语言支持**：每项运动均有 6 种语言的逐步指导翻译（EN、ES、IT、TR、RU、ZH），便于构建国际化应用。
- **结构化元数据**：每条记录包含名称、类别、目标肌群、所需器材、分类标签（category、body-part、equipment、target、muscle-group）。
- **媒体引用标识**：每条记录保留 `media_id` 字段，指向原始 ExerciseDB 媒体资源，方便开发者自行获取或关联媒体文件。
- **开发者工具导向**：一次性提供 DB Schema 设计思路、API 代码示例和 LLM 提示模板，加速从数据到应用的开发流程。
- **原始数据溯源**：数据基于 ExerciseDB v1（AscendAPI）并经 Kaggle 二次发布，确保了数据质量与可追溯性。

## 技术架构

项目主要数据存储为 JSON 格式（`data/exercises.json`），便于程序读取和解析。数据集的设计考虑了以下架构特点：

- **抽象化媒体层**：由于运动媒体（缩略图、动画 GIF）存在权益争议，项目将媒体引用与元数据分离，使用 `media_id` 作为引用标识。开发者需要自行获取或替换媒体文件，避免了版权风险。
- **语言分离**：指令翻译作为每项运动记录的独立字段存储（如 `instructions_en`、`instructions_es` 等），支持按需加载不同语言版本。
- **分类标准化**：类别、身体部位、器材、目标肌群均使用标准化的标签体系（如 `body-part`、`equipment`），便于数据库建模和 API 查询。
- **开发脚手架属性**：项目不仅仅是数据集，更是一个“开发设置向导”，引导开发者完成从原始数据到后端服务的搭建过程，包括数据库 Schema 设计、API 代码生成和 LLM 提示优化。

## 安装与使用

1. **获取数据集**：直接克隆或下载仓库，数据文件位于 `data/exercises.json`。
2. **选择所需语言**：在代码中解析 JSON，根据需求提取指定语言的指令字段（如 `instructions_zh`）。
3. **集成媒体（可选）**：如需使用媒体资源，需根据 `media_id` 自行获取或替换。常见的做法包括：
   - 使用 ExerciseDB API 获取原始媒体链接。
   - 替换为自行录制的运动演示视频/图片。
   - 在应用中留空，仅展示文字说明。
4. **构建数据库**：将 JSON 数据导入支持 JSON 字段的数据库（如 MongoDB、PostgreSQL 的 JSONB 列）或拆分为关系表（如 exercises表、translations表、muscle_groups表）。
5. **编写 API**：基于数据 Schema 编写 RESTful 或 GraphQL API，支持查询、过滤和分页。
6. **集成 LLM**：将数据结构传递给 LLM，用于生成个性化训练计划、运动推荐等高级功能。

**最小可用示例**（Python）：
```python
import json

with open('data/exercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# 查询所有锻炼胸肌的运动
chest_exercises = [ex for ex in exercises if 'chest' in ex.get('target_muscle_group', '').lower()]

# 打印名称和中文说明
for ex in chest_exercises[:5]:
    print(f"{ex['name']}: {ex.get('instructions_zh', '')[:50]}...")
```

## 适用场景

- **健身应用开发**：作为运动数据库的核心，支撑动作库搜索、过滤和展示功能。
- **多语言健康平台**：利用 6 种语言的支持，为全球用户提供本地化的锻炼指导。
- **AI 健身教练**：将结构化数据馈入 LLM，生成个性化训练计划，或与动作识别模型结合，实现实时动作纠正。
- **数据科学项目**：作为健身运动元数据的基准数据集，用于分类、聚类或推荐系统的研究与实验。

## 项目亮点

- **数据版权免责设计**：明确分离元数据与媒体文件，解决了常见健身数据集中的版权隐患，开发者无需担心媒体资源的合法性。
- **多语言一键集成**：无需额外翻译工作即可提供 6 种语言的运动说明，极大降低国际化门槛。
- **开发脚手架而非单纯数据**：不仅给出数据，还提供了从数据库设计到 API 编写的思路，节省了架构决策时间。
- **高活跃度与社区验证**：7,320 颗星和单日 1,000+ 的增长表明项目得到了开发社区的认可。

## 相关链接

- [GitHub 仓库](https://github.com/hasaneyldrm/exercises-dataset)
- [原始 ExerciseDB v1 文档](https://oss.exercisedb.dev)
- [原始 ExerciseDB API 文档](https://oss.exercisedb.dev/docs)
- [Kaggle 数据源](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset)
