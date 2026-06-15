---
tags:
  - trending
  - article
repo: pytest-dev/pytest
date: 2026-06-15
language: Python
stars_total: 14097
stars_today: 14
---
## 项目概述

pytest 是一个成熟、功能齐全的 Python 测试框架，旨在帮助开发者轻松编写小型测试，同时能够灵活扩展以支持复杂的功能测试场景。无论你是刚接触测试的新手，还是维护大型项目的资深工程师，pytest 都能提供简洁、可读性强且功能强大的测试方案。该项目由 pytest-dev 组织维护，采用 MIT 许可证开源，在 GitHub 上已获得超过 1.4 万颗星标，是 Python 生态中最流行的测试工具之一。

pytest 的核心目标是通过减少样板代码、提供直观的断言语法以及丰富的插件机制，降低测试编写和维护的成本。它能够直接替代 `unittest` 和 `nose`，并兼容已有的测试用例。

## 核心功能

- **简洁的测试编写**：无需继承类或使用特定语法，普通 Python 函数即可作为测试用例。断言直接使用 Python 内置的 `assert` 语句，失败时自动提供详细的上下文信息（如预期值、实际值、差异对比）。
- **自动发现测试**：pytest 能够递归扫描目录，自动发现所有符合命名约定（如 `test_*.py` 或 `*_test.py` 文件，`test_` 开头的函数或类方法）的测试用例，无需额外配置。
- **强大的夹具（Fixture）系统**：通过 `@pytest.fixture` 装饰器，你可以创建可复用的测试环境（如数据库连接、临时文件、模拟对象）。夹具支持作用域（session、module、class、function）和自动请求，并能通过依赖注入机制自动传递给测试函数。
- **参数化测试**：使用 `@pytest.mark.parametrize` 可以轻松对同一个测试函数运行多组输入数据，避免编写大量重复的测试代码。支持嵌套参数化和从外部数据源（如 CSV、JSON）读取参数。
- **丰富的插件生态**：pytest 拥有数百个第三方插件，覆盖代码覆盖率（pytest-cov）、并行测试（pytest-xdist）、HTML 报告（pytest-html）、持续集成集成等场景。你可以通过 `pip install pytest-<name>` 直接安装。
- **全面的兼容性**：pytest 原生支持运行 `unittest.TestCase` 和 `nose` 风格的测试用例，无需重写已有代码。同时提供 `pytest.mark.skip`、`pytest.mark.xfail` 等标记，用于有条件跳过或预期失败的测试。

## 技术架构

pytest 采用基于钩子的插件化架构。其核心是一个事件驱动的执行引擎，通过钩子函数（hookspec）暴露生命周期中的关键节点（如测试收集、测试执行、报告生成）。所有内置功能（如 fixture、参数化、断言重写）实际上都是以插件形式实现，第三方扩展也通过同样的钩子接口集成。这种设计使得 pytest 高度模块化、可扩展，且易于定制。

技术上，pytest 利用 Python 的内省能力（元编程）来自动发现和解析测试文件，并通过 AST（抽象语法树）重写来增强 `assert` 语句，使其在失败时显示详细的表达式结果。执行过程中，pytest 采用一个中央调度器来管理测试顺序、夹具生命周期和并行运行（通过 xdist 插件）。

此外，pytest 对 Python 的 `unittest` 和 `doctest` 模块提供了内置兼容层，能够无缝运行这些框架编写的测试。

## 安装与使用

**安装**：
```bash
pip install pytest
```
或者通过 conda 安装：
```bash
conda install -c conda-forge pytest
```

**最小可用示例**：
创建一个名为 `test_sample.py` 的文件，内容如下：
```python
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

在终端中执行：
```bash
pytest
```
你将看到类似如下的输出：
```
============================= test session starts ==============================
collected 1 item

test_sample.py F                                                         [100%]

=================================== FAILURES ===================================
_________________________________ test_answer __________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:5: AssertionError
=========================== 1 failed in 0.05s ===========================
```
pytest 自动找到了测试函数，执行失败并明确指出了 `inc(3)` 返回了 4，而非期望的 5。

**带有夹具和参数化的复杂示例**：
```python
import pytest

@pytest.fixture
def input_data():
    return [1, 2, 3]

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input_data, input, expected):
    assert input_data[input-1] + 1 == expected
```

## 适用场景

- **单元测试**：对 Python 项目中的函数、类方法进行精确的独立测试。pytest 的 fixture 和 mock 机制能有效隔离测试依赖。
- **集成测试**：验证不同模块、服务或数据库之间的交互。通过 scope 为 `module` 或 `session` 的 fixture，可以搭建共享的测试环境（如临时数据库、HTTP 服务器）。
- **API 测试**：结合 `requests` 库和 pytest 的参数化功能，可以高效地编写并维护 RESTful API 的端到端测试用例。
- **持续集成/持续交付（CI/CD）**：pytest 能够生成 JUnit XML 格式的测试报告，与 Jenkins、GitLab CI、GitHub Actions 等工具无缝整合。其并行执行和代码覆盖率插件可显著提升 CI 流水线的效率。

## 项目亮点

与 Python 标准库的 `unittest` 和已停止维护的 `nose` 相比，pytest 具有以下差异化优势：

1. **零样板代码**：无需继承 `TestCase` 或编写 `self.assertEqual()` 等繁琐方法。直接使用 `assert` 即可，且错误信息更清晰。
2. **开箱即用的功能**：自动发现测试、参数化、夹具系统等都是内置功能，而 `unittest` 需要额外安装第三方库或手动实现。
3. **极致的灵活性**：插件架构使其可以适应任何测试需求——从简单的单元测试到复杂的异步测试、Web 测试或数据科学验证。
4. **社区活跃度极高**：作为 Python 测试事实上的标准，pytest 拥有庞大的用户和贡献者社区，问题响应快，文档完善，且与所有主流 Python Web 框架（Django、Flask、FastAPI）和科学计算库（NumPy、Pandas）都有集成。
5. **语言功能利用**：pytest 充分利用 Python 的元编程、装饰器和 AST 能力，实现了简洁的 API 和强大的内省功能，这是其他语言或框架难以复制的。

## 相关链接

- [GitHub 仓库](https://github.com/pytest-dev/pytest)
- [官方文档](https://docs.pytest.org/en/stable/)
- [PyPI 页面](https://pypi.org/project/pytest/)
- [插件列表](https://docs.pytest.org/en/stable/reference/plugin_list.html)
- [Discord 社区](https://discord.com/invite/pytest-dev)
