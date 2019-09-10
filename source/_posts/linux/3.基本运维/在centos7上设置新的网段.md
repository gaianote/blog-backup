---
title: 在centos7上设置新的网段
author: 李云鹏
date: 2019-01-10 09:30:20
tags: linux
---



## 1. eth0 eth0:1 和eth0.1三者的关系

eth0 eth0:1 和eth0.1三者的关系分别对应于物理网卡、子网卡、虚拟VLAN网卡的关系：

1. **物理网卡**：物理网卡这里指的是服务器上实际的网络接口设备，这里我服务器上双网卡，在系统中看到的2个物理网卡分别对应是eth0和eth1这两个网络接口。

2. **子网卡**：子网卡在这里并不是实际上的网络接口设备，但是可以作为网络接口在系统中出现，如eth0:1、eth1:2这种网络接口。它们必须要依赖于物理网卡，虽然可以与物理网卡的网络接口同时在系统中存在并使用不同的IP地址，而且也拥有它们自己的网络接口配置文件。但是当所依赖的物理网卡不启用时（Down状态）这些子网卡也将一同不能工作。

3. **虚拟VLAN网卡**：这些虚拟VLAN网卡也不是实际上的网络接口设备，也可以作为网络接口在系统中出现，但是与子网卡不同的是，他们没有自己的配置文件。他们只是通过将物理网加入不同的VLAN而生成的VLAN虚拟网卡。如果将一个物理网卡通过vconfig命令添加到多个VLAN当中去的话，就会有多个VLAN虚拟网卡出现，他们的信息以及相关的VLAN信息都是保存在/proc/net/vlan/config这个临时文件中的，而没有独自的配置文件。它们的网络接口名是eth0.1、eth1.2这种名字。

注意：当需要启用VLAN虚拟网卡工作的时候，关联的物理网卡网络接口上必须没有IP地址的配置信息，并且，这些主物理网卡的子网卡也必须不能被启用和必须不能有IP地址配置信息。这个在网上看到的结论根据我的实际测试结果来看是不准确的，物理网卡本身可以绑定IP，并且给本征vlan提供通信网关的功能，但必须是在802.1q下。



## 2. /sbin/ifconfig 查看、配置、启用或禁用网络接口（网卡）的工具

ifconfig 是一个用来查看、配置、启用或禁用网络接口的工具，这个工具极为常用的。比如我们可以用这个工具来配置网卡的IP地址、MAC地址、掩码、广播地址等。

值得一说的是用ifconfig 为网卡指定IP地址，**这只是用来调试网络用的，并不会更改系统关于网卡的配置文件**。服务器每次重启后，配置都会消失。

### 1. ifconfig配置网络接口语法：

```
ifconfig 网络端口 IP地址 hw MAC地址 netmask 掩码地址 broadcast 广播地址 [up/down]
```

### 2. ifconfig常用用法：

- `ifconfig` ： 查看主机激活状态的网络接口情况； 输出结果中：lo 是表示主机的回坏地址，eth0 表示第一块网卡， 其中 HWaddr 表示网卡的物理地址（MAC地址）； inet addr 用来表示网卡的IP地址，Bcast表示广播地址，Mask表示掩码地址
- `ifconfig -a` ： 查看主机所有（包括没有被激活的）网络接口的情况
- `ifconfig eth0` ： 查看特定网络接口的状态
- `ifconfig eth0 down = ifup eth0` ： 如果eth0是激活的，就把它终止掉。此命令等同于 ifdown eth0；
- `ifconfig eth0 up = ifdown eth0` ： 激活eth0 ； 此命令等同于 ifup eth0
- `ifconfig eth0 192.168.1.99 broadcast 192.168.1.255 netmask 255.255.255.0` ： 配置 eth0的IP地址、广播地址和网络掩码；
- `ifconfig eth0 192.168.1.99 broadcast 192.168.1.255 netmask 255.255.255.0 up` ： 配置IP地址、网络掩码、广播地址的同时，激活网卡eth0
- `ifconfig eth1 hw ether 00:11:00:00:11:22` ： 设置网卡的物理地址（MAC地址）。其中 hw 后面所接的是网络接口类型， ether表示以太网， 同时也支持 ax25 、ARCnet、netrom等，详情请查看 man ifconfig ；

虚拟IP技术在高可用领域像数据库SQLSERVER、web服务器等场景下使用很多，很疑惑它是怎么实现的，偶然，发现了一种方式可以实现虚拟ip。它的原理在于同一个物理网卡，是可以拥有多个ip地址的，至于虚拟网卡，也可用通过该方式拥有多个ip。  即对外提供数据库服务器的主机除了有一个真实IP外还有一个虚IP，使用这两个IP中的 任意一个都可以连接到这台主机，所有项目中数据库链接一项配置的都是这个虚IP，当服务器发生故障无法对外提供服务时，动态将这个虚IP切换到备用主机。

其实现原理主要是靠TCP/IP的ARP协议。因为ip地址只是一个逻辑地址，在以太网中MAC地址才是真正用来进行数据传输的物理地址，每台主机中都有一个ARP高速缓存，存储同一个网络内的IP地址与MAC地址的对应关系，以太网中的主机发送数据时会先从这个缓存中查询目标IP对应的MAC地址，会向这个MAC地址发送数据。操作系统会自动维护这个缓存。这就是整个实现 的关键。

在eth0处引用别名，设置完子网掩码即可

```bash
$ ifconfig eth0:0 166.111.69.100 netmask 255.255.255.0 up
```

此时查看网卡信息

```bash
eth0 Link encap:Ethernet HWaddr 08:00:27:64:59:11
          inet addr:166.111.69.17 Bcast:166.111.69.255 Mask:255.255.255.0
          inet6 addr: 2402:f000:1:4412:a00:27ff:fe64:5911/64 Scope:Global
          inet6 addr: fe80::a00:27ff:fe64:5911/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
          RX packets:597673 errors:0 dropped:0 overruns:0 frame:0
          TX packets:215472 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:67285933 (67.2 MB) TX bytes:22782158 (22.7 MB)

eth0:0 Link encap:Ethernet HWaddr 08:00:27:64:59:11
          inet addr:166.111.69.100 Bcast:166.111.69.255 Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1

lo Link encap:Local Loopback
          inet addr:127.0.0.1 Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING MTU:16436 Metric:1
          RX packets:843 errors:0 dropped:0 overruns:0 frame:0
          TX packets:843 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:67174 (67.1 KB) TX bytes:67174 (67.1 KB)
```

然后找另一台机器ping这个vip(eth0:0)就可以看到显示结果了。
写在`/etc/rc.local`里也可以，写在这里就不怕断电后机器无法正常使用了。

### 3. 用ifconfig 来配置虚拟网络接口：

有时我们为了满足不同的需要还需要配置虚拟网络接口，比如我们用不同的IP地址来架运行多个HTTPD服务器，就要用到虚拟地址；这样就省却了同一个IP地址，如果开设两个的HTTPD服务器时，要指定端口号。

虚拟网络接口指的是为一个网络接口指定多个IP地址，虚拟接口是这样的 eth0:0 、 eth0:1、eth0:2 ... .. eth1N。当然您为eth1 指定多个IP地址，也就是 eth1:0、eth1:1、eth1:2 ... ...以此类推；

```bash
ifconfig eth1:0 192.168.1.250 hw ether 00:11:00:00:11:44 netmask 255.255.255.0 broadcast 192.168.1.255 up
ifconfig eth1:1 192.168.1.249 hw ether 00:11:00:00:11:55 netmask 255.255.255.0 broadcast 192.168.1.255 up
ifconfig eth1:3 192.168.1.251
```
注意：指定时，要为每个虚拟网卡指定不同的物理地址；

## 3.持久化的设置网段

本机的ip地址是192.168.71.192，无法ping通192.168.72网段的服务器，因为，需要给服务器设置新的网段。

**1. 列出所有的网卡和虚拟网卡**

```bash
$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: em1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 20:04:0f:eb:cd:98 brd ff:ff:ff:ff:ff:ff
    inet 192.168.71.192/24 brd 192.168.71.255 scope global em1
       valid_lft forever preferred_lft forever
    inet 172.10.3.192/24 brd 172.10.3.255 scope global em1:0
       valid_lft forever preferred_lft forever
    inet6 fe80::ba64:d3bb:4896:90b1/64 scope link
       valid_lft forever preferred_lft forever
.....
```
由于本机ip地址是192.168.71.192，由此可知，网卡为em1

**2. 复制虚拟网卡**

```bash
$ cd /etc/sysconfig/network-scripts/
$ ls
ifcfg-em1 ifcfg-em1:0  ifcfg-lo  ifdown-bnep  ifdown-ipv6  ifdown-routes ...
$ cp  ifcfg-em1:0 ifcfg-em1:1
$ ls
ifcfg-em1 ifcfg-em1:0  ifcfg-em1:1 ifcfg-lo  ifdown-bnep  ifdown-ipv6 ...
```
**3. 编辑复制好的虚拟网卡**

修改DEVICE和新的ip地址，注意修改`DEVICE`和`IPADDR`

```bash
[root@localhost network-scripts]# vim ifcfg-em1:1
DEVICE=em1:1
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.72.192
NETMASK=255.255.255.0
#GATEWAY=
```
**4. 重启网络服务**
```
[root@localhost network-scripts]# systemctl restart network
```