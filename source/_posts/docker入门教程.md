---
title: docker入门教程
date: 2018-07-18 12:49:57
tags:
---
## 什么是docker

### 环境配置难题

软件开发的最大麻烦之一，就是环境的配置。软件，硬件乃至于依赖的不一致，都会给软件的开发，部署以及测试造成种种困扰。有没有一种软件自带原始环境的解决方案呢?

### 虚拟机

对于软件环境的配置,虚拟机是一种解决方案，但是它有以下几个问题:

* 资源占用多：虚拟机会独占一部分内存和硬盘空间。它运行的时候，其他程序就不能使用这些资源了。哪怕虚拟机里面的应用程序，真正使用的内存只有 1MB，虚拟机依然需要几百 MB 的内存才能运行。
* 冗余步骤多:虚拟机是完整的操作系统，一些系统级别的操作步骤，往往无法跳过，比如用户登录。
* 启动慢：启动操作系统需要多久，启动虚拟机就需要多久。可能要等几分钟，应用程序才能真正运行。

### Linux 容器

由于虚拟机存在这些缺点，Linux 发展出了另一种虚拟化技术：Linux 容器（Linux Containers，缩写为 LXC）。

Linux 容器不是模拟一个完整的操作系统，而是对进程进行隔离。由于容器是进程级别的，相比虚拟机有很多优势：

* 启动快：容器里面的应用，直接就是底层系统的一个进程，而不是虚拟机内部的进程。所以，启动容器相当于启动本机的一个进程，而不是启动一个操作系统，速度就快很多。

* 资源占用少：容器只占用需要的资源，不占用那些没有用到的资源；虚拟机由于是完整的操作系统，不可避免要占用所有资源。另外，多个容器可以共享资源，虚拟机都是独享资源。

* 体积小：容器只要包含用到的组件即可，而虚拟机是整个操作系统的打包，所以容器文件比虚拟机文件要小很多。

### Docker 是什么

Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口。Docker 的主要用途，目前有三大类：

* **提供一次性的环境：**比如，本地测试他人的软件、持续集成的时候提供单元测试和构建的环境。

* **提供弹性的云服务：**因为 Docker 容器可以随开随关，很适合动态扩容和缩容。

* **组建微服务架构：**。通过多个容器，一台机器可以跑多个服务，因此在本机就可以模拟出微服务架构。

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


## 容器的基本操作

### 启动容器

启动交互式容器

```bash
$ docker run -i -t 镜像名 bash
```

### 显示容器

显示正在运行的容器,通常是守护式容器

```
$ docker ps
```

显示所有的容器

```
$ docker ps -a
```

显示最近创建的一条容器

```
$ docker ps -l
```

### 显示容器详细信息

查看容器详细信息，返回一个json字符串

```
$ docker inspect 容器ID/容器名
```

### 自定义容器NAME

启动命令时，增加name选项

```
$ docker run --name = container01 -i -t centos bash
```

### 重新启动已经停止的容器

`-i`参数是指进入交互界面;run是指创建容器，用于镜像名

```
$ docker start -i 容器名
```

### 删除容器

```
$ docker rm 容器名
```

## 守护式容器

守护式容器是指适合作为服务器后端(后台)稳定长期运行的容器。

### 以守护式运行容器

方法1:

1. 以交互形式创建容器

```
$ docker run -i -t 镜像名 bash
```

2. 使用`ctrl + P` 和 `ctrl + Q`退出容器，之后容器会在后台运行

方法2:

`-d`是指以后台的形式运行容器，容器执行指令完毕后仍会停止。

```
$ docker run -d 镜像名 指令
```

### 进入守护式容器

```
$ docker attach 容器名
```

### 查看守护式容器运行情况

```
$ docker logs [-f] [-t] [--tail] 容器名
```

* `-f` : 一直跟踪日志变化，实时刷新。默认false
* `-t` : 为log输出添加时间戳。默认false
* `--tail` : 默认为所有，可以选择数值,比如 --tail = 5

可以用以下命令实时查看后台输出

```
$ docker logs -f -t --tail = 0 容器名
```

### 查看守护式容器正在运行的进程

```
$ docker top 容器名
```

### 在运行的容器内启动新进程

```bash
$ docker exec [-d][-i][-t] 容器名 [COMMAND]
```

如下命令，相当于在容器中新建一个终端:

```
$ docker exec -i -t 容器名 bash
```

### 停止守护式容器

* stop命令会发送一个信号给容器,等待其停止
* kill命令会直接停止容器

```bash
$ docker stop 容器名
$ docker kill 容器名
```

## 使用容器部署静态网站

### 设置容器端口映射

**选项`-P`**:

将容器暴露所有端口进行映射，默认为false

```
docker run -P -i -t centos bash
```
**选项`-p`**:

1. 只指定容器端口,宿主机端口随机映射

```
$ docker run -p -80 -i -t centos bash
```

2. 指定容器端口:宿主机端口

```
$ docker run -p 8080:80 -i -t centos bash
```

3. 指定ip:容器端口:

```
$ docker run -p 0.0.0.0:80 -i -t centos bash
```

4. 指定ip:容器端口:宿主机端口

```
$ docker run -p 0.0.0.0:80 -i -t centos bash
```

