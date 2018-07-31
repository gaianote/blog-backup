---
title: centos使用yum安装python3以及pip3
date: 2018-07-30 19:20:41
tags:
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
