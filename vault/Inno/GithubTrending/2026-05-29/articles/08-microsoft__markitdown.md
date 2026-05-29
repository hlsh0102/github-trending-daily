---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-05-29
language: Python
stars_total: 128129
stars_today: 1410
---
## 项目概述

MarkItDown 是由微软开源的一款轻量级 Python 工具，旨在将多种常见文档格式和文件类型转换为 Markdown 格式。该项目主要服务于大语言模型（LLM）及其相关的文本分析管道，解决了不同格式文档难以统一处理的问题。目标用户包括 AI 开发者、数据分析师、知识管理工作者以及任何需要从非结构化文档中提取结构化文本内容的专业人士。通过将 PDF、Word、Excel、PowerPoint 等文件转换为统一的 Markdown 格式，MarkItDown 显著降低了预处理环节的复杂度，使得大量文档数据可以方便地被下游的文本分析任务消费。

## 核心功能

- **多格式支持**：能够将 PDF、PowerPoint、Word、Excel、图片（含 EXIF 元数据和 OCR 文字识别）、音频（含 EXIF 元数据和语音转文字）、HTML、CSV、JSON、XML、EPUB、ZIP 压缩包以及 YouTube 视频链接等众多格式转换为 Markdown。
- **结构保持**：在转换过程中尽力保留原始文档的重要结构元素，包括标题层级、列表、表格、链接等，确保输出的 Markdown 文档具有良好的可读性和语义完整性。
- **流式与本地转换**：提供 `convert_stream()` 和 `convert_local()` 等细粒度函数，允许用户根据输入源选择最合适的转换方式，兼顾灵活性与安全性。
- **与 LLM 管道无缝集成**：MarkItDown 默认设计的输出格式专为文本分析工具消费，其轻量化、纯文本的特性完美适配 RAG（检索增强生成）、文本摘要、知识图谱构建等 AI 工作流。
- **最小依赖安装**：默认只安装与 Python 标准库原生兼容的功能，如 HTML、CSV、JSON 等格式的转换，用户可根据需要选择性安装对 PDF、Office 文档等的支持（如 `pip install markitdown[pdf]`）。

## 技术架构

MarkItDown 基于模块化设计，核心转换逻辑以插件式架构实现。每种文件格式对应一个独立的转换器（converter），它们继承自统一的基类接口，从而保证扩展性。项目核心依赖于 Python 标准库中的 `io`、`csv`、`json`、`xml` 等模块处理纯文本格式；对于 PDF 和 Office 文档，则通过可选的第三方库（如 `pypdf`、`python-docx`、`openpyxl` 等）实现底层解析。在音频和图片处理方面，MarkItDown 利用 EXIF 提取和 OCR（如 `pytesseract`）技术，并结合 `whisper` 等语音识别库来完成转换。整体设计遵循最小化依赖原则，同时通过延迟加载和错误处理机制保证了各转换器之间的独立性。此外，为了提高安全性，项目引入了 `convert_stream()` 等细粒度接口，并强烈建议在不可信环境中对输入进行消毒。

## 安装与使用

安装 MarkItDown 非常简单，只需通过 pip 即可完成：

```bash
pip install markitdown
```

如果需要进行 PDF 转换，可以安装 PDF 支持：

```bash
pip install markitdown[pdf]
```

对于 Office 文档（Word、Excel、PowerPoint），安装 Office 支持：

```bash
pip install markitdown[docx,xlsx,pptx]
```

一个最小可用示例：

```python
from markitdown import MarkItDown

# 初始化转换器
md = MarkItDown()

# 从本地文件转换
result = md.convert_local("example.pdf")
print(result.text_content)

# 或从流转换
with open("example.docx", "rb") as f:
    result = md.convert_stream(f, file_extension=".docx")
    print(result.text_content)

# 对于 YouTube 链接
result = md.convert("https://www.youtube.com/watch?v=example")
print(result.text_content)
```

## 适用场景

- **AI 数据预处理**：在构建 RAG 系统或微调 LLM 前，需要将企业知识库中的 PDF、Word、PPT 等文档统一转换为 Markdown，便于分块和嵌入。
- **文档归档与迁移**：将遗留的 Office 文档、HTML 页面、EPUB 电子书等转换为 Markdown 格式，方便在 Git 仓库中版本管理或迁移至新的知识管理平台。
- **多模态内容分析**：从图片（如扫描件）和音频（如会议录音）中提取文字信息，转换为 Markdown 后供后续的文本分类、情感分析等任务使用。
- **内容聚合与索引**：批量处理来自不同来源（如 ZIP 压缩包、YouTube 链接）的文档，生成统一的 Markdown 集合，然后进行全文搜索或知识图谱构建。

## 项目亮点

- **微软背书与生态集成**：由微软开源，与 `autogen` 等微软 AI 框架天然兼容，社区活跃度高（GitHub Star 数突破 12.8 万），持续获得高频更新。
- **轻量级与即用性**：相比 `textract` 等同类工具，MarkItDown 默认安装极轻，无需大量系统依赖即可处理常见格式；同时支持动态加载第三方库，避免了不必要的臃肿。
- **安全优先的设计**：明确的安全注意事项文档，提供细粒度转换接口，帮助开发者规避在不可信环境下的文件遍历和资源泄露风险。
- **结构保留远超纯文本**：与仅提取纯文本的工具不同，MarkItDown 致力于保留标题、列表、表格等文档结构，使得输出更适合 LLM 理解和上下文关联。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 项目页](https://pypi.org/project/markitdown/)
