---
tags:
  - trending
  - article
repo: cloudflare/quiche
date: 2026-09-22
language: Rust
stars_total: 12434
stars_today: 32
---
quiche 是 Cloudflare 开源的 QUIC 传输协议和 HTTP/3 的 Rust 实现，遵循 IETF 标准。它提供处理 QUIC 数据包和管理连接状态的底层 API，应用程序需自行负责 I/O（如套接字处理）以及支持定时器的事件循环。该项目适用于需要在应用中集成 QUIC 或 HTTP/3 支持的开发者，已被 Cloudflare 边缘网络、Android DNS 解析器和 curl 等项目采用。
