---
tags:
  - trending
  - article
repo: Wei-Shaw/sub2api
date: 2026-08-23
language: Go
stars_total: 38819
stars_today: 278
---
## 项目概述

Sub2API 是一个开源的 AI API 网关平台，核心功能是将 Anthropic Claude、OpenAI、Google Gemini 以及 Grok 等主流大模型平台的订阅额度进行统一管理和二次分发。简单来说，它允许你购买一个官方订阅（如 Claude Pro），然后通过 Sub2API 将这份订阅额度转换成标准的 API 接口，供多个用户或多个应用共享使用。

这个项目解决的核心痛点是：官方 API 按量计费的成本高昂，而个人订阅虽然价格相对低廉，却只能通过官方网页或特定客户端使用，无法直接调用 API。Sub2API 打破了这一限制，让订阅额度以 API 形式流动起来，同时支持“拼车”模式，让多人分摊一个订阅的成本，极大降低了使用顶尖大模型 API 的经济门槛。

项目目标用户包括：需要高频调用大模型 API 的开发者、独立开发者、小型创业团队、AI 应用爱好者，以及希望以更低成本体验多种模型能力的个人用户。

## 核心功能

- **多平台协议接入**：无缝兼容 Anthropic、OpenAI、Gemini 和 Grok 四大主流模型的官方 API 协议，只需切换 Base URL 即可使用对应模型。
- **订阅额度池化管理**：将上游订阅账号汇聚为统一的额度池，通过 API Key 对下游用户进行分组、限速和配额管理。
- **跨模型路由**：支持通过单一网关请求不同提供商的模型，提供统一接口，简化多模型应用的集成复杂度。
- **用户与用量管理**：提供管理面板，支持创建多个下游用户、查看各用户用量、设置访问权限和速率限制。
- **Docker 一键部署**：内置完整的 Docker Compose 编排，一条命令即可拉起网关、数据库和缓存等全部依赖。
- **高性能网关**：基于 Go 语言实现，具备高并发处理能力和低延迟转发性能，适合生产级使用。

## 技术架构

Sub2API 采用现代化的前后端分离架构。后端基于 **Go** 语言构建，利用其出色的并发模型和高效的网络 I/O，实现高性能的 API 请求转发与配额计量。前端则采用 **Vue.js** 构建管理控制台，提供直观的用户界面用于管理订阅、用户和查看统计信息。

数据持久化上，项目使用 **PostgreSQL** 作为主数据库，存储用户、订阅、用量记录等核心业务数据；使用 **Redis** 作为缓存层和限流组件，保障高频请求下网关的响应速度和稳定性。项目对数据库和缓存均采用强制初始化策略（在启动时自动执行），若配置错误则直接拒绝启动，避免运行期出现不一致状态。

在部署层面，项目全面拥抱容器化，提供 Dockerfile 和 Docker Compose 配置，将 Go 后端、Vue 前端、PostgreSQL 和 Redis 封装为相互连接的容器服务组，开发者可快速在任意支持 Docker 的环境（如 VPS、NAS）中完成搭建。

网关协议设计上，Sub2API 采用适配器模式，为每个上游提供商（Anthropic、OpenAI 等）实现独立的协议转换层，对外暴露统一的 OpenAI 风格 API 格式，降低下游应用的接入复杂度。

## 安装与使用

**前提要求**：需要一台可访问互联网的服务器（Linux/macOS），安装 Docker 和 Docker Compose。

**第一步：克隆仓库**

```bash
git clone https://github.com/Wei-Shaw/sub2api.git
cd sub2api
```

**第二步：配置环境变量**

复制 `.env.example` 为 `.env`，填写必要的配置项：

```bash
cp .env.example .env
```

编辑 `.env` 文件，至少需要配置数据库连接信息、Redis 连接信息，以及管理后台的初始用户名密码。

**第三步：启动服务**

```bash
docker-compose up -d
```

等待所有容器启动完成后，访问 `http://your-server-ip:3000` 即可打开管理面板。

**第四步：添加订阅并创建 API Key**

> 以下步骤需要自行在管理面板中操作（具体菜单选项以实际版本为准）：

1. 登录管理面板，进入“订阅管理”，添加你已购买的 Claude/OpenAI 等订阅账号凭证。
2. 进入“用户管理”，创建一个下游用户，并生成专属的 API Key。
3. 将生成的 API Key 和网关地址（`http://your-server-ip:3000`）作为 Base URL 提供给下游用户。

**最小示例（使用 OpenAI SDK）：**

以 Python 为例，将官方 SDK 的 `base_url` 指向 Sub2API 网关：

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxx-your-sub2api-key",
    base_url="http://your-server-ip:3000"
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",  # 使用上游支持的模型名称
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

## 适用场景

- **团队拼车共享**：几个开发者或朋友共同购买一个 Claude Pro 或 ChatGPT Plus 订阅，通过 Sub2API 搭建内网共享网关，按需分配额度，成本立减数倍。
- **多模型应用开发**：AI 应用需要同时调用 Claude、GPT-4 等多种模型，Sub2API 统一了接口，修改模型名即可切换，无需维护多个 SDK 和密钥。
- **个人自动化工作流**：开发者想在自己的脚本、博客、或 IDE 插件中使用订阅账号的能力，但不想支付昂贵 API 费用，Sub2API 可作为个人 API 代理使用。
- **学习与二次开发**：作为学习 API 网关设计、Go 后端开发、配额管理系统的优秀开源参考项目。

## 项目亮点

- **成本优势显著**：相比直接购买官方 API，通过订阅共享可节省 80%–90% 的费用，尤其适合高频、大批量请求场景。
- **多协议融合**：业内少见地同时兼容 Anthropic、OpenAI、Gemini 和 Grok 四家协议，一个网关覆盖主流模型，避免多系统并存维护的麻烦。
- **开源可审计**：完全开源且采用 LGPL-3.0 协议，代码透明，开发者可自由审计其配额计算、密钥管理逻辑，无闭源黑盒风险。
- **社区热度验证**：GitHub 上已获得超过 38,000 颗星，社区活跃，持续迭代速度快，生态和文档相对完善。

## 相关链接

- [GitHub 仓库](https://github.com/Wei-Shaw/sub2api)
- [项目趋势页面](https://trendshift.io/repositories/21823)

> 注意：使用本项目可能违反上游提供商的服务条款（ToS），请务必审阅相关条款并自行承担使用风险。项目仅供技术学习与研究使用。
