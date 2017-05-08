---
title: node基础教程之http模块
date: 2017-05-08 11:22:30
tags: nodejs
---

## 第一个http服务器

要开发HTTP服务器程序，从头处理TCP连接，解析HTTP是不现实的。这些工作实际上已经由Node.js自带的http模块完成了。应用程序并不直接和HTTP协议打交道，而是操作http模块提供的request和response对象。

request对象封装了HTTP请求，我们调用request对象的属性和方法就可以拿到所有HTTP请求的信息；

response对象封装了HTTP响应，我们操作response对象的方法，就可以把HTTP响应返回给浏览器。

用Node.js实现一个HTTP服务器程序非常简单。我们来实现一个最简单的Web程序hello.js，它对于所有请求，都返回Hello world!：

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    // 回调函数接收request和response对象,
    // 获得HTTP请求的method和url:
    console.log(req.method + ': ' + req.url);
    // 将HTTP响应200写入response, 同时设置Content-Type: text/html:
    res.writeHead(200, {'Content-Type': 'text/html'});
    // 将HTTP响应的正文写入response:
    res.end('<h1>Hello world!</h1>');
});
//错误处理
server.on('clientError', (err, socket) => {
  socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
});
// 让服务器监听8080端口:
server.listen(8080);
console.log('Server is running at http://127.0.0.1:8080/');
```

在命令提示符下运行该程序，可以看到以下输出：

```bash
$ node hello.js
Server is running at http://127.0.0.1:8080/
```

不要关闭命令提示符，直接打开浏览器输入http://localhost:8080，即可在浏览器看到服务器响应的内容Hello world：

同时，在命令提示符窗口，可以看到程序打印的请求信息：

```bash
GET: /
GET: /favicon.ico
```

这就是我们编写的第一个HTTP服务器程序！

## 文件服务器

我们需要使用 nodejs 提供的 url 模块对 req.url 进行解析，使用 fs 模块对文件进行处理

### 解析url

```javascript
var url = require('url');
console.log(url.parse('http://user:pass@host.com:8080/path/to/file?query=string#hash'));
```

结果如下：

```javascript
Url {
  protocol: 'http:',
  slashes: true,
  auth: 'user:pass',
  host: 'host.com:8080',
  port: '8080',
  hostname: 'host.com',
  hash: '#hash',
  search: '?query=string',
  query: 'query=string',
  pathname: '/path/to/file',
  path: '/path/to/file?query=string',
  href: 'http://user:pass@host.com:8080/path/to/file?query=string#hash' }
```

### 构建文件服务器

文件结构如下

```
|-index.html
|-file-server.js
```

index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
  <h1>hello world!</h1>
</body>
</html>
```

file-server.js

```javascript
const
    fs = require('fs'),
    url = require('url'),
    path = require('path'),
    http = require('http');

const server = http.createServer((req, res) => {
    //通过req.url得到本地对应的文件路径
    const pathname = url.parse(req.url).pathname;
    const filepath = path.join(__dirname, pathname);

    fs.stat(filepath, (err, stats) => {
        if (!err && stats.isFile()) {
          //如果文件存在并且未出现错误，读取文件并传给res
            console.log('200 ' + req.url);
            res.writeHead(200);
            fs.createReadStream(filepath).pipe(res);
        } else {
          //否则返回404错误
            console.log('404 ' + req.url);
            res.writeHead(404);
            res.end('404 Not Found');
        }
    });
});

server.listen(8080);

console.log('Server is running at http://127.0.0.1:8080/');
```

当我们使用浏览器访问 http://127.0.0.1:8080/index.html 时，可以看到 hello world！ 字样，访问其他路径时，会得到 404 not found 的提示

## 参考资料
