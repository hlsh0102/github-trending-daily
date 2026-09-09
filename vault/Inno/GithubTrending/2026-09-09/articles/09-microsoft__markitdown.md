---
tags:
  - trending
  - article
repo: microsoft/markitdown
date: 2026-09-09
language: Python
stars_total: 181942
stars_today: 2047
---
## 项目概述

MarkItDown 是微软开源的一款轻量级 Python 工具，致力于将各种常见格式的文件和办公文档转换为 Markdown 格式。该项目最初的核心目标是服务于大语言模型（LLM）和文本分析管道——在将文档送入 LLM 前，需要一种既保留文档结构又足够简洁的中间格式，而 Markdown 恰好平衡了这两点。

该工具面向的典型用户包括：人工智能工程师需要将本地文档批量转换为 LLM 可消费的文本；数据分析师希望从复杂的办公文档中提取结构化内容；知识库维护者需要将多种格式的源文件统一为 Markdown 存储。无论哪种场景，MarkItDown 都提供了一条简单直接的路径，让用户无需手动复制粘贴或编写复杂的解析脚本。

## 核心功能

- **多格式支持**：覆盖 PDF、PowerPoint、Word、Excel、HTML、EPub 等主流文档格式，以及 CSV、JSON、XML 等纯文本格式、图片（EXIF 元数据与 OCR）、音频（EXIF 元数据与语音转录）和 ZIP 压缩包（自动迭代内部文件）。
- **视频 URL 解析**：支持直接输入 YouTube 链接，提取视频页面的文本描述和元数据，便于将在线视频内容纳入文本分析流程。
- **结构保留**：在转换过程中尽力保留原始文档的标题层级、列表、表格、链接等关键结构，使得输出 Markdown 不仅便于阅读，更适合被解析器进一步处理。
- **灵活的输出方式**：既支持从本地文件路径直接转换（`convert()`），也支持对文件流（`convert_stream()`）和本地路径对象（`convert_local()`）进行操作，方便集成到自定义 I/O 流程中。
- **命令行工具**：项目提供简洁的命令行接口，允许用户快速将单个文件转换为 Markdown 并输出或保存为文件，无需编写额外 Python 代码。
- **Python API**：为开发者提供清晰的 `MarkItDown` 类接口，可轻松嵌入到更大型的数据处理或模型微调管线中。

## 技术架构

MarkItDown 的架构设计遵循“适配器模式”——每种输入格式对应一个独立的转换器，统一向核心引擎返回结构化内容，最终由核心引擎将其渲染为 Markdown 字符串。这种插件化的设计思路使得扩展新格式变得十分容易：只需新增一个适配器即可复用整条转换链路。

项目依赖一些成熟的底层库来实现具体格式解析，例如使用 PDF 解析器处理 PDF 文件，利用 Python 的标准库或第三方库解析 HTML 和 XML，并通过 OCR 与语音识别工具（如针对图片和音频的识别方案）补充非文本内容的提取。底层库的选用侧重于保持项目“轻量”，避免引入过于沉重的框架。此外，MarkItDown 在 I/O 设计上区分了本地文件、流和网络 URL 三种资源访问方式，允许调用者根据自身环境选择合适的入口函数，并据此进行有效的权限管控。

在安全方面，项目文档明确强调：MarkItDown 的 I/O 操作会继承当前进程的权限（类似 `open()` 或 `requests.get()`），因此在不信任环境中必须对输入来源进行消毒，并尽量使用权限范围最窄的转换函数。这一安全考量被作为重要的架构级提醒，尤其对处理不可信文件的场景至关重要。

## 安装与使用

MarkItDown 可通过 pip 轻松安装。需要注意的是，根据你要处理的文件类型，可能需要额外安装对应的依赖包，例如处理图片 OCR 或音频转录时需要安装额外的扩展依赖。

```bash
# 基础安装
pip install markitdown

# 如需图片 OCR 与音频转录功能，可安装完整依赖
pip install "markitdown[all]"
```

安装完成后，既可以使用命令行工具快速转换文件，也可以在 Python 脚本中通过 API 调用。

**命令行示例：**

```bash
# 将 PDF 或 Word 文档转换为 Markdown 并输出到终端
markitdown path/to/document.pdf

# 将输出保存至文件
markitdown path/to/presentation.pptx -o output.md
```

**Python API 用法：**

```python
from markitdown import MarkItDown

# 初始化转换器
mid = MarkItDown()

# 将本地文件转换为 Markdown
result = mid.convert("report.docx")
print(result.text_content)

# 处理网络资源
result = mid.convert("https://example.com/article.html")
```

若需要处理的是已被打开的文件流，可以使用 `convert_stream()` 方法，这对于上层应用已持有的文件对象或网络流非常友好。

## 适用场景

**LLM 数据准备工作流** —— 在构建 RAG 系统或训练语料库时，常需将散落在 PDF、Word、Excel 等格式中的知识统一转换为 Markdown，再进一步切片或向量化。MarkItDown 将文档结构保留为 Markdown 格式，使得切片时能更好地保留上下文边界。

**多格式文档聚合与搜索** —— 企业或个人知识库通常同时包含网页、PPT 和办公文档，MarkItDown 可以作为统一的“文档转换层”，将所有内容归一化后，存入支持 Markdown 的文档数据库或搜索引擎中，使后续检索不受源格式限制。

**音视频内容文本化** —— 对于包含演讲录音或图片信息的资料，该工具能从音频文件中提取转录文本、从图片中读取 EXIF 信息和 OCR 文字，从而填补传统文本解析无法覆盖的空白。

**快速原型开发** —— 由于接口极其简洁（两行代码完成转换），开发者可以在项目早期快速取用 MarkItDown 作为临时抽取工具，而无需为每种格式引入独立的解析方案。

## 项目亮点

与文本抽取领域较为知名的 textract 相比，MarkItDown 的核心差异体现在“以 Markdown 为核心输出格式”这一设计选择上。它不仅提取纯文本，还保留了文档的标题、列表、表格等结构信息，对 LLM 和文本分析工具的输入友好度极高，输出结果在需要时也能直接呈现给人阅读。

另一大亮点是覆盖格式的广度。内置的多格式适配器在安装阶段无需用户预先安装大量的系统级转换工具（如 LibreOffice），维持了良好的开箱即用体验。活跃的社区和微软背书也确保了工具的持续演进，目前项目已获得超过 18 万 Star，更新频繁，用户可以期待持续的新格式支持和稳定性增强。

## 相关链接

- [GitHub 仓库](https://github.com/microsoft/markitdown)
- [PyPI 项目页](https://pypi.org/project/markitdown/)
