---
tags:
  - trending
  - article
repo: tursodatabase/turso
date: 2026-06-23
language: Rust
stars_total: 21616
stars_today: 540
---
## 项目概述

Turso 是一个与 SQLite 兼容的进程内 SQL 数据库，使用 Rust 语言编写。它旨在为开发者提供一个简单、快速且可嵌入的数据库解决方案，特别适合边缘计算、无服务器架构和移动应用场景。Turso 解决了传统 SQLite 在分布式环境中的局限性，通过引入轻量级复制和远程访问能力，让 SQLite 能够无缝运行在多个节点上，同时保持其低延迟、零配置的特性。目标用户包括需要数据库但不愿管理复杂基础设施的前后端开发者、边缘计算工程师以及嵌入式系统开发者。

## 核心功能

- **SQLite 兼容性**：完全兼容 SQLite 的语法和 API，支持所有标准 SQLite 操作，无需修改现有代码即可迁移。
- **进程内嵌入**：作为库直接嵌入应用程序中，零网络开销，提供极高的读取性能，适合延迟敏感的场景。
- **分布式复制**：支持通过 libSQL 分支实现多节点复制，数据可在不同地理位置的节点间同步，适用于全球分布式部署。
- **多语言绑定**：提供 Rust、JavaScript/TypeScript、Python、Java 等主流语言的客户端库，方便在不同技术栈中集成。
- **边缘友好**：优化了冷启动时间和内存占用，能够在边缘计算环境（如 Cloudflare Workers、Deno）中高效运行。
- **实时备份**：内置自动备份机制，支持按时间点恢复，保障数据安全。

## 技术架构

Turso 基于 SQLite 的 libSQL 分支构建，该分支扩展了 SQLite 的核心引擎，增加了复制、远程过程调用（RPC）和嵌入式数据库服务器功能。核心架构分为三层：

- **存储层**：使用 SQLite 的 B-tree 存储引擎，通过 libSQL 引入 WAL（预写日志）增强并发写能力，同时支持多副本的最终一致性同步。
- **网络层**：采用 Rust 的异步运行时（Tokio）实现高效的网络通信，通过自定义二进制协议支持客户端与服务器间的低延迟交互。
- **嵌入层**：提供统一的 C 语言 API，便于绑定到不同语言环境。在客户端模式下，Turso 可直接在本地运行数据库实例；在服务器模式下，它作为轻量级守护进程处理远程请求。

设计上，Turso 遵循“单进程、多线程”模型，利用 Rust 的所有权系统保证内存安全，并通过零拷贝技术减少数据序列化开销。这种架构使其在嵌入式场景下性能接近原生 SQLite，同时具备网络数据库的灵活性。

## 安装与使用

### 安装
Turso 支持多种安装方式，推荐通过包管理器或源代码编译：

```bash
# Rust 用户
cargo add turso

# Node.js 用户
npm install @tursodatabase/database

# Python 用户
pip install pyturso

# 直接下载二进制
curl -sSfL https://get.turso.org | sh
```

### 最小可用示例（JavaScript）
```javascript
import { createClient } from '@tursodatabase/database';

// 创建客户端（支持本地文件或远程数据库）
const db = createClient({
  url: 'file://mydb.db', // 本地 SQLite 文件
  // url: 'https://db.turso.io?token=xxx' // 远程 Turso 数据库
});

// 执行查询
await db.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)');
await db.execute("INSERT INTO users (name) VALUES ('Alice')");

// 读取数据
const result = await db.execute('SELECT * FROM users');
console.log(result.rows); // 输出 [{ id: 1, name: 'Alice' }]
```

### 最小可用示例（Rust）
```rust
use turso::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open("mydb.db")?;
    db.execute_batch("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")?;
    db.execute("INSERT INTO users (name) VALUES (?1)", params!["Bob"])?;
    
    let rows = db.query("SELECT * FROM users", (), |row| {
        let id: i32 = row.get(0)?;
        let name: String = row.get(1)?;
        Ok((id, name))
    })?;
    println!("{:?}", rows);
    Ok(())
}
```

## 适用场景

1. **边缘计算与无服务器函数**：在 Cloudflare Workers、AWS Lambda 等环境中作为轻量级数据库，避免冷启动延迟。
2. **移动应用与嵌入式设备**：替代传统 SQLite 的复杂配置，通过远程同步实现多设备数据共享。
3. **原型开发与内部工具**：快速搭建数据存储层，无需部署独立数据库服务。
4. **多区域分布式应用**：利用复制功能在全球范围提供低延迟数据访问。

## 项目亮点

- **零配置体验**：无需安装数据库服务器，即拿即用，降低开发门槛。
- **性能平衡**：既保留了 SQLite 的单机读取性能，又通过异步网络实现了合理的写并发能力。
- **生态兼容**：无需学习全新查询语言，直接沿用 SQLite 生态中的工具和 ORM。
- **语言丰富度**：相比其他嵌入式数据库（如 DuckDB），Turso 提供更完整的语言绑定覆盖。
- **活跃社区**：作为开源项目，拥有超过 2 万 GitHub Stars，持续获得来自 Cloudflare 等公司的贡献。

## 相关链接

- [GitHub 仓库](https://github.com/tursodatabase/turso)
- [官方文档](https://docs.turso.tech)
- [npm 包](https://www.npmjs.com/package/@tursodatabase/database)
- [Rust crate](https://crates.io/crates/turso)
