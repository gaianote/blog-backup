---
title: docker微服务教程
date: 2018-07-16 17:00:08
tags:
---

Docker 是一个容器工具，提供虚拟环境。很多人认为，它改变了我们对软件的认识。

站在 Docker 的角度，软件就是容器的组合：业务逻辑容器、数据库容器、储存容器、队列容器......Docker 使得软件可以拆分成若干个标准化容器，然后像搭积木一样组合起来。

![img](http://www.ruanyifeng.com/blogimg/asset/2018/bg2018021306.png)

这正是微服务（microservices）的思想：软件把任务外包出去，让各种外部服务完成这些任务，软件本身只是底层服务的调度中心和组装层。

![img](http://www.ruanyifeng.com/blogimg/asset/2018/bg2018021302.png)

微服务很适合用 Docker 容器实现，每个容器承载一个服务。一台计算机同时运行多个容器，从而就能很轻松地模拟出复杂的微服务架构。

![img](http://www.ruanyifeng.com/blogimg/asset/2018/bg2018021303.png)

[上一篇教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)介绍了 Docker 的概念和基本用法，本文接着往下介绍，如何在一台计算机上实现多个服务，让它们互相配合，组合出一个应用程序。

![img](http://www.ruanyifeng.com/blogimg/asset/2018/bg2018021304.png)

我选择的示例软件是 [WordPress](https://wordpress.org/)。它是一个常用软件，全世界用户据说超过几千万。同时它又非常简单，只要两个容器就够了（业务容器 + 数据库容器），很适合教学。而且，这种"业务 + 数据库"的容器架构，具有通用性，许多应用程序都可以复用。