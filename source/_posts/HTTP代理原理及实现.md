---
title: HTTP代理原理及实现
date: 2017-05-08 10:02:14
tags:
---

## 普通代理服务器

普通代理服务器充当中间人的角色，对于连接到它的客户端来说，它是服务端；对于要连接的服务端来说，它是客户端。它就负责在两端之间来回传送 HTTP 报文。

```javascript
const http = require('http');
const net = require('net');
const url = require('url');

function request(cReq, cRes) {
    const u = url.parse(cReq.url);

    const options = {
        hostname : u.hostname,
        port     : u.port || 80,
        path     : u.path,
        method     : cReq.method,
        headers     : cReq.headers
    };
    // 解析options，新建到服务端的请求
    const pReq = http.request(options, function(pRes) {
        cRes.writeHead(pRes.statusCode, pRes.headers);
        pRes.pipe(cRes);
    }).on('error', function(e) {
        cRes.end();
    });
    // 把代理收到的请求转发给新建的请求
    cReq.pipe(pReq);
}

http.createServer().on('request', request).listen(8888, '0.0.0.0');
```

以上代码运行后，会在本地 8888 端口开启 HTTP 代理服务，这个服务从请求报文中解析出请求 URL 和其他必要参数，新建到服务端的请求，并把代理收到的请求转发给新建的请求，最后再把服务端响应返回给浏览器。修改浏览器的 HTTP 代理为 127.0.0.1:8888 后再访问 HTTP 网站，代理可以正常工作。

这个代理提供的是 HTTP 服务，没办法承载 HTTPS 服务 ，HTTPS 代理需要使用隧道代理实现

## 隧道代理

HTTP 客户端通过 CONNECT 方法请求隧道代理创建一条到达任意目的服务器和端口的 TCP 连接，并对客户端和服务器之间的后继数据进行盲转发。

```javascript
const http = require('http');
const net = require('net');
const url = require('url');

function connect(cReq, cSock) {
    const u = url.parse('http://' + cReq.url);

    const pSock = net.connect(u.port, u.hostname, function() {
        cSock.write('HTTP/1.1 200 Connection Established\r\n\r\n');
        pSock.pipe(cSock);
    }).on('error', function(e) {
        cSock.end();
    });

    cSock.pipe(pSock);
}

http.createServer().on('connect', connect).listen(8888, '0.0.0.0');
```

隧道代理主要用于 `https` ，因此我们将上述两段代码合二为一,同时处理 `http` 与 `https` 请求

```javascript
var http = require('http');
var net = require('net');
var url = require('url');

function request(cReq, cRes) {
    var u = url.parse(cReq.url);

    var options = {
        hostname : u.hostname,
        port     : u.port || 80,
        path     : u.path,
        method     : cReq.method,
        headers     : cReq.headers
    };

    var pReq = http.request(options, function(pRes) {
        cRes.writeHead(pRes.statusCode, pRes.headers);
        pRes.pipe(cRes);
    }).on('error', function(e) {
        cRes.end();
    });

    cReq.pipe(pReq);
}

function connect(cReq, cSock) {
    var u = url.parse('http://' + cReq.url);

    var pSock = net.connect(u.port, u.hostname, function() {
        cSock.write('HTTP/1.1 200 Connection Established\r\n\r\n');
        pSock.pipe(cSock);
    }).on('error', function(e) {
        cSock.end();
    });

    cSock.pipe(pSock);
}

http.createServer()
    .on('request', request)
    .on('connect', connect)
    .listen(8888, '0.0.0.0');
```

## 参考资料

[HTTP 代理原理及实现](https://imququ.com/post/web-proxy.html)

