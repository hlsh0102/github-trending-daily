---
tags:
  - trending
  - article
repo: firecrawl/pdf-inspector
date: 2026-08-05
language: Rust
stars_total: 10327
stars_today: 2540
---
## 项目概述

pdf-inspector 是一个用 Rust 编写的高性能 PDF 检查、分类与文本提取库，由 Firecrawl 团队开发并开源。其核心目标是在**无需 OCR** 的前提下，快速判断一个 PDF 是文本型还是扫描型，并针对文本型 PDF 进行高质量的内容提取。

该项目解决了一个实际痛点：在文档处理流水线中，约有 54% 的 PDF 本质上是文本型的，并不需要昂贵的 OCR 服务。pdf-inspector 能够在 200 毫秒内完成本地处理，从而大幅节省成本和延迟。它提供 Rust 原生库，并附带 Python、Node.js 和浏览器 WebAssembly 绑定，适合需要智能路由 PDF 处理流程的开发者或团队。

## 核心功能

- **智能分类**：在 10–50 毫秒内通过采样内容流，将 PDF 判定为 TextBased（文本型）、Scanned（扫描型）、ImageBased（图像型）或 Mixed（混合型），并返回 0.0–1.0 的置信度分数，支持按页粒度进行 OCR 路由决策。
- **位置感知文本提取**：在提取文本的同时保留字体信息、X/Y 坐标，并自动处理多栏阅读顺序，确保还原真实版面结构。
- **Markdown 转换**：基于字体大小比例识别标题层级（H1–H4），支持项目符号、编号、字母列表，识别等宽字体生成代码块，支持矩形绘制操作与文本对齐两种方式的表格检测，以及粗体、斜体、URL 链接和分页符处理。
- **CID 字体支持**：通过 ToUnicode CMap 解码 Type0/Identity-H 字体，解决中文、日文等东亚语言 PDF 中常见的字体编码难题。
- **表格检测双模式**：同时支持基于 PDF 绘图操作的矩形检测，以及基于文本对齐方式的启发式检测，可处理财务报表、脚注及跨页续表。
- **跨语言绑定**：除 Rust 原生 API 外，提供 Python、Node.js（N-API）和浏览器 WebAssembly 版本，方便在不同技术栈中集成。

## 技术架构

pdf-inspector 采用纯 Rust 实现，核心设计思路是**内容流采样优先**。它并不预先解析整个 PDF，而是通过快速采样页面内容流来做出分类判断，这在很大程度上保证了性能——尤其对于大文件而言，可以避免不必要的全量解析。

在文本提取层面，库对 PDF 的内部对象结构进行了深度处理：支持对 Type0 字体的 CMap 解析，能够处理复杂的编码映射；在版面分析上，结合字体尺寸、文本坐标和绘图操作符等多维信息，重建文档的语义结构。这种设计使其在提取准确性和速度之间取得了良好平衡。

项目采用模块化架构，将分类、提取、Markdown 转换和表格检测分离为独立组件，便于扩展和维护。通过 C ABI 和 N-API 层实现跨语言绑定，底层核心逻辑保持一致。

## 安装与使用

**Rust（Cargo）**：

```bash
cargo add pdf-inspector
```

**Python（pip）**：

```bash
pip install pdf-inspector
```

**Node.js（npm）**：

```bash
npm install @firecrawl/pdf-inspector
```

**最小可用示例（Python）**：

```python
from pdf_inspector import classify_pdf, extract_text

# 分类 PDF
result = classify_pdf("document.pdf")
print(result.kind)          # TextBased / Scanned / ImageBased / Mixed
print(result.confidence)    # 0.0 - 1.0

# 提取文本 (仅文本型 PDF)
if result.kind == "TextBased":
    pages = extract_text("document.pdf")
    print(pages[0].markdown)  # 第一页的 Markdown 内容
```

**最小可用示例（Rust）**：

```rust
use pdf_inspector::{classify_pdf, extract_text};

let classification = classify_pdf("document.pdf").await?;
println!("{:?} (confidence: {})", classification.kind, classification.confidence);

let pages = extract_text("document.pdf").await?;
println!("{}", pages[0].markdown);
```

## 适用场景

- **PDF 处理流水线智能路由**：在文档管理系统中，先使用 pdf-inspector 判断 PDF 类型，将文本型文档直接本地提取，仅将扫描型文档发送到 OCR 服务，从而节省 API 成本和提升吞吐量。
- **RAG 与知识库构建**：为检索增强生成（RAG）系统提供高质量的 PDF 文本预处理，将 PDF 转换为结构化的 Markdown，便于后续切片和向量化。
- **金融与法律文档解析**：处理包含大量表格、复杂排版的财报、合同等文档，利用多模式表格检测和位置感知提取，确保数据还原准确。
- **多语言 PDF 批处理**：对包含日文、中文等使用 CID 字体的 PDF 进行批量转换，无需依赖外部转换服务即可完成文本抽取。

## 项目亮点

- **性能极佳**：分类仅需几十毫秒，整体文本提取在 200ms 内完成，远超基于 Python 的传统方案，适合对延迟敏感的生产环境。
- **免 OCR 的智能判断**：能准确区分扫描件和文本型 PDF，避免对文本型文档白白消耗 OCR 配额，这是许多通用 PDF 库不具备的能力。
- **高质量 Markdown 输出**：不只是提取纯文本，而是还原标题、列表、表格、代码块等结构，输出可直接用于文档渲染或 LLM 输入。
- **开源且跨语言**：以 MIT 协议开源，提供 Python、Node.js、WASM 多语言绑定，团队可以在不同技术栈中统一使用同一套核心逻辑。
- **扎实的字体处理**：对 CID/Type0 字体有专门的解码支持，在东亚语言 PDF 的处理上具有明显优势。

## 相关链接

- [GitHub 仓库](https://github.com/firecrawl/pdf-inspector)
- [crates.io 发布页](https://crates.io/crates/pdf-inspector)
- [npm 发布页](https://www.npmjs.com/package/@firecrawl/pdf-inspector)
- [PyPI 发布页](https://pypi.org/project/pdf-inspector/)
- [Firecrawl 官网](https://firecrawl.dev)
