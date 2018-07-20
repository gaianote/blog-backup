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

