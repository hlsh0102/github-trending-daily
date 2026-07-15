---
tags:
  - trending
  - article
repo: hasaneyldrm/exercises-dataset
date: 2026-07-15
language: HTML
stars_total: 13716
stars_today: 851
---
## 项目概述

Exercises Dataset 是一个开源的健身动作数据集，包含 1,324 个精心整理的训练动作。每个动作都配有动画 GIF 演示、180×180 像素缩略图，以及详细的肌肉群、器械分类数据。该数据集同时提供 9 种语言（英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语、韩语）的分步指导说明。项目最初作为健身追踪应用 LogPress 的数据层而创建，现已独立发布，供任何需要结构化健身动作数据的开发者使用。

## 核心功能

- **完整的动作数据**：覆盖 1,324 个健身动作，包含类别、身体部位、器械、目标肌群等结构化字段
- **视觉化演示**：每个动作均配备高质量动画 GIF 和 180×180 缩略图，便于快速预览和理解动作要领
- **多语言支持**：分步指导说明提供 9 种语言版本，降低国际使用的门槛
- **标准化数据结构**：以 JSON 格式组织数据，包含 `category`、`bodyPart`、`equipment`、`target`、`muscleGroup` 等核心字段
- **即拿即用**：数据集可直接嵌入任何后端服务，无需额外处理或转换
- **开源授权**：采用宽松的授权协议，允许商业和非商业使用

## 技术架构

项目采用纯数据驱动架构，核心数据存储在 `data/exercises.json` 文件中。每个动作条目包含：

- 唯一标识符
- 动作名称（中英文对照）
- 分类标签（力量、有氧、拉伸等）
- 身体部位定位（胸、背、腿、肩等）
- 所需器械（杠铃、哑铃、弹力带、自重等）
- 目标肌群与协同肌群
- 动作描述与分步指导

视觉媒体文件按类型分别存储在 `videos/` 和 `images/` 目录，使用哈希文件名避免冲突。项目没有复杂的构建流程，采用纯 HTML/CSS 进行展示，最大程度降低维护成本。

## 安装与使用

1. **克隆仓库**
```bash
git clone https://github.com/hasaneyldrm/exercises-dataset.git
cd exercises-dataset
```

2. **访问数据**
```python
import json

with open('data/exercises.json', 'r', encoding='utf-8') as f:
    exercises = json.load(f)

# 查看第一个动作
print(exercises[0]['name'])
print(exercises[0]['instructions']['en'])
```

3. **使用演示文件**
```html
<!-- 直接在 HTML 中引用 GIF -->
<img src="videos/0025-EIeI8Vf.gif" alt="Barbell Bench Press" width="120" />
```

4. **集成到后端**：将 `exercises.json` 文件导入数据库或直接作为静态数据服务。参考 LogPress 项目的集成方式，可在其源码中看到完整的使用示例。

## 适用场景

- **健身应用开发**：为 workout tracker、健身计划生成器、AI 教练等应用提供标准化的动作数据库
- **教学与研究**：体育院校、健身培训机构可用于制作教学材料或动作分析研究
- **内容创作**：健身博主或内容平台使用动画和说明制作演示内容
- **智能硬件**：与智能镜、体感摄像头等设备结合，提供动作库支持

## 项目亮点

- **数据完整性**：1,324 个动作覆盖了主流健身动作的绝大多数，且每个动作都有完整的视觉和文本信息
- **开箱即用**：无需爬取、整理或翻译，直接 JSON 加载即可使用
- **高质量视觉素材**：动画 GIF 由专业人员制作，动作标准、清晰，避免自行录制的高昂成本
- **持续更新**：项目作为 LogPress 的基础数据层，会随着应用发展不断补充新动作
- **社区驱动**：已有 13,000+ 星标，活跃的社区贡献者持续完善数据质量

## 相关链接

- [GitHub 仓库](https://github.com/hasaneyldrm/exercises-dataset)
- [LogPress 应用](https://github.com/hasaneyldrm/logpress-public)
- [Gym Visual](https://gymvisual.com/)（媒体素材来源）
