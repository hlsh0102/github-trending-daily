---
tags:
  - trending
  - article
repo: tursodatabase/turso
date: 2026-06-22
language: Rust
stars_total: 20976
stars_today: 548
---
## 项目概述

Turso 是一个进程内（in-process）SQL 数据库，完全兼容 SQLite。它由 Rust 语言编写，旨在为开发者提供一种轻量级、高性能且易于嵌入的数据存储方案。Turso 解决了传统客户端-服务器数据库在小型应用、边缘计算或嵌入式场景中过于臃肿的问题，同时也弥补了 SQLite 在多线程并发和网络访问方面的不足。目标用户包括对性能敏感的全栈开发者、需要本地持久化存储的移动应用或桌面应用开发者，以及希望在边缘节点上运行数据库的云原生工程师。

## 核心功能

- **完全 SQLite 兼容**：Turso 使用与 SQLite 相同的 SQL 语法、数据类型和文件格式，现有基于 SQLite 的应用迁移成本极低，只需更改连接方式即可。
- **嵌入式运行**：作为进程内数据库，Turso 直接运行在应用进程中，无需独立的数据库服务器进程，减少了部署复杂度和资源消耗。
- **多语言支持**：提供 Rust、JavaScript（Node.js 和浏览器）、Python、Java 等多种语言的 SDK，方便在不同技术栈中集成。
- **远程访问能力**：除了本地嵌入模式，Turso 还支持通过 libsql 协议进行远程连接，允许应用从多台机器并发访问同一数据库实例，弥补了传统 SQLite 的并发局限性。
- **边缘计算优化**：针对边缘环境（如 Cloudflare Workers、Vercel Edge Functions）进行了专门优化，支持在无服务器函数中高效运行，启动时间极短。
- **高性能与低延时**：基于 Rust 的内存安全和零成本抽象特性，Turso 在查询执行、事务处理和 I/O 操作上表现出色，原生支持预编译语句和 WAL 模式。

## 技术架构

Turso 的核心基于 Rust 编写，底层数据库引擎本身是 SQLite 的一个增强分支，称为 libsql。它保留了 SQLite 最具吸引力的特性——单一文件存储、零配置和久经考验的稳定性，同时引入了多项改进：

- **并发模型**：通过引入多版本并发控制（MVCC）和细粒度的锁机制，Turso 支持多个读取器和单个写入器并发操作，提高了在并发环境下的吞吐能力。
- **网络层抽象**：将本地文件操作抽象为可插拔的存储后端和网络协议栈，使得 Turso 既可以作为本地嵌入式数据库使用，也可以暴露为一个网络服务，通过 gRPC 或自定义 TCP 协议进行访问。
- **跨平台编译**：借助 Rust 的跨平台能力，Turso 可以编译为 Linux、macOS、Windows 以及 WebAssembly 等目标平台，覆盖从服务器到浏览器的多种运行环境。
- **模块化设计**：Turso 的代码结构清晰分层，核心引擎（libsql）与网络层、客户端 SDK 分离，便于社区贡献和独立迭代。

## 安装与使用

安装 Turso 非常简单，你可以通过包管理器或源码编译获取：

**使用包管理器（示例为 npm）**：

```bash
npm install @tursodatabase/database
```

**通过 Rust 的 Cargo 安装**：

```bash
cargo install turso
```

**最小可用示例（JavaScript）**：

```javascript
import { createClient } from '@tursodatabase/database';

// 创建内存数据库（本地模式）
const client = createClient();

// 执行 SQL 查询
client.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)");
client.execute("INSERT INTO users (name) VALUES ('Alice')");
const result = client.execute("SELECT * FROM users");

console.log(result.rows);
// 输出: [ { id: 1, name: 'Alice' } ]
```

若需要使用远程连接模式，只需在 `createClient` 中传入数据库 URL 和认证令牌即可。

## 适用场景

- **本地桌面或移动应用**：需要轻量级本地数据持久化存储，且希望避免 SQLite 的并发限制时，Turso 可以作为更好的替代选择。
- **边缘计算函数**：在 Cloudflare Workers、Deno Deploy 等无服务器边缘环境中，Turso 的极短启动时间和低资源消耗使其非常适合作为临时或持久化数据存储。
- **IoT 设备与嵌入式系统**：由于 Rust 编译出的二进制文件体积小、无运行时依赖，Turso 适合部署在资源受限的物联网设备上。
- **开发与测试环境**：作为一个进程内数据库，Turso 无需安装额外服务，非常适合作为单元测试或本地开发中的数据库模拟层。

## 项目亮点

与同类项目相比，Turso 的差异化优势在于：

- **“SQLite 增强”而非替代**：Turso 并不推翻 SQLite，而是保留了其最核心的兼容性和文件格式，让开发者只需更换驱动即可升级，降低了迁移风险。
- **原生边缘兼容**：许多嵌入式数据库无法在边缘环境中运行，而 Turso 通过编译为 WebAssembly 和提供轻量级 SDK，完美适配边缘计算场景。
- **多语言一体**：其他类似项目通常只提供一种语言的 SDK，而 Turso 覆盖了主流编程语言，且各 SDK 的 API 设计一致，学习成本低。
- **活跃的开源社区**：项目在 GitHub 上拥有超过 2 万颗星，每天新增数百个 Star，贡献者活跃，问题响应迅速，持续推动功能和性能改进。

## 相关链接

- [GitHub 仓库](https://github.com/tursodatabase/turso)
- [官方文档](https://docs.turso.tech)
- [NPM 包](https://www.npmjs.com/package/@tursodatabase/database)
- [Rust Crate](https://crates.io/crates/turso)
- [Python PyPI](https://pypi.org/project/pyturso/)
- [Java Maven 中心](https://central.sonatype.com/artifact/tech.turso/turso)
