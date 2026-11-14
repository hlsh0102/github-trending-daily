---
tags:
  - trending
  - article
repo: tailscale/tailcat
date: 2026-11-14
language: Go
stars_total: 9605
stars_today: 256
---
Tailcat 是 Tailscale 开源组件的一个重混项目，旨在提供类似 netcat 的功能，但使用 Tailscale 的数据平面（magicsock）进行点对点加密通信，而不依赖 Tailscale 的控制平面。它通过 WireGuard 加密隧道实现端到端安全传输，并利用 DERP 服务器进行 NAT 穿透和兜底中继。该工具适用于需要快速建立加密连接但不想使用完整 Tailscale 服务的开发者，可通过命令行或 Go 库使用，且无需 Tailscale 账户或 root 权限。
