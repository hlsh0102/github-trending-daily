---
tags:
  - trending
  - article
repo: firecrawl/pdf-inspector
date: 2026-08-04
language: Rust
stars_total: 8666
stars_today: 1699
---
## 项目概述

`pdf-inspector` 是一个用 Rust 编写的高性能 PDF 检测、分类与文本提取库，由 Firecrawl 团队开发并开源。该项目的核心目标是解决 PDF 处理流程中的首要痛点：**如何快速判断一个 PDF 是文本型还是扫描型（图像型）**，从而帮助开发者做出智能路由决策——是直接进行本地文本提取，还是将其发送到昂贵的 OCR 服务。

在当下的数据处理管线中，PDF 文件形态各异，据 Firecrawl 团队统计，约 54% 的 PDF 实际上并不需要 OCR。然而，传统工具链往往对每个 PDF 都盲目调用 OCR 服务，导致不必要的延迟和成本。`pdf-inspector` 通过极速的分类检测（约 10–50 毫秒）解决了这一问题，为大规模 PDF 处理场景提供了高效的预处理层。

该项目支持 Rust、Python、Node.js 以及浏览器 WebAssembly 等多语言环境，目标用户包括数据工程师、文档处理系统开发者、AI 应用构建者以及任何需要批量处理 PDF 的团队。

## 核心功能

- **智能分类检测**：在 10–50 毫秒内将 PDF 分类为 TextBased（纯文本）、Scanned（扫描件）、ImageBased（纯图像）或 Mixed（混合型），并给出 0.0–1.0 的置信度评分，同时支持逐页的 OCR 路由建议。
- **位置感知文本提取**：提取文本时保留字体信息、X/Y 坐标，并自动处理多栏排版，确定正确的阅读顺序。
- **Markdown 转换**：基于字体大小比例识别标题层级（H1–H4），自动识别项目符号、数字和字母列表，检测等宽字体生成代码块，通过矩形区域和文本对齐启发式算法提取表格，支持粗体/斜体格式、URL 链接以及分页符。
- **双模式表格检测**：通过 PDF 绘图指令的矩形检测和文本对齐的启发式检测双重机制，能够处理财务表格、脚注以及跨页续接表格。
- **CID 字体支持**：完整实现 ToUnicode CMap 解码，支持 Type0 / Identity-H 等复杂字体编码，确保 CJK 等非拉丁文字的正确提取。

## 技术架构

`pdf-inspector` 的核心架构以「采样优先」为设计原则。它在初步阶段并不解析整个 PDF 文档，而是仅抽取内容流（content streams）中的关键样本进行分析，从而在极短时间内完成分类判断。这种机制使其能够在不足 200 毫秒内完成一个文本型 PDF 的完整本地处理。

项目的模块化设计体现在跨语言绑定上：底层核心逻辑以 Rust 实现，通过 N-API 桥接 Node.js，通过 PyO3 提供 Python 绑定，并借助 WebAssembly 支持浏览器端运行。各语言暴露的 API 保持一致，使开发者可以在不同技术栈之间无缝切换。

在文本提取和 Markdown 转换层面，项目运用了多种启发式规则：例如通过字体大小与基准字体的比例确定标题级别，通过字体等宽属性识别代码块，以及基于坐标和几何关系重建表格结构。这种无 OCR 的纯算法路线，使其在速度和成本上拥有显著优势，同时也避免了依赖外部模型带来的环境复杂性。

## 安装与使用

以下是各语言环境下的基本安装方式：

**Rust（Cargo）**

```bash
cargo add pdf-inspector
```

**Python（pip）**

```bash
pip install pdf-inspector
```

**Node.js（npm）**

```bash
npm install @firecrawl/pdf-inspector
```

**浏览器（WebAssembly）**

可通过 npm 包直接在前端项目中引入。

最小使用示例（以 Python 为例）：

```python
import pdf_inspector

# 检测 PDF 类型
result = pdf_inspector.classify("document.pdf")
print(result.kind)          # "TextBased" / "Scanned" / "ImageBased" / "Mixed"
print(result.confidence)    # 0.0 - 1.0

# 提取文本并转换为 Markdown
markdown = pdf_inspector.to_markdown("document.pdf")
print(markdown)
```

在 Rust 中，使用方式同样简洁：

```rust
use pdf_inspector::inspect;

fn main() {
    let result = inspect("path/to/file.pdf").expect("解析失败");
    println!("类型: {}", result.kind);
    println!("置信度: {}", result.confidence);
}
```

## 适用场景

- **大规模文档管道预处理**：在需要将 PDF 批量送入下游系统的场景中，先使用 `pdf-inspector` 完成分类和轻量提取，只有扫描件才转发给 OCR 服务，大幅降低计算成本和响应时间。
- **RAG（检索增强生成）与 AI 应用**：将 PDF 转换为带结构的 Markdown 后，作为向量数据库的输入源，提升知识库检索质量；位置感知能力可用于版面分析。
- **文档管理系统的内容索引**：快速提取标题、正文和表格结构，用于企业文档管理、法律文书检索等领域的内容归档与搜索。
- **前端浏览器端 PDF 解析**：借助 WebAssembly 绑定，在浏览器本地完成 PDF 交
