---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-05-31
language: Python
stars_total: 132973
stars_today: 2470
---
## 项目概述

MarkItDown 是一个由微软开源的轻量级 Python 工具，专门用于将各类文件和办公文档转换为 Markdown 格式。该项目主要面向大语言模型（LLM）及相关文本分析管线的预处理需求，其核心目标是为机器阅读而非人工浏览提供高质量的 Markdown 输出。

在日常工作流中，开发者需要从 PDF、Word、Excel、PowerPoint、图片甚至音频中提取文本信息，但不同格式之间的转换往往面临结构丢失、格式混乱等问题。MarkItDown 专为此而生：它专注于保留文档中的关键结构（如标题、列表、表格、链接等），以 Markdown 形式输出，使得下游的 LLM 或文本分析工具能够准确理解文档内容。该项目目前已在 GitHub 上获得超过 13 万颗星，社区热度极高。

## 核心功能

- **多格式支持**：支持 PDF、PowerPoint、Word、Excel、图片（EXIF 元数据和 OCR）、音频（EXIF 元数据和语音转录）、HTML、CSV、JSON、XML、EPUB、ZIP（遍历内部文件），以及 YouTube 视频链接等多种输入源。
- **结构化 Markdown 输出**：输出结果保留原始文档的标题层级、列表、表格、超链接、图片引用等关键结构，而非纯文本提取。
- **OCR 与语音转录**：对于图片和音频文件，自动调用 OCR 和语音识别功能（如依赖系统或第三方引擎）提取其中包含的文本信息。
- **安全设计**：明确提示使用者注意 I/O 安全，建议在不可信环境中对输入进行消毒，并根据需要调用最细粒度的转换函数（如 `convert_stream()`、`convert_local()`），减少攻击面。
- **轻量可扩展**：项目结构清晰，基于 Python 实现，易于集成到现有管线中，也方便社区贡献新的格式支持插件。
- **与 LLM 生态对齐**：输出格式专为 LLM 输入优化，输出的 Markdown 可直接作为提示词（prompt）的上下文内容，降低预处理成本。

## 技术架构

MarkItDown 采用模块化架构设计，每种文件格式对应一个独立的转换器（converter）。核心调度器根据输入文件类型自动加载对应的转换器实例，调用其负责的转换逻辑。

技术关键点包括：
- **解析引擎**：对不同文档类型采用业界成熟的解析库，如 PDF 使用 PyMuPDF（fitz）、文档格式使用 python-docx / openpyxl、图片 OCR 使用 pytesseract 或与系统集成的 Tesseract 引擎等。
- **流式处理**：支持从流（stream）和本地文件路径两种方式读取输入，适应 Web 服务或本地脚本的不同场景。
- **安全隔离**：设计上限制每个转换函数只执行必要的 I/O 操作，避免不必要的高权限调用，降低 RCE 或 SSRF 风险。
- **结构保留逻辑**：在生成 Markdown 时，通过遍历文档元素树（如段落、列表项、表格行）逐级写出对应的 Markdown 语法，而非简单的文本拼接。

整体上，MarkItDown 追求的是“足够好的结构保留”与“高效的文本提取”之间的平衡，其输出并非为人类阅读优化（因此排版可能不完美），但对于 LLM 而言，Markdown 的轻量标记结构远比纯文本更有信息量。

## 安装与使用

安装要求 Python 3.9 以上版本，通过 pip 直接安装：

```bash
pip install markitdown
```

最小可用示例如下，将本地 PDF 文件转换为 Markdown：

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

如果需要从 URL 获取内容（如 YouTube 视频），则使用 `convert_url`：

```python
result = md.convert_url("https://www.youtube.com/watch?v=example")
print(result.text_content)
```

进阶使用时可指定输出文件路径，或针对特定格式调整 OCR / 语音转录的选项。

## 适用场景

1. **LLM 提示构建**：将企业内部的各种文档（报告、邮件、表格）统一转为 Markdown，作为 LLM 的上下文提示词，用于问答、分析或摘要生成。
2. **数据预处理管线**：在文本挖掘、NLP 分析项目中，将非结构化文档批量清洗为结构化 Markdown，便于后续分词、向量化或索引。
3. **信息归档与检索**：将大量 Office 文档、PDF 教材、网页内容转换为统一的 Markdown 格式，存入向量数据库或全文检索引擎，实现快速搜索和回溯。
4. **自动化内容搬运**：从含 YouTube 视频的页面提取音频转录并与文本结合，生成包含标题、时间戳和文字内容的 Markdown 笔记。

## 项目亮点

- **聚焦 LLM 场景**：与通用文档转换工具（如 pandoc、textract）不同，MarkItDown 刻意牺牲一部分人读的排版完美度，换取对机器阅读（特别是 LLM）更友好的标记化输出，这在 AI 工程中极为实用。
- **极简 API**：仅需一行代码即可完成转换，无需了解底层解析细节，显著降低集成门槛。
- **活跃的微软生态**：作为微软官方开源项目，社区贡献积极，更新迭代快，且与 Microsoft Autogen 等项目存在协同。
- **安全第一的惯例**：文档中明确警示 I/O 风险，并提供细粒度函数指导，这在处理用户上传的文件时尤其重要，体现了工程设计的严谨性。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 包页面](https://pypi.org/project/markitdown/)
- [官方文档（含安全考量）](https://github.com/microsoft/markitdown#security-considerations)
