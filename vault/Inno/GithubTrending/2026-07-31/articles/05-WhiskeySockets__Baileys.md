---
tags:
  - trending
  - article
repo: WhiskeySockets/Baileys
date: 2026-07-31
language: JavaScript
stars_total: 10482
stars_today: 19
---
## 项目概述

Baileys 是一个基于 WebSocket 的 TypeScript 库，用于与 WhatsApp Web API 进行交互。它为开发者提供了一套完整、类型安全且无浏览器依赖的接口，使得在 Node.js 环境中构建 WhatsApp 自动化工具、聊天机器人和集成服务成为可能。

该项目解决了开发者无法通过官方 WhatsApp Business API 轻松访问消息发送和接收功能的问题。Baileys 通过连接 WhatsApp Web 的底层协议，实现了与官方 Web 客户端等效的功能，而无需使用 Selenium 等重型浏览器自动化工具。它的目标用户是希望在 JavaScript/TypeScript 生态中高效开发 WhatsApp 相关功能的开发者，从个人项目爱好者到企业级服务提供商。

## 核心功能

- **完整消息收发**：支持发送和接收文本、媒体（图片、视频、音频、文档）、位置、联系人、贴纸等多种消息类型，并对接收到的消息进行结构化解析。
- **群组与广播管理**：支持创建群组、添加/移除成员、修改群设置（如群名、头像、描述），并支持向广播列表发送消息。同时可管理群内管理员权限。
- **多设备支持**：基于 WhatsApp 最新的多设备协议，Baileys 允许跨多个设备同时使用 WhatsApp，并将自己的会话作为多设备中的一个节点。每个设备都有独立的凭据。
- **会话管理与状态同步**：提供强大的会话管理机制，包括配对码或二维码的扫码登录，以及会话的持久化存储，方便恢复登录状态。它能够同步联系人、已读回执、在线状态和打字状态等实时事件。
- **消息历史记录**：可以获取Chat历史记录，包括旧消息、已编辑消息和已删除消息，为数据迁移提供可能。
- **类型安全与高可定制性**：整个库使用 TypeScript 编写，提供了完整的类型定义，增强了开发体验和代码健壮性。同时，底层的 Socket 连接和事件发射器架构允许开发者对消息处理流程进行深度定制。

## 技术架构

Baileys 基于 WebSocket 协议实现与 WhatsApp Web 服务器的通信。其架构核心是一个简洁的传输层，它模拟了 WhatsApp Web 浏览器的网络行为。

技术上，该库大量使用了 JavaScript 的异步特性，如 Promise 和 Async/Await，来处理高并发的消息交互。它将 WhatsApp 的二进制编码协议转换为了友好的 JSON 对象，屏蔽了底层协议复杂性。库的内部主要由以下几个核心部分构成：

- **Socket 层**：负责 WebSocket 连接的建立、心跳检测、连接中断后的自动重连（可配置）。
- **Session 管理**：负责会话凭据（Credentials）的生成、验证和刷新，并支持将凭据持久化到本地存储（如文件、Redis），以便服务重启后再次使用。
- **消息处理引擎**：负责接收 WebSocket 推送的原始数据，对其进行解码、解密（涉及消息加密层）和解析，最终转换为结构化的消息对象，通过事件（Events）触发给上层应用。
- **发送队列**：为了保证消息有序不丢包，库内部实现了发送队列机制，对发送请求进行序列化处理。

该库的架构设计着重于模块化和可扩展性，开发者可以实例化不同的组件，并为其提供特定的实现（例如自定义的日志器、存储代理等）。

## 安装与使用

安装 Baileys 非常简单，可以通过 npm 或 yarn 进行：

```bash
npm install baileys
# 或者
yarn add baileys
```

**最小可用示例（连接并监听消息）：**

```javascript
import makeWASocket, { useMultiFileAuthState } from 'baileys'

async function connectToWhatsApp() {
  const { state, saveCreds } = await useMultiFileAuthState('auth_info')
  const sock = makeWASocket({
    printQRInTerminal: true,
    auth: state
  })

  sock.ev.on('connection.update', (update) => {
    const { connection, lastDisconnect } = update
    if (connection === 'close') {
      // 重连策略
      console.log('连接断开，尝试重连')
      connectToWhatsApp()
    } else if (connection === 'open') {
      console.log('连接成功！')
    }
  })

  sock.ev.on('creds.update', saveCreds)
  sock.ev.on('messages.upsert', async (m) => {
    console.log('收到消息', m.messages[0])
    // 自动回复 '嗨'
    if (m.messages[0].key.remoteJid === 'user@whatsapp.net') {
      await sock.sendMessage(m.messages[0].key.remoteJid, { text: 'Hi!' })
    }
  })
}

connectToWhatsApp()
```

在代码中，你需要提供自己的 WhatsApp 号码进行扫码或配对，库会将登录状态保存到 `auth_info` 文件夹中，以便后续复用。

## 适用场景

- **个人自动化助理**：搭建个人专属的 WhatsApp 助手，用于自动回复、日程提醒、天气预报查询，甚至结合 OpenAI API 构建私有的 AI 聊天机器人。
- **客户服务与支持**：企业可以使用 Baileys 构建基于 WhatsApp 的客服系统，例如自动回答常见问题、为用户分配人工客服、发送订单状态通知。
- **消息群发与营销工具**：构建营销工具，向目标客户群推送促销信息、验证码或者重要通知（需注意 WhatsApp 官方政策对非用户主动消息的限制）。
- **社区管理与运营**：用于管理大型 WhatsApp 社区群组，实现自动欢迎消息、入群验证、关键词过滤，以及对群内内容进行监控和数据统计。

## 项目亮点

- **纯协议实现，不依赖浏览器**：与基于 Puppeteer 的方案不同，Baileys 直接通过 WebSocket 与 WhatsApp 服务器通信，因此在并发量、资源占用和运行速度上都远优于浏览器自动化方案，非常适合大规模或服务器端部署。
- **TypeScript 原生支持**：提供了全面的类型定义，有效减少了运行时错误，让代码更易于维护和重构，这对大型项目尤其重要。
- **活跃的社区与持续迭代**：项目在 GitHub 上拥有超过一万颗星，社区活跃，能快速响应 WhatsApp Web 协议的变更，并提供及时的修复和新功能支持。
- **多设备协议的前沿支持**：Baileys 对 WhatsApp 多设备功能的支持，使其能以一个真实设备节点的身份融入用户的 WhatsApp 生态，而不仅仅是模拟一个额外的客户端。

## 相关链接

- [GitHub 仓库](https://github.com/WhiskeySockets/Baileys)
- [使用文档](https://baileys.wiki)
- [Discord 社区](https://whiskey.so/discord)
