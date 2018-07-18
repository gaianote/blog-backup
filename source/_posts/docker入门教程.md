---
title: docker入门教程
date: 2018-07-18 12:49:57
tags:
---

## docker的基本组成

1. 下载镜像
2. 使用容器，修改容器
3. 将修改的容器保存为新镜像
4. 将新镜像推送到docker-hub

示例:

```bash
# 搜索查看文件名包含tutorial的镜像
docker search tutorial
# 下载镜像 tutorial 到本地
docker pull learn/tutorial
# 执行learn/tutorial镜像,进入容器安装ping命令,这个操作是在镜像的可写层执行的
docker run learn/tutorial apt-get install -y ping
# 使用ps命令 查看CONTAINER ID，诸如 eb68b860a036
docker ps -l
# 提交容器,形成新镜像,并给新镜像起个名字 docker commit CONTAINER_ID NEW_IMAGE_NAME
docker commit eb68b860a036 learn/ping
# 使用新镜像
docker run learn/ping www.google.com
# 查看容器的详细信息，返回一个包含信息的json
docker inspect eb68b860a036
# 查看本地所有镜像
docker image ls
# 将镜像推送保存到docker-hub
docker push learn/ping
```

## docker容器的相关技术简介

**docker依赖的linux内核特性**

1. Namespace命名空间
2. Controlgroups控制组

**Namespace命名空间**

* 编程语言:封装 => 代码隔离
* 操作系统:系统资源的隔离 => 进程，网络，文件系统

**docker使用的Namespace命名空间**

* PID 进程隔离
* NET 管理网络接口
* IPC 管理跨进程通信访问
* MNT 管理挂载点.文件管理
* UTS 隔离内核和版本标识

**Controlgroups控制组**

Controlgroups控制组用来分配进程资源，来源与google,后被整合入linux内核，是容器技术的基础。

**docker容器的能力**

* 文件系统隔离:每个容器都有自己的root系统
* 进程隔离:每个容器都运行在自己的进程环境中
* 网络隔离:容器间的虚拟网络接口和IP地址都是分开的
* 资源隔离和分组:使用cgroup将cup和内存之类的资源独立分配给每个Docker容器




