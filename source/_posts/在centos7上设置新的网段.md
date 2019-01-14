title: 在centos7上设置新的网段
author: 李云鹏
date: 2019-01-10 09:30:20
tags:
---
本机的ip地址是192.168.71.192，无法ping通192.168.72网段的服务器，因为，需要给服务器设置新的网段。

**1. 列出所有的网卡和虚拟网卡**

```bash
[root@localhost test_control_center]# ip a
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
3: em2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN qlen 1000
    link/ether 20:04:0f:eb:cd:99 brd ff:ff:ff:ff:ff:ff
    inet 172.10.13.104/24 brd 172.10.13.255 scope global em2
       valid_lft forever preferred_lft forever
    inet6 fe80::261f:1d55:543e:a107/64 scope link tentative
       valid_lft forever preferred_lft forever
4: em3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN qlen 1000
    link/ether 20:04:0f:eb:cd:9a brd ff:ff:ff:ff:ff:ff
5: em4: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN qlen 1000
    link/ether 20:04:0f:eb:cd:9b brd ff:ff:ff:ff:ff:ff
6: p3p1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 6c:b3:11:3c:48:d8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.3.192/24 brd 192.168.3.255 scope global p3p1
       valid_lft forever preferred_lft forever
    inet6 fe80::a123:12d8:ad76:86f8/64 scope link
       valid_lft forever preferred_lft forever
7: p3p2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN qlen 1000
    link/ether 6c:b3:11:3c:48:da brd ff:ff:ff:ff:ff:ff
8: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN
    link/ether 02:42:a8:ce:0c:5d brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
9: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN qlen 1000
    link/ether 52:54:00:f8:45:a9 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
       valid_lft forever preferred_lft forever
10: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN qlen 1000
    link/ether 52:54:00:f8:45:a9 brd ff:ff:ff:ff:ff:ff
```
由于本机ip地址是192.168.71.192，由此可知，网卡为em1

**2. 复制虚拟网卡**

```bash
[root@localhost test_control_center]# cd /etc/sysconfig/network-scripts/
[root@localhost network-scripts]# ls
ifcfg-em1 ifcfg-em1:0  ifcfg-lo  ifdown-bnep  ifdown-ipv6  ifdown-routes ...
[root@localhost network-scripts]# cp  ifcfg-em1:0 ifcfg-em1:1
[root@localhost network-scripts]# ls
ifcfg-em1 ifcfg-em1:0  ifcfg-em1:1 ifcfg-lo  ifdown-bnep  ifdown-ipv6 ...
```
**3. 编辑复制好的虚拟网卡**

修改DEVICE和新的ip地址

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