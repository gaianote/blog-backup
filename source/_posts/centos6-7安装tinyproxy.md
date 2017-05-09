---
title: centos6/7安装tinyproxy
date: 2017-05-09 17:44:14
tags: linux
---

centos7安装tinyproxy，centos6安装tinyproxy，centos6/7安装tinyproxy(yum安装)，yum安装tinyproxy

## 首先启用：CentOS Extras repository

如果 `wget` 不存在，首先安装 `wget`

```bash
yum -y install wget
```

CentOS and Red Hat Enterprise Linux 5.x

```bash
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm
sudo rpm -Uvh epel-release-5*.rpm
```

CentOS and Red Hat Enterprise Linux 6.x

```bash
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
sudo rpm -Uvh epel-release-6*.rpm
```

CentOS and Red Hat Enterprise Linux 7.x

```bash
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo rpm -Uvh epel-release-latest-7*.rpm
```

## 安装tinyproxy

```bash
yum install tinyproxy
```

## 配置tinyproxy

修改Allow 127.0.0.1为自己IP，只允许自己使用，或者在Allow前面打#注释，允许任何IP都可以连接

```bash
vi /etc/tinyproxy/tinyproxy.conf
```

## 启动Tinyproxy服务，并设置开机自启

```bash
service tinyproxy restart
chkconfig --level 345 tinyproxy on
#centos7如下设置:
systemctl restart  tinyproxy.service
systemctl enable tinyproxy.service
```

## 防火墙开放8888（或已经自定义）端口

```bash
iptables -I INPUT -p tcp --dport 8888 -j ACCEPT
#centos7如下设置:
firewall-cmd --zone=public --add-port=8888/tcp --permanent
firewall-cmd --reload
```
