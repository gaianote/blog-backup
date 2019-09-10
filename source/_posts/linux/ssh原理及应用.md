---
title: ssh原理及应用
date: 2017-05-09 10:26:16
tags: linux
---

## 1. 什么是SSH？

简单说，SSH是一种网络协议，用于计算机之间的加密登录。
如果一个用户从本地计算机，使用SSH协议登录另一台远程计算机，我们就可以认为，这种登录是安全的，即使被中途截获，密码也不会泄露。
最早的时候，互联网通信都是明文通信，一旦被截获，内容就暴露无疑。1995年，芬兰学者Tatu Ylonen设计了SSH协议，将登录信息全部加密，成为互联网安全的一个基本解决方案，迅速在全世界获得推广，目前已经成为Linux系统的标准配置。
需要指出的是，SSH只是一种协议，存在多种实现，既有商业实现，也有开源实现。本文针对的实现是OpenSSH，它是自由软件，应用非常广泛。
此外，本文只讨论SSH在Linux Shell中的用法。如果要在Windows系统中使用SSH，会用到另一种软件PuTTY，这需要另文介绍。

## 2. 最基本的用法

SSH主要用于远程登录。假定你要以用户名user，登录远程主机host，只要一条简单命令就可以了。

```bash
$ ssh user@host
```

如果本地用户名与远程用户名一致，登录时可以省略用户名。

```bash
$ ssh host
```

SSH的默认端口是22，也就是说，你的登录请求会送进远程主机的22端口。使用p参数，可以修改这个端口。

```bash
$ ssh -p 2222 user@host
```

上面这条命令表示，ssh直接连接远程主机的2222端口。


## 3. 公钥登录

使用密码登录，每次都必须输入密码，非常麻烦。好在SSH还提供了公钥登录，可以省去输入密码的步骤。
所谓"公钥登录"，原理很简单，就是用户将自己的公钥储存在远程主机上。登录的时候，远程主机会向用户发送一段随机字符串，用户用自己的私钥加密后，再发回来。远程主机用事先储存的公钥进行解密，如果成功，就证明用户是可信的，直接允许登录shell，不再要求密码。
这种方法要求用户必须提供自己的公钥。如果没有现成的，可以直接用ssh-keygen生成一个：

**1. 生成公钥**
　　

```bash
$ ssh-keygen
```

运行上面的命令以后，系统会出现一系列提示，可以一路回车。其中有一个问题是，要不要对私钥设置口令（passphrase），如果担心私钥的安全，这里可以设置一个。
运行结束以后，在 `$HOME/.ssh/` 目录下，会新生成两个文件：`id_rsa.pub` 和 `id_rsa`。前者是你的公钥，后者是你的私钥。

这时再输入下面的命令，将公钥传送到远程主机host上面：

**2. 发送公钥**
　　

```bash
$ ssh-copy-id user@host
```

好了，从此你再登录，就不需要输入密码了。

## 4. scp

scp用于本地主机和远程主机之间进行文件传输，常用的有以下命令：

### 1. 本地文件复制到远程

**复制文件**

```bash
scp -P 2222 local_filename root@host:remote_filename
```

**复制目录**

```bash
scp -P 2222 -r local_folder root@host:remote_folder
```
### 2. 远程文件复制到本地

**复制文件**

```bash
scp -P 2222 root@host:remote_filename local_filename
```

**复制目录**

```bash
scp -P 2222 -r root@host:remote_folder local_folder
```

### 3. 参数说明

- `-v` 和大多数 linux 命令中的 -v 意思一样 , 用来显示进度 . 可以用来查看连接 , 认证 , 或是配置错误 .
- `-C` 使能压缩选项 .
- `-P` 选择端口 . 注意 -p 已经被 rcp 使用 .
- `-4` 强行使用 IPV4 地址 .
- `-6` 强行使用 IPV6 地址 .

### 4. 行为模式

1. 如果目录san存在，则会将remoteIO目录移动到san目录下
```bash
$ scp -r remoteIO root@192.168.71.195:/tmp/ztest/san
$ ls san
remoteIO
```
2. 如果目录san不存在，则会创建san目录，并将remoteIO内的内容复制到san目录下
```bash
$ scp -r remoteIO root@192.168.71.195:/tmp/ztest/san
$ ls san
config.yaml ... # remoteIO的内容
```


## 5. 参考资料

[SSH原理与运用（一）：远程登录](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)