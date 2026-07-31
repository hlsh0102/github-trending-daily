---
tags:
  - trending
  - article
repo: ansible/ansible
date: 2026-07-31
language: Python
stars_total: 69937
stars_today: 29
---
## 项目概述

Ansible 是一个极其简单的 IT 自动化平台，旨在让应用程序和系统的部署与维护变得更加轻松。它能够处理配置管理、应用部署、云资源 provisioning、临时任务执行、网络自动化以及多节点编排等各类运维需求。Ansible 使用接近自然语言的描述方式，基于 SSH 协议工作，无需在远程系统上安装任何代理（agent），极大地降低了自动化的入门门槛。项目采用 GPL-3.0 许可证，目前由 Red Hat 主导维护，在 GitHub 上获得了超过 7 万星标，是社区中最活跃的运维自动化项目之一。

Ansible 的目标用户非常广泛，包括系统管理员、DevOps 工程师、网络工程师、云平台管理者，以及任何希望将重复性 IT 工作进行自动化的人员。无论你管理的是几台服务器，还是数千台跨云环境的节点，Ansible 都能提供统一且易用的管理方式。

## 核心功能

- **配置管理**：通过 Playbook 定义系统应有的状态，确保每台服务器上的配置保持一致，支持从基础软件安装到复杂服务调优。
- **应用部署**：支持多阶段、零停机滚动更新，可与负载均衡器联动，实现应用发布过程中的流量切换与健康检查。
- **临时命令执行（Ad-hoc）**：无需编写完整的 Playbook，即可使用一条命令在大量主机上并行执行操作，如分发密钥、重启服务、查询系统信息。
- **云资源编排**：提供丰富的云模块（AWS、Azure、GCP、OpenStack 等），可直接在 Playbook 中创建、销毁和调整云主机、网络等资源，实现基础设施即代码（IaC）。
- **网络自动化**：专门面向网络设备（如 Cisco、Juniper、Arista 等）的模块，支持使用统一的语言管理网络设备的配置和状态。
- **多节点编排**：通过依赖关系定义任务的执行顺序，可跨多台主机协调复杂的工作流，比如先升级应用服务器，再升级数据库服务器，最后刷新缓存。

## 技术架构

Ansible 采用无代理（agentless）的极简架构，核心设计基于以下关键技术:

- **基于 SSH 的传输层**：默认利用系统自带的 OpenSSH 作为远程执行通道，无需在目标主机上安装任何额外的服务或代理。对于 Windows 主机，则使用 WinRM 协议。这种设计避免了对目标系统的侵入，也减少了安全漏洞暴露面。
- **模块化执行模型**：Ansible 将任务封装成模块（Module），这些模块是用 Python 或其他动态语言编写的可执行脚本。执行时，Ansible 将模块和参数打包并通过 SSH 传输到目标主机，执行完毕后将结果返回到控制节点，整个过程不依赖目标端的 Ansible 安装。
- **幂等性设计**：绝大多数模块在设计时遵循幂等原则，即重复执行相同任务不会产生副作用，系统会始终收敛到目标状态。这保证了 Playbook 可安全地重复运行。
- **YAML 声明式语言**：Playbook 采用 YAML 编写，使用 "任务（Task）" 列表来定义期望的状态和操作。这种格式对人类极其友好，既容易编写，也容易被代码审查工具追踪变更。
- **基于 Inventory 的主机管理**：通过简单的静态文件（INI 格式）或动态脚本，将主机分组管理，用户可以基于组、主机名或通配符来指定任务执行的目标范围。
- **可扩展性**：除了 Python 模块，还支持使用 Ruby、JavaScript 等任何动态语言编写自定义模块，并通过 `ansible-galaxy` 共享角色（Role），实现内容的复用。

## 安装与使用

Ansible 的控制端（即你执行命令的机器）需要安装 Python 环境。虽然它支持多种 Linux/Unix 发行版，但 macOS 和 Windows（通过 WSL）也可以使用。

**安装步骤（以使用 pip 为例）**：

```bash
# 安装最新版本的 ansible（包含额外功能集合）
pip install ansible

# 或者仅安装核心引擎（体积更小，按需安装 collection）
pip install ansible-core
```

在 Ubuntu/Debian 等系统上，也可以通过 `apt` 安装：
```bash
sudo apt update
sudo apt install ansible
```

**最小可用示例**：

1.  创建一个名为 `hosts` 的清单文件，定义你的服务器地址（使用 SSH 密钥或密码认证）：

    ```ini
    [web_servers]
    192.168.1.10
    192.168.1.11
    ```

2.  使用 `ping` 模块测试控制端与这些主机的连通性：

    ```bash
    ansible web_servers -i hosts -m ping
    ```

3.  执行一条临时命令（ad-hoc），比如在 Web 服务器上检查磁盘空间：

    ```bash
    ansible web_servers -i hosts -m shell -a "df -h"
    ```

4.  编写一个简单的 Playbook（`playbook.yml`）来安装 Nginx：

    ```yaml
    ---
    - name: Ensure Nginx is installed
      hosts: web_servers
      become: yes
      tasks:
        - name: Install nginx
          ansible.builtin.apt:
            name: nginx
            state: present
    ```

    然后使用 `ansible-playbook -i hosts playbook.yml` 运行它。

## 适用场景

- **基础设施即代码（IaC）与配置漂移防护**：企业可以把服务器配置、软件包版本、服务状态等全部写成代码存入 Git。当审计发现配置漂移时，只需重新运行 Playbook，系统即会恢复到期望状态。
- **CI/CD 持续交付流水线**：Ansible 常被集成到 Jenkins、GitLab CI 等流水线中，负责代码构建后的自动化测试环境部署、生产环境发布以及回滚操作。
- **混合云环境管理**：对于同时使用私有数据中心和公有云的场景，Ansible 结合动态 Inventory，可实现统一的资源管理和编排，例如在业务高峰时自动扩展云主机。
- **大规模服务器初始化**：新买的裸机或新创建的云虚拟机，可以纳入 Ansible 的管理范围，自动完成用户创建、安全加固、基础软件安装等初始化操作，实现“开机即纳管”。

## 项目亮点

- **极低的学习曲线**：与 Puppet 或 Chef 相比，Ansible 无需学习特定的领域特定语言（DSL），掌握 YAML 和 SSH 基础即可快速上手。
- **真正的无代理架构**：无需在目标机维护客户端状态，升级 Ansible 版本不会影响已纳管的节点，也降低了被入侵和端口扫描的风险。
- **内容生态丰富**：通过 `ansible-galaxy` 可下载社区共享的大量 Role，涵盖常见的应用配置和云服务，节省大量的重复造轮子时间。
- **易于审计与协作**：声明式的 Playbook 使得代码审查变得非常直观，所有变更都有迹可循，非常适合团队的规范化运维。
- **可衡量的轻量级**：控制端仅需 Python，对硬件资源要求极低，管理端无需任何预装软件，真正实现了“即连即用”。

## 相关链接

- [GitHub 仓库](https://github.com/ansible/ansible)
- [官方文档](https://docs.ansible.com)
- [官方站点](https://ansible.com)
