---
tags:
  - trending
  - article
repo: denoland/celld
date: 2026-08-09
language: Rust
stars_total: 2629
stars_today: 432
---
## 项目概述

celld 是一个开源的、自托管的分布式 Durable Objects 守护进程，允许你在自己的机器上运行 Cloudflare Workers 和 Durable Objects。它解决了开发者在云厂商锁定（vendor lock-in）下的痛点：无需依赖 Cloudflare 的托管服务，即可获得 Durable Objects 的全部能力，同时保持数据自主权和基础设施控制权。

每个 celld 对象都是一个独立的 SQLite 数据库，通过名称寻址，并复制到你拥有的 S3 兼容存储桶中。节点之间仅通过该存储桶协调，无需控制平面或共识协议。由于每个对象本身就是一个小型数据库，应用天然实现了分片——单一共享数据库的争用和爆炸半径问题被设计性地消除，而非被动管理。空闲的 cell 会自动休眠到近乎零的资源占用。

项目目标用户包括：希望摆脱云厂商依赖的独立开发者、需要在自有基础设施上提供多租户服务的团队、以及追求极致弹性和数据主权边缘计算场景的技术人员。

## 核心功能

- **自托管 Durable Objects**：在自有机器上完整实现 Cloudflare Workers 与 Durable Objects 的运行时环境，API 兼容，迁移成本极低。
- **基于 S3 的无协调协作**：多个节点仅通过共享的 S3 兼容存储桶通信，利用对象存储的 compare-and-swap（CAS）原语确保同一时刻只有一个节点拥有特定 cell，无需成员协议、故障检测器或共识服务。
- **持续 SQLite 复制**：每个 cell 的 SQLite 数据库持续增量复制到存储桶；当 cell 迁移或唤醒时，新节点从存储桶恢复数据库并继续执行。存储桶是持久的事实来源，节点可随意替换。
- **空闲休眠**：长期无请求的 cell 自动进入休眠状态，几乎不消耗 CPU 与内存，显著降低闲置成本。
- **名称寻址**：对象通过名称直接访问，无需关心其当前运行在哪台机器上，系统自动处理路由与迁移。
- **可验证的安装与部署**：提供一键安装脚本，二进制产物支持 GitHub Attestation 验证，确保供应链安全。

## 技术架构

celld 的核心设计理念是“存储即协调”（storage-as-coordination），彻底颠覆了传统分布式系统的构建范式。

每个 celld 节点内置 V8 引擎，直接执行 Wrangler 构建的 Worker 包。集群中的所有节点共享一个 S3 兼容存储桶，该桶中保存三类数据：部署包（deployments）、各 cell 的状态快照（cell state）、以及小型的所有权记录（ownership records）。节点之间的协调完全依赖对象存储的原子操作——通过 CAS 更新所有权记录，实现单写者（single-writer）语义，避免了传统分布式系统中最棘手的脑裂（split-brain）问题。

这一架构带来的显著优势是：**没有控制平面**、**没有心跳检测**、**没有 Paxos/Raft 共识集群**。系统的复杂度被大幅降低，运维模型简化为“存储桶可用，系统可用”。任何节点故障或重启都不会影响系统整体，因为存储桶始终保有全部持久状态，新节点加入或旧节点恢复后可以立即接管。

每个 cell 的 SQLite 数据库是独立维护的，这意味着数据隔离天然存在——一个 cell 的写入峰值或数据损坏不会影响其他 cell。应用层通过对象粒度进行分片，避免了传统共享数据库的“吵闹邻居”问题。此外，SQLite 单文件数据库的设计使得复制和恢复操作非常轻量，配合增量同步机制，cell 迁移通常在毫秒级完成。

## 安装与使用

**安装**（Linux/macOS）：

```sh
curl -fsSL https://celld.dev/install.sh | sh
```

安装完毕后，将 `~/.local/bin` 加入 `PATH` 环境变量（如果提示需要）。安装后的二进制产物可通过 `gh attestation verify` 验证其真实性与完整性。

**最小使用示例**：

1. 配置一个 S3 兼容存储桶（如 AWS S3、MinIO、Cloudflare R2 等），并获取访问密钥。
2. 启动第一个 celld 节点：

```sh
celld start --bucket my-bucket --access-key xxx --secret-key yyy --region us-east-1
```

3. 部署 Worker 项目（需已使用 Wrangler 构建）：

```sh
celld deploy ./dist/worker.js --name my-worker
```

4. 再次启动第二个节点（使用同一存储桶），实现自动负载均衡与容灾：

```sh
celld start --bucket my-bucket --access-key xxx --secret-key yyy --region us-east-1
```

现在你的 Durable Objects 已运行在自托管集群上，支持水平扩展与多节点冗余。

## 适用场景

- **边缘计算基础设施**：在自有边缘节点上运行地理分布式应用，数据留在本地，满足数据主权和低延迟要求。
- **多租户 SaaS 平台**：每个租户对应一个独立 cell，天然隔离数据与资源，支持按租户粒度弹性伸缩。
- **成本敏感型 Web 服务**：利用空闲休眠机制大幅降低长尾请求服务开销，将闲置成本压缩至近乎零。
- **合规与私有化部署**：政府、金融、医疗等对数据驻留有严格要求的行业，可在内网/专用云上完全自建同 Firebase/Cloudflare Durable Objects 类似的能力。

## 项目亮点

- **无共识分布式**：完全绕开 Paxos/Raft 等一致性协议，将协调负担转移给对象存储的原子操作，设计简洁且难以出错。
- **精简运维模型**：唯一的运维依赖是 S3 兼容存储桶，无需维护控制平面、服务发现或故障转移组件，从根本上降低了分布式系统的运维复杂度。
- **弹性资源效率**：每个对象独立数据库 + 休眠机制，使得资源分配精确到对象粒度，避免传统共享数据库的资源浪费。
- **高可移植性**：代码基于 Cloudflare Workers 生态标准编写，兼容现有工具链和开发流程，迁移成本极低（仅需替换运行时入口）。
- **数据自主权**：源代码开源（Apache-2.0），数据存储于自有存储桶，彻底摆脱云厂商绑定。

## 相关链接

- [GitHub 仓库](https://github.com/denoland/celld)
- [官方网站](https://celld.dev)
- [项目文档](https://celld.dev/docs)
