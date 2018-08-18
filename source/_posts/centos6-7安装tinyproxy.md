---
title: centos6/7安装tinyproxy
date: 2017-05-09 17:44:14
tags: linux
---

## 安装tinyproxy

```bash
yum install -y epel-release
yum update
yum -y install tinyproxy
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
