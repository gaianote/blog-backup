title: 5个 Curl 命令下载文件
author: 李云鹏
date: 2019-01-03 19:05:07
tags:
---
curl命令文件工具支持下载和上传文件。Curl是系统管理使用于很多的工作中，网络开发调用Web服务等。在本教程中，我们提供了5个Curl经常使用的命令，从远程服务器下载文件非常有用。

1. curl命令来下载和保存文件
为了简单地下载使用以下语法Curl使用的文件。 -O用于在本地系统上保存文件，远程系统上相同的名称。
```
$ curl -O http://example.com/download/myfile.zip
```

2. Curl下载并保存其他名称
如果你想保存在本地系统上不同的名字文件，请使用-o用新的文件名。
```
$ curl -o localname.zip http://example.com/download/myfile.zip
```
3. Curl下载多个文件
Curl还提供了选项，同时下载多个文件。要下载多个文件使用以下语法。所有文件将与原文件名保存。
```
$ curl -O http://example.com/myfile.zip -O http://example.com/myfile2.zip
```
4. 传递登录凭证与Curl下载
如果文件被后面验证HTTP或FTP服务器。你可以通过登录使用像下面的例子-u命令行参数的凭据。
```
$ curl -u user:password -O http://example.com/myfile.zip
$ curl -u ftpuser:ftppassword -O ftp://ftp.example.com/myfile.zip
```
5. 通过Curl代理服务器下载文件
如果服务器上的文件只能通过代理服务器，或者你要使用代理下载文件，使用-x其次是代理服务器地址和端口，通过代理服务器来下载文件。
```
$ curl -x my.proxy.com:3128 -O http://example.net/myfile.zip$ 