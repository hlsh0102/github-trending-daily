---
tags:
  - trending
  - article
repo: maziyarpanahi/openmed
date: 2026-06-11
language: Python
stars_total: 2413
stars_today: 527
---
## 项目概述

OpenMed 是一个面向医疗健康领域的本地优先开源 AI 工具包，致力于在保障患者数据隐私的前提下，将临床文本转化为结构化洞察。项目提供实体抽取、PII（个人身份信息）脱敏等核心能力，并附带 1000 多个经过验证的医学专用模型。所有推理过程均在用户自有硬件上完成，无需将任何数据上传至云端。

OpenMed 专为医疗系统开发者、数据科学家、医疗机构以及隐私合规团队设计，目标是在不牺牲功能的前提下消除对第三方云服务的依赖，彻底解决医疗 AI 落地中的数据主权与合规问题。

## 核心功能

- **临床实体抽取**：从非结构化临床笔记、病历、放射学报告中自动提取疾病名称、药物、剂量、解剖部位、实验室检查值等医学实体。
- **PII 脱敏与去标识化**：检测并移除（或替换）患者姓名、身份证号、联系方式、地址等敏感信息，输出符合 HIPAA/GDPR 合规要求的结构化数据。
- **1000+ 医学专用模型**：基于 Hugging Face 生态，覆盖病理学、放射学、肿瘤学、心脏病学、精神病学等主要专科领域，支持 zero-shot 与微调两种使用模式。
- **纯本地推理**：所有模型推理完全在本地硬件上执行，不产生任何网络请求，最大限度降低数据泄露风险。
- **多端部署支持**：兼容 Python（通过 PyPI 包）、Apple MLX（原生 Swift App）等运行时，支持从服务器集群到 iPhone 终端的全栈部署。
- **单行代码 API**：提供高度简化的 Python 接口，一句话即可完成加载模型与执行预测的完整流程。

## 技术架构

OpenMed 采用分层解耦的设计，核心由三部分组成：

- **底层推理引擎**：通过苹果 MLX 框架与 PyTorch 后端实现统一的模型加载与推理接口。MLX 后端专门针对 Apple Silicon（M 系列芯片）优化，可在 Mac 设备上实现高效本地推理，同时为传统 x86 服务器提供 Python/CUDA 回退方案。
- **模型仓库层**：项目在 Hugging Face 上维护了一个开放模型仓库（OpenMed 组织），托管超过 1000 个经过筛选和评测的医学领域模型。这些模型涵盖各种规模和架构（从轻量级 DistillBERT 到 LLaMA 系列），用户可根据硬件的显存与算力自由选择。
- **应用层工具链**：提供面向不同临床场景的预制流水线，例如 `extract_entities()`、`deidentify_text()`、`classify_document()` 等高级函数，内部自动完成模型加载、预处理、推理与后处理。用户也可通过底层 API 自行组合构建定制工作流。

架构的核心理念是“本地优先（Local-first）”——所有数据路径严格限制在设备内存内，绝不暴露给外网。这通过三层隔离机制实现：无网络依赖的模型加载（模型预先下载）、本地 tokenizer 处理、本地输出序列化。网络只在首次下载模型时使用，后续推理全程离线。

## 安装与使用

**安装**

OpenMed 可通过 pip 直接安装，最低要求 Python 3.10+：

```bash
pip install openmed
```

如需使用 MLX 后端加速（仅限 macOS 且配备 Apple Silicon），可额外安装：

```bash
pip install openmed[mlx]
```

**最小可用示例**

以下示例演示如何加载一个临床实体抽取模型并对一段病历文本进行推理：

```python
from openmed import load_pipeline

# 加载预设的实体识别流水线（自动下载模型）
ner_pipeline = load_pipeline("entity-extraction")

# 输入一段临床笔记
text = "Patient John Doe (DOB: 1985-03-15) was diagnosed with metastatic pancreatic adenocarcinoma. Administered Gemcitabine 1000 mg/m² IV on day 1."

# 执行实体抽取
result = ner_pipeline(text)

# 输出结构化的实体列表
for entity in result["entities"]:
    print(f"{entity['type']}: {entity['text']} (confidence: {entity['score']:.2f})")
```

输出结果类似如下格式（具体字段取决于所选模型）：

```
NAME: John Doe (confidence: 0.98)
DATE: 1985-03-15 (confidence: 0.99)
DISEASE: metastatic pancreatic adenocarcinoma (confidence: 0.94)
DRUG: Gemcitabine (confidence: 0.96)
DOSAGE: 1000 mg/m² (confidence: 0.91)
ROUTE: IV (confidence: 0.93)
```

PII 脱敏操作同样简洁：

```python
deid_pipeline = load_pipeline("deidentification")
safe_text = deid_pipeline(text, replacement="[REDACTED]")
# 返回已替换敏感信息的文本
```

## 适用场景

- **临床数据分析/研究**：研究机构需要从大量非结构化电子病历中提取关键变量用于回顾性分析时，OpenMed 可在本地完成批量抽取，避免因云上传触发的伦理审查延迟。
- **院内集成 / EHR 系统增强**：医院业务系统（如电子健康记录系统）可通过本地 API 集成 OpenMed，在不改动现有网络架构和防火墙的策略下获得实体识别与脱敏能力。
- **移动端医疗应用**：移动医疗 App 开发者可以利用 Apple MLX 后端，在 iPhone / iPad 上直接运行医学模型，实现隐私保护下的离线智能问诊或健康记录分析。
- **合规数据处理**：面临 HIPAA、GDPR 或本地数据主权法规的企业，需要通过可审计的本地方案对医疗文本进行去标识化处理后方可共享或二次使用。

## 项目亮点

- **真正的数据主权**：与其他医疗 AI 服务不同，OpenMed 不需要将任何患者数据上传到云端。模型在本地运行，数据在设备内存中完成所有处理流程，从根源上杜绝了数据泄露风险。
- **开箱即用的丰富模型库**：项目附带 1000+ 个经过开源社区验证的医学模型，覆盖绝大多数临床专科，且全部免费使用。用户无需自己训练模型就能获得接近 state-of-the-art 的性能。
- **极简交互设计**：整个库的设计遵循“一行 Python 代码解决一个问题”的理念，极大降低了非 AI 专家的使用门槛。即使没有深度学习经验，临床研究人员也能快速上手。
- **全端生态覆盖**：从 Python 服务器端到原生 Swift 应用，OpenMed 提供了跨平台的统一编程模型。同样的代码逻辑可以不加修改地部署在实验室工作站、院内服务器、或 Apple 移动设备上。
- **学术开源双保险**：项目附有 arXiv 论文说明技术细节，并提供 Apache 2.0 开源许可，适合在学术研究和商用产品中自由使用。

## 相关链接

- [GitHub 仓库](https://github.com/maziyarpanahi/openmed)
- [Hugging Face 模型仓库](https://huggingface.co/OpenMed)
- [arXiv 论文](https://arxiv.org/abs/2508.01630)
- [PyPI 包](https://pypi.org/project/openmed/)
