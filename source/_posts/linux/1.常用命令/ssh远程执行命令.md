---
title: ssh远程执行命令
date: 2019-06-13 11:15:39
tags: linux
---

## ssh-keygen命令详解

同一ip地址更换主机，导致ssh无法连接，使用以下方法删除密钥后解决:

```
ssh-keygen -f "/root/.ssh/known_hosts" -R 172.10.16.5
```

- `-f filename` 指定密钥文件名
- `-R hostname` 从 `known_hosts` 文件中删除所有属于 `hostname`的密钥。

## 1. 远程执行命令

如果我们要查看一下某台主机的磁盘使用情况，是不是必须要登录到目标主机上才能执行 df 命令呢？当然不是的，我们可以使用 ssh 命令在远程的主机上执行 df 命令，然后直接把结果显示出来。整个过程就像是在本地执行了一条命令一样：

```
$ ssh root@192.168.199.199 "df -h"
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root   17G  5.3G   12G  31% /
devtmpfs                 470M     0  470M   0% /dev
...
```

那么如何一次执行多条命令呢？其实也很简单，使用分号把不同的命令隔起来就 OK 了：

```
$ ssh root@192.168.199.199 "cd /home;ls"
admin
```

注意，当命令多于一个时用引号括起来，否则在有的系统中除了第一个命令，其它都是在本地执行的。

## 2. 远程执行需要交互的命令

通常情况下，当你通过 ssh 在远程主机上执行命令时，并不会为这个远程会话分配 TTY。此时 ssh 会立即退出远程主机，所以需要交互的命令也随之结束。好在我们可以通过`-t` 参数显式的告诉 ssh，我们需要一个 TTY 远程 shell 进行交互！

```
$ ssh -t root@192.168.199.199 "top"

PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND                 1 root      20   0  128580   5000   2908 S  0.0  0.5   0:16.97 systemd                   2 root      20   0       0      0      0 S  0.0  0.0   0:00.25 kthreadd                    3 root      20   0       0      0      0 S  0.0  0.0   0:38.07 ksoftirqd/0    
...
```

上面的情况`-t`参数是必须的，否则终端会提示`TERM environment variable not set.`错误

```
ssh root@192.168.199.199 "top"
TERM environment variable not set.
```

## 3. 远程执行脚本

对于要完成一些复杂功能的场景，如果是仅仅能执行几个命令的话，简直是弱爆了。我们可能需要写长篇累牍的 shell 脚本去完成某项使命！此时 SSH 依然是不辱使命的好帮手(哈哈，前面的内容仅仅是开胃菜啊！)。

### 1. 执行本地的脚本

我们在本地创建一个脚本文件 test.sh，内容为：

```bash
ls
pwd
```

然后运行下面的命令：

```
$ ssh root@192.168.199.199 < test.sh
/root
```

要想在这种情况下(远程执行本地的脚本)执行带有参数的脚本，需要为 bash 指定` -s `参数：

```
$ ssh root@192.168.199.199 'bash -s' < test.sh hello
```

### 2. 执行远程服务器上的脚本

除了执行本地的脚本，还有一种情况是脚本文件存放在远程服务器上，而我们需要远程的执行它！
此时在远程服务器上用户 nick 的家目录中有一个脚本 test.sh。文件的内容如下：

```bash
ls
pwd
```

执行下面的命令：

```bash
$ ssh root@192.168.199.199 "/home/nick/test.sh"
```

注意，此时需要指定脚本的绝对路径！

下面我们也尝试为脚本传递参数。在远程主机上的 test.sh 文件的末尾添加两行：

```bash
echo $0
```

然后尝试执行下面的命令：

```bash
$ ssh root@192.168.199.199 /home/nick/test.sh hello
```

程序可以正常执行