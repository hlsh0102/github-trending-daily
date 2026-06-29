---
tags:
  - trending
  - article
repo: opendatalab/MinerU
date: 2026-06-29
language: Python
stars_total: 71914
stars_today: 380
---
## 项目概述

MinerU 是一个专注于将复杂文档（如 PDF、Office 文件等）转换为大语言模型（LLM）可直接使用的 Markdown 或 JSON 格式的开源工具。它解决了当前 AI 应用中一个关键痛点：非结构化文档数据难以被 LLM 高效理解与利用。无论是 PDF 中的表格、图片、多栏排版，还是 Word、PPT 中的复杂元素，MinerU 都能精准解析并输出结构化、语义化的内容，为构建智能体（Agent）工作流提供高质量的数据基础。目标用户包括数据科学家、AI 工程师、文档处理开发者以及任何需要将大量文档转化为训练数据或知识库的个人与团队。

## 核心功能

- **智能文档解析**：支持 PDF、Word、PPT、Excel、图片等多种格式，自动识别并处理版面布局、表格、图表、页眉页脚等复杂元素。
- **高质量结构化输出**：将解析结果直接转换为 Markdown 和 JSON 格式，保留文档的层级结构、表格关系、列表顺序等语义信息，方便 LLM 直接消费。
- **多栏与跨页处理**：能够正确处理多栏排版、跨页表格、同一页内嵌套表格等复杂场景，保证输出内容的连续性和准确性。
- **公式与代码识别**：内含识别能力可准确提取文档中的数学公式、代码块，并格式化为对应的 Markdown 语法，避免信息丢失。
- **元数据保留**：在 JSON 输出中保留字体、颜色、坐标、超链接等元数据，便于下游应用进行精细化处理或索引。
- **推理优化与加速**：支持 GPU 加速和批量处理，可在有限硬件资源下高效运行，并提供推理优化选项，平衡速度与精度。

## 技术架构

MinerU 采用基于深度学习的端到端文档解析架构，核心由多个专用模型组成：

1.  **版面分析模型**：基于 Transformer 的视觉模型，用于识别文档页面的区域类型（文本、表格、图片、页眉页脚等），并生成精确的边界框与类别标签。
2.  **OCR 引擎**：集成高性能 OCR 模型，用于提取图片、扫描件或非可编辑 PDF 中的文字内容，支持中英文等多种语言。
3.  **表格结构识别模型**：专门设计的模型，用于从表格区域中恢复行、列、合并单元格等结构信息，并输出可被 Markdown 表格语法解析的原生结构。
4.  **公式识别模型**：专用于 LaTeX 公式的检测与识别，能够将文档中的数学表达式转换为格式正确的 LaTeX 代码。
5.  **后处理与格式化引擎**：整合所有模型的输出，进行去重、排序、层叠合并、版面流式计算，最终输出语义一致、结构清晰的 Markdown 或 JSON 文档。

整体设计遵循“分而治之”的思路：先通过版面分析进行区域分割，再对不同类型区域调用专用解析模型，最后通过后处理引擎统一编排输出。这种模块化设计使得每个组件都可以独立优化，也便于未来集成更先进的基础模型。

## 安装与使用

**推荐环境**：Python 3.8+，CUDA（如果使用 GPU 推理）。

**通过 pip 安装**：

```bash
pip install mineru
```

**推荐使用 Docker 部署**：

```bash
docker pull opendatalab/mineru:latest
docker run -it --rm -v /path/to/your/docs:/data opendatalab/mineru:latest mineru /data/input.pdf -o /data/output/
```

**最小使用示例**：

```python
from mineru import MinerU

# 初始化
extractor = MinerU()

# 解析 PDF 文件
result = extractor.extract("document.pdf", output_format="markdown")

# 输出 Markdown 格式的文档内容
print(result.markdown)

# 保存到文件
result.save("output.md")
```

**命令行使用**：

```bash
# 解析单个 PDF 文件，输出为 Markdown
mineru input.pdf -o output.md

# 指定输出为 JSON 格式
mineru input.pdf -o output.json --format json

# 批量处理目录中的所有 PDF
mineru --input-dir ./pdfs --output-dir ./outputs --format markdown
```

对于更高级的用法（如自定义模型配置、调整推理参数、使用 GPU 等），请参考 `--help` 命令或官方文档。

## 适用场景

- **RAG（检索增强生成）系统构建**：将企业内部文档（如合同、报告、操作手册）转换为结构化知识库，为 LLM 驱动的问答系统提供高质量检索源。
- **LLM 训练数据准备**：从学术论文、书籍、网页等大量非结构化 PDF 中提取训练数据，清洗并格式化后用于微调或预训练大模型。
- **智能文档分析平台**：作为核心 OCR 和版面解析引擎，嵌入 SaaS 或企业级文档管理系统，提供文档分类、摘要、信息提取等能力。
- **数据清洗与知识管理**：将扫描件、图片式 PDF 等难以编辑的文档转化为可检索、可复制的文本和表格数据，用于知识资产数字化和管理。

## 项目亮点

- **端到端一站式**：无需多个工具组合，一个项目即可实现从 PDF/Office 到结构化 Markdown/JSON 的完整流程，降低了集成成本。
- **高精度与鲁棒性**：基于前沿的视觉-语言模型，在复杂排版（如多栏、图文混排、不规则表格）场景下依然保持极高的解析质量，远超传统 OCR 方案。
- **LLM 原生适配**：输出格式专为 LLM 优化。Markdown 可直接嵌入提示词，JSON 可被结构化调用，极大简化了 Agent 工作流的开发难度。
- **活跃的开源生态**：社区活跃，更新频繁，Star 数超过 7 万，且有配套的 Web 演示、桌面客户端、API 服务，降低了使用门槛。
- **可扩展性强**：模型组件可被替换或微调，支持定制化需求。也提供了 Docker 镜像，便于生产环境部署和分布式处理。

## 相关链接

- [GitHub 仓库](https://github.com/opendatalab/MinerU)
- [在线体验（零安装 Web 版）](https://mineru.net/?source=github)
- [Hugging Face 在线 Demo](https://huggingface.co/spaces/opendatalab/MinerU)
- [ModelScope 在线 Demo](https://www.modelscope.cn/studios/OpenDataLab/MinerU)
- [Google Colab 演示](https://colab.research.google.com/gist/myhloli/a3cb16570ab3cfeadf9d8f0ac91b4fca/mineru_demo.ipynb)
