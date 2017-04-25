---
title: koa2学习系列教程4 context应用上下文
date: 2017-04-25 14:46:55
tags:
- nodejs
- koa
---


## context对象的全局属性

- request：指向Request对象
- response：指向Response对象
- req：指向Node的request对象
- res：指向Node的response对象
- app：指向App对象
- state：用于在中间件传递信息。

### state 对象

```javascript
cyx.state.user = await User.find(id);
```

上面代码中，user属性存放在this.state对象上面，可以被另一个中间件读取。

### Request与Response 对象

我们可以使用`ctx.request`，`ctx.response`获取请求头与响应头

```javascript
app.use( async(ctx) => {
  ctx.request; // is a koa Request
  ctx.response; // is a koa Response
});
```

尝试输出以上信息，输出结果如下

```
# ctx.request
{ method: 'GET',
  url: '/',
  header:
   { host: '127.0.0.1:3000',
     connection: 'keep-alive',
     'upgrade-insecure-requests': '1',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
     accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'accept-encoding': 'gzip, deflate, sdch, br',
     'accept-language': 'zh-CN,zh;q=0.8' } }
# ctx.response
{ status: 200,
  message: 'OK',
  header:
   { 'content-type': 'text/plain; charset=utf-8',
     'content-length': '9' },
  body: 'Hello Koa' }
```

Koa 的上下文封装了 request 与 response 对象至一个对象中，并提供了一些帮助开发者编写业务逻辑的方法。

**Request 对象**

- ctx.header
- ctx.method
- ctx.method=
- ctx.url
- ctx.url=
- ctx.path
- ctx.path=
- ctx.query
- ctx.query=
- ctx.querystring
- ctx.querystring=
- ctx.length
- ctx.host
- ctx.fresh
- ctx.stale
- ctx.socket
- ctx.protocol
- ctx.secure
- ctx.ip
- ctx.ips
- ctx.subdomains
- ctx.is()
- ctx.accepts()
- ctx.acceptsEncodings()
- ctx.acceptsCharsets()
- ctx.acceptsLanguages()
- ctx.get()

**Response 对象**

- ctx.body
- ctx.body=
- ctx.status
- ctx.status=
- ctx.length=
- ctx.type
- ctx.type=
- ctx.headerSent
- ctx.redirect()
- ctx.attachment()
- ctx.set()
- ctx.remove()
- ctx.lastModified=
- ctx.etag=

## context对象的全局方法

- throw()：抛出错误，直接决定了HTTP回应的状态码。
- assert()：如果一个表达式为false，则抛出一个错误。

### ctx.throw()

`ctx.throw(msg, [status])` 抛出常规错误的辅助方法，默认 status 为 500。

以下几种写法都有效：

```javascript
ctx.throw(403)
ctx.throw('name required', 400)
ctx.throw(400, 'name required')
ctx.throw('something exploded')
```

实际上，`ctx.throw('name required', 400)` 是此代码片段的简写方法：

```javascript
var err = new Error('name required');
err.status = 400;
throw err;
```

需要注意的是，ctx.throw 创建的错误，均为用户级别错误（标记为err.expose），会被返回到客户端。

### ctx.assert()

```javascript
// 格式
ctx.assert(value, [msg], [status], [properties])

// 例子
this.assert(this.user, 401, 'User not found. Please login!');
```
