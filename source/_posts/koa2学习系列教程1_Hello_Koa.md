---
title: koa2学习系列教程1 Hello Koa
date: 2017-04-24 15:09:55
tags:
- nodejs
- koa
---

## 安装

koa依赖于node v7.6.0或者更高的node版本，如果版本未达到要求，请升级

```bash
$ npm install koa
```

## Hello koa

```javascript
const Koa = require('koa');
const app = new Koa();

// response
app.use(ctx => {
  ctx.body = 'Hello Koa';
});

app.listen(3000);
```
* `ctx.body` = 'Hello World'这行代码表示设置response.body的值为'Hello World,
* 一个Koa应用就是一个对象，包含了一个middleware数组，这个数组由一组同步或异步函数组成。
* 这些函数负责对HTTP请求进行各种加工，比如生成缓存、指定代理、请求重定向等等。
* 变量app就是一个Koa应用。它监听3000端口，返回一个内容为Hello Koa的网页
* app.use方法用于向middleware数组添加相应函数。
* listen方法指定监听端口，并启动当前应用。

## 中间件 (async需要node v7.6+)

koa是一个可以使用两种函数作为中间件的中间件框架

* async function
* common function

```javascript
app.use(async (ctx, next) => {
  const start = new Date();
  await next();
  const ms = new Date() - start;
  console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});
```

app.use方法的参数就是中间件，它是一个async函数

async函数是Generator函数的语法糖，当程序遇到await时，将程序的执行权转交给下一个中间件，即await next()，要等到下一个中间件返回结果，才会继续往下执行。

上面四行代码运行顺序为：

1.第一行赋值语句首先执行，开始计时
2.第二行await语句将执行权交给下一个中间件，当前中间件就暂停执行。等到后面的中间件全部执行完成，执行权就回到原来暂停的地方，继续往下执行
3.得到程序运行所花费的时间。
4.第四行将这个时间打印出来。


[koa 中文文档](https://github.com/guo-yu/koa-guide)
[koa实战](http://book.apebook.org/minghe/koa-action/xtemplate/xtemplate.html)