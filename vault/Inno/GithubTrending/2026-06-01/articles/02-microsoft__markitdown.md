---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-06-01
language: Python
stars_total: 135907
stars_today: 2798
---
## 项目概述

MarkItDown 是微软开源的一款轻量级 Python 工具，专门用于将多种文件格式和办公文档转换为 Markdown 格式。该项目解决的核心问题是：在大语言模型（LLM）和文本分析管线的应用中，各种异构文档（PDF、Office 文档、图片、音频等）难以被直接处理。MarkItDown 提供了一种统一的方式，将这些文档转换为结构清晰的 Markdown 文本，从而方便 LLM 进行读取、理解和分析。

目标用户主要是开发者、数据科学家、AI 研究人员以及任何需要将大量非结构化文档转化为 LLM 可消费文本格式的从业者。它特别适合用于构建 RAG（检索增强生成）系统、文档分析工具、知识库构建以及自动化数据处理流水线。

## 核心功能

- **多格式支持**：支持 PDF、PowerPoint、Word、Excel、图片（EXIF 元数据和 OCR）、音频（EXIF 元数据和语音转录）、HTML、CSV、JSON、XML、ZIP 文件、YouTube 视频链接以及 ePub 电子书等多种常见的文件与数据格式。
- **结构保留**：在转换过程中尽可能保留原文档的重要结构信息，如标题、列表、表格、链接、图片描述等，确保生成的 Markdown 在语义上与原文档一致。
- **轻量易用**：作为 Python 库设计，安装简单（`pip install markitdown`），API 直观，能够快速集成到现有项目中，无需复杂的配置。
- **安全考虑**：项目明确提示了安全性注意事项，建议在不可信环境中对输入进行清洗，并使用最窄权限的转换函数（如 `convert_stream()`、`convert_local()`），避免潜在的安全风险。
- **可扩展性**：开源且采用 MIT 许可证，开发者可根据需要扩展支持更多文件格式或自定义转换逻辑。

## 技术架构

MarkItDown 基于 Python 构建，核心设计思路是提供一个统一、轻量的转换层。其技术架构具有以下特点：

- **模块化设计**：每种文件格式对应一个独立的转换模块，便于维护和扩展。例如，PDF 处理可能依赖 PyMuPDF 或 pdfminer，而图片 OCR 可能集成 Tesseract 或类似引擎。
- **专注 LLM 消费**：与追求视觉保真度的传统文档转换工具不同，MarkItDown 更注重生成语义丰富、结构清晰的文本，以适应 LLM 的分词和理解能力。Markdown 作为输出格式，兼具文本的可读性和结构表达能力。
- **安全层次**：项目通过提供不同粒度的 API（如 `convert_stream()` 处理流式输入、`convert_local()` 处理本地文件），允许用户根据信任级别选择最安全的调用方式，防止意外访问系统资源。
- **跨平台兼容**：纯 Python 实现，可运行于 Windows、macOS 和 Linux，无平台依赖性。

## 安装与使用

**安装步骤**：

MarkItDown 通过 PyPI 发布，使用 pip 即可安装：

```bash
pip install markitdown
```

**最小可用示例**：

以下是一个简单的 Python 脚本，演示如何将本地 PDF 文件转换为 Markdown：

```python
from markitdown import MarkItDown

md = MarkItDown()

# 转换本地文件
result = md.convert("example.pdf")

# 输出 Markdown 文本
print(result.text_content)
```

如果需要处理来自不可信网络的数据流，可以使用更安全的方式：

```python
from markitdown import MarkItDown
import requests

md = MarkItDown()

response = requests.get("https://example.com/document.pdf")
result = md.convert_stream(response.content)
print(result.text_content)
```

对于最受信任的本地文件，可以直接使用 `convert_local()`：

```python
result = md.convert_local("/path/to/secure/document.docx")
```

## 适用场景

- **LLM 数据预处理**：在大规模训练或微调 LLM 之前，需要将 PDF、网页、办公文档等异构数据统一转换为 Markdown 格式，作为文本输入源。
- **RAG 系统文档导入**：在构建 RAG 知识库时，利用 MarkItDown 解析各种文档（如报告、手册、论文），将其内容存储为向量索引，以便后续检索增强生成。
- **文档自动化分析**：构建自动化工具，批量处理公司内部或网络上的文档，提取关键信息并生成摘要、问答或分类标签。
- **内容迁移与备份**：将重要文档（如 Word 文件、Excel 表格、网页内容）转为轻量的 Markdown 格式，便于版本控制、迁移或长期存档。

## 项目亮点

与同类工具（如 textract、unstructured、pandoc）相比，MarkItDown 具有以下差异化优势：

- **专注 LLM 生态**：输出直接针对 LLM 消费优化，而非追求人类阅读的视觉完美，生成的 Markdown 结构紧凑、语义明确，减少 token 浪费。
- **微软背书与活跃维护**：由微软官方维护，社区活跃，已获得超过 135k 星标，更新频繁，保证了项目的长期可用性和质量。
- **极简 API 与可扩展性**：API 设计极其简洁（4 个核心方法：`convert`、`convert_local`、`convert_stream`、`convert` 的变体），同时易于扩展支持新格式，适合快速集成。
- **内置安全机制**：通过 API 设计层面强调安全性，避免在不安全环境中滥用 `convert()` 导致的资源访问风险，同类工具中较少有此设计。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 包页面](https://pypi.org/project/markitdown/)
- [Microsoft AutoGen 项目](https://github.com/microsoft/autogen)
