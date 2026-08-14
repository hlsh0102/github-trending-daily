---
tags:
  - trending
  - daily
date: 2026-08-14
type: daily
count: 10
---

# GitHub Trending — 2026-08-14

## 1. [[repos/cathrynlavery__diagram-design|cathrynlavery/diagram-design]]

Diagram Design 是一个面向 Claude Code 等 AI 编程工具的技能包，提供 27 种编辑级风格的图表类型（如流程图、金字塔图、飞轮图等），全部以自包含的 HTML 和 SVG 输出，不依赖 Figma 或通用模板。它解决了 AI 生成图表样式千篇一律、与品牌视觉脱节的问题，能够通过读取网站自动匹配配色和字体，并支持将 draw.io 文件重新绘制为所需格式。适合需要在文档或网站中快速生成高质量、符合品牌风格图表的开发者、设计师和技术写作者。

[GitHub](https://github.com/cathrynlavery/diagram-design)
[详细介绍 →](2026-08-14/articles/01-cathrynlavery__diagram-design.md)

## 2. [[repos/semantica-agi__semantica|semantica-agi/semantica]]

Semantica 是一个开源的图原生基础设施，用于构建可问责的 AI 系统。它帮助企业从数据中提取关键信息，构建上下文图和知识图谱，并在其上运行图分析和因果推理，同时记录完整的决策来源。该项目面向金融、医疗等高风险、强监管领域，支持 RDF 和 LPG 等多种图存储格式，并遵循 W3C 标准，确保可解释、可追踪和可信赖。

[GitHub](https://github.com/semantica-agi/semantica)
[详细介绍 →](2026-08-14/articles/02-semantica-agi__semantica.md)

## 3. [[repos/anthropics__skills|anthropics/skills]]

该仓库是Anthropic公开发布的Agent Skills实现集合，包含一系列用于Claude的、自包含的技能文件夹（每个技能包含SKILL.md指令文件及相关资源）。这些技能覆盖创意应用、技术任务和企业工作流等多个领域，旨在让Claude能以可重复的方式完成特定任务。适用于希望利用或参考Claude技能系统来扩展AI助手能力的开发者和企业用户。

[GitHub](https://github.com/anthropics/skills)
[详细介绍 →](2026-08-14/articles/03-anthropics__skills.md)

## 4. [[repos/cactus-compute__needle|cactus-compute/needle]]

Needle 2 是一个面向手机、可穿戴设备、智能家居和机器人等小型设备的开源基础模型，参数量为4500万，整个模型打包为约14MB的二进制文件，可在约28MB内存中运行完整会话。它专为工具调用、设备使用和结构化数据提取而设计，支持Python环境下的推理、LoRA微调和导出，并通过内置的置信度评分和工具检索机制，在极小资源占用下提供可靠的结构化输出，适合物联网和边缘计算场景。该模型采用自研的简单注意力网络架构和CQ2量化压缩技术，在体积上远小于同类模型，同时保持有竞争力的性能。此仓库是其Python包，包含推理、LoRA微调和导出功能，安装后即可使用。

[GitHub](https://github.com/cactus-compute/needle)
[详细介绍 →](2026-08-14/articles/04-cactus-compute__needle.md)

## 5. [[repos/altic-dev__FluidVoice|altic-dev/FluidVoice]]

FluidVoice 是一款开源的 macOS 离线语音转文字听写应用，所有处理均在本地完成，无需网络连接且数据不会离开设备。它利用本地 AI 模型实现近乎零延迟的实时听写，适合注重隐私且需要快速、准确语音输入的用户。项目遵循 GPL-3.0 许可证，可通过 Homebrew 安装或手动下载最新版本。

[GitHub](https://github.com/altic-dev/FluidVoice)
[详细介绍 →](2026-08-14/articles/05-altic-dev__FluidVoice.md)

## 6. [[repos/unslothai__unsloth|unslothai/unsloth]]

Unsloth 是一个本地运行的桌面应用程序，用于运行和训练大型语言模型（LLM）和扩散模型，支持 Qwen3.8、Kimi K3、MiniMax-H3、Gemma 4、DeepSeek-V4、FLUX 等模型。它旨在简化模型的使用和微调流程，适合需要在本地环境中进行模型实验和开发的开发者。通过提供直观的用户界面，用户无需深入底层技术细节即可完成模型的上手操作和训练任务。

[GitHub](https://github.com/unslothai/unsloth)
[详细介绍 →](2026-08-14/articles/06-unslothai__unsloth.md)

## 7. [[repos/macro-inc__macro|macro-inc/macro]]

Macro 是一个面向团队的统一工作空间，将邮件、聊天、文档、任务、代理、通话和 CRM 集成在一个界面中，并通过共享的团队级 AI 记忆实现各模块间的 @ 链接和统一搜索。该项目旨在解决团队因使用 Slack、Linear、Notion 等分散工具而导致的信息割裂和协作效率低下的问题。它适合希望减少工具切换、提升团队协作效率的中小型团队使用，项目采用 Rust 编写并遵循 AGPL-3.0 许可。

[GitHub](https://github.com/macro-inc/macro)
[详细介绍 →](2026-08-14/articles/07-macro-inc__macro.md)

## 8. [[repos/megadose__holehe|megadose/holehe]]

holehe 是一个开源的 OSINT（开源情报）工具，用于检查指定邮箱地址是否在 Twitter、Instagram、Imgur 等超过 120 个网站上注册过账号。它通过利用网站的“忘记密码”功能来查询注册信息，且不会向目标邮箱发送任何通知，从而避免惊动被调查者。该工具以 Python 编写，既可作为命令行工具使用，也可作为 Python 库集成到其他自动化情报收集脚本中，适合安全研究人员、渗透测试人员及隐私保护相关从业者使用。

[GitHub](https://github.com/megadose/holehe)
[详细介绍 →](2026-08-14/articles/08-megadose__holehe.md)

## 9. [[repos/smicallef__spiderfoot|smicallef/spiderfoot]]

SpiderFoot 是一个开源的 OSINT（开源情报）自动化工具，用于威胁情报分析和攻击面测绘。它集成了超过 200 个数据源模块，能够自动收集、分析并关联公开信息，帮助安全研究人员和渗透测试人员识别目标资产可能存在的风险。该工具提供 Web 界面和命令行两种使用方式，支持数据导出与自定义关联规则，适用于安全评估、漏洞管理和红队侦察等场景。

[GitHub](https://github.com/smicallef/spiderfoot)
[详细介绍 →](2026-08-14/articles/09-smicallef__spiderfoot.md)

## 10. [[repos/NVIDIA-NeMo__Switchyard|NVIDIA-NeMo/Switchyard]]

Switchyard 是一个用 Rust 编写的 LLM 流量代理和库，用于在模型和提供商之间路由请求，同时保持对 OpenAI 和 Anthropic API 的原生兼容。它解决了大型语言模型应用中模型选择、基准测试和成本/性能优化的问题，支持协议转换、多后端路由和操作指标收集。该项目面向需要灵活管理多种模型调用、进行 A/B 测试或实现自定义路由算法的开发者。目前处于预 alpha 阶段，API 可能发生较大变化，不适合生产环境使用。

[GitHub](https://github.com/NVIDIA-NeMo/Switchyard)
[详细介绍 →](2026-08-14/articles/10-NVIDIA-NeMo__Switchyard.md)
