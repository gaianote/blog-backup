---
title: centos使用yum安装python3以及pip3
date: 2018-07-30 19:20:41
tags: linux
---

因为CentOS 7上默认的Python版本是2.7, 所以我们可以通过添加其他源方式再安装Python3.6.

安装EPEL和IUS软件源


```bash
yum install epel-release
yum install https://centos7.iuscommunity.org/ius-release.rpm
```

安装Python3.6


```bash
yum install python36u
```

创建python3连接符


```bash
ln -s /bin/python3.6 /bin/python3
```

安装pip3


```bash
yum install python36u-pip
```

创建pip3链接符


```bash
ln -s /bin/pip3.6 /bin/pip3
```

这样就完成了

安装一些常用的支持


```bash
pip3 install requests
pip3 install pymysql
pip3 install xmltodict
pip3 install six
```

## Yum 简介
Yum（全称为 Yellow dog Updater, Modified）是一个在Fedora和RedHat以及CentOS中的Shell前端软件包管理器。基于RPM包管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包，无须繁琐地一次次下载、安装。

## 常用的 Yum 命令

1、显示已经安装的软件包
```
yum list installed
```


2、查找可以安装的软件包 （以 tomcat 为例）
```
yum list tomcat
```


3、安装软件包 （以 tomcat 为例）
```
yum install tomcat
```


4、卸载软件包 （以 tomcat 为例）
```
yum remove tomcat
```


5、列出软件包的依赖 （以 tomcat 为例）
```
yum deplist tomcat
```



6、-y 自动应答yes
在安装软件的时候，会有中断，让用户选择是否要继续，如下图：



我们可以用 -y 来应答所有的 yes , 比如我们安装 tomcat 的时候，用下面的命令，将安装任务一气呵成，不会中断。
```
yum -y install tomcat
```
7、info 显示软件包的描述信息和概要信息
以 tomcat 为例
```
yum info tomcat
```


8、升级软件包
升级所有的软件包
```
yum update
```
升级某一个软件包 ，以升级 tomcat 为例
```
yum update tomcat
```
检查可更新的程序
```
yum check-update
```