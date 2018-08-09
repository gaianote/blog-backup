---
title: docker微服务教程
date: 2018-07-16 17:00:08
tags:
---

## docker 微服务

Docker 是一个容器工具，提供虚拟环境。很多人认为，它改变了我们对软件的认识。

站在 Docker 的角度，软件就是容器的组合：业务逻辑容器、数据库容器、储存容器、队列容器......Docker 使得软件可以拆分成若干个标准化容器，然后像搭积木一样组合起来。

![img](/images/dcd885aaf103425ea23e1b86ac047851.png)
这正是微服务（microservices）的思想：软件把任务外包出去，让各种外部服务完成这些任务，软件本身只是底层服务的调度中心和组装层。

![img](/images/31e614c314144a12bee4648055ad195e.png)
微服务很适合用 Docker 容器实现，每个容器承载一个服务。一台计算机同时运行多个容器，从而就能很轻松地模拟出复杂的微服务架构。

![img](/images/3a621e11b77b40e29777a78d8906ffc1.png)
[上一篇教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)介绍了 Docker 的概念和基本用法，本文接着往下介绍，如何在一台计算机上实现多个服务，让它们互相配合，组合出一个应用程序。

![img](/images/ec5729df2c614de6a3c9a2a9c5b81df1.png)
我选择的示例软件是 [WordPress](https://wordpress.org/)。它是一个常用软件，全世界用户据说超过几千万。同时它又非常简单，只要两个容器就够了（业务容器 + 数据库容器），很适合教学。而且，这种"业务 + 数据库"的容器架构，具有通用性，许多应用程序都可以复用。

## Docker Compose 工具

如果我们自己处理容器的话，必须自己分别启动两个容器，启动的时候，还要在命令行提供容器之间的连接信息。所幸，Docker 提供了一种更简单的方法，来管理多个容器的联动。

### 4.1 Docker Compose 简介

![img](http://www.ruanyifeng.com/blogimg/asset/2018/bg2018021311.jpg)

[Compose](https://docs.docker.com/compose/) 是 Docker 公司推出的一个工具软件，可以管理多个 Docker 容器组成一个应用。你需要定义一个 [YAML](http://www.ruanyifeng.com/blog/2016/07/yaml.html) 格式的配置文件`docker-compose.yml`，写好多个容器之间的调用关系。然后，只要一个命令，就能同时启动/关闭这些容器。

```bash

# 启动所有服务
$ docker-compose up
# 关闭所有服务
$ docker-compose stop

```

### 4.2 Docker Compose 的安装

Mac 和 Windows 在安装 docker 的时候，会一起安装 docker compose。Linux 系统下的安装参考[官方文档](https://docs.docker.com/compose/install/#install-compose)。

安装完成后，运行下面的命令。

```bash

$ docker-compose --version

```

### 4.3 WordPress 示例

在`docker-demo`目录下，新建`docker-compose.yml`文件，写入下面的内容。

```yaml

mysql:
    image: mysql:5.7
    environment:
     - MYSQL_ROOT_PASSWORD=123456
     - MYSQL_DATABASE=wordpress
web:
    image: wordpress
    links:
     - mysql
    environment:
     - WORDPRESS_DB_PASSWORD=123456
    ports:
     - "127.0.0.3:8080:80"
    working_dir: /var/www/html
    volumes:
     - wordpress:/var/www/html

```

上面代码中，两个顶层标签表示有两个容器`mysql`和`web`。每个容器的具体设置，前面都已经讲解过了，还是挺容易理解的。

启动两个容器。

```bash
$ docker-compose up
```

浏览器访问 http://127.0.0.3:8080，应该就能看到 WordPress 的安装界面。

现在关闭两个容器。

```

$ docker-compose stop

```

关闭以后，这两个容器文件还是存在的，写在里面的数据不会丢失。下次启动的时候，还可以复用。下面的命令可以把这两个容器文件删除（容器必须已经停止运行）。

```
$ docker-compose rm
```

## 参考资料
[Docker 微服务教程](http://www.ruanyifeng.com/blog/2018/02/docker-wordpress-tutorial.html_)