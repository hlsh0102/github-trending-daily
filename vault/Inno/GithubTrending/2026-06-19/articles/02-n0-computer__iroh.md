---
tags:
  - trending
  - article
repo: n0-computer/iroh
date: 2026-06-19
language: Rust
stars_total: 10077
stars_today: 369
---
## 项目概述

iroh 是一个用 Rust 编写的模块化网络栈，其核心理念是“按公钥拨号”而非传统的 IP 地址。在当今动态 IP 环境、移动网络和容器化部署中，IP 地址常常变化或不可靠，iroh 通过公钥标识端点，自动发现、维护并优化连接路径。该项目由 n0-computer 团队开发，旨在解决分布式应用和 P2P 通信中连接建立与维护的痛点。目标用户包括需要构建去中心化应用、实时同步、边缘计算或私有通信系统的开发者。

## 核心功能

- **按公钥拨号**：使用节点公钥作为唯一标识，irroh 自动解析并连接到目标节点，无需关心其 IP 地址变化。
- **自动 NAT 穿透**：内置 UDP 打洞技术，优先建立对等直连；若直连失败，则自动回退到公共中继服务器。
- **基于 QUIC 协议**：底层采用 noq 实现的 QUIC 协议，提供认证加密、多路复用流、流优先级控制和数据报支持，避免队头阻塞。
- **模块化协议组合**：提供如 `iroh-blobs`（基于 BLAKE3 的内容分发协议）等预构建协议模块，开发者可快速组合扩展。
- **持续性能优化**：通过公开的性能测试平台持续测量连接质量，确保直连和中继路径的延迟与吞吐量达到最优。
- **跨平台支持**：纯 Rust 实现，可运行在 Linux、macOS、Windows 等主流操作系统上。

## 技术架构

iroh 的技术栈以 QUIC 协议为核心，其架构特点包括：

- **分层设计**：底层网络传输层（noq 实现的 QUIC）负责加密、多路复用和数据报；中间层是拨号与连接管理层，负责公钥解析、NAT 穿透和中继选择；上层提供可组合的应用协议接口。
- **公钥身份体系**：每个节点拥有一对 Ed25519 密钥对，公钥作为全局唯一标识。连接建立时通过公钥验证身份，无需证书签发机构。
- **混合连接策略**：优先尝试 UDP 打洞建立直连；若失败，则通过分布式或中心化中继服务器转发数据，中继节点之间也可建立优化转发路径。
- **性能可测量**：项目公开性能测试平台（iroh-perf），持续测量不同网络条件下的连接延迟和吞吐量，为路径选择算法提供数据支持。
- **异步运行时**：基于 Rust 的 async/await 模型，利用 tokio 或 smol 等运行时实现高并发、低内存占用的网络 I/O。

## 安装与使用

### 安装

作为 Rust 库，在项目的 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
iroh = "0.35"
```

或通过 `cargo install` 安装 iroh（如果提供 CLI 工具）：

```bash
cargo install iroh
```

### 最小可用示例

以下示例展示如何建立一个 iroh 端点并连接到另一个节点：

```rust
use iroh::Endpoint;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let ep = Endpoint::builder().bind().await?;
    let my_id = ep.node_id();

    // 连接到对端（对端公钥为 pubkey_bytes）
    let conn = ep.connect(pubkey_bytes, &["localhost:1234"]).await?;
    let (mut send, mut recv) = conn.open_bi().await?;
    send.write_all(b"Hello from iroh!").await?;
    send.finish()?;
    let mut buf = vec![0u8; 1024];
    let n = recv.read(&mut buf).await?;
    println!("Received: {:?}", &buf[..n]);
    Ok(())
}
```

更多高级用法（如使用 `iroh-blobs` 传输文件）请参考[官方文档](https://iroh.computer/docs)。

## 适用场景

- **去中心化文件同步**：利用 `iroh-blobs` 协议在多个节点间同步文件，节点离线后再上线可自动重新连接，无需静态 IP。
- **远程设备管理与监控**：管理位于 NAT 后方的边缘设备（如 IoT 设备、家庭服务器），通过公钥直接连接，无需端口映射。
- **实时协作应用**：如分布式白板、聊天应用，使用 iroh 的流和数据报功能实现低延迟、加密的 P2P 通信。
- **私有网络服务发现**：在零信任环境中建立服务网格，节点通过公钥认证自动发现并连接到其他微服务。

## 项目亮点

与传统的 WebRTC、libp2p 或 TCP/TLS 方案相比，iroh 的差异化优势在于：

- **QUIC 原生优势**：无需额外封装，直接利用 QUIC 的加密、流控制、0-RTT 握手和连接迁移能力，减少协议栈复杂度。
- **公钥即地址**：无需 DHCP、DNS 或证书颁发机构，所有节点天然自带全局唯一身份，适合去中心化架构。
- **最优路径自动选择**：结合打洞和中继，兼顾直连的低延迟和中继的可靠性，且通过持续性能测试保证路径质量。
- **模块化可组合**：提供 `iroh-blobs` 等协议模块，开发者可像搭积木一样构建自定义 P2P 协议，降低重复开发成本。
- **纯 Rust 生态**：利用 Rust 的内存安全性和高性能，无运行时依赖，适合嵌入式或资源受限设备。

## 相关链接

- [GitHub 仓库](https://github.com/n0-computer/iroh)
- [官方文档](https://iroh.computer/docs)
- [Rust API 文档](https://docs.rs/iroh)
- [社区 Discord](https://discord.com/invite/DpmJgtU7cW)
