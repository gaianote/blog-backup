---
title: 在ubantu16.04上搭建shadowsocks服务
date: 2018-08-15 11:48:14
tags:
---


## shadowsocks 服务器安装

更新软件源

```bash
sudo apt-get update
```

然后安装 PIP 环境

```bash
sudo apt-get install python-setuptools
sudo apt-get install python-pip
```

安装 shadowsocks

```bash
sudo pip install shadowsocks
```

## 运行 shadowsocks 服务器

### 命令行直接启动

启动命令如下：如果要停止运行，将命令中的start改成stop。

```bash
sudo ssserver -p 8388 -k password -m rc4-md5 -d start
# -p 端口
# -k 密码
# -m 加密方式
```

停止

```
sudo ssserver -d stop
```

### 使用配置文件启动

也可以使用配置文件进行配置，方法创建`/etc/shadowsocks.json`文件，填入如下内容：

```json
{
    "server":"0.0.0.0",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"rc4-md5",
    "fast_open":true
 }
```



各字段的含义：

|     字段    |                                含义                                |
|-------------|--------------------------------------------------------------------|
| server      | 服务器 IP (IPv4/IPv6)，注意这也将是服务端监听的 IP 地址            |
| server_port | 服务器端口                                                         |
| local_port  | 本地端端口                                                         |
| password    | 用来加密的密码                                                     |
| timeout     | 超时时间（秒）                                                     |
| method      | 加密方法，可选择 “bf-cfb”, “aes-256-cfb”, “des-cfb”, “rc4″, 等等。 |

> 加密方式推荐使用rc4-md5，因为 RC4 比 AES 速度快好几倍，如果用在路由器上会带来显著性能提升。旧的 RC4 加密之所以不安全是因为 Shadowsocks 在每个连接上重复使用 key，没有使用 IV。现在已经重新正确实现，可以放心使用。更多可以看 issue。

如果需要配置多个用户,可以这样来设置:

```json
{
    "server":"my_server_ip",
    "port_password": {
        "端口1": "密码1",
        "端口2": "密码2"
        },
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": true
}
```

然后使用配置文件在后台运行：

```
sudo ssserver -c /etc/shadowsocks.json -d start
```

## 配置开机自启动

1. 编辑 /etc/rc.local 文件

```
sudo vi /etc/rc.local
```

2. 在 exit 0 这一行的上边加入如下

```
/usr/local/bin/ssserver –c /etc/shadowsocks.json
```

或者 不用配置文件 直接加入命令启动如下：

```
/usr/local/bin/ssserver -p 8388 -k password -m aes-256-cfb -d start
```

到此重启服务器后，会自动启动。

# TCP BBR 魔改版 for Debian/Ubuntu

BBR 是来自 Google 的一个 TCP 拥塞控制算法，单边加速，可以提升你的网络利用率。


## 安装

### 确认你可以使用 BBR

直接运行以下命令即可：

```
wget --no-check-certificate -qO 'BBR.sh' 'https://moeclub.org/attachment/LinuxShell/BBR.sh' && chmod a+x BBR.sh && bash BBR.sh -f
```

脚本会自动安装并重启

此脚本运行时会自动选择最新的**非rc版本**（非候选发布版）内核进行安装，并且自动卸载旧内核（无需人工干预）。
安装完成后，执行以下命令：

```
lsmod | grep 'bbr'
```

**如果结果不为空，则说明成功开启了 BBR，那么你就可以使用后续的 BBR 加强版。**


### 安装 BBR 魔改版

```
wget --no-check-certificate -qO 'BBR_POWERED.sh' 'https://moeclub.org/attachment/LinuxShell/BBR_POWERED.sh' && chmod a+x BBR_POWERED.sh && bash BBR_POWERED.sh
```

执行过程中会重新编译模块，等待完成即可。

安装完成后执行

```
lsmod | grep 'bbr_powered'
```

如果结果不为空，则说明成功开启了 BBR 加强版。

## 网络测试

从下面的测试结果来看，安装bbr魔改版效果比较好

### 测试方法

秉承着怎么方便怎么来的做法，我在`CentOS 6.9`系统下进行`什么都不装`和`锐速`的网络测试，在`Ubuntu 16.04`下进行`BBR`和`BBR魔改`的网络测试

网络测试有两部分：

* 使用`ZBench-CN.sh`进行测试
* 在`深圳天威联通100M`网络环境下进行H5网页测速

用到的代码：

```python
# CentOS 6.9 锐速
wget --no-check-certificate -O appex.sh https://raw.githubusercontent.com/0oVicero0/serverSpeeder_Install/master/appex.sh && chmod +x appex.sh && bash appex.sh install '2.6.32-642.el6.x86_64'
# Ubuntu/Debian BBR
wget --no-check-certificate -qO 'BBR.sh' 'https://moeclub.org/attachment/LinuxShell/BBR.sh' && chmod a+x BBR.sh && bash BBR.sh -f
# Ubuntu/Debian BBR魔改
wget --no-check-certificate -qO 'BBR_POWERED.sh' 'https://moeclub.org/attachment/LinuxShell/BBR_POWERED.sh' && chmod a+x BBR_POWERED.sh && bash BBR_POWERED.sh
# ZBench-CN.sh 测速脚本
wget https://raw.githubusercontent.com/FunctionClub/ZBench/master/ZBench-CN.sh && bash ZBench-CN.sh
# Docker 一键安装脚本
wget -qO- https://get.docker.com/ | sh
# H5网页测速 Docker
docker run -d -p 2333:80 ilemonrain/html5-speedtest:latest
```

### 测试结果

### Vultr 日本（低延迟低丢包）

#### H5网页测速

* 什么都不装
![img](/images/7e93dcf93d7c4efc95f4061e4152a9b2.png)
* 锐速
![img](/images/49a246c846a043aa9a93ea88d347f3ac.png)
* BBR
![img](/images/5fc62db8e775484b82c649854c905c43.png)
* BBR魔改
![img](/images/c4c0bbae2fa54a218af9f86fbb920632.png)

#### 测速脚本

* 什么都不装
![img](/images/4ff82c1dbdd74d6f9a1e07680d3591b2.png)

* 锐速
![img](/images/bbb9650d89644eab8e1532b26852d986.png)

* BBR
![img](/images/19c7638430344fcda27fa4814c358a83.png)
* BBR魔改
![img](/images/7317fa2ca53646639dcb0c513615228a.png)


## 参考链接

[[小实验] 锐速&BBR究竟哪家强？个人PC有必要上锐速吗？](https://lolico.moe/gotagota/compare-serverspeeder-and-bbr.html)