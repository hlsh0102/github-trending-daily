---
tags:
  - trending
  - article
repo: opengeos/GeoLibre
date: 2026-07-30
language: TypeScript
stars_total: 4191
stars_today: 671
---
## 项目概述

GeoLibre 是一个免费开源、轻量级、云原生的地理信息系统（GIS）平台，用于可视化、探索和分析地理空间数据。它几乎可以在任何环境中运行——不论是在浏览器、桌面、移动端还是 Jupyter Notebook 中——同时始终保证用户数据仅存储在本地，无需上传到任何服务器。该项目由 opengeos 组织维护，基于 TypeScript 开发，采用 MIT 许可证发布。

GeoLibre 致力于解决传统 GIS 软件对专业环境依赖强、安装配置复杂、数据有泄露风险等问题。目标用户包括地理信息从业者、数据科学家、教育工作者、开发者以及所有有地理空间数据浏览与分析需求的普通用户。

## 核心功能

- **跨平台运行**：同一代码库可构建为原生桌面应用（Windows/macOS/Linux）、原生 Android 应用、Web 应用，并自适应手机等小屏幕设备。
- **本地隐私优先**：所有数据均在用户设备上处理，无需将数据上传至任何第三方服务器，保障数据安全与隐私。
- **可视化与分析**：基于 MapLibre GL JS 和 deck.gl 提供高性能的二维和三维地理空间可视化能力，支持交互式探索与基础分析操作。
- **插件扩展系统**：提供插件市场（plugins.geolibre.app），支持社区贡献功能扩展，用户可按需安装插件增强平台能力。
- **Jupyter 集成**：提供 Python 包（geolibre），可在 Jupyter Notebook 和 Google Colab 中直接使用 GeoLibre 的功能，方便数据科学工作流。
- **多格式数据支持**：通过 DuckDB-WASM Spatial 提供本地端空间数据查询能力，支持常见地理空间数据格式的加载与处理。

## 技术架构

GeoLibre 采用模块化的技术栈构建：

- **桌面端**：使用 **Tauri v2** 作为桌面应用框架，将 Web 前端与系统原生能力结合，使得应用体积小、启动快、安全性高。Android 端则使用 WebView 封装相同的前端应用。
- **前端**：基于 **React** 和 **TypeScript** 构建，组件化架构使得代码可维护性强，且易于在不同平台间复用。
- **地图引擎**：使用 **MapLibre GL JS** 提供高性能的矢量/栅格地图渲染，支持 Mapbox Style 规范，兼容主流底图与样式。
- **数据层**：集成 **DuckDB-WASM Spatial**，在浏览器中直接运行空间 SQL 查询，无需后端服务；配合 **deck.gl** 实现大规模点、线、面数据的 WebGL 可视化。
- **打包与分发**：单一代码仓库通过不同构建配置分别编译出浏览器版本、桌面安装包以及移动端应用，最大化代码复用率。

## 安装与使用

**Web 端（无需安装）：**

直接访问 [https://web.geolibre.app/](https://web.geolibre.app/) 即可启动完整应用，所有功能均在浏览器内运行。

**桌面端：**

从 [https://geolibre.app/downloads/](https://geolibre.app/downloads/) 下载对应操作系统的安装包，按提示安装即可。Windows 用户也可以从 Microsoft Store 获取。

**移动端：**

Android 用户可以从 Google Play 商店安装。

**Python 包（Jupyter 集成）：**

可通过 pip 或 conda 安装：

```bash
pip install geolibre
# 或
conda install -c conda-forge geolibre
```

安装后在 Jupyter Notebook 中导入即可使用：

```python
import geolibre
geolibre.show()  # 在 notebook 中嵌入地图界面
```

更多示例可参考 [Google Colab 笔记本](https://colab.research.google.com/github/opengeos/GeoLibre/blob/main/python/examples/getting-started.ipynb)。

## 适用场景

- **教学与科研**：教师或研究人员可以快速搭建地理空间数据可视化环境，无需学生在各自设备上安装复杂软件。使用 Jupyter 集成可直接在实验报告中嵌入交互地图。
- **现场数据采集验证**：移动端版本可随身携带，在野外或施工现场快速加载和查看已有的地理空间数据，验证采集结果或辅助决策。
- **轻量级数据展示平台**：地方政府、非营利组织或小型企业可通过 GeoLibre 创建无需后端服务器支撑的地图展示页面，快捷分享给利益相关方。
- **前端开发与原型测试**：开发者可以利用其插件体系与 React 组件化结构，快速为特定 GIS 场景定制界面或功能原型，缩短开发周期。

## 项目亮点

- **真正的跨平台统一体验**：与多数“移动端是 Web 套壳、桌面端另起炉灶”的 GIS 方案不同，GeoLibre 在桌面、Web、移动端使用完全相同的代码基础构建，用户界面与功能高度一致，学习成本极低。
- **隐私云原生的独特结合**：虽然冠以“云原生”之名，但数据完全本地处理，不依赖云后台。这使得它在保持现代前端架构优势的同时，避免了传统云 GIS 带来的隐私顾虑。
- **插件市场驱动扩展**：从第一天起就设计为可扩展的架构，社区可以贡献插件并发布到插件市场，使得平台成长不依赖于核心维护团队。
- **极小体积与极快启动**：得益于 Tauri 的底层技术，桌面端安装包通常仅几十 MB，启动速度远优于 Electron 构建的传统 GIS 桌面应用。
- **学术友好的开放性**：完全开源、有 DOI 引用号（10.5281/zenodo.20785400），适合学术工作引用，在数据科学社区（Jupyter 生态）中也有良好支持。

## 相关链接

- [GitHub 仓库](https://github.com/opengeos/GeoLibre)
- [在线 Web 版](https://web.geolibre.app/)
- [插件市场](https://plugins.geolibre.app/)
- [桌面应用下载页](https://geolibre.app/downloads/)
- [Google Colab 入门示例](https://colab.research.google.com/github/opengeos/GeoLibre/blob/main/python/examples/getting-started.ipynb)
- [PyPI 包](https://pypi.python.org/pypi/geolibre)
- [Conda 包](https://anaconda.org/conda-forge/geolibre)
- [Microsoft Store](https://apps.microsoft.com/detail/9nwt67rv531x)
- [Google Play](https://play.google.com/store/apps/details?id=org.geolibre.app)
- [Arch Linux AUR 包](https://aur.archlinux.org/packages/geolibre-bin)
- [Flathub](https://flatpark.org/apps/app.geolibre.GeoLibre/)
