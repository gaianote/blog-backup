---
title: 03 Linux系统维护管理
date: 2019-04-12 14:18:36
tags: linux
---


```
data 查看日期，设置日期
clear 清屏
man 查看帮助信息
who 查看用户信息
w 用户信息，更全面
uname 操作系统信息
uptime 输出系统任务队列信息
last 输出上次和过去系统用户登陆的信息,详细的日志信息，包括用户名，终端，ip，登陆时间以及断开时间
dmesg 显示开机信息
free 显示系统内存状态
```

## date

查看日期，设置日期（只有root用户才可以设置时间）

```
# date
Tue Apr  2 22:28:17 CST 2019
```

结合`+`号输出特定的格式

```
# date '+%Y年%m月%d日 %H时%M分%S秒'
2019年04月02日 22时26分55秒
```

设置时间

```
# data -s 2020-01-01
```

## who

```
# who
root     tty2         2019-04-02 22:01
root     pts/0        2019-04-02 22:02 (192.168.199.233)
```

## w

```
# w
 22:37:14 up 36 min,  2 users,  load average: 0.00, 0.01, 0.03
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty2                      22:01   35:22   0.06s  0.06s -bash
root     pts/0    192.168.199.233  22:02    2.00s  0.17s  0.00s w
```

## uname

```
# uname -a
Linux localhost.localdomain 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

## dmesg

`dmesg -c` 显示并清空开机信息

## free

Mem：物理内存
Swap：虚拟分区，当物理内存不足时，用于缓解问题

```
[root@localhost ~]# free -h                                                        
              total        used        free      shared  buff/cache   available    
Mem:           3.7G        418M        2.9G         14M        412M        3.0G    
Swap:          2.0G          0B        2.0G      
```                                  
