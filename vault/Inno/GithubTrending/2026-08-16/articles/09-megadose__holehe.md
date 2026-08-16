---
tags:
  - trending
  - article
repo: megadose/holehe
date: 2026-08-16
language: Python
stars_total: 13135
stars_today: 382
---
## 项目概述

holehe 是一款基于 Python 的开源 OSINT（开源情报）工具，用于检测指定邮箱地址是否在 Twitter、Instagram、Imgur 等 120 多个网站平台上注册过账号。该项目由安全研究人员 megadose 开发并维护，在 GitHub 上拥有超过 13000 颗星，是目前最受欢迎的邮箱关联账号检测工具之一。

holehe 的核心价值在于帮助安全研究人员、渗透测试人员和隐私关注者快速了解一个邮箱地址的数字足迹。它通过各平台的"忘记密码"功能来验证邮箱是否与账号关联，而不会向目标邮箱发送任何通知邮件，这使得它成为一种隐蔽且高效的信息收集工具。项目采用 GPL-3.0 许可证开源，支持命令行操作和 Python 模块嵌入两种使用方式。

## 核心功能

- **多平台检测**：支持 120 多个主流网站和服务的邮箱注册检测，涵盖社交媒体（Twitter、Instagram、Snapchat）、开发平台（GitHub、GitLab）、影音平台（YouTube、Twitch）等各类服务。

- **静默探测**：利用"忘记密码"功能进行账号存在性验证，全程不向目标邮箱发送任何邮件通知，避免打草惊蛇。

- **信息丰富输出**：不仅能判断邮箱是否注册，还能返回账号的用户名、可能的个人资料等信息（取决于各平台接口的返回数据）。

- **双模式使用**：既可作为独立命令行工具使用，也可作为 Python 库导入到自己的脚本或工具链中，方便二次开发。

- **异步高性能**：基于 trio 和 httpx 异步框架构建，能够高效并发处理多个平台的检测请求，大幅缩短整体检测时间。

- **跨平台支持**：完全使用 Python 3 编写，可在 Windows、Linux、macOS 等主流操作系统上运行，并支持 Docker 容器化部署。

## 技术架构

holehe 采用模块化插件架构设计，每个目标平台对应一个独立的检测模块。这些模块位于 `holehe/modules/` 目录下，按照平台类型进行组织，例如 `social_media/`、`dev/`、`mail/` 等子目录。

每个检测模块都是独立的异步函数，接收三个参数：目标邮箱地址、httpx 异步客户端以及输出结果列表。这种设计使得新增平台支持非常简单，只需按照模板编写相应的检测逻辑即可。模块内部通常模拟浏览器的忘记密码流程，向各平台的密码重置接口发送请求，根据响应状态码或返回内容判断邮箱是否已注册。

项目使用 trio 作为异步并发框架，结合 httpx 提供 HTTP 客户端能力。这种异步架构允许 holehe 同时向多个平台发起请求，大大提高了检测效率。同时，项目还为每个模块配置了适度的并发控制，避免对目标平台造成过大请求压力。

输出结果采用结构化格式，包含每个检测模块的结果字典，记录账号是否存在、是否返回错误、使用的 HTTP 方法等信息。这些数据既可直接打印为可读文本，也可被其他程序解析处理。

## 安装与使用

### 安装步骤

**通过 PyPI 安装（推荐）：**

```bash
pip3 install holehe
```

**通过 GitHub 源码安装：**

```bash
git clone https://github.com/megadose/holehe.git
cd holehe/
python3 setup.py install
```

**使用 Docker：**

```bash
docker build . -t my-holehe-image
docker run my-holehe-image holehe test@gmail.com
```

### 基础使用

**命令行模式：**

```bash
holehe test@gmail.com
```

该命令会检测 `test@gmail.com` 在所有支持的平台上是否注册过账号，并输出检测结果。可以使用 `--only-used` 参数只显示已注册的平台，使用 `--no-color` 禁用颜色输出。

**Python 模块调用：**

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

上述示例展示了如何在自己的 Python 项目中单独调用某个平台的检测模块，适合需要定制检测范围或集成到其他工具链的场景。

## 适用场景

- **渗透测试与红队行动**：在授权测试中，通过邮箱快速识别目标在网络上的账号资产，扩大攻击面或寻找社工攻击的切入点。

- **OSINT 信息收集**：安全研究人员利用该工具收集目标的公开数字足迹，进行人物画像、关联分析或威胁情报工作。

- **隐私审计**：普通用户可以使用 holehe 检查自己的邮箱在哪些网站上有注册记录，了解个人数据在网络上的暴露范围，及时清理不用的账号。

- **账号安全评估**：企业安全团队可用它检测员工使用公司邮箱注册的非授权服务，评估潜在的数据泄露风险。

## 项目亮点

- **不通知目标**：这是 holehe 区别于其他同类工具最显著的特点。绝大多数邮箱检测工具会向目标邮箱发送验证邮件，这很容易暴露检测行为。holehe 通过巧妙地利用密码找回功能规避了这一问题。

- **覆盖面广**：支持超过 120 个平台，且持续更新中。社区贡献机制使得新增平台支持变得简单，保持了工具的生命力。

- **双模式易集成**：既提供开箱即用的 CLI 工具，又允许作为库嵌入到其他 Python 项目中，灵活性极强。

- **异步高效**：采用现代异步 I/O 架构，而非传统的同步请求方式，检测速度快且资源占用低。

## 相关链接

- [GitHub 仓库](https://github.com/megadose/holehe)
- [在线版本](https://osint.industries/)
