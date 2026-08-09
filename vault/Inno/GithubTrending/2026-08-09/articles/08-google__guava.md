---
tags:
  - trending
  - article
repo: google/guava
date: 2026-08-09
language: Java
stars_total: 51864
stars_today: 93
---
## 项目概述

Guava 是 Google 开源的一套核心 Java 库，由 Google 内部大量项目实践沉淀而成。它提供了一系列精心设计、高效可靠的集合类型、不可变集合、图处理库，以及并发、I/O、哈希、基本类型、字符串处理等工具类。Guava 在 Google 内部绝大多数 Java 项目中被广泛使用，同时也被全球众多企业采用，是 Java 生态中最具影响力的基础库之一。

该项目主要面向 Java 开发者，尤其是那些需要处理复杂集合操作、并发编程、缓存设计等场景的工程团队。Guava 提供两种版本：JRE 版要求 JDK 1.8 或更高版本，适合标准 Java 环境；Android 版则针对 Android 平台或希望兼容 Android 的库设计。

## 核心功能

- **新集合类型**：提供 Multimap（多值映射）、Multiset（多重集合）、BiMap（双向映射）、Table（二维表）等高级集合，解决了 JDK 原生集合在特定场景下的不足。
- **不可变集合**：提供真正不可变的集合实现，保证线程安全与数据不可变性，适合作为常量或缓存数据。
- **图处理库**：内置一套完整的图结构 API，支持构建可变/不可变图、遍历、路径查找等常见图操作。
- **并发工具**：简化并发编程，提供监听器式 Future、原子值处理、限流器（RateLimiter）、 Striped 锁等高级并发原语。
- **缓存框架**：本地缓存实现，支持自动过期、逐出策略、统计信息收集，是 Caffeine 出现前的主流选择。
- **通用工具类**：涵盖字符串处理（拼接/分割/匹配）、I/O 操作（简化流与文件处理）、哈希（多种哈希函数）、基本类型转换与区间定义等日常生活常用功能。

## 技术架构

Guava 的设计核心在于对 Java 集合框架的深度扩展与优化。其集合类型采用泛型设计，注重类型安全，且在内部实现上大量利用现代 JDK 的特性（如 `java.util.function` 相关接口）来保证 API 的流畅性。不可变集合则通过拒绝变更操作的方式，规避了并发环境下的同步开销，提高了性能。

库以模块化方式组织，核心依赖极少，便于集成到各类项目中。其并发包通过自定义的抽象层，在兼容 JDK 并发工具的同时提供了更高层的语义封装。整个项目采用 Apache-2.0 许可，代码风格严格遵循 Google Java Style，经过长时间的生产环境验证，性能和稳定性均有保障。

## 安装与使用

使用 Maven 时，在 `pom.xml` 中添加如下依赖：

```xml
<dependency>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>33.6.0-jre</version>
</dependency>
```

若目标环境为 Android，则将版本号改为 `33.6.0-android`。Gradle 用户可对应添加：

```gradle
implementation 'com.google.guava:guava:33.6.0-jre'
```

以下是一个最小使用示例，演示如何利用 Guava 创建不可变集合并拼接字符串：

```java
import com.google.common.collect.ImmutableList;
import com.google.common.base.Joiner;

public class Example {
    public static void main(String[] args) {
        ImmutableList<String> list = ImmutableList.of("a", "b", "c");
        String result = Joiner.on(", ").join(list);
        System.out.println(result); // 输出 a, b, c
    }
}
```

## 适用场景

- **数据处理管线**：需要大量使用集合转换、过滤、分组操作的场景，利用 Guava 的集合工具类可显著减少样板代码。
- **并发服务开发**：需要实现请求限流、异步回调、线程安全的缓存等功能的服务器端应用，Guava 提供了成熟稳定的解决方案。
- **Android 应用开发**：需要避免受 DEX 方法数限制，同时期望获得与 Java 8+ 一致的高级集合体验的 Android 项目。
- **工具库或框架开发**：作为基础依赖，为其他库或框架提供通用的集合、字符串、I/O 能力，它自身也常被用作测试工具。

## 项目亮点

与 Apache Commons 等其他 Java 工具库相比，Guava 在 API 设计上更具现代感与连贯性，功能模块间关联紧密，学习曲线平缓。其不可变集合和高级集合类型不仅是简单的数据结构，更体现了对并发安全和代码可维护性的深思熟虑。此外，Guava 由 Google 强力维护，社区活跃，问题响应及时，代码质量与文档成熟度均处于行业顶尖水平。虽然部分功能（如缓存、图处理）已有更强替代品，但 Guava 的广度和稳定性仍使其成为 Java 项目中最值得引入的基础依赖之一。

## 相关链接

- [GitHub 仓库](https://github.com/google/guava)
- [Guava 官方 Wiki](https://github.com/google/guava/wiki)
- [Guava 发布说明](https://github.com/google/guava/releases)
