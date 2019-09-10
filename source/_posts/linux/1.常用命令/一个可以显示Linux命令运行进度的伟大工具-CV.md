---
title: linux显示进度条
date: 2019-07-16 14:13:33
tags: linux
---

progress前用名Coreutils Viewer，是使用C语言开发的，用来显示Linux命令执行进度的工具
支持cp, mv, tar, dd, gzip/gunzip, cat, grep等coreutils基本命令。

https://github.com/Xfennec/progress

Linux安装progress
progress依赖libncurses库显示进度条；安装依赖：

```bash
# CentOS
yum install ncurses-devel -y
# Fedora 22
dnf install ncurses-devel
# Ubuntu
sudo apt-get install libncurses5-dev
```
下载源码，编译安装：

```bash
git clone  https://github.com/Xfennec/progress;cd progress;make;make install
```

[安装教程](http://blog.topspeedsnail.com/archives/9464)