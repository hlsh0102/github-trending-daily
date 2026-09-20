---
tags:
  - trending
  - article
repo: cloudflare/quiche
date: 2026-09-20
language: Rust
stars_total: 12096
stars_today: 31
---
## 项目概述

quiche 是 Cloudflare 开源的一个 QUIC 传输协议与 HTTP/3 的 Rust 实现，遵循 IETF 制定的相关规范。QUIC 是一种基于 UDP 的通用传输协议，旨在替代 TCP + TLS 的组合，提供更低延迟的连接建立、多路复用、连接迁移以及内建加密等能力；HTTP/3 则是构建在 QUIC 之上的 HTTP 语义映射。

quiche 解决的核心问题是：为开发者提供一个可嵌入、可控的 QUIC/HTTP/3 协议栈，使其能够在不绑定特定运行时或网络模型的前提下，把 QUIC 集成进既有系统。它不负责套接字管理、事件循环或定时器调度，而是把 I/O 和事件处理交由上层应用自行实现。这种设计让 quiche 可以适配不同的编程语言和运行环境。

目标用户包括：需要在自有服务中启用 HTTP/3 的服务端开发者、构建自定义网络客户端或代理的工程师、以及在嵌入式或高性能场景中希望精细控制协议行为的团队。它同时也被用于跨语言绑定，例如为 C/C++、Android 等环境提供接口。

## 核心功能

- **QUIC 传输协议实现**：支持连接建立、流管理、流量控制、丢包检测与重传、拥塞控制等 QUIC 核心机制，遵循 IETF QUIC 规范。
- **HTTP/3 支持**：在 QUIC 之上实现 HTTP/3 语义，包括请求/响应处理与 QPACK 头部压缩。
- **低层 API**：暴露处理 QUIC 数据包与连接状态的底层接口，由应用负责 I/O（如套接字）与事件循环。
- **可插拔的 I/O 模型**：不假设特定的异步运行时或线程模型，便于集成到多种架构中。
- **命令行应用**：仓库提供示例客户端与服务端程序，用于快速验证和实验协议行为。
- **跨语言集成能力**：通过 C 接口等方式被 curl、Android DNS 解析器等外部项目采用。

## 技术架构

quiche 使用 Rust 编写，强调内存安全与性能。其架构上的显著特点是"库而非框架"的定位：库内部维护连接状态机、加密上下文、流调度与拥塞控制逻辑，但不直接进行网络读写或定时器管理。

具体来说，应用需要自行完成以下工作：

1. **数据包收发**：从 UDP 套接字读取字节并交给 quiche 解析，或将 quiche 生成的待发送数据写入套接字。
2. **事件循环与定时器**：QUIC 依赖超时机制处理重传和连接生命周期，应用需根据 quiche 返回的超时时间调度定时任务。
3. **TLS 集成**：quiche 使用 BoringSSL 处理 TLS 1.3 握手，双方通过回调交换加密数据。

这种分层让 quiche 不依赖 tokio、async-std 等具体运行时，可以被同步或异步代码、单线程或多线程模型调用。其 API 围绕 `Connection` 对象展开，通过 `recv`、`send`、`stream_send`、`stream_recv` 等方法推进协议状态。

## 安装与使用

quiche 以 Rust crate 形式发布，可在 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
quiche = "0.20"
```

使用前需确保系统中已提供构建 BoringSSL 所需的工具链（如 cmake、Go 等），具体依赖随版本变化，建议参考构建文档。

以下是最小化的使用思路（伪代码，用于说明 API 调用顺序）：

```rust
// 1. 配置 quiche，指定版本、ALPN、TLS 证书等
let config = quiche::Config::new(quiche::PROTOCOL_VERSION)?;
config.load_cert_chain_from_pem_file("cert.pem")?;
config.load_priv_key_from_pem_file("key.pem")?;

// 2. 为新连接创建本地 Connection
let mut conn = quiche::accept(&scid, None, &mut local, &mut peer, &mut config)?;

// 3. 从套接字读取数据，交给 quiche 解析
let (read, _) = socket.recv_from(&mut buf)?;
let recv_info = quiche::RecvInfo { /* ... */ };
conn.recv(&mut buf[..read], recv_info)?;

// 4. 将待发送数据取出并写入套接字
while let Ok((write, send_info)) = conn.send(&mut out) {
    socket.send_to(&out[..write], send_info.to)?;
}

// 5. 根据超时时间推进定时器
if let Some(timeout) = conn.timeout() { /* 调度定时任务 */ }
```

仓库还附带命令行工具，例如 `quiche-client` 与 `quiche-server`，可参照文档编译并运行以进行端到端测试。

## 适用场景

- **为现有服务添加 HTTP/3 支持**：在自有服务器或反向代理中集成 quiche，向客户端提供 QUIC/HTTP/3 接入。
- **客户端与工具开发**：构建支持 HTTP/3 的客户端、命令行工具或调试工具，例如 curl 的 HTTP/3 支持即基于 quiche。
- **研究协议行为**：通过命令行示例与可配置参数，实验 QUIC 的拥塞控制、版本协商、连接迁移等行为。
- **跨语言封装**：借助 C 接口将 quiche 集成进非 Rust 项目，如 Android 的 DNS over HTTP/3 解析器。

## 项目亮点

- **I/O 无关设计**：不与特定异步运行时绑定，适配面广，便于嵌入既有系统。
- **生产级验证**：驱动 Cloudflare 边缘网络的 HTTP/3 支持，并用于 Android DNS 解析与 curl，经过大规模实际流量检验。
- **Rust 实现**：在性能与内存安全之间取得平衡，适合对稳定性要求较高的网络组件。
- **完整协议覆盖**：同时提供 QUIC 传输与 HTTP/3 语义，减少自行拼装协议栈的成本。

## 相关链接

- [GitHub 仓库](https://github.com/cloudflare/quiche)
- [文档（docs.quic.tech）](https://docs.quic.tech/quiche/)
- [crates.io](https://crates.io/crates/quiche)
- [docs.rs](https://docs.rs/quiche)
- [Cloudflare 博客介绍文章](https://blog.cloudflare.com/enjoy-a-slice-of-quic-and-rust/)
