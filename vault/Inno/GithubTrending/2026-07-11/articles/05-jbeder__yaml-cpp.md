---
tags:
  - trending
  - article
repo: jbeder/yaml-cpp
date: 2026-07-11
language: C++
stars_total: 6095
stars_today: 69
---
## 项目概述

yaml-cpp 是一个用 C++ 编写的 YAML 解析器和发射器（emitter），严格遵循 YAML 1.2 规范。该项目旨在为 C++ 开发者提供一个高效、易用的 YAML 序列化与反序列化工具，解决在 C++ 应用中处理配置文件、数据交换格式等场景下对 YAML 的支持需求。目标用户包括 C++ 后端开发者、游戏引擎工程师、嵌入式系统开发者以及任何需要在 C++ 项目中处理 YAML 数据的程序员。

## 核心功能

- **完整的 YAML 1.2 支持**：完全兼容 YAML 1.2 规范，能够正确解析包括标量、序列、映射、锚点、标签等所有 YAML 数据类型。
- **双向解析与发射**：既支持将 YAML 文本解析为 C++ 数据结构（Parser），也支持将 C++ 数据结构序列化为 YAML 文本（Emitter）。
- **易用的 C++ 接口**：提供类似 STL 容器的 API，支持迭代器、下标操作和类型转换，降低学习成本。
- **跨平台构建**：基于 CMake 构建系统，支持 Windows、macOS、Linux 等主流操作系统以及多种编译器。
- **灵活的构建选项**：支持编译为静态库或共享库，可根据项目需求选择。
- **完善的错误处理**：解析过程中能够提供明确的错误信息，帮助开发者快速定位问题。

## 技术架构

yaml-cpp 采用模块化设计，核心架构包含以下几个关键部分：

- **词法分析器（Scanner）**：将原始 YAML 文本分解为 Token 流，处理缩进、注释和行结构。
- **解析器（Parser）**：根据 Token 流构建 YAML 节点树，支持流式解析和文档边界处理。
- **节点系统（Node）**：使用树形结构表示 YAML 数据，每个节点可以是标量、序列或映射。节点类型通过 `YAML::NodeType` 枚举标识。
- **发射器（Emitter）**：将节点树反向转换为格式化的 YAML 文本，支持缩进控制、样式选择（块/流）等格式化选项。
- **类型转换系统**：通过模板特化实现 C++ 原生类型（`int`、`string`、`vector`、`map` 等）与 YAML 节点的无缝互转。

设计上，yaml-cpp 采用 RAII 资源管理，无需手动释放内存。解析和发射均支持异常安全，在错误时抛出 `YAML::Exception` 子类异常。项目遵循现代 C++ 标准（C++11/14），并保持向后兼容性。

## 安装与使用

### 安装步骤

1. **克隆仓库**：
   ```bash
   git clone https://github.com/jbeder/yaml-cpp.git
   cd yaml-cpp
   ```

2. **构建与安装**：
   ```bash
   mkdir build && cd build
   cmake -DYAML_BUILD_SHARED_LIBS=ON ..
   make
   sudo make install
   ```
   如需静态库，将 `-DYAML_BUILD_SHARED_LIBS=ON` 替换为 `-DYAML_BUILD_SHARED_LIBS=OFF`（默认）。

3. **集成到项目**：
   在 `CMakeLists.txt` 中添加：
   ```cmake
   find_package(yaml-cpp REQUIRED)
   target_link_libraries(your_target yaml-cpp::yaml-cpp)
   ```

### 最小可用示例

**解析 YAML 文件**：
```cpp
#include <yaml-cpp/yaml.h>
#include <iostream>

int main() {
    YAML::Node config = YAML::LoadFile("config.yaml");
    std::cout << "name: " << config["name"].as<std::string>() << std::endl;
    std::cout << "version: " << config["version"].as<int>() << std::endl;
    return 0;
}
```

**发射 YAML**：
```cpp
#include <yaml-cpp/yaml.h>
#include <iostream>

int main() {
    YAML::Emitter out;
    out << YAML::BeginMap;
    out << YAML::Key << "name" << YAML::Value << "myapp";
    out << YAML::Key << "version" << YAML::Value << 2;
    out << YAML::EndMap;
    std::cout << out.c_str() << std::endl;
    return 0;
}
```

## 适用场景

- **配置文件解析**：游戏引擎、服务器应用等使用 YAML 作为配置文件格式时，可快速读取和修改配置。
- **数据序列化**：在 C++ 程序中需要保存或传输结构化数据（如游戏存档、分析报告）时，将其序列化为 YAML 格式。
- **国际化与本地化**：处理多语言资源文件（如 YAML 格式的翻译表），支持 Unicode 编码。
- **测试数据生成**：测试框架中使用 YAML 描述测试用例的输入和期望输出，提高可读性和可维护性。

## 项目亮点

- **规范完全兼容**：相比于部分只支持 YAML 1.0/1.1 的库，yaml-cpp 完整实现 YAML 1.2 规范，确保与最新标准的一致性。
- **API 设计优雅**：采用 C++ 惯用设计，运算符重载和模板推导让代码简洁直观，无需繁琐的标记化操作。
- **活跃维护**：GitHub 上超过 6000 星，长期保持更新，社区活跃，问题响应及时。
- **性能优异**：使用基于流的解析器，内存占用可控，解析速度满足大多数生产环境需求。
- **无外部依赖**：纯 C++ 实现，无需额外运行时库，集成简单。

## 相关链接

- [GitHub 仓库](https://github.com/jbeder/yaml-cpp)
- [使用教程](https://github.com/jbeder/yaml-cpp/wiki/Tutorial)
- [如何发射 YAML](https://github.com/jbeder/yaml-cpp/wiki/How-To-Emit-YAML)
- [API 文档](https://codedocs.xyz/jbeder/yaml-cpp/)
