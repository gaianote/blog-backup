---
title: OSI模型
date: 2018-08-24 10:20:04
tags: 网络原理
---

## 层次划分

根据建议X.200，OSI将计算机网络体系结构划分为以下七层，标有1～7，第1层在底部。现“OSI/RM”是[英文](https://zh.wikipedia.org/wiki/%E8%8B%B1%E6%96%87)“Open Systems Interconnection Reference Model”的缩写。

### 第7层 应用层

[应用层](https://zh.wikipedia.org/wiki/%E5%BA%94%E7%94%A8%E5%B1%82)（Application Layer）提供为应用软件而设的接口，以设置与另一应用软件之间的通信。例如: HTTP，HTTPS，FTP，TELNET，SSH，SMTP，POP3等。

### 第6层 表达层

[表达层](https://zh.wikipedia.org/wiki/%E8%A1%A8%E9%81%94%E5%B1%82)（Presentation Layer）把数据转换为能与接收者的系统格式兼容并适合传输的格式。

### 第5层 会话层

[会话层](https://zh.wikipedia.org/wiki/%E4%BC%9A%E8%AF%9D%E5%B1%82)（Session Layer）负责在数据传输中设置和维护计算机网络中两台计算机之间的通信连接。

### 第4层 传输层

[传输层](https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%BE%93%E5%B1%82)（Transport Layer）把传输表头（TH）加至数据以形成数据包。传输表头包含了所使用的协议等发送信息。例如:传输控制协议（TCP）等。

### 第3层 网络层

[网络层](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E5%B1%82)（Network Layer）决定数据的路径选择和转寄，将网络表头（NH）加至数据包，以形成分组。网络表头包含了网络数据。例如:互联网协议（IP）等。

### 第2层 数据链路层

[数据链路层](https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E9%93%BE%E8%B7%AF%E5%B1%82)（Data Link Layer）负责网络寻址、错误侦测和改错。当表头和表尾被加至数据包时，会形成帧。数据链表头（DLH）是包含了物理地址和错误侦测及改错的方法。数据链表尾（DLT）是一串指示数据包末端的字符串。例如以太网、无线局域网（Wi-Fi）和通用分组无线服务（GPRS）等。

分为两个子层：逻辑链路控制（logic link control，LLC）子层和介质访问控制（media access control，MAC）子层。

### 第1层 物理层

[物理层](https://zh.wikipedia.org/wiki/%E7%89%A9%E7%90%86%E5%B1%82)（Physical Layer）在局部局域网上传送[数据帧](https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%B8%A7)（data frame），它负责管理计算机通信设备和网络媒体之间的互通。包括了针脚、电压、线缆规范、集线器、中继器、网卡、主机适配器等。

## ping与shadowsocks代理

ip协议在OSI模型的第3层（网络层）工作，SOCKS协议在第5层（会话层）工作，http协议在第7层（应用层）工作。ping消息不能通过SOCKS传递，但http消息可以。
因此如果使用shadowsocks(socks5)代理上网的话,`ping google.com`无法ping通,但是可以正常上网(http/https)

如果坚持要能Ping通才行，需要使用常规VPN（PPTP/L2PT/IPSec等)