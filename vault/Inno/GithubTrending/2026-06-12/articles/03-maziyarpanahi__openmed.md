---
tags:
  - trending
  - article
repo: maziyarpanahi/openmed
date: 2026-06-12
language: Python
stars_total: 2914
stars_today: 426
---
## 项目概述
OpenMed 是一个本地优先的开源医疗人工智能框架，致力于解决医疗数据隐私与 AI 能力之间的核心矛盾。它允许开发者和医疗机构在本地硬件上运行实体提取、PII 去标识化等临床文本处理任务，无需将敏感患者数据上传到云端。项目目标用户包括医疗软件开发人员、研究机构、医院 IT 部门以及注重数据隐私的健康科技创业者。通过提供从 Python 单行调用到 iOS Swift 原生应用的全链路支持，OpenMed 让安全、私密的医疗 AI 部署变得触手可及。

## 核心功能
- **临床实体提取**：从非结构化临床文本中自动抽取症状、药物、诊断、检验值等医疗实体，支持中文、英文等多语言。
- **PII 去标识化**：内置敏感信息识别引擎，自动检测并脱敏患者姓名、身份证号、住址、电话号码等个人标识信息，满足 HIPAA/GDPR 合规要求。
- **1000+ 预训练模型库**：基于 Hugging Face 生态，涵盖医学命名实体识别、文本分类、关系抽取、问答等细分任务，覆盖专科与全科场景。
- **跨平台运行**：支持从笔记本 CPU 到 GPU 服务器的多种设备，并特别针对 Apple Silicon 芯片进行优化（MLX 框架），可在 iPhone/iPad 上离线运行。
- **一键式 Python API**：通过 `pip install openmed` 即可使用，核心推理调用仅需一行代码，降低医疗 AI 的工程门槛。
- **Swift 原生 SDK**：提供面向 Apple 生态的原生 Swift 包，便于在移动医疗应用中集成本地模型推理。

## 技术架构
OpenMed 采用模块化微服务架构，核心由以下组件构成：
- **模型调度层**：抽象了 PyTorch、ONNX Runtime、Apple MLX 等多种推理后端，根据硬件自动选择最优执行引擎。对于 Apple Silicon 设备，优先使用 MLX 获得高效的内存利用和推理速度。
- **临床流水线（Clinical Pipeline）**：定义了标准化的文本预处理、实体候选生成、后处理与规范化流程。支持 SPIKE（结构化提示与知识增强）等定制化提示策略。
- **统一模型接口**：所有预训练模型遵循一致的输入/输出格式，可通过 Hugging Face Hub 动态加载或下载后离线使用。模型分为“基座模型”和“专科适配器”两层，方便领域微调与持续学习。
- **隐私沙箱**：在推理生命周期内严格隔离数据——所有计算在本地内存中完成，模型权重可完全离线存储，避免任何网络通信导致的隐私泄露风险。
- **跨语言适配**：针对中文医疗文本特有的缩写、病名变体、中文数字等维度，设计了专门的 tokenizer 扩展与标签映射。

## 安装与使用
### 安装
```bash
pip install openmed
```
推荐使用 Python 3.10 及以上版本。如需 Apple MLX 加速，确保在 macOS 14+ 和 Apple Silicon 设备上运行。

### 最小可用示例
从临床文本中抽取实体并去标识化：
```python
from openmed import Pipeline

# 初始化医疗流水线
pipeline = Pipeline("clinical-ner")  # 自动下载最优模型

# 执行推理
text = "患者李明，男，45岁，因持续性胸痛于2024年3月入院，诊断为急性心肌梗死。"
result = pipeline(text)

# 查看实体
for entity in result.entities:
    print(f"{entity.text} -> {entity.label} (置信度: {entity.score:.2f})")
# 输出: 李明 -> PATIENT_NAME, 持续性胸痛 -> SYMPTOM, 急性心肌梗死 -> DIAGNOSIS

# 去标识化
deidentified = pipeline.deidentify(text)
print(deidentified)
# 输出: 患者[患者姓名]，男，45岁，因持续性胸痛于[入院日期]入院，诊断为急性心肌梗死。
```

### iOS/Swift 集成（片段）
```swift
import OpenMed

let pipeline = try OpenMed.Pipeline(model: "clinical-ner-mlx")
let result = pipeline.analyze("Patient John Doe reports headache.")
// result.entities 包含结构化数据
```

## 适用场景
- **电子病历（EHR）智能录入**：从医生口述或自由文本病历中自动提取结构化临床数据，降低人工编码负担。
- **医疗数据合规清洗**：在数据出库、二次分析或医学研究共享前，自动去除所有可识别个人身份的信息，确保数据隐私合规。
- **远程医疗与移动健康**：在患者端（iOS/Android）本地运行去标识化和初步诊断建议，避免敏感数据在传输途中暴露。
- **临床决策支持研究**：快速对大规模去标识化医疗文本进行实体统计与模式分析，支持流行病学研究和药物不良反应信号检测。

## 项目亮点
- **真正的本地优先**：与大多数依赖云端 API 的医疗 AI 工具不同，OpenMed 默认在本地完成全部推理。即使弱网或离线环境，功能不受影响。
- **开箱即用的临床知识**：1000+ 预训练模型覆盖了从病历命名实体识别到 ICD-10 编码推荐的广泛场景，无需从零训练。
- **无供应商锁定**：基于 Apache 2.0 许可证，模型权重完全开放，支持自托管与定制微调，不会因第三方服务变动而中断业务。
- **全平台覆盖**：从服务器集群到个人电脑，再到轻量级移动端，同一代码库逻辑可跨平台部署，降低维护成本。
- **专为敏感数据设计**：架构层面将隐私嵌入每一次操作，不进行默认的数据上传、日志记录或遥测。

## 相关链接
- [GitHub 仓库](https://github.com/maziyarpanahi/openmed)
- [PyPI 包](https://pypi.org/project/openmed/)
- [Hugging Face 模型库](https://huggingface.co/OpenMed)
- [技术论文 (arXiv)](https://arxiv.org/abs/2508.01630)
