---
title: selenium与docker-selenium进行自动化测试
date: 2018-07-17 11:25:37
tags:
---

Selenium官方提供了基于selenium hub的方式来管理selenium的node节点，提供了分布式的远程调度方案，可以为SeleniumGrid添加各种类型的WebDriver。

Selenium Grid架构图,分为hub控制节点和node浏览器节点:
![img](/images/20180717_01.png)



1. 查找Selenium相关镜像
命令为：

```bash
docker search selenium
```

2. 此次我们需要3个镜像（1个Hub，2个Node），同时为了可以直观的看到实验结果，决定选用自带VNC Server的版本。获取官网上的镜像命令为:

```bash
docker pull selenium/hub
docker pull selenium/node-firefox-debug
docker pull selenium/node-chrome-debug
```

[Selenium结合 Docker-Selenium 镜像进行 Web 应用并发自动化测试](https://testerhome.com/topics/8148)

https://www.jianshu.com/p/382ebaa4b7a9