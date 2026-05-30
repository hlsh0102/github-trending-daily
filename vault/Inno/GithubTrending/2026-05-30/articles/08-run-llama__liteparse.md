---
tags:
  - trending
  - article
repo: run-llama/liteparse
date: 2026-05-30
language: Rust
stars_total: 7458
stars_today: 701
---
## 项目概述

LiteParse 是一个由 LlamaIndex 团队开发的开源 PDF 解析工具，专注于提供**快速且轻量**的文档解析能力。它能够从 PDF 文件中提取高质量的空间文本信息，并返回包含边界框（bounding boxes）的结构化数据。与依赖云端大语言模型（LLM）或专有服务的解析器不同，LiteParse 完全在本地运行，没有外部依赖，适合对速度和隐私有高要求的场景。目标用户包括需要快速提取 PDF 文本内容的开发者、数据工程师，以及希望避免将敏感文档上传到云服务的团队。项目采用 Rust 语言编写，同时提供了 Python 和 JavaScript 的包，便于跨语言集成。

## 核心功能

- **快速文本解析**：针对 PDF 文档进行优化，能够高效提取纯文本内容，速度远超传统基于 LLM 的解析方案。
- **空间布局保留**：解析结果包含每个文本元素的边界框坐标（比如位置、宽度、高度），便于后续结构化分析和布局还原。
- **轻量无依赖**：无需安装任何 LLM 模型或连接云服务，所有计算都在本地设备上完成，减少了部署和运维成本。
- **多语言支持**：通过 Python 包（`liteparse`）、JavaScript 包（`@llamaindex/liteparse`、`@llamaindex/liteparse-wasm`）以及 Rust 原生的 `liteparse` crate 提供统一接口，支持多种开发环境。
- **开源免费**：采用 Apache-2.0 许可证，代码完全开放，用户可以自由使用、修改和分发。

## 技术架构

LiteParse 基于 Rust 语言开发，充分利用了 Rust 在系统编程中的高性能和内存安全特性。核心设计思路是“专一且高效”：不试图处理所有文档类型，而是聚焦于 PDF 文件的文本解析，这使其代码量和运行时开销都保持在极低水平。解析引擎直接操作 PDF 的底层内容流（如文本对象、字体映射和坐标系统），避免了通过第三方库（如 PyMuPDF、PDFBox）带来的额外开销。为了支持多语言生态，项目提供了 Python 绑定和 JavaScript/WASM 绑定，其中 WASM 版本可以在浏览器中直接运行，进一步扩展了使用场景。整个架构强调模块化和零外部依赖，核心库本身不引用任何 LLM 推理框架或网络请求库。

## 安装与使用

**安装（以 Python 为例）**：
```bash
pip install liteparse
```

**最小可用示例**：
```python
from liteparse import LiteParse

lp = LiteParse()
# 从文件流或路径解析
result = lp.parse("/path/to/document.pdf")
# 遍历提取的文本元素
for element in result.elements:
    print(element.text, element.bbox)  # bbox 是 (x, y, w, h) 格式
```

**安装（JavaScript / Node.js）**：
```bash
npm install @llamaindex/liteparse
```
**使用**：
```javascript
const { LiteParse } = require('@llamaindex/liteparse');
const lp = new LiteParse();
const result = await lp.parse('document.pdf');
console.log(result.elements);
```

**WASM 版本**可在浏览器中直接使用，无需安装原生依赖，通过 `@llamaindex/liteparse-wasm` 包引入。

## 适用场景

- **文档预处理流水线**：在大规模文本处理管道中（如 RAG 系统、搜索引擎索引），需要快速从 PDF 中提取文本并过滤掉无关元数据。
- **敏感文档处理**：企业内网、医疗或金融场景中，文档包含隐私数据无法上传至云端，LiteParse 的本地运行特性保证了数据安全。
- **轻量级嵌入式系统**：在资源受限的环境（如边缘设备）中，无法运行完整的 LLM 服务，LiteParse 的低开销使其成为理想选择。
- **文档布局分析的前置工具**：先通过 LiteParse 获取文本位置信息，再结合规则或轻量模型进行表格识别、标题提取或版面重构。

## 项目亮点

LiteParse 的主要差异化优势在于**极致的速度与简洁性**。与 LlamaParse 等云服务相比，它不需要网络请求、API 密钥或 GPU 资源，可以在毫秒级完成单页解析。与 PyPDF2、pdfplumber 等传统 Python 库相比，Rust 原生的实现使其在处理大文件时性能提升明显，且内存占用更稳定。另外，LiteParse 的输出直接包含边界框信息，这为后续的视觉布局重建（如将文本还原到原始位置）提供了便利，而许多轻量解析器往往忽略这一高级特征。它也是 LlamaIndex 生态中第一个完全开源的本地文档解析器，提供了从本地到云端的平滑过渡方案——用户在简单场景下使用 LiteParse，遇到复杂文档时可以无缝切换到 LlamaParse。

## 相关链接

- [GitHub 仓库](https://github.com/run-llama/liteparse)
- [官方文档](https://developers.llamaindex.ai/liteparse/)
- [LlamaParse 云服务](https://developers.llamaindex.ai/python/cloud/llamaparse/)
