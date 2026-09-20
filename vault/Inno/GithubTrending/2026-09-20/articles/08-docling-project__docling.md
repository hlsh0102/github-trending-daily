---
tags:
  - trending
  - article
repo: docling-project/docling
date: 2026-09-20
language: Python
stars_total: 67263
stars_today: 129
---
## 项目概述

Docling 是一个由 docling-project 组织维护的开源文档处理工具库，采用 Python 编写，基于 MIT 许可证发布。项目的核心定位是“为生成式 AI 准备文档”，即把各种来源的文档转换为结构化、可供大语言模型或检索系统直接消费的数据。

在实际工作中，PDF、DOCX、PPTX、XLSX 等格式虽然便于人类阅读，但对机器并不友好：版面复杂、表格嵌套、阅读顺序含糊，直接投喂给模型往往效果不佳。Docling 正是为解决这一环节而生，它负责解析多种文档格式并输出统一的文档表示，包括文本、表格、图片以及版面结构信息。其目标用户主要是构建 RAG 系统、文档问答、知识抽取或数据清洗流水线的开发者与研究者。

项目附带学术论文（arXiv:2408.09869），并被纳入 LF AI & Data 基金会，具备一定的社区治理基础。

## 核心功能

- **多格式解析**：支持 PDF、DOCX、PPTX、XLSX、HTML、EPUB、Apple Pages、Box Notes，以及邮件格式；此外还支持 WAV、MP3、WebVTT 等音频与字幕类输入。
- **高级 PDF 理解**：针对 PDF 提供版面分析、阅读顺序还原、表格结构识别与图片提取，能处理传统纯文本抽取工具难以应对的复杂文档。
- **统一文档模型**：解析结果被转换为一致的结构化表示，方便后续在多种下游任务中复用，而非每种格式各自为政。
- **生成式 AI 生态集成**：可与主流 LLM 框架、向量数据库及检索流程对接，支持将文档直接转换为 Markdown、JSON 等便于索引的格式。
- **可选 OCR 与模型增强**：对扫描件或图像型 PDF，可通过 OCR 与视觉模型补充识别能力，提升覆盖范围。
- **命令行与编程接口并存**：既提供 CLI 便于快速试用，也提供 Python API 便于嵌入既有工程。

## 技术架构

Docling 采用模块化的流水线设计。输入文档先经过格式识别，再进入对应的后端解析器；PDF 路径会额外经过版面分析与表格识别模型，这些模型以预训练权重形式提供，可按需下载。解析完成后，系统将内容归一化为统一的文档对象模型，描述页面、文本块、表格、图片及其层级关系。

这种“解析后端 + 统一模型”的分层思路，使得新增格式或替换模型时不必改动上层调用代码。项目使用 Pydantic 做数据建模与校验，构建与依赖管理方面可见对 uv、ruff 等现代 Python 工具链的采用，说明工程实践较为规范。整体依赖按功能可选安装，避免基础安装体积过大。

## 安装与使用

基础安装可通过 pip 完成：

```bash
pip install docling
```

若需要 OCR 或特定格式的额外能力，可安装对应的可选依赖组。使用 Python API 的最小示例如下：

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("sample.pdf")
print(result.document.export_to_markdown())
```

也可以使用命令行：

```bash
docling sample.pdf
```

首次运行涉及 PDF 解析时可能需要下载模型文件，请确保网络可用。具体参数、支持的格式清单与进阶用法请以官方文档为准。

## 适用场景

- **RAG 与知识库构建**：将企业内部 PDF、Word、PPT 资料批量转换为 Markdown 或结构化 JSON，作为向量库的数据源。
- **文档问答系统**：在解析阶段保留表格与版面信息，使模型回答能引用准确的结构化上下文。
- **数据抽取与合规处理**：从合同、报告、财务表格中抽取字段，供后续分析或审计使用。
- **学术与科研数据处理**：批量处理论文与报告，提取正文、图表与引用结构。

## 项目亮点

与常见的纯文本抽取工具相比，Docling 的差异主要体现在三点：一是格式覆盖面广，且对 PDF 这类难点格式有专门的版面与表格处理；二是输出统一模型，减少下游适配成本；三是与生成式 AI 生态的衔接较为直接，转换结果可直接用于索引与推理。此外，项目有论文支撑、有基金会背书、社区活跃度高（GitHub 星标已超过 6.7 万），在文档解析这一细分方向上属于少数兼具工程完整性与研究背景的选择。

## 相关链接

- [GitHub 仓库](https://github.com/docling-project/docling)
- [官方文档](https://docling-project.github.io/docling/)
- [PyPI 包](https://pypi.org/project/docling/)
- [技术论文（arXiv:2408.09869）](https://arxiv.org/abs/2408.09869)
- [Discord 社区](https://docling.ai/discord)
