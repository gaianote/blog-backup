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

## 异步编程终极解决方案 async

async是js异步执行的最佳方案，await无法单独出现，总是需要与async配合使用;

async 函数返回一个 Promise 对象，可以使用 then 方法添加回调函数。当函数执行的时候，一旦遇到 await 就会先返回，等到触发的异步操作完成，再接着执行函数体内后面的语句。

```javascript
async function foo ()=>{
  console.log('foo start')
  await sub()
  console.log('foo end')
}
async function sub ()=>{
  console.log('sub')
}
```

`async`表示这个函数是异步的

`await sub()` 表示等待 `sub()` 执行完毕,并返回结果后，继续向下执行

输出结果如下：

```
foo start
sub
foo end
```

## 中间件 (async需要node v7.6+)

koa是一个可以使用两种函数作为中间件的中间件框架

* async function
* common function

```javascript
//异步的
app.use(async (ctx, next) => {
  console.log('first middleware start')
  await next();
  await sub();
  console.log('first middleware end')
});
//同步的
app.use(()=>{
  console.log('second middleware')
})

const sub = ()=>{
  console.log('sub')
}
```

输出结果如下：

```
first middleware start
second middleware
sub
first middleware end
```

app.use的参数就是中间件，可以看出，通过`await next()`可以调用下一个中间件，通过`await func()`可以调用其他函数


## 参考文档

[koa 中文文档](https://github.com/guo-yu/koa-guide)
[koa实战](http://book.apebook.org/minghe/koa-action/xtemplate/xtemplate.html)