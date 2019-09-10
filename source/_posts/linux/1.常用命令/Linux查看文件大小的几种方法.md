---
title: Linux查看文件大小的几种方法
date: 2019-06-12 13:12:36
tags: linux
---

## 1. stat命令

```bash
stat filepath

xanarry@ThinkPad:/$ stat ~/Downloads/jdk-8u60-linux-x64.tar.gz
  File: '/home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz'
  Size: 181238643       Blocks: 353984     IO Block: 4096   regular file
Device: 808h/2056d      Inode: 261742      Links: 1
Access: (0666/-rw-rw-rw-)  Uid: ( 1000/ xanarry)   Gid: ( 1000/ xanarry)
Access: 2017-02-01 17:36:43.177892508 +0800
Modify: 2015-10-02 12:43:29.853291000 +0800
Change: 2016-12-26 23:33:34.619480450 +0800
```

## 2. wc命令
wc -c filename 参数-c表示统计字符, 因为一个字符一个字节, 所以这样得到字节数

```
xanarry@ThinkPad:/$ wc -c  ~/Downloads/jdk-8u60-linux-x64.tar.gz
181238643 /home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz
```

## 3. du命令

```
du -b filepath 参数-b表示以字节计数

xanarry@ThinkPad:/$ du -b  ~/Downloads/jdk-8u60-linux-x64.tar.gz
181238643       /home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz
```

或者

du -h filepath 直接得出人好识别的文件大小

```
xanarry@ThinkPad:/$ du -h  ~/Downloads/jdk-8u60-linux-x64.tar.gz
173M    /home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz
```

## 4. ls命令
`ls -l filepath` 第五列为文件字节数

```
$ ls -l  ~/Downloads/jdk-8u60-linux-x64.tar.gz
-rw-rw-rw- 1 xanarry xanarry 181238643 10月  2  2015 /home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz
```
`ls -lh filepath` h表示human, 加-h参数得到人好读的文件大小

```bash
$ ls -lh  ~/Downloads/jdk-8u60-linux-x64.tar.gz
-rw-rw-rw- 1 xanarry xanarry 173M 10月  2  2015 /home/xanarry/Downloads/jdk-8u60-linux-x64.tar.gz
```
