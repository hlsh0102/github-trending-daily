---
tags:
  - trending
  - article
repo: LMCache/LMCache
date: 2026-06-13
language: Python
stars_total: 8686
stars_today: 28
---
## 项目概述

LMCache 是一个专为大规模 LLM 推理设计的 KV Cache 管理层，旨在解决长上下文推理过程中显存瓶颈与重复计算问题。随着大语言模型上下文窗口不断扩展，KV Cache 的存储和复用成为推理性能的关键限制因素——传统方案往往将 KV Cache 完全存储在 GPU 显存中，导致显存利用率低、推理延迟高、多轮对话场景下重复计算严重。LMCache 通过引入分层缓存架构，在 GPU 显存、CPU 内存和分布式节点间智能调度 KV Cache，将缓存命中率提升至 90% 以上，同时将首 token 延迟降低 5-10 倍。该项目的目标用户包括：构建长上下文 LLM 应用的开发者、部署大规模推理服务的运维团队、以及研究 LLM 推理优化的科研人员。

## 核心功能

- **分层 KV Cache 管理**：自动在 GPU 显存、CPU 内存和远程节点之间缓存 KV 状态，支持 LRU、LFU 等多种替换策略，最大化缓存命中率。
- **零拷贝跨设备传输**：通过 CUDA IPC 和 RDMA 技术实现 GPU↔CPU 和节点间 KV Cache 的零拷贝共享，避免数据搬运开销。
- **多轮对话缓存复用**：针对 Agent 工作负载和对话场景，自动识别并复用前缀 KV Cache，避免重复计算历史 token，将多轮对话推理延迟降低 5 倍以上。
- **动态预取与流水线**：基于注意力模式预测未来需要访问的 KV Cache 块，提前从慢速存储层预取到 GPU 显存，实现缓存加载与计算的重叠。
- **兼容主流推理框架**：提供与 vLLM、SGLang、TGI 等主流框架的无缝集成接口，支持 PyTorch 原生接入，无需修改模型代码。
- **多节点 CPU 内存共享**：支持多节点间通过高速网络（如 InfiniBand）共享 CPU 内存中的 KV Cache，实现跨节点的缓存池化，大幅扩展有效缓存容量。

## 技术架构

LMCache 采用分层解耦的架构设计，核心分为三层：**缓存管理层**、**存储后端层** 和 **传输引擎层**。

缓存管理层负责 KV Cache 的分布式哈希索引、生命周期管理和替换策略决策。它维护一个全局的 KV 块索引表，记录每个缓存块在各级存储中的位置和访问统计信息，支持细粒度的块级缓存而非整个序列缓存，从而在缓存碎片和复用粒度间取得平衡。

存储后端层支持多种存储介质：GPU 显存（基于 PyTorch CUDA 张量）、CPU 内存（使用内存映射文件或预分配共享内存）、以及远程节点内存（通过 RDMA 或 TCP 协议）。每个存储后端都实现了统一的 `put`/`get` 接口，并针对不同介质的特性进行优化——例如 GPU 后端利用 CUDA 流进行并发操作，CPU 后端使用内存池避免频繁分配。

传输引擎层是 LMCache 的性能关键所在。对于 GPU↔CPU 传输，它使用 CUDA IPC 机制实现进程间零拷贝共享；对于节点间传输，它支持 RDMA（InfiniBand/ROCE）和 TCP 协议，并通过多线程流水线实现传输与计算的重叠。最新引入的多进程（MP）架构将缓存管理与模型推理分离到不同进程中，避免了 GIL 竞争和 CUDA context 切换开销，在 MoE 模型上实现了 10 倍的推理性能提升。

## 安装与使用

LMCache 可通过 pip 快速安装：

```bash
pip install lmcache
```

如需使用 RDMA 或 CUDA IPC 特性，请安装完整依赖：

```bash
pip install lmcache[all]
```

最小可用示例——在 vLLM 中集成 LMCache：

```python
from vllm import LLM, SamplingParams
import lmcache

# 创建带 LMCache 的 LLM 实例
llm = LLM(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    enable_lmcache=True,           # 启用 LMCache
    lmcache_config={"chunk_size": 256, "max_cpu_cache_size": 100}  # GPU显存:CPU内存=1:100
)

# 多轮对话自动利用缓存
for turn in range(10):
    outputs = llm.generate(f"User turn {turn}: What is the capital of France?")
    print(outputs[0].outputs[0].text)
```

高级用法——自定义缓存策略：

```python
from lmcache import LMCacheEngine, StorageConfig

config = StorageConfig(
    gpu_memory_ratio=0.3,
    cpu_memory_limit="50GB",
    remote_url="rdma://node2:9400",
    eviction_policy="lru"
)
engine = LMCacheEngine(config)
engine.prefetch(prefix_ids=[1, 2, 3])  # 预计算前缀
```

## 适用场景

- **长上下文 RAG 应用**：当文档集超过 10 万 token 时，LMCache 可将首次推理延迟从分钟级降至秒级，通过复用历史 KV Cache 避免重新编码整个上下文。
- **多轮 Agent 工作负载**：Agent 在多轮工具调用和思考过程中，频繁重复使用系统提示和对话历史，LMCache 的智能复用能将每轮推理成本降低 80% 以上。
- **大规模推理服务集群**：在部署数百个模型副本的场景中，LMCache 的多节点 CPU 内存共享允许所有实例共享同一个 KV Cache 池，将整体缓存命中率提升至 95%，显著降低 GPU 显存压力和 TCO。
- **MoE 模型推理**：针对 Mixtral 等 MoE 模型的专家路由特性，LMCache 的新多进程架构通过分离缓存管理和专家调度，实现了 10 倍的推理吞吐提升。

## 项目亮点

与同类项目相比，LMCache 具有以下差异化优势：

1. **全栈硬件优化**：支持从单 GPU 到多节点 RDMA 集群的多种硬件配置，且针对 AMD MI300X 等非 NVIDIA 硬件也有专门优化，覆盖更广的部署场景。
2. **零开销集成**：提供与 vLLM、SGLang 等主流推理引擎的一行代码集成，用户无需修改模型代码或重写推理逻辑，即可获得缓存加速。
3. **极致性能**：在长上下文和多轮对话场景下，LMCache 可将首 token 延迟降低 5-10 倍，端到端推理吞吐提升 2-3 倍，且缓存命中率稳定在 90%+。
4. **社区活跃**：项目由学术界和工业界联合维护，有清晰的路线图（包括 2026 年 Q3 的分布式 GPU 共享、Q4 的模型并行支持），社区每周举行技术会议，生态快速成长。

## 相关链接

- [GitHub 仓库](https://github.com/LMCache/LMCache)
- [官方文档](https://docs.lmcache.ai/)
- [技术博客](https://blog.lmcache.ai/)
- [社区 Slack](https://join.slack.com/t/lmcacheworkspace/shared_invite/zt-3zxjao8h0-lRfBfnLqbALOtLsWn2ITxA)
- [项目路线图](https://github.com/LMCache/LMCache/issues/2923)
