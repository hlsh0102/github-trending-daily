---
tags:
  - trending
  - article
repo: firecrawl/pdf-inspector
date: 2026-08-06
language: Rust
stars_total: 11669
stars_today: 1582
---
## 项目概述

pdf-inspector 是一个基于 Rust 编写的高性能 PDF 检查、分类与文本提取库。它能够在极短的时间内智能判断 PDF 是文本型还是扫描型，并据此帮助开发者做出路由决策——哪些 PDF 需要送入 OCR 服务，哪些可以直接本地处理。该项目由 Firecrawl 开发并开源，旨在解决大规模 PDF 处理场景中的成本与效率问题：据统计，约 54% 的 PDF 本质上是文本型的，并不需要昂贵的 OCR 服务。通过使用 pdf-inspector，开发者可以跳过这些不必要的开销，仅在必要时才调用 OCR。

该项目面向的典型用户包括：文档处理管线的开发者、数据抓取与内容提取工具的构建者、知识库管理系统的设计者，以及任何需要在本地快速判断和处理 PDF 内容的团队。

## 核心功能

- **智能分类**：通过对 PDF 内容流进行采样，在约 10-50 毫秒内将 PDF 分类为 TextBased、Scanned、ImageBased 或 Mixed 四种类型，并提供 0.0-1.0 的置信度分数和逐页 OCR 路由建议。
- **位置感知文本提取**：提取文本时保留字体信息、X/Y 坐标等元数据，能够自动识别多栏布局的阅读顺序，保证提取结果的逻辑正确。
- **Markdown 转换**：基于字体大小比例识别标题层级（H1-H4），支持项目符号、编号和字母列表的还原，通过等宽字体检测识别代码块，并通过矩形检测与启发式算法识别表格，同时保留粗体、斜体、URL 链接等格式信息。
- **表格检测双模式**：既可通过 PDF 绘图操作的矩形来检测表格边界，也可通过文本对齐的启发式规则来识别表格结构，支持财务表格、脚注和跨页连续表格的处理。
- **CID 字体支持**：内置 ToUnicode CMap 解码能力，能够正确处理 Type0/Identity-H 等复杂字体编码，确保对中日韩等非拉丁文字文本的准确提取。
- **多语言绑定**：提供 Python、Node.js 和浏览器 WebAssembly 绑定，使得非 Rust 生态的开发者也能便捷使用。

## 技术架构

pdf-inspector 的核心设计哲学是"快"与"准"的平衡。在架构上，它直接解析 PDF 的内容流（content streams），而不是依赖完整的 PDF 渲染引擎，这使得分类和提取过程极其轻量。分类阶段通过采样而非全量解析来加速判断，这种策略在保证高准确率的同时将延迟控制在数十毫秒级别。

文本提取模块采用了位置感知的设计，保存每个字符的坐标和字体元数据，这使得后续的阅读顺序推理和版面分析成为可能。Markdown 转换器构建于位置提取之上，通过字号比例推断标题层级，通过字体类型判断代码块，通过坐标对齐关系还原表格结构。

Rust 语言的特性为该项目带来了内存安全和高并发性能。此外，通过 N-API 和 PyO3 提供的 Node.js 与 Python 绑定，以及编译为 WebAssembly 的能力，使得项目的核心逻辑可以在几乎任何运行时环境中复用，而无需重写算法。

## 安装与使用

### Rust

在 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
pdf-inspector = "0.1"
```

最小使用示例：

```rust
use pdf_inspector::{inspect_pdf, PdfType};

fn main() {
    let pdf_data = std::fs::read("document.pdf").unwrap();
    let result = inspect_pdf(&pdf_data).unwrap();
    
    match result.pdf_type {
        PdfType::TextBased => println!("文本型 PDF，可本地提取"),
        PdfType::Scanned => println!("扫描型 PDF，建议路由到 OCR"),
        _ => println!("混合型，需逐页判断"),
    }
}
```

### Python

```bash
pip install pdf-inspector
```

```python
from pdf_inspector import inspect_pdf

result = inspect_pdf("document.pdf")
print(f"类型: {result.pdf_type}, 置信度: {result.confidence}")
```

### Node.js

```bash
npm install @firecrawl/pdf-inspector
```

```javascript
const { inspectPDF } = require('@firecrawl/pdf-inspector');

const result = inspectPDF('document.pdf');
console.log(result.pdfType);
```

## 适用场景

**智能文档路由**：在文档处理管线中，先使用 pdf-inspector 快速分类，将文本型 PDF 直接送入本地提取流程，仅将扫描型 PDF 发送到 OCR 服务，从而大幅降低 API 成本和等待时间。

**大规模爬虫与数据采集**：网络爬虫通常面对大量异构 PDF，pdf-inspector 的毫秒级分类能力使得爬虫可以在不阻塞流程的情况下实时决定每个 PDF 的处理策略。

**知识库与 RAG 系统构建**：构建检索增强生成系统时，需要将 PDF 批量转换为 Markdown 格式以便切分和向量化。pdf-inspector 的 Markdown 转换能力保留了文档的结构信息（标题、表格、列表），有助于生成更高质量的向量表示。

## 项目亮点

pdf-inspector 最显著的差异化优势在于其速度：在本地处理文本型 PDF 的目标延迟在 200 毫秒以下，分类阶段更是仅需 10-50 毫秒。这一性能指标使得它能够在实时或准实时的管道中作为前置过滤器使用，而不至于成为瓶颈。

其次，它完全不需要 OCR 即可完成文本提取和 Markdown 转换，对于文本型 PDF 来说是零外部依赖的解决方案。同时，全功能模块（分类、提取、转换）都支持 Python、Node.js 和浏览器环境，这种多语言覆盖在 Rust 生态的 PDF 库中较为少见。

最后，cid-font 支持和多栏阅读顺序推断能力使其在处理非英文 PDF 和复杂排版文档时表现出色，这相对于许多仅支持简单文本抽取的工具是一个重要补充。

## 相关链接

- [GitHub 仓库](https://github.com/firecrawl/pdf-inspector)
- [crates.io 发布页](https://crates.io/crates/pdf-inspector)
- [npm 包](https://www.npmjs.com/package/@firecrawl/pdf-inspector)
- [PyPI 发布页](https://pypi.org/project/pdf-inspector/)
- [Firecrawl 官网](https://firecrawl.dev)
