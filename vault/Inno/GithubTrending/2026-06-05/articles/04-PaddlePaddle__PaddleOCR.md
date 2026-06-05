---
tags:
  - trending
  - article
repo: PaddlePaddle/PaddleOCR
date: 2026-06-05
language: Python
stars_total: 80107
stars_today: 141
---
## 项目概述

PaddleOCR 是由百度飞桨团队开发的一款高性能光学字符识别（OCR）工具包，旨在将 PDF 文档和图像高效转换为结构化数据（如 JSON 和 Markdown），为 AI 应用提供可直接用于大语言模型（LLM）和检索增强生成（RAG）的数据源。该项目解决了从非结构化图像或文档中提取文字、表格、公式等信息的关键痛点，特别适合需要构建智能文档处理系统的开发者和企业用户。PaddleOCR 拥有超过 80,000 个 GitHub Stars，并被 Dify、RAGFlow、Cherry Studio 等知名项目广泛采用，已经成为文档解析领域的标杆工具。

## 核心功能

- **智能文档解析（LLM-Ready）**：支持将 PDF 和图像转换为结构化 JSON 或 Markdown 数据，直接对接 LLM 和 RAG 系统，实现从视觉到文本的无缝转换。
- **SOTA 文档视觉语言模型**：内置 PaddleOCR-VL-1.6（0.9B）轻量级视觉语言模型，在 OmniDocBench v1.6 基准上达到 96.3% 的准确率，领先于同类算法。在文本、公式和表格识别方面表现优异，并对古籍、生僻字、印章等复杂场景有显著增强。
- **多语言支持**：支持超过 100 种语言的文字识别，涵盖简体中文、繁体中文、英文、日文、韩文、法文、俄文、西班牙文、阿拉伯文等，满足全球用户的跨国界应用需求。
- **轻量高效**：模型体积小巧（0.9B 参数），可在 CPU 或 GPU 上快速部署，兼顾高精度与低资源消耗，适合边缘设备和云服务场景。
- **端到端流程**：从图像预处理、文字检测、文字识别到结构化输出，提供完整的自动化管线，减少人工干预。

## 技术架构

PaddleOCR 基于百度飞桨（PaddlePaddle）深度学习框架构建，核心技术设计如下：

- **视觉语言模型（VLM）**：采用 PaddleOCR-VL 系列模型，结合视觉编码器和语言解码器，直接端到端理解文档布局和语义，无需传统的多阶段流水线。1.6 版本进一步优化了在复杂版面（如表格、公式、古籍）上的识别能力。
- **多阶段 OCR 管线**：对于非 VLM 场景，仍然保留经典的文字检测（如 DB、EAST）和识别（如 CRNN、SVTR）两阶段方案，支持灵活配置。
- **结构化输出引擎**：智能识别文档中的标题、段落、列表、表格、公式等元素，并自动转换为 Markdown 或 JSON 格式，保留排版思维。表格解析模块能还原单元格结构和行列关系。
- **预训练与迁移学习**：利用大规模多语言数据集进行预训练，用户可通过少量标注数据微调模型，适应特定领域（如发票、合同、证件）。
- **跨平台部署**：支持 Python 环境、Docker 容器、ONNX 导出等，兼容 Linux、Windows 和 macOS。

## 安装与使用

PaddleOCR 的安装非常简便，推荐使用 Python 3.8 或更高版本。

**安装步骤**：

```bash
# 安装 PaddlePaddle（如需 GPU 支持请参考官方文档）
pip install paddlepaddle

# 安装 PaddleOCR
pip install paddleocr
```

**最小可用示例**：

```python
from paddleocr import PaddleOCR

# 初始化识别器（使用轻量模型，自动下载）
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# 单张图像识别
img_path = 'example.jpg'
results = ocr.ocr(img_path, cls=True)

# 输出识别结果
for line in results[0]:
    print(line[1][0])  # 识别文本
    print(line[1][1])  # 置信度
```

**PDF 转 Markdown 示例**：

```python
from paddleocr import PPStructure

engine = PPStructure(show_log=True)
result = engine('document.pdf')
for res in result:
    print(res['type'], res['res'])
# 输出包含标题、表格、列表等结构化内容
```

详细文档和更多模型（如 VLM 版本）请参考项目 GitHub 仓库的 readme 文件。

## 适用场景

- **企业文档数字化**：将扫描的合同、发票、报告自动转为可编辑或可搜索的文本，用于数据归档和检索。PaddleOCR 的表格和公式识别能力尤其适合金融、保险、科研领域。
- **智能问答与 RAG 系统**：作为文档预处理器，将 PDF 或图像内容转为 LLM 友好的 Markdown/JSON，输入至 Dify、RAGFlow 等平台，构建基于私有知识的问答机器人。
- **多语言文献翻译与阅读**：对古籍、外文书籍或学术论文进行 OCR，结合翻译工具实现跨语言信息获取。对生僻字和古老字符的增强支持使其在此场景下具有独特优势。
- **边缘设备文字识别**：在手机、嵌入式设备或离线环境下部署轻量模型，实现身份证识别、车牌识别、商品标签扫描等应用，无需云服务器。

## 项目亮点

- **行业领先的准确性**：在标准基准测试（如 OmniDocBench）中保持最高水平，尤其对复杂文档（表格、公式、古籍）的解析能力远超同类工具。
- **轻量与可部署性**：0.9B 参数的 VLM 模型在保持高精度的同时，可在消费级 GPU 甚至 CPU 上运行，资源需求远低于竞品。
- **全生态集成**：已被 Dify（低代码 AI 平台）、RAGFlow（RAG 框架）和 Cherry Studio（AI 应用平台）等主流项目深度集成，可以直接调用，无需额外开发。
- **开源与活跃社区**：Apache-2.0 许可确保商业友好，80k+ Stars 和数千个依赖项目保证了持续的更新和维护，文档支持多语言（中、英、日、韩等）。

## 相关链接

- [GitHub 仓库](https://github.com/PaddlePaddle/PaddleOCR)
- [官网与在线体验](https://www.paddleocr.com)
- [DeepWiKi 技术解析](https://deepwiki.com/PaddlePaddle/PaddleOCR)
