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

## 发送请求

### get()

`get` 方法用于发送 `GET` 请求,使用格式如下（详细用法件request）

```javascript
http.get(options[, callback])
```

```javascript
function getTestPersonaLoginCredentials(callback) {
  return http.get({
    host: 'personatestuser.org',
    path: '/email'
  }, function(response) {
    var body = '';

    response.on('data', function(d) {
      body += d;
    });

    response.on('end', function() {
      var parsed = JSON.parse(body);
      callback({
        email: parsed.email,
        password: parsed.pass
      });
    });
  });
},
```

### request()

request方法用于发出HTTP请求，它的使用格式如下。

```javascript
http.request(options[, callback])
```

request方法的options参数，可以是一个对象，也可以是一个字符串。如果是字符串，就表示这是一个URL，Node内部就会自动调用url.parse()，处理这个参数。

options对象可以设置如下属性:

- `host`：HTTP请求所发往的域名或者IP地址，默认是localhost。
- `hostname`：该属性会被url.parse()解析，优先级高于host。
- `port`：远程服务器的端口，默认是80。
- `localAddress`：本地网络接口。
- `socketPath`：Unix网络套接字，格式为host:port或者socketPath。
- `method`：指定HTTP请求的方法，格式为字符串，默认为GET。
- `path`：指定HTTP请求的路径，默认为根路径（/）。可以在这个属性里面，指定查询字符串，比如/index.html?page=12。如果这个属性里面包含非法字符（比如空格），就会抛出一个错误。
- `headers`：一个对象，包含了HTTP请求的头信息。
- `auth`：一个代表HTTP基本认证的字符串user:password。
- `agent`：控制缓存行为，如果HTTP请求使用了agent，则HTTP请求默认为Connection: keep-alive，它的可能值如下：
- `undefined`（默认）：对当前host和port，使用全局Agent。
- `Agent`：一个对象，会传入agent属性。
- `false`：不缓存连接，默认HTTP请求为Connection: close。
- `keepAlive`：一个布尔值，表示是否保留socket供未来其他请求使用，默认等于false。
- `keepAliveMsecs`：一个整数，当使用KeepAlive的时候，设置多久发送一个TCP KeepAlive包，使得连接不要被关闭。默认等于1000，只有keepAlive设为true的时候，该设置才有意义。

