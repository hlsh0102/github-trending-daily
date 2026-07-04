---
tags:
  - trending
  - article
repo: ansible/ansible
date: 2026-07-04
language: Python
stars_total: 69242
stars_today: 65
---
## 项目概述

Ansible 是一个极致简洁的 IT 自动化平台，旨在让应用程序和系统的部署与维护变得前所未有的简单。它通过 SSH 协议管理远程机器，无需在目标系统上安装任何代理程序，使用接近自然语言的方式描述基础设施，从而解决了传统自动化工具配置复杂、学习曲线陡峭、需要代理客户端等核心痛点。目标用户包括系统管理员、运维工程师、开发人员、网络工程师以及任何需要自动化管理 IT 环境的从业者。

## 核心功能

- **配置管理**：确保系统处于期望状态，包括软件包安装、服务启动、文件配置等，支持幂等性操作。
- **应用部署**：自动化代码发布流程，支持零停机滚动更新、蓝绿部署等高级策略，可与负载均衡器协同工作。
- **云资源编排**：管理多云环境下的基础设施，支持快速创建、销毁和调整云实例（如 AWS、Azure、GCP），实现基础设施即代码。
- **临时任务执行**：在数百台机器上瞬间执行 ad-hoc 命令（如批量重启服务、查看日志），无需编写完整剧本。
- **网络自动化**：管理网络设备配置，支持交换机、路由器、防火墙等多种网络设备的自动化操作。
- **多节点编排**：协调复杂任务在多台机器上的执行顺序，确保前后依赖关系正确，例如先更新数据库再更新应用。

## 技术架构

Ansible 采用无代理（agentless）架构，核心设计原则如下：

- **SSH 基础**：默认通过 SSH 协议控制远程机器，无需在远程主机上安装额外软件或开放特殊端口，极大地简化了安全管理和网络配置。
- **模块化设计**：所有操作由模块（Modules）完成，模块可以用 Python、Shell 甚至动态语言（如 Perl、Ruby）编写，并支持通过任务计划（Playbook）组合调用。
- **幂等性**：大多数模块设计为幂等操作，即多次执行同一任务结果一致，避免了重复配置带来的副作用。
- **YAML 描述**：使用 YAML 格式编写 Playbook 和角色（Roles），语法直观接近自然语言，降低了编写和维护自动化脚本的门槛。
- **基于推送的模式**：控制节点主动推送配置和命令到被管理节点，相比于拉取模式更加灵活和实时。
- **无状态设计**：被管理节点不保持连接状态，控制节点负责维护任务队列和结果收集，适合大规模集群管理。

## 安装与使用

### 安装步骤

Ansible 可以安装在 Linux、macOS 或 Windows（通过 WSL）上。推荐使用系统包管理器安装：

```bash
# 在 Debian/Ubuntu 上
sudo apt update
sudo apt install ansible

# 在 CentOS/RHEL 上
sudo yum install epel-release
sudo yum install ansible
```

或通过 pip 安装最新版本：

```bash
pip install ansible
```

### 最小可用示例

1. **创建主机清单文件**（inventory.ini）：
```ini
[webservers]
web1.example.com
web2.example.com

[databases]
db.example.com
```

2. **测试连通性**：
```bash
ansible all -i inventory.ini -m ping
```

3. **编写简单 Playbook**（test.yml）：
```yaml
---
- name: 确保 nginx 已安装并启动
  hosts: webservers
  tasks:
    - name: 安装 nginx
      apt:
        name: nginx
        state: present
    - name: 启动 nginx
      service:
        name: nginx
        state: started
```

4. **执行 Playbook**：
```bash
ansible-playbook -i inventory.ini test.yml
```

## 适用场景

- **服务器标准化配置**：在数十或数百台服务器上统一安装软件包、配置系统参数、设置用户权限，确保所有环境一致。
- **持续交付与部署**：集成到 CI/CD 流水线中，自动执行代码发布、数据库迁移、服务重启等步骤，支持灰度发布和回滚。
- **多云资源管理**：使用 Ansible 模块（如 ec2、gce、azure_rm）批量创建和管理不同云平台的虚拟机、存储和网络资源。
- **网络设备管理**：通过专门的网络模块（如 ios、junos、eos）管理路由器、交换机的配置备份、版本升级和合规检查。

## 项目亮点

- **极低的学习曲线**：YAML 语法直观，接近英文描述，新手可在数小时内上手编写自动化任务，而无需学习复杂的领域特定语言。
- **无代理架构**：无需在远程机器上安装客户端，省去了代理分发、升级和维护的麻烦，特别适合管理老旧系统或安全敏感的隔离网络。
- **生态丰富**：拥有数千个内置模块和社区贡献的角色（Ansible Galaxy），覆盖系统管理、云平台、数据库、网络设备等几乎所有主流场景。
- **安全性高**：操作通过 SSH 传输，加密通信；Playbook 使用纯文本描述，易于审查和审计，支持基于角色的访问控制（RBAC）。
- **跨平台支持**：不仅管理 Linux/Unix 主机，也支持 Windows（通过 WinRM）和网络设备，实现异构环境的统管。
- **可扩展性强**：支持自定义模块（任何动态语言）和插件，可轻松集成现有脚本或第三方工具。

## 相关链接

- [GitHub 仓库](https://github.com/ansible/ansible)
- [官方文档](https://docs.ansible.com)
- [官方站点](https://ansible.com)
