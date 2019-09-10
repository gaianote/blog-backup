---
title: linux 技巧：使用 screen 管理你的远程会话
author: 李云鹏
date: 2018-09-08 01:58:52
tags: linux
---

你是不是经常需要 SSH 或者 telent 远程登录到 Linux 服务器？你是不是经常为一些长时间运行的任务而头疼，比如系统备份、ftp传输等等。通常情况下我们都是为每一个这样的任务开一个远程终端窗口，因为他们执行的时间太长了。必须等待它执行完毕，在此期间可不能关掉窗口或者断开连接，否则这个任务就会被杀掉，一切半途而废了。所幸，通过使用screen命令可以有效解决这个问题。

<!--more-->

## 元凶：SIGHUP信号

让我们来看看为什么关掉窗口/断开连接会使得正在运行的程序死掉。

在Linux/Unix中，有这样几个概念：

* 进程组（process group）：一个或多个进程的集合，每一个进程组有唯一一个进程组ID，即进程组长进程的ID。
* 会话期（session）：一个或多个进程组的集合，有唯一一个会话期首进程（session                    leader）。会话期ID为首进程的ID。
* 会话期可以有一个单独的控制终端（controlling terminal）。与控制终端连接的会话期首进程叫做控制进程（controlling                    process）。当前与终端交互的进程称为前台进程组。其余进程组称为后台进程组。

根据POSIX.1定义：

* 挂断信号（SIGHUP）默认的动作是终止程序。
* 当终端接口检测到网络连接断开，将挂断信号发送给控制进程（会话期首进程）。
* 如果会话期首进程终止，则该信号发送到该会话期前台进程组。
* 一个进程退出导致一个孤儿进程组中产生时，如果任意一个孤儿进程组进程处于STOP状态，发送SIGHUP和SIGCONT信号到该进程组中所有进程。

因此当网络断开或终端窗口关闭后，控制进程收到SIGHUP信号退出，会导致该会话期内其他进程退出。

## 开始使用Screen

简单来说，Screen是一个可以在多个进程之间多路复用一个物理终端的窗口管理器。Screen中有会话的概念，用户可以在一个screen会话中创建多个screen窗口，在每一个screen窗口中就像操作一个真实的telnet/SSH连接窗口那样。在screen中创建一个新的窗口有这样几种方式：

1．直接在命令行键入screen命令

`[root@tivf06 ~]# screen`

Screen将创建一个执行shell的全屏窗口。你可以执行任意shell程序，就像在ssh窗口中那样。在该窗口中键入`exit`退出该窗口，如果这是该screen会话的唯一窗口，该screen会话退出，否则screen自动切换到前一个窗口。

2．Screen命令后跟你要执行的程序。

`[root@tivf06 ~]# screen vi test.c`

Screen创建一个执行vi test.c的单窗口会话，退出vi将退出该窗口/会话。

3．以上两种方式都创建新的screen会话。我们还可以在一个已有screen会话中创建新的窗口。在当前screen窗口中键入`C-a c`，即Ctrl键+a键，之后再按下c键，screen在该会话内生成一个新的窗口并切换到该窗口。

screen还有更高级的功能。你可以不中断screen窗口中程序的运行而暂时断开（detach）screen会话，并在随后时间重新连接（attach）该会话，重新控制各窗口中运行的程序。例如，我们打开一个screen窗口编辑/tmp/abc文件：

`[root@tivf06 ~]# screen vi /tmp/abc`
之后我们想暂时退出做点别的事情，比如出去散散步，那么在screen窗口键入`C-a d`，Screen会给出detached提示：

![img](/images/f2b550b76c3940e49621f6ffbd5fc3b0.jpg)

半个小时之后回来了，找到该screen会话：

```
[root@tivf06 ~]# screen -ls
There is a screen on:
        16582.pts-1.tivf06      (Detached)
1 Socket in /tmp/screens/S-root.
```

重新连接会话：

```
[root@tivf06 ~]# screen -r 16582
```

看看出现什么了，太棒了，一切都在。继续干吧。

你可能注意到给screen发送命令使用了特殊的键组合`C-a`。这是因为我们在键盘上键入的信息是直接发送给当前screen窗口，必须用其他方式向screen窗口管理器发出命令，默认情况下，screen接收以`C-a`开始的命令。这种命令形式在screen中叫做键绑定（key binding），`C-a`叫做命令字符（command character）。

可以通过`C-a ?`来查看所有的键绑定，常用的键绑定有：

* `C-a ?`	显示所有键绑定信息
* `C-a w`	显示所有窗口列表
* `C-a C-a`	切换到之前显示的窗口
* `C-a c`	创建一个新的运行shell的窗口并切换到该窗口
* `C-a n`	切换到下一个窗口
* `C-a p`	切换到前一个窗口(与C-a n相对)
* `C-a 0..9`	切换到窗口0..9
* `C-a a`	发送 C-a到当前窗口
* `C-a d`	暂时断开screen会话
* `C-a k`	杀掉当前窗口
* `C-a`  进入拷贝/回滚模式


## Screen常用命令


* `screen -d|-D [pid.tty.host]`	不开启新的screen会话，而是断开其他正在运行的screen会话
* `screen -h num`	指定历史回滚缓冲区大小为num行
* `screen -list|-ls`	列出现有screen会话，格式为pid.tty.host
* `screen -d -m`	启动一个开始就处于断开模式的会话
* `screen -r sessionowner/ [pid.tty.host]`	重新连接一个断开的会话。多用户模式下连接到其他用户screen会话需要指定sessionowner，需要setuid-root权限
* `screen -S sessionname`	创建screen会话时为会话指定一个名字
* `screen -v`	显示screen版本信息
* `screen -wipe [match]`	同-list，但删掉那些无法连接的会话


下例显示当前有两个处于detached状态的screen会话，你可以使用`screen -r` <screen_pid>重新连接上：

```
[root@tivf18 root]# screen –ls
There are screens on:
        8736.pts-1.tivf18       (Detached)
        8462.pts-0.tivf18       (Detached)
2 Sockets in /root/.screen.
 
[root@tivf18 root]# screen –r 8736
```

如果由于某种原因其中一个会话死掉了（例如人为杀掉该会话），这时screen -list会显示该会话为dead状态。使用screen -wipe命令清除该会话：

```
[root@tivf18 root]# kill -9 8462
[root@tivf18 root]# screen -ls  
There are screens on:
        8736.pts-1.tivf18       (Detached)
        8462.pts-0.tivf18       (Dead ???)
Remove dead screens with 'screen -wipe'.
2 Sockets in /root/.screen.
 
[root@tivf18 root]# screen -wipe
There are screens on:
        8736.pts-1.tivf18       (Detached)
        8462.pts-0.tivf18       (Removed)
1 socket wiped out.
1 Socket in /root/.screen.
 
[root@tivf18 root]# screen -ls  
There is a screen on:
        8736.pts-1.tivf18       (Detached)
1 Socket in /root/.screen.
 
[root@tivf18 root]#
```

-d –m 选项是一对很有意思的搭档。他们启动一个开始就处于断开模式的会话。你可以在随后需要的时候连接上该会话。有时候这是一个很有用的功能，比如我们可以使用它调试后台程序。该选项一个更常用的搭配是：`-dmS sessionname`

启动一个初始状态断开的screen会话：

```
[root@tivf06 tianq]# screen -dmS mygdb gdb execlp_test
```
连接该会话：

```
[root@tivf06 tianq]# screen -r mygdb
```

## 参考链接

[linux 技巧：使用 screen 管理你的远程会话](https://www.ibm.com/developerworks/cn/linux/l-cn-screen/index.html)
