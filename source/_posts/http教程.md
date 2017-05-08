---
title: http教程
date: 2017-05-08 10:59:54
tags: http
---
## HTTP教程

HTTP协议（HyperText Transfer Protocol，超文本传输协议）是因特网上应用最为广泛的一种网络传输协议，所有的WWW文件都必须遵守这个标准。
HTTP是一个基于TCP/IP通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。

## HTTP消息结构

客户端请求消息

客户端发送一个HTTP请求到服务器的请求消息包括以下格式：请求行（request line）、请求头部（header）、空行和请求数据四个部分组成
HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文

客户端请求：

```
GET /hello.txt HTTP/1.1
User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3
Host: www.example.com
Accept-Language: en, mi
```

服务端响应:

```
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Content-Type: text/plain
```

## HTTP请求方法

根据HTTP标准，HTTP请求可以使用多种请求方法。

HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法。
HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。

- `GET` 请求指定的页面信息，并返回实体主体。
- `HEAD`  类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
- `POST`  向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
- `PUT` 从客户端向服务器传送的数据取代指定的文档的内容。
- `DELETE`  请求服务器删除指定的页面。
- `CONNECT` HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
- `OPTIONS` 允许客户端查看服务器的性能。
- `TRACE` 回显服务器收到的请求，主要用于测试或诊断。
