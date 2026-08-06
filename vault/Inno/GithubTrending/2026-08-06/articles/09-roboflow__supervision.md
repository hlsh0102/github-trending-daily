---
tags:
  - trending
  - article
repo: roboflow/supervision
date: 2026-08-06
language: Python
stars_total: 49009
stars_today: 146
---
## 项目概述

Supervision 是 Roboflow 团队开源的一套可复用的计算机视觉工具库，旨在帮助开发者快速构建、调试和部署视觉应用。它提供了从模型推理结果到可视化、过滤、跟踪和数据集处理的全流程工具，覆盖了计算机视觉项目中大量重复且繁琐的“非建模”工作。无论你正在使用 YOLOv8、RT-DETR 还是其他主流模型，Supervision 都能无缝接入，让你专注于模型和业务逻辑本身，而不是编写底层绘图和数据处理代码。项目当前在 GitHub 上拥有超过 4.9 万 Star，并持续保持较高的社区活跃度。

## 核心功能

- **多种预置标注器（Annotators）**：提供包括边界框、掩码、关键点、多边形、像素级分割等超过 20 种可视化标注器，支持对图像和视频帧进行快速标注，且所有标注器均支持批量处理。
- **模型结果统一接口**：通过 `sv.Detections` 和 `sv.mask` 等统一数据结构，将不同框架（如 Ultralytics YOLO、Transformers、Detectron2 等）的推理输出标准化，使切换模型时无需修改下游处理代码。
- **目标跟踪（Tracking）**：内置基于 ByteTrack 的跟踪器，只需一行代码即可为检测结果添加跨帧 ID 跟踪，并支持自定义轨迹绘制样式。
- **智能过滤与上下文管理**：提供按类别、置信度、区域（Zone）以及相对尺寸等条件对检测结果进行过滤的能力，并可结合上下文分析（如统计区域进出人数）实现业务逻辑。
- **数据集加载与处理**：内置对 COCO 和 YOLO 数据集格式的加载、采样、拆分以及标注转换功能，支持将检测结果直接导出为数据集，用于迭代训练。
- **视频与实时流处理**：提供基于生成器的视频帧读取、处理与写入接口，可轻松集成到摄像头或视频文件流中，实现实时或离线的分析流程。

## 技术架构

Supervision 采用纯 Python 编写，核心设计理念是“结果标准化”与“功能解耦”。所有模型输出首先被转换为统一的 `Detections` 数据结构（包含边界框、掩码、类别、置信度、跟踪器 ID 等信息），后续的标注、过滤、跟踪等所有操作均基于该结构进行。这种设计使得 Supervision 与具体模型框架彻底解耦，用户既可选择项目自带的加载器，也可以手动构建 `Detections` 对象以适应任意自定义模型。

在底层实现上，标注器主要依赖 OpenCV 和 NumPy 进行高效的图像处理与数组运算，保证了在大量目标下的性能。跟踪模块则集成了 byte_tracker 库，实现了高效的在线多目标跟踪。此外，项目通过优秀的模块化设计，让每个功能组件（如标注器、跟踪器、数据加载器）都可以独立使用，也可自由组合成完整的工作流。项目还提供了官方 Colab 笔记本和在线注解器演示，方便用户快速体验和集成。

## 安装与使用

Supervision 已发布至 PyPI，可通过 pip 直接安装。基础安装仅包含核心依赖（NumPy、OpenCV、Pydantic、PyYAML 等），若需使用跟踪或数据集加载功能，可安装对应扩展依赖。

```bash
# 基础安装
pip install supervision

# 安装跟踪功能依赖 (如果需要使用 ByteTrack)
pip install supervision[track] 

# 或安装全部额外依赖（用于开发或使用所有功能）
pip install supervision[dev]
```

以下是一个使用 Ultralytics YOLOv8 模型 + Supervision 进行视频标注并输出的最小示例：

```python
import cv2
import supervision as sv
from ultralytics import YOLOv8

# 初始化模型和标注器
model = YOLOv8("yolov8n.pt")
box_annotator = sv.BoxAnnotator()

# 读取视频帧生成器
for frame in sv.get_video_frames_generator("input.mp4"):
    # 模型推理
    result = model(frame)[0]
    # 将推理结果转换为 supervision 标准格式
    detections = sv.Detections.from_ultralytics(result)
    
    # 使用标注器在帧上绘制结果
    annotated_frame = box_annotator.annotate(
        scene=frame, detections=detections)
    
    # 显示或保存帧
    cv2.imshow("Frame", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
```

更多示例（如跟踪、区域计数、数据集导出等）可在项目的官方文档和演示笔记本中找到。

## 适用场景

- **快速原型验证**：在短时间内将目标检测、分割模型的结果进行可视化，验证模型效果或调试模型输出，无需编写任何绘图代码。
- **视频监控与分析**：结合目标跟踪和区域过滤功能，实现人员/车辆计数、入侵检测、人流统计等实时视频分析系统。
- **自动化数据标注与准备**：利用模型进行初步推理，并将结果通过 `sv.Detections` 导出为 COCO 或 YOLO 格式数据集，辅助人工标注或进行自动标注（Auto Labeling）流程。
- **计算机视觉教学与实验**：作为教学工具，帮助学生或研究人员快速搭建视觉处理流水线，专注于算法本身的比较与改进。

## 项目亮点

- **模型无关的统一抽象**：核心的 `Detections` 数据结构屏蔽了底层模型差异，大大提高了代码复用性，这是其与一般可视化工具最显著的区别。
- **极高的开发效率**：从模型输出到带标注的视频或数据集，只需几行代码，极大缩短了从想法到验证的周期。
- **全面的功能覆盖**：从简单的画框到复杂的目标跟踪、区域统计和数据集管理，工具链完整，能满足大多数视觉项目需求。
- **活跃的社区与生态**：依托 Roboflow 生态（Notebooks、Inference、Autodistill 等），拥有丰富的教程、示例和社区支持，项目本身也保持了非常高的更新频率。

## 相关链接

- [GitHub 仓库](https://github.com/roboflow/supervision)
- [官方文档](https://supervision.roboflow.com)
- [在线标注器演示](https://huggingface.co/spaces/Roboflow/Annotators)
- [官方 Colab 快速上手](https://colab.research.google.com/github/roboflow/supervision/blob/main/demo.ipynb)
