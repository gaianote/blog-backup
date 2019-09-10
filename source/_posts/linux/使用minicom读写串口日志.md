---
title: 使用minicom管理串口
tags: linux
date: 2019-01-17 02:45:03
---

## 1. minicom简介

### 1. 安装

minicom是linux下一款常用的串口调试工具。ubuntu环境下，使用如下命令安装

```
sudo apt-get install minicom
```

### 2. 配置

使用前需要进行配置，执行

```bash
sudo minicom -s
```

可打开minicom并进入配置模式，使用方向键，选择需要配置的项目，如 **Serial port setup** ，回车进入配置，可以看到多个配置项，此时光标在最下方。

需要修改某个配置，则输入对应的字母，光标即会跳转到对应的项，编辑后，回车确认，光标再次回到最下方。

一般而言，需要修改

```
A -    Serial Device
E -    Bps/Par/Bits
F -    Hardware Flow Control
```

A配置项，指定USB设备。一般USB转串口会生成设备/dev/ttyUSBx，x是数字序号。可以执行以下命令确认下

```bash
ls -l /dev/ttyUSB*
```

E配置项，根据实际情况，指定波特率等参数

F配置项，硬件流控，要看你的设备是否有。如果没有，或者你不确定的话，可以先关掉，将默认的Yes切换为No.

修改好之后，回车退到上一个界面，此时记得往下，选择 **Save setup as dfl** 将刚刚的修改保存为默认配置，避免下次使用还需要再次配置。

最后，选择 **Exit** 会退出配置界面，并打开minicom。选择 **Exit from Minicom** 则会直接退出minicom。



### 3. 退出

minicom使用前缀按键 `Ctrl-A`，即执行特殊操作时，都需要先按 `Ctrl+A`，再按某个按键使用对应的功能。

`Ctrl+A`，再按 Z， 可查看帮助，从帮助可以看到，退出时，要先按` Ctrl+A`，再按` X`



## 2. 配置权限

minicom 本身不需要sudo权限，但因为要打开串口设备/dev/xxx ，所以一般会需要使用sudo来启动minicom。

这里我们可以修改下串口设备的权限，这样以后就不用使用sudo了。



### 1. 使用命令更改

简单粗暴地使用chmod命令修改

```
sudo chmod 666 /dev/ttyUSB0
```



### 2. 配置udev规则(推荐)

修改配置文件

```
sudo vim /etc/udev/rules.d/70-ttyusb.rules
```

增加一行

```
KERNEL=="ttyUSB[0-9]*", MODE="0666"
```

修改后，需要重新插拔设备，以重新生成设备节点。



## 3. 自动设置设备名

如果日常只用一个设备，设备名固定是/dev/ttyUSB0，那每次直接打开minicom即可。

但当你可能需要使用多个串口时，问题就来了，每次需要先查看下设备名

```
ls /dev/ttyUSB* 
```

再配置下minicom，手工改成这个设备，才能使用。一点都不方便。因此推荐使用命令行的方式实现设置

### 1. 使用参数指定设备

研究下mincom的参数后，发现有更简单的实现方式，使用minicom的-D参数。

同样编写脚本~/.myminicom.sh

```
com() {
    ports_USB=$(ls /dev/ttyUSB*)
    ports_ACM=$(ls /dev/ttyACM*)  #arduino
    ports="$ports_USB $ports_ACM"
    select port in $ports;do
        if [ "$port" ]; then
            echo "You select the choice '$port'"
            minicom -D "$port" $@"
            break
        else
            echo "Invaild selection"
        fi
    done
}
```

在~/.bashrc中引入此函数

```
echo 'source ~/.myminicom.sh' >> ~/.bashrc
source ~/.bashrc
```

添加完毕后，可使用 **com** 命令调用。

### 2. 使用效果

```
zhuangqiubin@zhuangqiubin-PC:~$ com
1) /dev/ttyUSB0
2) /dev/ttyUSB1
#?
```

此时输入数字，选择要的打开的串口设备，回车即可。



## 4. 自动保存log

让 minicom 自动保存log，可以方便调试。

查看参数，minicom可以使用 -C 参数指定保存log文件。于是完善脚本，自动把log以日期命名，保存到/tmp目录下。

注意，tmp目录关机即清空，如果想持久保存log，需要修改到其他目录。

修改后脚本如下

```
com() {
    ports_USB=$(ls /dev/ttyUSB*)
    ports_ACM=$(ls /dev/ttyACM*)  #arduino
    ports="$ports_USB $ports_ACM"
    datename=$(date +%Y%m%d-%H%M%S)
    select port in $ports;do
        if [ "$port" ]; then
            echo "You select the choice '$port'"
            minicom -D "$port" -C /tmp/"$datename".log "$@"
            break
        else
            echo "Invaild selection"
        fi
    done
}
com
```



## 5. 暂停输出

Ctrl+A 是mimicom的特殊功能前缀按键，但还有另一个很实用的作用，就是暂停屏幕输出。

在设备开始大量输出log时，基本看不清屏幕内容。此时可以按 Ctrl+A，暂停输出，方便查看所需log。



## 6. 打开minicom时间戳

在minicom中，按下 Ctrl+A，再按 N，即可激活时间戳，在每行log前添加当前系统的时间戳。

用于观察启动时间之类的，还是比较方便。



## 7. 发送接收文件

设备端支持的话，按下 Ctrl+A，再按 S，即可向设备端发送文件。

按 Ctrl+A，再按 R，可接收文件。



## 8. 自动换行

当你的log中可能存在，单行长度超过屏幕宽度的log时（比如启动时打印的kernel cmdline），可以使用mimicom的自动换行功能。

在启动minicom时加上 -w 选项，或者在minicom中，按 Ctrl+A 再按 W。



## 9. 更多功能

可以使用 minicom -h 查看，也可在mincon中，按 Ctrl+A 再按 Z 查看。

有什么其他使用功能或技巧，也欢迎留言告诉我。



## 源码

文中的代码非最新版本，请访问 <https://github.com/zqb-all/EasierMinicom> 获取带有更多功能的最新版本。

如果觉得本文对你有帮助的的话，顺手点下推荐哦～～