---
title: python获取本机IP、mac地址、计算机名
date: 2017-05-11 14:36:20
tags: python
---

在Python中获取ip地址和在PHP中有很大不同，在php中往往比较简单。那再python中怎么做呢？
我们先来看一下python 获得本机MAC地址：

```python
import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
```

下面再来看一下python获取IP的方法：使用socket

```python
import socket
#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)
print myname
print myaddr
```

## 在linux下可用

```python
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

get_ip_address('lo')
# '127.0.0.1'

get_ip_address('eth0')
# '38.113.228.130'

get_ip_address('ppp0')
# '123.163.166.00'
```
