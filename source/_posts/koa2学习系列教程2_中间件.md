---
title: koa2学习系列教程2 中间件
date: 2017-04-24 15:09:55
tags:
- nodejs
- koa
---

## koa应用

```javascript
var koa = require('koa');
var app = new koa();

app.use(function *(){
  this.body = 'Hello World';
});

app.listen(3000);
```

* 一个Koa应用就是一个对象，包含了一个middleware数组，这个数组由一组Generator函数组成。
* 这些Generator函数负责对HTTP请求进行各种加工，比如生成缓存、指定代理、请求重定向等等。
* 变量app就是一个Koa应用。它监听3000端口，返回一个内容为Hello World的网页
* app.use方法用于向middleware数组添加Generator函数。
* listen方法指定监听端口，并启动当前应用。

## 中间件

```javascript
app.use(function* (next){
  var start = new Date; // （1）
  yield next;  // （2）
  var ms = new Date - start; // （3）
  console.log('%s %s - %s', this.method, this.url, ms); // （4）
});
```

app.use方法的参数就是中间件，它是一个Generator函数

Generator函数内部使用yield命令，将程序的执行权转交给下一个中间件，即yield next，要等到下一个中间件返回结果，才会继续往下执行。

上面四行代码运行顺序为：

1.第一行赋值语句首先执行，开始计时
2.第二行yield语句将执行权交给下一个中间件，当前中间件就暂停执行。等到后面的中间件全部执行完成，执行权就回到原来暂停的地方，继续往下执行
3.得到程序运行所花费的时间。
4.第四行将这个时间打印出来。

```javascript
app.use(function *() {
  this.body = "header\n";
  yield saveResults.call(this);
  this.body += "footer\n";
});

function *saveResults() {
  this.body += "Results Saved!\n";
}
```

