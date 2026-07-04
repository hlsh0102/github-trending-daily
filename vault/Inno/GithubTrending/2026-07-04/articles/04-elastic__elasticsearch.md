---
tags:
  - trending
  - article
repo: elastic/elasticsearch
date: 2026-07-04
language: Java
stars_total: 77370
stars_today: 91
---
## 项目概述

Elasticsearch 是一个开源的分布式搜索与分析引擎，同时也是一款可扩展的数据存储和向量数据库。它专为生产级工作负载优化，能够在速度和相关性上满足严苛要求。作为 Elastic 开放平台的核心组件，Elasticsearch 支持在近实时场景下对海量数据集进行搜索、执行向量搜索、与生成式 AI 应用集成，并提供更多高级功能。无论是开发人员、数据工程师还是运维工程师，只要需要从大量数据中快速获取洞察，Elasticsearch 都是一个理想的选择。

## 核心功能

- **全文搜索**：提供高性能、高相关性的全文检索能力，支持复杂的查询语法、分词器和评分算法，适用于文档、网页内容等文本数据的搜索。
- **向量搜索**：内建向量数据库能力，支持近似最近邻（ANN）搜索，可与机器学习模型生成的嵌入向量配合，用于语义搜索、推荐系统和图像检索等场景。
- **近实时分析**：数据索引后通常在1秒内即可被搜索到，支持聚合、过滤和分组操作，能够对日志、指标、事务等数据执行实时分析和可视化。
- **分布式存储与扩展**：自动将数据分片分发到多个节点，支持水平扩展，即使节点故障也能通过副本保证数据可用性和查询持续性。
- **RESTful API**：所有操作均通过 HTTP 接口暴露，使用 JSON 格式进行数据交互，便于与任何编程语言或工具集成。
- **多数据源支持**：原生支持结构化、半结构化和非结构化数据，可存储 JSON 文档并动态映射字段类型，无需预先定义严格的 Schema。

## 技术架构

Elasticsearch 基于 Apache Lucene 构建，后者是业界领先的全文搜索引擎库。其核心架构特点包括：

- **分片与副本**：每个索引被分为多个分片（shard），每个分片是一个完整的 Lucene 索引。分片可分布在集群的不同节点上，副本分片则提供数据冗余和查询吞吐量提升。
- **节点类型**：集群中的节点可以扮演不同角色，如主节点（管理集群状态）、数据节点（存储数据和执行搜索）、协调节点（处理客户端请求并分发任务）等，使得架构高度灵活。
- **倒排索引**：为了支持快速全文搜索，Elasticsearch 使用倒排索引存储词条到文档的映射，并结合 TF-IDF 或 BM25 等评分模型计算相关性。
- **向量引擎**：基于 HNSW（Hierarchical Navigable Small World）图算法实现向量搜索，支持欧几里得距离、余弦相似度等多种度量方式，能够在大规模向量数据中高效检索。
- **集群发现与通信**：节点通过 Zen Discovery 或更现代的基于 Raft 的协调机制发现彼此，并使用内部传输协议进行数据同步和任务协调，保证集群的一致性。

## 安装与使用

### 安装
1. **下载并解压**：从 Elasticsearch 官方网站或 GitHub Releases 页面下载最新版本的压缩包，解压到目标目录。
2. **配置**：编辑 `config/elasticsearch.yml` 文件，设置集群名称、节点名称、网络绑定地址等参数。单机模式下大多采用默认配置即可。
3. **启动**：运行 `bin/elasticsearch`（Linux/Mac）或 `bin\elasticsearch.bat`（Windows）。默认监听在 `localhost:9200`。

### 最小可用示例
启动后，使用 curl 测试基本功能：
```bash
# 查看集群健康状态
curl -X GET "localhost:9200/_cluster/health?pretty"

# 创建一个索引
curl -X PUT "localhost:9200/my-index"

# 插入一条文档
curl -X POST "localhost:9200/my-index/_doc/1" -H "Content-Type: application/json" -d '{"title": "Hello World", "content": "Elasticsearch is awesome"}'

# 搜索文档
curl -X GET "localhost:9200/my-index/_search?q=Hello&pretty"
```

编程语言集成示例（Python 使用 `elasticsearch-py` 客户端）：
```python
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 插入文档
doc = {"title": "测试", "content": "这是一个测试文档"}
resp = es.index(index="test-index", id=1, document=doc)
print(resp['result'])

# 搜索
resp = es.search(index="test-index", query={"match": {"content": "测试"}})
print(resp['hits']['hits'])
```

## 适用场景

- **站内搜索**：电商网站商品搜索、知识库内容检索、博客文章搜索等，利用 Elasticsearch 的全文搜索和排序功能提升用户体验。
- **日志与指标分析**：集中收集服务器、应用或网络设备的日志数据，通过 Kibana 可视化工具进行实时监控、告警和故障排查。
- **向量检索与 AI 应用**：与大型语言模型（LLM）结合，实现检索增强生成（RAG）；或者为图像、音频等非文本数据构建相似度搜索服务。
- **安全分析与事件响应**：对安全日志进行实时分析和异常检测，支持 SIEM（安全信息和事件管理）场景，如威胁狩猎和取证调查。

## 项目亮点

- **性能与相关性**：基于 Lucene 的成熟搜索算法和自研向量引擎，在亿级数据量下仍能保持亚秒级响应和高搜索质量。
- **易于上手**：RESTful API 设计简洁，无需复杂配置即可快速启动；丰富的官方客户端库（Java、Python、Go、.NET 等）降低集成门槛。
- **生态完善**：与 Elastic Stack（Logstash、Kibana、Beats）深度集成，形成从数据采集、处理到可视化的全链条解决方案。
- **云与混合部署**：既可通过 Elastic Cloud 托管，也可自建集群；支持容器化部署（Docker、Kubernetes），适应不同环境需求。
- **社区活跃**：作为 GitHub 上星标超过 77k 的开源项目，拥有庞大的社区、丰富的插件和详细的文档，问题响应迅速。

## 相关链接

- [GitHub 仓库](https://github.com/elastic/elasticsearch)
- [Elasticsearch 产品页面](https://www.elastic.co/products/elasticsearch)
- [Elastic Cloud 托管服务](https://www.elastic.co/cloud/as-a-service)
- [Search Labs（技术博客与示例）](https://www.elastic.co/search-labs)
