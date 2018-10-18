title: 在ubantu16.04上搭建shadowsocks服务
date: 2018-08-15 11:48:14
tags:
---
以前我们科学上网的时候最常用的就是vpn了，而2年前，ss被开源(ss出现一年后，开源社区的破娃小姐姐在ss的基础上发布了ssr)，现在已经是最流行的科学上网方案。



<!--more-->

## vpn与shadowsocks

### 什么是vpn

在很多人心目中就是用来翻墙的工具，其实不是。vpn最主要的功能，并不是用来翻墙，只是它可以达到翻墙的目的。

vpn指虚拟专用网络，它的功能是：在公用网络上建立专用网络，进行加密通讯。在企业网络和高校的网络中应用很广泛。你接入vpn，其实就是接入了一个专有网络，你的网络访问都从这个出口出去，你和vpn之间的通信是否加密，取决于你连接vpn的方式或者协议。



### ss与ssr

ss作者是clowwindy，大约两年前，他自己为了翻墙写了shadowsocks，简称ss或者叫影梭，后来他觉得这个东西非常好用，速度快，而且不会被封锁，他就把源码共享在了github上，然后就火了，但是后来作者被请去喝茶，删了代码，并且保证不再参与维护更新。现在这个好像是一个国外的大兄弟在维护。

ssr：在ss作者被喝茶之后，github上出现了一个叫breakwa11(破娃)的帐号，声称ss容易被防火墙检测到，所以在混淆和协议方面做了改进，更加不容易被检测到，而且兼容ss，改进后的项目叫shadowsocks-R，简称ssr，然后ss用户和ssr用户自然分成了两个派别，互相撕逼，直到前阵子，破娃被人肉出来，无奈之下删除了ssr的代码，并且解散了所有相关群组。

ss和ssr它的原理都是一样的，就是socks5代理。socks代理只是简单的传递数据包，而不必关心是何种协议，所以socks代理比其他应用层代理要快的多。socks5代理是把你的网络数据请求通过一条连接你和代理服务器之间的通道，由服务器转发到目的地，这个过程中你是没有通过一条专用通道的，只是数据包的发出，然后被代理服务器收到，整个过程并没有额外的处理。通俗的说，现在你有一个代理服务器在香港，比如你现在想要访问google，你的电脑发出请求，流量通过socks5连接发到你在香港的服务器上，然后再由你在香港的服务器去访问google，再把访问结果传回你的电脑，这样就实现了翻墙。

直连模式就是流量不走代理 ，PAC模式简单说就是国内地址不走代理，国外走代理，全局模式就是不管国内国外，所有流量通过代理服务器访问


![img](/images/2748df9aff684540b2bf54c77322b0d2.png)

### vpn和ss/ssr的区别和优缺点

通过上面的介绍，其实基本已经能看出vpn和ss/ssr的区别了，那么他们到底孰优孰劣。

因为vpn是走的专用通道，它是用来给企业传输加密数据用的，所以vpn的流量特征很明显，以openvpn为例，更详细的在这里不说了，流量特征明显，防火墙直接分析你的流量，如果特征匹配，直接封掉。目前就翻墙来说，PPTP类型的vpn基本死的差不多了，L2TP大部分地区干扰严重很不稳定。

ss/ssr的目的就是用来翻墙的，而vpn的目的是用来加密企业数据的，对于vpn来说安全是第一位的，而对于ss/ssr来说穿透防火墙是第一位，抗干扰性强，而且对流量做了混淆，所有流量在通过防火墙的时候，基本上都被识别为普通流量，也就是说你翻墙了，但是政府是检测不到你在翻墙的。两者的出发点和着重点就不同，ss/ssr更注重流量的混淆加密。如果要安全匿名上网，可以用vpn+tor或者ss/ssr+tor。

而安全性方面还要补充的一点就是，国内vpn服务商，政府是很容易拿到他们的服务器日志的，如果他们真的这样做了，你翻墙做了什么，一览无余

## 云主机提供商[Vultr](https://www.vultr.com/?ref=7507302)

[Vultr](https://www.vultr.com/?ref=7507302)官网是一家提供日本、美国、欧洲等多个国家和地区机房的VPS主机商，硬盘都是采用SSD，VPS主机都是KVM架构，VPS配置最少的内存512MB、硬盘为15GB的VPS只要2.5美元/月，vultr是根据VPS使用小时来计费（0.007/h,折合人民币4分6/小时）的，使用多长时间就算多长时间，计费对应的款。Vultr是KVM系统架构，目前已开通15个机房，比较适合国内的是日本东京（tokyo）,美国洛杉矶（ Los Angeles ），美国西雅图（ Seattle ）这三个机房相对国内线路较好。vultr支持支付宝（Alipay）付费使用。

使用要点：

1. Vultr注册时的邮箱必须是真实有效的，后续开通主机需要验证邮箱
2. 不要选择2.5美元/月的主机，这个主机只支持ipv6，目前大部分网站和网络运营商都是不支持的
3. 通过[http://www.pingms.com/](http://www.pingms.com/)查看各个云主机到本地的延迟，东京一般情况是延迟最低的

## shadowsocks 服务器安装

首先选择os版本 ubantu16.04 , 本文是根据这个系统及版本部署的。

1. 更新软件源

```bash
sudo apt-get update
```

2. 然后安装 PIP 环境

```bash
sudo apt-get install python-setuptools
sudo apt-get install python-pip
```

3. 安装 shadowsocks

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

### ipv6的支持

#### VPS 开启 IPv6

以 Vultr 为例，其他 VPS 类似。

**1.已创建 VPS 开启 IPv6**

进入控制面板，选择 “Settings” ——> “IPv6” ——> “Assign Ipv6 Network” ，然后重启 VPS 即可。

![img](/images/e693fc58a0534b37b3038e3bd2bd11d9.png)

**2.新创建VPS开启IPv6**

在创建 VPS 时，在第四项的 “Enable IPv6” 前打勾即可创建一个开启 IPv6 的机器。

![img](/images/01475e08e091470b854ea40a92f1b88a.png)

**3. 开启后同样前往 “Settings” 的 “IPv6” 中即可查看到 IPv6 地址。**

#### SS 配置 IPv6 支持

打开 SS 配置文件

vi /etc/shadowsocks.json|1|vi/etc/shadowsocks.json|

编辑配置文件，使 ss 支持 IPv4 和 IPv6 地址

```json
{
 "server":"::",      //同时支持 IPv4 和 IPv6
 "port_password": "mypassword",
 // ...
}
```

`Esc`，输入 `:wq` 保存退出。重启 SS 即可。

#### 客户端设置

客户端的设置和以前一样，只不过把 IP 地址改为 IPv6 的地址即可。

在使用时，可以先用 IPv4 的地址进行测试，看能不能上 Google 等，如果正常，再换位 IPv6 的地址进行测试。

要先查看自己的网络是否支持 IPv6，右键任务栏“win10设置” ——> “网络和Internet”——> “以太网” ——>“打开网络共享中心” ，点击 “宽带连接”（拨号上网）或 “以太网”（路由器上网），查看网络状态，看 IPv6 是否有 Internet 连接。

没有的话可以点击下面的“属性” ——> “网络”，查看是否勾选 “IPv6” Internet 协议，一般如果已经勾选，网络支持 IPv6 会自动启用，如果勾选了 IPv6 仍不可用，可以咨询运营商是否支持。不支持的话就没办法了。

![img](/images/4186c069f84744a0b50b242341cc5547.png)

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



## 安装 TCP BBR

BBR 是来自 Google 的一个 TCP 拥塞控制算法，单边加速，可以提升你的网络利用率。

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


### 修改/关闭bbr方法

1. 使用root用户登录，运行以下命令：

```
vim /etc/sysctl.conf
```
2. 删除或注释掉其中的两行：

```
# net.core.default_qdisc = fq           用#注释掉
# net.ipv4.tcp_congestion_control = bbr 用#注释掉
```
3. 执行命令：

```
sysctl -p
```
最后重启服务器生效！

## 客户端

### 下载

ios客户端：搜索windy，需要日区的apple id，因为中国区没有上架，日区美区都可以
pc以及其它客户端: 建议到[shadowsocks.org](https://shadowsocks.org/en/download/clients.html)进行下载，或者[github](https://github.com/shadowsocks/shadowsocks-windows/releases)进行下载

### 使用

#### **电脑**

打开客户端，将上面记录的相应连接信息填入客户端，确定。

![img](/images/bac8537dba3f474dac3c4f0c480636db.png)
右键任务栏托盘小飞机图标，“启动”，可以选择合适的代理模式。

* **PAC**：只代理国外网站；
* **全局**：所有网站都通过SS。

![img](/images/4c3d5ea3154042739da3ae1d65e79e86.png)
其它系统客户端的设置基本如此

## 网络测试

对我而言还是推荐bbr的加速方式

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
[Vpn与ss/ssr的区别](https://deeponion.org/community/threads/vpnss-ssr.901/)
[vultr-vps-搭建-shadowsocks（ss）教程（新手向）](https://go2think.com/%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%EF%BC%9Avultr-vps-%E6%90%AD%E5%BB%BA-shadowsocks%EF%BC%88ss%EF%BC%89%E6%95%99%E7%A8%8B%EF%BC%88%E6%96%B0%E6%89%8B%E5%90%91%EF%BC%89/)