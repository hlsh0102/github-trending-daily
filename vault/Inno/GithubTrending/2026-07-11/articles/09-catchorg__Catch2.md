---
tags:
  - trending
  - article
repo: catchorg/Catch2
date: 2026-07-11
language: C++
stars_total: 20629
stars_today: 76
---
## 项目概述

Catch2 是一个现代、C++ 原生、仅头文件的单元测试框架，支持 C++14、C++17 及更高版本，同时也为需要 C++11 支持的用户提供了 v2.x 分支。该项目由 Catchorg 维护，是 C++ 社区中最受欢迎的测试框架之一，在 GitHub 上拥有超过 2 万颗星标。

Catch2 主要解决 C++ 开发者编写单元测试时的痛点：测试代码应当像普通 C++ 代码一样自然易读，测试名称不必是有效标识符，断言表达式应当直接使用 C++ 布尔表达式，而无需为测试框架学习额外的领域特定语言。Catch2 的目标用户是所有需要进行 C++ 软件质量保证的开发者，从个人项目到大型企业级应用，都能从中受益。

## 核心功能

- **自然断言语法**：使用 `REQUIRE` 和 `CHECK` 宏，接受任何 C++ 布尔表达式作为断言，无需记忆大量专用断言函数
- **灵活的测试组织**：通过 `TEST_CASE` 定义测试，使用标签（如 `[factorial]`）对测试进行分类和筛选
- **共享设置/清理代码**：利用 `SECTION` 机制，在同一个测试用例中定义多个共享上下文的子测试，代码重用自然且局部化
- **内置微基准测试**：提供基本的性能基准测试功能，允许开发者在测试框架内直接进行简单性能评估
- **BDD 风格支持**：提供 `SCENARIO`、`GIVEN`、`WHEN`、`THEN` 等宏，支持行为驱动开发风格
- **丰富的测试报告格式**：支持多种输出格式，包括控制台、JUnit XML 等，方便集成到 CI/CD 流水线
- **命令行过滤器**：支持基于名称、标签、通配符等多种方式选择和排除测试用例

## 技术架构

Catch2 采用**仅头文件**（header-only）设计，这意味着开发者不需要链接额外的库文件，只需将 `catch2` 头文件目录纳入包含路径即可使用。这种设计极大简化了集成过程。

其核心架构围绕以下设计思想构建：
1. **宏驱动的测试注册**：通过预处理器宏自动收集和注册测试用例，无需手动管理测试列表
2. **表达式分解**：断言宏会将 C++ 表达式分解为左右操作数，在断言失败时提供详细的比较信息
3. **Section 堆栈**：`SECTION` 机制通过运行时栈实现，允许同一个 `TEST_CASE` 中的不同 section 共享设置代码而互不干扰
4. **完全可定制**：支持通过命令行参数和配置文件调整输出格式、测试过滤、失败处理等行为

Catch2 支持 CMake 构建系统，提供 `find_package` 集成，也可作为子项目嵌入到其他 CMake 项目中。

## 安装与使用

### 安装方式

**方式一：作为 CMake 子项目（推荐）**
```cmake
# 1. 将 Catch2 克隆到项目子目录
# 2. 在主 CMakeLists.txt 中添加
add_subdirectory(lib/catch2)
target_link_libraries(your_test_target PRIVATE Catch2::Catch2WithMain)
```

**方式二：使用包管理器**
```bash
# vcpkg
vcpkg install catch2

# Conan
conan install --requires=catch2/3.x.x
```

**方式三：单头文件直接引用**
可以从 GitHub Release 页面下载 `catch_amalgamated.hpp`，直接包含即可。

### 最小可用示例

```cpp
// tests.cpp
#define CATCH_CONFIG_MAIN  // 告诉 Catch 提供 main 函数
#include <catch2/catch_test_macros.hpp>

TEST_CASE("加法测试", "[math]") {
    REQUIRE(1 + 1 == 2);
    CHECK(2 + 2 == 4);
}
```

编译运行：
```bash
g++ -std=c++17 tests.cpp -o tests && ./tests
```

输出示例：
```
===============================================================================
All tests passed (2 assertions in 1 test case)
```

## 适用场景

- **单元测试驱动开发（TDD）**：快速编写和运行测试，验证代码行为，Catch2 的简洁语法让测试先行变得顺畅
- **持续集成/持续部署（CI/CD）**：Catch2 支持 JUnit XML 输出格式，可无缝集成到 Jenkins、GitLab CI、GitHub Actions 等平台
- **开源项目的测试基础**：许多 C++ 开源项目（如 nlohmann/json、fmtlib、spdlog）使用 Catch2 作为测试框架
- **跨平台 C++ 项目**：Catch2 支持 Windows、Linux、macOS 等主流平台，以及 MSVC、GCC、Clang 编译器

## 项目亮点

- **最低心智负担**：与 Google Test 等框架相比，Catch2 的测试代码更接近自然语言，学习曲线平缓
- **无需额外依赖**：仅头文件设计，无需编译库文件，特别适合快速原型和小型项目
- **丰富的 CI/CD 集成**：提供 GitHub Actions 徽章、AppVeyor 构建状态、Codecov 覆盖率报告等
- **活跃的社区**：拥有 Discord 服务器和官方在线编译器（Godbolt）示例，社区响应迅速
- **许可证友好**：采用 BSL-1.0 许可证，商业使用友好

## 相关链接

- [GitHub 仓库](https://github.com/catchorg/Catch2)
- [在线编译器示例](https://godbolt.org/z/EdoY15q9G)
- [Discord 社区](https://discord.gg/4CWS9zD)
- [Release 页面](https://github.com/catchorg/catch2/releases)
