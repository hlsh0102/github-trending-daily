---
tags:
  - trending
  - article
repo: 3b1b/manim
date: 2026-09-02
language: Python
stars_total: 92695
stars_today: 86
---
## 项目概述

Manim（Mathematical Animation Engine）是一个用于创建精确编程动画的引擎，专为制作解说式数学视频而设计。该项目最初是 3Blue1Brown（3b1b）频道作者 Grant Sanderson 的个人项目，用于制作该频道广受欢迎的教学视频。通过编写 Python 代码，用户可以定义数学对象、变换和动画序列，从而生成高质量的视频内容。

Manim 的目标用户是数学教育者、视频创作者、数据可视化爱好者以及任何希望通过动态视觉方式解释复杂数学概念的人。它解决了传统数学教学中静态图表难以展示动态过程的问题，使抽象概念（如微积分中的极限、线性代数中的向量变换）变得直观可见。目前该仓库在 GitHub 上拥有超过 92,000 颗星，是数学可视化领域最具影响力的开源项目之一。

值得注意的是，Manim 存在两个主要版本：本仓库所代表的 ManimGL（原版）和 2020 年由社区开发者分叉出的 Manim Community Edition。社区版更注重稳定性、测试覆盖和社区协作，而本仓库则更贴近 3Blue1Brown 视频制作的实际需求。

## 核心功能

- **精确的数学对象渲染**：支持 LaTeX 公式、几何图形、坐标轴、函数图像等数学对象的编程化定义和渲染
- **声明式动画系统**：通过 `self.play()` 等简单调用，即可实现对象移动、缩放、旋转、颜色变化等复杂过渡效果
- **基于场景的编程模型**：每个视频片段对应一个 `Scene` 类，支持场景间的平滑过渡、暂停和切换
- **实时预览与视频输出**：既可实时预览动画效果，也能输出高质量的视频文件（支持 4K 分辨率）
- **丰富的几何与数学工具**：内置向量运算、矩阵变换、复数操作、微积分可视化等数学辅助函数
- **灵活的摄像机控制**：支持多相机视角、空间移动、缩放跟随，以及“帧内”动画效果（如部分遮盖、闪烁高亮）

## 技术架构

Manim 构建于 Python 3 之上，核心架构采用“场景（Scene）- 对象（Mobject）- 动画（Animation）”的三层设计。其中，`Mobject`（数学对象）是一切可视化元素的基类，通过继承和组合可以构建复杂的图像结构；`Scene` 负责管理时间线和对象生命周期；`Animation` 则封装了插值算法，负责计算对象属性在时间轴上的变化。

底层渲染方面，Manim 依赖 **Cairo**（2D 矢量图形库）或 **OpenGL**（3D 加速渲染），其中 OpenGL 模式（ManimGL）提供更快的渲染速度和更流畅的交互体验。LaTeX 排版功能通过系统安装的 TeX 发行版实现，确保公式输出的专业性。所有对象位置和运动轨迹均基于浮点数坐标计算，支持任意精细度的动画插值。

设计上，Manim 强调“代码即视频”——视频制作完全由 Python 脚本驱动，抛弃了传统逐帧编辑方式。这种声明式编程模型虽然需要一定的编程基础，但换来的是极高的可重复性和版本控制便利性。代码结构的模块化也使得扩展新对象类型或动画效果十分容易。

## 安装与使用

> **重要提示**：以下安装说明仅适用于 ManimGL（本仓库版本）。若需安装社区版（manim），请查阅 [Manim Community](https://github.com/ManimCommunity/manim) 的文档，两种版本的安装步骤差异较大，混用可能导致环境冲突。

**系统要求**：
- Python 3.7 或更高版本
- 安装有 TeX 发行版（推荐 TeX Live 或 MiKTeX）
- FFmpeg（用于视频编码）
- 可选：Pango 和 LaTeX 依赖库

**安装步骤**（以 pip 为例）：

```bash
# 安装 ManimGL
pip install manimgl

# 可选：安装开发版本（从源码安装）
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
```

**最小可用示例**：创建一个名为 `demo.py` 的文件，内容如下：

```python
from manimlib import *

class BasicScene(Scene):
    def construct(self):
        # 创建文本对象
        title = Text("Hello, Manim!")
        formula = Tex("e^{i\\pi} + 1 = 0")
        
        # 显示标题并等待
        self.play(Write(title))
        self.wait(1)
        
        # 替换为公式并等待
        self.play(Transform(title, formula))
        self.wait(2)
```

在终端运行：

```bash
manimgl demo.py BasicScene
```

该命令会启动交互式窗口并播放动画。如需直接输出视频文件，可加入 `-w` 标志（写入文件）和 `-o` 指定输出文件名。更多命令行选项（如分辨率、帧率）可通过 `manimgl --help` 查看。

## 适用场景

- **数学教育视频制作**：从初等数论到高等数学，快速生成用于课堂或在线课程的动态演示动画
- **科普内容创作**：适合科技类自媒体创作者制作 3Blue1Brown 风格的深度解析视频
- **科研论文辅助说明**：在学术报告中可视化复杂定理证明过程或数据动态变化
- **算法可视化**：将排序算法、图遍历等计算过程转化为直观动画，便于教学和演讲

## 项目亮点

- **原版血统**：作为 3Blue1Brown 视频的官方制作工具，Manim 在数学表达精确性上经过大量实际视频的极端检验
- **极致的视觉表现力**：对 LaTeX 公式、矢量图、渐变色彩的支持堪称教科书级，可营造沉浸式数学体验
- **高度可编程性**：相比 Powerpoint 等工具的动画功能，Manim 允许用 Python 完全控制对象属性，支持复杂逻辑和条件渲染
- **活跃的生态与灵感库**：虽然目前社区版更活跃，但本仓库仍持续更新，且大量知名数学动画项目（如 3Blue1Brown 视频合集）基于此版本构建，提供了丰富的学习资源和灵感

## 相关链接

- [GitHub 仓库](https://github.com/3b1b/manim)
- [项目主页与文档](https://3b1b.github.io/manim/)
- [社区版仓库](https://github.com/ManimCommunity/manim)
- [Python 包页面](https://pypi.org/project/manimgl/)
- [Reddit 社区](https://www.reddit.com/r/manim/)
- [Discord 讨论组](https://discord.com/invite/bYCyhM9Kz2)
