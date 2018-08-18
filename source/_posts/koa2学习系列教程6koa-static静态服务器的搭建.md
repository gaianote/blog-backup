---
title: koa2学习系列教程6 koa-static静态服务器的搭建
date: 2017-04-28 13:44:34
tags: koa
---

我们可以使用 koa-static 快速搭建静态服务器，用于访问 koa 服务器内的js，css，img等静态文件。

## hello koa-static

首先安装 koa-static

```bash
npm install koa-static --save
```

然后定义 static 服务器文件夹所在目录，这里定义为 `./static` , `static` 文件夹根目录对应网站根目录，里面的内容可以通过 url 直接访问

```javascript
const serve = require('koa-static');
app.use(serve(__dirname + '/static'));
```

## 文件结构

```
hello-koa-static
|-views
| |-index.html
|-static
| |-img
|   |-koa.png
app.js
```

index.html

```html
<!DOCTYPE html>
<html>
<head>
  <title>{{title}}</title>
</head>
<body>
  <div style="text-align: center;">
    <img src="img/koa.png">
  </div>
</body>
</html>
```

app.js

```javascript
const Koa = require('koa');
const app = new Koa();

const nunjucks = require('nunjucks');
nunjucks.configure('views', { autoescape: true });

const serve = require('koa-static');
app.use(serve(__dirname + '/static'));

app.use(async (ctx,next)=>{
  if (ctx.path === '/') {
    ctx.body = nunjucks.render('index.html', { title: 'hello koa-static' })
  } else {
    await next;
  }
})

app.listen(3000);
```

打开 192.168.1.101:3000 可以看到 koa 的 logo 图片 ，同样，我们也可以直接访问 192.168.1.101:3000/img/koa.png 查看此图片。