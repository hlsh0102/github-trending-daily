---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-06-04
language: Python
stars_total: 143269
stars_today: 1984
---
## 项目概述

MarkItDown 是由微软开源的一款轻量级 Python 工具，旨在将各种常见文件格式转换为 Markdown。它的核心目标是为大语言模型（LLM）和文本分析管线提供干净、结构化的输入数据。与传统的文档转换工具不同，MarkItDown 特别注重保留原文档的标题、列表、表格、链接等结构信息，而非追求高保真的可视化呈现。因此，它非常适合需要从不同来源提取文本并统一格式的场景，其目标用户包括 AI 工程师、数据科学家、文档处理开发者以及任何需要批量转换文件为 Markdown 的团队。

## 核心功能

- **多格式支持**：目前支持 PDF、PowerPoint、Word、Excel、图片（EXIF 元数据和 OCR）、音频（EXIF 元数据和语音转录）、HTML、CSV/JSON/XML 等文本格式、ZIP 压缩包、YouTube 链接以及 EPub 电子书。
- **Markdown 结构化输出**：自动将文档中的标题、列表、表格、链接等元素转换为对应的 Markdown 语法，保留原始层级和语义。
- **可扩展的转换架构**：提供统一的 `convert_*` 接口（如 `convert_stream()`、`convert_local()`），方便开发者针对不同来源（本地文件、HTTP 流、内存对象）进行转换。
- **轻量级与低依赖**：核心功能仅依赖 Python 标准库和少量第三方库（如 `python-magic`、`Pillow`），方便快速集成。
- **安全考虑**：明确提示安全注意事项，建议在不可信环境中使用最窄的转换函数（如 `convert_stream()`）以避免不必要的文件系统访问。
- **流式与批量处理**：支持从流对象转换，也支持对 ZIP 压缩包内文件自动迭代处理。

## 技术架构

MarkItDown 采用插件化的设计思路。核心模块 `markitdown` 提供 `MarkItDown` 类，它根据输入文件的 MIME 类型或扩展名自动路由到对应的转换器（Converter）。每个转换器负责特定格式的解析和 Markdown 输出。这种设计使得新增格式支持只需添加新的转换器类，而无需修改核心代码。

在实现上，MarkItDown 倾向于使用轻量级的解析方式：例如，对于 PDF，它使用 `PyMuPDF` 或 `pdftotext` 提取文本并重建标题层级；对于 Office 文档，则通过 `python-pptx`、`python-docx`、`openpyxl` 等库获取结构化内容。图片和音频的元数据提取依赖 `Pillow` 和 `mutagen`，而 OCR 和语音转文字则通过可选的插件实现（如 `pytesseract`、`whisper`）。该工具不追求完整还原所有格式细节，而是专注于提取“LLM 友好”的结构化内容。

## 安装与使用

### 安装

通过 pip 即可安装核心版本：

```bash
pip install markitdown
```

若需要 OCR 或语音转录支持，可安装额外依赖：

```bash
pip install markitdown[ocr] markitdown[audio]
```

### 最小可用示例

```python
from markitdown import MarkItDown

# 初始化转换器
md = MarkItDown()

# 从本地文件转换
result = md.convert_local("presentation.pptx")
print(result.text_content)

# 从 URL 转换（如 YouTube 视频）
result = md.convert_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(result.text_content)

# 从内存流转换
import requests
response = requests.get("https://example.com/report.pdf")
result = md.convert_stream(response.content)
print(result.text_content)
```

转换结果以 `MarkItDownResult` 对象返回，包含 `text_content`（Markdown 字符串）和 `metadata`（如标题、作者、语言）等信息。

## 适用场景

- **LLM 数据准备**：将企业文档库（如 Word、PDF 报告）批量转换为 Markdown，用于微调或 RAG 管线的语料注入。
- **多语言内容分析**：处理包含多种格式（如 YouTube 转录、Excel 数据、图片说明）的混合内容，统一为 Markdown 后进行分析。
- **自动化文档流水线**：在 CI/CD 或数据处理管道中，自动将上传的文件（如 PowerPoint 演示、PDF 合同）转换为 Markdown，供下游系统索引或摘要。
- **知识库构建**：将 EPub 电子书、HTML 网页、CSV 表格等多种来源的文档转换为标准 Markdown，存入向量数据库以支持语义搜索。

## 项目亮点

- **与 LLM 的天然亲和性**：Markdown 因其结构简单、贴近纯文本，已成为 LLM 输入的标准格式。MarkItDown 专门为此场景设计输出，减少了格式转换中的信息丢失。
- **微软官方维护与社区活跃**：作为微软开源项目，具有较高的代码质量和社区支持。目前 GitHub 星数超过 14 万，且每日增长迅速，反映了广泛的认可度。
- **安全设计意识**：明确的安全指南和分级的转换函数（`convert_local` vs `convert_stream`）帮助开发者避免潜在的文件路径注入风险，这在处理不可信输入时尤为重要。
- **扩展性良好**：插件式架构允许社区轻松添加新格式支持，例如已支持的 ZIP 文件自动展开功能就体现了这种灵活性。
- **对比传统工具**：与 `textract`、`pandoc` 等工具相比，MarkItDown 更聚焦于 LLM 场景，输出更适合直接输入到语言模型中进行后续处理，而非追求完美的可视化还原。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 包](https://pypi.org/project/markitdown/)
