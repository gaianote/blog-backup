title: 使用WolCmd.exe工具远程唤醒主机
author: 李云鹏
date: 2019-08-27 11:04:07
tags:
---

wolcmd.exe是一款应用于windows上的wake on lan的工具，通过它，我们可以轻易的唤醒远程主机。

## 1. 进入的WolCmd.exe的同级目录,键入WolCmd.exe，可以看到它的语法结构

```bash
λ WolCmd.exe
Wake On Lan Command Line...

Usage: wolcmd [mac address] [ipaddress] [subnet mask] [port number]

i.e.  wolcmd 009027a322fc 195.188.159.20 255.255.255.0 7

or    wolcmd 009027a322fc depicus.com 255.255.255.0 7

Copyright www.depicus.com (Brian Slack) 1966-2005
```

## 2. 根据实际情况传入参数即可

比如我的主机mac地址是08CA45D60A80，ip地址是192.168.72.107，子网掩码是255.255.255.0，端口号是8900

```bash
WolCmd.exe 08CA45D60A80 192.168.72.107 255.255.255.0 8900
```

## 3. [点击下载WolCmd](/files/WolCmd.exe)