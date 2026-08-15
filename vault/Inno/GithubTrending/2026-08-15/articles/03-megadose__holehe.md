---
tags:
  - trending
  - article
repo: megadose/holehe
date: 2026-08-15
language: Python
stars_total: 12873
stars_today: 427
---
## 项目概述

holehe 是一款基于 Python 的开源 OSINT（开源情报）工具，旨在通过电子邮件地址快速检测其在各类网站平台上的注册情况。它利用各网站的“忘记密码”功能，在不触发邮件通知的前提下，判断目标邮箱是否关联了 Twitter、Instagram、Imgur 等超过 120 个主流网站的账户。该项目主要面向安全研究人员、渗透测试人员、隐私保护倡导者以及需要进行账户关联分析的调查人员，帮助用户高效发现电子邮件与在线身份之间的隐藏联系。

## 核心功能

- **跨平台账户检测**：支持 120+ 网站的邮箱注册状态查询，覆盖社交媒体、论坛、电商、云服务等主流平台。
- **无痕探测机制**：通过模拟密码找回流程判断账户存在性，全程不向目标邮箱发送任何验证邮件，避免惊动被调查对象。
- **多引擎支持**：内置异步请求引擎，基于 `trio` 和 `httpx` 实现并发查询，大幅提升批量检测效率。
- **灵活的模块化设计**：每个网站对应独立的检查模块，用户可自定义集成，仅调用所需站点的探测逻辑。
- **双模式操作**：既提供命令行工具（CLI）供直接使用，也开放 Python API 便于嵌入其他安全工具链。
- **零依赖部署**：支持 PyPI 安装、GitHub 源码安装及 Docker 容器化运行，适配各类使用环境。

## 技术架构

holehe 采用模块化异步架构，核心基于 Python 3.7+，利用 `trio` 作为并发原语，配合 `httpx` 异步 HTTP 客户端实现高效的网络请求管理。每个目标网站被封装为独立的 Python 模块（例如 `holehe/modules/social_media/snapchat.py`），模块内部实现具体网站的探测逻辑，包括构造密码重置请求、解析响应或错误信息，从而判断邮箱是否注册。所有模块统一通过 `email`、`client`、`out` 三个参数进行交互，便于统一调度和结果收集。

项目设计上强调可扩展性与最小化副作用：由于不依赖浏览器自动化，仅通过构造标准 HTTP 请求模拟“忘记密码”流程，因此既避免了触发反爬机制，也确保了隐私安全性。查询结果以结构化数据形式输出，支持标准输出、JSON 或自定义回调，方便与其他 OSINT 工具链集成。此外，项目刻意避免任何数据库依赖，保持轻量级特性，使用户可以快速部署于临时分析环境。

## 安装与使用

### 安装方式

推荐使用 PyPI 安装：

```bash
pip3 install holehe
```

或从 GitHub 源码安装：

```bash
git clone https://github.com/megadose/holehe.git
cd holehe/
python3 setup.py install
```

Docker 用户可使用：

```bash
docker build . -t my-holehe-image
docker run my-holehe-image holehe test@gmail.com
```

### 最小可用示例

CLI 直接查询单个邮箱：

```bash
holehe test@gmail.com
```

Python 内嵌调用（以 Snapchat 为例）：

```python
import trio
import httpx

from holehe.modules.social_media.snapchat import snapchat

async def main():
    email = "test@gmail.com"
    out = []
    client = httpx.AsyncClient()

    await snapchat(email, client, out)

    print(out)
    await client.aclose()

trio.run(main)
```

### 输出说明

查询结果将列出每个网站（如 `snapchat`、`twitter`），并标记 `exists`（是否注册）、`emailrecovery`（是否泄露恢复邮箱）等状态，同时允许输出为 JSON 以便程序化处理。

## 适用场景

- **安全审计与红队侦察**：在授权渗透测试中，安全人员可利用 holehe 快速映射目标邮箱的在线足迹，为后续社工或钓鱼攻击提供情报基础。
- **个人隐私排查**：普通用户可通过查询自己的邮箱，发现哪些平台保存了个人数据，从而及时清理不用的账户、降低信息泄露风险。
- **威胁情报关联**：调查人员通过交叉比对多个邮箱的注册信息，可追踪同一实体在不同平台的活动痕迹，辅助构建数字身份图谱。
- **账户恢复与验证**：在账户找回或认证流程中，运维人员可借助该工具验证邮箱归属，防止恶意绑定。

## 项目亮点

- **真正的无痕探测**：许多同类工具（如 `email-hunter`、`hunter.io`）在验证时可能触发目标邮箱的提醒邮件，而 holehe 通过模拟“忘记密码”流程（而非发送确认邮件）实现了完全静默，这一特性在敏感调查中尤为关键。
- **海量站点覆盖与持续更新**：内置 120+ 模块且社区活跃，新站点支持不断加入，覆盖面远超多数商业 API 服务。
- **轻量且易于集成**：无浏览器依赖、无数据库负担，异步并发设计使其性能优于串行请求，且提供干净的 Python API，可快速嵌入现有安全工具。
- **开源透明**：采用 GPL-3.0 许可，所有探测逻辑完全公开，用户可审计代码、定制模块，避免使用闭源服务带来的不可信风险。

## 相关链接

- [GitHub 仓库](https://github.com/megadose/holehe)
- [在线版本（Holehe Online）](https://osint.industries/)
