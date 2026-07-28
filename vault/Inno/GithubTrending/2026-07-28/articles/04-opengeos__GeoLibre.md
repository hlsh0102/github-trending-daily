---
tags:
  - trending
  - article
repo: opengeos/GeoLibre
date: 2026-07-28
language: TypeScript
stars_total: 2861
stars_today: 420
---
## 项目概述

GeoLibre 是一个免费开源、轻量级的云原生 GIS 平台，用于可视化、探索和分析地理空间数据。它的核心理念是“随处运行”——无论是在 Web 浏览器、桌面端、移动设备，还是 Jupyter notebook 中，GeoLibre 都能提供一致的 GIS 体验，同时确保用户数据的本地化和隐私性。

该项目由 opengeos 团队维护，使用 MIT 许可证开源。GeoLibre 旨在降低 GIS 工具的使用门槛，让地理空间分析不再局限于专业的桌面软件或复杂的服务器部署。无论你是 GIS 专家、数据科学家，还是地理信息爱好者，都可以快速上手使用。

## 核心功能

- **跨平台运行**：一套代码同时支持 Web 浏览器、桌面端（Windows/macOS/Linux）、Android 移动端以及 Jupyter notebook 环境，无需为不同平台单独部署。
- **多种数据格式支持**：原生支持 GeoJSON、CSV、Shapefile、GeoParquet、GPKG、KML、GPX 等常见地理空间数据格式，可直接拖拽或打开加载。
- **丰富的数据可视化**：基于 MapLibre GL JS 和 deck.gl 构建，支持矢量瓦片、栅格图层、点云、热力图、3D 建筑等多种可视化样式。
- **本地化空间分析**：集成 DuckDB-WASM Spatial 引擎，支持在浏览器端执行空间查询、距离计算、缓冲区分析、矢量瓦片生成等操作，无需后端服务。
- **交互式探索工具**：提供数据属性表查看、属性筛选、空间选择、坐标拾取、距离与面积测量等交互工具。
- **可扩展的插件系统**：提供插件接口，用户可自定义添加数据源、分析工具或 UI 组件，拓展平台功能。

## 技术架构

GeoLibre 采用了现代化的技术栈，实现了“一次编写，随处运行”的目标：

- **前端框架**：使用 React 与 TypeScript 构建界面，确保代码的类型安全和可维护性。
- **跨平台框架**：采用 Tauri v2 作为桌面端和移动端的原生壳，结合 WebView 渲染前端页面，实现原生级的性能和 API 访问能力。
- **地图引擎**：MapLibre GL JS 负责底图渲染和矢量瓦片显示，deck.gl 用于处理大规模地理数据（如热力图、聚集点、路径等）的高性能 WebGL 可视化。
- **空间计算引擎**：DuckDB-WASM Spatial 是在浏览器中运行的空间数据库引擎，支持 SQL 空间查询和地理计算，所有运算都在用户本地完成，保障数据隐私。
- **数据处理**：前端通过 Web Workers 和 WASM 模块处理数据加载与转换，避免阻塞 UI 线程。

这种架构设计使得 GeoLibre 在 Web 浏览器中即可运行完整的 GIS 功能，同时通过 Tauri 封装为原生应用后，能够访问本地文件系统和设备硬件，提供更佳的性能体验。

## 安装与使用

GeoLibre 提供了多种使用方式，用户可根据需求选择：

**1. 直接使用 Web 版本**  
无需安装，打开浏览器访问`https://web.geolibre.app/`即可立即使用全部功能。

**2. 下载桌面客户端**  
从项目主页`https://geolibre.app/downloads/`下载对应操作系统的安装包（Windows .exe、macOS .dmg、Linux .AppImage 或 .deb），安装后即可离线使用。

**3. 从源码构建**  
```bash
git clone https://github.com/opengeos/GeoLibre.git
cd GeoLibre
npm install
npm run dev      # 启动开发服务器
npm run tauri build  # 构建桌面应用
```

**4. 在 Jupyter notebook 中使用**  
```python
# 安装 Python 包
pip install geolibre
# 在 notebook 中启动
from geolibre import GeoLibreApp
app = GeoLibreApp()
```

**5. 在 Google Colab 中使用**  
点击 README 中的 Colab 徽章，可直接在浏览器中运行交互式 notebook 示例。

## 适用场景

- **数据可视化与探索**：快速加载和展示 geojson 或 csv 格式的地理数据，进行交互式地图探索和属性筛选，适合数据产品经理、地理信息分析师日常使用。
- **教学与科研**：在 Jupyter notebook 中集成 GIS 功能，适合地理信息科学、遥感、城市数据分析等课程教学和科研实验。
- **野外数据采集与汇报**：在移动端（Android）打开 GeoLibre，现场查看和编辑地理数据，配合投影或大屏展示，满足外业汇报需求。
- **原型开发与演示**：无需部署后端服务，直接在浏览器中运行完整 GIS 应用，快速验证数据产品原型或向客户演示分析能力。

## 项目亮点

- **真正的跨平台一致性**：与传统的 Web GIS 或桌面 GIS 不同，GeoLibre 实现了同一套代码在浏览器、桌面、移动端和 notebook 中完全一致的功能体验，用户无需重新学习操作。
- **数据隐私优先**：所有空间分析运算（DuckDB-WASM）都在用户本地浏览器或设备中执行，不会上传用户数据到任何服务器，解决了 GIS 应用中常见的数据安全顾虑。
- **轻量且高性能**：得益于 Tauri 的优化，桌面端安装包仅数十 MB，远小于传统桌面 GIS 软件；同时利用 WebGL 和 WASM 技术，即使处理百万级数据点也能保持流畅交互。
- **完整的插件生态**：提供 Web 端和桌面端的插件市场（plugins.geolibre.app），支持社区贡献和第三方扩展，避免了单体应用的固化和封闭。

## 相关链接

- [GitHub 仓库](https://github.com/opengeos/GeoLibre)
- [Web 版应用](https://web.geolibre.app/)
- [桌面端下载](https://geolibre.app/downloads/)
- [插件市场](https://plugins.geolibre.app/)
- [Python 包（PyPI）](https://pypi.python.org/pypi/geolibre)
- [Colab 入门示例](https://colab.research.google.com/github/opengeos/GeoLibre/blob/main/python/examples/getting-started.ipynb)
- [项目文档与入门指南](https://geolibre.app/getting-started/)
