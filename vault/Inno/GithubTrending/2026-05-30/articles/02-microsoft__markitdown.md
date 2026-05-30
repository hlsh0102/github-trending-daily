---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-05-30
language: Python
stars_total: 130366
stars_today: 1873
---
## 项目概述

MarkItDown 是由微软开发的一款轻量级 Python 工具，专注于将多种常见文件格式和办公文档转换为 Markdown 格式。该项目旨在解决文本分析工具（尤其是大语言模型）在处理不同格式文档时的输入一致性问题。传统上，开发者需要为 PDF、Word、Excel 等不同格式编写各自的解析逻辑，而 MarkItDown 提供了一个统一的转换接口，让用户能够轻松地将各种文档转化为结构清晰、机器易读的 Markdown 文本。该项目的目标用户包括 AI/ML 工程师、数据分析师、文档处理开发者以及任何需要将文档内容输入文本分析管线的技术人员。

## 核心功能

- **多格式支持**：支持 PDF、PowerPoint、Word、Excel、HTML、EPUB、CSV/JSON/XML 等文本格式、图片（EXIF 元数据与 OCR）、音频（EXIF 元数据与语音转录）、YouTube 网址以及 ZIP 压缩包内容等多达十几种文件格式的转换。
- **结构保留**：转换过程中尽可能保留原文档的重要结构信息，包括标题层级、列表、表格、链接等 Markdown 元素，使输出结果在机器分析时具有更高的语义价值。
- **轻量易用**：提供简洁的 Python API，只需几行代码即可完成文件转换，同时也支持命令行调用，适合快速集成到现有工作流中。
- **流式与本地转换**：支持 `convert_stream()` 和 `convert_local()` 等细粒度转换方法，允许开发者根据安全需求选择最低权限的接口。
- **扩展灵活性**：项目采用插件式架构设计，可以方便地扩展支持新的文件格式，社区贡献者也能够轻松添加自定义转换器。

## 技术架构

MarkItDown 基于 Python 开发，采用了模块化的文件格式处理器架构。核心设计包括：

- **基类抽象**：核心定义了一个 `DocumentConverter` 基类和一系列 `FormatHandler` 接口，每种文件格式对应一个独立的处理器实现。
- **依赖管理**：针对不同格式使用不同的底层库，例如 PDF 使用 `PyMuPDF`（或 `pdfminer`），Office 文档使用 `python-pptx`、`python-docx`、`openpyxl`，图片 OCR 使用 `pytesseract`，音频转录依赖 Whisper 等。这实现了按需加载，避免不必要的依赖膨胀。
- **安全设计**：项目明确强调安全边界，建议用户在不可信环境下使用窄范围转换函数（如 `convert_stream()`），并对外部输入进行消毒处理，防止特权提升风险。
- **输出标准化**：所有格式最终统一输出为 Markdown 字符串，保留标题（#）、列表（- / 1.）、表格（|-|）、链接（[]()）等关键结构，同时尽可能压缩无关冗余格式（如字体、颜色）以保持输出精简。

## 安装与使用

### 安装

推荐使用 pip 进行安装：

```bash
pip install markitdown
```

如果需要特定格式的支持（例如 OCR 或音频转录），可以安装对应扩展：

```bash
pip install markitdown[pdf,image,audio]
```

### 最小可用示例

以下是一个简单的 Python 使用示例：

```python
from markitdown import convert_file

# 转换 PDF 文件为 Markdown
md_text = convert_file("report.pdf")
print(md_text)

# 转换 Word 文档
md_text = convert_file("document.docx")

# 转换网页内容
md_text = convert_file("https://example.com/article.html")
```

也支持命令行直接使用：

```bash
markitdown report.pdf > report.md
markitdown https://example.com -o output.md
```

## 适用场景

- **LLM 数据预处理**：将不同格式的训练数据、知识库文档统一转换为纯文本 Markdown，供大语言模型微调或检索增强生成（RAG）管线使用。
- **文档合规分析**：处理大量合同、报告等办公文档，提取表格和标题结构，进行关键词检索或信息抽取。
- **自动化工作流**：在 CI/CD 或数据处理流水线中集成 MarkItDown，自动将上传的多种格式文件转换为标准 Markdown 供下游分析。
- **内容迁移与存档**：将老旧格式的文档批量转换为可长期保存的 Markdown 文本，便于版本管理和全文搜索。

## 项目亮点

- **统一接口**：与 textract 等同类工具相比，MarkItDown 更专注于结构保留和 Markdown 输出，而非简单的文本提取。其输出中标题、表格、链接等语义元素得以保留，更适合 LLM 下游任务。
- **微软官方维护**：作为微软开源项目，拥有高质量代码规范、完善的文档和活跃的社区支持，且与 Azure OpenAI 等微软生态深度兼容。
- **极低的集成成本**：API 设计极为简洁，单函数调用即可完成转换，无需手动配置每种格式的解析器。
- **安全优先**：明确的安全考虑文档和细粒度函数设计，让用户能够在敏感环境中安全使用，避免文件 I/O 权限滥用问题。
- **活跃的社区贡献**：GitHub 上拥有超过 13 万星，社区持续贡献新格式支持（如 EPUB、YouTube URLs 等），扩展生态丰富。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 包页面](https://pypi.org/project/markitdown/)
- [安全考虑文档](https://github.com/microsoft/markitdown#security-considerations)
