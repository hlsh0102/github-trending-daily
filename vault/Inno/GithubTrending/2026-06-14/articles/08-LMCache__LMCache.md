---
tags:
  - trending
  - article
repo: LMCache/LMCache
date: 2026-06-14
language: Python
stars_total: 8964
stars_today: 238
---
## 项目概述

LMCache 是一个专为大语言模型（LLM）推理场景设计的 KV Cache 管理层，旨在解决长序列推理和多轮对话中计算与内存效率的瓶颈。核心思路是通过智能缓存、跨层次存储和高效传输策略，让 KV Cache 不再是推理链路上的短板，而是真正加速推理的引擎。目标用户包括 LLM 推理引擎开发人员、部署 LLM 服务的基础设施工程师，以及从事高性能计算和模型优化的研究人员。

## 核心功能

- 快速 KV Cache 缓存与检索：将计算结果复用机制引入 LLM 推理管线，避免在上下文复用场景中重复计算相同 KV Cache，显著降低首 token 延迟和整体推理时间。
- 多层存储后端支持：支持将 KV Cache 存放在 GPU 显存、CPU 内存、SSD 或分布式节点内存，并能根据访问频率和距离自动选择最优存储层次。
- 跨节点 Peer-to-Peer（P2P）共享：在多节点部署中，支持节点间直接通过高速网络（如 InfiniBand、NVLink）共享 CPU 内存中的 KV Cache，实现低延迟跨节点复用。
- 多进程（MP）架构优化：采用独立的后端进程处理缓存事务，将缓存操作与 GPU 计算解耦，避免阻塞推理主线程，特别适用于高并发或 MoE 模型场景。
- 无缝集成常见推理框架：提供 Python API，可与 vLLM、Hugging Face Transformers 等主流推理系统配合使用，通过少量代码修改即可启用缓存加速。
- 深度缓存策略配置：允许用户自定义缓存淘汰策略（如 LRU、LFU、TTL），以及预取策略，根据历史访问模式主动加载预期会再次使用的 KV Cache。

## 技术架构

LMCache 的核心架构围绕“异步缓存事务”与“分片存储管理”两个原则设计。缓存系统运行在独立的多进程环境中，通过共享内存和 IPC（进程间通信）与主推理进程交互，从而将缓存命中/写入操作的延迟从推理路径中剥离。

存储方面采用分层设计：最上层是 GPU 显存中的热缓存，用于存放当前批次或近期频繁访问的 KV Cache 块；中间层是 CPU 内存中的温缓存，通过高效的序列化格式（如 NumPy 数组或自定义内存布局）存储更大规模的 KV 数据；底层支持 SSD 或远端内存，用于存放不常用但可被预取的数据。

传输层针对不同硬件拓扑做了优化：当节点内 GPU 间共享缓存时，使用 NVLink 或 PCIe P2P；当跨节点共享 CPU 内存中的缓存时，使用 libfabric 或 NCCL 后端，实现零拷贝路径。架构上还支持“缓存预取”——根据 Prompt 的前缀哈希，在上一轮推理结束后异步加载下一轮可能用到的 KV 块。

## 安装与使用

推荐使用 pip 安装：

```bash
pip install lmcache
```

最简集成示例（与 vLLM 配合）：

```python
import lmcache
from vllm import LLM, SamplingParams

# 在创建 LLM 实例前启用 LMCache
lmcache.enable(vllm_llm=True)

llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1")
prompts = ["What is the capital of France?"]

# 第一次推理正常执行
outputs = llm.generate(prompts, SamplingParams(max_tokens=256))

# 第二次推理同一 Prompt 将利用缓存，加速首 token 输出
outputs = llm.generate(prompts, SamplingParams(max_tokens=256))
```

也可通过环境变量配置缓存存储后端和策略：

```bash
export LMCACHE_STORAGE_BACKEND="cpu"
export LMCACHE_KV_CACHE_SIZE_GB=32
```

## 适用场景

- 多轮对话系统：每次交互响应需要重新计算历史上下文 KV Cache，LMCache 可以在多轮之间复用部分缓存，使长对话的首 token 延迟降低 50% 以上。
- Agentic 工作负载：多步骤的 LLM 代理任务中频繁需要复用前一步推理的结果，LMCache 的预取和跨节点共享机制特别适用于这种模式。
- 长文档分析应用：处理数万 token 的上下文时，LMCache 的分层存储使得 KV Cache 不必全部占用 GPU 显存，降低对高端硬件的依赖。

## 项目亮点

与传统的 KV Cache 管理方案（如手工管理显存、简单 FIFO 淘汰）相比，LMCache 的差异化优势明显。首先，其多进程架构将缓存事务从推理热路径中移除，对推理吞吐量的影响接近零，而同类方案往往会在缓存操作时同步阻塞 GPU。其次，跨节点 P2P CPU 内存共享能力是新突破——其他方案通常只考虑单机内缓存，LMCache 将分布式缓存视为一等成员，特别适合多 GPU 集群部署。此外，活跃的社区维护、详尽的文档以及与 vLLM 等主流框架的深度集成，让该项目在本领域具有较高的成熟度和可用性。

## 相关链接

- [GitHub 仓库](https://github.com/LMCache/LMCache)
- [官方博客](https://blog.lmcache.ai/)
- [技术文档](https://docs.lmcache.ai/)
