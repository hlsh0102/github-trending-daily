---
tags:
  - trending
  - article
repo: google/guava
date: 2026-08-07
language: Java
stars_total: 51660
stars_today: 13
---
## 项目概述

Guava 是 Google 官方开源的一套 Java 核心库，由 Google 内部大量项目积累的通用工具代码整理而成。它提供了一系列经过实战检验的数据结构与工具方法，极大地简化了 Java 开发中的常见任务。Guava 解决了 Java 标准库在集合类型、并发控制、字符串处理、I/O 操作等方面的不足，为开发者提供了更安全、更高效、更符合现代编程习惯的 API。该项目目标用户涵盖所有使用 Java 进行开发的工程师，无论是大型企业级应用、Android 移动开发，还是开源库的构建，Guava 都能显著提升开发效率和代码质量。目前，Guava 被 Google 内部绝大多数 Java 项目使用，同时也在大量其他公司中广泛采用，是 Java 生态中最具影响力的基础库之一。

## 核心功能

- **增强集合类型**：提供了 Multimap（一个键对应多个值的映射）、Multiset（允许重复元素的集合，可统计频次）、BiMap（双向映射）等标准库不具备的数据结构，极大丰富了集合处理的表达能力。
- **不可变集合**：提供 `ImmutableList`、`ImmutableSet`、`ImmutableMap` 等实现，保证集合在创建后不可被修改，天然支持线程安全，并能在编译期规避误修改的 bug。
- **并发工具**：封装了 `ListenableFuture`、`Service` 框架、`RateLimiter`（限流器）、`Striped`（分段锁）等高阶并发原语，简化了异步编程与多线程协作的复杂度。
- **图处理库**：自带一套完整的图（Graph）数据结构，支持可变与不可变图，涵盖有向图、无向图、网络等类型，并提供遍历、转换、子图等算法支持。
- **工具类集合**：涵盖字符与字符串处理（`Strings`）、哈希散列（`Hashing`）、原始类型处理（`Primitives`）、I/O 操作（`ByteStreams`、`CharStreams`）、异常传播与反射工具等，几乎覆盖日常开发所有基础需求。
- **缓存框架**：提供 `Cache` 接口与本地缓存实现，支持基于容量、时间或引用的过期策略，并内置统计信息，可替代简单的自研缓存逻辑。

## 技术架构

Guava 的设计遵循“成熟、稳定、高性能”的原则，其核心架构特点体现在以下几个方面：

- **分 flavor 发布**：项目针对 JRE（JDK 8+）与 Android 环境提供两种风格（flavor）的构建产物，Maven 坐标中通过版本号后缀（如 `33.6.0-jre` 与 `33.6.0-android`）区分。这使得 Android 开发者能够使用 Guava 而无需过度引入不被支持的 API。
- **无外部依赖**：Guava 除了自身的依赖（如 `failureaccess`）外，不强制依赖任何第三方库，保证了可作为底层库被任意项目平滑引入，避免了依赖冲突。
- **模块化与包结构**：代码按功能模块划分为 `collect`、`concurrent`、`graph`、`hash`、`io`、`primitives`、`reflect` 等包，职责清晰，便于开发者按需查阅与引用。
- **重视不可变性**：Guava 大量采用不可变对象设计，结合 JDK 的 `@Nullable` 注解与内置的空值检查（`Preconditions`），从类型与 API 设计层面帮助开发者规避空指针与并发修改等常见问题。
- **高效算法实现**：在集合与哈希的底层实现上，Guava 针对常见场景做了大量性能优化，例如使用开放寻址法优化 `ImmutableSet`，以及采用紧凑的内存布局减少存储开销。

## 安装与使用

要在项目中使用 Guava，只需在构建配置中添加依赖。以 Maven 为例，在 `pom.xml` 中加入：

```xml
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>33.6.0-jre</version>
</dependency>
```

如果使用 Gradle：

```groovy
implementation 'com.google.guava:guava:33.6.0-jre'
```

若项目需兼容 Android，则将版本号替换为 `33.6.0-android`。

**最小可用示例**：下面展示了使用 Guava 的不可变集合与字符串工具类的基础用法：

```java
import com.google.common.collect.ImmutableList;
import com.google.common.base.Joiner;

public class QuickStart {
    public static void main(String[] args) {
        // 创建不可变列表
        ImmutableList<String> names = ImmutableList.of("Alice", "Bob", "Charlie");
        
        // 使用 Joiner 将列表拼接为字符串
        String result = Joiner.on(", ").join(names);
        System.out.println(result);  // 输出：Alice, Bob, Charlie
    }
}
```

对于 Maven 用户，建议使用 `dependencyManagement` 配合 BOM（如 `guava-bom`）管理版本，以便统一多个模块的依赖版本。

## 适用场景

Guava 适用于几乎所有需要编写可靠、可维护 Java 代码的场景，典型的场景包括：

- **服务端业务开发**：在 Web 服务或微服务中，使用 Guava 的缓存、限流、集合与字符串处理工具，提升开发效率并减少手写工具类造成的重复代码。
- **数据处理与转换管道**：在处理日志、数据清洗或 ETL 任务时，利用不可变集合与 `Iterables` 等工具安全的传输与切分数据。
- **Android 客户端开发**：Android flavor 提供了与 Java 8 兼容的 API 子集，适合在移动端处理集合、异步任务与轻量级缓存。
- **编写开源库或框架**：由于 Guava 无重依赖且经过大规模生产验证，适合作为底层依赖嵌入到各类开源项目中，降低自身工具代码的维护负担。

## 项目亮点

- **来源 Google，久经考验**：由 Google 核心工程团队维护，内部绝大多数 Java 项目都在使用，bug 修复与更新迭代及时，稳定性由全球最大规模的 Java 应用场景背书。
- **全面的 API 覆盖**：从集合到并发，从 I/O 到反射，几乎覆盖了 Java 开发中的所有基础痛点，避免为每个项目重新发明轮子。
- **不可变与安全优先**：设计上强化不可变集合与并发安全，帮助开发者在编译阶段避免大量潜在缺陷，提升代码健壮性。
- **Android 友好**：独有的 Android flavor 使移动端开发者无需回避较新的 API 即可精准使用所需功能。
- **活跃的社区与生态**：拥有数万星标，文档详尽（包含 Wiki），问题响应及时，且被 Spring、Hadoop 等众多知名项目依赖，技术生态成熟。

## 相关链接

- [GitHub 仓库](https://github.com/google/guava)
- [Guava 官方文档与 Wiki](https://github.com/google/guava/wiki)
