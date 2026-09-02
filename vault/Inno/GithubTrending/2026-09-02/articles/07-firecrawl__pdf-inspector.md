---
tags:
  - trending
  - article
repo: firecrawl/pdf-inspector
date: 2026-09-02
language: Rust
stars_total: 18116
stars_today: 541
---
## 项目概述

pdf-inspector 是一个由 Firecrawl 团队开发的高性能 Rust 库，专注于 PDF 的智能分类与文本提取。它能够在无需 OCR 的情况下，快速判断 PDF 是文本型还是扫描型，并提取带有位置信息的文本内容，最终转换为结构清晰的 Markdown 格式。该项目旨在解决 PDF 处理中常见的「盲目 OCR」痛点——即对所有 PDF 统一调用昂贵的 OCR 服务，而实际上约 54% 的 PDF 根本不需要 OCR。通过 pdf-inspector，用户可以在本地以极低的延迟完成 PDF 分类和提取，从而显著降低成本并提升处理效率。该库面向 Rust 开发者、Python/Node.js 使用者以及需要浏览器端处理能力的 Web 开发者，同时提供了多种语言绑定和 WebAssembly 支持。

## 核心功能

- **智能分类**：在 10-50ms 内通过采样内容流，将 PDF 判定为文本型（TextBased）、扫描型（Scanned）、图片型（ImageBased）或混合型（Mixed），返回 0.0-1.0 的置信度分数，并给出逐页的 OCR 路由建议。
- **位置感知文本提取**：提取包含字体信息、X/Y 坐标的文本内容，并自动处理多栏阅读顺序，确保输出逻辑正确。
- **Markdown 转换**：自动生成带标题层级（H1-H4，依据字号比例）、有序/无序列表、代码块（通过等宽字体识别）、表格、加粗/斜体格式及 URL 链接的 Markdown，并保留分页标记。
- **双模式表格检测**：结合基于绘图操作的矩形检测与基于文本对齐的启发式检测，能够正确处理财务报表、脚注以及跨页延续表格。
- **选择性 OCR 支持**：原生 Rust 和 CLI 使用者可以按需对判定为扫描或混合型的页面启用 OCR，而非全量处理。

## 技术架构

pdf-inspector 采用 Rust 编写，核心设计围绕「先分类，后提取」的管线思路。其分类器并非使用复杂的机器学习模型，而是通过解析 PDF 内容流中的操作符和对象特征进行模式判断，这种轻量级方案保证了毫秒级的响应速度。文本提取模块深度依赖 PDF 的字体编码信息和内容流解析，实现对字符位置与样式属性的还原。在 Markdown 转换环节，引擎利用字号比例推断标题层级，通过绘图指令识别表格框架，并使用矩形边界结合文本对齐的双重策略来捕捉复杂表格结构——例如跨页的延续表格和包含脚注的表格块。架构上，pdf-inspector 提供了清晰的原生 Rust API，并在此之上封装了 N-API（Node.js）、PyO3（Python）以及 Wasm 三种绑定层，使得同一套核心逻辑在不同语言环境下都能保持一致的行为和性能。此外，库内设计了「无 OCR 默认路径」和「按需 OCR」两条执行链路，允许调用方根据分类结果灵活选择将哪些页面送入 OCR，做到成本与质量的动态平衡。

## 安装与使用

以下以 Rust 和 Python 为例，演示基本的安装与最小调用方式。

**Rust（Cargo 依赖）**

在 `Cargo.toml` 中添加：
```toml
[dependencies]
pdf-inspector = "0.1"
```

最小示例：
```rust
use pdf_inspector::classify_and_extract;

fn main() {
    let pdf_bytes = std::fs::read("document.pdf").unwrap();
    let result = classify_and_extract(&pdf_bytes).unwrap();
    
    println!("分类结果: {:?}", result.classification);
    println!("置信度: {:.2}", result.confidence);
    println!("提取的 Markdown:\n{}", result.markdown);
}
```

**Python（pip 安装）**

```bash
pip install pdf-inspector
```

```python
import pdf_inspector

with open("document.pdf", "rb") as f:
    pdf_bytes = f.read()

result = pdf_inspector.process(pdf_bytes)
print(f"类型: {result.type}，置信度: {result.confidence}，页数: {len(result.pages)}")
for page in result.pages:
    print(page.markdown)
```

CLI 工具同样可用，例如 `pdf-inspector classify sample.pdf` 输出分类结果，`pdf-inspector extract sample.pdf -o output.md` 执行提取转换。

## 适用场景

- **大规模文档处理管道**：在日处理百万级 PDF 的系统中，先以极低成本识别出无需 OCR 的文本型 PDF，仅将少数染色后的页面送入 OCR 服务，直接节省第三方 API 成本。
- **端到端内容提取服务**：例如将 PDF 文档转换为结构化知识库或数据集的流程，可依靠其位置感知能力和表格识别特性生成干净数据。
- **浏览器内即时预览**：通过 WebAssembly 编译版本，前端应用可实时将用户上传的 PDF 转为可编辑的 Markdown，无需上传至服务器，保护隐私和降低带宽。
- **多格式档案分类**：在网盘或企业中批量整理 PDF 档案时，利用分类置信度实现自动化归档（扫描件文件夹、文本件文件夹、混合件进入人工队列）。

## 项目亮点

与通用的 PDF 解析库（如 `pdfplumber`、`PyPDF2`）或纯 OCR 方案（如 Tesseract）相比，pdf-inspector 最大的差异化在于将「分类」这一决策步骤内置为一级功能，给出了可量化的置信度分数和逐页路由建议，这是同类工具很少提供的。其速度优势也十分突出——文本型 PDF 的处理耗时控制在 200ms 以内（单页分类仅需数十毫秒），这得益于 Rust 的系统级性能和无依赖轻量设计，使得成本估算不再依赖外部网络。此外，它对 Markdown 结构的还原度较高（标题层级、阅读顺序、复杂表格），而非简单输出纯文本，这让下游应用（如向量导入、Markdown 知识库）直接受益。多语言运行时支持也为团队异构架构提供了极大的整合便利。

## 相关链接

- [GitHub 仓库](https://github.com/firecrawl/pdf-inspector)
- [Crates.io 发布页](https://crates.io/crates/pdf-inspector)
- [Python 包索引](https://pypi.org/project/pdf-inspector/)
- [Firecrawl 官网](https://firecrawl.dev)
